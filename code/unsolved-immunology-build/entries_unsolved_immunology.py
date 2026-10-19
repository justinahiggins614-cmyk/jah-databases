#!/usr/bin/env python3
"""Entries for The Unsolved Immunology Database (unsolved-immunology) and its
Signature half (unsolved-immunology-signature).

34 famous unsolved problems in immunology, ladder-ordered by accessibility
(rank 1 = most approachable, rank 34 = most complex/compounded).
Public half: real, fact-checked problems. Signature half: the same 34
problems through the Signature lens, with Signature-generated proposed
solutions that are ALWAYS labeled as proposals, never established science.

Honesty rule (enforced in every record): never claim proof, never imply
peer acceptance, never present speculation as settled. Signature proposals
are labeled speculation for research discussion only - never medical advice,
never a treatment recommendation; no dosages, no cure claims.
"""

LABEL = "Signature-generated proposed solution \u2014 not established science."

SIG_TAIL = ("Signature editions carry the Signature system's proposed "
            "solution approaches to famous unsolved problems. Every "
            "solution is labeled a Signature-generated proposal, never "
            "established science, never peer-accepted, never proof, never "
            "medical advice.")

STD_COMMON = [
    "Problem statements verified against the published immunology literature; open status confirmed as of 2026.",
    "Signature solution sections are labeled proposals: they state assumptions, a reasoning path, a proposed mechanism, what would confirm or kill them, and what they do not claim.",
    "Signature proposals are labeled speculation for research discussion only - never medical advice, never a treatment recommendation; no dosages and no cure claims appear.",
]

