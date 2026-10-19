#!/usr/bin/env python3
"""Entries for The Unsolved Toxicology Database (unsolved-toxicology) and its
Signature half (unsolved-toxicology-signature).

34 famous unsolved problems in toxicology, ladder-ordered by accessibility
(rank 1 = most approachable, rank 34 = most complex/compounded).
Public half: real, fact-checked problems. Signature half: the same 34
through the Signature lens, ALWAYS labeled as proposals, never established
science.

SAFETY: all dose-response demonstrations use abstract "compound X" with
arbitrary units - no real substances, no harmful dosages, no instructions
facilitating harm.

ID prefixes JAH-USTO- / JAH-USTOS- verified free in manifest id_prefix
values (exact + substring, both directions).
"""

LABEL = "Signature-generated proposed solution \u2014 not established science."

FIELD = {
 "tag": "toxicology",
 "disp": "toxicology",
 "name": "The Unsolved Toxicology Database",
 "sig_name": "The Unsolved Toxicology Signature Database",
 "prefix": "JAH-USTO-",
 "sig_prefix": "JAH-USTOS-",
 "ai": "JAH Unsolved Toxicology Archivist",
 "tagline": ("Thirty-four famous open problems in toxicology, from dose-response to the exposome: real, "
             "fact-checked, each with its full story and a clearly labeled Signature proposed solution."),
 "sig_tagline": ("His original Signature solution method applied to all 34 great open problems of toxicology: "
                 "Signature-generated proposed solutions with assumptions declared, confirm and refute conditions "
                 "stated, and limits honestly marked. Clearly labeled Signature-made, never established science."),
 "pub_line": ("Public records - 34 famous open problems in toxicology, real and fact-checked: dose-response "
              "extrapolation, mixture toxicity, endocrine disruption, developmental toxicity, carcinogen "
              "classification, genotoxicity testing, skin sensitization, eye irritation alternatives, acute "
              "toxicity replacement, bioaccumulation, and PBT assessment - every record carrying the problem "
              "statement, background, why it matters, key points, requirements, standards, citations, and a "
              "working solution-explorer demonstration (abstract compound X, arbitrary units), organized in the "
              "Signature system."),
 "sig_line": ("Signature originals - his original Signature solution method: the same 34 famous unsolved "
              "toxicology problems approached as a covenant between the known and the unknown, each carrying "
              "the full Signature-generated proposed solution with its assumptions declared, its confirm and "
              "refute conditions stated, and its limits honestly marked. Clearly labeled Signature-made, never "
              "presented as established science or authentic public record."),
 "ladder_text": (" Records are ordered by the teaching ladder: Foundations (dose-response, mixture toxicity, "
                 "endocrine disruption, developmental toxicity, carcinogen classification, genotoxicity, skin "
                 "sensitization, eye irritation alternatives, acute toxicity replacement, bioaccumulation, PBT "
                 "assessment) -> Compounded (adverse outcome pathways, read-across, QSAR domains, in-vitro to "
                 "in-vivo extrapolation, PBPK modeling, nanomaterials, microplastics, PFAS, pesticide mixtures, "
                 "metal speciation, air mixtures, water mixtures) -> Advanced (exposome, gene-environment, "
                 "epigenetic toxicity, transgenerational effects, microbiome, immunotoxicity, "
                 "neurodevelopmental toxicity, endocrine screening, new approach methodologies, risk uncertainty, "
                 "unified toxicology)."),
 "search_ph": ("Search dose-response, mixtures, endocrine disruptors, PFAS, nanomaterials, exposome, risk "
               "assessment..."),
 "chat_ph": "Ask about the great open problems of toxicology...",
 "greet_pub": ("I am the JAH Unsolved Toxicology Archivist. Ask me about the great open problems of toxicology - "
               "from dose-response, mixtures, and endocrine disruption through nanomaterials and PFAS, to the "
               "exposome, new methodologies, and unified toxicology."),
 "greet_sig": ("I am the JAH Unsolved Toxicology Archivist (Signature). Ask me about the Signature proposed "
               "solutions to the great open problems of toxicology - every approach labeled as a proposal, "
               "never established science."),
 "role_pub": ("unsolved toxicology archivist - the great open problems of toxicology, from dose-response, "
              "mixtures, and endocrine disruption through nanomaterials and PFAS, to the exposome, new "
              "methodologies, and unified toxicology; teaches progressively along the ladder from foundations "
              "through compounded to advanced; answers from many angles - definition, example, analogy, "
              "application, history, math - using only archive data from this system"),
 "role_sig": ("unsolved toxicology archivist - Signature editions: his original Signature solution method "
              "applied to the 34 great open problems of toxicology, each carrying the full Signature-generated "
              "proposed solution, clearly labeled Signature-made and never presented as established science; "
              "teaches progressively along the ladder from foundations through compounded to advanced; answers "
              "from many angles - definition, example, analogy, application, history, math - using only archive "
              "data from this system"),
 "gen_desc": "Generate clearly-labeled unsolved toxicology studies. Seeded archive records are the authoritative entries.",
 "standards": [
  "Problem statements verified against the published literature; open status confirmed as of 2026.",
  "Quantitative claims cross-checked against standard references (Casarett and Doull's Toxicology; OECD Test Guidelines).",
  "All demonstrations use abstract compound X with arbitrary units - no real substances, no harmful dosages, no instructions facilitating harm.",
  "Signature solution sections are labeled proposals: they state assumptions, a reasoning path, a proposed mechanism, what would confirm or kill them, and what they do not claim.",
 ],
 "sig_tail": ("Signature editions carry the Signature system's proposed solution approaches to famous "
              "unsolved problems. Every solution is labeled a Signature-generated proposal, never "
              "established science, never peer-accepted, never proof."),
}

