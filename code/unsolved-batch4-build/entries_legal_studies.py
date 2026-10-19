#!/usr/bin/env python3
"""Entries for the Unsolved Legal Studies databases (batch 4).

34 famous open problems in legal studies, ladder-ordered by accessibility.
ID prefixes: JAH-USLS- (public) and JAH-USLSS- (signature), verified free
in the manifest id_prefix values (exact + substring, 2026-10-18) and across
all shard index files in jah-databases-data-1.

No website references. No Facebook. No religious framing. Nothing
hate-adjacent, profane, or inappropriate.
"""

ENTRIES = [
    dict(
        key="legal-studies-01",
        name="Can Deterrence Be Measured",
        group="Theory",
        ladder_rank=1,
        ladder_tier="foundations",
        problem=("Does punishment deter crime - and can the deterrent effect "
                 "ever be separated from incapacitation and other causes?"),
        background=("Becker's economic model predicts deterrence from "
                    "certainty and severity; empirical work finds certainty "
                    "matters more than severity, but isolating deterrence "
                    "from incapacitation (criminals jailed cannot reoffend) "
                    "is notoriously hard. The death-penalty deterrence "
                    "literature collapsed under methodological criticism. "
                    "Whether punishment deters at all remains contested."),
        why_it_matters=("Deterrence justifies much punishment. If it cannot "
                        "be measured, a pillar of criminal justice rests on "
                        "faith."),
        sig_lens=("The Signature lens treats deterrence as a perception "
                  "ledger: the Signature approach asks what potential "
                  "offenders actually perceive."),
        sig_body=("The Signature proposal models deterrence as perceived "
                  "certainty, not actual severity. Assumptions: (1) "
                  "offenders discount the future heavily; (2) they "
                  "overweight vivid risks and underweight abstract ones; "
                  "(3) certainty is perceived through local experience. "
                  "Reasoning path: the proposal predicts deterrence "
                  "should track perceived apprehension risk - explaining "
                  "why severity hikes fail (undiscounted futures do not "
                  "deter) while focused policing works. Measurement then "
                  "needs perception data, not statute books. Limits: the "
                  "model needs better perception measures; incapacitation "
                  "confounds remain."),
        pointer=('The Signature system models deterrence as perceived certainty, predicting severity hikes fail while focused policing works. The Signature test: deterrence tracks perceived-certainty measures. It would be refuted if severity hikes deter where certainty is held constant.'),
        key_points=[
            "Certainty of punishment matters more than severity.",
            "Isolating deterrence from incapacitation is notoriously hard.",
            "Death-penalty deterrence studies collapsed methodologically.",
            "Offenders discount futures and misperceive risks.",
        ],
        requirements=[
            "Perception data on apprehension risk.",
            "Separation of deterrence from incapacitation.",
            "An account of the death-penalty literature's failure.",
        ],
        standards=[
            "Claims checked against the deterrence literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Becker GS. Crime and punishment: an economic approach. Journal of Political Economy; 1968.",
            "Nagin DS. Deterrence in the twenty-first century. 2013.",
        ],
        hypotheses=[
            "Perceived certainty is the operative variable.",
            "Deterrence effects are negligible overall.",
            "Severity deters specific calculative crimes.",
            "The concept is unmeasurable in principle.",
        ],
        confirm="Deterrence tracks perceived-certainty measures.",
        refute="Severity hikes deter where certainty is held constant.",
    ),
    dict(
        key="legal-studies-02",
        name="Why Do Legal Transplants Fail",
        group="Comparative",
        ladder_rank=2,
        ladder_tier="foundations",
        problem=("Why do laws transplanted from one country so often fail "
                 "in another - and when do they succeed?"),
        background=("Watson argued legal transplants are easy and common; "
                    "Legrand replied they are impossible - law is culture. "
                    "The record is mixed: Japanese commercial law adapted "
                    "Western codes successfully; many developing-world "
                    "transplants became dead letter. What makes a transplant "
                    "take remains the open question."),
        why_it_matters=("Legal reform worldwide runs on transplants. Their "
                        "success conditions determine whether rule-of-law "
                        "aid works."),
        sig_lens=("The Signature lens treats transplants as an ecology "
                  "ledger: the Signature approach asks what soil the new "
                  "law needs."),
        sig_body=("The Signature proposal models transplant success as "
                  "institutional-ecology matching. Assumptions: (1) laws "
                  "need complementary institutions (courts, professions, "
                  "norms); (2) transplants arrive without their ecology; "
                  "(3) local actors adapt or ignore them. Reasoning path: "
                  "the proposal predicts success where the receiving "
                  "ecology already resembles the source's - explaining "
                  "Japan's commercial-code success and many failed "
                  "criminal-justice transplants. Reform then means "
                  "building ecology, not importing text. Limits: the "
                  "model needs ecology measures; successful mutations "
                  "need study."),
        pointer=('The Signature system models transplant success as institutional-ecology matching, with reform building ecology rather than importing text. The Signature test: success tracks ecology-similarity measures. It would be refuted if transplants succeed in alien ecologies regularly.'),
        key_points=[
            "Watson: transplants are easy; Legrand: impossible.",
            "Japan adapted Western commercial law successfully.",
            "Many developing-world transplants became dead letter.",
            "Complementary institutions are the leading success factor.",
        ],
        requirements=[
            "Institutional-ecology measures.",
            "An account of successful adaptations.",
            "Separation of text from context effects.",
        ],
        standards=[
            "Claims checked against the comparative-law literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Watson A. Legal Transplants. Scottish Academic Press; 1974.",
            "Legrand P. The impossibility of legal transplants. 1997.",
        ],
        hypotheses=[
            "Ecology matching determines transplant fate.",
            "Transplants always mutate; purity is impossible.",
            "Elite commitment is the decisive variable.",
            "Transplants fail more than the literature admits.",
        ],
        confirm="Success tracks ecology-similarity measures.",
        refute="Transplants succeed in alien ecologies regularly.",
    ),
    dict(
        key="legal-studies-03",
        name="What Is Law: Hart Versus Dworkin",
        group="Theory",
        ladder_rank=3,
        ladder_tier="foundations",
        problem=("Is law a system of rules (Hart) or an interpretive "
                 "practice aiming at integrity (Dworkin) - and can the "
                 "debate be settled?"),
        background=("Hart's Concept of Law grounded law in social rules; "
                    "Dworkin replied that hard cases show judges appealing "
                    "to principles beyond rules. The debate defined "
                    "jurisprudence for fifty years without resolution. "
                    "Whether it is a substantive disagreement or a "
                    "methodological one remains disputed."),
        why_it_matters=("The nature of law determines what judges do - and "
                        "whether their power is legitimate."),
        sig_lens=("The Signature lens treats the debate as a practice "
                  "ledger: the Signature approach asks what judges "
                  "actually do in hard cases."),
        sig_body=("The Signature proposal models the debate as "
                  "describing different moments of legal practice. "
                  "Assumptions: (1) easy cases run on rules; (2) hard "
                  "cases require principles; (3) both describe real "
                  "judicial behavior. Reasoning path: the proposal shows "
                  "Hart captures the routine and Dworkin the exceptional "
                  "- predicting that rule-talk dominates trial courts "
                  "while principle-talk dominates appellate hard cases. "
                  "The debate then dissolves into a division of labor. "
                  "Limits: the model needs systematic opinion analysis; "
                  "the philosophical stakes may exceed the empirical "
                  "resolution."),
        pointer=('The Signature system dissolves the debate into a division of labor: rules for routine cases, principles for hard ones. The Signature test: opinion language tracks case difficulty as predicted. It would be refuted if judges use one mode uniformly.'),
        key_points=[
            "Hart grounded law in social rules; Dworkin in interpretive integrity.",
            "The debate defined jurisprudence for fifty years.",
            "Hard cases are the central battleground.",
            "Whether the dispute is substantive or methodological is open.",
        ],
        requirements=[
            "Systematic analysis of judicial reasoning in hard cases.",
            "An account of routine versus exceptional adjudication.",
            "Separation of descriptive from normative claims.",
        ],
        standards=[
            "Claims checked against the jurisprudence literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Hart HLA. The Concept of Law. Oxford University Press; 1961.",
            "Dworkin R. Law's Empire. Harvard University Press; 1986.",
        ],
        hypotheses=[
            "Division of labor dissolves the debate.",
            "Hart's positivism is correct.",
            "Dworkin's interpretivism is correct.",
            "The debate is irresolvable methodologically.",
        ],
        confirm="Opinion language tracks case difficulty as predicted.",
        refute="Judges use one mode uniformly.",
    ),
    dict(
        key="legal-studies-04",
        name="Originalism Versus Living Constitution: The Empirical Stakes",
        group="Courts",
        ladder_rank=4,
        ladder_tier="foundations",
        problem=("Does originalism actually constrain judges more than "
                 "living constitutionalism - the central empirical claim "
                 "in the debate?"),
        background=("Originalists claim fidelity to original meaning "
                    "constrains discretion; critics reply originalism is "
                    "indeterminate in practice and constrains no one. "
                    "Empirical work on whether originalist judges vote "
                    "differently is mixed. The debate is usually "
                    "philosophical, but its key premise is empirical."),
        why_it_matters=("The premise justifies a theory now dominant on the "
                        "US Supreme Court. Its truth matters for "
                        "legitimacy."),
        sig_lens=("The Signature lens treats the claim as a constraint "
                  "ledger: the Signature approach asks whether "
                  "originalist decisions are more predictable."),
        sig_body=("The Signature proposal models constraint as "
                  "predictability. Assumptions: (1) a constraining theory "
                  "should make decisions predictable from text and "
                  "history; (2) indeterminacy allows motivated reasoning; "
                  "(3) both theories face hard cases. Reasoning path: the "
                  "proposal predicts that if originalism constrains, "
                  "originalist opinions should cite historical sources "
                  "more and reach less ideologically predictable results "
                  "- a testable claim. Early evidence is mixed, "
                  "suggesting the constraint is real but partial. Limits: "
                  "the model needs large-scale opinion coding; "
                  "selection effects (which cases reach the Court) "
                  "confound."),
        pointer=("The Signature system tests originalism's constraint claim through decision predictability from text and history. The Signature test: originalist decisions prove less ideologically predictable. It would be refuted if no predictability difference appears."),
        key_points=[
            "Originalism claims to constrain judicial discretion.",
            "Critics call it indeterminate in practice.",
            "Empirical work on voting differences is mixed.",
            "The key premise is empirical, not philosophical.",
        ],
        requirements=[
            "Large-scale opinion coding.",
            "Predictability measures by interpretive method.",
            "An account of selection effects.",
        ],
        standards=[
            "Claims checked against the constitutional-theory literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Scalia A. A Matter of Interpretation. Princeton University Press; 1997.",
            "Strauss DA. The Living Constitution. Oxford University Press; 2010.",
        ],
        hypotheses=[
            "Originalism constrains partially but really.",
            "It constrains no more than alternatives.",
            "Indeterminacy defeats the constraint claim.",
            "The debate is philosophical, not empirical.",
        ],
        confirm="Originalist decisions prove less ideologically predictable.",
        refute="No predictability difference appears.",
    ),
    dict(
        key="legal-studies-05",
        name="Can Juries Understand Complex Cases",
        group="Courts",
        ladder_rank=5,
        ladder_tier="foundations",
        problem=("Can lay juries competently decide complex cases - "
                 "antitrust, securities fraud, patent disputes - or is "
                 "the jury obsolete for them?"),
        background=("Critics argue modern litigation outstrips lay "
                    "comprehension; defenders cite jury competence studies "
                    "showing jurors generally follow evidence. Reforms "
                    "proposed: expert juries, better instructions, special "
                    "verdicts. Whether complexity systematically defeats "
                    "juries remains empirically open."),
        why_it_matters=("The jury is democracy's direct participation in "
                        "justice. Its competence limits determine its "
                        "future."),
        sig_lens=("The Signature lens treats jury competence as a "
                  "comprehension ledger: the Signature approach asks what "
                  "jurors retain versus what experts assume they need."),
        sig_body=("The Signature proposal models jury competence as "
                  "narrative-driven. Assumptions: (1) jurors reason "
                  "through stories, not doctrines; (2) well-told cases "
                  "are decidable; (3) incomprehension follows poor "
                  "presentation. Reasoning path: the proposal predicts "
                  "jury performance should track case presentation "
                  "quality more than technical complexity - explaining "
                  "why juries handle complex facts when lawyers teach "
                  "well. The problem is then pedagogy, not capacity. "
                  "Limits: the model needs better comprehension "
                  "measures; some domains may exceed narrative "
                  "capacity."),
        pointer=('The Signature system models jury competence as narrative-driven, with performance tracking presentation quality over technical complexity. The Signature test: performance tracks presentation quality. It would be refuted if well-presented complex cases still defeat juries.'),
        key_points=[
            "Critics say modern cases outstrip lay comprehension.",
            "Competence studies show jurors generally follow evidence.",
            "Reforms proposed: expert juries, better instructions.",
            "Whether complexity systematically defeats juries is open.",
        ],
        requirements=[
            "Comprehension measures by case type.",
            "Separation of presentation from complexity effects.",
            "Reform evaluations.",
        ],
        standards=[
            "Claims checked against the jury literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Hans VP, Vidmar N. Judging the Jury. Plenum; 1986.",
            "Lempert RO. Civil juries and complex cases. 1981.",
        ],
        hypotheses=[
            "Narrative competence suffices with good presentation.",
            "Complexity systematically defeats juries.",
            "Expert juries are the answer.",
            "Instructions, not capacity, are the problem.",
        ],
        confirm="Performance tracks presentation quality.",
        refute="Well-presented complex cases still defeat juries.",
    ),
    dict(
        key="legal-studies-06",
        name="Does the Death Penalty Deter",
        group="Courts",
        ladder_rank=6,
        ladder_tier="foundations",
        problem=("Does capital punishment deter murder - and why did the "
                 "deterrence literature collapse?"),
        background=("Early econometric studies claimed each execution "
                    "saved lives; the National Research Council "
                    "concluded the research was fundamentally flawed. "
                    "The debate illustrates how hard causal inference is "
                    "when the treatment is rare and confounded. Whether "
                    "any credible deterrence evidence exists remains "
                    "open."),
        why_it_matters=("Deterrence is the main consequentialist defense of "
                        "execution. Its evidentiary status matters for "
                        "life and death."),
        sig_lens=("The Signature lens treats the literature as a methods "
                  "ledger: the Signature approach asks what went wrong "
                  "and whether repair is possible."),
        sig_body=("The Signature proposal models the literature's failure "
                  "as a small-N identification problem. Assumptions: (1) "
                  "executions are rare; (2) murder rates have many "
                  "causes; (3) models are fragile to specification. "
                  "Reasoning path: the proposal shows the conflicting "
                  "findings follow from model sensitivity - predicting "
                  "that no credible design can extract a signal from "
                  "such thin data. The honest conclusion is not 'no "
                  "deterrence' but 'unknowable with these methods.' "
                  "Limits: the model concedes the question may be "
                  "permanently unanswerable; natural experiments are "
                  "scarce."),
        pointer=('The Signature system argues the deterrence question is unanswerable with available methods - a small-N identification failure. The Signature test: no design extracts a stable signal. It would be refuted if a credible design finds a robust effect.'),
        key_points=[
            "Early studies claimed lives saved per execution.",
            "The National Research Council found the research fundamentally flawed.",
            "Executions are rare; murder has many causes.",
            "Model sensitivity drives the conflicting findings.",
        ],
        requirements=[
            "A credible identification strategy.",
            "An account of the literature's methodological failure.",
            "Separation of absence of evidence from evidence of absence.",
        ],
        standards=[
            "Claims checked against the deterrence literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "National Research Council. Deterrence and the Death Penalty. 2012.",
            "Donohue JJ, Wolfers J. Uses and abuses of empirical evidence in the death penalty debate. 2005.",
        ],
        hypotheses=[
            "The question is unanswerable with available methods.",
            "Better designs will find the effect.",
            "There is no deterrent effect.",
            "The effect exists but is small.",
        ],
        confirm="No design extracts a stable signal.",
        refute="A credible design finds a robust effect.",
    ),
    dict(
        key="legal-studies-07",
        name="The Access to Justice Gap",
        group="Rights",
        ladder_rank=7,
        ladder_tier="foundations",
        problem=("Why do most legal needs go unmet - and can the justice "
                 "gap be closed without massive funding increases?"),
        background=("Studies find most civil legal needs (housing, family, "
                    "debt) get no legal help; legal aid is chronically "
                    "underfunded. Proposed fixes: simplified procedures, "
                    "non-lawyer providers, technology, and upstream "
                    "prevention. Whether the gap reflects funding, "
                    "complexity, or design remains debated."),
        why_it_matters=("Equal justice under law is hollow if most cannot "
                        "access it. The gap is the rule of law's "
                        "credibility crisis."),
        sig_lens=("The Signature lens treats the gap as a design ledger: "
                  "the Signature approach asks whether the system is "
                  "built for lawyers or for people."),
        sig_body=("The Signature proposal models the gap as a "
                  "complexity tax. Assumptions: (1) legal procedures "
                  "assume represented parties; (2) most disputants are "
                  "unrepresented; (3) complexity deters and defeats "
                  "them. Reasoning path: the proposal predicts the gap "
                  "should be largest where procedures are most complex "
                  "relative to stakes - which matches the data - and "
                  "that simplification plus non-lawyer help closes more "
                  "gap per dollar than more lawyers. The system needs "
                  "redesign, not just funding. Limits: the model needs "
                  "better outcome measures; some matters genuinely "
                  "need lawyers."),
        pointer=('The Signature system models the gap as a complexity tax, with simplification closing more gap per dollar than funding. The Signature test: simplified procedures close the gap cost-effectively. It would be refuted if only lawyer-funding increases move outcomes.'),
        key_points=[
            "Most civil legal needs get no legal help.",
            "Legal aid is chronically underfunded.",
            "Simplification and non-lawyer providers are proposed fixes.",
            "Whether funding, complexity, or design is the cause is debated.",
        ],
        requirements=[
            "Outcome measures for unrepresented parties.",
            "Evaluations of simplification reforms.",
            "A design theory for people-centered justice.",
        ],
        standards=[
            "Claims checked against the access-to-justice literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Rhode DE. Access to Justice. Oxford University Press; 2004.",
            "Sandefur RL. Accessing justice in the contemporary USA. 2014.",
        ],
        hypotheses=[
            "Complexity, not funding, is the binding constraint.",
            "Massive funding is the only answer.",
            "Technology can close the gap.",
            "Non-lawyer providers are the key reform.",
        ],
        confirm="Simplified procedures close the gap cost-effectively.",
        refute="Only lawyer-funding increases move outcomes.",
    ),
    dict(
        key="legal-studies-08",
        name="Why Do People Obey the Law",
        group="Theory",
        ladder_rank=8,
        ladder_tier="foundations",
        problem=("Why do people obey the law - fear of punishment, moral "
                 "agreement, or perceived legitimacy?"),
        background=("Tyler's procedural-justice research found legitimacy "
                    "predicts compliance better than deterrence. But "
                    "legitimacy is hard to build and easy to destroy, and "
                    "the causal direction is debated (do the compliant "
                    "perceive legitimacy, or vice versa?). The relative "
                    "weights of fear, morality, and legitimacy remain "
                    "open."),
        why_it_matters=("Compliance is the foundation of legal order. Its "
                        "sources determine whether policing should "
                        "emphasize force or fairness."),
        sig_lens=("The Signature lens treats obedience as a legitimacy "
                  "ledger: the Signature approach asks what deposits "
                  "and withdrawals the authorities make."),
        sig_body=("The Signature proposal models compliance as a "
                  "legitimacy account. Assumptions: (1) fair procedures "
                  "deposit legitimacy; (2) unfair treatment withdraws "
                  "it; (3) deterrence works at the margin. Reasoning "
                  "path: the proposal predicts compliance should track "
                  "experienced procedural fairness - which the data "
                  "support - making legitimacy a renewable resource "
                  "that policing can build or burn. The policy "
                  "implication: fairness is not softness but strategy. "
                  "Limits: the model needs longitudinal legitimacy "
                  "measures; cultural variation is large."),
        pointer=('The Signature system models compliance as a legitimacy account that fair procedures build and unfair treatment burns. The Signature test: compliance tracks experienced procedural fairness. It would be refuted if deterrence changes swamp legitimacy effects.'),
        key_points=[
            "Legitimacy predicts compliance better than deterrence.",
            "Procedural justice is the leading mechanism.",
            "Causal direction is debated.",
            "Legitimacy is easy to destroy, hard to build.",
        ],
        requirements=[
            "Longitudinal legitimacy measures.",
            "Causal identification of the legitimacy effect.",
            "Cross-cultural testing.",
        ],
        standards=[
            "Claims checked against the compliance literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Tyler TR. Why People Obey the Law. Princeton University Press; 2006.",
            "Sunshine J, Tyler TR. The role of procedural justice. 2003.",
        ],
        hypotheses=[
            "Legitimacy is the primary compliance source.",
            "Deterrence dominates at the margin.",
            "Moral agreement does most of the work.",
            "The three are inseparable in practice.",
        ],
        confirm="Compliance tracks experienced procedural fairness.",
        refute="Deterrence changes swamp legitimacy effects.",
    ),
    dict(
        key="legal-studies-09",
        name="Common Law Versus Civil Law: Which Is Better",
        group="Comparative",
        ladder_rank=9,
        ladder_tier="foundations",
        problem=("Do common-law systems outperform civil-law systems "
                 "economically - the legal-origins thesis - or is the "
                 "claim overstated?"),
        background=("La Porta and colleagues linked common law to better "
                    "investor protection and growth. Critics replied the "
                    "measures were crude, the history selective, and the "
                    "causality reversed (rich countries chose their law). "
                    "The debate matters because the World Bank's Doing "
                    "Business rankings pushed reforms on its basis."),
        why_it_matters=("The thesis drove global legal reform. Its truth "
                        "determines whether those reforms helped or "
                        "harmed."),
        sig_lens=("The Signature lens treats the thesis as a measurement "
                  "ledger: the Signature approach asks what the indices "
                  "actually measured."),
        sig_body=("The Signature proposal models the legal-origins "
                  "finding as partially artifactual. Assumptions: (1) "
                  "the indices measured specific rules, not systems; (2) "
                  "colonial history confounds origins; (3) financial "
                  "development has many causes. Reasoning path: the "
                  "proposal shows the correlation weakens with better "
                  "measures and controls - predicting that specific "
                  "investor protections matter while 'common law' as a "
                  "brand does not. Reform should copy rules, not "
                  "systems. Limits: the model needs better historical "
                  "instruments; the finance-law link itself is "
                  "debated."),
        pointer=("The Signature system argues specific investor protections matter while the 'common law' brand does not. The Signature test: outcomes track specific rules, not origins. It would be refuted if origin predicts outcomes with full controls."),
        key_points=[
            "Legal-origins theory linked common law to growth.",
            "Critics cite crude measures and reversed causality.",
            "Doing Business rankings pushed reforms on this basis.",
            "The finance-law link itself is debated.",
        ],
        requirements=[
            "Better measures of legal rules.",
            "Historical instruments for legal origin.",
            "Separation of rules from systems.",
        ],
        standards=[
            "Claims checked against the legal-origins literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "La Porta R et al. Law and finance. Journal of Political Economy; 1998.",
            "Dam KW. The Law-Growth Nexus. Brookings; 2006.",
        ],
        hypotheses=[
            "Specific rules matter; system brands do not.",
            "Common law genuinely outperforms.",
            "The whole thesis is artifactual.",
            "Colonial history explains the correlation.",
        ],
        confirm="Outcomes track specific rules, not origins.",
        refute="Origin predicts outcomes with full controls.",
    ),
    dict(
        key="legal-studies-10",
        name="The Efficiency of Law: Does It Hold",
        group="Theory",
        ladder_rank=10,
        ladder_tier="foundations",
        problem=("Is the common law efficient - as Posner claimed - or is "
                 "efficiency a just-so story?"),
        background=("Posner argued common-law rules tend toward economic "
                    "efficiency through litigation selection. Critics "
                    "replied the mechanism is unproven, the efficiency "
                    "claims are post hoc, and distributional concerns are "
                    "ignored. Whether law has any efficiency tendency "
                    "remains law-and-economics' foundational question."),
        why_it_matters=("The claim justifies the economic analysis of law. "
                        "Its truth determines whether efficiency is law's "
                        "logic or economists' projection."),
        sig_lens=("The Signature lens treats the claim as a selection "
                  "ledger: the Signature approach asks whether litigation "
                  "actually selects for efficiency."),
        sig_body=("The Signature proposal models the efficiency tendency "
                  "as domain-limited. Assumptions: (1) inefficient rules "
                  "generate more litigation; (2) litigation gives courts "
                  "chances to revise; (3) judges need not intend "
                  "efficiency. Reasoning path: the proposal predicts "
                  "efficiency pressure should be strongest in "
                  "high-stakes, frequently litigated areas (commercial "
                  "law) and weakest elsewhere - which matches the "
                  "pattern of evidence. The invisible hand works where "
                  "litigation is the selection mechanism. Limits: the "
                  "model needs better inefficiency measures; "
                  "distributional effects are bracketed."),
        pointer=('The Signature system models efficiency pressure as domain-limited, strongest where litigation is frequent and stakes high. The Signature test: efficiency tracks litigation frequency by domain. It would be refuted if no efficiency pattern appears anywhere.'),
        key_points=[
            "Posner claimed common law tends toward efficiency.",
            "Litigation-selection is the proposed mechanism.",
            "Critics call the claims post hoc.",
            "Distributional concerns are standardly bracketed.",
        ],
        requirements=[
            "Inefficiency measures independent of the theory.",
            "Tests of the selection mechanism.",
            "Domain-specific predictions.",
        ],
        standards=[
            "Claims checked against the law-and-economics literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Posner RA. Economic Analysis of Law. Little Brown; 1973.",
            "Priest GL. The common law process and the selection of efficient rules. 1977.",
        ],
        hypotheses=[
            "Efficiency pressure is real but domain-limited.",
            "The common law is systematically efficient.",
            "The claims are post hoc rationalization.",
            "Distributional analysis defeats the efficiency frame.",
        ],
        confirm="Efficiency tracks litigation frequency by domain.",
        refute="No efficiency pattern appears anywhere.",
    ),
    dict(
        key="legal-studies-11",
        name="Rights: Where Do They Come From",
        group="Rights",
        ladder_rank=11,
        ladder_tier="foundations",
        problem=("Are rights natural, constructed, or invented - and does "
                 "their source affect their force?"),
        background=("Natural-rights theory grounds rights in human nature; "
                    "constructivists ground them in social agreement; "
                    "skeptics call them useful fictions. The debate is "
                    "usually philosophical, but it has practical stakes: "
                    "natural rights resist majoritarian override, "
                    "constructed rights invite it."),
        why_it_matters=("Rights are the trump cards of political morality. "
                        "Their source determines their strength."),
        sig_lens=("The Signature lens treats rights as a practice ledger: "
                  "the Signature approach asks what rights do in "
                  "political argument regardless of their metaphysics."),
        sig_body=("The Signature proposal models rights as "
                  "institutionalized trumps. Assumptions: (1) rights "
                  "function by blocking certain justifications; (2) "
                  "their force comes from institutional entrenchment; "
                  "(3) metaphysical grounding is secondary. Reasoning "
                  "path: the proposal predicts rights should be "
                  "strongest where institutionally entrenched (courts, "
                  "constitutions) regardless of philosophical fashion - "
                  "which matches the comparative record. The source "
                  "debate then matters less than the entrenchment. "
                  "Limits: the model brackets the philosophy; "
                  "entrenchment itself needs explaining."),
        pointer=('The Signature system models rights as institutionalized trumps whose force comes from entrenchment rather than metaphysics. The Signature test: enforcement tracks entrenchment, not philosophy. It would be refuted if metaphysical grounding predicts enforcement differences.'),
        key_points=[
            "Natural, constructed, and fictional accounts compete.",
            "The source affects resistance to majoritarian override.",
            "Institutional entrenchment predicts rights' strength.",
            "The debate is usually philosophical with practical stakes.",
        ],
        requirements=[
            "Comparative data on rights enforcement.",
            "Entrenchment measures.",
            "An account of rights' argumentative function.",
        ],
        standards=[
            "Claims checked against the rights literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Dworkin R. Taking Rights Seriously. Harvard University Press; 1977.",
            "Waldron J. Law and Disagreement. Oxford University Press; 1999.",
        ],
        hypotheses=[
            "Entrenchment, not metaphysics, determines rights' force.",
            "Natural rights are real and binding.",
            "Rights are useful fictions.",
            "The source debate is irresolvable.",
        ],
        confirm="Enforcement tracks entrenchment, not philosophy.",
        refute="Metaphysical grounding predicts enforcement differences.",
    ),
    dict(
        key="legal-studies-12",
        name="The Plea Bargain Problem",
        group="Courts",
        ladder_rank=12,
        ladder_tier="compounded",
        problem=("Is plea bargaining - resolving 95 percent of criminal "
                 "cases without trial - compatible with justice?"),
        background=("Plea bargaining dominates American criminal justice, "
                    "yet it is barely regulated: prosecutors set the "
                    "terms, the innocent may plead to avoid risk, and "
                    "sentencing differentials coerce. Defenders call it "
                    "necessary triage; critics call it an assembly line "
                    "that punishes the exercise of trial rights. Whether "
                    "it can be reformed without collapse is open."),
        why_it_matters=("Plea bargaining IS the criminal justice system in "
                        "practice. Its legitimacy is the system's "
                        "legitimacy."),
        sig_lens=("The Signature lens treats pleas as a risk ledger: the "
                  "Signature approach asks what the innocent do when the "
                  "trial penalty is ruinous."),
        sig_body=("The Signature proposal models plea bargaining as a "
                  "risk-pricing system. Assumptions: (1) trial penalties "
                  "(sentence differentials) price the trial right; (2) "
                  "risk-averse defendants accept overpriced pleas; (3) "
                  "prosecutors maximize convictions. Reasoning path: the "
                  "proposal predicts innocent pleas should concentrate "
                  "where differentials are largest - which the exoneration "
                  "data support - making the trial penalty the reform "
                  "target. Capping differentials preserves the system's "
                  "efficiency while protecting the innocent. Limits: the "
                  "model needs better innocent-plea measures; "
                  "prosecutorial incentives need reform too."),
        pointer=('The Signature system models plea bargaining as risk pricing, with the trial penalty as the reform target. The Signature test: innocent pleas track trial-penalty size. It would be refuted if innocent pleas are unrelated to differentials.'),
        key_points=[
            "About 95 percent of criminal cases end in pleas.",
            "Trial penalties coerce pleas, including from the innocent.",
            "Prosecutors dominate the process with little oversight.",
            "Reform without systemic collapse is the challenge.",
        ],
        requirements=[
            "Innocent-plea measures.",
            "Trial-penalty quantification.",
            "Reform models preserving function.",
        ],
        standards=[
            "Claims checked against the plea-bargaining literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Bibas S. Plea bargaining outside the shadow of trial. Harvard Law Review; 2004.",
            "Stuntz WJ. Plea bargaining and criminal law's disappearing shadow. 2004.",
        ],
        hypotheses=[
            "Trial-penalty caps can reform the system.",
            "Plea bargaining is irreformable.",
            "Prosecutorial regulation is the answer.",
            "The system works adequately as is.",
        ],
        confirm="Innocent pleas track trial-penalty size.",
        refute="Innocent pleas are unrelated to differentials.",
    ),
    dict(
        key="legal-studies-13",
        name="Eyewitness Testimony: How Reliable",
        group="Courts",
        ladder_rank=13,
        ladder_tier="compounded",
        problem=("How reliable is eyewitness identification - the leading "
                 "cause of wrongful convictions - and can procedures fix "
                 "it?"),
        background=("Eyewitness error contributed to most DNA exonerations. "
                    "Psychology shows memory is reconstructive: stress, "
                    "weapons focus, cross-race effects, and suggestive "
                    "procedures corrupt identifications. Reforms (blind "
                    "lineups, sequential presentation) help, but the "
                    "underlying malleability remains."),
        why_it_matters=("Eyewitness testimony convicts the innocent. Its "
                        "reliability determines how courts should weigh "
                        "it."),
        sig_lens=("The Signature lens treats eyewitness memory as a "
                  "contamination ledger: the Signature approach asks what "
                  "the procedure adds to the memory."),
        sig_body=("The Signature proposal models identification accuracy "
                  "as a procedure-contamination function. Assumptions: "
                  "(1) memory traces decay and distort; (2) procedures "
                  "can contaminate or preserve; (3) confidence is "
                  "malleable. Reasoning path: the proposal predicts "
                  "accuracy should track procedure quality - blind "
                  "administration, proper fillers, no feedback - which "
                  "the research confirms. Courts should then treat "
                  "identification as procedure-dependent evidence, with "
                  "admissibility conditioned on protocol. Limits: the "
                  "model needs better field data; some errors resist "
                  "procedural fixes."),
        pointer=('The Signature system models identification accuracy as procedure-dependent, with admissibility conditioned on protocol. The Signature test: accuracy tracks procedure-quality measures. It would be refuted if reformed procedures show no accuracy gain.'),
        key_points=[
            "Eyewitness error is the leading cause of wrongful convictions.",
            "Memory is reconstructive and malleable.",
            "Reforms (blind, sequential lineups) improve accuracy.",
            "Confidence is a poor guide to accuracy.",
        ],
        requirements=[
            "Procedure-quality measures in real cases.",
            "Field data on reformed procedures.",
            "Admissibility standards tied to protocol.",
        ],
        standards=[
            "Claims checked against the eyewitness literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Wells GL et al. Eyewitness identification procedures. Law and Human Behavior; 1998.",
            "Innocence Project. Eyewitness misidentification data. 2024.",
        ],
        hypotheses=[
            "Procedure quality determines reliability.",
            "Eyewitness evidence is irredeemably unreliable.",
            "Reforms solve the problem adequately.",
            "Expert testimony on memory is the answer.",
        ],
        confirm="Accuracy tracks procedure-quality measures.",
        refute="Reformed procedures show no accuracy gain.",
    ),
    dict(
        key="legal-studies-14",
        name="Forensic Science: How Scientific",
        group="Courts",
        ladder_rank=14,
        ladder_tier="compounded",
        problem=("How scientific is forensic science - and which disciplines "
                 "rest on validated foundations?"),
        background=("The 2009 National Academy report found most forensic "
                    "disciplines (bite marks, hair comparison, fingerprints) "
                    "lack validation; only DNA is firmly grounded. "
                    "Reforms followed slowly. The question is which "
                    "pattern-matching disciplines can be validated and "
                    "which should be excluded."),
        why_it_matters=("Forensic testimony convicts. Its scientific status "
                        "determines what courts should admit."),
        sig_lens=("The Signature lens treats forensics as a validation "
                  "ledger: the Signature approach asks what each "
                  "discipline has proven about its error rate."),
        sig_body=("The Signature proposal models forensic validity as "
                  "empirical, not credential-based. Assumptions: (1) "
                  "validity requires measured error rates; (2) "
                  "examiner expertise does not substitute for validation; "
                  "(3) adversarial pressure resists the findings. "
                  "Reasoning path: the proposal predicts disciplines "
                  "should be admitted proportionally to their validation "
                  "- DNA freely, fingerprints cautiously, bite marks not "
                  "at all - which is the reform direction. The "
                  "resistance is then institutional, not scientific. "
                  "Limits: the model needs ongoing validation research; "
                  "the transition costs are real."),
        pointer=('The Signature system argues forensic admissibility should track measured error rates, not examiner credentials. The Signature test: error rates predict real-world accuracy. It would be refuted if unvalidated disciplines prove accurate in testing.'),
        key_points=[
            "The 2009 NAS report found most forensics unvalidated.",
            "Only DNA is firmly scientifically grounded.",
            "Bite-mark and hair comparison have been discredited.",
            "Reform has been slow against institutional resistance.",
        ],
        requirements=[
            "Error-rate studies by discipline.",
            "Admissibility standards tied to validation.",
            "An account of institutional resistance.",
        ],
        standards=[
            "Claims checked against the forensic-science literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "National Research Council. Strengthening Forensic Science in the United States. 2009.",
            "PCAST. Forensic Science in Criminal Courts. 2016.",
        ],
        hypotheses=[
            "Validation-proportional admissibility is the answer.",
            "Most pattern forensics can be validated with effort.",
            "Most should be excluded.",
            "The system is reforming adequately.",
        ],
        confirm="Error rates predict real-world accuracy.",
        refute="Unvalidated disciplines prove accurate in testing.",
    ),
    dict(
        key="legal-studies-15",
        name="The Insanity Defense: Can It Work",
        group="Courts",
        ladder_rank=15,
        ladder_tier="compounded",
        problem=("Can the insanity defense fairly separate the mad from the "
                 "bad - and does it serve justice or excuse?"),
        background=("The M'Naghten rules and their successors try to draw "
                    "the line, but psychiatry and law speak different "
                    "languages. The defense succeeds rarely; public "
                    "backlash follows notorious acquittals. Whether any "
                    "formulation can work fairly remains open."),
        why_it_matters=("The defense marks the boundary of moral "
                        "responsibility - the deepest question criminal "
                        "law asks."),
        sig_lens=("The Signature lens treats the defense as a capacity "
                  "ledger: the Signature approach asks what capacities "
                  "responsibility requires."),
        sig_body=("The Signature proposal models responsibility as "
                  "capacity-graded. Assumptions: (1) responsibility "
                  "needs rational and control capacities; (2) mental "
                  "illness impairs them by degrees; (3) binary verdicts "
                  "fit poorly. Reasoning path: the proposal predicts "
                  "that graded outcomes (diminished responsibility, "
                  "treatment dispositions) should outperform binary "
                  "acquittal-or-prison - which comparative evidence "
                  "supports. The M'Naghten binary is then the problem. "
                  "Limits: the model needs better capacity measures; "
                  "public acceptance of graded outcomes is uncertain."),
        pointer=('The Signature system models responsibility as capacity-graded, favoring diminished-responsibility over binary verdicts. The Signature test: graded systems show better outcomes. It would be refuted if binary systems outperform graded ones.'),
        key_points=[
            "The insanity defense rarely succeeds.",
            "Psychiatry and law use incompatible languages.",
            "Notorious acquittals provoke backlash.",
            "Graded alternatives exist comparatively.",
        ],
        requirements=[
            "Capacity measures for responsibility.",
            "Comparative outcome data.",
            "Public-acceptability analysis.",
        ],
        standards=[
            "Claims checked against the criminal-law literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Morse SJ. Excusing the crazy. 1985.",
            "Slobogin C. An end to insanity. 2000.",
        ],
        hypotheses=[
            "Graded responsibility outperforms binary verdicts.",
            "The defense should be abolished.",
            "M'Naghten works adequately.",
            "Treatment dispositions are the answer.",
        ],
        confirm="Graded systems show better outcomes.",
        refute="Binary systems outperform graded ones.",
    ),
    dict(
        key="legal-studies-16",
        name="Corporate Personhood: The Limits",
        group="Rights",
        ladder_rank=16,
        ladder_tier="compounded",
        problem=("Which rights should corporations have - and where does "
                 "corporate personhood end?"),
        background=("Citizens United extended speech rights to "
                    "corporations; Hobby Lobby extended religious exercise. "
                    "Critics argue corporations are not moral persons; "
                    "defenders argue rights protect the humans behind "
                    "them. The boundary - which rights, which "
                    "corporations - remains unmapped."),
        why_it_matters=("Corporate rights shape elections, regulation, and "
                        "religion. The boundary determines corporate "
                        "power's limits."),
        sig_lens=("The Signature lens treats personhood as a function "
                  "ledger: the Signature approach asks which rights "
                  "serve the humans behind the corporation."),
        sig_body=("The Signature proposal models corporate rights as "
                  "derivative. Assumptions: (1) corporations are not moral "
                  "persons; (2) rights can protect associated humans; (3) "
                  "the derivative logic has limits. Reasoning path: the "
                  "proposal predicts speech rights (protecting human "
                  "expression through association) fit the derivative "
                  "logic while religious exercise strains it - explaining "
                  "the controversy pattern. The boundary is then "
                  "functional: rights that serve humans qualify; rights "
                  "that serve the entity do not. Limits: the model needs "
                  "better theories of the derivative logic; nonprofit "
                  "versus for-profit differences need mapping."),
        pointer=('The Signature system models corporate rights as derivative: they qualify where they serve associated humans, not the entity. The Signature test: rights track the derivative-function criterion. It would be refuted if no functional pattern explains the case law.'),
        key_points=[
            "Citizens United and Hobby Lobby extended corporate rights.",
            "Critics deny corporations are moral persons.",
            "Defenders invoke the humans behind them.",
            "The boundary remains unmapped.",
        ],
        requirements=[
            "A functional theory of derivative rights.",
            "Nonprofit versus for-profit distinctions.",
            "An account of the controversy pattern.",
        ],
        standards=[
            "Claims checked against the corporate-rights literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Winkler A. We the Corporations. Liveright; 2018.",
            "Pollman E. Reconceiving corporate personhood. 2011.",
        ],
        hypotheses=[
            "Derivative-function theory maps the boundary.",
            "Corporations should have no constitutional rights.",
            "Corporations should have full rights.",
            "The distinction is unworkable in practice.",
        ],
        confirm="Rights track the derivative-function criterion.",
        refute="No functional pattern explains the case law.",
    ),
    dict(
        key="legal-studies-17",
        name="Hate Speech Versus Free Speech: The Line",
        group="Rights",
        ladder_rank=17,
        ladder_tier="compounded",
        problem=("Where should the line between hate speech and free speech "
                 "be drawn - and can it be drawn consistently?"),
        background=("The US protects hate speech broadly; Europe restricts "
                    "it. Philosophers debate whether hate speech causes "
                    "harm (Waldron: dignity) or whether restriction causes "
                    "more harm (Dworkin: legitimacy). Platforms now draw "
                    "the line daily with inconsistent results. Whether a "
                    "principled line exists remains open."),
        why_it_matters=("The line determines the boundaries of public "
                        "discourse - and who gets silenced."),
        sig_lens=("The Signature lens treats the line as a harm ledger: "
                  "the Signature approach asks what speech does versus "
                  "what restriction does."),
        sig_body=("The Signature proposal models the line as a "
                  "comparative-harm balance. Assumptions: (1) hate speech "
                  "causes real dignitary harm; (2) restriction causes "
                  "legitimacy and abuse harms; (3) both are hard to "
                  "measure. Reasoning path: the proposal predicts the "
                  "optimal line should vary with institutional trust - "
                  "restrictions work where institutions are trusted to "
                  "apply them narrowly, backfiring where they are not - "
                  "explaining the US-Europe divergence. There is then no "
                  "universal line, only contextual optima. Limits: the "
                  "model needs better harm measures; platform contexts "
                  "need separate analysis."),
        pointer=('The Signature system models the optimal line as contextual, varying with institutional trust. The Signature test: outcomes track institutional-trust conditioning. It would be refuted if one line proves optimal across contexts.'),
        key_points=[
            "The US protects hate speech; Europe restricts it.",
            "Dignity-harm versus legitimacy-harm arguments compete.",
            "Platforms draw the line daily and inconsistently.",
            "Whether a principled universal line exists is open.",
        ],
        requirements=[
            "Harm measures for speech and restriction.",
            "Institutional-trust conditioning.",
            "Platform-specific analysis.",
        ],
        standards=[
            "Claims checked against the free-speech literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Waldron J. The Harm in Hate Speech. Harvard University Press; 2012.",
            "Dworkin R. Foreword to Extreme Speech and Democracy. 2009.",
        ],
        hypotheses=[
            "The optimal line is contextual, not universal.",
            "Broad protection is always correct.",
            "Restriction is always justified.",
            "Platforms need distinct rules from states.",
        ],
        confirm="Outcomes track institutional-trust conditioning.",
        refute="One line proves optimal across contexts.",
    ),
    dict(
        key="legal-studies-18",
        name="Privacy in the Digital Age",
        group="Rights",
        ladder_rank=18,
        ladder_tier="compounded",
        problem=("What should privacy mean when data is the economy's fuel - "
                 "and can law keep up with surveillance capitalism?"),
        background=("Warren and Brandeis invented the right to privacy in "
                    "1890; the digital age made data collection ambient. "
                    "The EU's GDPR and California's CCPA attempt control, "
                    "but enforcement lags and business models adapt. "
                    "Whether privacy is an individual right, a collective "
                    "good, or an obsolete concept remains debated."),
        why_it_matters=("Privacy shapes autonomy in the digital age. Its "
                        "legal form determines who controls the data "
                        "economy."),
        sig_lens=("The Signature lens treats privacy as a power ledger: "
                  "the Signature approach asks who gains from knowing."),
        sig_body=("The Signature proposal models privacy as a collective "
                  "action problem. Assumptions: (1) individual consent "
                  "cannot govern systemic collection; (2) data gains "
                  "power in aggregation; (3) the harms are diffuse. "
                  "Reasoning path: the proposal predicts consent-based "
                  "regimes should fail - which GDPR experience partly "
                  "confirms - and that effective protection needs "
                  "structural limits (data minimization, purpose "
                  "limitation) rather than individual choice. Privacy is "
                  "then environmental, not transactional. Limits: the "
                  "model needs better harm measures; innovation costs "
                  "need honest accounting."),
        pointer=('The Signature system models privacy as a collective-action problem needing structural limits rather than individual consent. The Signature test: structural regimes outperform consent regimes. It would be refuted if well-designed consent fully protects privacy.'),
        key_points=[
            "Data collection is ambient and continuous.",
            "GDPR and CCPA attempt control with mixed results.",
            "Consent-based models show strain.",
            "Privacy as right, good, or obsolete concept is debated.",
        ],
        requirements=[
            "Harm measures for data practices.",
            "Evaluation of structural versus consent approaches.",
            "Innovation-cost accounting.",
        ],
        standards=[
            "Claims checked against the privacy literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Warren S, Brandeis L. The right to privacy. Harvard Law Review; 1890.",
            "Solove DJ. Understanding Privacy. Harvard University Press; 2008.",
        ],
        hypotheses=[
            "Structural limits outperform consent models.",
            "Consent can be fixed with better design.",
            "Privacy is obsolete; adapt instead.",
            "Collective data governance is the answer.",
        ],
        confirm="Structural regimes outperform consent regimes.",
        refute="Well-designed consent fully protects privacy.",
    ),
    dict(
        key="legal-studies-19",
        name="Intellectual Property: The Optimal Length",
        group="Regulation",
        ladder_rank=19,
        ladder_tier="compounded",
        problem=("How long should intellectual property last - and does "
                 "the current system promote or hinder innovation?"),
        background=("Copyright now lasts life plus 70 years; patents 20. "
                    "Economists argue the optimal term balances incentives "
                    "against monopoly costs, but the current terms reflect "
                    "lobbying more than optimization. Evidence on whether "
                    "stronger IP promotes innovation is mixed - and "
                    "open-source successes challenge the premise."),
        why_it_matters=("IP law shapes innovation, culture, and access to "
                        "knowledge. Its calibration affects everyone."),
        sig_lens=("The Signature lens treats IP as an incentive ledger: "
                  "the Signature approach asks what term length the "
                  "incentive actually needs."),
        sig_body=("The Signature proposal models optimal IP as "
                  "innovation-specific. Assumptions: (1) incentives need "
                  "only cover creation costs plus risk; (2) monopoly "
                  "costs grow with term; (3) industries differ wildly. "
                  "Reasoning path: the proposal predicts optimal terms "
                  "should be far shorter than current ones - most "
                  "creation needs only years of protection - and should "
                  "vary by industry. The current uniformity then "
                  "reflects rent-seeking, not optimization. Limits: the "
                  "model needs better creation-cost data; international "
                  "coordination constrains reform."),
        pointer=('The Signature system models optimal IP terms as far shorter than current law, varying by industry. The Signature test: innovation tracks incentive-adequacy, not term length. It would be refuted if longer terms correlate with more innovation.'),
        key_points=[
            "Copyright: life plus 70; patents: 20 years.",
            "Terms reflect lobbying more than optimization.",
            "Evidence on IP and innovation is mixed.",
            "Open source challenges the incentive premise.",
        ],
        requirements=[
            "Creation-cost data by industry.",
            "Monopoly-cost measures.",
            "A reform path through international constraints.",
        ],
        standards=[
            "Claims checked against the IP literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Boldrin M, Levine DK. Against Intellectual Monopoly. Cambridge University Press; 2008.",
            "Landes WM, Posner RA. The Economic Structure of Intellectual Property Law. Harvard University Press; 2003.",
        ],
        hypotheses=[
            "Shorter, industry-varying terms are optimal.",
            "Current terms are approximately optimal.",
            "IP should be abolished.",
            "The system needs redesign, not just recalibration.",
        ],
        confirm="Innovation tracks incentive-adequacy, not term length.",
        refute="Longer terms correlate with more innovation.",
    ),
    dict(
        key="legal-studies-20",
        name="Antitrust: What Is Consumer Welfare",
        group="Regulation",
        ladder_rank=20,
        ladder_tier="compounded",
        problem=("Should antitrust protect consumer welfare narrowly "
                 "defined - or broader values like competition, labor, "
                 "and democracy?"),
        background=("The Bork revolution made consumer welfare (low "
                    "prices) the sole goal; neo-Brandeisians argue this "
                    "blessed monopolies that harm workers, suppliers, and "
                    "democracy. Digital platforms - free to consumers, "
                    "dominant in markets - broke the price test. Whether "
                    "antitrust needs new goals or better price theory is "
                    "the live fight."),
        why_it_matters=("Antitrust shapes the structure of the economy. "
                        "Its goal determines whether bigness itself is "
                        "the problem."),
        sig_lens=("The Signature lens treats antitrust as a power ledger: "
                  "the Signature approach asks what market power does "
                  "beyond prices."),
        sig_body=("The Signature proposal models antitrust goals as "
                  "multi-dimensional. Assumptions: (1) market power "
                  "affects workers, suppliers, and innovation, not just "
                  "prices; (2) the price test misses these; (3) broader "
                  "goals risk politicization. Reasoning path: the "
                  "proposal predicts the consumer-welfare standard "
                  "should fail exactly for zero-price platforms - which "
                  "it does - and that a competition-process standard "
                  "captures the harms without abandoning rigor. The "
                  "answer is then neither Bork nor Brandeis but a "
                  "process standard. Limits: the model needs better "
                  "non-price harm measures; politicization risks are "
                  "real."),
        pointer=('The Signature system proposes a competition-process standard capturing non-price harms without abandoning rigor. The Signature test: non-price harms track market power measures. It would be refuted if price effects capture all significant harms.'),
        key_points=[
            "Consumer welfare (low prices) has been the sole goal.",
            "Zero-price platforms broke the price test.",
            "Neo-Brandeisians urge broader goals.",
            "Politicization risks attend broader standards.",
        ],
        requirements=[
            "Non-price harm measures.",
            "A workable process standard.",
            "An account of politicization risks.",
        ],
        standards=[
            "Claims checked against the antitrust literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Bork RH. The Antitrust Paradox. Free Press; 1978.",
            "Khan LM. Amazon's antitrust paradox. Yale Law Journal; 2017.",
        ],
        hypotheses=[
            "A competition-process standard is the answer.",
            "Consumer welfare suffices with better price theory.",
            "Neo-Brandeisian goals are needed.",
            "Antitrust cannot handle platform power.",
        ],
        confirm="Non-price harms track market power measures.",
        refute="Price effects capture all significant harms.",
    ),
    dict(
        key="legal-studies-21",
        name="Environmental Law: Can It Work",
        group="Regulation",
        ladder_rank=21,
        ladder_tier="compounded",
        problem=("Can environmental law actually protect the environment - "
                 "or does it merely manage decline?"),
        background=("Decades of environmental law cleaned air and water "
                    "locally while the climate crisis worsened. Critics "
                    "argue the framework - permits, standards, litigation "
                    "- cannot handle global, cumulative problems. "
                    "Defenders cite real gains. Whether the toolkit fits "
                    "the crisis is the open question."),
        why_it_matters=("The climate crisis is the ultimate test of law's "
                        "capacity. The answer determines legal strategy."),
        sig_lens=("The Signature lens treats environmental law as a scale "
                  "ledger: the Signature approach asks which problems "
                  "fit the toolkit and which do not."),
        sig_body=("The Signature proposal models environmental law as "
                  "scale-mismatched. Assumptions: (1) the toolkit was "
                  "built for local point-source pollution; (2) climate "
                  "is global and cumulative; (3) litigation needs "
                  "identifiable harms. Reasoning path: the proposal "
                  "predicts success where problems match the toolkit "
                  "(local pollution) and failure where they do not "
                  "(climate) - which matches the record. The answer is "
                  "then new instruments (carbon pricing, global "
                  "treaties) rather than more of the same. Limits: the "
                  "model needs better instrument evaluations; "
                  "political feasibility constrains everything."),
        pointer=('The Signature system models environmental law as scale-mismatched, succeeding locally while needing new instruments for climate. The Signature test: outcomes track toolkit-problem matching. It would be refuted if traditional tools solve global problems.'),
        key_points=[
            "Local air and water improved; climate worsened.",
            "The toolkit was built for point-source pollution.",
            "Climate is global and cumulative.",
            "New instruments are proposed but politically hard.",
        ],
        requirements=[
            "Instrument evaluations by problem scale.",
            "A design theory for global problems.",
            "Political-feasibility analysis.",
        ],
        standards=[
            "Claims checked against the environmental-law literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Lazarus RJ. The Making of Environmental Law. University of Chicago Press; 2004.",
            "Stewart RB. Instrument choice. 2001.",
        ],
        hypotheses=[
            "Scale mismatch explains the pattern; new instruments are needed.",
            "More of the same toolkit will work.",
            "Law cannot solve climate; only technology can.",
            "Litigation will force the transition.",
        ],
        confirm="Outcomes track toolkit-problem matching.",
        refute="Traditional tools solve global problems.",
    ),
    dict(
        key="legal-studies-22",
        name="International Law: Is It Law",
        group="Comparative",
        ladder_rank=22,
        ladder_tier="compounded",
        problem=("Is international law really law - without a sovereign, "
                 "with selective compliance - or is it something else?"),
        background=("Austin denied it; modern scholars affirm it while "
                    "conceding the enforcement problem. Compliance is "
                    "puzzlingly high in some areas (trade, diplomacy) and "
                    "low in others (human rights, war). Whether "
                    "international law constrains the powerful or merely "
                    "coordinates the willing remains open."),
        why_it_matters=("The answer determines what international "
                        "institutions can achieve - and whether global "
                        "governance is possible."),
        sig_lens=("The Signature lens treats international law as a "
                  "compliance ledger: the Signature approach asks when "
                  "states obey without enforcement."),
        sig_body=("The Signature proposal models compliance as "
                  "interest-plus-reputation. Assumptions: (1) states "
                  "comply when it serves interests; (2) reputation "
                  "matters for repeat players; (3) power asymmetries "
                  "shape both. Reasoning path: the proposal predicts "
                  "high compliance where coordination benefits all "
                  "(trade, communications) and low compliance where "
                  "interests clash (war, human rights) - which matches "
                  "the pattern. International law is then real law for "
                  "coordination problems, aspirational for conflict "
                  "problems. Limits: the model needs better compliance "
                  "measures; the powerful-compliance question persists."),
        pointer=('The Signature system models international law as real for coordination problems, aspirational for conflict problems. The Signature test: compliance tracks coordination-versus-conflict structure. It would be refuted if compliance is uniform across domains.'),
        key_points=[
            "Enforcement is weak; compliance varies by domain.",
            "Trade and diplomacy show high compliance.",
            "Human rights and war show low compliance.",
            "Whether it constrains the powerful is the core question.",
        ],
        requirements=[
            "Compliance measures by domain.",
            "An account of the powerful-compliance puzzle.",
            "A theory of when law binds states.",
        ],
        standards=[
            "Claims checked against the international-law literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Henkin L. How Nations Behave. Columbia University Press; 1979.",
            "Goldsmith JL, Posner EA. The Limits of International Law. Oxford University Press; 2005.",
        ],
        hypotheses=[
            "Coordination-conflict split explains compliance.",
            "International law is not really law.",
            "Reputation explains most compliance.",
            "Power explains everything.",
        ],
        confirm="Compliance tracks coordination-versus-conflict structure.",
        refute="Compliance is uniform across domains.",
    ),
    dict(
        key="legal-studies-23",
        name="Transitional Justice: Does It Heal",
        group="Comparative",
        ladder_rank=23,
        ladder_tier="compounded",
        problem=("Do truth commissions, trials, and reparations heal "
                 "divided societies - or reopen wounds?"),
        background=("South Africa's TRC is the famous case; Rwanda's "
                    "gacaca, Latin American trials, and ICC prosecutions "
                    "offer varied models. Evidence on reconciliation "
                    "effects is mixed: some studies find healing, others "
                    "find renewed division. Whether justice helps peace "
                    "or threatens it remains contested."),
        why_it_matters=("Post-conflict societies must choose between "
                        "justice and peace - or find both. The evidence "
                        "should guide the choice."),
        sig_lens=("The Signature lens treats transitional justice as a "
                  "sequencing ledger: the Signature approach asks what "
                  "order of truth, justice, and peace works."),
        sig_body=("The Signature proposal models outcomes as "
                  "sequence-dependent. Assumptions: (1) truth-telling, "
                  "prosecution, and reparations have different effects; "
                  "(2) their order matters; (3) local ownership conditions "
                  "everything. Reasoning path: the proposal predicts "
                  "truth-first processes should reconcile better than "
                  "prosecution-first ones where divisions are deep - "
                  "matching the South Africa versus retributive cases. "
                  "The answer is then design, not doctrine. Limits: the "
                  "model needs better reconciliation measures; "
                  "counterfactuals are unavailable."),
        pointer=('The Signature system models transitional-justice outcomes as sequence-dependent, with truth-first processes reconciling better. The Signature test: outcomes track process sequencing. It would be refuted if sequencing shows no systematic effect.'),
        key_points=[
            "South Africa's TRC is the iconic case.",
            "Evidence on reconciliation effects is mixed.",
            "Peace-versus-justice is the core tension.",
            "Local ownership appears crucial.",
        ],
        requirements=[
            "Reconciliation measures over time.",
            "Sequence comparisons across cases.",
            "An account of local-ownership effects.",
        ],
        standards=[
            "Claims checked against the transitional-justice literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Teitel RG. Transitional Justice. Oxford University Press; 2000.",
            "Gibson JL. Overcoming Apartheid. Russell Sage; 2004.",
        ],
        hypotheses=[
            "Sequencing determines outcomes.",
            "Justice always helps peace.",
            "Justice threatens peace; amnesties work better.",
            "The effects are too contextual to generalize.",
        ],
        confirm="Outcomes track process sequencing.",
        refute="Sequencing shows no systematic effect.",
    ),
    dict(
        key="legal-studies-24",
        name="The Countermajoritarian Difficulty",
        group="Theory",
        ladder_rank=24,
        ladder_tier="advanced",
        problem=("How can unelected judges overruling elected legislatures "
                 "be democratic - Bickel's countermajoritarian difficulty?"),
        background=("Bickel posed the puzzle in 1962; generations of "
                    "theorists answered: representation-reinforcement "
                    "(Ely), rights protection (Dworkin), popular "
                    "constitutionalism (Kramer), or acceptance that it "
                    "is not democratic. The difficulty persists because "
                    "judicial review keeps striking down popular laws."),
        why_it_matters=("The difficulty is constitutional theory's "
                        "founding problem. Its resolution legitimates or "
                        "delegitimates judicial power."),
        sig_lens=("The Signature lens treats the difficulty as a time "
                  "ledger: the Signature approach asks which majority "
                  "counts - today's or the constitution's."),
        sig_body=("The Signature proposal models the difficulty as "
                  "intertemporal majoritarianism. Assumptions: (1) "
                  "constitutions record past supermajorities; (2) judges "
                  "enforce those against present majorities; (3) "
                  "amendment is the escape valve. Reasoning path: the "
                  "proposal shows judicial review is democratic across "
                  "time - past peoples binding present ones - predicting "
                  "the difficulty should bite hardest where amendment is "
                  "impossible, which matches the American case. The "
                  "answer is then institutional, not philosophical. "
                  "Limits: the model needs a theory of intergenerational "
                  "binding; the dead-hand problem persists."),
        pointer=('The Signature system models judicial review as intertemporal majoritarianism, with the difficulty biting where amendment is impossible. The Signature test: legitimacy tracks amendment accessibility. It would be refuted if unamendable review proves equally legitimate.'),
        key_points=[
            "Bickel posed the puzzle in 1962.",
            "Representation-reinforcement, rights, and popular constitutionalism compete.",
            "Judicial review keeps striking down popular laws.",
            "No resolution commands consensus.",
        ],
        requirements=[
            "A theory of intergenerational binding.",
            "An account of amendment's role.",
            "Comparative data on review legitimacy.",
        ],
        standards=[
            "Claims checked against the constitutional-theory literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Bickel AM. The Least Dangerous Branch. Yale University Press; 1962.",
            "Ely JH. Democracy and Distrust. Harvard University Press; 1980.",
        ],
        hypotheses=[
            "Intertemporal majoritarianism resolves the difficulty.",
            "The difficulty is irresolvable; accept it.",
            "Popular constitutionalism is the answer.",
            "Judicial review is simply undemocratic.",
        ],
        confirm="Legitimacy tracks amendment accessibility.",
        refute="Unamendable review proves equally legitimate.",
    ),
    dict(
        key="legal-studies-25",
        name="Legal Indeterminacy: How Much",
        group="Theory",
        ladder_rank=25,
        ladder_tier="advanced",
        problem=("How indeterminate is law - do legal materials determine "
                 "outcomes, or do judges decide and rationalize?"),
        background=("Legal realists and critical legal studies argued "
                    "indeterminacy is pervasive; formalists reply that "
                    "most cases are easy. Empirical work shows ideology "
                    "predicts appellate votes substantially - but most "
                    "cases settle or go unappealed, suggesting the "
                    "indeterminacy is concentrated in hard cases. How much "
                    "law is indeterminate remains the field's empirical "
                    "hole."),
        why_it_matters=("Indeterminacy determines whether law rules or "
                        "rulers do. Its measure is the rule of law's "
                        "measure."),
        sig_lens=("The Signature lens treats indeterminacy as a selection "
                  "ledger: the Signature approach asks which cases reach "
                  "judges."),
        sig_body=("The Signature proposal models observed indeterminacy "
                  "as selection-biased. Assumptions: (1) clear cases "
                  "settle; (2) litigated cases are the close ones; (3) "
                  "ideology matters most where law is unclear. Reasoning "
                  "path: the proposal predicts ideology should predict "
                  "votes strongly in appellate samples but weakly in the "
                  "full case population - which matches the evidence. "
                  "Law is then mostly determinate; the indeterminacy "
                  "scholars study is a selected sample. Limits: the "
                  "model needs better population data; settlement "
                  "itself reflects predicted indeterminacy."),
        pointer=('The Signature system models observed indeterminacy as selection bias: clear cases settle, leaving the close ones for judges. The Signature test: ideology effects shrink in population samples. It would be refuted if ideology predicts equally in unselected samples.'),
        key_points=[
            "Ideology predicts appellate votes substantially.",
            "Most cases settle or go unappealed.",
            "Realists claim pervasive indeterminacy.",
            "Selection bias may inflate the findings.",
        ],
        requirements=[
            "Population-level (not appellate-only) data.",
            "A selection model of litigation.",
            "Indeterminacy measures by case type.",
        ],
        standards=[
            "Claims checked against the indeterminacy literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Kennedy D. Legal Education and the Reproduction of Hierarchy. 1983.",
            "Epstein L et al. The behavior of federal judges. 2013.",
        ],
        hypotheses=[
            "Selection bias explains the indeterminacy findings.",
            "Indeterminacy is genuinely pervasive.",
            "Hard cases are indeterminate; easy cases are not.",
            "The question is unanswerable empirically.",
        ],
        confirm="Ideology effects shrink in population samples.",
        refute="Ideology predicts equally in unselected samples.",
    ),
    dict(
        key="legal-studies-26",
        name="The Moral Reading of Law",
        group="Theory",
        ladder_rank=26,
        ladder_tier="advanced",
        problem=("Should judges read the constitution morally - as Dworkin "
                 "urged - or does moral reading license judicial "
                 "imposition?"),
        background=("Dworkin's moral reading asks judges to find the best "
                    "moral interpretation of constitutional principles. "
                    "Critics reply that moral disagreement makes this "
                    "undemocratic and unpredictable. The debate parallels "
                    "the originalism fight but on moral rather than "
                    "historical grounds."),
        why_it_matters=("The moral reading underwrites rights revolutions "
                        "(and backlashes). Its legitimacy is constitutional "
                        "law's legitimacy."),
        sig_lens=("The Signature lens treats moral reading as a "
                  "disagreement ledger: the Signature approach asks whose "
                  "morality the judge reads."),
        sig_body=("The Signature proposal models moral reading as "
                  "disagreement-bounded. Assumptions: (1) constitutional "
                  "principles are morally laden; (2) moral disagreement "
                  "is reasonable; (3) judges need constraining sources. "
                  "Reasoning path: the proposal predicts moral reading "
                  "should be legitimate where it tracks evolving social "
                  "morality and illegitimate where it imposes elite "
                  "morality - explaining both the rights-revolution "
                  "successes and the backlashes. The constraint is then "
                  "sociological, not textual. Limits: the model needs "
                  "better social-morality measures; the line between "
                  "tracking and imposing is thin."),
        pointer=('The Signature system bounds moral reading sociologically: legitimate where it tracks evolving social morality. The Signature test: decisions track social-morality measures. It would be refuted if moral readings systematically impose elite morality.'),
        key_points=[
            "Dworkin urged the best moral interpretation of principles.",
            "Critics cite disagreement and democratic deficit.",
            "The debate parallels the originalism fight.",
            "Rights revolutions and backlashes both invoke moral reading.",
        ],
        requirements=[
            "Social-morality measures independent of decisions.",
            "An account of tracking versus imposing.",
            "A constraint theory for moral judgment.",
        ],
        standards=[
            "Claims checked against the constitutional-theory literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Dworkin R. Freedom's Law. Harvard University Press; 1996.",
            "Fleming JE. Fidelity to Our Imperfect Constitution. 2015.",
        ],
        hypotheses=[
            "Sociological tracking bounds moral reading legitimately.",
            "Moral reading is undemocratic imposition.",
            "Text and history constrain it adequately.",
            "The debate is irresolvable.",
        ],
        confirm="Decisions track social-morality measures.",
        refute="Moral readings systematically impose elite morality.",
    ),
    dict(
        key="legal-studies-27",
        name="Algorithmic Justice: Can It Be Fair",
        group="Courts",
        ladder_rank=27,
        ladder_tier="advanced",
        problem=("Can risk-assessment algorithms be fair - and what does "
                 "fairness even mean when base rates differ?"),
        background=("COMPAS and similar tools predict recidivism; ProPublica "
                    "found racial disparities in error rates. The "
                    "impossibility theorems show competing fairness "
                    "definitions cannot all hold when base rates differ. "
                    "Whether algorithms improve on human bias or encode it "
                    "remains fiercely contested."),
        why_it_matters=("Algorithms increasingly decide bail, sentencing, "
                        "and parole. Their fairness is justice's fairness."),
        sig_lens=("The Signature lens treats algorithmic fairness as a "
                  "tradeoff ledger: the Signature approach asks which "
                  "fairness definition the law should choose."),
        sig_body=("The Signature proposal models the fairness debate as a "
                  "mathematical tradeoff requiring a normative choice. "
                  "Assumptions: (1) impossibility theorems are correct; "
                  "(2) base rates differ by group; (3) human judges are "
                  "also biased. Reasoning path: the proposal shows the "
                  "question is not technical but normative - which errors "
                  "should be equalized - predicting that the right "
                  "comparison is algorithm-versus-human, not algorithm-"
                  "versus-perfection. Transparency then matters more than "
                  "any single metric. Limits: the model needs better "
                  "human-baseline data; the normative choice needs "
                  "democratic input."),
        pointer=('The Signature system frames algorithmic fairness as a normative choice among incompatible definitions, compared against human baselines. The Signature test: algorithms outperform human baselines transparently. It would be refuted if no fairness definition proves workable in practice.'),
        key_points=[
            "Risk tools predict recidivism; disparities documented.",
            "Impossibility theorems block satisfying all fairness definitions.",
            "Base-rate differences drive the tradeoffs.",
            "Human judges are the relevant baseline.",
        ],
        requirements=[
            "Human-baseline bias measures.",
            "A normative framework for choosing fairness definitions.",
            "Transparency standards for the tools.",
        ],
        standards=[
            "Claims checked against the algorithmic-fairness literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Angwin J et al. Machine bias. ProPublica; 2016.",
            "Corbett-Davies S, Goel S. The measure and mismeasure of fairness. 2018.",
        ],
        hypotheses=[
            "Normative choice plus human baselines resolves the debate.",
            "Algorithms cannot be fair; ban them.",
            "Algorithms beat humans and should be used.",
            "The debate is technically confused.",
        ],
        confirm="Algorithms outperform human baselines transparently.",
        refute="No fairness definition proves workable in practice.",
    ),
    dict(
        key="legal-studies-28",
        name="Restorative Justice: Does It Work",
        group="Courts",
        ladder_rank=28,
        ladder_tier="advanced",
        problem=("Does restorative justice - victim-offender dialogue, "
                 "repair over punishment - reduce reoffending and heal?"),
        background=("Experiments (notably in Australia and the UK) show "
                    "restorative conferences can reduce reoffending for "
                    "some crimes. But selection effects loom (willing "
                    "participants differ), serious crimes are rarely "
                    "included, and scaling from experiments to systems is "
                    "unproven. Whether restoration can replace retribution "
                    "remains open."),
        why_it_matters=("Restorative justice promises a different criminal "
                        "justice - healing rather than hurting. Its "
                        "evidence base determines its future."),
        sig_lens=("The Signature lens treats restoration as a selection "
                  "ledger: the Signature approach asks who participates "
                  "and what that means for the results."),
        sig_body=("The Signature proposal models restorative effects as "
                  "real but selection-bounded. Assumptions: (1) "
                  "willingness to participate signals remorse and "
                  "victim readiness; (2) the conference mechanism "
                  "(shame, repair, reintegration) works on the willing; "
                  "(3) unwilling cases differ fundamentally. Reasoning "
                  "path: the proposal predicts effects should be genuine "
                  "within the participant population but not generalizable "
                  "to all offenders - explaining the positive experiments "
                  "and the scaling doubts together. Restoration is then "
                  "a complement, not a replacement. Limits: the model "
                  "needs better selection-adjusted estimates; serious-"
                  "crime applications need study."),
        pointer=('The Signature system models restorative effects as genuine but selection-bounded - a complement to retribution, not a replacement. The Signature test: effects persist with selection adjustment. It would be refuted if no effect survives selection controls.'),
        key_points=[
            "Experiments show reduced reoffending for some crimes.",
            "Selection effects loom large.",
            "Serious crimes are rarely included.",
            "Scaling from experiments to systems is unproven.",
        ],
        requirements=[
            "Selection-adjusted effect estimates.",
            "Serious-crime applications data.",
            "A scaling theory.",
        ],
        standards=[
            "Claims checked against the restorative-justice literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Sherman LW, Strang H. Restorative Justice: The Evidence. 2007.",
            "Braithwaite J. Restorative Justice and Responsive Regulation. Oxford University Press; 2002.",
        ],
        hypotheses=[
            "Effects are real but bounded by selection.",
            "Restoration can replace retribution broadly.",
            "The effects are entirely selection artifacts.",
            "Restoration works for serious crimes too.",
        ],
        confirm="Effects persist with selection adjustment.",
        refute="No effect survives selection controls.",
    ),
    dict(
        key="legal-studies-29",
        name="The Carceral State: Why America",
        group="Comparative",
        ladder_rank=29,
        ladder_tier="advanced",
        problem=("Why does the United States incarcerate at 5-10 times the "
                 "rate of other democracies - and why did the buildup "
                 "happen when it did?"),
        background=("Mass incarceration grew from the 1970s, driven by "
                    "drug war policies, mandatory minimums, and "
                    "prosecutorial discretion - with stark racial "
                    "disparities. Explanations: crime rates, politics "
                    "(tough-on-crime competition), institutional "
                    "fragmentation, and racial control. The recent "
                    "modest decline raises the question of reversibility."),
        why_it_matters=("Mass incarceration is America's distinctive "
                        "social policy. Its causes determine whether it "
                        "can be undone."),
        sig_lens=("The Signature lens treats incarceration as a political "
                  "ledger: the Signature approach asks who gained from "
                  "the buildup."),
        sig_body=("The Signature proposal models mass incarceration as a "
                  "political equilibrium. Assumptions: (1) tough-on-crime "
                  "politics rewarded severity; (2) prosecutors and "
                  "legislators faced asymmetric incentives; (3) the costs "
                  "fell on the powerless. Reasoning path: the proposal "
                  "predicts the buildup should track political "
                  "competition on crime - which it does - and that "
                  "reversal needs changed incentives, not just changed "
                  "minds. The racial disparities then reflect both "
                  "targeting and the political economy of punishment. "
                  "Limits: the model needs better incentive measures; "
                  "the crime-rate contribution is debated."),
        pointer=('The Signature system models mass incarceration as a political equilibrium, with reversal needing changed incentives. The Signature test: incarceration tracks political-competition measures. It would be refuted if incarceration falls with incentives unchanged.'),
        key_points=[
            "US incarceration is 5-10 times peer democracies.",
            "The buildup began in the 1970s.",
            "Racial disparities are stark.",
            "A modest decline has begun; reversibility is open.",
        ],
        requirements=[
            "Political-incentive measures over time.",
            "An account of the racial disparities.",
            "A reversibility theory.",
        ],
        standards=[
            "Claims checked against the punishment literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Alexander M. The New Jim Crow. New Press; 2010.",
            "Pfaff JF. Locked In. Basic Books; 2017.",
        ],
        hypotheses=[
            "Political equilibrium explains the buildup and its persistence.",
            "Crime rates drove the policy.",
            "Racial control was the primary purpose.",
            "Prosecutorial discretion is the key mechanism.",
        ],
        confirm="Incarceration tracks political-competition measures.",
        refute="Incarceration falls with incentives unchanged.",
    ),
    dict(
        key="legal-studies-30",
        name="Sharia and Secular Law: The Interface",
        group="Comparative",
        ladder_rank=30,
        ladder_tier="advanced",
        problem=("How do Islamic legal traditions and secular state law "
                 "interact - and can they coexist without conflict?"),
        background=("Muslim-majority states mix sharia with civil and "
                    "common law in varied hybrids; Western states face "
                    "questions of accommodation (arbitration, family law). "
                    "The interaction is often framed as clash, but the "
                    "reality is centuries of coexistence and adaptation. "
                    "Whether stable pluralism is achievable remains "
                    "contested."),
        why_it_matters=("The interface affects hundreds of millions. Its "
                        "stability determines whether legal pluralism "
                        "works."),
        sig_lens=("The Signature lens treats the interface as a "
                  "jurisdiction ledger: the Signature approach asks "
                  "which law governs which domain."),
        sig_body=("The Signature proposal models stable pluralism as "
                  "domain separation. Assumptions: (1) legal systems can "
                  "divide labor by domain (family, commerce, crime); (2) "
                  "conflict concentrates at the boundaries; (3) "
                  "accommodation needs institutional channels. Reasoning "
                  "path: the proposal predicts coexistence succeeds "
                  "where domains are clearly allocated - as in "
                  "historical Ottoman millet arrangements and modern "
                  "arbitration - and fails where boundaries blur. The "
                  "clash narrative then mistakes boundary disputes for "
                  "system incompatibility. Limits: the model needs "
                  "better boundary-dispute data; power asymmetries "
                  "shape every interface."),
        pointer=('The Signature system models stable pluralism as domain separation, with conflict concentrating at boundaries. The Signature test: stability tracks domain-clarity measures. It would be refuted if clear domains still produce systemic conflict.'),
        key_points=[
            "Muslim-majority states use varied legal hybrids.",
            "Western states face accommodation questions.",
            "Centuries of coexistence belie the clash narrative.",
            "Whether stable pluralism is achievable is contested.",
        ],
        requirements=[
            "Domain-allocation analysis across systems.",
            "Boundary-dispute case studies.",
            "An account of power asymmetries.",
        ],
        standards=[
            "Claims checked against the Islamic-law literature; sensitivity observed.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Hallaq WB. Sharia. Cambridge University Press; 2009.",
            "An-Na'im AA. Islam and the Secular State. Harvard University Press; 2008.",
        ],
        hypotheses=[
            "Domain separation enables stable pluralism.",
            "The systems are fundamentally incompatible.",
            "Accommodation works through institutional channels.",
            "Secularization will dissolve the question.",
        ],
        confirm="Stability tracks domain-clarity measures.",
        refute="Clear domains still produce systemic conflict.",
    ),
    dict(
        key="legal-studies-31",
        name="Indigenous Law and State Law",
        group="Comparative",
        ladder_rank=31,
        ladder_tier="advanced",
        problem=("How should indigenous legal orders relate to state law - "
                 "recognition, autonomy, or integration?"),
        background=("Colonial states suppressed indigenous law; "
                    "decolonization revived it. Models range from "
                    "constitutional recognition (Bolivia, Ecuador) to "
                    "tribal courts (US, Canada) to informal coexistence. "
                    "Tensions arise over rights conflicts (gender, "
                    "punishment) and jurisdictional boundaries. The "
                    "normative and practical questions remain open."),
        why_it_matters=("Indigenous justice affects millions and tests "
                        "whether legal pluralism can be just."),
        sig_lens=("The Signature lens treats the relationship as a "
                  "sovereignty ledger: the Signature approach asks what "
                  "self-determination requires legally."),
        sig_body=("The Signature proposal models recognition as "
                  "jurisdiction-plus-rights-floor. Assumptions: (1) "
                  "self-determination needs real jurisdiction; (2) "
                  "individual rights need protection; (3) the two can "
                  "conflict. Reasoning path: the proposal predicts "
                  "stable arrangements combine indigenous jurisdiction "
                  "with rights floors - as in the best tribal-court "
                  "systems - while pure autonomy risks rights gaps and "
                  "pure integration erases the law. The design problem "
                  "is then genuine, not rhetorical. Limits: the model "
                  "needs better outcome data; the rights-floor content "
                  "is contested."),
        pointer=('The Signature system models stable arrangements as indigenous jurisdiction with rights floors. The Signature test: outcomes track jurisdiction-rights combinations. It would be refuted if no arrangement satisfies both demands.'),
        key_points=[
            "Colonial suppression gave way to revival movements.",
            "Recognition models vary: constitutional, tribal-court, informal.",
            "Rights conflicts (gender, punishment) create tensions.",
            "The normative questions remain open.",
        ],
        requirements=[
            "Outcome data across recognition models.",
            "An account of rights-conflict resolution.",
            "A design theory for pluralism.",
        ],
        standards=[
            "Claims checked against the indigenous-law literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Borrows J. Canada's Indigenous Constitution. University of Toronto Press; 2010.",
            "Tamanaha BZ. Understanding legal pluralism. 2008.",
        ],
        hypotheses=[
            "Jurisdiction plus rights floors is the stable design.",
            "Full autonomy is required by self-determination.",
            "Integration best protects individuals.",
            "Pluralism is unworkable in practice.",
        ],
        confirm="Outcomes track jurisdiction-rights combinations.",
        refute="No arrangement satisfies both demands.",
    ),
    dict(
        key="legal-studies-32",
        name="The Future of Legal Personhood",
        group="Rights",
        ladder_rank=32,
        ladder_tier="advanced",
        problem=("Should legal personhood extend to animals, ecosystems, "
                 "or AIs - and what would it mean?"),
        background=("Rivers gained personhood (New Zealand, India); "
                    "animal-personhood cases advanced and stalled; AI "
                    "personhood is debated prospectively. Each extension "
                    "forces the question of what personhood is for - "
                    "protection, standing, or moral recognition. The "
                    "trajectory suggests expansion, but the principles "
                    "remain unarticulated."),
        why_it_matters=("Personhood extensions remake the moral and legal "
                        "universe. The principles will govern the next "
                        "century's hardest cases."),
        sig_lens=("The Signature lens treats personhood as a standing "
                  "ledger: the Signature approach asks what interests "
                  "need legal voice."),
        sig_body=("The Signature proposal models personhood as "
                  "interest-representation. Assumptions: (1) personhood "
                  "grants standing and protection; (2) the function is "
                  "giving voiceless interests legal voice; (3) the "
                  "criterion should be interests, not species or "
                  "substrate. Reasoning path: the proposal predicts "
                  "extensions should track protectable interests - "
                  "rivers (ecological integrity), animals (sentience), "
                  "AIs (if conscious) - providing a principled path "
                  "instead of ad hoc expansion. Limits: the model needs "
                  "interest theories for each candidate; the AI case is "
                  "speculative."),
        pointer=('The Signature system models personhood as interest-representation, with extensions tracking protectable interests. The Signature test: extensions track interest criteria. It would be refuted if extensions prove arbitrary and unprincipled.'),
        key_points=[
            "Rivers have gained legal personhood in several jurisdictions.",
            "Animal personhood cases advanced and stalled.",
            "AI personhood is debated prospectively.",
            "The underlying principles remain unarticulated.",
        ],
        requirements=[
            "Interest theories for candidate persons.",
            "An account of the river precedents.",
            "A principled extension criterion.",
        ],
        standards=[
            "Claims checked against the personhood literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Stone CD. Should Trees Have Standing? Oxford University Press; 2010.",
            "Wise SM. Rattling the Cage. Perseus; 2000.",
        ],
        hypotheses=[
            "Interest-representation provides the principled path.",
            "Personhood should stay human-only.",
            "Expansion is inevitable and unprincipled.",
            "The concept will dissolve under pressure.",
        ],
        confirm="Extensions track interest criteria.",
        refute="Extensions prove arbitrary and unprincipled.",
    ),
    dict(
        key="legal-studies-33",
        name="Global Constitutionalism: Possible",
        group="Comparative",
        ladder_rank=33,
        ladder_tier="advanced",
        problem=("Is global constitutionalism - constitutional principles "
                 "beyond the state - possible or coherent?"),
        background=("Scholars propose constitutionalizing international "
                    "law: human rights as higher law, judicial review of "
                    "global governance. Critics reply there is no global "
                    "demos, no enforcement, and the project smuggles "
                    "Western liberalism. Whether the constitutional "
                    "imaginary fits global politics remains open."),
        why_it_matters=("Global problems need global governance; "
                        "constitutionalism would legitimate it. The "
                        "possibility determines the institutional "
                        "horizon."),
        sig_lens=("The Signature lens treats the project as a demos ledger: "
                  "the Signature approach asks what constitutionalism "
                  "needs that the globe lacks."),
        sig_body=("The Signature proposal models global "
                  "constitutionalism as functionally partial. "
                  "Assumptions: (1) constitutionalism needs constraint "
                  "of power; (2) global power is fragmented; (3) "
                  "rights regimes already constrain partially. "
                  "Reasoning path: the proposal predicts "
                  "constitutional functions should emerge piecemeal - "
                  "human-rights review, trade dispute settlement - "
                  "without a global constitution, which matches the "
                  "record. The project is then real but partial by "
                  "nature. Limits: the model needs better "
                  "functional-equivalence measures; the democratic "
                  "deficit persists."),
        pointer=('The Signature system models global constitutionalism as functionally partial, emerging piecemeal without a global constitution. The Signature test: constitutional functions emerge piecemeal. It would be refuted if no constitutional function operates globally.'),
        key_points=[
            "Scholars propose constitutionalizing international law.",
            "Critics cite no global demos and no enforcement.",
            "Rights regimes already constrain partially.",
            "Whether the imaginary fits remains open.",
        ],
        requirements=[
            "Functional-equivalence measures.",
            "An account of the democratic deficit.",
            "A theory of partial constitutionalization.",
        ],
        standards=[
            "Claims checked against the global-constitutionalism literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Peters A. Compensatory constitutionalism. 2006.",
            "Dunoff JL, Trachtman JP. Ruling the World? Cambridge University Press; 2009.",
        ],
        hypotheses=[
            "Piecemeal functional constitutionalism is real.",
            "The project is incoherent without a demos.",
            "It smuggles Western liberalism.",
            "A global constitution will eventually emerge.",
        ],
        confirm="Constitutional functions emerge piecemeal.",
        refute="No constitutional function operates globally.",
    ),
    dict(
        key="legal-studies-34",
        name="A Unified Theory of Law",
        group="Theory",
        ladder_rank=34,
        ladder_tier="advanced",
        problem=("Can jurisprudence unify its schools - positivism, "
                 "natural law, realism, critical theory - into one "
                 "account of law?"),
        background=("Each school captures something: positivism the "
                    "social sources, natural law the moral aspiration, "
                    "realism the judicial behavior, critical theory the "
                    "power relations. Unification attempts remain "
                    "programmatic. Whether law's nature permits one "
                    "theory is jurisprudence's foundational question."),
        why_it_matters=("This is legal theory's capstone: the answer "
                        "determines what law is."),
        sig_lens=("The Signature lens treats the schools as an aspect "
                  "ledger: the Signature approach asks what aspect of "
                  "law each school owns."),
        sig_body=("The Signature proposal models unification as "
                  "aspect-integration. Assumptions: (1) law has "
                  "multiple aspects (source, morality, behavior, "
                  "power); (2) each school captures one well; (3) "
                  "aspects interact. Reasoning path: the proposal "
                  "assigns positivism to sources, natural law to "
                  "aspiration, realism to behavior, critical theory to "
                  "power - with legal practice as the integrator. "
                  "Unity comes from the practice that holds the aspects "
                  "together, not from one theory's victory. Limits: "
                  "the integration is sketched; partisans may reject "
                  "the settlement."),
        pointer=('The Signature system assigns each school its aspect of law, with legal practice as the integrator. The Signature test: integrated models predict across aspects. It would be refuted if aspects prove irreducible to common theory.'),
        key_points=[
            "Four schools offer incompatible images of law.",
            "Each captures what the others miss.",
            "Unification attempts remain programmatic.",
            "Whether one theory is possible is foundational.",
        ],
        requirements=[
            "An aspect architecture for the schools.",
            "An account of aspect interaction.",
            "Testable implications of the integration.",
        ],
        standards=[
            "Claims checked against the jurisprudence literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Hart HLA. The Concept of Law. Oxford University Press; 1961.",
            "Dworkin R. Law's Empire. Harvard University Press; 1986.",
        ],
        hypotheses=[
            "Aspect-integration unifies jurisprudence.",
            "The schools are incommensurable.",
            "One school will absorb the rest.",
            "Pluralism is permanent.",
        ],
        confirm="Integrated models predict across aspects.",
        refute="Aspects prove irreducible to common theory.",
    ),
]