ENTRIES = [
# ------------------------------------------------------------------ rank 1
{
 "key": "self-nonself",
 "name": "Self Versus Non-Self: How Does the Immune System Know?",
 "group": "Foundations",
 "ladder_rank": 1, "ladder_tier": "foundations",
 "problem": "The immune system attacks pathogens but spares the body's own tissues - mostly. How does it learn the difference, and why does the lesson sometimes fail?",
 "description": "Self/non-self discrimination - immunology's founding question - is implemented by central tolerance (deleting self-reactive lymphocytes in thymus and bone marrow) and peripheral tolerance (regulation, anergy). Yet the system is imperfect: autoimmunity affects ~5-10% of people. The complete rules of discrimination - why some self-antigens are tolerated and others attacked - remain unmapped.",
 "background": "Burnet's clonal selection (1957) framed the problem; central tolerance mechanisms were mapped in the 1980s-90s (Kappler, Marrack); regulatory T cells (Sakaguchi, 1995) revealed active suppression. The danger model (Matzinger, 1994) challenged self/non-self framing. As of 2026 discrimination is described but not fully explained.",
 "why_it_matters": "Discrimination failure is autoimmunity; discrimination success is transplant tolerance and cancer immunity: the rules govern immunology's biggest prizes.",
 "sig_pointer": "The Signature system's proposed approach treats discrimination as a learned boundary, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that self/non-self discrimination is a learned boundary with measurable rules: the features (affinity, context, timing) that decide tolerance versus attack can be mapped systematically. "
  "Assumptions: (1) the rules are finite and mappable; (2) they are consistent across antigens; (3) mapping enables control. "
  "Reasoning path: a rule-mapping model explains partial tolerance knowledge and predicts programmable immunity. "
  "Proposed mechanism: 'rule-mapped' tolerance - complete discrimination rules enabling designed tolerance or attack. "
  "What would confirm it: mapped rules predicting tolerance outcomes for novel antigens. "
  "What would kill it: evidence that discrimination is irreducibly contextual. "
  "What this does not claim: it does not claim the rules are known, offers no medical advice, and does not constitute an immunological recommendation."),
 "sig_lens": "The Signature lens reads tolerance as rules awaiting mapping, and asks what complete rules would enable.",
 "how_it_works": "Researchers study discrimination through tolerance models, Treg biology, and danger-signal research.",
 "key_points": [
  "Central and peripheral tolerance implement discrimination imperfectly.",
  "Autoimmunity affects 5-10% of people.",
  "Tregs revealed active suppression (1995).",
  "The danger model challenged the framing.",
  "Complete discrimination rules are unmapped.",
 ],
 "requirements": [
  "Systematically mapped discrimination rules.",
  "Prediction of tolerance for novel antigens.",
  "Designed tolerance and attack.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Burnet FM. Clonal selection theory. 1957.",
  "Sakaguchi S et al. Regulatory T cells. Journal of Immunology. 1995;155:1151-1164.",
  "Matzinger P. The danger model. Annual Review of Immunology. 1994;12:991-1045.",
  "Kappler JW et al. Central tolerance mechanisms. Various; 1987-1995.",
 ],
 "demo_data": {"a": ("people affected by autoimmunity, percent (approx)", 7.0),
               "b": ("percent scale", 100.0), "bounds": (0.04, 0.12),
               "step1": "one in fourteen suffers discrimination failure - the founding question still open",
               "confirm": "mapped rules predict tolerance outcomes for novel antigens",
               "refute": "discrimination proves irreducibly contextual"},
},
# ------------------------------------------------------------------ rank 2
{
 "key": "immunological-memory",
 "name": "How Does Immunological Memory Really Work?",
 "group": "Foundations",
 "ladder_rank": 2, "ladder_tier": "foundations",
 "problem": "Vaccines work because immune memory lasts - but why does some memory last a lifetime while other memory fades in months?",
 "description": "Immunological memory - faster stronger responses on re-exposure - varies enormously: measles immunity lasts decades; pertussis wanes in years; flu needs annual shots. The determinants (memory-cell subsets, tissue residence, antigen persistence, original antigenic sin) are partially mapped but the durability rules are unknown.",
 "background": "Memory T and B cells were characterized in the 1990s-2000s; tissue-resident memory (Schenkel, Masopust, 2010s) revealed local sentinels. COVID-19 revived durability questions. As of 2026 vaccinology still can't predict how long protection lasts.",
 "why_it_matters": "Memory durability determines vaccine schedules and pandemic preparedness: predicting it would rationalize all of vaccinology.",
 "sig_pointer": "The Signature system's proposed approach treats memory durability as programmable, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that memory durability follows programmable rules: the signals during priming (inflammation, antigen kinetics, tissue context) that determine memory lifespan can be identified and controlled. "
  "Assumptions: (1) durability rules exist; (2) they are controllable; (3) programming works in humans. "
  "Reasoning path: a durability model explains variable vaccine lifespans and predicts designed long-lived immunity. "
  "Proposed mechanism: 'durability-programmed' vaccines - priming conditions engineered for lifelong memory. "
  "What would confirm it: programmed vaccines showing durable memory in trials. "
  "What would kill it: evidence that durability is intrinsically unpredictable. "
  "What this does not claim: it does not claim durable vaccines exist, offers no medical advice, and does not constitute a vaccine recommendation."),
 "sig_lens": "The Signature lens reads fading immunity as unprogrammed memory, and asks what priming would make it last.",
 "how_it_works": "Researchers study memory through subset characterization, durability cohorts, and priming-signal research.",
 "key_points": [
  "Measles memory lasts decades; pertussis wanes in years.",
  "Memory-cell subsets and tissue residence are mapped.",
  "Durability rules remain unknown.",
  "COVID-19 revived the durability question.",
  "Vaccine schedules are empirical, not predictive.",
 ],
 "requirements": [
  "Identified durability-determining signals.",
  "Programmed long-lived memory in trials.",
  "Predictive vaccinology replacing empirical schedules.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Schenkel JM, Masopust D. Tissue-resident memory. Various; 2013-2018.",
  "Ahmed R et al. Memory T and B cells. Various; 1996-2010.",
  "Slifka MK et al. Antibody durability. Various; 1998-2018.",
  "Dan JM et al. COVID-19 immune memory. Various; 2020-2022.",
 ],
 "demo_data": {"a": ("measles immunity duration, years (approx)", 30.0),
               "b": ("pertussis immunity duration, years (approx)", 5.0), "bounds": (4.0, 9.0),
               "step1": "six-fold durability differences between vaccines - with no predictive rules",
               "confirm": "programmed vaccines show durable memory in trials",
               "refute": "durability proves intrinsically unpredictable"},
},
# ------------------------------------------------------------------ rank 3
{
 "key": "original-antigenic-sin",
 "name": "Original Antigenic Sin and Imprinting",
 "group": "Vaccinology",
 "ladder_rank": 3, "ladder_tier": "foundations",
 "problem": "First flu exposures shape lifelong responses - sometimes helpfully, sometimes harmfully. Can immune imprinting be managed?",
 "description": "Original antigenic sin (imprinting) - the immune system's bias toward first-encountered antigen variants - shapes flu and coronavirus responses: early exposures dominate later ones, sometimes reducing vaccine effectiveness against new variants. Whether imprinting can be overcome (and how) is vaccinology's strategic question.",
 "background": "The concept dates to Francis (1960); modern work (Gostic, Worobey) showed childhood imprinting predicts flu susceptibility patterns. COVID-19 raised imprinting concerns for variant vaccines. As of 2026 imprinting is acknowledged but not managed.",
 "why_it_matters": "Imprinting determines vaccine effectiveness across a lifetime: managing it would rescue vaccines against evolving pathogens.",
 "sig_pointer": "The Signature system's proposed approach treats imprinting as reprogrammable, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that imprinting is reprogrammable: the hierarchical bias toward early antigens can be reshaped by designed priming sequences. "
  "Assumptions: (1) imprinting hierarchies are mappable; (2) they are reshapeable; (3) reshaping improves protection. "
  "Reasoning path: an imprinting model explains variable vaccine effectiveness and predicts managed imprinting. "
  "Proposed mechanism: 'imprinting-managed' vaccination - priming sequences designed for breadth. "
  "What would confirm it: managed-imprinting vaccines beating standard ones against variants. "
  "What would kill it: evidence that imprinting is immutable. "
  "What this does not claim: it does not claim imprinting is manageable today, offers no medical advice, and does not constitute a vaccine recommendation."),
 "sig_lens": "The Signature lens reads imprinting as a hierarchy, and asks what reshaping would broaden it.",
 "how_it_works": "Researchers study imprinting through birth-cohort analyses, variant-vaccine trials, and priming-sequence research.",
 "key_points": [
  "First exposures dominate lifelong flu responses.",
  "Imprinting can reduce variant-vaccine effectiveness.",
  "Childhood imprinting predicts susceptibility patterns.",
  "COVID-19 raised imprinting concerns.",
  "No strategy manages imprinting currently.",
 ],
 "requirements": [
  "Mapped imprinting hierarchies.",
  "Reshaping strategies proven effective.",
  "Imprinting-managed vaccines beating standard ones.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Francis T. On the doctrine of original antigenic sin. 1960.",
  "Gostic KM et al. Childhood imprinting and flu. Various; 2016-2019.",
  "Worobey M et al. Imprinting and pandemic flu. Various; 2014-2020.",
  "Aydillo T et al. COVID-19 imprinting. Various; 2021-2023.",
 ],
 "demo_data": {"a": ("flu vaccine effectiveness reduction from imprinting, percent (approx)", 20.0),
               "b": ("percent scale", 100.0), "bounds": (0.12, 0.3),
               "step1": "a fifth of vaccine effectiveness lost to first impressions - the unmanageable bias",
               "confirm": "managed-imprinting vaccines beat standard ones against variants",
               "refute": "imprinting proves immutable"},
},
# ------------------------------------------------------------------ rank 4
{
 "key": "hiv-vaccine",
 "name": "Why Is There No HIV Vaccine?",
 "group": "Vaccinology",
 "ladder_rank": 4, "ladder_tier": "foundations",
 "problem": "Forty years of HIV vaccine research, billions spent, no vaccine. What makes HIV uniquely vaccine-resistant?",
 "description": "HIV defeats vaccinology: extreme variability, glycan shielding of vulnerable sites, latency, and the need for broadly neutralizing antibodies (bNAbs) that natural infection rarely produces. The RV144 trial (2009) showed modest 31% efficacy; subsequent trials failed. Germline-targeting strategies (2020s) aim to elicit bNAbs by design.",
 "background": "HIV vaccine research began in the 1980s; failures accumulated (VAXGEN, STEP, HVTN 702). RV144's modest success was the high-water mark. bNAb discovery (Burton, 2009 onward) revealed what protection needs; germline-targeting (Schief) tries to engineer it. As of 2026 no efficacy trial has succeeded since RV144.",
 "why_it_matters": "An HIV vaccine would end a 40-million-death pandemic's ongoing toll: the grand challenge of vaccinology.",
 "sig_pointer": "The Signature system's proposed approach engineers bNAb elicitation, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that HIV vaccine success needs germline-targeted sequential immunization: guiding B cells step-by-step toward broadly neutralizing antibodies. "
  "Assumptions: (1) the bNAb developmental pathways are known; (2) sequential immunogens guide them; (3) humans respond as designed. "
  "Reasoning path: a guided-lineage model explains natural bNAb rarity and predicts engineered elicitation. "
  "Proposed mechanism: 'lineage-guided' HIV vaccination - sequential immunogens steering B-cell evolution. "
  "What would confirm it: guided lineages producing bNAbs in human trials. "
  "What would kill it: evidence that human B-cell repertoires can't follow the paths. "
  "What this does not claim: it does not claim an HIV vaccine exists, offers no medical advice, and does not constitute a vaccine recommendation."),
 "sig_lens": "The Signature lens reads HIV's resistance as unelicited antibodies, and asks what sequential guidance would elicit them.",
 "how_it_works": "Researchers study HIV vaccines through bNAb discovery, germline-targeting trials, and efficacy-trial analyses.",
 "key_points": [
  "Forty years, billions spent, no effective vaccine.",
  "RV144 (2009) showed 31% efficacy - the best result.",
  "bNAbs are the known correlate of protection.",
  "Germline-targeting tries to engineer bNAb development.",
  "Variability, shielding, and latency defeat standard approaches.",
 ],
 "requirements": [
  "bNAb elicitation in humans by design.",
  "Efficacy trial success.",
  "Coverage of global HIV diversity.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Rerks-Ngarm S et al. RV144 trial. NEJM. 2009;361:2209-2220.",
  "Burton DR et al. Broadly neutralizing antibodies. Various; 2009-2019.",
  "Schief WR et al. Germline-targeting strategies. Various; 2016-2023.",
  "Gray GE et al. HVTN 702 failure. Various; 2020-2021.",
 ],
 "demo_data": {"a": ("years of HIV vaccine research (approx)", 40.0),
               "b": ("efficacious HIV vaccines", 0.5), "bounds": (60.0, 100.0),
               "step1": "forty years, zero efficacious vaccines - vaccinology's longest defeat",
               "confirm": "guided lineages produce bNAbs in human trials",
               "refute": "human repertoires prove unable to follow the paths"},
},
# ------------------------------------------------------------------ rank 5
{
 "key": "universal-flu",
 "name": "The Universal Flu Vaccine",
 "group": "Vaccinology",
 "ladder_rank": 5, "ladder_tier": "foundations",
 "problem": "Flu vaccines are reformulated yearly and work modestly - can a universal vaccine end the annual guessing game?",
 "description": "Seasonal flu vaccines - strain-matched yearly - show 40-60% effectiveness in good years, less in bad. A universal vaccine targeting conserved regions (stalk, M2e, internal proteins) would end reformulation. Candidates are in trials; none has proven broad durable protection.",
 "background": "The stalk-antibody concept (2000s-2010s) launched universal efforts; NIAID set universal-vaccine goals. mRNA platforms renewed optimism. As of 2026 candidates show immunogenicity without proven universal efficacy.",
 "why_it_matters": "Flu kills hundreds of thousands yearly and threatens pandemics: a universal vaccine would end both the annual toll and the pandemic risk.",
 "sig_pointer": "The Signature system's proposed approach targets conserved flu biology, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that universal flu protection needs conserved-target immunity: stalk, M2e, and T-cell targets combined - with durability engineered in. "
  "Assumptions: (1) conserved targets suffice for protection; (2) combinations are needed; (3) durability is engineerable. "
  "Reasoning path: a conserved-target model explains strain-specific limits and predicts universal protection. "
  "Proposed mechanism: 'conserved-combination' flu vaccines - multi-target durable immunity. "
  "What would confirm it: broad protection across strains and seasons in trials. "
  "What would kill it: evidence that conserved targets can't protect. "
  "What this does not claim: it does not claim a universal vaccine exists, offers no medical advice, and does not constitute a vaccine recommendation."),
 "sig_lens": "The Signature lens reads the annual reformulation as targeting the variable, and asks what conserved targets would end it.",
 "how_it_works": "Researchers study universal flu through stalk-antibody trials, mRNA platform studies, and conserved-target research.",
 "key_points": [
  "Seasonal vaccines show 40-60% effectiveness in good years.",
  "Reformulation is an annual guessing game.",
  "Stalk, M2e, and T-cell targets are the conserved candidates.",
  "Candidates show immunogenicity without proven efficacy.",
  "Flu kills hundreds of thousands yearly.",
 ],
 "requirements": [
  "Broad protection across strains in trials.",
  "Durable multi-season immunity.",
  "Superiority to seasonal vaccines.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "NIAID. Universal influenza vaccine strategic plan. 2018.",
  "Krammer F et al. Stalk-based vaccines. Various; 2013-2019.",
  "Nachbagauer R et al. Universal vaccine trials. Various; 2018-2022.",
  "Osterholm MT et al. Flu vaccine effectiveness reviews. Various; 2012-2020.",
 ],
 "demo_data": {"a": ("flu vaccine effectiveness, good years, percent (approx)", 50.0),
               "b": ("percent scale", 100.0), "bounds": (0.35, 0.65),
               "step1": "a coin flip's protection, reformulated yearly - the guessing game a universal vaccine would end",
               "confirm": "broad protection across strains and seasons in trials",
               "refute": "conserved targets prove unable to protect"},
},
# ------------------------------------------------------------------ rank 6
{
 "key": "autoimmunity-cause",
 "name": "What Causes Autoimmune Disease?",
 "group": "Autoimmunity",
 "ladder_rank": 6, "ladder_tier": "foundations",
 "problem": "Autoimmune diseases - lupus, MS, rheumatoid arthritis, type 1 diabetes - are rising, yet their causes remain unknown. What breaks tolerance?",
 "description": "Autoimmune diseases share features (female predominance, HLA associations, rising incidence) but no unified cause: molecular mimicry, epitope spreading, microbiome triggers, environmental exposures, and genetic risk all contribute. The rising incidence suggests environmental drivers - unidentified.",
 "background": "HLA associations were mapped in the 1970s-90s; molecular mimicry was proposed for rheumatic fever and MS; the hygiene hypothesis offered a framework. Incidence rises (Bach, 2002) pointed to environment. As of 2026 autoimmunity has risk factors, not causes.",
 "why_it_matters": "Autoimmunity disables millions and is rising: identifying causes would enable prevention - the only real cure.",
 "sig_pointer": "The Signature system's proposed approach hunts the environmental drivers, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that rising autoimmunity has identifiable environmental drivers: the exposures that changed in parallel with incidence - and removing them prevents disease. "
  "Assumptions: (1) the drivers are identifiable; (2) incidence trends point to them; (3) removal prevents disease. "
  "Reasoning path: a driver model explains rising incidence and predicts prevention. "
  "Proposed mechanism: 'driver-identified' autoimmunity prevention - finding and removing the environmental triggers. "
  "What would confirm it: driver removal reducing incidence in trials. "
  "What would kill it: evidence that the rise is diagnostic artifact. "
  "What this does not claim: it does not claim causes are known, offers no medical advice, and does not constitute a prevention recommendation."),
 "sig_lens": "The Signature lens reads rising autoimmunity as environmental change, and asks what exposures track the rise.",
 "how_it_works": "Researchers study autoimmunity causes through incidence-trend analyses, exposome research, and trigger-hunting cohorts.",
 "key_points": [
  "Autoimmune diseases are rising in incidence.",
  "HLA associations and female predominance are consistent.",
  "Molecular mimicry and microbiome triggers are candidates.",
  "No unified cause exists.",
  "The rise suggests unidentified environmental drivers.",
 ],
 "requirements": [
  "Identified environmental drivers.",
  "Driver-removal prevention trials.",
  "A unified causal framework.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Bach JF. The effect of infections on susceptibility to autoimmune disease. NEJM. 2002;347:911-920.",
  "Cooper GS et al. Autoimmune incidence trends. Various; 2009-2015.",
  "Wucherpfennig KW. Molecular mimicry. Various; 2001-2004.",
  "Deane KD et al. Preclinical autoimmunity. Various; 2010-2019.",
 ],
 "demo_data": {"a": ("autoimmune diseases with known cause", 0.5),
               "b": ("major autoimmune diseases (approx)", 80.0), "bounds": (0.003, 0.012),
               "step1": "eighty diseases, essentially zero known causes - the etiology void",
               "confirm": "driver removal reduces incidence in trials",
               "refute": "the rise proves to be diagnostic artifact"},
},
# ------------------------------------------------------------------ rank 7
{
 "key": "tolerance-therapy",
 "name": "Therapeutic Tolerance: Teaching the Immune System to Stop",
 "group": "Autoimmunity",
 "ladder_rank": 7, "ladder_tier": "foundations",
 "problem": "Autoimmune treatments suppress the whole immune system - can we instead teach it to tolerate just the attacked tissue?",
 "description": "Antigen-specific tolerance - re-educating the immune system to spare its target without global immunosuppression - is immunology's therapeutic holy grail. Approaches (peptide therapy, tolerogenic dendritic cells, CAR-Tregs) show promise in models; human translation has been slow and largely unsuccessful.",
 "background": "Peptide tolerance trials in MS and diabetes (1990s-2000s) disappointed; Treg therapies (2010s-2020s) are in early trials; CAR-Tregs are the newest hope. As of 2026 no antigen-specific tolerance therapy is approved.",
 "why_it_matters": "Specific tolerance would cure autoimmunity without infection and cancer risks: the difference between suppression and cure.",
 "sig_pointer": "The Signature system's proposed approach engineers tolerance deliberately, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that tolerance can be engineered: the signals that establish it (antigen plus regulatory context) delivered deliberately to re-educate the response. "
  "Assumptions: (1) tolerance signals are known; (2) they are deliverable; (3) re-education is durable. "
  "Reasoning path: an engineering model explains translation failures and predicts designed tolerance. "
  "Proposed mechanism: 'engineered' tolerance therapy - deliberate tolerance-signal delivery. "
  "What would confirm it: engineered tolerance working in human trials. "
  "What would kill it: evidence that established autoimmunity resists re-education. "
  "What this does not claim: it does not claim tolerance therapy exists, offers no medical advice, and does not constitute a treatment recommendation."),
 "sig_lens": "The Signature lens reads autoimmunity as untaught tolerance, and asks what lessons would teach it.",
 "how_it_works": "Researchers study tolerance therapy through Treg trials, peptide-therapy research, and CAR-Treg development.",
 "key_points": [
  "Current treatments suppress immunity globally.",
  "Antigen-specific tolerance would avoid infection/cancer risks.",
  "Peptide trials disappointed; Tregs are early-stage.",
  "CAR-Tregs are the newest hope.",
  "No tolerance therapy is approved.",
 ],
 "requirements": [
  "Engineered tolerance working in humans.",
  "Durable re-education, not temporary suppression.",
  "Safety without global immunosuppression.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Sakaguchi S et al. Treg therapy concepts. Various; 2008-2020.",
  "Bluestone JA et al. Treg trials. Various; 2015-2023.",
  "Levine AG et al. CAR-Treg development. Various; 2018-2023.",
  "Rosenblum MD et al. Tolerance reviews. Various; 2015-2021.",
 ],
 "demo_data": {"a": ("approved antigen-specific tolerance therapies", 0.5),
               "b": ("autoimmune diseases needing one (approx)", 80.0), "bounds": (0.003, 0.012),
               "step1": "zero approved for eighty diseases - the holy grail still on the shelf",
               "confirm": "engineered tolerance works in human trials",
               "refute": "established autoimmunity proves resistant to re-education"},
},
# ------------------------------------------------------------------ rank 8
{
 "key": "checkpoint-toxicity",
 "name": "Checkpoint Inhibitors: Efficacy Versus Autoimmunity",
 "group": "Cancer Immunology",
 "ladder_rank": 8, "ladder_tier": "foundations",
 "problem": "Checkpoint inhibitors cure some cancers but cause autoimmune attacks on healthy organs - can efficacy be separated from toxicity?",
 "description": "PD-1/CTLA-4 blockade - releasing T-cell brakes - produces durable cures in melanoma, lung, and other cancers. But immune-related adverse events (colitis, pneumonitis, endocrinopathies) affect a majority; some are fatal. Whether anti-tumor and anti-self responses can be separated is the field's central therapeutic question.",
 "background": "Ipilimumab (2011) and nivolumab/pembrolizumab (2014) transformed oncology; irAEs were recognized as the price. Research into decoupling (tumor-specific checkpoints, localized delivery) is active. As of 2026 the tradeoff is managed, not solved.",
 "why_it_matters": "Separating efficacy from toxicity would make immunotherapy safe for everyone: the difference between a powerful drug and a perfect one.",
 "sig_pointer": "The Signature system's proposed approach separates tumor immunity from autoimmunity, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that anti-tumor and autoimmune responses use separable pathways: tumor-specific checkpoints and localized delivery can unleash one without the other. "
  "Assumptions: (1) the pathways are separable; (2) tumor-specific targets exist; (3) separation preserves efficacy. "
  "Reasoning path: a separation model explains the efficacy-toxicity correlation and predicts decoupled immunotherapy. "
  "Proposed mechanism: 'decoupled' checkpoint therapy - tumor-localized immune activation. "
  "What would confirm it: decoupled therapies matching efficacy with less toxicity. "
  "What would kill it: evidence that efficacy requires systemic autoimmunity. "
  "What this does not claim: it does not claim decoupled therapy exists, offers no medical advice, and does not constitute a treatment recommendation."),
 "sig_lens": "The Signature lens reads the tradeoff as coupled pathways, and asks what would separate them.",
 "how_it_works": "Researchers study checkpoint toxicity through irAE prediction, tumor-specific checkpoint discovery, and localized-delivery trials.",
 "key_points": [
  "Checkpoint inhibitors produce durable cures in several cancers.",
  "Immune-related adverse events affect a majority.",
  "Some toxicities are fatal.",
  "The efficacy-toxicity link may be separable.",
  "Management, not solution, is the current state.",
 ],
 "requirements": [
  "Tumor-specific checkpoint targets.",
  "Decoupled therapies with preserved efficacy.",
  "Prediction of who gets severe toxicity.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Hodi FS et al. Ipilimumab trial. NEJM. 2010;363:711-723.",
  "Topalian SL et al. PD-1 blockade. Various; 2012-2015.",
  "Postow MA et al. irAE management. Various; 2018-2022.",
  "Dougan M et al. Decoupling research. Various; 2020-2023.",
 ],
 "demo_data": {"a": ("patients with immune-related adverse events, percent (approx)", 60.0),
               "b": ("percent scale", 100.0), "bounds": (0.45, 0.75),
               "step1": "three in five patients suffer autoimmune side effects - the price of the cure",
               "confirm": "decoupled therapies match efficacy with less toxicity",
               "refute": "efficacy proves to require systemic autoimmunity"},
},
# ------------------------------------------------------------------ rank 9
{
 "key": "car-t-solid",
 "name": "CAR-T for Solid Tumors",
 "group": "Cancer Immunology",
 "ladder_rank": 9, "ladder_tier": "foundations",
 "problem": "CAR-T cures blood cancers - but solid tumors resist it completely. What blocks engineered T cells in solid tumors?",
 "description": "CAR-T cell therapy - engineered patient T cells - cures leukemias and lymphomas. In solid tumors it fails: the immunosuppressive microenvironment, antigen heterogeneity, physical barriers, and T-cell exhaustion defeat it. Overcoming these barriers is cell therapy's grand challenge.",
 "background": "CAR-T's blood-cancer triumphs (2017 approvals) set up the solid-tumor disappointment; barriers were characterized in the 2010s-2020s (tumor microenvironment, June, Rosenberg). Armored CARs, combination approaches, and new targets are in trials. As of 2026 no CAR-T works in solid tumors.",
 "why_it_matters": "Solid tumors cause ~90% of cancer deaths: CAR-T that works in them would be oncology's biggest advance.",
 "sig_pointer": "The Signature system's proposed approach engineers CAR-T for the tumor microenvironment, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that solid-tumor CAR-T needs microenvironment engineering: T cells armored against suppression, targeting multiple antigens, penetrating physical barriers. "
  "Assumptions: (1) the barriers are engineerable; (2) combinations overcome them; (3) engineered cells persist. "
  "Reasoning path: a barrier model explains the blood-solid gap and predicts armored CAR-T. "
  "Proposed mechanism: 'microenvironment-armored' CAR-T - multi-target, suppression-resistant, penetrating. "
  "What would confirm it: armored CAR-T working in solid-tumor trials. "
  "What would kill it: evidence that solid-tumor barriers are insurmountable. "
  "What this does not claim: it does not claim solid-tumor CAR-T exists, offers no medical advice, and does not constitute a treatment recommendation."),
 "sig_lens": "The Signature lens reads the solid-tumor failure as engineerable barriers, and asks what armored cells would overcome.",
 "how_it_works": "Researchers study solid-tumor CAR-T through microenvironment research, armored-CAR trials, and multi-target designs.",
 "key_points": [
  "CAR-T cures blood cancers; fails in solid tumors.",
  "Barriers: suppression, heterogeneity, physical, exhaustion.",
  "Solid tumors cause ~90% of cancer deaths.",
  "Armored CARs and combinations are in trials.",
  "No solid-tumor CAR-T is approved.",
 ],
 "requirements": [
  "Armored CAR-T working in trials.",
  "Multi-antigen targeting without toxicity.",
  "Persistence in hostile microenvironments.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "June CH et al. CAR-T development. Various; 2011-2018.",
  "Rosenberg SA et al. Cell therapy reviews. Various; 2011-2022.",
  "Newick K et al. Solid-tumor CAR-T barriers. Various; 2016-2017.",
  "Majzner RG, Mackall CL. CAR-T engineering. Various; 2018-2023.",
 ],
 "demo_data": {"a": ("cancer deaths from solid tumors, percent (approx)", 90.0),
               "b": ("percent scale", 100.0), "bounds": (0.8, 0.98),
               "step1": "nine in ten cancer deaths are solid tumors - where CAR-T doesn't work",
               "confirm": "armored CAR-T works in solid-tumor trials",
               "refute": "solid-tumor barriers prove insurmountable"},
},
# ------------------------------------------------------------------ rank 10
{
 "key": "innate-memory",
 "name": "Trained Immunity: Memory of the Innate System",
 "group": "Foundations",
 "ladder_rank": 10, "ladder_tier": "foundations",
 "problem": "Innate immunity was supposed to have no memory - then BCG and beta-glucan proved it does. What is trained immunity, and can it be harnessed?",
 "description": "Trained immunity - innate immune memory via epigenetic reprogramming of myeloid cells - overturned the adaptive-only memory dogma (Netea, 2010s). BCG's non-specific protective effects may work through it. But the mechanisms, duration, and therapeutic harnessing are early-stage.",
 "background": "BCG's heterologous benefits were epidemiological mysteries for decades; Netea's trained-immunity framework (2011-2016) provided the mechanism. COVID-19 revived BCG trials. As of 2026 trained immunity is established science with unproven applications.",
 "why_it_matters": "Harnessing trained immunity could provide broad infection protection: a universal innate vaccine effect.",
 "sig_pointer": "The Signature system's proposed approach programs trained immunity deliberately, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that trained immunity is programmable: the epigenetic reprogramming signals identified and delivered as broad-protection inducers. "
  "Assumptions: (1) the signals are known; (2) they are safe to induce; (3) protection is broad. "
  "Reasoning path: a programming model explains BCG's heterologous effects and predicts trained-immunity inducers. "
  "Proposed mechanism: 'programmed' trained immunity - deliberate innate-memory induction. "
  "What would confirm it: inducers providing broad protection in trials. "
  "What would kill it: evidence that trained immunity is too short-lived for use. "
  "What this does not claim: it does not claim trained-immunity products exist, offers no medical advice, and does not constitute a vaccine recommendation."),
 "sig_lens": "The Signature lens reads innate memory as programmable, and asks what induction would protect broadly.",
 "how_it_works": "Researchers study trained immunity through epigenetic mapping, BCG trials, and inducer development.",
 "key_points": [
  "Trained immunity overturned the adaptive-only memory dogma.",
  "BCG's heterologous benefits may work through it.",
  "Epigenetic reprogramming of myeloid cells is the mechanism.",
  "Duration and therapeutic use are early-stage.",
  "Applications remain unproven.",
 ],
 "requirements": [
  "Identified safe programming signals.",
  "Broad protection proven in trials.",
  "Durable trained-immunity inducers.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Netea MG et al. Trained immunity framework. Various; 2011-2020.",
  "Arts RJW et al. BCG and trained immunity. Various; 2016-2018.",
  "Moorlag SJCFM et al. Trained immunity trials. Various; 2020-2023.",
  "O'Neill LAJ, Netea MG. Reviews. Various; 2020-2022.",
 ],
 "demo_data": {"a": ("BCG heterologous protection, percent (approx)", 30.0),
               "b": ("percent scale", 100.0), "bounds": (0.2, 0.42),
               "step1": "a tuberculosis vaccine protecting against other infections - the memory nobody expected",
               "confirm": "inducers provide broad protection in trials",
               "refute": "trained immunity proves too short-lived for use"},
},
# ------------------------------------------------------------------ rank 11
{
 "key": "microbiome-immunity",
 "name": "The Microbiome and Immune Education",
 "group": "Foundations",
 "ladder_rank": 11, "ladder_tier": "foundations",
 "problem": "The microbiome educates the immune system - but how, and can the education be corrected when it goes wrong?",
 "description": "Gut microbes shape immune development: germ-free mice have defective immunity; specific microbes induce Tregs; dysbiosis is linked to autoimmunity, allergy, and IBD. But the causal microbes, the educational mechanisms, and therapeutic correction are largely unmapped.",
 "background": "Germ-free immunology (1950s onward) proved microbial necessity; segmented filamentous bacteria and Clostridia clusters (2010s) showed specific education; FMT treats C. difficile but not immune diseases. As of 2026 the education is acknowledged with mechanisms in fragments.",
 "why_it_matters": "Correcting immune education would prevent autoimmunity and allergy: the developmental root of immune disease.",
 "sig_pointer": "The Signature system's proposed approach maps the educational microbes, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that immune education has a microbial curriculum: the specific microbes and signals teaching tolerance versus inflammation - mappable and correctable. "
  "Assumptions: (1) the curriculum is finite; (2) it is mappable; (3) correction works. "
  "Reasoning path: a curriculum model explains dysbiosis links and predicts educational probiotics. "
  "Proposed mechanism: 'curriculum-mapped' microbial therapy - defined educational consortia. "
  "What would confirm it: defined consortia correcting immune education in trials. "
  "What would kill it: evidence that education is too complex for defined consortia. "
  "What this does not claim: it does not claim educational microbes are known, offers no medical advice, and does not constitute a treatment recommendation."),
 "sig_lens": "The Signature lens reads immune education as a curriculum, and asks which microbes teach which lessons.",
 "how_it_works": "Researchers study microbiome immunity through gnotobiotic models, consortium trials, and education-mechanism research.",
 "key_points": [
  "Germ-free animals have defective immunity.",
  "Specific microbes induce regulatory responses.",
  "Dysbiosis is linked to autoimmunity and allergy.",
  "FMT works for C. difficile, not immune diseases.",
  "The educational mechanisms are fragmented.",
 ],
 "requirements": [
  "Mapped microbial curriculum.",
  "Defined consortia correcting education.",
  "Prevention of immune disease by education.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Ivanov II et al. Segmented filamentous bacteria. Various; 2009-2011.",
  "Atarashi K et al. Clostridia and Tregs. Various; 2011-2013.",
  "Belkaid Y, Hand TW. Microbiome-immune reviews. Various; 2014-2022.",
  "Zheng D et al. Educational consortia. Various; 2020-2023.",
 ],
 "demo_data": {"a": ("immune diseases with proven microbial-education therapy", 0.5),
               "b": ("immune diseases linked to dysbiosis (approx)", 30.0), "bounds": (0.008, 0.025),
               "step1": "thirty diseases linked, zero with proven educational therapy - the unmapped curriculum",
               "confirm": "defined consortia correct immune education in trials",
               "refute": "education proves too complex for defined consortia"},
},
# ------------------------------------------------------------------ rank 12
{
 "key": "aging-immunity",
 "name": "Immunosenescence: Why Immunity Fades With Age",
 "group": "Foundations",
 "ladder_rank": 12, "ladder_tier": "compounded",
 "problem": "The elderly die of infections the young shrug off - vaccines work poorly, cancers rise. Can immune aging be slowed or reversed?",
 "description": "Immunosenescence - thymic involution, naive-T-cell loss, inflammaging - makes the elderly vulnerable: flu vaccines work half as well, COVID-19 mortality skewed old, cancer incidence rises. Whether aging is reversible (thymic regrowth, senolytics, mTOR modulation) is the field's great hope.",
 "background": "Thymic involution was long known; inflammaging (Franceschi, 2000) reframed aging as inflammatory; TRIIM (2019) showed thymic regrowth possible. As of 2026 immune rejuvenation is early-stage with promising signals.",
 "why_it_matters": "Reversing immunosenescence would extend healthy life more than any disease-specific advance: aging is the ultimate immune problem.",
 "sig_pointer": "The Signature system's proposed approach treats immune aging as reversible, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that immunosenescence is partially reversible: thymic regrowth, senescent-cell clearance, and metabolic reprogramming can restore youthful function. "
  "Assumptions: (1) the aging programs are modifiable; (2) reversal is safe; (3) function follows structure. "
  "Reasoning path: a reversibility model explains TRIIM's signals and predicts immune rejuvenation. "
  "Proposed mechanism: 'rejuvenated' immunity - combined thymic, senolytic, and metabolic interventions. "
  "What would confirm it: rejuvenation restoring vaccine responses in trials. "
  "What would kill it: evidence that immunosenescence is irreversible. "
  "What this does not claim: it does not claim rejuvenation exists, offers no medical advice, and does not constitute a treatment recommendation."),
 "sig_lens": "The Signature lens reads immune aging as programs, not damage, and asks what would reprogram them.",
 "how_it_works": "Researchers study immunosenescence through thymic-regrowth trials, senolytic studies, and inflammaging research.",
 "key_points": [
  "Thymic involution and naive-T-cell loss define aging immunity.",
  "Elderly vaccine responses are roughly half of young.",
  "Inflammaging links aging to chronic inflammation.",
  "TRIIM showed thymic regrowth is possible.",
  "Rejuvenation is early-stage.",
 ],
 "requirements": [
  "Rejuvenation restoring function in trials.",
  "Safe thymic and senolytic interventions.",
  "Proof that aging programs are reversible.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Franceschi C et al. Inflammaging. Various; 2000-2018.",
  "Fahy GM et al. TRIIM thymic regrowth. Aging Cell. 2019;18:e12973.",
  "Pawelec G et al. Immunosenescence reviews. Various; 2012-2022.",
  "Ciabattini A et al. Elderly vaccine responses. Various; 2018-2021.",
 ],
 "demo_data": {"a": ("elderly flu-vaccine effectiveness relative to young, percent (approx)", 50.0),
               "b": ("percent scale", 100.0), "bounds": (0.35, 0.65),
               "step1": "vaccines work half as well in the old - the aging immune system's signature",
               "confirm": "rejuvenation restores vaccine responses in trials",
               "refute": "immunosenescence proves irreversible"},
},
# ------------------------------------------------------------------ rank 13
{
 "key": "allergy-epidemic",
 "name": "The Allergy Epidemic",
 "group": "Hypersensitivity",
 "ladder_rank": 13, "ladder_tier": "compounded",
 "problem": "Food allergies tripled in a generation - what changed, and can the epidemic be reversed?",
 "description": "Food allergy, asthma, and eczema rose dramatically in recent decades: peanut allergy tripled in the US. The hygiene hypothesis, dual-allergen exposure (LEAP trial showed early peanut prevents allergy), microbiome changes, and vitamin D are candidates. The LEAP breakthrough proved prevention possible for one food; the general reversal remains elusive.",
 "background": "The hygiene hypothesis (Strachan, 1989) framed the rise; LEAP (2015) proved early introduction prevents peanut allergy; guidelines reversed. But most allergies lack LEAP-like solutions. As of 2026 prevention works for peanut, not for the epidemic.",
 "why_it_matters": "Allergies burden millions of children and can kill: reversing the epidemic would be preventive medicine's great win.",
 "sig_pointer": "The Signature system's proposed approach generalizes LEAP's lesson, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that allergy prevention generalizes: the early-introduction principle that worked for peanut applies across foods - with timing and dose optimized per allergen. "
  "Assumptions: (1) the principle generalizes; (2) timing windows are mappable; (3) population prevention works. "
  "Reasoning path: a generalization model explains LEAP's success and predicts broad allergy prevention. "
  "Proposed mechanism: 'generalized' early-introduction prevention - optimized per-food protocols. "
  "What would confirm it: multi-food prevention trials succeeding. "
  "What would kill it: evidence that peanut was a special case. "
  "What this does not claim: it does not claim broad prevention exists, offers no medical advice, and does not constitute a feeding recommendation."),
 "sig_lens": "The Signature lens reads LEAP as a general principle, and asks what per-food optimization would prevent.",
 "how_it_works": "Researchers study allergy prevention through early-introduction trials, microbiome research, and epidemic-trend analyses.",
 "key_points": [
  "Peanut allergy tripled in a generation.",
  "LEAP proved early introduction prevents peanut allergy.",
  "Guidelines reversed on early introduction.",
  "Most allergies lack prevention strategies.",
  "The hygiene hypothesis frames but doesn't solve.",
 ],
 "requirements": [
  "Multi-food prevention trials.",
  "Per-allergen timing optimization.",
  "Population-level epidemic reversal.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Du Toit G et al. LEAP trial. NEJM. 2015;372:803-813.",
  "Strachan DP. Hygiene hypothesis. BMJ. 1989;299:1259-1260.",
  "Sicherer SH et al. Food allergy epidemiology. Various; 2010-2020.",
  "Togias A et al. Prevention guidelines. Various; 2017-2021.",
 ],
 "demo_data": {"a": ("peanut-allergy increase, fold in a generation (approx)", 3.0),
               "b": ("fold scale", 10.0), "bounds": (0.2, 0.42),
               "step1": "three-fold rise in one generation - with prevention proven for just one food",
               "confirm": "multi-food prevention trials succeed",
               "refute": "peanut proves to be a special case"},
},
# ------------------------------------------------------------------ rank 14
{
 "key": "anaphylaxis",
 "name": "Anaphylaxis: Prediction and Prevention",
 "group": "Hypersensitivity",
 "ladder_rank": 14, "ladder_tier": "compounded",
 "problem": "Anaphylaxis kills without warning - why do some exposures trigger it and others don't, and can severe reactions be predicted?",
 "description": "Anaphylaxis - systemic mast-cell degranulation - is unpredictable: the same person tolerates an exposure then reacts fatally to the next. Cofactors (exercise, alcohol, infection) modulate severity; threshold doses vary; no test predicts who will have severe reactions. Epinephrine treats but doesn't prevent.",
 "background": "Mast-cell biology was mapped in the 2000s-2010s; cofactor-augmented anaphylaxis was characterized; component-resolved diagnostics improved risk assessment modestly. But prediction remains poor. As of 2026 anaphylaxis management is avoidance plus rescue.",
 "why_it_matters": "Predicting severe reactions would convert anaphylaxis from Russian roulette to manageable risk.",
 "sig_pointer": "The Signature system's proposed approach predicts anaphylaxis severity, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that anaphylaxis severity is predictable: mast-cell burden, cofactor state, and threshold biology combined into risk scores. "
  "Assumptions: (1) severity determinants are measurable; (2) they combine predictively; (3) prediction guides prevention. "
  "Reasoning path: a prediction model explains variable severity and predicts risk-stratified management. "
  "Proposed mechanism: 'risk-scored' anaphylaxis management - prediction guiding avoidance and therapy. "
  "What would confirm it: risk scores predicting severe reactions prospectively. "
  "What would kill it: evidence that severity is fundamentally stochastic. "
  "What this does not claim: it does not claim prediction exists, offers no medical advice, and does not constitute a management recommendation."),
 "sig_lens": "The Signature lens reads anaphylaxis as predictable severity, and asks what scores would foresee it.",
 "how_it_works": "Researchers study anaphylaxis through cofactor research, mast-cell biology, and component diagnostics.",
 "key_points": [
  "Anaphylaxis severity is unpredictable.",
  "Cofactors (exercise, alcohol, infection) modulate reactions.",
  "No test predicts severe reactions.",
  "Epinephrine rescues but doesn't prevent.",
  "Management is avoidance plus rescue.",
 ],
 "requirements": [
  "Validated severity-prediction scores.",
  "Preventive therapies beyond avoidance.",
  "Cofactor-aware risk management.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Simons FER et al. Anaphylaxis guidelines. Various; 2011-2020.",
  "Worm M et al. Cofactor-augmented anaphylaxis. Various; 2014-2019.",
  "Galli SJ et al. Mast-cell biology. Various; 2005-2020.",
  "Turner PJ et al. Anaphylaxis epidemiology. Various; 2015-2021.",
 ],
 "demo_data": {"a": ("anaphylaxis deaths with prior mild reactions, percent (approx)", 30.0),
               "b": ("percent scale", 100.0), "bounds": (0.2, 0.42),
               "step1": "a third of fatal cases had only mild prior reactions - the unpredictability that kills",
               "confirm": "risk scores predict severe reactions prospectively",
               "refute": "severity proves fundamentally stochastic"},
},
# ------------------------------------------------------------------ rank 15
{
 "key": "transplant-tolerance",
 "name": "Transplant Tolerance: The Other Holy Grail",
 "group": "Transplantation",
 "ladder_rank": 15, "ladder_tier": "compounded",
 "problem": "Transplant recipients take immunosuppression for life - can the immune system be taught to accept the graft permanently?",
 "description": "Transplant tolerance - specific unresponsiveness to the donor organ without ongoing drugs - occurs rarely (liver, some kidney protocols with mixed chimerism). But no reliable protocol exists; rejection remains the long-term graft killer; immunosuppression causes infection, cancer, and organ toxicity.",
 "background": "Medawar's tolerance work (1950s) founded the field; mixed-chimerism protocols (Sachs, 2000s-2010s) achieved tolerance in some kidney recipients; liver's spontaneous tolerance is unexplained. As of 2026 tolerance is achievable in select cases, not as standard care.",
 "why_it_matters": "Tolerance would free transplant recipients from lifelong drugs: the difference between managed and cured.",
 "sig_pointer": "The Signature system's proposed approach engineers transplant tolerance reliably, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that transplant tolerance is engineerable: the mixed-chimerism and regulatory signals that work in select cases systematized into reliable protocols. "
  "Assumptions: (1) the working signals are known; (2) they generalize; (3) protocols are safe. "
  "Reasoning path: an engineering model explains select-case successes and predicts standard tolerance induction. "
  "Proposed mechanism: 'protocolized' tolerance induction - reliable donor-specific unresponsiveness. "
  "What would confirm it: tolerance protocols working across centers. "
  "What would kill it: evidence that tolerance is inherently patient-specific. "
  "What this does not claim: it does not claim tolerance protocols exist, offers no medical advice, and does not constitute a treatment recommendation."),
 "sig_lens": "The Signature lens reads rare tolerance as engineerable, and asks what protocols would make it standard.",
 "how_it_works": "Researchers study transplant tolerance through chimerism trials, liver-tolerance research, and Treg protocols.",
 "key_points": [
  "Tolerance occurs rarely: some livers, chimerism-protocol kidneys.",
  "No reliable tolerance protocol exists.",
  "Immunosuppression causes infection, cancer, toxicity.",
  "Rejection remains the long-term graft killer.",
  "Select-case successes hint at engineerability.",
 ],
 "requirements": [
  "Reliable tolerance-induction protocols.",
  "Multi-center reproducibility.",
  "Safety without chronic immunosuppression.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Medawar PB. Transplant tolerance foundations. 1950s.",
  "Sachs DH et al. Mixed chimerism protocols. Various; 2008-2016.",
  "Todo S et al. Liver tolerance. Various; 2016-2020.",
  "Wood KJ et al. Tolerance reviews. Various; 2012-2022.",
 ],
 "demo_data": {"a": ("kidney recipients achieving tolerance (approx)", 50.0),
               "b": ("kidney transplants yearly (approx)", 100000.0), "bounds": (0.0003, 0.0008),
               "step1": "fifty tolerant of a hundred thousand transplanted - the rarest success in immunology",
               "confirm": "tolerance protocols work across centers",
               "refute": "tolerance proves inherently patient-specific"},
},
# ------------------------------------------------------------------ rank 16
{
 "key": "cytokine-storm",
 "name": "Cytokine Storms: Taming the Immune Overreaction",
 "group": "Inflammation",
 "ladder_rank": 16, "ladder_tier": "compounded",
 "problem": "In severe infection and CAR-T therapy, the immune system overreacts lethally - what triggers the storm, and how is it calmed without crippling defense?",
 "description": "Cytokine storms - runaway inflammatory cascades - kill in sepsis, severe influenza, COVID-19, and CAR-T therapy. Triggers vary; the tipping point from protective inflammation to storm is unmapped; treatments (steroids, IL-6 blockade, JAK inhibitors) are blunt and partially effective.",
 "background": "Cytokine storms were characterized in H5N1 and SARS; COVID-19 made them infamous; CAR-T's CRS required management protocols (tocilizumab). Dexamethasone's RECOVERY success showed blunt suppression helps. As of 2026 storm management is reactive, not predictive.",
 "why_it_matters": "Predicting and preempting storms would save the patients that infections and immunotherapies kill through overreaction.",
 "sig_pointer": "The Signature system's proposed approach predicts the storm's tipping point, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that cytokine storms have detectable tipping points: the inflammatory trajectory's inflection predictable from early mediators - enabling preemptive calming. "
  "Assumptions: (1) tipping points exist; (2) they are detectable early; (3) preemption works. "
  "Reasoning path: a tipping-point model explains variable storm occurrence and predicts preemptive therapy. "
  "Proposed mechanism: 'tipping-point' storm management - early detection triggering calibrated suppression. "
  "What would confirm it: early mediators predicting storms prospectively. "
  "What would kill it: evidence that storms are unpredictable. "
  "What this does not claim: it does not claim storm prediction exists, offers no medical advice, and does not constitute a treatment recommendation."),
 "sig_lens": "The Signature lens reads the storm as a tipping point, and asks what early signals precede it.",
 "how_it_works": "Researchers study cytokine storms through mediator profiling, RECOVERY-style trials, and CAR-T CRS management.",
 "key_points": [
  "Storms kill in sepsis, severe viral infection, and CAR-T.",
  "The protective-to-storm tipping point is unmapped.",
  "Treatments are blunt and partially effective.",
  "Dexamethasone helped in COVID-19.",
  "Management is reactive, not predictive.",
 ],
 "requirements": [
  "Early tipping-point biomarkers.",
  "Preemptive calming proven effective.",
  "Suppression calibrated to preserve defense.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "RECOVERY Collaborative Group. Dexamethasone in COVID-19. NEJM. 2021;384:693-704.",
  "Fajgenbaum DC, June CH. Cytokine storm. NEJM. 2020;383:2255-2273.",
  "Lee DW et al. CAR-T CRS management. Various; 2014-2019.",
  "Sinha P et al. Storm prediction research. Various; 2020-2023.",
 ],
 "demo_data": {"a": ("sepsis deaths involving dysregulated inflammation, percent (approx)", 60.0),
               "b": ("percent scale", 100.0), "bounds": (0.45, 0.75),
               "step1": "three in five sepsis deaths involve the overreaction - the immune system killing its host",
               "confirm": "early mediators predict storms prospectively",
               "refute": "storms prove unpredictable"},
},
# ------------------------------------------------------------------ rank 17
{
 "key": "vaccine-adjuvants",
 "name": "Vaccine Adjuvants: The Science of the Boost",
 "group": "Vaccinology",
 "ladder_rank": 17, "ladder_tier": "compounded",
 "problem": "Adjuvants make vaccines work - but how they work is partly mysterious, and better ones are needed. What's the science of the boost?",
 "description": "Adjuvants (alum, MF59, AS01, CpG) - immune stimulants added to vaccines - are essential for many vaccines, yet their mechanisms were long obscure (alum's mechanism was debated for 90 years). Rational adjuvant design - matching adjuvant to desired response - is the field's goal.",
 "background": "Alum was used empirically since the 1920s; its inflammasome mechanism was clarified in the 2000s. Modern adjuvants (AS01 in Shingrix) show what's possible. Systems vaccinology (Pulendran) maps adjuvant signatures. As of 2026 adjuvant design is becoming rational but remains partly empirical.",
 "why_it_matters": "Better adjuvants mean fewer doses, broader protection, and vaccines for the currently unvaccinable: the lever of vaccinology.",
 "sig_pointer": "The Signature system's proposed approach designs adjuvants rationally, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that adjuvants should be designed by response: the immune profile each vaccine needs dictating the adjuvant - matched deliberately. "
  "Assumptions: (1) adjuvant-response rules are mappable; (2) they are predictable; (3) matching improves vaccines. "
  "Reasoning path: a matching model explains empirical adjuvant history and predicts rational design. "
  "Proposed mechanism: 'response-matched' adjuvant design - deliberate adjuvant selection per vaccine. "
  "What would confirm it: matched adjuvants outperforming empirical ones in trials. "
  "What would kill it: evidence that adjuvant effects are unpredictable. "
  "What this does not claim: it does not claim designed adjuvants exist, offers no medical advice, and does not constitute a vaccine recommendation."),
 "sig_lens": "The Signature lens reads adjuvants as unmapped levers, and asks what deliberate matching would achieve.",
 "how_it_works": "Researchers study adjuvants through systems vaccinology, mechanism research, and rational-design trials.",
 "key_points": [
  "Adjuvants are essential for many vaccines.",
  "Alum's mechanism was debated for 90 years.",
  "AS01 showed modern adjuvants' potential.",
  "Rational design is the goal; empiricism the history.",
  "Matching adjuvant to response is the frontier.",
 ],
 "requirements": [
  "Mapped adjuvant-response rules.",
  "Rationally designed adjuvants in trials.",
  "Superiority to empirical adjuvants.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Pulendran B et al. Systems vaccinology. Various; 2010-2020.",
  "Reed SG et al. Adjuvant development. Various; 2009-2013.",
  "Coffman RL et al. Adjuvant mechanisms. Various; 2010-2017.",
  "Didierlaurent AM et al. AS01 mechanism. Various; 2014-2017.",
 ],
 "demo_data": {"a": ("licensed adjuvants (approx)", 6.0),
               "b": ("vaccines needing better adjuvants (approx)", 30.0), "bounds": (0.12, 0.3),
               "step1": "six adjuvants for thirty needs - the lever with too few settings",
               "confirm": "matched adjuvants outperform empirical ones in trials",
               "refute": "adjuvant effects prove unpredictable"},
},
# ------------------------------------------------------------------ rank 18
{
 "key": "t-cell-exhaustion",
 "name": "T-Cell Exhaustion: Reversing Immune Fatigue",
 "group": "Cancer Immunology",
 "ladder_rank": 18, "ladder_tier": "compounded",
 "problem": "T cells fighting chronic infection and cancer become exhausted - can exhaustion be reversed, or only blocked?",
 "description": "T-cell exhaustion - progressive dysfunction from chronic antigen exposure - limits immunity in cancer and chronic infection. Checkpoint blockade partially reverses it; but the epigenetic programs locking exhaustion in are deep. Whether exhaustion is reversible or only preventable is the key question.",
 "background": "Exhaustion was characterized in LCMV models (Zajac, 1998) and cancer (2000s-2010s); checkpoint blockade's mechanism is partly exhaustion-reversal. Epigenetic studies (2010s-2020s) showed the programs are entrenched. As of 2026 reversal is partial; prevention is the hope.",
 "why_it_matters": "Reversing exhaustion would restore immunity in cancer and chronic infection: the difference between blocking fatigue and curing it.",
 "sig_pointer": "The Signature system's proposed approach reprograms exhausted T cells, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that exhaustion is epigenetically programmed and reprogrammable: the locking marks identified and erased - restoring function. "
  "Assumptions: (1) the programs are mappable; (2) they are erasable; (3) erasure restores function safely. "
  "Reasoning path: a reprogramming model explains partial checkpoint reversal and predicts full restoration. "
  "Proposed mechanism: 'exhaustion-reprogrammed' T cells - epigenetic erasure restoring function. "
  "What would confirm it: reprogrammed cells restoring immunity in trials. "
  "What would kill it: evidence that exhaustion is terminal differentiation. "
  "What this does not claim: it does not claim reprogramming exists, offers no medical advice, and does not constitute a treatment recommendation."),
 "sig_lens": "The Signature lens reads exhaustion as locked programs, and asks what erasure would unlock.",
 "how_it_works": "Researchers study exhaustion through epigenetic mapping, checkpoint-mechanism research, and reprogramming trials.",
 "key_points": [
  "Exhaustion limits immunity in cancer and chronic infection.",
  "Checkpoint blockade partially reverses it.",
  "Epigenetic programs entrench the exhausted state.",
  "Reversal versus prevention is the key question.",
  "Full restoration is unachieved.",
 ],
 "requirements": [
  "Mapped exhaustion programs.",
  "Erasure restoring function in trials.",
  "Safety of reprogrammed cells.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Zajac AJ et al. T-cell exhaustion in LCMV. JEM. 1998;188:2205-2213.",
  "Wherry EJ et al. Exhaustion reviews. Various; 2011-2023.",
  "Pauken KE et al. Epigenetics of exhaustion. Various; 2016-2021.",
  "McLane LM et al. Checkpoint and exhaustion. Various; 2019-2022.",
 ],
 "demo_data": {"a": ("checkpoint responses that are durable, percent (approx)", 25.0),
               "b": ("percent scale", 100.0), "bounds": (0.15, 0.35),
               "step1": "three-quarters of checkpoint responses fade - the exhaustion that blockade can't fully reverse",
               "confirm": "reprogrammed cells restore immunity in trials",
               "refute": "exhaustion proves to be terminal differentiation"},
},
# ------------------------------------------------------------------ rank 19
{
 "key": "nk-cells",
 "name": "NK Cells: The Innate Killers' Untapped Potential",
 "group": "Cell Therapy",
 "ladder_rank": 19, "ladder_tier": "compounded",
 "problem": "Natural killer cells kill tumors without prior sensitization - can they become off-the-shelf cancer therapy?",
 "description": "NK cells - innate lymphocytes killing stressed cells - offer allogeneic (off-the-shelf) therapy potential: no graft-versus-host disease, no prior sensitization needed. But persistence is short, solid-tumor efficacy is unproven, and CAR-NK is early. The field debates whether NK cells can match T-cell therapy.",
 "background": "NK biology was mapped in the 1990s-2000s (KIR, missing-self); CAR-NK trials (Liu, 2020) showed safety and signals in blood cancers. Persistence engineering (IL-15) is active. As of 2026 NK therapy is promising but unproven beyond early trials.",
 "why_it_matters": "Off-the-shelf NK therapy would democratize cell therapy: no patient-specific manufacturing, available immediately.",
 "sig_pointer": "The Signature system's proposed approach engineers NK persistence, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that NK therapy's barrier is persistence: engineering long-lived, tumor-penetrating NK cells - making the off-the-shelf product durable. "
  "Assumptions: (1) persistence is engineerable; (2) engineered cells stay safe; (3) durability brings efficacy. "
  "Reasoning path: a persistence model explains early-trial limits and predicts durable NK therapy. "
  "Proposed mechanism: 'persistence-engineered' NK cells - long-lived off-the-shelf killers. "
  "What would confirm it: engineered NK cells showing durable responses in trials. "
  "What would kill it: evidence that NK cells are intrinsically short-lived. "
  "What this does not claim: it does not claim NK therapy works, offers no medical advice, and does not constitute a treatment recommendation."),
 "sig_lens": "The Signature lens reads NK therapy as persistence-limited, and asks what engineering would extend it.",
 "how_it_works": "Researchers study NK therapy through CAR-NK trials, persistence engineering, and allogeneic safety studies.",
 "key_points": [
  "NK cells kill without prior sensitization.",
  "Allogeneic use avoids graft-versus-host disease.",
  "CAR-NK showed early safety and signals.",
  "Persistence is short; solid-tumor efficacy unproven.",
  "Off-the-shelf potential is the transformative promise.",
 ],
 "requirements": [
  "Persistence-engineered NK cells.",
  "Durable responses in trials.",
  "Solid-tumor efficacy proof.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Liu E et al. CAR-NK trial. NEJM. 2020;382:545-553.",
  "Vivier E et al. NK biology reviews. Various; 2011-2021.",
  "Shimasaki N et al. NK therapy engineering. Various; 2020-2023.",
  "Myers JA, Miller JS. NK therapy reviews. Various; 2021-2023.",
 ],
 "demo_data": {"a": ("CAR-T manufacturing time, weeks (approx)", 3.0),
               "b": ("NK off-the-shelf availability, weeks (approx)", 0.5), "bounds": (4.0, 9.0),
               "step1": "weeks of manufacturing versus immediate availability - the access gap NK could close",
               "confirm": "engineered NK cells show durable responses in trials",
               "refute": "NK cells prove intrinsically short-lived"},
},
# ------------------------------------------------------------------ rank 20
{
 "key": "mucosal-immunity",
 "name": "Mucosal Immunity: Defense at the Gates",
 "group": "Vaccinology",
 "ladder_rank": 20, "ladder_tier": "compounded",
 "problem": "Most pathogens enter through mucosa - yet almost all vaccines are injected systemically. Can mucosal vaccines block infection at entry?",
 "description": "Mucosal immunity (IgA, tissue-resident memory at entry sites) - the defense where pathogens arrive - is poorly induced by injected vaccines. Intranasal and oral vaccines promise sterilizing immunity but face delivery, safety (Bell's palsy with nasal adjuvants), and efficacy hurdles. Only a few mucosal vaccines exist (oral polio, FluMist).",
 "background": "Mucosal immunology matured in the 1990s-2000s; FluMist showed the concept; COVID-19 revived intranasal efforts. Safety scares slowed progress. As of 2026 mucosal vaccines are a promising minority.",
 "why_it_matters": "Mucosal vaccines could block transmission, not just disease: the difference between personal and population protection.",
 "sig_pointer": "The Signature system's proposed approach engineers safe mucosal delivery, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that mucosal vaccines need delivery engineering: safe adjuvants and vectors that induce strong mucosal immunity without the historical safety issues. "
  "Assumptions: (1) safe mucosal adjuvants exist; (2) delivery is engineerable; (3) mucosal immunity blocks transmission. "
  "Reasoning path: a delivery model explains the slow progress and predicts effective mucosal vaccines. "
  "Proposed mechanism: 'delivery-engineered' mucosal vaccines - safe potent mucosal induction. "
  "What would confirm it: mucosal vaccines blocking transmission in trials. "
  "What would kill it: evidence that mucosal immunity can't be safely induced. "
  "What this does not claim: it does not claim mucosal vaccines exist broadly, offers no medical advice, and does not constitute a vaccine recommendation."),
 "sig_lens": "The Signature lens reads the entry-gate gap as delivery-limited, and asks what safe vectors would open it.",
 "how_it_works": "Researchers study mucosal immunity through intranasal trials, adjuvant-safety research, and transmission-blocking studies.",
 "key_points": [
  "Most pathogens enter through mucosa.",
  "Injected vaccines poorly induce mucosal immunity.",
  "Only a few mucosal vaccines exist.",
  "Safety concerns slowed nasal vaccines.",
  "Transmission-blocking is the transformative promise.",
 ],
 "requirements": [
  "Safe potent mucosal adjuvants.",
  "Transmission-blocking proven in trials.",
  "Mucosal vaccines for major pathogens.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Holmgren J, Czerkinsky C. Mucosal immunity. Various; 2005-2021.",
  "Ahmad SM et al. Intranasal COVID vaccines. Various; 2021-2023.",
  "Mestecky J et al. Mucosal vaccine reviews. Various; 2005-2015.",
  "Lavelle EC, Ward RW. Mucosal adjuvants. Various; 2021-2022.",
 ],
 "demo_data": {"a": ("licensed mucosal vaccines (approx)", 5.0),
               "b": ("licensed injected vaccines (approx)", 50.0), "bounds": (0.06, 0.16),
               "step1": "five mucosal of fifty-five vaccines - defending everywhere except where pathogens enter",
               "confirm": "mucosal vaccines block transmission in trials",
               "refute": "mucosal immunity proves unable to be safely induced"},
},
# ------------------------------------------------------------------ rank 21
{
 "key": "immune-repertoire",
 "name": "Mapping the Immune Repertoire",
 "group": "Systems Immunology",
 "ladder_rank": 21, "ladder_tier": "compounded",
 "problem": "Each person carries billions of unique immune receptors - can repertoire sequencing diagnose and predict immune states?",
 "description": "Adaptive immune receptor repertoire (AIRR) sequencing - reading the TCR/BCR diversity - promises diagnostics: infection history, vaccine response, autoimmunity signatures from a blood draw. But the repertoire is astronomically diverse, public clones are few, and clinical validation is early.",
 "background": "High-throughput repertoire sequencing emerged in the 2010s (Robins, Boyd); COVID-19 showed repertoire signatures of infection; Adaptive Biotechnologies commercialized T-cell testing. As of 2026 repertoire diagnostics are emerging with limited clinical use.",
 "why_it_matters": "Repertoire reading would make immune history legible: every infection, every vaccine response, every autoimmune tendency - from one test.",
 "sig_pointer": "The Signature system's proposed approach builds repertoire diagnostics systematically, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that repertoire diagnostics need systematic mapping: disease-associated receptor signatures catalogued across populations - with clinical validation per signature. "
  "Assumptions: (1) signatures exist; (2) they are cataloguable; (3) they validate clinically. "
  "Reasoning path: a mapping model explains early commercialization and predicts clinical repertoire medicine. "
  "Proposed mechanism: 'signature-catalogued' repertoire diagnostics - validated immune-history reading. "
  "What would confirm it: catalogued signatures diagnosing in clinical trials. "
  "What would kill it: evidence that repertoires are too individual for shared signatures. "
  "What this does not claim: it does not claim repertoire diagnostics work broadly, offers no medical advice, and does not constitute a diagnostic recommendation."),
 "sig_lens": "The Signature lens reads the repertoire as an unread medical record, and asks what cataloguing would decipher.",
 "how_it_works": "Researchers study repertoires through AIRR sequencing, signature-discovery cohorts, and clinical-validation trials.",
 "key_points": [
  "Repertoires contain billions of unique receptors.",
  "Disease signatures are discoverable in principle.",
  "COVID-19 showed infection signatures.",
  "Commercial T-cell testing is early.",
  "Clinical validation is limited.",
 ],
 "requirements": [
  "Catalogued validated disease signatures.",
  "Clinical-grade repertoire diagnostics.",
  "Proof of utility beyond research.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Robins H et al. Repertoire sequencing. Various; 2009-2013.",
  "Boyd SD et al. AIRR community. Various; 2015-2020.",
  "Nolan S et al. COVID-19 TCR signatures. Various; 2020-2021.",
  "Greiff V et al. Repertoire diagnostics reviews. Various; 2020-2023.",
 ],
 "demo_data": {"a": ("repertoire-based diagnostics in clinical use (approx)", 2.0),
               "b": ("candidate repertoire signatures published (approx)", 100.0), "bounds": (0.01, 0.04),
               "step1": "two clinical of a hundred candidates - the unread medical record's early pages",
               "confirm": "catalogued signatures diagnose in clinical trials",
               "refute": "repertoires prove too individual for shared signatures"},
},
# ------------------------------------------------------------------ rank 22
{
 "key": "complement",
 "name": "The Complement System's Dark Matter",
 "group": "Innate Immunity",
 "ladder_rank": 22, "ladder_tier": "compounded",
 "problem": "Complement - the ancient cascade - drives diseases from macular degeneration to kidney failure. But its full roles are unmapped.",
 "description": "The complement system - 50+ proteins cascading to kill pathogens - is implicated in AMD, atypical HUS, lupus nephritis, and more. Eculizumab proved complement blockade works; but which diseases are complement-driven, and the system's non-canonical roles (intracellular complosome), are incompletely mapped.",
 "background": "Complement genetics (CFH in AMD, 2005) revealed disease links; eculizumab (2007) proved therapeutic blockade; the complosome (intracellular complement, 2010s) expanded the biology. As of 2026 complement is a proven drug target with unmapped scope.",
 "why_it_matters": "Mapping complement's disease scope would unlock blockbusters for currently untreatable complement-driven diseases.",
 "sig_pointer": "The Signature system's proposed approach maps complement's disease scope, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that complement's disease scope is systematically mappable: genetic, biomarker, and trial evidence per disease - defining where blockade works. "
  "Assumptions: (1) the scope is finite; (2) it is mappable; (3) mapping guides drug development. "
  "Reasoning path: a mapping model explains scattered successes and predicts systematic expansion. "
  "Proposed mechanism: 'scope-mapped' complement therapeutics - blockade matched to proven complement-driven diseases. "
  "What would confirm it: mapped diseases responding to blockade in trials. "
  "What would kill it: evidence that complement's roles are too diffuse for mapping. "
  "What this does not claim: it does not claim complement drives any specific disease, offers no medical advice, and does not constitute a treatment recommendation."),
 "sig_lens": "The Signature lens reads complement as a proven target with unknown scope, and asks what mapping would reveal.",
 "how_it_works": "Researchers study complement through disease-genetics, complosome research, and blockade trials.",
 "key_points": [
  "Complement drives AMD, aHUS, and other diseases.",
  "Eculizumab proved blockade works.",
  "The complosome expanded complement biology intracellularly.",
  "Full disease scope is unmapped.",
  "Non-canonical roles are emerging.",
 ],
 "requirements": [
  "Systematically mapped disease scope.",
  "Blockade trials per mapped disease.",
  "Complosome biology clarified.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Klein RJ et al. CFH and AMD. Science. 2005;308:385-389.",
  "Ricklin D et al. Complement therapeutics. Various; 2010-2018.",
  "Arbore G et al. The complosome. Various; 2016-2020.",
  "Zelek WM et al. Complement disease reviews. Various; 2019-2023.",
 ],
 "demo_data": {"a": ("diseases with approved complement blockers (approx)", 5.0),
               "b": ("diseases with complement evidence (approx)", 50.0), "bounds": (0.06, 0.16),
               "step1": "five treated of fifty implicated - the proven target's unmapped scope",
               "confirm": "mapped diseases respond to blockade in trials",
               "refute": "complement's roles prove too diffuse for mapping"},
},
# ------------------------------------------------------------------ rank 23
{
 "key": "interferon",
 "name": "Interferons: The Double-Edged Sword",
 "group": "Innate Immunity",
 "ladder_rank": 23, "ladder_tier": "compounded",
 "problem": "Interferons fight viruses but drive lupus - how is the same pathway protective in one context and pathogenic in another?",
 "description": "Type I interferons - antiviral alarms - are essential for virus control (COVID-19 showed interferon defects cause severe disease) yet drive lupus and interferonopathies when chronic. The context rules - what makes interferon protective versus pathogenic - are the key unsolved question.",
 "background": "Interferon discovery (1957) launched innate immunology; lupus's interferon signature (2003) revealed the dark side; COVID-19 (2020) showed interferon timing determines outcome. JAK inhibitors modulate the pathway. As of 2026 the context rules remain unmapped.",
 "why_it_matters": "Mastering interferon context would enable antiviral boosting without autoimmune cost: the innate lever.",
 "sig_pointer": "The Signature system's proposed approach maps interferon's context rules, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that interferon's context rules are mappable: timing, tissue, chronicity, and co-signals determining protective versus pathogenic outcomes. "
  "Assumptions: (1) the rules are finite; (2) they are mappable; (3) they are actionable. "
  "Reasoning path: a context model explains the double edge and predicts tuned interferon therapy. "
  "Proposed mechanism: 'context-tuned' interferon therapy - delivering the right signal in the right context. "
  "What would confirm it: context rules predicting outcomes in trials. "
  "What would kill it: evidence that context effects are unpredictable. "
  "What this does not claim: it does not claim interferon therapy is ready, offers no medical advice, and does not constitute a treatment recommendation."),
 "sig_lens": "The Signature lens reads interferon as context-dependent, and asks what rules govern the switch.",
 "how_it_works": "Researchers study interferons through timing studies, lupus-signature research, and JAK-inhibitor trials.",
 "key_points": [
  "Interferons are essential antivirals.",
  "Chronic interferon drives lupus.",
  "COVID-19 showed timing determines outcome.",
  "JAK inhibitors modulate the pathway.",
  "Context rules are unmapped.",
 ],
 "requirements": [
  "Mapped context rules.",
  "Context-tuned therapies in trials.",
  "Antiviral benefit without autoimmune cost.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Isaacs A, Lindenmann J. Interferon discovery. 1957.",
  "Baechler EC et al. Lupus interferon signature. Various; 2003-2006.",
  "Zhang Q et al. Interferon defects in severe COVID-19. Various; 2020-2021.",
  "Crow MK et al. Interferon reviews. Various; 2014-2022.",
 ],
 "demo_data": {"a": ("lupus patients with interferon signature, percent (approx)", 70.0),
               "b": ("percent scale", 100.0), "bounds": (0.55, 0.85),
               "step1": "seven in ten lupus patients carry the antiviral alarm stuck on - the double edge quantified",
               "confirm": "context rules predict outcomes in trials",
               "refute": "context effects prove unpredictable"},
},
# ------------------------------------------------------------------ rank 24
{
 "key": "thymus-regeneration",
 "name": "Thymus Regeneration",
 "group": "Aging",
 "ladder_rank": 24, "ladder_tier": "advanced",
 "problem": "The thymus - where T cells are born - withers with age. Can it be regrown, and would that rejuvenate immunity?",
 "description": "Thymic involution - the organ shrinking from puberty onward - starves the aging immune system of new T cells. Regeneration strategies (IL-7, KGF, FOXN1, sex-steroid ablation, bioengineered thymi) show promise in animals; TRIIM showed human signals. But durable functional regrowth is unproven.",
 "background": "Thymic involution was long accepted as irreversible; sex-steroid ablation (2000s) showed regrowth in animals; FOXN1 reprogramming (2010s) regenerated aged thymi in mice; TRIIM (2019) suggested human thymic regrowth. As of 2026 regeneration is promising but unproven.",
 "why_it_matters": "A regrown thymus would restore naive T-cell production: the fountain of immune youth.",
 "sig_pointer": "The Signature system's proposed approach regenerates the thymus deliberately, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that thymic regeneration is achievable: the developmental programs (FOXN1 and others) reactivated to regrow functional thymic tissue. "
  "Assumptions: (1) the programs are reactivatable; (2) regrowth is functional; (3) it is safe. "
  "Reasoning path: a reactivation model explains animal successes and predicts human regeneration. "
  "Proposed mechanism: 'program-reactivated' thymic regrowth - deliberate developmental reactivation. "
  "What would confirm it: regrown thymi producing naive T cells in trials. "
  "What would kill it: evidence that involution is irreversible. "
  "What this does not claim: it does not claim regeneration exists, offers no medical advice, and does not constitute a treatment recommendation."),
 "sig_lens": "The Signature lens reads the withered thymus as dormant programs, and asks what would reactivate them.",
 "how_it_works": "Researchers study thymic regeneration through FOXN1 research, TRIIM follow-ups, and bioengineering.",
 "key_points": [
  "Thymic involution starves aging immunity of new T cells.",
  "FOXN1 reprogramming regenerated aged mouse thymi.",
  "TRIIM showed human regrowth signals.",
  "IL-7, KGF, and steroid ablation are candidate strategies.",
  "Durable functional regrowth is unproven.",
 ],
 "requirements": [
  "Functional thymic regrowth in humans.",
  "Naive T-cell restoration proven.",
  "Safe durable regeneration protocols.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Boehm T et al. FOXN1 and thymic regeneration. Various; 2014-2020.",
  "Fahy GM et al. TRIIM. Aging Cell. 2019;18:e12973.",
  "Holland AM, van den Brink MRM. Thymic regeneration. Various; 2011-2019.",
  "Lynch HE et al. Thymic involution reviews. Various; 2009-2020.",
 ],
 "demo_data": {"a": ("thymic output at age 60 relative to youth, percent (approx)", 5.0),
               "b": ("percent scale", 100.0), "bounds": (0.02, 0.1),
               "step1": "five percent of youthful T-cell output at sixty - the organ that forgot how to grow",
               "confirm": "regrown thymi produce naive T cells in trials",
               "refute": "involution proves irreversible"},
},
# ------------------------------------------------------------------ rank 25
{
 "key": "vaccines-elderly",
 "name": "Vaccines for the Elderly: Overcoming Immunosenescence",
 "group": "Vaccinology",
 "ladder_rank": 25, "ladder_tier": "advanced",
 "problem": "Vaccines protect the young well and the old poorly - can vaccines be designed for aging immune systems?",
 "description": "Elderly vaccine responses are blunted: flu, COVID-19, and shingles vaccines work less well with age. High-dose, adjuvanted (Fluad), and recombinant (Shingrix) formulations help; but the fundamental problem - aged immune systems respond poorly - needs vaccines designed for senescence.",
 "background": "High-dose flu vaccine (2009) and adjuvanted vaccines improved elderly protection; Shingrix (2017) showed strong efficacy in the old. But most vaccines remain young-optimized. As of 2026 elderly vaccinology is adapted, not designed.",
 "why_it_matters": "The elderly bear infectious-disease mortality: vaccines designed for them would save the most vulnerable.",
 "sig_pointer": "The Signature system's proposed approach designs vaccines for aged immunity, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that elderly vaccines should be designed from aged immunology: the response defects mapped and formulations engineered to overcome them. "
  "Assumptions: (1) the defects are mappable; (2) they are overcomeable; (3) designed vaccines work. "
  "Reasoning path: a defect-targeted model explains adapted-vaccine limits and predicts designed elderly vaccines. "
  "Proposed mechanism: 'senescence-designed' vaccines - formulations for aged immune systems. "
  "What would confirm it: designed vaccines beating adapted ones in elderly trials. "
  "What would kill it: evidence that aged responses can't be improved. "
  "What this does not claim: it does not claim designed vaccines exist, offers no medical advice, and does not constitute a vaccine recommendation."),
 "sig_lens": "The Signature lens reads elderly vaccines as young designs in old bodies, and asks what aged-immunology design would do.",
 "how_it_works": "Researchers study elderly vaccines through high-dose/adjuvanted trials, Shingrix follow-ups, and senescence-immunology research.",
 "key_points": [
  "Elderly vaccine responses are substantially blunted.",
  "High-dose and adjuvanted formulations help.",
  "Shingrix showed strong elderly efficacy.",
  "Most vaccines remain young-optimized.",
  "Fundamental senescence defects are unaddressed.",
 ],
 "requirements": [
  "Mapped elderly response defects.",
  "Designed vaccines beating adapted ones.",
  "Protection matching young-adult levels.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "DiazGranados CA et al. High-dose flu vaccine. NEJM. 2014;371:635-645.",
  "Cunningham AL et al. Shingrix trials. NEJM. 2016;375:1019-1032.",
  "Weinberger B et al. Elderly vaccinology. Various; 2008-2020.",
  "Crooke SN et al. Vaccine senescence reviews. Various; 2019-2022.",
 ],
 "demo_data": {"a": ("Shingrix efficacy in the elderly, percent (approx)", 90.0),
               "b": ("percent scale", 100.0), "bounds": (0.8, 0.98),
               "step1": "ninety percent efficacy proves elderly protection is possible - the exception that should be the rule",
               "confirm": "designed vaccines beat adapted ones in elderly trials",
               "refute": "aged responses prove unable to be improved"},
},
# ------------------------------------------------------------------ rank 26
{
 "key": "pandemic-vaccines",
 "name": "Pandemic Vaccines in 100 Days",
 "group": "Vaccinology",
 "ladder_rank": 26, "ladder_tier": "advanced",
 "problem": "COVID-19 vaccines took a year - the goal is 100 days. Can platform vaccinology deliver pandemic vaccines at pandemic speed?",
 "description": "The 100-day mission - vaccines against a novel pathogen within 100 days - needs platform technologies (mRNA, viral vectors), pre-made prototype vaccines, and streamlined trials. COVID-19 proved platforms work; but the regulatory, manufacturing, and trial infrastructure for 100-day delivery is incomplete.",
 "background": "CEPI's 100-day mission (2022) set the goal; COVID-19's year-long timeline was the baseline; prototype-pathogen approaches are in development. As of 2026 the platforms exist but the system doesn't.",
 "why_it_matters": "The next pandemic's toll depends on vaccine speed: 100-day delivery would save millions.",
 "sig_pointer": "The Signature system's proposed approach builds the 100-day system, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that 100-day vaccines need pre-built systems: prototype vaccines per viral family, warm manufacturing, and pre-agreed trial protocols - ready before the pathogen. "
  "Assumptions: (1) prototype approaches generalize; (2) systems can be pre-built; (3) regulators will accept. "
  "Reasoning path: a pre-built model explains COVID-19's timeline and predicts 100-day delivery. "
  "Proposed mechanism: 'pre-built' pandemic vaccinology - platforms, prototypes, and protocols ready. "
  "What would confirm it: a 100-day vaccine in the next pandemic. "
  "What would kill it: evidence that novel pathogens defeat prototypes. "
  "What this does not claim: it does not claim 100-day vaccines exist, offers no medical advice, and does not constitute a policy recommendation."),
 "sig_lens": "The Signature lens reads pandemic speed as pre-built systems, and asks what readiness would deliver.",
 "how_it_works": "Researchers study pandemic vaccinology through prototype-pathogen research, CEPI programs, and platform trials.",
 "key_points": [
  "COVID-19 vaccines took about a year.",
  "The 100-day mission is CEPI's goal.",
  "mRNA platforms proved rapid development possible.",
  "Prototype vaccines per viral family are in development.",
  "The system - not the science - is the bottleneck.",
 ],
 "requirements": [
  "Prototype vaccines for major viral families.",
  "Warm manufacturing capacity.",
  "Pre-agreed trial and regulatory protocols.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "CEPI. 100-day mission. 2022.",
  "Graham BS et al. Prototype pathogen approach. Various; 2018-2021.",
  "Krammer F et al. Pandemic platform reviews. Various; 2020-2023.",
  "Saville M et al. CEPI strategy. Various; 2022-2024.",
 ],
 "demo_data": {"a": ("COVID-19 vaccine timeline, days (approx)", 350.0),
               "b": ("100-day mission target, days", 100.0), "bounds": (2.5, 5.0),
               "step1": "three-and-a-half times the target - the gap the next pandemic must close",
               "confirm": "a 100-day vaccine in the next pandemic",
               "refute": "novel pathogens prove to defeat prototypes"},
},
# ------------------------------------------------------------------ rank 27
{
 "key": "tuberculosis-vaccine",
 "name": "A Better Tuberculosis Vaccine",
 "group": "Vaccinology",
 "ladder_rank": 27, "ladder_tier": "advanced",
 "problem": "BCG is a century old and unreliable against adult TB - why is a better tuberculosis vaccine so hard, and what would work?",
 "description": "Tuberculosis - the top infectious killer - has only BCG: effective in children, unreliable against adult pulmonary TB. M72/AS01E (2019) showed 50% efficacy - the first positive adult TB trial. Correlates of protection are unknown; the field advances slowly.",
 "background": "BCG (1921) is the oldest widely used vaccine; its adult failure was long known. M72's phase 2b success (2019) was the breakthrough; correlates research is active. As of 2026 no licensed adult TB vaccine exists.",
 "why_it_matters": "TB kills over a million yearly: an effective adult vaccine would be the biggest infectious-disease advance in decades.",
 "sig_pointer": "The Signature system's proposed approach finds TB's correlates of protection, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that TB vaccine progress needs correlates of protection: the immune responses that prevent TB identified - enabling rational vaccine design. "
  "Assumptions: (1) correlates exist; (2) they are identifiable; (3) they guide design. "
  "Reasoning path: a correlates model explains slow progress and predicts rational TB vaccines. "
  "Proposed mechanism: 'correlates-driven' TB vaccinology - design guided by protection markers. "
  "What would confirm it: correlates predicting efficacy in trials. "
  "What would kill it: evidence that protection has no measurable correlate. "
  "What this does not claim: it does not claim a TB vaccine exists, offers no medical advice, and does not constitute a vaccine recommendation."),
 "sig_lens": "The Signature lens reads TB vaccinology as correlate-blind, and asks what protection markers would guide.",
 "how_it_works": "Researchers study TB vaccines through M72 follow-ups, correlates research, and BCG-revaccination trials.",
 "key_points": [
  "BCG is a century old; unreliable against adult TB.",
  "M72/AS01E showed 50% efficacy - the first positive signal.",
  "Correlates of protection are unknown.",
  "TB kills over a million yearly.",
  "No licensed adult TB vaccine exists.",
 ],
 "requirements": [
  "Identified correlates of protection.",
  "Correlates-driven vaccine design.",
  "Licensed effective adult TB vaccine.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Tait DR et al. M72/AS01E trial. NEJM. 2019;381:2429-2439.",
  "Andersen P, Scriba TJ. TB vaccine reviews. Various; 2019-2023.",
  "Vekemans J et al. BCG history and limits. Various; 2019-2021.",
  "Scriba TJ et al. Correlates research. Various; 2020-2023.",
 ],
 "demo_data": {"a": ("M72 efficacy, percent (approx)", 50.0),
               "b": ("percent scale", 100.0), "bounds": (0.35, 0.65),
               "step1": "fifty percent - the first real hope after a century of BCG",
               "confirm": "correlates predict efficacy in trials",
               "refute": "protection proves to have no measurable correlate"},
},
# ------------------------------------------------------------------ rank 28
{
 "key": "malaria-vaccine",
 "name": "Malaria Vaccines That Last",
 "group": "Vaccinology",
 "ladder_rank": 28, "ladder_tier": "advanced",
 "problem": "RTS,S and R21 protect against malaria - but efficacy wanes. Can a durable malaria vaccine be built?",
 "description": "Malaria vaccines RTS,S (2021 WHO recommendation) and R21 (2023) show 60-75% efficacy - but protection wanes within years. The parasite's complexity (lifecycle stages, antigenic variation) defeats durable immunity; natural immunity takes years of exposure. Next-generation vaccines target multiple stages.",
 "background": "RTS,S took 30 years of development; R21 improved on it; WHO recommended both. Durability is the shared weakness. Whole-sporozoite approaches (PfSPZ) aim higher. As of 2026 malaria vaccinology has working but waning tools.",
 "why_it_matters": "Malaria kills 600,000+ yearly, mostly children: durable vaccines would end one of humanity's oldest scourges.",
 "sig_pointer": "The Signature system's proposed approach builds durable multi-stage malaria immunity, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that durable malaria protection needs multi-stage immunity: pre-erythrocytic plus blood-stage plus transmission-blocking - with durability engineered. "
  "Assumptions: (1) multi-stage immunity is achievable; (2) durability is engineerable; (3) combinations work. "
  "Reasoning path: a multi-stage model explains waning single-stage protection and predicts durable vaccines. "
  "Proposed mechanism: 'multi-stage durable' malaria vaccines - combined lifecycle targeting. "
  "What would confirm it: multi-stage vaccines showing durable protection. "
  "What would kill it: evidence that the parasite defeats all durable immunity. "
  "What this does not claim: it does not claim durable vaccines exist, offers no medical advice, and does not constitute a vaccine recommendation."),
 "sig_lens": "The Signature lens reads waning protection as single-stage limits, and asks what multi-stage immunity would sustain.",
 "how_it_works": "Researchers study malaria vaccines through R21 rollout, PfSPZ trials, and multi-stage combination research.",
 "key_points": [
  "RTS,S and R21 show 60-75% efficacy.",
  "Protection wanes within years.",
  "The parasite's complexity defeats durable immunity.",
  "Natural immunity takes years of exposure.",
  "Multi-stage approaches are the next generation.",
 ],
 "requirements": [
  "Multi-stage vaccines with durable protection.",
  "Efficacy sustained beyond current waning.",
  "Deployment at malaria-burden scale.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "RTS,S Clinical Trials Partnership. Various; 2011-2021.",
  "Datoo MS et al. R21 trial. Lancet. 2021;397:1809-1818.",
  "WHO. Malaria vaccine recommendations. 2021, 2023.",
  "Crompton PD et al. Malaria immunity reviews. Various; 2014-2022.",
 ],
 "demo_data": {"a": ("R21 efficacy, percent (approx)", 70.0),
               "b": ("percent scale", 100.0), "bounds": (0.55, 0.85),
               "step1": "seventy percent that fades - the best malaria vaccine still needs durability",
               "confirm": "multi-stage vaccines show durable protection",
               "refute": "the parasite proves to defeat all durable immunity"},
},
# ------------------------------------------------------------------ rank 29
{
 "key": "cancer-vaccines",
 "name": "Therapeutic Cancer Vaccines",
 "group": "Cancer Immunology",
 "ladder_rank": 29, "ladder_tier": "advanced",
 "problem": "Preventive vaccines work; therapeutic cancer vaccines mostly failed - can personalized neoantigen vaccines finally succeed?",
 "description": "Therapeutic cancer vaccines - treating existing cancer by vaccination - failed for decades (one approved: Provenge, marginal benefit). Personalized neoantigen vaccines (mRNA, peptide) plus checkpoint blockade show early promise (Moderna/Merck melanoma data, 2022-2023). Whether they become standard care is the open question.",
 "background": "Cancer-vaccine failures accumulated through the 2000s-2010s; Provenge (2010) was approved with tiny benefit. Neoantigen personalization (2010s) plus mRNA platforms renewed the field. Early combination data is promising. As of 2026 therapeutic cancer vaccines are in clinical testing, not practice.",
 "why_it_matters": "Working therapeutic vaccines would make cancer treatment preventive-personalized: the immunotherapy endgame.",
 "sig_pointer": "The Signature system's proposed approach makes neoantigen vaccines standard, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that therapeutic cancer vaccines need neoantigen-plus-checkpoint standardization: personalized vaccines with checkpoint blockade as routine combination - proven indication by indication. "
  "Assumptions: (1) neoantigens are the right targets; (2) combinations are needed; (3) manufacturing scales. "
  "Reasoning path: a combination model explains historical failures and predicts clinical success. "
  "Proposed mechanism: 'neoantigen-standard' cancer care - personalized vaccines as routine. "
  "What would confirm it: phase 3 wins for neoantigen-checkpoint combinations. "
  "What would kill it: evidence that established tumors resist vaccination. "
  "What this does not claim: it does not claim cancer vaccines work, offers no medical advice, and does not constitute a treatment recommendation."),
 "sig_lens": "The Signature lens reads the failures as wrong targets and solo therapy, and asks what personalized combinations would achieve.",
 "how_it_works": "Researchers study cancer vaccines through neoantigen trials, mRNA platform studies, and combination research.",
 "key_points": [
  "Decades of therapeutic cancer vaccines failed.",
  "Provenge was approved with marginal benefit.",
  "Neoantigen personalization renewed the field.",
  "Early mRNA-checkpoint combination data is promising.",
  "Phase 3 proof is pending.",
 ],
 "requirements": [
  "Phase 3 combination wins.",
  "Scalable personalized manufacturing.",
  "Standard-care adoption per indication.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Kantoff PW et al. Provenge trial. NEJM. 2010;363:411-422.",
  "Sahin U et al. Neoantigen vaccines. Various; 2017-2021.",
  "Moderna/Merck. mRNA-4157 melanoma data. 2022-2023.",
  "Blass E, Ott PA. Cancer vaccine reviews. Various; 2021-2023.",
 ],
 "demo_data": {"a": ("therapeutic cancer vaccines approved with major benefit", 0.5),
               "b": ("therapeutic cancer vaccine trials (approx hundreds)", 200.0), "bounds": (0.001, 0.005),
               "step1": "two hundred trials, zero major-benefit approvals - the field's long defeat, possibly ending",
               "confirm": "phase 3 wins for neoantigen-checkpoint combinations",
               "refute": "established tumors prove resistant to vaccination"},
},
# ------------------------------------------------------------------ rank 30
{
 "key": "systems-immunology",
 "name": "Systems Immunology: Predicting Immune Responses",
 "group": "Systems Immunology",
 "ladder_rank": 30, "ladder_tier": "advanced",
 "problem": "The immune system is the body's most complex - can it be modeled well enough to predict vaccine and treatment responses?",
 "description": "Systems immunology - computational modeling of immune responses - promises prediction: who responds to vaccines, who gets autoimmunity, who benefits from immunotherapy. But the system's complexity (cell types, signals, timescales) challenges modeling; predictions are early-stage.",
 "background": "Systems vaccinology (Pulendran, 2010s) predicted vaccine responses from early signatures; the Human Immunology Project Consortium built data resources. Machine-learning approaches are growing. As of 2026 prediction is promising but not clinical.",
 "why_it_matters": "Predictive immunology would personalize all immune interventions: the computational foundation of the field's future.",
 "sig_pointer": "The Signature system's proposed approach builds predictive immune models, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that immune prediction needs multi-scale models: molecular, cellular, and organismal data integrated - validated against real response outcomes. "
  "Assumptions: (1) the system is modelable; (2) multi-scale integration works; (3) predictions validate. "
  "Reasoning path: a modeling approach explains early successes and predicts clinical prediction. "
  "Proposed mechanism: 'multi-scale' immune prediction - integrated models guiding interventions. "
  "What would confirm it: models predicting responses in prospective trials. "
  "What would kill it: evidence that immune complexity defeats modeling. "
  "What this does not claim: it does not claim predictive models exist, offers no medical advice, and does not constitute a methodological recommendation."),
 "sig_lens": "The Signature lens reads immunity as modelable complexity, and asks what multi-scale integration would predict.",
 "how_it_works": "Researchers study systems immunology through HIPC data, vaccine-signature prediction, and machine-learning models.",
 "key_points": [
  "Systems vaccinology predicted responses from early signatures.",
  "The immune system's complexity challenges modeling.",
  "Multi-scale integration is the goal.",
  "Predictions are promising but not clinical.",
  "Personalized immune intervention is the prize.",
 ],
 "requirements": [
  "Multi-scale validated models.",
  "Prospective prediction trials.",
  "Clinical deployment of predictions.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Pulendran B et al. Systems vaccinology. Various; 2010-2020.",
  "HIPC. Human Immunology Project Consortium. Various; 2012-2022.",
  "Davis MM et al. Systems immunology reviews. Various; 2008-2020.",
  "Tsang JS et al. Immune prediction models. Various; 2014-2022.",
 ],
 "demo_data": {"a": ("immune-response predictions in clinical use (approx)", 2.0),
               "b": ("immune interventions needing prediction (approx)", 50.0), "bounds": (0.02, 0.08),
               "step1": "two predictions clinical of fifty needed - the modelable system's early map",
               "confirm": "models predict responses in prospective trials",
               "refute": "immune complexity proves to defeat modeling"},
},
# ------------------------------------------------------------------ rank 31
{
 "key": "sex-differences",
 "name": "Sex Differences in Immunity",
 "group": "Systems Immunology",
 "ladder_rank": 31, "ladder_tier": "advanced",
 "problem": "Women get more autoimmunity; men die more of infection - why does sex shape immunity so profoundly, and should medicine account for it?",
 "description": "Sex differences in immunity are profound: females mount stronger responses (more autoimmunity, better vaccine responses), males suffer worse infections. X-chromosome immune genes, hormones, and microbiome differences all contribute. But sex-stratified medicine is rare; most trials ignore sex.",
 "background": "The female autoimmune bias was long known; X-chromosome dosage (TLR7 and lupus, 2020s) provided mechanisms; COVID-19's male bias revived attention. As of 2026 sex-aware immunology is advocated more than practiced.",
 "why_it_matters": "Sex-aware dosing and treatment would improve outcomes for everyone: half the population is systematically under-served by unisex medicine.",
 "sig_pointer": "The Signature system's proposed approach builds sex-aware immunology, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that immunology should be sex-aware: dosing, vaccine schedules, and treatment thresholds stratified by sex - based on mapped mechanisms. "
  "Assumptions: (1) the mechanisms are mappable; (2) stratification improves outcomes; (3) medicine will adopt. "
  "Reasoning path: a sex-aware model explains differential outcomes and predicts better medicine. "
  "Proposed mechanism: 'sex-stratified' immune medicine - sex-aware protocols. "
  "What would confirm it: stratified protocols improving outcomes in trials. "
  "What would kill it: evidence that sex differences don't affect treatment outcomes. "
  "What this does not claim: it does not claim sex-specific treatments exist, offers no medical advice, and does not constitute a treatment recommendation."),
 "sig_lens": "The Signature lens reads unisex immunology as ignoring half the biology, and asks what stratification would improve.",
 "how_it_works": "Researchers study sex differences through X-chromosome research, hormone studies, and sex-stratified trial analyses.",
 "key_points": [
  "Females: stronger responses, more autoimmunity.",
  "Males: worse infection outcomes.",
  "X-chromosome genes (TLR7) explain part of lupus bias.",
  "Most trials ignore sex.",
  "Sex-aware medicine is advocated, rarely practiced.",
 ],
 "requirements": [
  "Mapped sex-difference mechanisms.",
  "Sex-stratified protocols in trials.",
  "Outcome improvements from stratification.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Klein SL, Flanagan KL. Sex differences in immunity. Various; 2016-2022.",
  "Souyris M et al. TLR7 and lupus sex bias. Various; 2018-2023.",
  "Takahashi T et al. COVID-19 sex differences. Various; 2020-2021.",
  "Gubbels Bupp MR. Sex-aware medicine reviews. Various; 2021-2023.",
 ],
 "demo_data": {"a": ("autoimmune patients who are female, percent (approx)", 80.0),
               "b": ("percent scale", 100.0), "bounds": (0.65, 0.95),
               "step1": "four in five autoimmune patients are women - the bias unisex medicine ignores",
               "confirm": "stratified protocols improve outcomes in trials",
               "refute": "sex differences prove not to affect treatment outcomes"},
},
# ------------------------------------------------------------------ rank 32
{
 "key": "neuroimmune",
 "name": "Neuroimmune Crosstalk",
 "group": "Systems Immunology",
 "ladder_rank": 32, "ladder_tier": "advanced",
 "problem": "The nervous and immune systems talk constantly - but the conversation's grammar is unmapped. What does neuroimmune crosstalk control?",
 "description": "Neuroimmune crosstalk - vagus-nerve inflammatory reflexes, microglial pruning, sickness behavior, stress-immune links - connects brain and immunity. The inflammatory reflex (Tracey) enables bioelectronic medicine; but the full map of neural immune control is unknown.",
 "background": "The inflammatory reflex (Tracey, 2000s) showed vagus control of inflammation; microglia research revealed brain-immune integration; sickness behavior linked cytokines to mood. Bioelectronic trials are early. As of 2026 the crosstalk is acknowledged with the grammar unmapped.",
 "why_it_matters": "Mastering neuroimmune control would enable treating inflammation with electricity: bioelectronic medicine's foundation.",
 "sig_pointer": "The Signature system's proposed approach maps neuroimmune grammar, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that neuroimmune crosstalk has mappable grammar: the neural signals controlling specific immune functions - identified systematically. "
  "Assumptions: (1) the grammar is finite; (2) it is mappable; (3) it is therapeutically usable. "
  "Reasoning path: a grammar model explains scattered findings and predicts bioelectronic therapies. "
  "Proposed mechanism: 'grammar-mapped' neuroimmune therapy - neural control of immunity. "
  "What would confirm it: mapped signals controlling immunity in trials. "
  "What would kill it: evidence that the crosstalk is too diffuse for mapping. "
  "What this does not claim: it does not claim bioelectronic therapies work broadly, offers no medical advice, and does not constitute a treatment recommendation."),
 "sig_lens": "The Signature lens reads the crosstalk as unmapped language, and asks what grammar would translate it.",
 "how_it_works": "Researchers study neuroimmune crosstalk through vagus-stimulation trials, microglia research, and reflex mapping.",
 "key_points": [
  "The vagus nerve controls inflammation reflexively.",
  "Microglia integrate brain and immune function.",
  "Sickness behavior links cytokines to mood.",
  "Bioelectronic medicine is early-stage.",
  "The control grammar is unmapped.",
 ],
 "requirements": [
  "Mapped neuroimmune grammar.",
  "Bioelectronic therapies in trials.",
  "Neural control of specific immune functions.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Tracey KJ. The inflammatory reflex. Various; 2002-2016.",
  "Pavlov VA, Tracey KJ. Bioelectronic medicine. Various; 2012-2022.",
  "Dantzer R et al. Sickness behavior. Various; 2008-2018.",
  "Schafer DP, Stevens B. Microglia reviews. Various; 2013-2020.",
 ],
 "demo_data": {"a": ("bioelectronic anti-inflammatory therapies approved", 0.5),
               "b": ("inflammatory diseases potentially treatable (approx)", 30.0), "bounds": (0.008, 0.025),
               "step1": "zero approved for thirty candidates - the unmapped grammar's therapeutic gap",
               "confirm": "mapped signals control immunity in trials",
               "refute": "the crosstalk proves too diffuse for mapping"},
},
# ------------------------------------------------------------------ rank 33
{
 "key": "immune-theory",
 "name": "A Unified Theory of Immunity",
 "group": "Theory",
 "ladder_rank": 33, "ladder_tier": "advanced",
 "problem": "Immunology has models - clonal selection, danger, discontinuity - but no unified theory. Can the immune system's logic be fully formalized?",
 "description": "Immunology's theoretical frameworks compete: self/non-self, danger, discontinuity, and systems models each explain part. No unified theory predicts immune behavior across contexts. Whether the immune system has a formalizable logic - or is evolved complexity resisting theory - is the discipline's deepest question.",
 "background": "Burnet's clonal selection (1957) was the last near-unified theory; subsequent frameworks fragmented the field. Mathematical immunology grew without unifying. As of 2026 immunology is data-rich and theory-poor.",
 "why_it_matters": "A unified theory would make immunology predictive: designing immunity rather than discovering it.",
 "sig_pointer": "The Signature system's proposed approach formalizes immune logic computationally, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that immune logic is formalizable: the decision rules (tolerate, attack, remember) expressed computationally - with competing frameworks as special cases. "
  "Assumptions: (1) the logic is finite; (2) it is formalizable; (3) formalization predicts. "
  "Reasoning path: a formalization model explains framework fragmentation and predicts theoretical unity. "
  "Proposed mechanism: 'formalized' immune theory - computational models unifying frameworks. "
  "What would confirm it: formal models predicting immune behavior across contexts. "
  "What would kill it: evidence that immunity resists formalization. "
  "What this does not claim: it does not claim a unified theory exists, offers no medical advice, and does not constitute a methodological recommendation."),
 "sig_lens": "The Signature lens reads the frameworks as partial logics, and asks what formalization would unify.",
 "how_it_works": "Researchers study immune theory through mathematical modeling, framework comparisons, and predictive testing.",
 "key_points": [
  "Competing frameworks each explain part of immunity.",
  "No unified theory predicts across contexts.",
  "Clonal selection was the last near-unified theory.",
  "Mathematical immunology grew without unifying.",
  "Theory poverty amid data abundance defines the field.",
 ],
 "requirements": [
  "Formalized immune decision logic.",
  "Predictions across contexts.",
  "Unification of competing frameworks.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Burnet FM. Clonal selection. 1957.",
  "Matzinger P. Danger model. 1994.",
  "Pradeu T et al. Discontinuity theory. Various; 2012-2019.",
  "Perelson AS et al. Mathematical immunology. Various; 1997-2020.",
 ],
 "demo_data": {"a": ("unified immune theories with predictive success", 0.5),
               "b": ("competing frameworks (approx)", 5.0), "bounds": (0.05, 0.2),
               "step1": "five frameworks, zero unified theories - the logic nobody formalized",
               "confirm": "formal models predict immune behavior across contexts",
               "refute": "immunity proves resistant to formalization"},
},
# ------------------------------------------------------------------ rank 34
{
 "key": "immune-consciousness",
 "name": "The Immune Self: Immunology's Deepest Question",
 "group": "Theory",
 "ladder_rank": 34, "ladder_tier": "advanced",
 "problem": "The immune system defines the biological self - but what is the self it defends? Immunology's deepest question is philosophical.",
 "description": "The immune 'self' - the identity the system defends - is immunology's foundational concept and its least examined: self changes (pregnancy, chimerism, microbiome), yet the system adapts. Understanding immune identity would reframe autoimmunity, tolerance, and the organism itself.",
 "background": "The self concept dates to Burnet; pregnancy's tolerance paradox challenged it; chimerism and microbiome integration complicated it further. Philosophers of immunology (Pradeu, 2010s) formalized the questions. As of 2026 the immune self remains conceptually unresolved.",
 "why_it_matters": "The immune self defines the organism: resolving it reframes medicine's most basic category - what counts as the body.",
 "sig_pointer": "The Signature system's proposed approach defines the immune self dynamically, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that the immune self is dynamic: a continuously renegotiated boundary - definable as the set of entities the system has learned to tolerate. "
  "Assumptions: (1) the self is definable operationally; (2) it is measurable; (3) definition guides therapy. "
  "Reasoning path: a dynamic model explains pregnancy, chimerism, and microbiome tolerance - predicting self-based medicine. "
  "Proposed mechanism: 'self-defined' immunology - therapies based on measured immune identity. "
  "What would confirm it: measured self-boundaries predicting tolerance outcomes. "
  "What would kill it: evidence that the self is indefinable. "
  "What this does not claim: it does not claim the self is defined, offers no medical advice, and does not constitute a philosophical conclusion."),
 "sig_lens": "The Signature lens reads the self as renegotiated, not given, and asks what measurement would define it.",
 "how_it_works": "Researchers study the immune self through chimerism research, pregnancy-tolerance studies, and philosophy of immunology.",
 "key_points": [
  "The immune self is the field's foundational unexamined concept.",
  "Pregnancy, chimerism, and microbiome challenge static self.",
  "Philosophers formalized the questions (Pradeu).",
  "Dynamic self explains tolerance paradoxes.",
  "The concept remains unresolved.",
 ],
 "requirements": [
  "Operational definition of the immune self.",
  "Measured self-boundaries.",
  "Self-based therapeutic strategies.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Pradeu T. The Limits of the Self. Oxford University Press; 2012.",
  "Burnet FM. Self concepts. Various; 1957-1969.",
  "Rowe JH et al. Pregnancy tolerance. Various; 2012-2020.",
  "Starzl TE et al. Chimerism and tolerance. Various; 1993-2010.",
 ],
 "demo_data": {"a": ("pregnancies tolerated despite half-foreign fetus (approx)", 100.0),
               "b": ("percent scale", 100.0), "bounds": (0.9, 1.1),
               "step1": "every pregnancy tolerates the half-foreign - the self paradox in every birth",
               "confirm": "measured self-boundaries predict tolerance outcomes",
               "refute": "the self proves indefinable"},
},
]