ENTRIES = [
# ------------------------------------------------------------------ rank 1
{
 "key": "tx-dose-response",
 "name": "The Dose Response Extrapolation Problem",
 "group": "Risk Assessment",
 "ladder_rank": 1, "ladder_tier": "foundations",
 "problem": "High-dose animal studies must predict low-dose human risks - but what is the true shape of the dose-response curve at environmental exposures?",
 "background": "The dose-response problem - low-dose extrapolation - is toxicology's founding uncertainty: the linearized multistage model (conservative, linear to zero) versus threshold or hormetic models give wildly different risk estimates at environmental levels. The benchmark-dose method improved on NOAELs but still extrapolates. Endocrine disruptors' non-monotonic curves break the monotonic assumptions. The curve's low end - where regulation lives - is the least measured and most assumed.",
 "why_it_matters": "Exposure limits are set on the extrapolated low end. The assumed curve shape is the regulation's hidden dial.",
 "sig_lens": "The Signature lens reads dose-response as the unmeasured tail: the protocol must measure the tail (low-dose studies) - and report the shape honestly.",
 "sig_solution": LABEL + " Assumptions: (1) low end least measured, most assumed; (2) non-monotonic curves break models. Reasoning path: measure the low end - targeted low-dose studies with mode-of-action-informed models. Proposed mechanism: a tail protocol with low-dose-focused testing, mode-of-action-based extrapolation models, and uncertainty-quantified risk estimates. Confirm: measured low-dose data constrains the shape. Kill: the low end stays unmeasurable. Does NOT claim: the true curve - it measures the tail.",
 "pointer": "The Signature system's proposed approach measures low-dose responses with mode-of-action models; the companion Signature Edition record specifies the tail protocol.",
 "key_points": [
  "Linear-no-threshold vs threshold vs hormesis debated.",
  "Benchmark dose improved on NOAEL but still extrapolates.",
  "Endocrine non-monotonic curves break monotonic models.",
  "Regulation lives on the least-measured curve region.",
 ],
 "requirements": [
  "Targeted low-dose response studies.",
  "Mode-of-action-informed extrapolation.",
  "Uncertainty-quantified risk estimates.",
 ],
 "citations": [
  "NRC (2009) Science and Decisions: Advancing Risk Assessment. National Academies Press.",
 ],
 "demo": {"emax": 100.0, "ec50": 10.0, "n": 1.5, "c": [0.0, 1.0, 10.0, 100.0]},
},
# ------------------------------------------------------------------ rank 2
{
 "key": "tx-mixture",
 "name": "The Mixture Toxicity Problem",
 "group": "Risk Assessment",
 "ladder_rank": 2, "ladder_tier": "foundations",
 "problem": "People are exposed to chemical mixtures - but how can the combined toxicity be predicted when the components interact?",
 "background": "The mixture problem - concentration addition vs independent action vs interaction (synergy/antagonism) - is the real-world exposure question: regulations assess chemicals one at a time while exposures are mixtures. The default (dose addition for similar modes) is approximate; the interactions are mostly unstudied - testing all combinations is impossible. The whole-mixture testing is rare. The assessed single chemicals are not the experienced mixtures.",
 "why_it_matters": "Real exposures are mixtures; regulations are single-chemical. The gap is the unassessed real world.",
 "sig_lens": "The Signature lens reads mixtures as the cocktail: the protocol must test the priority cocktails (common co-exposures) - not just the single ingredients.",
 "sig_solution": LABEL + " Assumptions: (1) interactions mostly unstudied; (2) all-combination testing impossible. Reasoning path: prioritize - test common co-exposure mixtures whole, and model the rest. Proposed mechanism: a cocktail protocol with priority-mixture whole testing, interaction screening for high-concern pairs, and cumulative risk assessment frameworks. Confirm: the priority mixtures' risks characterized. Kill: the mixtures prove untestable at scale. Does NOT claim: all mixtures assessed - it tests the priority cocktails.",
 "pointer": "The Signature system's proposed approach tests priority chemical mixtures whole; the companion Signature Edition record specifies the cocktail protocol.",
 "key_points": [
  "Concentration addition vs independent action vs interaction.",
  "Regulations single-chemical; exposures mixtures.",
  "Interactions mostly unstudied.",
  "All-combination testing impossible.",
 ],
 "requirements": [
  "Priority co-exposure mixture testing.",
  "High-concern pair interaction screening.",
  "Cumulative risk assessment frameworks.",
 ],
 "citations": [
  "Kortenkamp A et al. (2009) State of the Art Report on Mixture Toxicity. EU.",
 ],
 "demo": {"emax": 90.0, "ec50": 8.0, "n": 1.2, "c": [0.0, 0.8, 8.0, 80.0]},
},
# ------------------------------------------------------------------ rank 3
{
 "key": "tx-edc",
 "name": "The Endocrine Disruption Problem",
 "group": "Mechanisms",
 "ladder_rank": 3, "ladder_tier": "foundations",
 "problem": "Hormone-mimicking chemicals act at tiny doses with non-monotonic curves - but how can endocrine disruptors be identified and regulated?",
 "background": "The EDC problem - bisphenol A, phthalates, and thousands of others - challenged toxicology's dose assumptions: low-dose effects, non-monotonic curves, and developmental windows of vulnerability. The identification criteria (EU: hazard-based) are contested; the testing (EDSP, OECD conceptual framework) is slow; and the regrettable-substitution cycle (BPA to BPS/BPF, similar activity) outruns regulation. The hormones' mimics are regulated chemical-by-chemical while acting as mixtures.",
 "why_it_matters": "EDCs affect development at environmental levels. The slow identification is the unprotected vulnerable window.",
 "sig_lens": "The Signature lens reads EDCs as the hormone impostors: the protocol must unmask them fast (high-throughput) - and regulate the class, not the chemical.",
 "sig_solution": LABEL + " Assumptions: (1) low-dose, non-monotonic, window-vulnerable; (2) substitution outruns regulation. Reasoning path: screen fast and regulate by class - high-throughput EDC screening with class-based restrictions. Proposed mechanism: an impostors protocol with ToxCast/Tox21 EDC screening, class-based regulation (bisphenols as a class), and developmental-window-focused testing. Confirm: the class approach prevents regrettable substitution. Kill: the screening misses the active chemicals. Does NOT claim: all EDCs identified - it unmasks them fast.",
 "pointer": "The Signature system's proposed approach screens endocrine disruptors high-throughput with class regulation; the companion Signature Edition record specifies the impostors protocol.",
 "key_points": [
  "Low-dose, non-monotonic, window-vulnerable effects.",
  "EU hazard-based criteria contested.",
  "BPA-to-BPS regrettable substitution cycle.",
  "Testing (EDSP) slow relative to chemical flow.",
 ],
 "requirements": [
  "High-throughput EDC screening.",
  "Class-based (not chemical-by-chemical) regulation.",
  "Developmental-window-focused testing.",
 ],
 "citations": [
  "Gore AC et al. (2015) EDC-2: The Endocrine Society's second scientific statement. Endocrine Reviews 36.",
 ],
 "demo": {"emax": 85.0, "ec50": 5.0, "n": 1.8, "c": [0.0, 0.5, 5.0, 50.0]},
},
# ------------------------------------------------------------------ rank 4
{
 "key": "tx-dev-tox",
 "name": "The Developmental Toxicity Problem",
 "group": "Mechanisms",
 "ladder_rank": 4, "ladder_tier": "foundations",
 "problem": "The developing organism is exquisitely vulnerable - but how can developmental toxicants be detected without extensive animal testing?",
 "background": "The developmental-toxicity problem - thalidomide's lesson - needs animal-free detection: the embryonic stem-cell tests, zebrafish assays, and the OECD test guidelines each cover part; the adverse-outcome pathways for development are incomplete; and the species differences (thalidomide's species-specificity) warn against extrapolation. The vulnerable window is the least-tested. The developing organism's protection lags.",
 "why_it_matters": "Developmental toxicants cause birth defects. The least-tested window is the most vulnerable.",
 "sig_lens": "The Signature lens reads development as the fragile construction: the protocol must inspect the site (alternative assays) - without waiting for the collapse.",
 "sig_solution": LABEL + " Assumptions: (1) alternative assays each partial; (2) species differences warn. Reasoning path: build the battery - integrated alternative testing with AOP-anchored developmental pathways. Proposed mechanism: a construction protocol with integrated developmental-toxicity batteries, AOP-anchored pathway coverage, and human-relevant stem-cell models. Confirm: the battery predicts known developmental toxicants. Kill: the assays miss the human-relevant effects. Does NOT claim: the developmental toxicants all found - it inspects the site.",
 "pointer": "The Signature system's proposed approach builds integrated developmental-toxicity test batteries; the companion Signature Edition record specifies the construction protocol.",
 "key_points": [
  "Thalidomide: species-specific developmental tragedy.",
  "Stem-cell, zebrafish assays each partial.",
  "Developmental AOPs incomplete.",
  "Vulnerable window least-tested.",
 ],
 "requirements": [
  "Integrated alternative test batteries.",
  "AOP-anchored developmental pathways.",
  "Human-relevant stem-cell models.",
 ],
 "citations": [
  "OECD Test Guideline 414: Prenatal Developmental Toxicity Study.",
 ],
 "demo": {"emax": 95.0, "ec50": 12.0, "n": 1.4, "c": [0.0, 1.2, 12.0, 120.0]},
},
# ------------------------------------------------------------------ rank 5
{
 "key": "tx-carcinogen",
 "name": "The Carcinogen Classification Problem",
 "group": "Mechanisms",
 "ladder_rank": 5, "ladder_tier": "foundations",
 "problem": "Classifying carcinogens (IARC Monographs) guides prevention - but how can the classifications keep up with the evidence, and do they communicate risk?",
 "background": "The classification problem - IARC's Group 1/2A/2B system - faces: the evidence backlog (most chemicals unclassified), the hazard-vs-risk confusion (Group 1 includes plutonium and processed meat - same hazard class, vastly different risk), and the mechanism integration (key characteristics of carcinogens). The classifications are authoritative and misunderstood. The hazard list grows; the risk communication lags.",
 "why_it_matters": "Carcinogen classifications guide prevention worldwide. The misunderstood hazard classes mislead the public.",
 "sig_lens": "The Signature lens reads classification as the warning label: the protocol must label the hazard - and print the risk (exposure) beside it.",
 "sig_solution": LABEL + " Assumptions: (1) most chemicals unclassified; (2) hazard-vs-risk confused. Reasoning path: classify faster (mechanism-based) and communicate risk alongside hazard. Proposed mechanism: a label protocol with key-characteristics-based classification, risk-context communication standards, and backlog-prioritized evaluations. Confirm: the classifications guide prevention better. Kill: the backlog never clears. Does NOT claim: all carcinogens classified - it labels with risk beside hazard.",
 "pointer": "The Signature system's proposed approach classifies carcinogens mechanistically with risk context; the companion Signature Edition record specifies the label protocol.",
 "key_points": [
  "IARC Groups 1/2A/2B: hazard classification.",
  "Most chemicals lack classification.",
  "Hazard-vs-risk confusion (plutonium vs processed meat).",
  "Key characteristics integrate mechanisms.",
 ],
 "requirements": [
  "Mechanism-based classification methods.",
  "Risk-context communication standards.",
  "Backlog-prioritized evaluations.",
 ],
 "citations": [
  "IARC Monographs on the Identification of Carcinogenic Hazards to Humans.",
 ],
 "demo": {"emax": 100.0, "ec50": 15.0, "n": 1.6, "c": [0.0, 1.5, 15.0, 150.0]},
},
# ------------------------------------------------------------------ rank 6
{
 "key": "tx-genotox",
 "name": "The Genotoxicity Testing Problem",
 "group": "Methods",
 "ladder_rank": 6, "ladder_tier": "foundations",
 "problem": "DNA-damaging chemicals must be caught - but how can genotoxicity be tested reliably when the assays disagree and the relevance is debated?",
 "background": "The genotoxicity problem - the Ames test plus in-vitro micronucleus/chromosome-aberration battery - has known gaps: the in-vitro positives that are in-vivo negatives (false positives from cytotoxicity), the germ-cell vs somatic relevance, and the threshold debate (is there a safe dose for genotoxicants?). The 3D skin models and the Pig-a assay improve relevance. The DNA-damage detectors are sensitive; their human relevance is half-known.",
 "why_it_matters": "Genotoxicants are the presumed no-threshold carcinogens. The half-known relevance is the regulation's uncertainty.",
 "sig_lens": "The Signature lens reads genotoxicity as the DNA alarm: the protocol must tune the alarm - sensitive enough to catch, specific enough to trust.",
 "sig_solution": LABEL + " Assumptions: (1) in-vitro/in-vivo discordance; (2) threshold debate unresolved. Reasoning path: improve relevance - 3D/human-relevant models with mode-of-action follow-up. Proposed mechanism: an alarm protocol with human-relevant genotoxicity models, mode-of-action-based follow-up of positives, and threshold-evidence standards. Confirm: the tuned battery predicts human relevance. Kill: the discordance persists. Does NOT claim: the genotoxicants all caught - it tunes the alarm.",
 "pointer": "The Signature system's proposed approach tunes genotoxicity testing for human relevance; the companion Signature Edition record specifies the alarm protocol.",
 "key_points": [
  "Ames + in-vitro battery: sensitive, debated relevance.",
  "In-vitro positives often in-vivo negative.",
  "Germ-cell vs somatic relevance open.",
  "Genotoxic threshold debated.",
 ],
 "requirements": [
  "Human-relevant (3D) genotoxicity models.",
  "Mode-of-action follow-up of positives.",
  "Threshold-evidence standards.",
 ],
 "citations": [
  "OECD Test Guidelines for genotoxicity (471, 473, 487).",
 ],
 "demo": {"emax": 88.0, "ec50": 9.0, "n": 1.3, "c": [0.0, 0.9, 9.0, 90.0]},
},
# ------------------------------------------------------------------ rank 7
{
 "key": "tx-skin-sens",
 "name": "The Skin Sensitization Problem",
 "group": "Methods",
 "ladder_rank": 7, "ladder_tier": "foundations",
 "problem": "Allergic skin reactions must be predicted - but how can sensitization be assessed without the mouse local lymph node assay?",
 "background": "The sensitization problem - replacing the LLNA - is the alternative-methods success story in progress: the OECD defined approaches (DPRA, KeratinoSens, h-CLAT integrated) cover the adverse-outcome pathway's key events, and the integrated testing is accepted. But the potency prediction (strong vs weak sensitizers) and the complex mixtures remain open. The animal test is being retired; its replacements are validating.",
 "why_it_matters": "Skin sensitizers are common contact allergens. The retiring animal test's replacements must predict potency.",
 "sig_lens": "The Signature lens reads sensitization as the immune memory: the protocol must test the memory's formation (key events) - without the mouse.",
 "sig_solution": LABEL + " Assumptions: (1) defined approaches cover AOP key events; (2) potency prediction open. Reasoning path: complete the replacement - potency-quantified integrated testing. Proposed mechanism: a memory protocol with AOP-complete defined approaches, potency-prediction models, and mixture-testing extensions. Confirm: the replacements predict potency. Kill: the potency stays unpredictable. Does NOT claim: the animal test fully replaced - it completes the retirement.",
 "pointer": "The Signature system's proposed approach completes animal-free skin sensitization testing; the companion Signature Edition record specifies the memory protocol.",
 "key_points": [
  "OECD defined approaches (DPRA, KeratinoSens, h-CLAT).",
  "AOP key events covered in vitro.",
  "Potency prediction still open.",
  "Complex mixtures untested.",
 ],
 "requirements": [
  "AOP-complete integrated testing.",
  "Potency-quantification models.",
  "Mixture-testing extensions.",
 ],
 "citations": [
  "OECD Guideline 497: Defined Approaches on Skin Sensitisation.",
 ],
 "demo": {"emax": 80.0, "ec50": 7.0, "n": 1.7, "c": [0.0, 0.7, 7.0, 70.0]},
},
# ------------------------------------------------------------------ rank 8
{
 "key": "tx-eye",
 "name": "The Eye Irritation Replacement Problem",
 "group": "Methods",
 "ladder_rank": 8, "ladder_tier": "foundations",
 "problem": "The rabbit eye test (Draize) is being retired - but can the in-vitro replacements cover the full irritation range?",
 "background": "The eye-irritation problem - replacing the Draize test - has validated methods (BCOP, ICE, reconstructed cornea: EpiOcular) for severe irritants and non-irritants, but the mild/moderate middle - the most common classification need - is the gap: the in-vitro methods underperform there. The tiered testing strategies manage the gap. The rabbit's retirement is scheduled; the middle range is half-covered.",
 "why_it_matters": "Eye irritation classification is required for thousands of chemicals. The half-covered middle is the regulatory gap.",
 "sig_lens": "The Signature lens reads eye irritation as the spectrum: the protocol must cover the middle (mild/moderate) - not just the extremes.",
 "sig_solution": LABEL + " Assumptions: (1) extremes covered; middle gapped; (2) tiered strategies manage. Reasoning path: close the middle - improved reconstructed-tissue models with mild-irritant validation. Proposed mechanism: a spectrum protocol with middle-range-focused method development, tiered testing optimization, and the Draize fully retired. Confirm: the middle covered. Kill: the middle stays elusive. Does NOT claim: the Draize replaced - it covers the spectrum.",
 "pointer": "The Signature system's proposed approach closes the mild-irritant testing gap; the companion Signature Edition record specifies the spectrum protocol.",
 "key_points": [
  "BCOP, ICE, EpiOcular validated for extremes.",
  "Mild/moderate range is the gap.",
  "Tiered testing strategies manage the gap.",
  "Draize retirement in progress.",
 ],
 "requirements": [
  "Middle-range method development.",
  "Mild-irritant validation sets.",
  "Optimized tiered strategies.",
 ],
 "citations": [
  "OECD Test Guidelines 437, 438, 492 (eye irritation).",
 ],
 "demo": {"emax": 92.0, "ec50": 11.0, "n": 1.5, "c": [0.0, 1.1, 11.0, 110.0]},
},
# ------------------------------------------------------------------ rank 9
{
 "key": "tx-acute",
 "name": "The Acute Toxicity Replacement Problem",
 "group": "Methods",
 "ladder_rank": 9, "ladder_tier": "foundations",
 "problem": "Acute lethality testing (LD50) uses many animals - but how can acute toxicity be assessed animal-free?",
 "background": "The acute-toxicity problem - replacing the LD50 - is the 3Rs' hard case: the in-vitro cytotoxicity (3T3 NRU) predicts starting doses (reducing animals) but not the classification alone; the GHS categories need the whole-animal integration (toxicokinetics, target organs). The weight-of-evidence and read-across approaches reduce testing. The animal test is reduced, not replaced - the integration gap is the barrier.",
 "why_it_matters": "Acute toxicity classification is required globally. The unreplaced animal test is the 3Rs' hard case.",
 "sig_lens": "The Signature lens reads acute toxicity as the whole-body integration: the protocol must model the integration (kinetics + targets) - not just the cells.",
 "sig_solution": LABEL + " Assumptions: (1) cytotoxicity predicts starting doses only; (2) whole-body integration the gap. Reasoning path: model the integration - in-vitro batteries plus PBPK plus target-organ models. Proposed mechanism: an integration protocol with cytotoxicity-plus-kinetics classification, target-organ in-vitro panels, and weight-of-evidence frameworks. Confirm: the integrated approach classifies correctly. Kill: the integration stays unmodelable. Does NOT claim: the LD50 replaced - it models the integration.",
 "pointer": "The Signature system's proposed approach models acute toxicity via integrated in-vitro and kinetic methods; the companion Signature Edition record specifies the integration protocol.",
 "key_points": [
  "3T3 NRU predicts starting doses, not classification.",
  "GHS categories need whole-animal integration.",
  "Toxicokinetics and target organs are the gap.",
  "Testing reduced, not replaced.",
 ],
 "requirements": [
  "Cytotoxicity-plus-PBPK classification models.",
  "Target-organ in-vitro panels.",
  "Weight-of-evidence frameworks.",
 ],
 "citations": [
  "OECD Guidance Document 129 (cytotoxicity for starting doses).",
 ],
 "demo": {"emax": 100.0, "ec50": 20.0, "n": 1.1, "c": [0.0, 2.0, 20.0, 200.0]},
},
# ----------------------------------------------------------------- rank 10
{
 "key": "tx-bioaccum",
 "name": "The Bioaccumulation Problem",
 "group": "Exposure",
 "ladder_rank": 10, "ladder_tier": "foundations",
 "problem": "Some chemicals concentrate up the food chain - but how can bioaccumulation be predicted for new chemicals without fish tests?",
 "background": "The bioaccumulation problem - the B in PBT - traditionally needs fish bioconcentration tests (OECD 305, animal-intensive): the in-vitro alternatives (hepatocyte clearance, gill models) plus in-silico (log Kow-based, mechanistic models) are developing but the metabolism (which reduces accumulation) is hard to predict. The regulatory B-criteria (BCF > 5000) need the fish data the alternatives approximate. The concentrating chemicals are the food-chain threat; their prediction is half-built.",
 "why_it_matters": "Bioaccumulative chemicals reach top predators - including humans - magnified. The half-built prediction is the food-chain gap.",
 "sig_lens": "The Signature lens reads bioaccumulation as the concentrating chain: the protocol must predict the concentration - including the metabolism that breaks it.",
 "sig_solution": LABEL + " Assumptions: (1) fish tests animal-intensive; (2) metabolism hard to predict. Reasoning path: predict mechanistically - in-vitro clearance plus physiologically-based models. Proposed mechanism: a chain protocol with in-vitro metabolic-clearance assays, mechanistic bioaccumulation models, and fish-test replacement validation. Confirm: the models predict BCF. Kill: the metabolism stays unpredictable. Does NOT claim: the fish test replaced - it predicts the chain.",
 "pointer": "The Signature system's proposed approach predicts bioaccumulation mechanistically without fish tests; the companion Signature Edition record specifies the chain protocol.",
 "key_points": [
  "OECD 305 fish test is animal-intensive.",
  "log Kow-based predictions miss metabolism.",
  "In-vitro clearance assays developing.",
  "BCF > 5000 is the regulatory trigger.",
 ],
 "requirements": [
  "In-vitro metabolic-clearance assays.",
  "Mechanistic bioaccumulation models.",
  "Replacement validation programs.",
 ],
 "citations": [
  "OECD Test Guideline 305: Bioaccumulation in Fish.",
 ],
 "demo": {"emax": 75.0, "ec50": 6.0, "n": 1.9, "c": [0.0, 0.6, 6.0, 60.0]},
},
# ----------------------------------------------------------------- rank 11
{
 "key": "tx-pbt",
 "name": "The PBT Assessment Problem",
 "group": "Exposure",
 "ladder_rank": 11, "ladder_tier": "foundations",
 "problem": "Persistent, bioaccumulative, toxic substances are the worst - but how can PBTs be identified efficiently among thousands of chemicals?",
 "background": "The PBT problem - REACH's PBT/vPvB criteria - needs persistence (degradation half-lives), bioaccumulation (BCF), and toxicity data that most chemicals lack: the assessment is data-hungry and slow. The screening (in-silico PBT profilers) prioritizes; the confirmation needs the missing data. The regrettable reality: the PBTs of tomorrow are in commerce today, unassessed. The worst chemicals are the least-tested.",
 "why_it_matters": "PBTs persist for generations and magnify in food chains. The unassessed PBTs are the irreversible pollution.",
 "sig_lens": "The Signature lens reads PBTs as the permanent poisons: the protocol must find them before they spread - by screening smart and confirming fast.",
 "sig_solution": LABEL + " Assumptions: (1) assessment data-hungry; (2) screening prioritizes, confirmation lags. Reasoning path: screen smart, confirm fast - in-silico PBT profiling with targeted confirmation testing. Proposed mechanism: a poisons protocol with high-throughput PBT screening, targeted confirmation batteries, and pre-market PBT assessment requirements. Confirm: the PBTs identified pre-market. Kill: the screening misses the true PBTs. Does NOT claim: all PBTs found - it finds them before spread.",
 "pointer": "The Signature system's proposed approach screens PBTs pre-market with targeted confirmation; the companion Signature Edition record specifies the poisons protocol.",
 "key_points": [
  "REACH PBT/vPvB criteria: persistence, bioaccumulation, toxicity.",
  "Most chemicals lack the needed data.",
  "In-silico profilers screen; confirmation lags.",
  "Tomorrow's PBTs in commerce today.",
 ],
 "requirements": [
  "High-throughput PBT screening.",
  "Targeted confirmation batteries.",
  "Pre-market PBT assessment.",
 ],
 "citations": [
  "REACH Annex XIII: PBT and vPvB criteria.",
 ],
 "demo": {"emax": 82.0, "ec50": 8.5, "n": 1.4, "c": [0.0, 0.85, 8.5, 85.0]},
},
# ----------------------------------------------------------------- rank 12
{
 "key": "tx-aop",
 "name": "The Adverse Outcome Pathway Problem",
 "group": "Mechanisms",
 "ladder_rank": 12, "ladder_tier": "compounded",
 "problem": "Toxicity starts with a molecular event and ends in disease - but how can the full pathway be mapped for predictive toxicology?",
 "background": "The AOP problem - molecular initiating event to adverse outcome via key events - is the predictive-toxicology framework: the AOP Wiki catalogs pathways, but most are incomplete (qualitative, missing quantitative key-event relationships); the AOP networks (interacting pathways) are nascent; and the regulatory use needs the quantitative KERs. The framework is built; the pathways are half-mapped.",
 "why_it_matters": "AOPs are predictive toxicology's roadmap. The half-mapped pathways are the unpaved roads.",
 "sig_lens": "The Signature lens reads AOPs as the roadmaps: the protocol must pave them - quantitatively - from the molecular event to the disease.",
 "sig_solution": LABEL + " Assumptions: (1) most AOPs qualitative; (2) quantitative KERs needed. Reasoning path: quantify the key events - dose-response for each KER, network interactions. Proposed mechanism: a roadmap protocol with quantitative AOP development, KER dose-response characterization, and AOP-network modeling. Confirm: the quantified AOPs predict outcomes. Kill: the pathways stay qualitative. Does NOT claim: the pathways complete - it paves the roads.",
 "pointer": "The Signature system's proposed approach quantifies adverse outcome pathways; the companion Signature Edition record specifies the roadmap protocol.",
 "key_points": [
  "AOP: molecular initiating event to adverse outcome.",
  "AOP Wiki catalogs; most pathways incomplete.",
  "Quantitative key-event relationships missing.",
  "AOP networks nascent.",
 ],
 "requirements": [
  "Quantitative AOP development.",
  "KER dose-response characterization.",
  "AOP-network modeling.",
 ],
 "citations": [
  "Ankley GT et al. (2010) Adverse outcome pathways: a conceptual framework. Environmental Toxicology and Chemistry 29.",
 ],
 "demo": {"emax": 90.0, "ec50": 10.0, "n": 1.5, "c": [0.0, 1.0, 10.0, 100.0]},
},
# ----------------------------------------------------------------- rank 13
{
 "key": "tx-read-across",
 "name": "The Read Across Problem",
 "group": "Methods",
 "ladder_rank": 13, "ladder_tier": "compounded",
 "problem": "Data-poor chemicals resemble data-rich ones - but when is read-across scientifically justified, and how is its uncertainty quantified?",
 "background": "The read-across problem - filling data gaps by analogy - is REACH's workhorse and its weak point: the justifications (structural similarity, common metabolites) are often asserted, not demonstrated; the uncertainty is unquantified; and the failed read-across (the analogy was wrong) is discovered late. The OECD guidance and the good-read-across-practice set standards; the practice lags. The analogy is the assessment; its rigor is half-built.",
 "why_it_matters": "Read-across fills most REACH data gaps. The unrigorous analogies are the assessments' hidden errors.",
 "sig_lens": "The Signature lens reads read-across as the analogy: the protocol must prove the analogy (mechanistic similarity) - and price its uncertainty.",
 "sig_solution": LABEL + " Assumptions: (1) justifications often asserted; (2) uncertainty unquantified. Reasoning path: justify mechanistically - AOP-anchored similarity with uncertainty quantification. Proposed mechanism: an analogy protocol with mechanism-based read-across justifications, uncertainty-quantified predictions, and failed-analogy learning systems. Confirm: the justified read-across predicts correctly. Kill: the analogies stay unprovable. Does NOT claim: the gaps all filled - it proves the analogies.",
 "pointer": "The Signature system's proposed approach justifies read-across mechanistically with uncertainty; the companion Signature Edition record specifies the analogy protocol.",
 "key_points": [
  "Read-across fills REACH data gaps.",
  "Similarity justifications often asserted.",
  "Uncertainty unquantified.",
  "Failed analogies discovered late.",
 ],
 "requirements": [
  "Mechanism-anchored similarity justifications.",
  "Uncertainty-quantified predictions.",
  "Failed-analogy learning systems.",
 ],
 "citations": [
  "OECD (2014) Guidance on Grouping of Chemicals (read-across).",
 ],
 "demo": {"emax": 86.0, "ec50": 9.5, "n": 1.6, "c": [0.0, 0.95, 9.5, 95.0]},
},
# ----------------------------------------------------------------- rank 14
{
 "key": "tx-qsar-domain",
 "name": "The QSAR Applicability Domain Problem",
 "group": "Methods",
 "ladder_rank": 14, "ladder_tier": "compounded",
 "problem": "QSAR models predict toxicity from structure - but how can the model's reliable domain be defined, so the predictions are trusted only where valid?",
 "background": "The applicability-domain problem - QSAR's reliability boundary - is the model's honesty: the predictions outside the training chemistry are extrapolations, but the domain definitions (descriptor ranges, structural alerts) are heuristic and the users ignore them. The OECD validation principles require the domain; the practice is loose. The models predict; their boundaries are advisory.",
 "why_it_matters": "QSAR predictions guide regulation. The ignored boundaries are the trusted extrapolations.",
 "sig_lens": "The Signature lens reads QSAR as the fortune-teller: the protocol must mark the crystal ball's range - and refuse readings beyond it.",
 "sig_solution": LABEL + " Assumptions: (1) domain definitions heuristic; (2) users ignore boundaries. Reasoning path: enforce the domain - rigorous domain metrics with prediction-blocking outside. Proposed mechanism: a ball protocol with quantitative applicability-domain metrics, out-of-domain prediction blocking, and domain-expansion via targeted testing. Confirm: the domain-respecting predictions validate. Kill: the domains prove undefinable. Does NOT claim: the QSARs all valid - it marks the range.",
 "pointer": "The Signature system's proposed approach enforces QSAR applicability domains rigorously; the companion Signature Edition record specifies the ball protocol.",
 "key_points": [
  "QSAR predicts from chemical structure.",
  "Applicability domain: the reliability boundary.",
  "Domain definitions heuristic; ignored in practice.",
  "OECD principles require the domain.",
 ],
 "requirements": [
  "Quantitative domain metrics.",
  "Out-of-domain prediction blocking.",
  "Targeted domain-expansion testing.",
 ],
 "citations": [
  "OECD (2014) Guidance Document on the Validation of QSAR Models.",
 ],
 "demo": {"emax": 94.0, "ec50": 13.0, "n": 1.2, "c": [0.0, 1.3, 13.0, 130.0]},
},
# ----------------------------------------------------------------- rank 15
{
 "key": "tx-ivive",
 "name": "The In Vitro to In Vivo Extrapolation Problem",
 "group": "Methods",
 "ladder_rank": 15, "ladder_tier": "compounded",
 "problem": "Cell assays give concentrations - but how can the in-vitro effect level be translated to a human exposure limit?",
 "background": "The IVIVE problem - from nominal in-vitro concentrations to human-equivalent doses - needs toxicokinetics: the free concentration (protein binding, plastic binding), the clearance, and the PBPK modeling. The ToxCast-to-risk translation is the program's goal; the uncertainties (in-vitro disposition, metabolic competence) are large. The cell's response is measured; the human's dose is inferred.",
 "why_it_matters": "High-throughput screening's regulatory use needs IVIVE. The inferred human doses are the screening's risk translation.",
 "sig_lens": "The Signature lens reads IVIVE as the translation: the protocol must translate carefully - free concentrations, kinetics - and show the translation's uncertainty.",
 "sig_solution": LABEL + " Assumptions: (1) in-vitro disposition uncertain; (2) metabolic competence limited. Reasoning path: translate mechanistically - measured free concentrations plus PBPK with uncertainty. Proposed mechanism: a translation protocol with in-vitro disposition measurement, PBPK-based IVIVE, and uncertainty-quantified human-equivalent doses. Confirm: the translated doses predict in-vivo. Kill: the uncertainties dominate. Does NOT claim: the human doses exact - it translates carefully.",
 "pointer": "The Signature system's proposed approach translates in-vitro effects to human doses with PBPK; the companion Signature Edition record specifies the translation protocol.",
 "key_points": [
  "In-vitro nominal vs free concentrations differ.",
  "Toxicokinetics needed for translation.",
  "ToxCast-to-risk is the program goal.",
  "In-vitro disposition uncertainties large.",
 ],
 "requirements": [
  "In-vitro disposition measurement.",
  "PBPK-based IVIVE modeling.",
  "Uncertainty-quantified human doses.",
 ],
 "citations": [
  "Wetmore BA et al. (2012) Integration of dosimetry and exposure. Toxicological Sciences 125.",
 ],
 "demo": {"emax": 78.0, "ec50": 7.5, "n": 1.8, "c": [0.0, 0.75, 7.5, 75.0]},
},
# ----------------------------------------------------------------- rank 16
{
 "key": "tx-pbpk",
 "name": "The PBPK Modeling Problem",
 "group": "Methods",
 "ladder_rank": 16, "ladder_tier": "compounded",
 "problem": "Physiologically-based kinetic models predict tissue doses - but how can they be parameterized for data-poor chemicals?",
 "background": "The PBPK problem - the models' hunger for partition coefficients, clearances, and permeabilities - limits their use: the in-vitro-to-in-vivo parameter prediction (QIVIVE) is developing; the generic models (httk) cover the well-studied; and the regulatory acceptance needs the validation. The models are powerful; their parameters are missing.",
 "why_it_matters": "PBPK is the kinetic bridge for risk assessment. The missing parameters are the unbuilt bridge.",
 "sig_lens": "The Signature lens reads PBPK as the body's plumbing map: the protocol must fill in the pipe sizes (parameters) - by measurement and prediction.",
 "sig_solution": LABEL + " Assumptions: (1) parameters missing for most chemicals; (2) in-vitro prediction developing. Reasoning path: parameterize at scale - high-throughput in-vitro parameters with generic-model validation. Proposed mechanism: a plumbing protocol with HT in-vitro parameter measurement, generic-PBPK validation programs, and regulatory-acceptance criteria. Confirm: the parameterized models predict kinetics. Kill: the parameters stay unmeasurable at scale. Does NOT claim: the models all parameterized - it fills the pipes.",
 "pointer": "The Signature system's proposed approach parameterizes PBPK models high-throughput; the companion Signature Edition record specifies the plumbing protocol.",
 "key_points": [
  "PBPK needs partitions, clearances, permeabilities.",
  "In-vitro parameter prediction developing.",
  "Generic models (httk) cover well-studied chemicals.",
  "Regulatory acceptance needs validation.",
 ],
 "requirements": [
  "High-throughput parameter measurement.",
  "Generic-model validation programs.",
  "Regulatory acceptance criteria.",
 ],
 "citations": [
  "Pearce RG et al. (2017) httk: R package for high-throughput toxicokinetics. J. Statistical Software 79.",
 ],
 "demo": {"emax": 98.0, "ec50": 16.0, "n": 1.3, "c": [0.0, 1.6, 16.0, 160.0]},
},
# ----------------------------------------------------------------- rank 17
{
 "key": "tx-nano",
 "name": "The Nanomaterial Toxicity Problem",
 "group": "Emerging Risks",
 "ladder_rank": 17, "ladder_tier": "compounded",
 "problem": "Engineered nanomaterials have novel properties - but how can their toxicity be assessed when the dose metric itself (mass? surface? number?) is debated?",
 "background": "The nano problem - the dose metric debate (mass vs surface area vs particle number), the characterization requirements, and the grouping/read-across for nanoforms - is the regulation's moving target: the EU's nanoform requirements (REACH) demand the characterization; the testing adapts slowly. The novel properties (translocation, protein corona) need novel assessment. The tiny particles are the big regulatory challenge.",
 "why_it_matters": "Nanomaterials are in commerce; their assessment lags. The debated dose metric is the unmeasured risk.",
 "sig_lens": "The Signature lens reads nanomaterials as the tiny strangers: the protocol must measure them properly (metric, characterization) - before judging.",
 "sig_solution": LABEL + " Assumptions: (1) dose metric debated; (2) characterization required but testing lags. Reasoning path: characterize then assess - metric-resolved testing with nanoform grouping. Proposed mechanism: a strangers protocol with dose-metric-resolved testing, nanoform grouping/read-across, and protein-corona-aware assessment. Confirm: the metric-resolved tests predict effects. Kill: the metrics never agree. Does NOT claim: the nano risks assessed - it measures the strangers.",
 "pointer": "The Signature system's proposed approach assesses nanomaterials with metric-resolved testing; the companion Signature Edition record specifies the strangers protocol.",
 "key_points": [
  "Dose metric: mass vs surface vs number debated.",
  "EU nanoform characterization requirements.",
  "Protein corona modifies the biological identity.",
  "Testing adapts slowly to novel properties.",
 ],
 "requirements": [
  "Dose-metric-resolved testing.",
  "Nanoform grouping and read-across.",
  "Protein-corona-aware assessment.",
 ],
 "citations": [
  "OECD (2022) Guidance on the characterisation of manufactured nanomaterials.",
 ],
 "demo": {"emax": 70.0, "ec50": 5.5, "n": 2.0, "c": [0.0, 0.55, 5.5, 55.0]},
},
# ----------------------------------------------------------------- rank 18
{
 "key": "tx-microplastic",
 "name": "The Microplastic Toxicity Problem",
 "group": "Emerging Risks",
 "ladder_rank": 18, "ladder_tier": "compounded",
 "problem": "Microplastics are everywhere - but are the particles themselves toxic, or are they vectors for chemicals, and at what exposures?",
 "background": "The microplastic problem - particle vs chemical toxicity - is the exposure-assessment nightmare: the particles are ubiquitous (detected in blood, placenta), but the effect levels vs environmental levels are debated; the test particles (pristine spheres) differ from environmental (weathered, additive-laden); and the nanoplastic fraction is unmeasurable. The concern is high; the risk characterization is low. The ubiquitous particles are the unquantified risk.",
 "why_it_matters": "Microplastics are in human blood. The unquantified risk is the public's concern without an answer.",
 "sig_lens": "The Signature lens reads microplastics as the ubiquitous dust: the protocol must separate the dust's harm (particles) from its cargo (chemicals) - at real exposures.",
 "sig_solution": LABEL + " Assumptions: (1) particle vs chemical debated; (2) test particles unrealistic. Reasoning path: test realistically - weathered particles at environmental levels, separating particle and chemical effects. Proposed mechanism: a dust protocol with environmentally realistic testing, particle-vs-chemical discrimination, and nanoplastic measurement development. Confirm: the realistic tests characterize the risk. Kill: the exposures stay unmeasurable. Does NOT claim: the microplastic risk known - it separates dust from cargo.",
 "pointer": "The Signature system's proposed approach tests microplastics realistically separating particle and chemical effects; the companion Signature Edition record specifies the dust protocol.",
 "key_points": [
  "Microplastics detected in blood and placenta.",
  "Particle vs adsorbed-chemical toxicity debated.",
  "Test particles differ from environmental.",
  "Nanoplastic fraction unmeasurable.",
 ],
 "requirements": [
  "Environmentally realistic particle testing.",
  "Particle-vs-chemical effect discrimination.",
  "Nanoplastic measurement methods.",
 ],
 "citations": [
  "Leslie HA et al. (2022) Discovery and quantification of plastic particle pollution in human blood. Environment International 163.",
 ],
 "demo": {"emax": 65.0, "ec50": 4.5, "n": 1.6, "c": [0.0, 0.45, 4.5, 45.0]},
},
# ----------------------------------------------------------------- rank 19
{
 "key": "tx-pfas",
 "name": "The PFAS Toxicity Problem",
 "group": "Emerging Risks",
 "ladder_rank": 19, "ladder_tier": "compounded",
 "problem": "Thousands of PFAS exist - but how can the 'forever chemicals' be assessed when only a few are well-studied?",
 "background": "The PFAS problem - thousands of per- and polyfluoroalkyl substances, a few well-studied (PFOA, PFOS) - is the regrettable-scale challenge: the persistence is the concern (forever chemicals), the health effects (immune, developmental, cholesterol) are being mapped for the famous few, and the class-based regulation (EU universal restriction proposal) is the policy answer. The studied few are the tip; the class is the iceberg.",
 "why_it_matters": "PFAS are in everyone's blood and persist forever. The unstudied thousands are the iceberg.",
 "sig_lens": "The Signature lens reads PFAS as the forever iceberg: the protocol must assess the class - not just the tip - and stop the flow.",
 "sig_solution": LABEL + " Assumptions: (1) thousands exist; few studied; (2) persistence is the core concern. Reasoning path: assess by class - grouping by structure/persistence with targeted testing of representatives. Proposed mechanism: an iceberg protocol with PFAS class-based assessment, representative testing programs, and source-reduction (essential-use) policies. Confirm: the class assessed and restricted. Kill: the class proves ungroupable. Does NOT claim: all PFAS assessed - it tackles the iceberg.",
 "pointer": "The Signature system's proposed approach assesses PFAS by class with essential-use policies; the companion Signature Edition record specifies the iceberg protocol.",
 "key_points": [
  "Thousands of PFAS; PFOA/PFOS best studied.",
  "Persistence ('forever') is the core concern.",
  "Health effects mapped for the famous few.",
  "EU universal restriction: class-based answer.",
 ],
 "requirements": [
  "Class-based PFAS assessment.",
  "Representative testing programs.",
  "Essential-use source-reduction policies.",
 ],
 "citations": [
  "Cousins IT et al. (2020) The high persistence of PFAS is sufficient for their management as a chemical class. Env. Sci.: Processes & Impacts 22.",
 ],
 "demo": {"emax": 88.0, "ec50": 8.0, "n": 1.7, "c": [0.0, 0.8, 8.0, 80.0]},
},
# ----------------------------------------------------------------- rank 20
{
 "key": "tx-pesticide-mix",
 "name": "The Pesticide Mixture Problem",
 "group": "Exposure",
 "ladder_rank": 20, "ladder_tier": "compounded",
 "problem": "Fields receive pesticide cocktails - but how can the mixture risks to workers, consumers, and ecosystems be assessed?",
 "background": "The pesticide-mixture problem - tank mixes and sequential applications - is the agricultural reality: the risk assessment is mostly single-active-ingredient; the co-formulants (adjuvants) are less tested; and the ecological mixtures (runoff cocktails) affect non-target species. The cumulative risk (common mechanism groups: organophosphates) is assessed partially. The sprayed cocktail is the assessed single.",
 "why_it_matters": "Pesticide mixtures are the field reality. The single-ingredient assessments miss the cocktail.",
 "sig_lens": "The Signature lens reads pesticide mixtures as the field cocktail: the protocol must test the tank mix - not just the active ingredient.",
 "sig_solution": LABEL + " Assumptions: (1) assessment single-ingredient; (2) co-formulants less tested. Reasoning path: assess the formulation - whole-formulation testing with cumulative common-mechanism groups. Proposed mechanism: a field protocol with whole-formulation mixture testing, co-formulant assessment requirements, and ecological cocktail monitoring. Confirm: the formulation tests predict field effects. Kill: the mixtures stay untestable. Does NOT claim: the mixtures all assessed - it tests the tank mix.",
 "pointer": "The Signature system's proposed approach tests pesticide formulations as mixtures; the companion Signature Edition record specifies the field protocol.",
 "key_points": [
  "Tank mixes and sequential applications are the reality.",
  "Assessment mostly single-active-ingredient.",
  "Co-formulants (adjuvants) less tested.",
  "Cumulative common-mechanism groups partially assessed.",
 ],
 "requirements": [
  "Whole-formulation mixture testing.",
  "Co-formulant assessment requirements.",
  "Ecological cocktail monitoring.",
 ],
 "citations": [
  "EFSA (2019) Guidance on harmonised methodologies for human health, animal health and ecological risk assessment of combined exposure.",
 ],
 "demo": {"emax": 92.0, "ec50": 10.5, "n": 1.4, "c": [0.0, 1.05, 10.5, 105.0]},
},
# ----------------------------------------------------------------- rank 21
{
 "key": "tx-metal-spec",
 "name": "The Heavy Metal Speciation Problem",
 "group": "Exposure",
 "ladder_rank": 21, "ladder_tier": "compounded",
 "problem": "A metal's toxicity depends on its chemical form - but how can speciation be accounted for when the forms interconvert in the environment and body?",
 "background": "The speciation problem - Cr(VI) vs Cr(III), methylmercury vs inorganic mercury, arsenite vs arsenate - is the metal-toxicity key: the total metal measures nothing about the risk; the species interconvert (redox, methylation); and the bioavailability depends on the matrix. The regulations on total metals mislead; the species-specific assessment is data-hungry. The element is not the poison - the species is.",
 "why_it_matters": "Metal risks are species-specific. The total-metal regulations mismeasure the poison.",
 "sig_lens": "The Signature lens reads metals as the shape-shifters: the protocol must track the forms (speciation) - not just count the atoms.",
 "sig_solution": LABEL + " Assumptions: (1) toxicity species-specific; (2) species interconvert. Reasoning path: assess the species - speciation-aware monitoring with transformation modeling. Proposed mechanism: a shifters protocol with species-specific analysis methods, environmental transformation modeling, and species-based standards. Confirm: the species assessments predict effects. Kill: the interconversion defeats assessment. Does NOT claim: all species tracked - it follows the forms.",
 "pointer": "The Signature system's proposed approach assesses metals by chemical species; the companion Signature Edition record specifies the shifters protocol.",
 "key_points": [
  "Cr(VI) vs Cr(III); methylmercury vs inorganic differ vastly.",
  "Total metal measures little about risk.",
  "Species interconvert via redox and methylation.",
  "Species-specific assessment data-hungry.",
 ],
 "requirements": [
  "Species-specific analytical methods.",
  "Environmental transformation modeling.",
  "Species-based regulatory standards.",
 ],
 "citations": [
  "Templeton DM et al. (2000) Guidelines for terms related to chemical speciation. Pure and Applied Chemistry 72.",
 ],
 "demo": {"emax": 84.0, "ec50": 7.0, "n": 1.5, "c": [0.0, 0.7, 7.0, 70.0]},
},
# ----------------------------------------------------------------- rank 22
{
 "key": "tx-air-mix",
 "name": "The Air Pollution Mixture Problem",
 "group": "Exposure",
 "ladder_rank": 22, "ladder_tier": "compounded",
 "problem": "Air pollution is a mixture - but which components drive the health effects, and how can the mixture be regulated?",
 "background": "The air-mixture problem - PM2.5's components (sulfate, nitrate, black carbon, metals, organics) differ in toxicity, but the regulation is mass-based: the component-specific risks are studied (black carbon, ultrafines suspected worse) but the standards stay mass-based. The accountability studies (did the regulation improve health?) are the gold standard, rarely done. The regulated mass is not the toxic mixture.",
 "why_it_matters": "Air pollution kills millions. The mass-based standards may target the wrong components.",
 "sig_lens": "The Signature lens reads air pollution as the mixed air: the protocol must find the harmful fractions (components) - and regulate those.",
 "sig_solution": LABEL + " Assumptions: (1) components differ in toxicity; (2) standards mass-based. Reasoning path: identify the drivers - component-specific epidemiology with accountability studies. Proposed mechanism: a mixed protocol with component-resolved health studies, targeted component controls, and regulation-accountability assessments. Confirm: the component controls improve health most. Kill: the components prove inseparable. Does NOT claim: the drivers identified - it finds the harmful fractions.",
 "pointer": "The Signature system's proposed approach identifies the most harmful air-pollution components; the companion Signature Edition record specifies the mixed protocol.",
 "key_points": [
  "PM2.5 components differ in toxicity.",
  "Regulation mass-based, not composition-based.",
  "Black carbon and ultrafines suspected worse.",
  "Accountability studies rarely done.",
 ],
 "requirements": [
  "Component-resolved health studies.",
  "Targeted component controls.",
  "Regulation-accountability assessments.",
 ],
 "citations": [
  "HEI (2020) Traffic-Related Air Pollution: A Critical Review. Special Report 23.",
 ],
 "demo": {"emax": 76.0, "ec50": 6.5, "n": 1.3, "c": [0.0, 0.65, 6.5, 65.0]},
},
# ----------------------------------------------------------------- rank 23
{
 "key": "tx-water-mix",
 "name": "The Water Contaminant Mixture Problem",
 "group": "Exposure",
 "ladder_rank": 23, "ladder_tier": "compounded",
 "problem": "Drinking water holds contaminant mixtures - but how can the combined risks be assessed when each is regulated alone?",
 "background": "The water-mixture problem - disinfection byproducts, PFAS, pesticides, pharmaceuticals co-occurring - is the tap-water reality: the MCLs are single-contaminant; the mixture's combined risk is unassessed; and the unregulated contaminants (the majority) lack even single standards. The effect-based monitoring (bioassays on water extracts) is the honest check, unstandardized. The regulated singles are not the drunk mixture.",
 "why_it_matters": "Tap water is a mixture; standards are singles. The unassessed mixture is the drunk water.",
 "sig_lens": "The Signature lens reads tap water as the mixed drink: the protocol must test the drink (bioassays) - not just list the ingredients.",
 "sig_solution": LABEL + " Assumptions: (1) MCLs single-contaminant; (2) most contaminants unregulated. Reasoning path: test the mixture - effect-based monitoring of water extracts with mixture-risk frameworks. Proposed mechanism: a drink protocol with bioassay-based water monitoring, mixture-risk assessment methods, and unregulated-contaminant screening. Confirm: the bioassays predict health relevance. Kill: the bioassays prove too variable. Does NOT claim: the mixture risk known - it tests the drink.",
 "pointer": "The Signature system's proposed approach monitors drinking-water mixtures with bioassays; the companion Signature Edition record specifies the drink protocol.",
 "key_points": [
  "MCLs regulate single contaminants.",
  "Tap water holds DBPs, PFAS, pesticides, pharmaceuticals.",
  "Most contaminants lack standards.",
  "Effect-based monitoring unstandardized.",
 ],
 "requirements": [
  "Bioassay-based water monitoring.",
  "Mixture-risk assessment methods.",
  "Unregulated-contaminant screening.",
 ],
 "citations": [
  "Escher BI et al. (2021) Effect-based trigger values for in vitro bioassays in water quality assessment. Env. Int. 152.",
 ],
 "demo": {"emax": 80.0, "ec50": 9.0, "n": 1.6, "c": [0.0, 0.9, 9.0, 90.0]},
},
# ----------------------------------------------------------------- rank 24
{
 "key": "tx-exposome",
 "name": "The Exposome Problem",
 "group": "Exposure",
 "ladder_rank": 24, "ladder_tier": "advanced",
 "problem": "Health reflects lifetime exposures - but how can the exposome (all exposures from conception on) be measured?",
 "background": "The exposome problem - Wild's 2005 concept of the total exposure - is the measurement moonshot: the internal exposome (metabolomics adducts), the external (sensors, geospatial), each partial; the timing (windows of vulnerability) multiplies the complexity; and the statistics (exposome-wide association) face the multiple-testing burden. The HELIX and EXPOsOMICS projects proved feasibility partially. The lifetime exposure is the unmeasured determinant.",
 "why_it_matters": "Chronic disease is substantially environmental. The unmeasured exposome is the unattributed disease burden.",
 "sig_lens": "The Signature lens reads the exposome as the life log: the protocol must record it - internal and external - across the vulnerable windows.",
 "sig_solution": LABEL + " Assumptions: (1) internal/external each partial; (2) windows multiply complexity. Reasoning path: record longitudinally - birth cohorts with multi-layer exposure monitoring. Proposed mechanism: a log protocol with longitudinal exposome cohorts, internal/external integration, and window-specific analyses. Confirm: the logged exposomes explain disease variance. Kill: the measurement stays infeasible. Does NOT claim: the exposome measured - it records the log.",
 "pointer": "The Signature system's proposed approach records lifetime exposomes in longitudinal cohorts; the companion Signature Edition record specifies the log protocol.",
 "key_points": [
  "Exposome: total lifetime exposure (Wild, 2005).",
  "Internal (adducts) and external (sensors) each partial.",
  "Windows of vulnerability multiply complexity.",
  "HELIX/EXPOsOMICS proved partial feasibility.",
 ],
 "requirements": [
  "Longitudinal exposome birth cohorts.",
  "Internal/external exposure integration.",
  "Window-specific exposure analyses.",
 ],
 "citations": [
  "Wild CP (2005) Complementing the genome with an exposome. Cancer Epi. Biomarkers Prev. 14.",
 ],
 "demo": {"emax": 90.0, "ec50": 12.0, "n": 1.5, "c": [0.0, 1.2, 12.0, 120.0]},
},
# ----------------------------------------------------------------- rank 25
{
 "key": "tx-gxe",
 "name": "The Gene Environment Interaction Problem",
 "group": "Mechanisms",
 "ladder_rank": 25, "ladder_tier": "advanced",
 "problem": "Genes and environment jointly cause disease - but how can their interactions be detected when both are high-dimensional?",
 "background": "The GxE problem - the interaction hunt - is statistically brutal: the genome-wide interaction scans need enormous samples; the exposure measurement is the weak link (the exposome problem again); and the reported interactions replicate poorly. The successes (NAT2-smoking-bladder cancer) are the template; the failures are the norm. The joint causation is real; its detection is underpowered.",
 "why_it_matters": "Disease is gene-environment joint causation. The undetected interactions are the misattributed risks.",
 "sig_lens": "The Signature lens reads GxE as the duet: the protocol must hear both parts (genes, exposures) - measured well - to catch the harmony.",
 "sig_solution": LABEL + " Assumptions: (1) interaction scans underpowered; (2) exposure the weak link. Reasoning path: power the duet - large cohorts with good exposure measurement and pathway-guided interaction tests. Proposed mechanism: a duet protocol with exposure-improved cohorts, pathway-guided GxE tests, and replication-required interaction claims. Confirm: the interactions replicate. Kill: the power never suffices. Does NOT claim: the interactions found - it powers the duet.",
 "pointer": "The Signature system's proposed approach powers gene-environment interaction detection; the companion Signature Edition record specifies the duet protocol.",
 "key_points": [
  "Genome-wide interaction scans need huge samples.",
  "Exposure measurement is the weak link.",
  "Reported interactions replicate poorly.",
  "NAT2-smoking is the template success.",
 ],
 "requirements": [
  "Exposure-improved large cohorts.",
  "Pathway-guided interaction tests.",
  "Replication-required interaction claims.",
 ],
 "citations": [
  "Hunter DJ (2005) Gene-environment interactions in human diseases. Nature Reviews Genetics 6.",
 ],
 "demo": {"emax": 85.0, "ec50": 11.0, "n": 1.4, "c": [0.0, 1.1, 11.0, 110.0]},
},
# ----------------------------------------------------------------- rank 26
{
 "key": "tx-epigenetic-tox",
 "name": "The Epigenetic Toxicity Problem",
 "group": "Mechanisms",
 "ladder_rank": 26, "ladder_tier": "advanced",
 "problem": "Chemicals alter epigenetic marks - but which alterations are adverse, and how can epigenetic toxicity be tested?",
 "background": "The epigenetic-toxicity problem - the adversity question - is the testing frontier: the epigenetic changes are measurable (methylation arrays), but the adverse vs adaptive distinction is unclear; the test guidelines lack epigenetic endpoints; and the transgenerational implications (the next entry) raise the stakes. The marks change; their meaning is half-read.",
 "why_it_matters": "Epigenetic toxicity may underlie developmental and transgenerational effects. The half-read marks are the unassessed hazard.",
 "sig_lens": "The Signature lens reads epigenetic marks as the annotations: the protocol must learn which annotations are warnings (adverse) - not just notes.",
 "sig_solution": LABEL + " Assumptions: (1) adversity distinction unclear; (2) guidelines lack endpoints. Reasoning path: define adversity - link epigenetic changes to phenotypic outcomes systematically. Proposed mechanism: an annotations protocol with epigenetic-phenotype linkage studies, adversity criteria development, and guideline endpoint proposals. Confirm: the adverse marks identified. Kill: the marks prove non-adverse generally. Does NOT claim: the adverse marks known - it learns the warnings.",
 "pointer": "The Signature system's proposed approach defines epigenetic adversity with phenotype linkage; the companion Signature Edition record specifies the annotations protocol.",
 "key_points": [
  "Chemical epigenetic alterations measurable.",
  "Adverse vs adaptive distinction unclear.",
  "Test guidelines lack epigenetic endpoints.",
  "Transgenerational stakes raise urgency.",
 ],
 "requirements": [
  "Epigenetic-phenotype linkage studies.",
  "Adversity criteria development.",
  "Guideline endpoint proposals.",
 ],
 "citations": [
  "Baccarelli A, Bollati V (2009) Epigenetics and environmental chemicals. Current Opinion Pediatrics 21.",
 ],
 "demo": {"emax": 78.0, "ec50": 8.5, "n": 1.6, "c": [0.0, 0.85, 8.5, 85.0]},
},
# ----------------------------------------------------------------- rank 27
{
 "key": "tx-transgen",
 "name": "The Transgenerational Toxicity Problem",
 "group": "Mechanisms",
 "ladder_rank": 27, "ladder_tier": "advanced",
 "problem": "Exposures may affect grandchildren - but which transgenerational effects are real, and how can they be tested rigorously?",
 "background": "The transgenerational problem - Skinner's vinclozolin claims and the controversy - is toxicology's replication flashpoint: the multigenerational designs (F3 as true transgenerational) are demanding; the positive reports replicate inconsistently; and the mechanism (epigenetic inheritance) is debated. The stakes (heritable exposure effects) are enormous; the evidence is contested. The grandchildren's risk is the most disputed claim.",
 "why_it_matters": "True transgenerational toxicity would rewrite risk assessment. The disputed claims are the highest-stakes uncertainty.",
 "sig_lens": "The Signature lens reads transgenerational effects as the echo: the protocol must verify the echo is real - with rigorous F3 designs - before amplifying it.",
 "sig_solution": LABEL + " Assumptions: (1) reports replicate inconsistently; (2) F3 designs demanding. Reasoning path: test rigorously - standardized multigenerational designs with mechanism requirements. Proposed mechanism: an echo protocol with rigorous F3 transgenerational designs, mechanism (epigenetic) requirements, and replication-before-regulation standards. Confirm: the echoes verified with mechanism. Kill: the effects prove non-replicable. Does NOT claim: the transgenerational effects - it verifies the echo.",
 "pointer": "The Signature system's proposed approach tests transgenerational toxicity with rigorous F3 designs; the companion Signature Edition record specifies the echo protocol.",
 "key_points": [
  "Vinclozolin claims sparked the controversy.",
  "F3 generation needed for true transgenerational.",
  "Positive reports replicate inconsistently.",
  "Epigenetic mechanism debated.",
 ],
 "requirements": [
  "Standardized multigenerational (F3) designs.",
  "Mechanism requirements for claims.",
  "Replication-before-regulation standards.",
 ],
 "citations": [
  "Anway MD et al. (2005) Epigenetic transgenerational actions of endocrine disruptors. Science 308.",
 ],
 "demo": {"emax": 72.0, "ec50": 7.5, "n": 1.5, "c": [0.0, 0.75, 7.5, 75.0]},
},
# ----------------------------------------------------------------- rank 28
{
 "key": "tx-microbiome-tox",
 "name": "The Microbiome Toxicity Problem",
 "group": "Mechanisms",
 "ladder_rank": 28, "ladder_tier": "advanced",
 "problem": "Gut microbes metabolize chemicals - but how does the microbiome modify toxicity, and how can it be accounted for?",
 "background": "The microbiome-toxicity problem - microbial metabolism of xenobiotics (digoxin, irinotecan examples) - is the hidden variable: the germ-free vs conventional differences are large; the interpersonal microbiome variation makes the toxicity individual; and the testing (germ-free models) is specialized. The risk assessment assumes a standard human; the microbiome personalizes it. The hidden metabolizers are the individual susceptibility.",
 "why_it_matters": "Microbiome variation personalizes chemical risks. The unaccounted microbes are the individual susceptibility.",
 "sig_lens": "The Signature lens reads the microbiome as the hidden pharmacists: the protocol must consult them - measuring their metabolism - in the risk assessment.",
 "sig_solution": LABEL + " Assumptions: (1) microbial metabolism modifies toxicity substantially; (2) interpersonal variation large. Reasoning path: include the pharmacists - microbiome-aware risk assessment with metabolic profiling. Proposed mechanism: a pharmacists protocol with microbiome-xenobiotic metabolism studies, susceptible-subpopulation identification, and microbiome-inclusive risk models. Confirm: the inclusive models predict variability. Kill: the variation proves unmanageable. Does NOT claim: the microbiome accounted - it consults the pharmacists.",
 "pointer": "The Signature system's proposed approach includes microbiome metabolism in risk assessment; the companion Signature Edition record specifies the pharmacists protocol.",
 "key_points": [
  "Microbes metabolize drugs and pollutants.",
  "Germ-free vs conventional toxicity differs largely.",
  "Interpersonal microbiome variation personalizes risk.",
  "Risk assessment assumes a standard human.",
 ],
 "requirements": [
  "Microbiome-xenobiotic metabolism studies.",
  "Susceptible-subpopulation identification.",
  "Microbiome-inclusive risk models.",
 ],
 "citations": [
  "Clayton TA et al. (2009) Pharmacometabonomic identification of a significant host-microbiome metabolic interaction. PNAS 106.",
 ],
 "demo": {"emax": 82.0, "ec50": 9.5, "n": 1.4, "c": [0.0, 0.95, 9.5, 95.0]},
},
# ----------------------------------------------------------------- rank 29
{
 "key": "tx-immuno",
 "name": "The Immunotoxicity Problem",
 "group": "Mechanisms",
 "ladder_rank": 29, "ladder_tier": "advanced",
 "problem": "Chemicals suppress or hyperactivate immunity - but how can immunotoxicity be detected when the immune system is so complex?",
 "background": "The immunotoxicity problem - PFAS immune suppression (reduced vaccine response), the developmental immunotoxicity (DIT) window - is the testing gap: the guidelines (OECD 443's immunotoxicity cohort) are recent; the functional assays (TDAR) are animal-intensive; and the human relevance (vaccine-response epidemiology) is the gold standard, rarely available. The immune effects are the subtle toxicity; their detection lags.",
 "why_it_matters": "Immune suppression raises infection and cancer risks. The lagging detection is the subtle vulnerability.",
 "sig_lens": "The Signature lens reads immunotoxicity as the weakened guard: the protocol must test the guard's function - not just count the soldiers.",
 "sig_solution": LABEL + " Assumptions: (1) functional assays animal-intensive; (2) human relevance rarely available. Reasoning path: test functionally, human-relevantly - in-vitro immune-function batteries with vaccine-response epidemiology. Proposed mechanism: a guard protocol with immune-function test batteries, developmental immunotoxicity focus, and human vaccine-response studies. Confirm: the batteries predict immune effects. Kill: the function stays untestable in vitro. Does NOT claim: the immunotoxicants all found - it tests the guard.",
 "pointer": "The Signature system's proposed approach tests immune function with human-relevant batteries; the companion Signature Edition record specifies the guard protocol.",
 "key_points": [
  "PFAS linked to reduced vaccine responses.",
  "Developmental immunotoxicity window critical.",
  "TDAR functional assay animal-intensive.",
  "Human vaccine-response epidemiology rare.",
 ],
 "requirements": [
  "In-vitro immune-function batteries.",
  "Developmental immunotoxicity testing.",
  "Human vaccine-response studies.",
 ],
 "citations": [
  "OECD Test Guideline 443 (extended one-generation, immunotoxicity cohort).",
 ],
 "demo": {"emax": 68.0, "ec50": 6.0, "n": 1.7, "c": [0.0, 0.6, 6.0, 60.0]},
},
# ----------------------------------------------------------------- rank 30
{
 "key": "tx-neurodev",
 "name": "The Neurodevelopmental Toxicity Problem",
 "group": "Mechanisms",
 "ladder_rank": 30, "ladder_tier": "advanced",
 "problem": "The developing brain is uniquely vulnerable - but how can neurodevelopmental toxicants be screened without massive animal studies?",
 "background": "The DNT problem - the developing brain's vulnerability (lead, methylmercury lessons) - needs high-throughput screening: the in-vitro batteries (neural differentiation, network formation) are developing; the OECD test guideline (426) is animal-intensive; and the AOPs for DNT are incomplete. The children's brains are the least-protected; their screening is the least-built.",
 "why_it_matters": "Neurodevelopmental toxicants damage children's brains permanently. The least-built screening protects the most vulnerable.",
 "sig_lens": "The Signature lens reads the developing brain as the fragile wiring: the protocol must test the wiring (in-vitro networks) - at scale.",
 "sig_solution": LABEL + " Assumptions: (1) in-vitro batteries developing; (2) DNT AOPs incomplete. Reasoning path: screen at scale - validated in-vitro DNT batteries with AOP anchoring. Proposed mechanism: a wiring protocol with high-throughput DNT screening batteries, AOP-anchored assay development, and regulatory acceptance pathways. Confirm: the batteries predict DNT. Kill: the in-vitro never recapitulates development. Does NOT claim: the DNTs all found - it tests the wiring at scale.",
 "pointer": "The Signature system's proposed approach screens neurodevelopmental toxicity high-throughput; the companion Signature Edition record specifies the wiring protocol.",
 "key_points": [
  "Lead and methylmercury: the historical lessons.",
  "OECD 426 DNT test animal-intensive.",
  "In-vitro neural batteries developing.",
  "DNT adverse-outcome pathways incomplete.",
 ],
 "requirements": [
  "Validated high-throughput DNT batteries.",
  "AOP-anchored assay development.",
  "Regulatory acceptance pathways.",
 ],
 "citations": [
  "OECD Test Guideline 426: Developmental Neurotoxicity Study.",
 ],
 "demo": {"emax": 74.0, "ec50": 7.0, "n": 1.5, "c": [0.0, 0.7, 7.0, 70.0]},
},
# ----------------------------------------------------------------- rank 31
{
 "key": "tx-edsp",
 "name": "The Endocrine Screening Problem",
 "group": "Methods",
 "ladder_rank": 31, "ladder_tier": "advanced",
 "problem": "Thousands of chemicals need endocrine screening - but how can the screening keep up without drowning in animal tests?",
 "background": "The screening problem - EPA's EDSP, OECD's conceptual framework - is the throughput crisis: the Tier 1 battery is slow and animal-intensive; the Tox21/ToxCast high-throughput assays cover the estrogen/androgen/thyroid pathways partially; and the validation for regulatory use lags. The chemical universe needs screening; the screens are half-built.",
 "why_it_matters": "Thousands of chemicals await endocrine screening. The half-built screens are the unassessed universe.",
 "sig_lens": "The Signature lens reads endocrine screening as the net: the protocol must weave it finer (pathway coverage) - and cast it wider (throughput).",
 "sig_solution": LABEL + " Assumptions: (1) Tier 1 slow, animal-intensive; (2) HTS covers pathways partially. Reasoning path: build the HTS net - pathway-complete high-throughput screening with regulatory validation. Proposed mechanism: a net protocol with pathway-complete HTS batteries, regulatory-validation programs, and tiered testing strategies. Confirm: the net catches the EDCs. Kill: the HTS never validates. Does NOT claim: the universe screened - it weaves the net.",
 "pointer": "The Signature system's proposed approach builds pathway-complete endocrine screening; the companion Signature Edition record specifies the net protocol.",
 "key_points": [
  "EDSP Tier 1 slow and animal-intensive.",
  "Tox21/ToxCast cover E/A/T pathways partially.",
  "Regulatory validation of HTS lags.",
  "Thousands of chemicals await screening.",
 ],
 "requirements": [
  "Pathway-complete HTS batteries.",
  "Regulatory validation programs.",
  "Tiered testing strategies.",
 ],
 "citations": [
  "OECD Conceptual Framework for Testing and Assessment of Endocrine Disrupters.",
 ],
 "demo": {"emax": 86.0, "ec50": 10.0, "n": 1.6, "c": [0.0, 1.0, 10.0, 100.0]},
},
# ----------------------------------------------------------------- rank 32
{
 "key": "tx-nam",
 "name": "The New Approach Methodologies Problem",
 "group": "Methods",
 "ladder_rank": 32, "ladder_tier": "advanced",
 "problem": "Animal-free toxicology (NAMs) is the goal - but how can the new methods be validated and accepted fast enough to matter?",
 "background": "The NAMs problem - the validation-acceptance bottleneck - is the paradigm shift's friction: the methods (organ-on-chip, in-silico, HTS) develop fast; the validation (OECD test guidelines) takes years; and the regulatory risk-aversion slows adoption. The animal tests' retirement is the goal; the NAMs' acceptance is the rate-limit. The future methods exist; their acceptance lags.",
 "why_it_matters": "NAMs are the animal-free future. The acceptance lag is the animals still tested.",
 "sig_lens": "The Signature lens reads NAMs as the replacements waiting in the wings: the protocol must get them on stage - validated, accepted, used.",
 "sig_solution": LABEL + " Assumptions: (1) methods develop fast; validation slow; (2) regulatory risk-aversion. Reasoning path: accelerate acceptance - validation science plus regulatory-confidence building. Proposed mechanism: a stage protocol with accelerated validation frameworks, confidence-building case studies, and defined-approach acceptances. Confirm: the NAMs accepted and used. Kill: the acceptance never comes. Does NOT claim: the animals retired - it gets the replacements on stage.",
 "pointer": "The Signature system's proposed approach accelerates NAMs validation and acceptance; the companion Signature Edition record specifies the stage protocol.",
 "key_points": [
  "Organ-on-chip, HTS, in-silico developing fast.",
  "OECD validation takes years.",
  "Regulatory risk-aversion slows adoption.",
  "Acceptance is the rate-limiting step.",
 ],
 "requirements": [
  "Accelerated validation frameworks.",
  "Regulatory confidence case studies.",
  "Defined-approach acceptances.",
 ],
 "citations": [
  "NRC (2007) Toxicity Testing in the 21st Century. National Academies Press.",
 ],
 "demo": {"emax": 90.0, "ec50": 12.5, "n": 1.3, "c": [0.0, 1.25, 12.5, 125.0]},
},
# ----------------------------------------------------------------- rank 33
{
 "key": "tx-uncertainty",
 "name": "The Risk Assessment Uncertainty Problem",
 "group": "Risk Assessment",
 "ladder_rank": 33, "ladder_tier": "advanced",
 "problem": "Risk assessments carry deep uncertainties - but how can they be quantified and communicated honestly?",
 "background": "The uncertainty problem - the assessment factors (10x for animals-to-humans, 10x for variability) are conventions, not measurements - is the risk assessment's honesty gap: the probabilistic methods (WHO/IPCS) exist but are underused; the communication (point estimates vs distributions) misleads; and the decisions need the uncertainty, not the pretense. The factors are placeholders; the quantification is the honesty.",
 "why_it_matters": "Risk decisions need honest uncertainty. The conventional factors are the pretense of precision.",
 "sig_lens": "The Signature lens reads uncertainty as the honest margin: the protocol must quantify it - probabilistically - and print it on every assessment.",
 "sig_solution": LABEL + " Assumptions: (1) assessment factors are conventions; (2) probabilistic methods underused. Reasoning path: quantify probabilistically - WHO/IPCS uncertainty methods with communicated distributions. Proposed mechanism: a margin protocol with probabilistic risk assessment, uncertainty-communicated decisions, and factor-replacement research. Confirm: the quantified assessments decide better. Kill: the quantification stays unused. Does NOT claim: the uncertainty eliminated - it prints the honest margin.",
 "pointer": "The Signature system's proposed approach quantifies risk-assessment uncertainty probabilistically; the companion Signature Edition record specifies the margin protocol.",
 "key_points": [
  "10x factors are conventions, not measurements.",
  "WHO/IPCS probabilistic methods exist, underused.",
  "Point estimates mislead; distributions inform.",
  "Decisions need the uncertainty.",
 ],
 "requirements": [
  "Probabilistic risk-assessment methods.",
  "Uncertainty-communicated decisions.",
  "Assessment-factor replacement research.",
 ],
 "citations": [
  "WHO/IPCS (2018) Guidance Document on Characterizing and Communicating Uncertainty in Exposure Assessment.",
 ],
 "demo": {"emax": 95.0, "ec50": 14.0, "n": 1.4, "c": [0.0, 1.4, 14.0, 140.0]},
},
# ----------------------------------------------------------------- rank 34
{
 "key": "tx-unified",
 "name": "The Unified Toxicology Problem",
 "group": "Risk Assessment",
 "ladder_rank": 34, "ladder_tier": "advanced",
 "problem": "Toxicology is fragmented into endpoints, media, and methods - but can the science of poisons be unified as one predictive discipline?",
 "background": "The unified-toxicology problem - one framework from molecules to populations - is the field's synthesis: the endpoints (cancer, repro, neuro) are separate; the media (air, water, food) are separate; the methods (animal, in-vitro, in-silico) are separate. The AOPs, the exposome, and the NAMs each unify partially. The poisons' science is one; its practice is many.",
 "why_it_matters": "The fragmented toxicology misses the whole organism and the whole exposure. The unification is the predictive discipline.",
 "sig_lens": "The Signature lens reads toxicology as the one science of harm: the protocol must unite it - AOPs to exposome to NAMs - in the predictive framework.",
 "sig_solution": LABEL + " Assumptions: (1) endpoints, media, methods fragmented; (2) partial unifications exist. Reasoning path: integrate the unifiers - AOP networks plus exposome plus NAMs in one predictive framework. Proposed mechanism: a harm protocol with integrated predictive-toxicology platforms, cross-endpoint AOP networks, and unified risk-assessment methods. Confirm: the unified framework predicts across endpoints. Kill: the fragments resist integration. Does NOT claim: toxicology unified - it builds the one science.",
 "pointer": "The Signature system's proposed approach unifies toxicology in a predictive framework; the companion Signature Edition record specifies the harm protocol.",
 "key_points": [
  "Endpoints, media, methods each fragmented.",
  "AOPs, exposome, NAMs unify partially.",
  "The poisons' science is one; practice many.",
  "Predictive discipline is the goal.",
 ],
 "requirements": [
  "Integrated predictive-toxicology platforms.",
  "Cross-endpoint AOP networks.",
  "Unified risk-assessment methods.",
 ],
 "citations": [
  "NRC (2007) Toxicity Testing in the 21st Century. National Academies Press.",
 ],
 "demo": {"emax": 100.0, "ec50": 15.0, "n": 1.5, "c": [0.0, 1.5, 15.0, 150.0]},
},
]
