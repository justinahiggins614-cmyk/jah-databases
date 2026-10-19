#!/usr/bin/env python3
"""Entries for the Unsolved Medicine Database pair (Manon's 16:15 orders,
Unsolved Problems Solved series, batch 1 - medicine).

The halves are two views of the SAME 34 famous unsolved medicine problems:
public = the problem as the world knows it (real, fact-checked); signature =
the same problem through the Signature lens, with the full proposed-solution
treatment. Titles suffixed " (Signature Edition)", src signature, clearly
labeled Signature-made.

Every record carries problem + background + why_it_matters + signature_solution.
The signature_solution opens with the EXACT label "Signature-generated proposed
solution - not established science." Public half carries a short pointer;
signature half carries the full treatment. HONESTY RULE throughout: never
claim proof, never imply peer acceptance, never present speculation as
settled. Proposed solutions are exploratory research directions - NEVER
medical advice or treatment claims. Nothing hate-adjacent, profane, or
inappropriate; no religious talk.

ID prefixes: JAH-USME- (public) and JAH-USMES- (signature), verified free
2026-10-17 in manifest id_prefix values (zero hits) and in all 874 shard
data directories of jah-databases-data-1 (zero hits).

Ladder: 1-34 unique ranks, simple -> compounded -> complex. Foundations 1-12,
Compounded 13-23, Advanced 24-34. The shard index is written in ladder order.

Dedupe: gate.check() on all 68 titles vs the whole system before authoring:
zero collisions, zero refusals.
"""

SIG_TAIL = ("Signature original - his original Signature Lens reading of the "
            "problem and a Signature-generated proposed solution, clearly "
            "labeled Signature-made. Proposed solutions are exploratory "
            "research directions, never medical advice or treatment claims, "
            "and are never presented as established science.")

LABEL = ("Signature-generated proposed solution - not established science.")

# --- shared citations (real landmarks) --------------------------------------
CIT_NIH = ("National Institutes of Health. Understanding the human body and "
           "disease research programs; Bethesda, MD.")
CIT_WHO = ("World Health Organization. Global health estimates and disease "
           "fact sheets; Geneva.")
CIT_NEJM = ("New England Journal of Medicine. Peer-reviewed clinical "
            "research archive.")
CIT_NATURE = ("Nature. Peer-reviewed biomedical research archive.")
CIT_LANCET = ("The Lancet. Peer-reviewed medical research archive.")
CIT_CDC = ("Centers for Disease Control and Prevention. Disease burden and "
           "surveillance reports; Atlanta, GA.")
CIT_ALZ = ("Alzheimer's Association. Alzheimer's Disease Facts and Figures "
           "report series; Chicago, IL.")
CIT_HARRISON = ("Harrison's Principles of Internal Medicine. Standard "
                "clinical reference.")
CIT_ROBBINS = ("Robbins and Cotran Pathologic Basis of Disease. Standard "
               "pathology reference.")
CIT_JANEWAY = ("Janeway's Immunobiology. Standard immunology reference.")
CIT_GUYTON = ("Guyton and Hall Textbook of Medical Physiology. Standard "
              "physiology reference.")
CIT_KANDEL = ("Kandel ER et al. Principles of Neural Science. Standard "
              "neuroscience reference.")
CIT_HALL = CIT_GUYTON

ENTRIES = [
    {
        "key": "common_cold",
        "name": "The Common Cold Problem: Why There Is Still No Cure",
        "group": "Foundations",
        "ladder_rank": 1,
        "ladder_tier": "foundations",
        "description": (
            "THE PROBLEM: humanity has walked on the moon and decoded the "
            "human genome, yet there is still no cure for the common cold - "
            "and no vaccine that prevents it. The common cold is not one "
            "disease but a clinical syndrome caused by more than 200 distinct "
            "viruses: over 160 serotypes of rhinovirus, plus coronaviruses, "
            "adenoviruses, enteroviruses, and others. BACKGROUND: rhinoviruses "
            "were isolated in the 1950s, and early vaccine efforts in the "
            "1960s and 1970s targeted a handful of serotypes at a time. Each "
            "vaccine protected only against the serotypes it contained, while "
            "the other hundred-plus circulated freely. Antiviral drugs ran "
            "into the same wall: agents that blocked one rhinovirus serotype "
            "often failed against others, and blocking the shared cell "
            "receptor (ICAM-1, used by most rhinoviruses to enter cells) "
            "proved too disruptive to normal biology to be a safe drug. "
            "Modern work has mapped the rhinovirus family tree and found "
            "conserved regions - parts of the virus that change little "
            "between serotypes - but turning a conserved target into a "
            "vaccine that generates protective immunity in the human nose "
            "remains unsolved. The cold costs the world billions of lost "
            "workdays every year and is the most common human illness, yet "
            "treatment is still rest, fluids, and symptom relief."
        ),
        "how_it_works": (
            "WHY IT MATTERS: a universal cold vaccine would erase the most "
            "common illness on earth, save enormous economic losses, and - "
            "more importantly - prove the platform for universal vaccines "
            "against far deadlier variable viruses. The same conserved-target "
            "strategy that would beat the cold could beat pandemic influenza "
            "and future coronaviruses. CURRENT STATE: research today focuses "
            "on the conserved inner-shell proteins of rhinoviruses (VP4 and "
            "parts of VP1) rather than the highly variable outer surface, and "
            "on nasal vaccines that build immunity where the virus actually "
            "lands. The honest status is that no candidate has yet shown "
            "broad protection in humans. The problem stands open: either "
            "immunity must be raised against dozens of serotypes at once, or "
            "a truly universal target must be found, or the virus must be "
            "blocked at a shared step of its life cycle without harming the "
            "host."
        ),
        "key_points": [
            "The common cold is a syndrome, not a single virus: 200-plus viruses and 160-plus rhinovirus serotypes cause identical symptoms.",
            "Serotype-specific vaccines failed because immunity to a few serotypes leaves the rest of the family free to infect.",
            "Most rhinoviruses enter cells through ICAM-1, a shared receptor, but blocking a shared human receptor is biologically risky.",
            "Conserved viral regions (VP4, inner VP1) are the current scientific hope for a broadly protective vaccine.",
            "Nasal immunity matters: the virus lands in the nose, so a useful vaccine likely must defend the airway surface, not just the blood.",
        ],
        "requirements": [
            "A solution must protect against the great majority of circulating rhinovirus serotypes, not a handful.",
            "Protection must be demonstrated in humans against natural infection, not only antibody titers in blood.",
            "Any shared-target drug must spare normal ICAM-1 function, which the immune system uses daily.",
            "Safety must be exceptional: the disease is mild, so no vaccine or drug can carry meaningful risk.",
            "Durability matters: protection should last multiple cold seasons, not weeks.",
        ],
        "standards": [
            "Efficacy claims require randomized, placebo-controlled human trials with laboratory-confirmed infection endpoints.",
            "Serotype coverage must be measured against contemporary circulating strains, not laboratory reference strains alone.",
            "Safety follow-up must cover at least one full cold season for any nasal or systemic vaccine.",
        ],
        "citations": [CIT_CDC, CIT_NATURE, CIT_NEJM],
        "sig_lens": (
            "The Signature read: the cold is a swarm, not a target - one "
            "name for two hundred invaders wearing different coats. Public "
            "science aimed at each coat; the Signature lens aims at what no "
            "coat can hide: the machinery every rhinovirus must use to copy "
            "itself once inside."
        ),
    },
    {
        "key": "flu_remade",
        "name": "Why Influenza Vaccines Must Be Remade Every Year",
        "group": "Foundations",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "THE PROBLEM: the influenza vaccine is reformulated almost every "
            "year because the virus keeps changing its face. Influenza "
            "carries two surface proteins, hemagglutinin (HA) and "
            "neuraminidase (NA), that the immune system learns to recognize. "
            "But influenza's copying machinery is sloppy: every replication "
            "introduces mutations, and the strains that escape last year's "
            "immunity are the ones that spread - a process called antigenic "
            "drift. Every few decades a bigger jump, antigenic shift, "
            "reshuffles whole gene segments and can start a pandemic. "
            "BACKGROUND: the first inactivated flu vaccines appeared in the "
            "1940s. Surveillance networks now track circulating strains "
            "worldwide and a committee picks each season's vaccine strains "
            "months ahead of winter - a forecast that is sometimes wrong. "
            "Vaccine effectiveness in a typical year sits around 40 to 60 "
            "percent, far below the protection of vaccines against stable "
            "viruses like measles. The 2009 H1N1 pandemic and the constant "
            "threat of an H5N1 bird-flu jump keep the problem urgent: drift "
            "makes flu a moving target, and we are still throwing seasonal "
            "darts at it."
        ),
        "how_it_works": (
            "WHY IT MATTERS: influenza still kills hundreds of thousands of "
            "people every year and hospitalizes millions. A vaccine that did "
            "not need yearly reformulation - a universal flu vaccine - would "
            "end the forecasting gamble, protect against surprise pandemic "
            "strains, and save the enormous yearly cost of manufacturing and "
            "re-vaccinating the planet. CURRENT STATE: the scientific "
            "consensus target is the HA stem - the stalk of the hemagglutinin "
            "protein, which changes far less than the head that current "
            "vaccines train immunity against. Stem-directed antibodies have "
            "been found in some people and protect animals against many flu "
            "strains. Early human trials of stem-based and mRNA-based "
            "universal candidates are underway. The honest status: no "
            "universal vaccine has yet proven broad, durable protection in "
            "people. Until one does, the yearly reformulation continues."
        ),
        "key_points": [
            "Antigenic drift: flu's error-prone replication mutates the HA and NA surface proteins, escaping last year's immunity.",
            "Antigenic shift: wholesale gene-segment reshuffling can create pandemic strains the population has never seen.",
            "Current vaccines mostly train immunity against the variable HA head, which is why they expire yearly.",
            "The HA stem is conserved across many strains and is the leading universal-vaccine target.",
            "Effectiveness of 40 to 60 percent is typical - useful, but far from the near-total protection of stable-virus vaccines.",
        ],
        "requirements": [
            "A universal vaccine must protect against drifted seasonal strains and shifted pandemic strains alike.",
            "Protection must be shown in humans over multiple seasons, not one winter.",
            "It must work in the elderly and the very young, the groups flu kills most.",
            "Manufacturing must scale to billions of doses without the months-long egg-based forecast cycle.",
            "Any stem-directed immunity must be shown not to backfire through antibody-dependent enhancement.",
        ],
        "standards": [
            "Universal-vaccine trials must predefine breadth endpoints: protection against mismatched and shifted strains.",
            "Strain selection and effectiveness measurement follow WHO global surveillance protocols.",
            "Safety follow-up must span multiple influenza seasons.",
        ],
        "citations": [CIT_WHO, CIT_CDC, CIT_NEJM],
        "sig_lens": (
            "The Signature read: flu is a locksmith that changes the lock "
            "every season while the keyhole - the machinery of entry and "
            "copying - stays the same shape. Public science keeps cutting new "
            "keys; the Signature lens studies the keyhole."
        ),
    },
    {
        "key": "placebo",
        "name": "The Placebo Effect: How Belief Changes Biology",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "THE PROBLEM: give a patient a sugar pill, tell them it is "
            "medicine, and measurable biology changes - pain drops, "
            "Parkinson's tremor eases, gut symptoms calm. The placebo effect "
            "is one of the most replicated findings in medicine and one of "
            "the least understood. It is not imagination: brain imaging shows "
            "real changes in pain circuits, dopamine release, and immune "
            "signaling. The nocebo mirror is equally real - expecting harm "
            "produces real symptoms. BACKGROUND: the effect was documented "
            "systematically by Henry Beecher in 1955, studying wounded "
            "soldiers who felt less pain than their injuries warranted. "
            "Modern work by Fabrizio Benedetti and others showed that "
            "placebo pain relief is blocked by naloxone, proving the body's "
            "own opioid system is involved, and that placebo dopamine "
            "release in Parkinson's patients can reach levels comparable to "
            "real drugs. Conditioning plays a role too: the body learns to "
            "respond to the ritual of treatment. Yet the full chain - from "
            "expectation, through which brain circuits, to which molecular "
            "changes in which tissues - has never been completely mapped. "
            "Drug trials must beat placebo to win approval, which means this "
            "unexplained effect quietly decides which medicines reach "
            "patients."
        ),
        "how_it_works": (
            "WHY IT MATTERS: understanding the placebo mechanism would let "
            "medicine amplify healing deliberately and ethically - boosting "
            "drug effects, cutting doses and side effects, and designing "
            "trials that measure true pharmacology instead of ritual plus "
            "molecule. The nocebo side matters equally: unexplained symptom "
            "reports may be expectation-driven biology, not drug toxicity. "
            "CURRENT STATE: researchers have mapped fragments - endogenous "
            "opioids and cannabinoids in placebo analgesia, dopamine in "
            "placebo motor improvement, prefrontal expectation circuits "
            "driving descending pain control. What is missing is the complete "
            "circuit diagram and the rules: who is a strong responder, which "
            "conditions respond, and how expectation physically reaches the "
            "immune system and gut. The honest status: we know the effect is "
            "real, neurochemical, and powerful, and we do not know how to "
            "prescribe it."
        ),
        "key_points": [
            "Placebo responses are measurable biology - opioid, cannabinoid, and dopamine systems activate, not just reported feelings.",
            "Naloxone blocks placebo pain relief, proving endogenous opioids carry part of the effect.",
            "Expectation and conditioning are the two known drivers: what the patient predicts and what the body has learned.",
            "The nocebo effect is the mirror: expecting harm creates real symptoms and real side-effect reports.",
            "Every drug trial must beat placebo, so this unexplained mechanism quietly gates all of pharmacology.",
        ],
        "requirements": [
            "A complete mechanism must trace the full chain: expectation -> brain circuits -> molecular changes in target tissue.",
            "It must explain individual differences: why some people and some conditions respond strongly and others do not.",
            "It must separate true placebo biology from regression to the mean and natural disease fluctuation.",
            "Any clinical use must be ethical: amplifying healing without deception.",
            "The nocebo arm must be explained by the same framework, not treated as a separate mystery.",
        ],
        "standards": [
            "Placebo-mechanism studies must include no-treatment arms to separate true effect from natural history.",
            "Neuroimaging claims require pre-registered analyses and replication, given the field's history of flexible analysis.",
            "Biomarker readouts (endogenous opioids, dopamine) need direct assay, not inference from symptom scores alone.",
        ],
        "citations": [CIT_KANDEL, CIT_NEJM, CIT_NATURE],
        "sig_lens": (
            "The Signature read: the body is its own pharmacy, and belief is "
            "a key the conscious mind holds to its door. Public science "
            "treats placebo as noise to subtract; the Signature lens treats "
            "it as a signal - proof of an inner dispensary whose formulary "
            "we have never read."
        ),
    },
    {
        "key": "allergy_misfire",
        "name": "The Allergy Misfire: Why the Immune System Attacks Harmless Things",
        "group": "Foundations",
        "ladder_rank": 4,
        "ladder_tier": "foundations",
        "description": (
            "THE PROBLEM: the immune system is a superb defender that "
            "sometimes declares war on peanuts, pollen, and pet dander - "
            "things that cannot hurt anyone. In allergy, harmless proteins "
            "are misread as threats: IgE antibodies arm mast cells, and on "
            "re-exposure the mast cells dump histamine and inflammatory "
            "chemicals, producing sneezing, hives, wheezing, or full "
            "anaphylaxis. BACKGROUND: the hygiene hypothesis, proposed in "
            "1989, noted that children with more early microbial exposure "
            "had fewer allergies, suggesting the immune system needs "
            "training data to calibrate. The idea has grown into the "
            "old-friends and microbiome versions: missing parasites and "
            "altered gut bacteria may leave the immune system trigger-happy. "
            "Yet none of this is settled - allergy rates keep rising in "
            "industrialized countries, food allergies in particular, and the "
            "exact misfire point differs by allergy: some are outgrown, some "
            "are lifelong, and peanut allergy can kill within minutes while "
            "hay fever merely annoys. Immunotherapy (allergy shots, oral "
            "immunotherapy) can retrain tolerance in some patients, proving "
            "the misfire is reversible - but nobody can fully explain why "
            "the misfire happens in the first place."
        ),
        "how_it_works": (
            "WHY IT MATTERS: allergies affect hundreds of millions of "
            "people, food allergies send families to emergency rooms, and "
            "the rising curve suggests something in modern life is breaking "
            "immune calibration. Solving the misfire would prevent allergies "
            "instead of managing them - and the same tolerance machinery is "
            "what fails in autoimmune disease and transplant rejection, so "
            "the answer echoes far beyond sneezing. CURRENT STATE: "
            "researchers know the effector chain (IgE, mast cells, Th2 "
            "skewing) in fine detail, and oral immunotherapy for peanut "
            "allergy won regulatory approval, proving desensitization is "
            "real. The open part is upstream: what decides, in the first "
            "months of life, whether a protein is filed as food or foe? The "
            "microbiome, birth mode, diet timing, and environmental "
            "microbes are all suspects. The honest status: we can describe "
            "the fire in detail and sometimes put it out, but we cannot say "
            "who will catch fire or how to fireproof a child."
        ),
        "key_points": [
            "Allergy is immune misclassification: harmless proteins trigger the IgE-mast cell alarm built for parasites.",
            "The hygiene hypothesis and its microbiome successors blame missing early microbial training, but the proof is incomplete.",
            "Allergy prevalence keeps rising in industrialized countries, especially food allergy in children.",
            "Immunotherapy proves the misfire is reversible - tolerance can be retrained, at least partially.",
            "The tolerance machinery that fails in allergy is the same machinery that fails in autoimmunity and transplant rejection.",
        ],
        "requirements": [
            "A real answer must predict, before symptoms, which infants will develop which allergies.",
            "It must explain the geography: why allergy rates differ so sharply between industrialized and traditional societies.",
            "It must explain specificity: why one child reacts to peanut and not to egg, when both are food proteins.",
            "Prevention must be proven in randomized trials, not inferred from observational associations.",
            "Any tolerance-retraining therapy must show durable, treatment-free remission, not suppression during dosing.",
        ],
        "standards": [
            "Allergy diagnosis for trials requires double-blind placebo-controlled food challenge or equivalent objective confirmation.",
            "Microbiome association claims require longitudinal sampling before disease onset, not cross-sectional snapshots.",
            "Desensitization claims must distinguish temporary desensitization from sustained unresponsiveness after therapy stops.",
        ],
        "citations": [CIT_JANEWAY, CIT_NEJM, CIT_LANCET],
        "sig_lens": (
            "The Signature read: the immune system is a border guard that "
            "learned its trade in a dirtier world and now, idle and "
            "over-trained, invents enemies. Public science catalogs the "
            "false alarms; the Signature lens asks what the guard's original "
            "orders were - and how to reissue them."
        ),
    },
    {
        "key": "chronic_pain",
        "name": "Chronic Pain Without Injury: The Mechanism Problem",
        "group": "Foundations",
        "ladder_rank": 5,
        "ladder_tier": "foundations",
        "description": (
            "THE PROBLEM: pain is supposed to be a signal - tissue is "
            "damaged, the alarm rings, the damage heals, the alarm stops. In "
            "chronic pain the alarm keeps ringing for months or years with "
            "no damage to report, or long after the damage has healed. "
            "Fibromyalgia, chronic back pain without a visible lesion, "
            "complex regional pain syndrome, and phantom limb pain all show "
            "the same puzzle: the pain is undeniably real, the scans are "
            "clean, and the usual painkillers barely touch it. BACKGROUND: "
            "the gate control theory of 1965 first proposed that the spinal "
            "cord actively modulates pain signals rather than relaying them "
            "passively. Later work found central sensitization - the nervous "
            "system turning up its own volume, so that normal touch reads as "
            "pain (allodynia) and mild pain reads as agony (hyperalgesia). "
            "Brain imaging shows chronic pain reshaping pain circuits "
            "themselves. Yet opioids, which crush acute pain, often fail "
            "against chronic pain and bring addiction; and the field still "
            "cannot point to the single switch that flips acute pain into "
            "the chronic state. An estimated one in five adults lives with "
            "chronic pain, making this one of the largest unsolved problems "
            "in medicine by sheer human cost."
        ),
        "how_it_works": (
            "WHY IT MATTERS: chronic pain disables more people than most "
            "diseases, drives the opioid crisis (prescribed for pain that "
            "opioids cannot fix), and costs economies hundreds of billions "
            "yearly. A true mechanism would redirect treatment from "
            "muffling the alarm to resetting the alarm system. CURRENT "
            "STATE: central sensitization is the leading framework, with "
            "glial cell activation in the spinal cord and brain emerging as "
            "a key amplifier - the nervous system's support cells joining "
            "the pain chorus. Research now hunts the transition: what "
            "molecular events in the first weeks after injury decide whether "
            "pain resolves or becomes self-sustaining? The honest status: we "
            "have strong suspects (glia, descending modulation failure, "
            "cortical reorganization) and weak treatments. Nobody can yet "
            "measure the volume knob directly or turn it down on demand."
        ),
        "key_points": [
            "Chronic pain is pain decoupled from damage: the alarm system itself becomes the disease.",
            "Central sensitization turns up neural volume - normal touch becomes painful, mild pain becomes severe.",
            "Opioids often fail against chronic pain while causing addiction, proving acute and chronic pain are different beasts.",
            "Glial cells in the spinal cord and brain are emerging as amplifiers of the pain signal.",
            "One in five adults lives with chronic pain - among the largest unsolved burdens in medicine.",
        ],
        "requirements": [
            "A mechanism must explain the transition: the molecular events that convert acute pain into self-sustaining chronic pain.",
            "It must be measurable - a biomarker or imaging readout of the sensitized state, not just patient report.",
            "It must explain the varieties: why fibromyalgia, phantom limb, and CRPS share features but differ in detail.",
            "A treatment derived from it must reset the system, not merely sedate the patient.",
            "It must account for the placebo-responsiveness of chronic pain without dismissing the pain as imaginary.",
        ],
        "standards": [
            "Chronic pain trials require validated pain scales plus functional outcomes, since pain scores alone are noisy.",
            "Central sensitization claims need objective correlates (quantitative sensory testing, imaging) alongside reports.",
            "Opioid-sparing claims must be measured against addiction and misuse endpoints, not just pain scores.",
        ],
        "citations": [CIT_KANDEL, CIT_NEJM, CIT_LANCET],
        "sig_lens": (
            "The Signature read: the nervous system is a scribe that learned "
            "to write the word PAIN so well it kept writing after the "
            "dictation ended. Public science studies the ink; the Signature "
            "lens studies the hand - the learning rule that taught the alarm "
            "to ring itself."
        ),
    },
    {
        "key": "migraine",
        "name": "Migraine: Cause and Reliable Prevention",
        "group": "Foundations",
        "ladder_rank": 6,
        "ladder_tier": "foundations",
        "description": (
            "THE PROBLEM: migraine strikes about one in seven people, yet "
            "medicine still cannot say exactly what a migraine IS. Is it a "
            "blood vessel disorder, a brain excitability disorder, an "
            "inflammatory event, or all three in sequence? The aura - "
            "visual shimmering, numbness - marches across the senses at the "
            "speed of cortical spreading depression, a slow wave of neural "
            "silencing first described in the 1940s. Then comes the headache, "
            "often one-sided, with nausea and light sensitivity, lasting "
            "hours to days. BACKGROUND: for decades migraine was blamed on "
            "blood vessels constricting then dilating, and the triptan drugs "
            "were built on that theory - they work, but imperfectly. The "
            "1990s discovery that CGRP, a neuropeptide, surges during "
            "migraine led to the new CGRP-blocking drugs, the first "
            "preventives designed from migraine biology rather than borrowed "
            "from epilepsy or blood pressure medicine. They help many "
            "patients and fail many others. Triggers are famously personal "
            "and inconsistent - the same food, weather, or stress triggers an "
            "attack one week and not the next - which suggests the trigger "
            "is not the cause but the last straw on a primed brain. What "
            "primes the brain, and what the migraine is FOR, remain open."
        ),
        "how_it_works": (
            "WHY IT MATTERS: migraine is a leading cause of disability "
            "worldwide, stealing workdays and lives' worth of hours from "
            "people in their most productive years. Reliable prevention "
            "would return that time. Deeper still, migraine is a window into "
            "how the brain regulates its own excitability - solving it would "
            "illuminate epilepsy, chronic pain, and sensory processing "
            "itself. CURRENT STATE: CGRP blockers proved that targeting "
            "migraine-specific biology beats repurposed drugs, but a third "
            "or more of patients get little relief, and the drugs treat the "
            "attack cascade rather than the priming. Research now focuses on "
            "the hypothalamus and brainstem as the attack generators and on "
            "genetic studies of familial migraine, which implicate ion "
            "channels - the brain's electrical gates. The honest status: we "
            "have better hammers for the headache and still no blueprint of "
            "the machine that schedules the attacks."
        ),
        "key_points": [
            "Migraine's aura matches cortical spreading depression - a slow wave of neural silencing crossing the cortex.",
            "The vascular theory built triptans; the CGRP discovery built the first migraine-designed preventives.",
            "CGRP blockers help many but fail a third or more of patients - the cascade is treated, not the priming.",
            "Triggers are inconsistent, suggesting they are last straws on a primed brain rather than causes.",
            "Familial migraine genetics point to ion channels - the brain's electrical gates - as suspects.",
        ],
        "requirements": [
            "A cause must explain the full sequence: priming, aura, headache, nausea, and the postdrome hangover.",
            "It must explain episodicity: why attacks come and go rather than striking constantly.",
            "Prevention must work across migraine subtypes, including migraine without aura and chronic migraine.",
            "It must explain the sex difference: migraine is two to three times more common in women.",
            "Any priming biomarker must predict attacks before they start, enabling true prevention.",
        ],
        "standards": [
            "Migraine prevention trials use monthly migraine-day reduction as the primary endpoint with pre-registered analysis.",
            "Aura claims require documented visual or sensory mapping, not retrospective recall alone.",
            "Genetic associations need genome-wide significance and replication in independent cohorts.",
        ],
        "citations": [CIT_KANDEL, CIT_NEJM, CIT_LANCET],
        "sig_lens": (
            "The Signature read: the migraine brain is an instrument tuned "
            "too sharp - every string true, every touch too loud. Public "
            "science muffles the strings one by one; the Signature lens "
            "asks who tuned the instrument sharp, and whether the tuning peg "
            "can be turned back."
        ),
    },
    {
        "key": "sleep_biology",
        "name": "Why We Must Sleep: The Full Biology of Sleep",
        "group": "Foundations",
        "ladder_rank": 7,
        "ladder_tier": "foundations",
        "description": (
            "THE PROBLEM: every animal with a nervous system sleeps, humans "
            "spend a third of life doing it, and total sleep deprivation "
            "kills laboratory animals within weeks - yet biology still lacks "
            "a complete answer to what sleep is FOR. It is not mere rest: "
            "the sleeping brain is wildly active, cycling through stages "
            "with distinct electrical signatures. BACKGROUND: the "
            "electroencephalogram revealed REM sleep in the 1950s - the "
            "stage of vivid dreaming, when the brain is nearly as active as "
            "waking while the body lies paralyzed. Memory researchers showed "
            "that sleep consolidates learning: skills and facts practiced by "
            "day are replayed and strengthened by night. In 2012 the "
            "glymphatic system was discovered - a brain-wide plumbing "
            "network that flushes metabolic waste during sleep, including "
            "the amyloid proteins implicated in Alzheimer disease. "
            "Immune function, hormone regulation, and emotional processing "
            "all lean on sleep. But these are functions sleep SERVES, not a "
            "unified theory of why unconsciousness is the price. The "
            "synaptic homeostasis hypothesis proposes sleep exists to "
            "downscale the day's synaptic strengthening, keeping the brain's "
            "wiring affordable - elegant, influential, and still unproven as "
            "the whole story."
        ),
        "how_it_works": (
            "WHY IT MATTERS: sleep loss is a public health crisis tied to "
            "obesity, diabetes, heart disease, depression, and dementia - "
            "and modern life keeps stealing it. A complete biology of sleep "
            "would turn sleep from lifestyle advice into precision medicine: "
            "knowing exactly what each stage does would let doctors "
            "prescribe sleep the way they prescribe drugs. It would also "
            "settle whether the brain can ever be safely kept awake longer, "
            "or whether the debt always comes due. CURRENT STATE: the field "
            "has catalogued sleep's jobs - memory consolidation, waste "
            "clearance, immune support, emotional regulation, synaptic "
            "downscaling - without agreeing on which are the load-bearing "
            "walls and which are decoration. The honest status: we know "
            "dozens of things sleep does and still cannot write the single "
            "sentence that says why an animal must surrender consciousness "
            "for hours every day."
        ),
        "key_points": [
            "Sleep is universal in animals with nervous systems and fatal when totally prevented - it is load-bearing, not optional.",
            "REM sleep pairs a near-waking brain with a paralyzed body; non-REM stages carry distinct electrical signatures.",
            "The glymphatic system flushes brain waste during sleep, including Alzheimer-linked amyloid.",
            "The synaptic homeostasis hypothesis proposes sleep downscales the day's synaptic strengthening - elegant but unproven as the full story.",
            "Chronic sleep loss tracks with obesity, diabetes, heart disease, depression, and dementia.",
        ],
        "requirements": [
            "A complete theory must explain why unconsciousness is required - why the jobs cannot be done awake.",
            "It must assign each sleep stage its necessary function and show what breaks when that stage alone is removed.",
            "It must explain the universality: the theory should hold from fruit fly to human.",
            "It must predict the dose-response: how much sleep of which kind prevents which specific harm.",
            "Any intervention claiming to replace sleep must demonstrate all of sleep's functions, not just alertness.",
        ],
        "standards": [
            "Sleep-stage claims require polysomnography with standardized scoring, not self-reported sleep.",
            "Causal claims about sleep loss need experimental deprivation or extension designs, not correlational surveys.",
            "Glymphatic findings in animals require human validation before clinical interpretation.",
        ],
        "citations": [CIT_KANDEL, CIT_GUYTON, CIT_NATURE],
        "sig_lens": (
            "The Signature read: sleep is the brain's night shift - the "
            "crew that comes in when the office empties to file the day's "
            "papers, take out the trash, and rebalance the books. Public "
            "science has listed the crew's tasks; the Signature lens asks "
            "for the foreman's ledger - the single account that explains "
            "why the office must close at all."
        ),
    },
    {
        "key": "obesity_setpoint",
        "name": "The Obesity Set-Point Problem",
        "group": "Foundations",
        "ladder_rank": 8,
        "ladder_tier": "foundations",
        "description": (
            "THE PROBLEM: the body defends its weight like a thermostat "
            "defends a temperature setting - dieters lose pounds and the "
            "body fights back with hunger, slowed metabolism, and hormonal "
            "shifts that persist for years, driving the weight back up. This "
            "is the set-point problem: somewhere in the brain, a defended "
            "weight is encoded, and willpower is fighting physiology. "
            "BACKGROUND: the 1994 discovery of leptin - the fat-derived "
            "hormone that tells the brain how much energy is stored - "
            "seemed to crack the code. But obese patients already have "
            "sky-high leptin; their brains simply stop listening, a state "
            "called leptin resistance. The hypothalamus integrates leptin, "
            "ghrelin, insulin, and gut hormones into hunger and satiety, and "
            "the GLP-1 drugs (semaglutide and cousins) proved the system is "
            "druggable - patients lose 15 percent or more of body weight. "
            "Yet stop the drug and the weight returns, because the set-point "
            "itself never moved. Meanwhile obesity rates have tripled "
            "worldwide since 1975, and the environment - cheap calories, "
            "engineered foods, sleep loss, stress - keeps pushing the "
            "thermostat up. What sets the set-point, and how to reset it "
            "permanently, is unsolved."
        ),
        "how_it_works": (
            "WHY IT MATTERS: obesity drives type 2 diabetes, heart disease, "
            "many cancers, and joint destruction - it is among the largest "
            "preventable burdens on human health. GLP-1 drugs help millions "
            "but require lifelong, expensive treatment; moving the set-point "
            "itself would be a true cure rather than a subscription. "
            "CURRENT STATE: the field knows the signaling cast (leptin, "
            "ghrelin, GLP-1, insulin, hypothalamic circuits) and can now "
            "push the system pharmacologically. The open questions are the "
            "deep ones: where exactly the defended weight is stored in "
            "neural circuitry, why the defense strengthens after weight "
            "loss (the Biggest Loser studies showed metabolisms still "
            "suppressed years later), and what environmental signals ratchet "
            "the set-point upward across generations. The honest status: we "
            "can override the thermostat with drugs, but we cannot yet "
            "reprogram it."
        ),
        "key_points": [
            "The body defends weight like a thermostat: weight loss triggers hunger, metabolic slowdown, and hormonal countermeasures lasting years.",
            "Leptin discovery revealed the signal; leptin resistance revealed the brain can go deaf to it.",
            "GLP-1 drugs prove the appetite system is druggable - but stopping them returns the weight, since the set-point never moved.",
            "Obesity has tripled worldwide since 1975, implicating environmental drivers beyond individual choice.",
            "Metabolic suppression after weight loss can persist for years, as long-term follow-up studies documented.",
        ],
        "requirements": [
            "A solution must move the defended weight itself, with weight staying off after treatment ends.",
            "It must locate the set-point in neural circuitry - which neurons, which plasticity rules.",
            "It must explain leptin resistance: the molecular basis of the brain going deaf to the satiety signal.",
            "It must separate the environmental drivers that ratchet set-points upward across populations.",
            "Safety must be metabolic, not just cosmetic: no trading fat for muscle, bone, or hormonal wreckage.",
        ],
        "standards": [
            "Weight-loss claims require at least one year of follow-up, with regain curves published, not just peak loss.",
            "Set-point claims need demonstration of defended weight after intervention withdrawal.",
            "Metabolic endpoints (insulin sensitivity, lipids, body composition) must accompany scale weight.",
        ],
        "citations": [CIT_NEJM, CIT_NATURE, CIT_GUYTON],
        "sig_lens": (
            "The Signature read: the body keeps a ledger of plenty and "
            "famine written in hormones, and the modern world forged the "
            "entries. Public science found the ink (leptin, GLP-1); the "
            "Signature lens hunts the handwriting - the neural ledger where "
            "the defended number is written, and the eraser that could "
            "rewrite it."
        ),
    },
    {
        "key": "vaccine_durability",
        "name": "Vaccine Durability: Why Immunity Fades",
        "group": "Foundations",
        "ladder_rank": 9,
        "ladder_tier": "foundations",
        "description": (
            "THE PROBLEM: some vaccines protect for life (measles, yellow "
            "fever) while others fade in months (COVID boosters, pertussis, "
            "seasonal flu). Medicine can build immunity but cannot reliably "
            "predict how long it will last - or why the same immune system "
            "remembers measles forever and forgets pertussis in a decade. "
            "BACKGROUND: immunology textbooks teach that long-lived plasma "
            "cells in the bone marrow pump out antibodies for decades, while "
            "memory B and T cells wait for re-exposure. The measles vaccine "
            "induces both durably. But the pertussis vaccine's protection "
            "wanes within years, COVID vaccine protection against infection "
            "fades in months (protection against severe disease lasts "
            "longer), and nobody fully understands the difference. Candidate "
            "explanations include the pathogen's own immune-evasion tricks, "
            "the type of vaccine platform (live vs. inactivated vs. mRNA), "
            "the route of exposure, and original antigenic sin - the "
            "immune system's habit of recalling its first answer to a "
            "pathogen family instead of learning the new variant. The "
            "practical cost is enormous: booster campaigns, resurgent "
            "whooping cough, and a public confused about why some shots are "
            "once-in-a-lifetime and others are seasonal subscriptions."
        ),
        "how_it_works": (
            "WHY IT MATTERS: durable immunity is the difference between "
            "eradicating a disease and managing it forever. If vaccinology "
            "could guarantee decades-long protection on demand, booster "
            "logistics would shrink, vaccine hesitancy driven by booster "
            "fatigue would ease, and pandemic vaccines could be one-and-done. "
            "CURRENT STATE: researchers compare durable and fading vaccines "
            "side by side, hunting the molecular signature of longevity in "
            "germinal centers - the lymph-node structures where B cells "
            "refine their antibodies. Early findings suggest the duration "
            "and quality of the germinal center reaction predicts plasma "
            "cell longevity. Adjuvants (vaccine additives) are being "
            "engineered to mimic the signals of long-lasting natural "
            "infection. The honest status: vaccinology remains partly "
            "empirical - we discover durability by waiting years and "
            "watching, because no short-term measurement yet reliably "
            "predicts decades of protection."
        ),
        "key_points": [
            "Measles vaccine protects for life; pertussis and COVID protection against infection fade in months to years - same immune system, different memory.",
            "Long-lived plasma cells in bone marrow are the presumed source of durable antibody, but what creates them is unclear.",
            "Original antigenic sin may trap the immune system in its first answer to a pathogen family.",
            "Germinal center quality is emerging as a predictor of how long protection lasts.",
            "Current vaccinology is partly empirical: durability is discovered by waiting, not predicted by design.",
        ],
        "requirements": [
            "A theory of durability must predict, from early immune measurements, how long protection will last.",
            "It must explain the spectrum: why live measles vaccine endures while acellular pertussis fades.",
            "Vaccine designs derived from it must show multi-year protection in humans, not just peak antibody titers.",
            "It must handle pathogen evolution: durability against the original strain means little if the target drifts.",
            "Booster strategies must be rationalized: who needs them, when, and with what formulation.",
        ],
        "standards": [
            "Durability claims require multi-year follow-up with clinical endpoints, not antibody titers alone.",
            "Correlates of protection must be validated prospectively before replacing efficacy trials.",
            "Comparisons across vaccine platforms need matched populations and exposure risks.",
        ],
        "citations": [CIT_JANEWAY, CIT_NEJM, CIT_CDC],
        "sig_lens": (
            "The Signature read: the immune system is a library, and some "
            "vaccines get shelved in the permanent collection while others "
            "are left on the returns cart. Public science reshelves by "
            "trial and error; the Signature lens studies the librarian - "
            "the germinal center's decision rule for what is worth "
            "remembering forever."
        ),
    },
]

ENTRIES.extend([
    {
        "key": "sepsis",
        "name": "Sepsis: The Immune Storm With No Specific Drug",
        "group": "Foundations",
        "ladder_rank": 10,
        "ladder_tier": "foundations",
        "description": (
            "THE PROBLEM: sepsis kills an estimated 11 million people a "
            "year - one in five deaths worldwide - and there is still no "
            "drug that treats sepsis itself. Sepsis is not the infection; "
            "it is the body's catastrophic overreaction to infection. "
            "Bacteria, viruses, or fungi trigger the immune system, and the "
            "immune system responds so violently that it destroys the "
            "patient's own organs: blood pressure collapses, kidneys fail, "
            "lungs fill, clotting runs wild. Antibiotics kill the invader, "
            "but the storm, once started, runs on its own. BACKGROUND: for "
            "decades sepsis was treated as runaway inflammation, and a "
            "generation of anti-inflammatory drugs was tested - steroids, "
            "anti-TNF antibodies, activated protein C. Nearly all failed. "
            "The field then realized sepsis is not one thing: early "
            "hyper-inflammation can flip into profound immune paralysis, "
            "where the patient cannot fight off even trivial secondary "
            "infections. Two patients with the same bacteria can be in "
            "opposite immune states. This heterogeneity is why one-size "
            "trials keep failing: the drug that helps the inflamed patient "
            "may kill the immunosuppressed one. Modern care is supportive - "
            "fluids, vasopressors, ventilation, antibiotics - buying time "
            "while the storm decides the outcome."
        ),
        "how_it_works": (
            "WHY IT MATTERS: sepsis is among the top killers in hospitals "
            "everywhere, striking newborns, the elderly, and the previously "
            "healthy alike. A drug that calmed the storm - or better, "
            "steered each patient's immune state back to balance - would "
            "save millions yearly and transform intensive care. CURRENT "
            "STATE: the frontier is immune staging - rapid tests that read "
            "whether a septic patient is in the hyper-inflammatory or the "
            "paralyzed phase, so therapy can be matched to state. "
            "Transcriptomic signatures (gene-activity patterns in blood) "
            "can now classify patients within hours in research settings. "
            "The honest status: we can describe the storm in exquisite "
            "detail and still cannot prescribe for it specifically. Until "
            "staging reaches the bedside and state-matched drugs pass "
            "trials, sepsis remains medicine's most lethal unsolved "
            "emergency."
        ),
        "key_points": [
            "Sepsis is the host response, not the infection: the immune overreaction destroys the patient's own organs.",
            "An estimated 11 million deaths yearly - one in five deaths worldwide - with no disease-specific drug.",
            "A generation of anti-inflammatory sepsis drugs failed, revealing sepsis is not one immune state but several.",
            "Hyper-inflammation can flip into immune paralysis; the same drug can help one phase and harm the other.",
            "Care remains supportive: antibiotics, fluids, vasopressors, ventilation - buying time while the storm runs.",
        ],
        "requirements": [
            "A therapy must be matched to immune state: staging the patient (inflamed vs. paralyzed) before drugging the storm.",
            "Staging must be rapid - a bedside or near-bedside test, since sepsis kills in hours.",
            "Trials must stratify by immune state rather than lumping all sepsis together as past failures did.",
            "The drug must modulate, not merely suppress: the patient still needs to fight the original infection.",
            "Prevention counts too: any therapy must be weighed against faster infection control and vaccination.",
        ],
        "standards": [
            "Sepsis trials use the Sepsis-3 definitions (suspected infection plus organ dysfunction) for enrollment consistency.",
            "Immune-state claims require validated transcriptomic or protein signatures with pre-registered cutoffs.",
            "Mortality endpoints need 28-day follow-up minimum; surrogate biomarker wins do not count as cures.",
        ],
        "citations": [CIT_NEJM, CIT_LANCET, CIT_WHO],
        "sig_lens": (
            "The Signature read: sepsis is a fire department that burns the "
            "city to save it - heroism without a commander. Public science "
            "tried to disarm the firefighters; the Signature lens asks for "
            "the commander's radio: a signal that tells each unit, in real "
            "time, whether to charge or stand down."
        ),
    },
    {
        "key": "long_covid",
        "name": "Long COVID and Post-Viral Syndromes",
        "group": "Foundations",
        "ladder_rank": 11,
        "ladder_tier": "foundations",
        "description": (
            "THE PROBLEM: for millions of people, the virus leaves but the "
            "illness stays. Months or years after infection, patients report "
            "crushing fatigue, brain fog, breathlessness, racing hearts, and "
            "post-exertional crashes - with standard tests showing nothing "
            "wrong. Long COVID made post-viral illness impossible to ignore, "
            "but it is not new: similar syndromes follow Epstein-Barr virus, "
            "SARS, influenza, and other infections, and myalgic "
            "encephalomyelitis/chronic fatigue syndrome (ME/CFS) has "
            "described the same territory for decades without a settled "
            "cause. BACKGROUND: competing explanations each have partial "
            "evidence. Viral persistence: fragments of virus or viral "
            "protein linger in tissues, keeping the immune system alarmed. "
            "Autoimmunity: the infection triggers antibodies against the "
            "patient's own tissues. Microclots: tiny clots impair oxygen "
            "delivery. Autonomic damage: the nervous system's autopilot is "
            "injured, explaining the racing heart and dizziness. Mitochondrial "
            "dysfunction: cells cannot make energy properly. The brutal "
            "truth is that different patients may be living different "
            "mechanisms under one umbrella name - which is why no single "
            "treatment has worked broadly, and why the condition spent "
            "decades being dismissed before the pandemic forced the reckoning."
        ),
        "how_it_works": (
            "WHY IT MATTERS: tens of millions live with long COVID "
            "worldwide, many unable to work; ME/CFS patients waited decades "
            "for the research attention the pandemic finally brought. A "
            "mechanism would end the era of normal-tests dismissal and open "
            "targeted treatment. CURRENT STATE: large research programs are "
            "phenotyping patients deeply - immune profiles, clotting "
            "markers, autonomic testing, exercise physiology - hunting "
            "subgroups with distinct biology. Early signals include "
            "endothelial dysfunction, viral reservoir signatures, and "
            "measurable exercise intolerance on cardiopulmonary testing. "
            "The honest status: the field has moved from 'is it real' to "
            "'which of several real things is it in this patient,' and no "
            "unified mechanism or broadly effective treatment exists yet."
        ),
        "key_points": [
            "Post-viral syndromes are not new: ME/CFS and post-SARS syndromes described the same territory decades before COVID.",
            "Standard tests are often normal despite disabling symptoms - the pathology hides below routine measurement.",
            "Competing mechanisms (viral persistence, autoimmunity, microclots, autonomic injury, mitochondrial failure) each have partial evidence.",
            "Different patients may have different mechanisms under one umbrella name - explaining why no single treatment works broadly.",
            "Post-exertional crashes are a hallmark: exertion worsens the illness, defying standard rehabilitation logic.",
        ],
        "requirements": [
            "A mechanism must explain the normal tests: the pathology must be measurable with the right instrument, not invisible by definition.",
            "It must account for subgroups: the biology of the breathless patient may differ from that of the brain-fogged one.",
            "It must explain post-exertional malaise, the signature feature that separates this from ordinary fatigue.",
            "Treatments must be tested against objective function (exercise capacity, work return), not only symptom scores.",
            "Prevention matters equally: understanding who develops post-viral illness after infection is part of the answer.",
        ],
        "standards": [
            "Post-viral syndrome studies need infected-but-recovered controls, not only healthy controls.",
            "Exercise intolerance claims require two-day cardiopulmonary exercise testing with pre-registered protocols.",
            "Viral persistence claims need tissue-level detection with contamination controls, not PCR fragments alone.",
        ],
        "citations": [CIT_NEJM, CIT_NATURE, CIT_LANCET],
        "sig_lens": (
            "The Signature read: the war ended but the soldiers never got "
            "the ceasefire order - alarms still ringing in empty streets. "
            "Public science debates which street the alarm is on; the "
            "Signature lens hunts the broken telegraph: the all-clear "
            "signal the body failed to send."
        ),
    },
    {
        "key": "antibiotic_resistance",
        "name": "Antibiotic Resistance: Outrunning the Resistant Microbe",
        "group": "Foundations",
        "ladder_rank": 12,
        "ladder_tier": "foundations",
        "description": (
            "THE PROBLEM: antibiotics were humanity's miracle - then bacteria "
            "started reading the playbook. Resistant infections now kill an "
            "estimated 1.27 million people directly each year, and the "
            "pipeline of new antibiotics has slowed to a trickle because "
            "the economics are broken: a new antibiotic is used sparingly "
            "to preserve it, which means it earns little, which means "
            "companies stop developing them. BACKGROUND: Alexander Fleming "
            "warned in his 1945 Nobel lecture that underdosing penicillin "
            "would breed resistance - and it did, within years. Bacteria "
            "swap resistance genes like trading cards through horizontal "
            "gene transfer, spreading a winning defense across species in "
            "months. Methicillin-resistant Staphylococcus aureus (MRSA), "
            "carbapenem-resistant Enterobacterales, and drug-resistant "
            "tuberculosis each defeated drug after drug. The modern nightmare "
            "is pan-resistance: infections treatable by nothing. Agriculture "
            "poured fuel on the fire, dosing livestock with tons of "
            "antibiotics yearly. Stewardship programs try to ration the "
            "remaining drugs, but rationing a dwindling arsenal is a "
            "retreat, not a solution."
        ),
        "how_it_works": (
            "WHY IT MATTERS: without working antibiotics, modern medicine "
            "unravels - not just infections, but surgery, chemotherapy, "
            "organ transplants, and childbirth all depend on infection "
            "control. The World Health Organization ranks antimicrobial "
            "resistance among the top global health threats. CURRENT STATE: "
            "science is attacking on several fronts. Phage therapy - viruses "
            "that eat bacteria - is being revived with modern engineering. "
            "Anti-virulence drugs aim to disarm bacteria rather than kill "
            "them, reducing the evolutionary pressure that breeds "
            "resistance. CRISPR-based antimicrobials could cut resistance "
            "genes directly. Rapid diagnostics would let doctors prescribe "
            "the right drug in minutes instead of blasting broad-spectrum "
            "antibiotics for days. The honest status: the biology is "
            "inventive, the economics are broken, and resistance is "
            "currently outrunning the pipeline. A technical fix without an "
            "economic fix will not hold."
        ),
        "key_points": [
            "Resistant infections kill an estimated 1.27 million people directly per year - and the number is rising.",
            "Horizontal gene transfer lets bacteria trade resistance genes across species in months.",
            "Fleming himself warned in 1945 that underdosing would breed resistance; it did within years.",
            "The antibiotic pipeline is economically broken: conserved drugs earn little, so development stalls.",
            "Without working antibiotics, surgery, chemotherapy, transplants, and childbirth all become far more dangerous.",
        ],
        "requirements": [
            "New approaches must impose less evolutionary pressure than kill-everything antibiotics, or resistance will repeat.",
            "Rapid diagnostics must identify the pathogen and its resistances in minutes at the bedside.",
            "The economic model must be fixed: new antibiotics need pull incentives that reward availability, not sales volume.",
            "Agricultural antibiotic use must be curtailed globally, since resistance ignores borders.",
            "Any anti-virulence or phage therapy must prove it does not simply select for new evasions.",
        ],
        "standards": [
            "Resistance burden estimates follow standardized attributable-mortality methods with uncertainty intervals.",
            "New antibiotic trials require superiority or non-inferiority against resistant-pathogen infections specifically.",
            "Phage therapy claims need defined phage cocktails with manufacturing and resistance-monitoring standards.",
        ],
        "citations": [CIT_WHO, CIT_CDC, CIT_LANCET],
        "sig_lens": (
            "The Signature read: we fought an arms race against an enemy "
            "that evolves faster than we invent - and we armed it ourselves "
            "with every careless prescription. Public science builds bigger "
            "guns; the Signature lens studies the enemy's mail: the gene "
            "trade itself, and whether the letters can be intercepted."
        ),
    },
    {
        "key": "autoimmune_triggers",
        "name": "Autoimmune Disease Triggers: What Flips Immune Tolerance",
        "group": "Compounded",
        "ladder_rank": 13,
        "ladder_tier": "compounded",
        "description": (
            "THE PROBLEM: in autoimmune disease the immune system - the "
            "body's defense force - turns its weapons on the body's own "
            "tissues. Lupus attacks everywhere at once; multiple sclerosis "
            "strips the insulation from nerves; rheumatoid arthritis eats "
            "the joints; type 1 diabetes kills the insulin factories. Over "
            "80 autoimmune diseases are catalogued, affecting up to one in "
            "ten people, and for nearly all of them the triggering event is "
            "unknown. BACKGROUND: the immune system learns self-tolerance "
            "early - in the thymus, developing immune cells that react "
            "strongly to the body's own proteins are deleted, and regulatory "
            "T cells patrol for escapees. Something breaks this truce. "
            "Suspects include molecular mimicry (a microbe that resembles a "
            "self-protein, so the defense against the invader cross-fires "
            "onto the self), the Epstein-Barr virus (now strongly linked to "
            "multiple sclerosis by a landmark 2022 study of 10 million "
            "military personnel), gut microbiome shifts, vitamin D "
            "deficiency, and plain genetic bad luck in immune genes. Women "
            "are struck far more often than men, for reasons still debated. "
            "Current treatments mostly suppress the whole immune system - "
            "effective, but leaving patients vulnerable to infections and "
            "cancers. Nobody can yet point to the moment tolerance breaks "
            "and say: there, that is where we intervene."
        ),
        "how_it_works": (
            "WHY IT MATTERS: autoimmune diseases are chronic, often strike "
            "the young, and accumulate lifelong disability and drug toxicity. "
            "Finding the trigger would allow prevention - vaccinating "
            "against the triggering microbe, correcting the microbiome, or "
            "catching the break early - and finding the tolerance switch "
            "would allow cures that retrain the immune system instead of "
            "suppressing it forever. CURRENT STATE: the Epstein-Barr-MS "
            "link is the strongest trigger evidence the field has ever had, "
            "and EBV vaccine efforts now carry autoimmune prevention as an "
            "explicit goal. Antigen-specific tolerance therapies - retraining "
            "the immune system against one self-protein without suppressing "
            "everything - are in early trials. The honest status: we have "
            "one strong trigger suspect for one disease, a good map of the "
            "tolerance machinery, and no general theory of the break. The "
            "truce fails, and we still do not know exactly why."
        ),
        "key_points": [
            "Over 80 autoimmune diseases affect up to one in ten people; the triggering event is unknown for nearly all.",
            "Self-tolerance is learned in the thymus and policed by regulatory T cells - the truce both systems enforce.",
            "The 2022 study of 10 million military personnel made Epstein-Barr virus the strongest trigger suspect ever found, for multiple sclerosis.",
            "Molecular mimicry - microbe resembling self-protein - is the leading mechanistic suspect for the initial break.",
            "Current treatments suppress the whole immune system; the goal is antigen-specific retraining instead.",
        ],
        "requirements": [
            "A trigger theory must explain timing: why disease starts at a particular age, often years after the suspected trigger.",
            "It must explain the sex bias: most autoimmune diseases strike women far more often.",
            "It must distinguish trigger from bystander: infection history is universal, autoimmunity is not.",
            "Tolerance-retraining therapies must prove durable, drug-free remission - not suppression during treatment.",
            "Prevention trials (e.g., EBV vaccine against MS) need decades of follow-up by design.",
        ],
        "standards": [
            "Trigger associations require prospective cohorts with pre-disease samples, not retrospective recall.",
            "Autoimmune trial endpoints need objective disease-activity measures plus patient function, not biomarkers alone.",
            "Tolerance-therapy claims must demonstrate antigen specificity: the rest of immunity stays intact.",
        ],
        "citations": [CIT_JANEWAY, CIT_NEJM, CIT_NATURE],
        "sig_lens": (
            "The Signature read: the guard turned on the city it was sworn "
            "to protect - and nobody heard the order given. Public science "
            "has mapped the mutiny in detail; the Signature lens rewinds "
            "the tape to the moment before, hunting the whisper - microbe, "
            "molecule, or misreading - that turned loyalty into treason."
        ),
    },
    {
        "key": "t1d_prevention",
        "name": "Type 1 Diabetes: Stopping the Attack on Beta Cells",
        "group": "Compounded",
        "ladder_rank": 14,
        "ladder_tier": "compounded",
        "description": (
            "THE PROBLEM: in type 1 diabetes the immune system hunts down "
            "and kills the pancreatic beta cells - the body's only insulin "
            "factories. Without insulin, blood sugar spirals out of control "
            "and the patient dies; with it, via lifelong injections or "
            "pumps, they survive but never rest - dosing insulin is a "
            "daily high-wire act between coma from too little and coma from "
            "too much. It often strikes children. BACKGROUND: the disease "
            "was a swift death sentence until 1921, when Banting and Best "
            "isolated insulin. The autoimmune nature was proven when "
            "islet-cell antibodies were found in patients' blood. Genetics "
            "sets the risk (HLA genes dominate), but identical twins often "
            "disagree on the disease - so environment pulls the trigger, "
            "with enteroviruses and early diet among the suspects. The "
            "attack unfolds in stages: antibodies appear years before "
            "symptoms, while most beta cells still live. In 2022 the first "
            "drug to delay onset - teplizumab, an anti-CD3 antibody - won "
            "approval, proving the attack can be slowed. Stem-cell-derived "
            "beta cell transplants have freed small numbers of patients "
            "from insulin entirely in trials. But nobody has yet STOPPED "
            "the attack permanently or prevented the disease in an "
            "at-risk child."
        ),
        "how_it_works": (
            "WHY IT MATTERS: type 1 diabetes means a lifetime of glucose "
            "management with no days off, and even well-managed patients "
            "face shortened lives and complication risks. Prevention in "
            "at-risk children would erase all of it; a true halt of the "
            "attack would free millions from the wire. CURRENT STATE: "
            "screening programs can now find at-risk children by antibodies "
            "years before symptoms, opening a prevention window that never "
            "existed before. Teplizumab delays onset by roughly two to "
            "three years - a proof of principle, not a cure. "
            "Stem-cell beta cells plus immune protection (encapsulation "
            "devices or tolerance induction) aim at functional cure. The "
            "honest status: the attack is now visible years early and "
            "delayable, but stopping it cold - permanent, drug-free "
            "tolerance - remains unsolved."
        ),
        "key_points": [
            "Type 1 diabetes is autoimmune destruction of the pancreatic beta cells - the body's only insulin source.",
            "Islet antibodies appear years before symptoms, creating a prevention window screening can now find.",
            "Teplizumab (2022) proved the attack can be delayed - by years, not permanently.",
            "Stem-cell-derived beta cells have freed trial patients from insulin, but immune protection remains the hurdle.",
            "Genetics loads the gun (HLA genes); environment pulls the trigger - identical twins often disagree.",
        ],
        "requirements": [
            "Prevention must work in antibody-positive children before symptoms, with safety suitable for healthy kids.",
            "A halt must be permanent and drug-free: lifelong immunosuppression trades one burden for another.",
            "Beta-cell replacement must survive without immune destruction - encapsulation or true tolerance.",
            "Therapies must preserve any remaining beta cells; even partial function transforms glucose control.",
            "Any cure claim needs years of insulin-independence with normal glucose regulation, not months.",
        ],
        "standards": [
            "Prevention trials enroll by validated antibody staging with pre-registered progression endpoints.",
            "Beta-cell function is measured by C-peptide, not insulin dose alone.",
            "Cure claims require documented insulin independence with continuous glucose monitoring data.",
        ],
        "citations": [CIT_NEJM, CIT_NATURE, CIT_JANEWAY],
        "sig_lens": (
            "The Signature read: the body's own factories burned by its own "
            "army - and the smoke is visible years before the fire. Public "
            "science now spots the smoke (antibodies) and slows the flames; "
            "the Signature lens asks what lit the match in the nursery of "
            "the immune system, and how to un-teach the arson."
        ),
    },
    {
        "key": "microbiome_map",
        "name": "The Gut Microbiome Disease Map",
        "group": "Compounded",
        "ladder_rank": 15,
        "ladder_tier": "compounded",
        "description": (
            "THE PROBLEM: the human gut carries some 38 trillion microbes - "
            "roughly as many as the body's own cells - and this inner "
            "ecosystem is linked to everything from digestion to immunity to "
            "mood. Yet medicine cannot say for most diseases WHICH microbes "
            "cause harm, which protect, and which are innocent bystanders. "
            "The associations are everywhere: altered microbiomes in "
            "obesity, inflammatory bowel disease, depression, autism, "
            "Parkinson disease, and more. But association is not causation, "
            "and the field is drowning in correlations. BACKGROUND: the "
            "Human Microbiome Project (2007-2016) catalogued the healthy "
            "microbiome and revealed its staggering person-to-person "
            "variation - there is no single 'normal.' Fecal microbiota "
            "transplant proved the microbiome can be medicine: it cures "
            "recurrent Clostridioides difficile infection with remarkable "
            "success. But for every other condition, transplants and "
            "probiotics have produced mixed, modest results. The core "
            "difficulty is ecological: the gut is a rainforest, and "
            "removing or adding one species ripples through hundreds. "
            "Strain-level differences matter - one E. coli strain is "
            "harmless, its cousin is deadly - but most studies still measure "
            "at the blurry genus level."
        ),
        "how_it_works": (
            "WHY IT MATTERS: a complete causal map would turn the "
            "microbiome into a pharmacy - precise microbial therapies for "
            "bowel disease, metabolic disease, even brain disorders, plus "
            "diagnostics that read disease risk from a stool sample. "
            "CURRENT STATE: the field is moving from census (who is there) "
            "to function (what they are doing) - measuring microbial "
            "metabolites like short-chain fatty acids and bile acid "
            "derivatives, which are the actual chemical messages microbes "
            "send to the body. Gnotobiotic mice (born germ-free, then given "
            "defined microbes) let researchers test causation one species "
            "at a time. The honest status: one proven microbiome cure "
            "exists (fecal transplant for C. difficile), a mountain of "
            "associations, and no complete causal map for any complex "
            "disease. The rainforest is mapped by satellite; nobody has "
            "walked most of its trails."
        ),
        "key_points": [
            "The gut holds ~38 trillion microbes - comparable to the body's own cell count - with huge person-to-person variation.",
            "Microbiome associations span obesity, bowel disease, depression, and Parkinson disease, but causation is rarely proven.",
            "Fecal transplant cures recurrent C. difficile - the one proven microbiome therapy, and the field's existence proof.",
            "Strain-level differences decide friend from foe, but most studies still measure at the blurry genus level.",
            "The field is shifting from census (who is there) to function (microbial metabolites as chemical messages).",
        ],
        "requirements": [
            "Causation needs interventional proof: defined microbial changes producing defined disease changes in humans.",
            "Measurements must reach strain level with functional readouts (metabolites), not genus-level headcounts.",
            "Therapies must show durability: a remodeled ecosystem that persists, not a probiotic that passes through.",
            "Safety must account for ecology: reshaping a rainforest can have cascading unintended effects.",
            "Diagnostics must be validated prospectively: predicting disease from microbiome before it appears.",
        ],
        "standards": [
            "Causal claims require gnotobiotic or defined-consortium experiments, not correlation alone.",
            "Fecal transplant protocols need donor screening standards equivalent to blood donation.",
            "Probiotic efficacy claims require strain identification and randomized trial evidence per indication.",
        ],
        "citations": [CIT_NATURE, CIT_NEJM, CIT_LANCET],
        "sig_lens": (
            "The Signature read: the gut is a rainforest with 38 trillion "
            "citizens and no census that names the criminals. Public "
            "science counts the trees from orbit; the Signature lens reads "
            "the mail - the chemical letters microbes send the body - "
            "because the message, not the messenger's name, is what moves "
            "the physiology."
        ),
    },
    {
        "key": "depression_biology",
        "name": "Depression Biology Beyond Serotonin",
        "group": "Compounded",
        "ladder_rank": 16,
        "ladder_tier": "compounded",
        "description": (
            "THE PROBLEM: depression disables more people than almost any "
            "other condition, and its biology is still largely a black box. "
            "The serotonin story - depression as a chemical imbalance fixed "
            "by raising serotonin - was always a simplification, and a "
            "2022 umbrella review found no consistent evidence that "
            "depression is caused by low serotonin. Yet SSRIs help many "
            "patients, somehow. A third of patients get little relief from "
            "any standard drug. BACKGROUND: the monoamine hypothesis ruled "
            "from the 1960s, born from the accident that tuberculosis drugs "
            "lifted mood. Then came stranger clues: ketamine, an "
            "anesthetic, lifts severe depression within hours - far too "
            "fast for serotonin theories - by acting on glutamate and "
            "apparently regrowing synaptic connections. Inflammation "
            "entered the picture: depressed patients often show elevated "
            "inflammatory markers, and some anti-inflammatory treatments "
            "ease mood. Chronic stress shrinks the hippocampus; depression "
            "runs in families but no single gene explains it. The emerging "
            "view is that depression is not one disease but several - a "
            "final common pathway of different broken mechanisms - which "
            "would explain why no single drug works for everyone and why "
            "the biology has resisted a unified theory for seventy years."
        ),
        "how_it_works": (
            "WHY IT MATTERS: depression is a leading cause of disability "
            "and suicide worldwide; treatment-resistant patients cycle "
            "through drugs for years. A true biology would allow matching "
            "each patient to the treatment for their mechanism - the "
            "psychiatry equivalent of cancer's move from one chemotherapy "
            "to targeted therapy. CURRENT STATE: ketamine and its cousins "
            "proved rapid-acting, glutamate-based antidepressants are real, "
            "shifting the field toward synaptic plasticity - the brain's "
            "ability to regrow connections - as a core mechanism. "
            "Researchers now hunt depression subtypes by brain imaging, "
            "inflammation profiles, and genetics. The honest status: the "
            "serotonin era is over as an explanation, the plasticity era "
            "has begun as a hypothesis, and no complete, predictive biology "
            "of depression exists yet."
        ),
        "key_points": [
            "A 2022 umbrella review found no consistent evidence that depression is caused by low serotonin - yet SSRIs help many, somehow.",
            "Ketamine lifts severe depression within hours via glutamate pathways, far too fast for serotonin theories.",
            "Treatment-resistant depression affects roughly a third of patients on standard drugs.",
            "Inflammation, hippocampal shrinkage, and synaptic loss are all implicated - possibly different diseases under one name.",
            "The emerging view: depression is a final common pathway of several broken mechanisms, not one chemical imbalance.",
        ],
        "requirements": [
            "A biology must explain the SSRI paradox: drugs built on a disproven theory that still help millions.",
            "It must define subtypes with biomarkers - which patient has the inflammatory form, the plasticity form, and so on.",
            "It must explain ketamine's speed: what regrows in hours that SSRIs take weeks to touch.",
            "Treatments derived from it must beat the one-third resistance rate, not just match existing drugs.",
            "It must connect mind and body: why depression predicts heart disease and diabetes, not just sadness.",
        ],
        "standards": [
            "Antidepressant trials require validated rating scales with pre-registered primary endpoints and adequate blinding.",
            "Biomarker subtype claims need prospective validation: predicting treatment response before treatment.",
            "Rapid-acting claims must demonstrate durability beyond the acute infusion window.",
        ],
        "citations": [CIT_KANDEL, CIT_NEJM, CIT_NATURE],
        "sig_lens": (
            "The Signature read: the depressed brain is a garden where the "
            "paths have overgrown - connections lost, not chemicals spilled. "
            "Public science spent decades topping up the fountain; the "
            "Signature lens studies the gardeners - the plasticity machinery "
            "that grows and prunes the paths, and why it stopped working."
        ),
    },
    {
        "key": "schizophrenia",
        "name": "Schizophrenia: Cause and Curative Treatment",
        "group": "Compounded",
        "ladder_rank": 17,
        "ladder_tier": "compounded",
        "description": (
            "THE PROBLEM: schizophrenia affects about one in a hundred "
            "people, typically striking in late adolescence or early "
            "adulthood, and medicine still does not know what causes it. "
            "Hallucinations, delusions, and disorganized thought are the "
            "visible symptoms; beneath them lie cognitive losses and social "
            "withdrawal that drugs barely touch. BACKGROUND: the dopamine "
            "hypothesis - too much dopamine signaling - was born from two "
            "accidents: antipsychotic drugs block dopamine receptors, and "
            "amphetamines (which flood dopamine) cause psychosis. Every "
            "antipsychotic in seventy years works on dopamine, yet none "
            "cures, many cause severe side effects (movement disorders, "
            "massive weight gain, diabetes), and the negative and cognitive "
            "symptoms barely respond. Genetics implicates over a hundred "
            "genes of small effect; prenatal infection and cannabis use in "
            "adolescence raise risk; brain imaging shows subtle wiring "
            "differences. The synaptic pruning hypothesis proposes the "
            "adolescent brain prunes too aggressively, cutting connections "
            "it should keep - supported by the discovery that complement "
            "protein C4, an immune tag for pruning, is overexpressed in "
            "schizophrenia. But the full causal chain from genes to pruning "
            "to psychosis has never been closed."
        ),
        "how_it_works": (
            "WHY IT MATTERS: schizophrenia shortens lives by 15 to 20 years "
            "on average, devastates families, and fills a tragic share of "
            "the homeless population. Current drugs manage psychosis while "
            "often damaging the body; a true cause would open prevention in "
            "high-risk youth and treatments that restore cognition instead "
            "of sedating symptoms. CURRENT STATE: the field is finally "
            "moving past dopamine-only thinking. Glutamate-based drugs, "
            "anti-inflammatory approaches, and the new muscarinic drug "
            "class (which treats psychosis without direct dopamine blockade) "
            "are expanding the pharmacology. The C4 pruning discovery gave "
            "the first mechanistic bridge from gene to brain change. The "
            "honest status: the dopamine drugs prove dopamine is involved, "
            "not that it is the cause; the cause remains open, and nothing "
            "in the pharmacy today cures."
        ),
        "key_points": [
            "About one in a hundred people develop schizophrenia, usually in late adolescence or early adulthood.",
            "Every antipsychotic in 70 years targets dopamine - yet none cures, and cognitive symptoms barely respond.",
            "Over 100 genes of small effect are implicated; no single gene explains the disease.",
            "The C4 complement discovery links genetics to excessive adolescent synaptic pruning - the first gene-to-brain bridge.",
            "Prenatal infection and adolescent cannabis use raise risk, implicating immune and developmental windows.",
        ],
        "requirements": [
            "A cause must explain timing: why a developmental process erupts specifically in late adolescence.",
            "It must explain the full symptom set: psychosis plus the cognitive and negative symptoms dopamine drugs miss.",
            "It must connect the 100-plus risk genes into a coherent pathway, not a list.",
            "A curative treatment must restore function and cognition, not merely suppress hallucinations.",
            "Prevention in high-risk youth must be proven safe enough for teenagers who might never develop the illness.",
        ],
        "standards": [
            "Antipsychotic trials need validated symptom scales plus functional and cognitive endpoints.",
            "Pruning-hypothesis claims require longitudinal imaging showing excessive loss before onset.",
            "Genetic risk claims need genome-wide significance with replication across ancestries.",
        ],
        "citations": [CIT_KANDEL, CIT_NEJM, CIT_NATURE],
        "sig_lens": (
            "The Signature read: the schizophrenic brain is a city whose "
            "planners demolished too many bridges in adolescence - the "
            "districts still stand, but the roads between them are gone. "
            "Public science polices the traffic (dopamine); the Signature "
            "lens investigates the demolition orders - the pruning signal "
            "that cut too deep, and whether the bridges can be rebuilt."
        ),
    },
])

ENTRIES.extend([
    {
        "key": "hiv_cure",
        "name": "An HIV Cure: Emptying the Latent Reservoir",
        "group": "Compounded",
        "ladder_rank": 18,
        "ladder_tier": "compounded",
        "description": (
            "THE PROBLEM: antiretroviral therapy turned HIV from a death "
            "sentence into a manageable condition - but it is not a cure. "
            "Stop the drugs and the virus roars back within weeks, because "
            "HIV hides its genetic blueprints inside long-lived immune "
            "cells, silent and invisible. This latent reservoir is the wall "
            "between treatment and cure. BACKGROUND: HIV integrates its DNA "
            "into the host cell's genome. In most infected cells the virus "
            "replicates and the cell dies; but in a small fraction of "
            "resting memory T cells, the integrated virus goes dormant - no "
            "viral proteins made, nothing for drugs or the immune system to "
            "see. These cells live for years, even decades. Antiretrovirals "
            "block every step of active replication but cannot touch silent "
            "DNA. The reservoir is seeded within days of infection, which is "
            "why even the earliest treatment cannot fully prevent it. A "
            "handful of extraordinary cases hint at cures: the Berlin and "
            "London patients, cured via stem-cell transplants from donors "
            "with a rare HIV-resistant mutation - a brutal procedure no one "
            "would choose electively. The leading strategy, 'shock and "
            "kill,' tries to wake the dormant virus (shock) so the immune "
            "system or drugs can destroy the cell (kill) - but waking it "
            "reliably without waking it dangerously has proven enormously "
            "hard."
        ),
        "how_it_works": (
            "WHY IT MATTERS: 39 million people live with HIV; lifelong daily "
            "drugs are a triumph but also a burden - cost, side effects, "
            "stigma, and the ever-present risk of resistance. A true cure "
            "would end the epidemic's long tail. CURRENT STATE: shock-and-"
            "kill trials have woken some virus but not shrunk the reservoir "
            "meaningfully. Newer strategies include 'block and lock' "
            "(forcing the virus into permanent deep sleep), engineered "
            "immune cells (CAR-T against HIV), and broadly neutralizing "
            "antibodies. The honest status: treatment is one of medicine's "
            "greatest victories, and cure remains one of its hardest "
            "unsolved problems - the reservoir is small, silent, scattered "
            "through the body, and seeded within days."
        ),
        "key_points": [
            "Antiretrovirals suppress HIV completely but cannot touch the silent integrated DNA in resting memory cells.",
            "The latent reservoir is seeded within days of infection and persists for decades.",
            "Stopping drugs leads to viral rebound within weeks - proof the reservoir survives treatment.",
            "The Berlin and London patients were cured via dangerous stem-cell transplants - proof of principle, not a therapy.",
            "'Shock and kill' has woken virus without meaningfully shrinking the reservoir so far.",
        ],
        "requirements": [
            "A cure must eliminate or permanently silence every replication-competent provirus, in every tissue including the brain.",
            "It must be safer than lifelong antiretrovirals - the bar is high because current treatment works well.",
            "Cure claims need years of drug-free remission with ultrasensitive viral monitoring, not months.",
            "It must work for the global majority, not just patients near elite research hospitals.",
            "Any latency-reversing agent must not trigger dangerous immune activation or viral spread.",
        ],
        "standards": [
            "Cure trials require analytical treatment interruption with pre-registered rebound-monitoring protocols.",
            "Reservoir measurements need validated assays distinguishing intact from defective proviruses.",
            "Remission claims require multi-year follow-up with ultrasensitive viral load testing.",
        ],
        "citations": [CIT_NEJM, CIT_NATURE, CIT_WHO],
        "sig_lens": (
            "The Signature read: HIV is an enemy that buried its battle "
            "plans inside our own soldiers and then went to sleep - "
            "invisible, patient, everywhere. Public science guards the "
            "gates against the marching army; the Signature lens hunts the "
            "sleepers: the signal that keeps them dormant, and whether "
            "dormancy can be made permanent - or broken on our terms."
        ),
    },
    {
        "key": "drug_resistant_tb",
        "name": "Drug-Resistant Tuberculosis",
        "group": "Compounded",
        "ladder_rank": 19,
        "ladder_tier": "compounded",
        "description": (
            "THE PROBLEM: tuberculosis has killed more humans than any "
            "other infection in history, and it is learning to survive our "
            "drugs. Standard TB is curable with six months of antibiotics; "
            "multidrug-resistant TB (MDR-TB) needs longer, harsher regimens; "
            "extensively drug-resistant TB (XDR-TB) defeats nearly "
            "everything. About 10 million people fall ill yearly, and "
            "drug-resistant strains now circulate on every continent. "
            "BACKGROUND: Mycobacterium tuberculosis is a slow, armored "
            "fortress of a bacterium - waxy cell wall, months-long "
            "generation of disease, the ability to sleep dormant in lung "
            "granulomas for decades (latent TB infects an estimated "
            "quarter of humanity). Treatment takes months because the "
            "bacteria hide in these granuloma fortresses and in a dormant "
            "state where most antibiotics, which target active growth, "
            "barely work. Incomplete treatment breeds resistance, and "
            "resistance spreads. The BCG vaccine, a century old, protects "
            "children from severe TB but barely dents adult lung disease. "
            "New drugs (bedaquiline, pretomanid) finally shortened MDR-TB "
            "treatment, but resistance to the new drugs is already "
            "appearing - the treadmill continues."
        ),
        "how_it_works": (
            "WHY IT MATTERS: TB remains the top infectious killer in many "
            "years, and drug-resistant TB threatens to return medicine to "
            "the pre-antibiotic era for the world's most common serious "
            "bacterial infection. A sterilizing cure - one that kills "
            "dormant bacteria in weeks, not months - would collapse both "
            "the disease and the resistance problem, since resistance "
            "breeds in long, incomplete treatments. CURRENT STATE: the "
            "newer all-oral regimens cut MDR-TB treatment to six months "
            "with good success rates - real progress. Research now targets "
            "the dormant state directly: drugs that kill non-replicating "
            "bacteria, host-directed therapies that help the granuloma "
            "finish the job, and vaccines that prevent adult lung disease. "
            "The honest status: treatment keeps improving at the margins "
            "while the core problems - dormancy, the granuloma fortress, "
            "and no effective adult vaccine - remain unsolved."
        ),
        "key_points": [
            "TB kills over a million people yearly; drug-resistant strains circulate on every continent.",
            "Latent TB infects an estimated quarter of humanity - a vast reservoir that can reactivate decades later.",
            "The waxy cell wall and dormant state shield the bacterium from drugs that target active growth.",
            "BCG, a century old, protects children from severe TB but barely prevents adult lung disease.",
            "Resistance to even the newest drugs (bedaquiline) is already appearing - the treadmill continues.",
        ],
        "requirements": [
            "A sterilizing cure must kill dormant, non-replicating bacteria - the population current drugs miss.",
            "Treatment must shrink to weeks, because months-long regimens breed the incomplete courses that create resistance.",
            "An adult vaccine must prevent lung disease and transmission, not just severe childhood TB.",
            "New drugs need resistance-proof deployment: combinations and stewardship from day one.",
            "Latent TB needs a safe, short preventive therapy suitable for a quarter of humanity.",
        ],
        "standards": [
            "TB drug trials require culture-confirmed cure with at least 12 months of post-treatment follow-up for relapse.",
            "Resistance claims need whole-genome sequencing with validated mutation catalogs.",
            "Vaccine efficacy must be measured against confirmed pulmonary TB in high-burden settings.",
        ],
        "citations": [CIT_WHO, CIT_NEJM, CIT_LANCET],
        "sig_lens": (
            "The Signature read: tuberculosis is a siege engineer's "
            "nightmare - a fortress with walls of wax, soldiers that play "
            "dead for decades, and supply lines of resistance genes. Public "
            "science storms the walls with longer ladders; the Signature "
            "lens studies the sleepers inside: what keeps the dormant "
            "bacteria dormant, and whether the fortress can be starved "
            "rather than stormed."
        ),
    },
    {
        "key": "universal_flu_vaccine",
        "name": "A Universal Influenza Vaccine",
        "group": "Compounded",
        "ladder_rank": 20,
        "ladder_tier": "compounded",
        "description": (
            "THE PROBLEM: this record's sibling (rank 2) explains why flu "
            "vaccines expire yearly; this record is the quest to end that "
            "cycle. A universal influenza vaccine would protect against all "
            "strains - seasonal drifted variants and shifted pandemic "
            "strains alike - for years from a single course. It is "
            "vaccinology's most wanted prize and has been 'five to ten "
            "years away' for decades. BACKGROUND: the scientific case is "
            "real. Some people naturally make broadly neutralizing "
            "antibodies against the conserved HA stem; these antibodies "
            "protect animals against lethal flu challenge across strains. "
            "The 2009 pandemic showed the population's vulnerability to a "
            "shifted strain and the cost of the months-long scramble to "
            "make a matched vaccine. Multiple candidates - stem-only "
            "immunogens, chimeric HA constructs that refocus immunity on "
            "the stem, mRNA cocktails, nanoparticle displays - have entered "
            "human trials. But breadth in a test tube is not protection in "
            "a population: no candidate has yet shown that stem-directed "
            "immunity actually prevents human influenza across seasons, and "
            "the immune system's stubborn preference for the variable head "
            "(immunodominance) keeps pulling responses back to the "
            "short-lived target."
        ),
        "how_it_works": (
            "WHY IT MATTERS: a universal vaccine ends the annual "
            "reformulation gamble, protects against surprise pandemics "
            "before they start, and would be the template for universal "
            "vaccines against coronaviruses and other variable viruses. It "
            "is the single highest-leverage project in vaccinology. "
            "CURRENT STATE: early-phase human trials are testing whether "
            "stem-focused immunogens can reliably elicit broadly "
            "neutralizing antibodies and - the harder question - whether "
            "those antibodies translate into real-world protection. "
            "Sequential immunization strategies try to train the immune "
            "system away from the variable head and onto the stem. The "
            "honest status: the immunology is the most promising it has "
            "ever been, and the clinical proof of broad, durable human "
            "protection does not yet exist."
        ),
        "key_points": [
            "A universal flu vaccine would protect against drifted seasonal strains and shifted pandemic strains for years.",
            "Naturally occurring stem-directed broadly neutralizing antibodies prove the human immune system CAN make them.",
            "Immunodominance is the obstacle: the immune system stubbornly prefers the variable HA head over the conserved stem.",
            "Multiple platforms (chimeric HA, stem nanoparticles, mRNA cocktails) are in human trials.",
            "Test-tube breadth has not yet translated into proven multi-season human protection.",
        ],
        "requirements": [
            "Candidates must show protection against mismatched and shifted strains in humans, not just antibody breadth in blood draws.",
            "Durability must span multiple seasons - the entire point is escaping the yearly cycle.",
            "It must protect the elderly, whose immune systems respond weakly and who die most from flu.",
            "Manufacturing must be rapid and scalable enough to matter in a pandemic's first months.",
            "Immune refocusing strategies must prove they overcome immunodominance durably, not transiently.",
        ],
        "standards": [
            "Universal claims require pre-registered breadth endpoints across defined strain panels.",
            "Human challenge trials, where used, need ethical review proportionate to the pathogen's risk.",
            "Effectiveness must be measured over at least two full seasons against circulating strains.",
        ],
        "citations": [CIT_WHO, CIT_NEJM, CIT_NATURE],
        "sig_lens": (
            "The Signature read: the immune system is a student that keeps "
            "memorizing the wrong chapter - the flashy variable head "
            "instead of the quiet conserved stem. Public science writes "
            "better textbooks; the Signature lens studies the student's "
            "habit: immunodominance itself, and how to retrain attention "
            "toward what never changes."
        ),
    },
    {
        "key": "malaria_durability",
        "name": "Malaria Vaccine Durability",
        "group": "Compounded",
        "ladder_rank": 21,
        "ladder_tier": "compounded",
        "description": (
            "THE PROBLEM: malaria still kills over half a million people a "
            "year, mostly African children under five - and the vaccines, "
            "long in coming, fade. RTS,S (Mosquirix), the first approved "
            "malaria vaccine, showed roughly 30 to 40 percent efficacy that "
            "waned within a few years; its successor R21/Matrix-M does "
            "better but still requires boosters and still does not match "
            "the near-total protection of the best viral vaccines. "
            "BACKGROUND: malaria is caused by Plasmodium parasites - "
            "single-celled organisms vastly more complex than viruses, "
            "with a multi-stage life cycle (mosquito to liver to blood) "
            "and thousands of genes. The parasite has co-evolved with "
            "humans for millennia, learning immune evasion tricks that "
            "make natural immunity itself slow to develop: children in "
            "endemic areas need years of repeated infection to build "
            "partial protection. Vaccine developers targeted the "
            "sporozoite stage (the form injected by the mosquito) to stop "
            "infection before it starts, but the parasite's surface "
            "proteins vary, and immunity wanes. Whole-parasite vaccines "
            "(radiation-weakened sporozoites) give stronger protection in "
            "trials but are a logistical nightmare to manufacture and "
            "deliver. The durability problem is the wall: even when a "
            "malaria vaccine works, it does not last."
        ),
        "how_it_works": (
            "WHY IT MATTERS: durable malaria protection would save hundreds "
            "of thousands of children's lives yearly and break transmission "
            "in endemic regions - one of the highest-value goals in global "
            "health. CURRENT STATE: R21 is being rolled out across Africa "
            "with real-world effectiveness studies underway; researchers "
            "are testing whether different dosing schedules, adjuvants, or "
            "multi-stage combinations (sporozoite plus blood-stage targets) "
            "extend protection. Monoclonal antibodies against the parasite "
            "offer an alternative: months of protection per injection, now "
            "in trials. The honest status: the world finally has malaria "
            "vaccines, they are imperfect and fading, and the durable "
            "solution - whether better vaccine, antibody, or combination - "
            "is still being built."
        ),
        "key_points": [
            "Malaria kills over half a million yearly, mostly children under five in Africa.",
            "RTS,S showed 30-40 percent efficacy that waned within years; R21 improves on it but still needs boosters.",
            "Plasmodium is a complex multi-stage parasite with thousands of genes - vastly harder than a virus to vaccinate against.",
            "Natural immunity takes years of repeated infection to develop - the parasite is a master of immune evasion.",
            "Monoclonal antibodies now offer months of protection per injection as a complementary strategy.",
        ],
        "requirements": [
            "Durability must reach years, not months, to be practical in the regions that need it most.",
            "Efficacy must hold against diverse field strains, not just laboratory parasites.",
            "Delivery must survive real conditions: heat-stable, affordable, fitting existing childhood vaccine schedules.",
            "Multi-stage approaches must prove the stages add protection rather than just adding complexity.",
            "Any antibody strategy needs cost reduction to reach endemic-country scale.",
        ],
        "standards": [
            "Malaria vaccine efficacy is measured against clinical episodes with parasite confirmation in endemic settings.",
            "Durability claims require multi-year follow-up through multiple transmission seasons.",
            "Strain-transcendence must be tested against local field isolates, not reference strains alone.",
        ],
        "citations": [CIT_WHO, CIT_LANCET, CIT_NEJM],
        "sig_lens": (
            "The Signature read: Plasmodium is a shape-shifter with a "
            "thousand faces and a million years of practice fooling immune "
            "systems. Public science aims at one face at a time; the "
            "Signature lens asks what all faces share - the machinery of "
            "the shape-shift itself - and whether immunity can be taught to "
            "recognize the trick rather than the mask."
        ),
    },
    {
        "key": "pancreatic_early",
        "name": "Pancreatic Cancer Early Detection",
        "group": "Compounded",
        "ladder_rank": 22,
        "ladder_tier": "compounded",
        "description": (
            "THE PROBLEM: pancreatic cancer is one of the deadliest cancers "
            "because it is found too late. The pancreas sits deep in the "
            "abdomen, early tumors cause no symptoms, and by the time "
            "jaundice, pain, or weight loss appear, the cancer has usually "
            "spread beyond surgical cure. Five-year survival hovers around "
            "12 percent - not because the cancer is uniquely untreatable, "
            "but because it is uniquely invisible. BACKGROUND: for breast, "
            "colon, and cervical cancer, screening transformed survival by "
            "catching disease early. Pancreatic cancer has no screening "
            "test: it is too rare in the general population for broad "
            "imaging (the false positives would overwhelm the true ones), "
            "and no blood marker is accurate enough. CA19-9, the standard "
            "marker, misses many cancers and rises in benign conditions. "
            "The biology conspires too: pancreatic tumors grow in a dense "
            "fibrous stroma that walls out drugs and immune cells alike, "
            "and the cancer spreads early - microscopic metastases may exist "
            "when the primary is still tiny. High-risk screening (for "
            "familial cases and certain gene carriers) with MRI and "
            "endoscopic ultrasound catches some early cancers, proving "
            "early detection saves lives here - but 90 percent of cases "
            "are sporadic, with no warning to screen for."
        ),
        "how_it_works": (
            "WHY IT MATTERS: caught early and surgically removed, pancreatic "
            "cancer survival jumps dramatically; caught late, it is nearly "
            "uniformly fatal. A reliable early-detection test would convert "
            "one of the worst cancer diagnoses into a treatable one. "
            "CURRENT STATE: the frontier is liquid biopsy - hunting tumor "
            "DNA, proteins, or exosomes in a blood draw. Multi-marker panels "
            "and methylation-based tests are in validation studies; "
            "artificial-intelligence analysis of routine medical scans and "
            "records tries to flag high-risk patients before symptoms. The "
            "honest status: no test is yet accurate enough for population "
            "screening, and the field is racing between the biology "
            "(finding signals the tiny tumor actually sheds) and the math "
            "(keeping false positives near zero in a rare disease)."
        ),
        "key_points": [
            "Five-year survival is ~12 percent, driven by late detection rather than unique untreatability.",
            "The pancreas is deep, early tumors are silent, and spread can precede symptoms.",
            "CA19-9 misses many cancers and rises in benign disease - inadequate for screening.",
            "High-risk screening proves early detection saves lives, but 90 percent of cases are sporadic.",
            "Dense fibrous stroma walls out drugs and immune cells, compounding the detection problem.",
        ],
        "requirements": [
            "A screening test needs near-perfect specificity: in a rare disease, even 99 percent specificity floods the system with false alarms.",
            "It must detect stage I disease, when surgery still cures - later detection adds little.",
            "The signal must come from the tumor itself (DNA, methylation, proteins), not from generic inflammation.",
            "It must be a blood test or similarly scalable - population imaging is impractical.",
            "Validation needs prospective trials showing mortality reduction, not just earlier diagnosis.",
        ],
        "standards": [
            "Early-detection claims require prospective validation in the intended-use population with pre-registered cutoffs.",
            "Lead-time and overdiagnosis biases must be accounted for before survival claims.",
            "Screening benefit must be shown as mortality reduction in randomized trials, not stage shift alone.",
        ],
        "citations": [CIT_NEJM, CIT_NATURE, CIT_LANCET],
        "sig_lens": (
            "The Signature read: pancreatic cancer is a thief that works in "
            "the dark - no noise until the house is empty. Public science "
            "waits for a scream; the Signature lens listens for the "
            "floorboards: the faintest molecular creaks - a methylated "
            "fragment, a stray protein - that betray the intruder while "
            "the house can still be saved."
        ),
    },
    {
        "key": "glioblastoma_bbb",
        "name": "Glioblastoma and the Blood-Brain Barrier",
        "group": "Compounded",
        "ladder_rank": 23,
        "ladder_tier": "compounded",
        "description": (
            "THE PROBLEM: glioblastoma is the most aggressive brain cancer, "
            "and the blood-brain barrier - the brain's security wall - "
            "protects the tumor from our drugs as faithfully as it protects "
            "the brain from toxins. Median survival remains around 15 "
            "months despite surgery, radiation, and chemotherapy. The "
            "barrier that keeps poisons out of the brain keeps medicines "
            "out too: over 95 percent of drugs cannot cross it. BACKGROUND: "
            "the blood-brain barrier is a wall of tightly sealed vessel "
            "cells, efflux pumps, and enzymatic guards - essential, since "
            "the brain cannot tolerate the chemical chaos of the blood. "
            "Glioblastoma exploits this: tumor cells infiltrate deep into "
            "healthy brain, making complete surgical removal impossible "
            "(cutting wide would destroy the mind to save the body), and "
            "the intact barrier around the infiltrating edges shelters "
            "residual cells from chemotherapy. Temozolomide, one of the few "
            "drugs that crosses modestly, added only months. "
            "Immunotherapy, triumphant in melanoma and lung cancer, has "
            "largely failed in glioblastoma - the brain's immune "
            "specialization plus the tumor's suppression prove a brutal "
            "combination. Focused ultrasound can now open the barrier "
            "temporarily and locally, a crack in a wall that has stood for "
            "all of drug development."
        ),
        "how_it_works": (
            "WHY IT MATTERS: glioblastoma strikes adults in their prime and "
            "kills with terrifying speed; solving drug delivery to the "
            "brain would unlock treatments not just for this cancer but for "
            "Alzheimer, Parkinson, and every brain disease walled off from "
            "pharmacology. CURRENT STATE: focused ultrasound with "
            "microbubbles opens the barrier reversibly in trials, letting "
            "chemotherapy and antibodies reach tumors; early results show "
            "feasibility and hints of benefit. Convection-enhanced delivery "
            "(pumping drugs directly into brain tissue), tumor-treating "
            "electric fields, and CAR-T cells engineered for brain tumors "
            "are all in trials. The honest status: the wall has its first "
            "cracks, but no approach has yet transformed survival. "
            "Glioblastoma remains the benchmark for how hard the brain is "
            "to treat."
        ),
        "key_points": [
            "Median survival is ~15 months; over 95 percent of drugs cannot cross the blood-brain barrier.",
            "Infiltrating tumor cells make complete surgery impossible without destroying healthy brain.",
            "The barrier shelters residual cancer cells from chemotherapy around the tumor's edges.",
            "Immunotherapy's triumphs elsewhere have largely failed in glioblastoma.",
            "Focused ultrasound can now open the barrier temporarily and locally - the first real crack in the wall.",
        ],
        "requirements": [
            "Delivery must reach the infiltrating edge, not just the tumor core surgeons already remove.",
            "Barrier opening must be reversible and safe - the barrier exists to protect the brain.",
            "Therapies must overcome the tumor's immune suppression, not just arrive at the address.",
            "Success means extended survival with preserved cognition, not tumor shrinkage on scans alone.",
            "Any approach must handle recurrence: glioblastoma nearly always returns.",
        ],
        "standards": [
            "Glioblastoma trials use overall survival as the primary endpoint; progression imaging alone is insufficient.",
            "Barrier-opening claims need imaging confirmation of delivery plus pharmacokinetic proof the drug arrived.",
            "Cognitive function must be tracked as a co-primary outcome in brain tumor trials.",
        ],
        "citations": [CIT_NEJM, CIT_NATURE, CIT_LANCET],
        "sig_lens": (
            "The Signature read: the brain is a citadel, and glioblastoma "
            "is a traitor inside the walls - the gates that keep armies out "
            "keep the executioner out too. Public science besieges the "
            "walls; the Signature lens studies the gatehouse: the barrier's "
            "own passwords, and how to speak them for exactly one delivery, "
            "then seal the gate again."
        ),
    },
])

ENTRIES.extend([
    {
        "key": "alzheimer",
        "name": "Alzheimer Disease: Mechanism and Cure",
        "group": "Advanced",
        "ladder_rank": 24,
        "ladder_tier": "advanced",
        "description": (
            "THE PROBLEM: Alzheimer disease steals memory, identity, and "
            "finally life itself - and after a century of study, its cause "
            "is still disputed and it has no cure. Alois Alzheimer described "
            "the plaques and tangles in 1906; today the disease affects "
            "tens of millions worldwide, with numbers rising as populations "
            "age. BACKGROUND: the amyloid hypothesis dominated for thirty "
            "years: sticky amyloid-beta plaques trigger tau tangles, which "
            "kill neurons. Billions were spent on anti-amyloid drugs, and "
            "nearly all failed - until lecanemab and donanemab finally "
            "showed that clearing amyloid modestly slows decline in early "
            "disease. Modestly is the key word: the benefit is small, the "
            "risks (brain swelling and bleeding) are real, and the drugs "
            "must be given early and indefinitely. Meanwhile the failures "
            "forced a reckoning: plaques correlate poorly with dementia - "
            "some brains are full of plaques with minds intact - while tau "
            "tangles, neuroinflammation (the brain's microglia turning "
            "destructive), vascular damage, and metabolic failure all claim "
            "shares of causation. Genetics implicates cholesterol transport "
            "(APOE4 is the strongest risk gene), immune function, and lipid "
            "metabolism - a far wider story than one sticky protein. The "
            "field now debates whether amyloid is the arsonist, the smoke "
            "alarm, or the ashes."
        ),
        "how_it_works": (
            "WHY IT MATTERS: Alzheimer is the most feared disease of aging "
            "and one of the costliest - in care, in grief, in lost selves. "
            "A true mechanism would redirect the field from clearing "
            "debris to preventing the fire; a cure would restore the "
            "stolen decades. CURRENT STATE: anti-amyloid antibodies proved "
            "amyloid matters (slowing decline ~25-35 percent in early "
            "disease) without proving it is the whole story. Attention is "
            "shifting to tau (which tracks symptoms better), to microglia "
            "(the brain's immune cells, with the TREM2 pathway as a "
            "therapeutic target), to vascular health, and to prevention "
            "trials in high-risk gene carriers. The honest status: the "
            "first disease-modifying drugs exist and are underwhelming; "
            "the mechanism is now understood as multi-factorial, which is "
            "progress of a kind - and an admission that the single-cause "
            "era failed."
        ),
        "key_points": [
            "After a century of study the cause is disputed and there is no cure; tens of millions affected and rising.",
            "Anti-amyloid drugs finally showed modest slowing of early decline - small benefit, real brain-bleed risks.",
            "Plaques correlate poorly with dementia; tau tangles track symptoms better.",
            "APOE4 (cholesterol transport) is the strongest risk gene - implicating lipids, not just amyloid.",
            "Microglial neuroinflammation, vascular damage, and metabolic failure all claim shares of causation.",
        ],
        "requirements": [
            "A mechanism must explain the plaque paradox: full plaques with intact minds, and dementia with modest plaques.",
            "It must integrate amyloid, tau, microglia, vascular, and metabolic evidence into one causal order.",
            "A cure must restore lost function or halt decline durably - not merely clear a biomarker.",
            "Prevention must be proven in at-risk populations (APOE4 carriers) before symptoms begin.",
            "Any therapy's benefit must clearly outweigh brain swelling and bleeding risks.",
        ],
        "standards": [
            "Disease-modification claims require clinical decline endpoints (CDR-SB or equivalent), not biomarker clearance alone.",
            "Amyloid-clearance trials must pre-register ARIA (brain swelling/bleeding) monitoring and stopping rules.",
            "Prevention trials need biomarker-confirmed at-risk enrollment with multi-year follow-up.",
        ],
        "citations": [CIT_ALZ, CIT_NEJM, CIT_NATURE],
        "sig_lens": (
            "The Signature read: Alzheimer is a city where the garbage "
            "collectors went on strike, the power grid failed, and the "
            "fire department started the fires - and science spent thirty "
            "years ticketing the litter. Public research now sees the "
            "whole failing city; the Signature lens asks for the mayor's "
            "first bad order: the upstream failure that turned maintenance "
            "into mayhem."
        ),
    },
    {
        "key": "parkinson_halt",
        "name": "Parkinson Disease: Halting Progression",
        "group": "Advanced",
        "ladder_rank": 25,
        "ladder_tier": "advanced",
        "description": (
            "THE PROBLEM: Parkinson disease slowly kills the brain's "
            "dopamine factories, freezing movement into tremor, rigidity, "
            "and stillness - and every treatment we have only masks the "
            "symptoms while the dying continues underneath. Levodopa, the "
            "gold-standard drug since the 1960s, replaces the missing "
            "dopamine brilliantly at first, then brings its own curse: "
            "dyskinesias (wild involuntary movements) and wearing-off, as "
            "the brain's remaining cells keep dying. BACKGROUND: James "
            "Parkinson described the shaking palsy in 1817. The dopamine "
            "link was proven in the 1960s, and levodopa was a miracle - "
            "patients frozen for years rose and walked. But the miracle "
            "fades because the disease marches on: by diagnosis, most of "
            "the substantia nigra's dopamine neurons are already gone, and "
            "the pathology - misfolded alpha-synuclein protein spreading "
            "cell to cell in Lewy bodies - keeps spreading. Braak's "
            "staging suggests it may start in the gut or nose years before "
            "the first tremor. Genetics (LRRK2, GBA, Parkin genes) "
            "implicates lysosomes - the cell's recycling centers - and "
            "mitochondria, the power plants. Deep brain stimulation helps "
            "symptoms dramatically in some patients but does not slow the "
            "disease. Nothing yet stops the dying."
        ),
        "how_it_works": (
            "WHY IT MATTERS: Parkinson affects millions and its prevalence "
            "is rising faster than aging alone explains (pesticides and "
            "industrial chemicals are suspects). Halting progression would "
            "convert a sentence of slow freezing into a manageable "
            "condition. CURRENT STATE: the field is racing to intervene "
            "earlier - detecting the disease in its prodromal phase (loss "
            "of smell, REM sleep behavior disorder) before most dopamine "
            "cells die. Alpha-synuclein antibodies, LRRK2 inhibitors, GBA "
            "pathway drugs, and GLP-1 agonists (borrowed from diabetes, "
            "showing surprising signals) are in trials. The honest status: "
            "symptom control keeps improving while disease modification "
            "remains unproven - every 'neuroprotective' candidate so far "
            "has failed to slow the dying in humans."
        ),
        "key_points": [
            "Levodopa masks symptoms brilliantly while the underlying cell death continues unchecked.",
            "By diagnosis, most substantia nigra dopamine neurons are already gone.",
            "Misfolded alpha-synuclein spreads cell to cell; Braak staging suggests gut or nose origins years before tremor.",
            "LRRK2, GBA, and Parkin genes implicate lysosomes and mitochondria - recycling and power plants.",
            "Deep brain stimulation helps symptoms dramatically but does not slow the disease.",
        ],
        "requirements": [
            "A halting therapy must show slowed clinical decline over years, not just biomarker changes.",
            "It must work in prodromal patients - by tremor onset, most target cells are already lost.",
            "It must address alpha-synuclein spread, the leading candidate for the progression engine.",
            "Trial design needs validated progression biomarkers to run feasible-length studies.",
            "Any therapy must preserve the levodopa response - patients need today's function while waiting for tomorrow's halt.",
        ],
        "standards": [
            "Disease-modification claims require delayed-start or washout designs separating symptomatic from protective effects.",
            "Alpha-synuclein seed-amplification assays need standardization before serving as trial endpoints.",
            "Prodromal enrollment requires validated risk markers (RBD, hyposmia, DAT imaging) with ethical counseling.",
        ],
        "citations": [CIT_KANDEL, CIT_NEJM, CIT_NATURE],
        "sig_lens": (
            "The Signature read: Parkinson is a city losing its power "
            "plants one by one while the mayor hands out flashlights. "
            "Public science perfected the flashlight (levodopa); the "
            "Signature lens hunts the saboteur - the misfolded protein, "
            "the failing recycler - that keeps blowing the plants, and "
            "asks what armors a power plant against the spreading dark."
        ),
    },
    {
        "key": "als_cure",
        "name": "ALS: Cause and Cure",
        "group": "Advanced",
        "ladder_rank": 26,
        "ladder_tier": "advanced",
        "description": (
            "THE PROBLEM: amyotrophic lateral sclerosis kills the motor "
            "neurons - the nerves that carry the brain's orders to the "
            "muscles - leaving the mind intact inside a body that stops "
            "obeying. Patients lose the ability to walk, speak, swallow, "
            "and finally breathe, usually within two to five years of "
            "diagnosis. The cause is unknown in 90 percent of cases. "
            "BACKGROUND: Lou Gehrig's 1939 farewell made the disease "
            "famous; Stephen Hawking lived with it for half a century, an "
            "inexplicable exception. Genetics cracked a door: SOD1 "
            "mutations (1993), then C9orf72 (2011, the commonest genetic "
            "cause), TDP-43, and FUS implicated protein mishandling - "
            "proteins misfolding, clumping, and jamming the cell's "
            "machinery. But most cases are sporadic, with no mutation to "
            "blame, and the trigger that starts a motor neuron dying in a "
            "previously healthy adult remains unknown. Riluzole and "
            "edaravone extend life by months at best. The antisense drug "
            "tofersen, targeting SOD1, proved gene-silencing can work in "
            "the genetic form - a genuine milestone that covers only a "
            "small slice of patients. For the sporadic majority, the "
            "disease is as mysterious as in Gehrig's day."
        ),
        "how_it_works": (
            "WHY IT MATTERS: ALS is among the cruelest diagnoses in "
            "medicine - rapid, certain, and conscious throughout. A cause "
            "would open prevention and early intervention; a cure would "
            "rescue the condemned. CURRENT STATE: the field converges on "
            "protein homeostasis failure - the motor neuron's quality "
            "control collapsing under misfolded protein load - with "
            "contributors from glial cells (the neuron's neighbors turning "
            "toxic), axonal transport breakdown, and excitotoxicity. "
            "Tofersen's success energized antisense and gene-therapy "
            "programs for other genetic forms. Biomarkers (neurofilament "
            "light chain in blood) now let trials measure neuron death "
            "directly and intervene earlier. The honest status: one small "
            "genetic slice has a disease-modifying drug; the sporadic "
            "majority still faces a disease of unknown cause and no "
            "effective treatment."
        ),
        "key_points": [
            "ALS kills motor neurons while sparing the mind; most patients die within 2-5 years of diagnosis.",
            "The cause is unknown in 90 percent of cases (sporadic ALS).",
            "SOD1, C9orf72, TDP-43, and FUS implicate protein misfolding and jammed cellular machinery.",
            "Tofersen proved gene-silencing works for SOD1 ALS - a milestone covering a small slice of patients.",
            "Neurofilament light chain in blood now lets trials measure neuron death directly.",
        ],
        "requirements": [
            "A cause must explain sporadic ALS - the 90 percent without a causative mutation.",
            "It must explain selectivity: why motor neurons die while neighboring cells survive.",
            "A cure must halt neuron loss and ideally restore function; months of extension is not the goal.",
            "Trials need earlier enrollment - by diagnosis, massive neuron loss has already occurred.",
            "Any genetic therapy must reach the spinal cord's motor neurons safely and durably.",
        ],
        "standards": [
            "ALS trials use validated functional scales (ALSFRS-R) plus survival with pre-registered analysis.",
            "Neurofilament light chain needs assay standardization before serving as a surrogate endpoint.",
            "Gene-therapy claims require durable target engagement in cerebrospinal fluid with long follow-up.",
        ],
        "citations": [CIT_NEJM, CIT_NATURE, CIT_KANDEL],
        "sig_lens": (
            "The Signature read: ALS is a telegraph network whose wires "
            "are cut one by one while the operator still taps the key. "
            "Public science found some of the wire-cutters (mutant "
            "proteins); the Signature lens asks why THESE wires - what "
            "makes the motor neuron, longest and hardest-working of cells, "
            "the chosen victim - and what armors a wire against the cut."
        ),
    },
    {
        "key": "metastasis",
        "name": "Metastatic Cancer: Why It Spreads and How to Stop It",
        "group": "Advanced",
        "ladder_rank": 27,
        "ladder_tier": "advanced",
        "description": (
            "THE PROBLEM: cancer kills not where it starts but where it "
            "goes. Roughly 90 percent of cancer deaths are caused by "
            "metastasis - cells breaking away from the primary tumor, "
            "traveling through blood or lymph, and colonizing distant "
            "organs. A primary tumor can often be cut out; metastatic "
            "disease, scattered through the body, usually cannot. "
            "BACKGROUND: Stephen Paget proposed the 'seed and soil' "
            "hypothesis in 1889: metastasis is not random - breast cancer "
            "seeds bone, colon cancer seeds liver - the seed needs "
            "congenial soil. A century later the molecular steps are "
            "partly mapped: cells undergo epithelial-to-mesenchymal "
            "transition (loosening their grip), invade vessels, survive "
            "the bloodstream's shear and immune patrols, exit at distant "
            "sites, and - the great mystery - often lie dormant for years "
            "before awakening. What wakes a dormant micrometastasis after "
            "a decade of silence is one of oncology's deepest questions. "
            "The pre-metastatic niche discovery showed primary tumors send "
            "signals ahead to prepare distant organs - the seed calls "
            "ahead to ready the soil. Yet no drug specifically prevents "
            "metastasis; every therapy targets growing cells, and dormant "
            "cells, by definition, are not growing."
        ),
        "how_it_works": (
            "WHY IT MATTERS: stopping metastasis would convert most "
            "cancers from killers into curable local diseases - the "
            "single largest prize in oncology. CURRENT STATE: research "
            "attacks each step - EMT inhibitors, anti-invasion agents, "
            "drugs that keep dormant cells asleep or wake them for the "
            "kill, and therapies targeting the pre-metastatic niche. "
            "Circulating tumor cell and tumor DNA monitoring now watches "
            "for spread in real time. The honest status: we can describe "
            "the journey in molecular detail and still cannot reliably "
            "block any single step in patients. Metastasis remains the "
            "unsolved core of cancer lethality."
        ),
        "key_points": [
            "~90 percent of cancer deaths are caused by metastasis, not the primary tumor.",
            "Paget's 1889 'seed and soil' hypothesis holds: spread follows organ preferences, not randomness.",
            "Dormancy is the deep mystery: micrometastases can sleep for years before awakening - the wake signal is unknown.",
            "Primary tumors prepare distant organs via the pre-metastatic niche - the seed calls ahead.",
            "No approved drug specifically prevents metastasis; all therapies target growing cells, and dormant cells do not grow.",
        ],
        "requirements": [
            "A solution must target a metastasis-specific step - blocking spread without merely poisoning all dividing cells.",
            "It must handle dormancy: either keep disseminated cells asleep forever or eliminate them while asleep.",
            "It must work across the seed-and-soil pairs, or at least the deadliest ones.",
            "Trials need metastasis-free survival as the endpoint - tumor shrinkage alone proves nothing about spread.",
            "It must explain organ tropism well enough to predict and intercept each cancer's preferred destinations.",
        ],
        "standards": [
            "Anti-metastatic claims require metastasis-free or overall survival endpoints, not response rates.",
            "Dormancy claims need models with validated long-term latency and defined awakening triggers.",
            "Circulating tumor cell counts need standardized assays before guiding therapy.",
        ],
        "citations": [CIT_NATURE, CIT_NEJM, CIT_LANCET],
        "sig_lens": (
            "The Signature read: metastasis is an invasion planned like a "
            "military campaign - scouts, prepared beaches, sleeper agents "
            "that wait years for the signal. Public science fights the "
            "landed army; the Signature lens intercepts the dispatches: "
            "the pre-metastatic signal, the dormancy order, the wake code "
            "- and asks which message, unsent, strands the invasion."
        ),
    },
    {
        "key": "cancer_immune_evasion",
        "name": "Cancer Immune Evasion",
        "group": "Advanced",
        "ladder_rank": 28,
        "ladder_tier": "advanced",
        "description": (
            "THE PROBLEM: the immune system destroys thousands of "
            "potentially cancerous cells daily - yet the cancers that "
            "matter are the ones that learned to become invisible to it. "
            "How tumors systematically blind, exhaust, and corrupt the "
            "immune response is only partly understood, and it is the "
            "reason immunotherapy cures some patients miraculously and "
            "fails most. BACKGROUND: the immune surveillance idea is old; "
            "the molecular evasions are newly mapped. Tumors downregulate "
            "MHC - the display cases that show their abnormal proteins to "
            "T cells. They express PD-L1, a 'do not attack' signal that "
            "exhausts approaching T cells - the discovery behind checkpoint "
            "inhibitor drugs, which won the 2018 Nobel Prize and cure a "
            "fraction of melanoma and lung cancer patients. They recruit "
            "regulatory T cells and myeloid suppressor cells as bodyguards, "
            "build fibrous walls, and starve T cells of nutrients. But "
            "checkpoint drugs fail in most cancers - pancreatic, "
            "glioblastoma, ovarian - and even responders often relapse as "
            "the tumor evolves new evasions. The tumor microenvironment is "
            "an entire corrupt ecosystem, and science has mapped only its "
            "outskirts."
        ),
        "how_it_works": (
            "WHY IT MATTERS: the immune system is the only 'drug' that can "
            "adapt as fast as cancer evolves - if tumors could not evade "
            "it, most cancers would be self-curing. Cracking evasion would "
            "extend immunotherapy's miracles from the lucky minority to "
            "the majority. CURRENT STATE: combination immunotherapies "
            "attack multiple evasions at once; personalized cancer "
            "vaccines train T cells on each tumor's unique mutations; "
            "engineered T cells (CAR-T) work in blood cancers but struggle "
            "against solid tumors' defenses. Researchers now profile the "
            "whole tumor-immune ecosystem cell by cell. The honest status: "
            "checkpoint blockade proved evasion is druggable and also "
            "proved it is redundant - block one trick and the tumor uses "
            "another. The full evasion playbook remains unwritten."
        ),
        "key_points": [
            "Tumors evade immunity through multiple redundant tricks: hiding display (MHC loss), fake surrender signals (PD-L1), recruited bodyguards, starvation, and walls.",
            "Checkpoint inhibitors won the 2018 Nobel Prize and cure a fraction of patients - proving evasion is druggable.",
            "Most cancers (pancreatic, glioblastoma, ovarian) still resist immunotherapy.",
            "Even responders relapse as tumors evolve new evasions - the defense adapts to the attack.",
            "CAR-T cures blood cancers but struggles against solid tumors' layered defenses.",
        ],
        "requirements": [
            "A solution must defeat redundant evasions simultaneously - single-trick drugs select for the next trick.",
            "It must work in immunologically 'cold' tumors, not just the inflamed ones checkpoint drugs favor.",
            "It must predict which evasion each patient's tumor uses, matching therapy to tumor.",
            "Engineered cells must penetrate solid tumors and survive their suppressive microenvironment.",
            "Autoimmune side effects of unleashed immunity must be controllable - the weapon must stay aimed.",
        ],
        "standards": [
            "Immunotherapy trials need overall survival endpoints; early tumor swelling (pseudoprogression) must not be misread as failure.",
            "Biomarker claims (PD-L1, tumor mutational burden) require pre-registered cutoffs and prospective validation.",
            "CAR-T efficacy in solid tumors must be measured against the suppressive microenvironment, not blood-cancer benchmarks.",
        ],
        "citations": [CIT_NATURE, CIT_NEJM, CIT_JANEWAY],
        "sig_lens": (
            "The Signature read: the tumor is a fortress flying false "
            "flags - surrender banners on the walls, bribed guards at the "
            "gate, poisoned wells for the besiegers. Public science "
            "captured one flag (PD-L1); the Signature lens maps the whole "
            "deception staff: every false signal, every bribed cell, and "
            "the command post that coordinates the masquerade."
        ),
    },
    {
        "key": "spinal_cord",
        "name": "Spinal Cord Injury Repair",
        "group": "Advanced",
        "ladder_rank": 29,
        "ladder_tier": "advanced",
        "description": (
            "THE PROBLEM: the spinal cord is the body's information "
            "superhighway, and when it is cut, the wires do not regrow. A "
            "severed peripheral nerve can regenerate; a severed spinal cord "
            "cannot - paralysis below the injury is permanent with current "
            "medicine. Millions live with spinal cord injury, and the "
            "central nervous system's refusal to heal is one of biology's "
            "starkest limits. BACKGROUND: the failure is active, not "
            "passive. After injury, a glial scar forms - astrocytes walling "
            "off the damage - and the scar secretes molecules (Nogo, MAG, "
            "OMgp) that actively repel regrowing axons. Myelin debris "
            "itself inhibits regrowth. Meanwhile the injured neurons "
            "mount only a feeble regrowth program, unlike peripheral "
            "neurons which switch on a vigorous one. In 2018, blocking the "
            "scar's inhibitory signals plus stimulating regrowth let rats "
            "with severe injuries walk again - a landmark proof that the "
            "blockade is reversible in principle. Epidural electrical "
            "stimulation has let some paralyzed patients stand and take "
            "steps by awakening dormant circuits below the injury. Stem "
            "cell transplants aim to bridge the gap with new neurons. But "
            "no therapy has yet reconnected a severed human spinal cord."
        ),
        "how_it_works": (
            "WHY IT MATTERS: reconnecting the cord would end paralysis - "
            "returning movement, independence, and freedom from the "
            "infections and complications that shorten injured lives. It "
            "is also the gateway problem: the same regrowth blockade "
            "limits recovery from stroke and brain injury. CURRENT STATE: "
            "the field pursues three converging paths - neutralizing the "
            "scar's stop signals, switching on the neuron's intrinsic "
            "growth program, and bridging the gap with cells or scaffolds - "
            "plus electrical stimulation that recruits surviving circuits. "
            "The honest status: rats walk in the lab, humans take assisted "
            "steps with stimulators, and true axon regrowth across a human "
            "spinal lesion remains unachieved."
        ),
        "key_points": [
            "A severed peripheral nerve regenerates; a severed spinal cord does not - the central nervous system actively blocks its own repair.",
            "The glial scar secretes Nogo, MAG, and OMgp - molecules that actively repel regrowing axons.",
            "Injured central neurons mount only a feeble growth program compared to peripheral neurons.",
            "Rat studies combining scar-blockade with growth stimulation restored walking - reversible in principle.",
            "Epidural stimulation lets some paralyzed patients stand by awakening dormant circuits below the injury.",
        ],
        "requirements": [
            "A repair must regrow axons across the lesion AND reconnect them to correct targets - growth without guidance is noise.",
            "It must neutralize the scar's inhibitors while preserving the scar's protective walling-off function.",
            "It must switch on the central neuron's dormant growth program, not just clear the path.",
            "Success means restored voluntary function, not just axon sprouting on a microscope slide.",
            "Chronic injuries (years old) must be treatable, not just fresh ones - most patients are chronic.",
        ],
        "standards": [
            "Regrowth claims require tract-tracing proof that axons crossed the lesion and formed synapses.",
            "Functional recovery needs standardized motor scores with blinded assessment.",
            "Stimulation-assisted stepping must be distinguished from true neural reconnection.",
        ],
        "citations": [CIT_KANDEL, CIT_NATURE, CIT_NEJM],
        "sig_lens": (
            "The Signature read: the spinal cord is a cut telegraph line "
            "whose repair crew was ordered to build a wall instead of "
            "splicing the wire. Public science studies the wall; the "
            "Signature lens countermands the order: silence the stop "
            "signals, wake the splicing program, and teach the regrowing "
            "wire which pole to climb."
        ),
    },
    {
        "key": "organ_regeneration",
        "name": "Organ Regeneration: Regrowing What Is Lost",
        "group": "Advanced",
        "ladder_rank": 30,
        "ladder_tier": "advanced",
        "description": (
            "THE PROBLEM: a salamander regrows a perfect limb - bone, "
            "muscle, nerves, skin - in weeks. A human cannot regrow so "
            "much as a fingertip past the nail. The machinery of "
            "regeneration exists in vertebrate biology, and mammals have "
            "largely switched it off. Why - and how to switch it back on - "
            "is unsolved. BACKGROUND: the liver is the great exception: "
            "humans can regenerate up to two-thirds of it, which is why "
            "living-donor liver transplant works. Skin heals, bone knits, "
            "but always with scarring - repair, not regeneration. The "
            "salamander's secret is the blastema: a mound of dedifferentiated "
            "cells at the amputation site that replays embryonic "
            "development, reading positional memory (cells 'know' whether "
            "they are shoulder or wrist) to rebuild exactly what was lost. "
            "Mammals form scar instead of blastema. Key regulators are "
            "emerging: the Hippo/YAP pathway controls organ size and "
            "regenerative growth; immune system differences (salamanders "
            "regenerate without the scarring inflammation mammals mount) "
            "may decide blastema vs. scar. In 2022, stimulating YAP in "
            "pig hearts after heart attack drove meaningful cardiac "
            "regeneration - the mammalian heart, famously non-regenerative, "
            "budged."
        ),
        "how_it_works": (
            "WHY IT MATTERS: true regeneration would end the organ "
            "shortage, heal heart attack damage, regrow limbs, and reverse "
            "injuries medicine currently manages forever. It is the "
            "difference between repairing the machine and regrowing the "
            "part. CURRENT STATE: the field has moved from marveling at "
            "salamanders to dissecting the mammalian block - mapping the "
            "gene circuits active in blastema but silent in scar, testing "
            "whether transient reprogramming can reopen the regenerative "
            "window without causing cancer (uncontrolled growth is "
            "regeneration's evil twin). The honest status: we understand "
            "pieces of the salamander's program and have nudged mammalian "
            "hearts and digits slightly toward it, but no one has regrown "
            "a complex mammalian organ or limb."
        ),
        "key_points": [
            "Salamanders regrow perfect limbs via the blastema; mammals form scar instead.",
            "The human liver regenerates substantially - the exception proving the machinery exists in us.",
            "Positional memory lets blastema cells rebuild exactly what was lost, not a generic lump.",
            "The Hippo/YAP pathway is emerging as a master regulator of regenerative growth.",
            "Uncontrolled growth is regeneration's evil twin: reopening the program risks cancer.",
        ],
        "requirements": [
            "Regeneration must be patterned, not just growth - a hand, not a tumor.",
            "It must be controllable: switched on for repair, switched off before cancer.",
            "It must work in adult mammals, not just embryos or amphibians.",
            "The immune system's scarring response must be modulated without crippling defense.",
            "Success means functional organs with nerves and vessels integrated, not tissue lumps.",
        ],
        "standards": [
            "Regeneration claims require histological proof of patterned, innervated, vascularized tissue.",
            "Growth-control claims need long-term tumor surveillance in treated animals.",
            "Functional integration must be demonstrated (contractile heart muscle, load-bearing bone), not just tissue presence.",
        ],
        "citations": [CIT_NATURE, CIT_NEJM, CIT_ROBBINS],
        "sig_lens": (
            "The Signature read: the body kept the blueprints for every "
            "part it ever built and then locked the archive - scarring "
            "where the salamander rebuilds. Public science admires the "
            "salamander; the Signature lens picks the mammalian lock: the "
            "blastema program sleeping in our own genome, and the precise "
            "key - signal, timing, and off-switch - that wakes it safely."
        ),
    },
    {
        "key": "transplant_tolerance",
        "name": "Transplant Immune Tolerance Without Lifelong Drugs",
        "group": "Advanced",
        "ladder_rank": 31,
        "ladder_tier": "advanced",
        "description": (
            "THE PROBLEM: organ transplantation saves lives, then demands a "
            "lifelong ransom: immunosuppressive drugs that keep the new "
            "organ from being rejected while leaving the patient vulnerable "
            "to infections, cancers, kidney damage, and diabetes. The "
            "immune system correctly identifies the donor organ as foreign "
            "and attacks it; the drugs blunt the entire immune system to "
            "stop the attack. Half of transplanted kidneys still fail "
            "within a decade or so, often to slow chronic rejection the "
            "drugs cannot fully prevent. BACKGROUND: the dream is "
            "tolerance - teaching the immune system to accept the organ as "
            "self, the way it accepts the body's own tissues, so drugs can "
            "stop. Nature provides the proof it is possible: a mother's "
            "immune system tolerates a fetus that is half foreign, through "
            "specialized regulatory mechanisms. In the 1950s, Medawar "
            "showed tolerance could be induced in mice; in humans, rare "
            "patients have stopped immunosuppression without rejecting - "
            "usually after losing the drugs to noncompliance, a dangerous "
            "experiment nobody prescribes. Mixed chimerism protocols "
            "(giving the recipient some of the donor's bone marrow so the "
            "two immune systems coexist) have induced tolerance in small "
            "trials, but the conditioning is harsh and the results "
            "inconsistent. Regulatory T cell therapies - infusing the "
            "immune system's own peacekeepers - are in early trials."
        ),
        "how_it_works": (
            "WHY IT MATTERS: true tolerance would free hundreds of "
            "thousands of transplant recipients from lifelong drugs and "
            "their toxicities, extend organ survival, and expand "
            "transplantation to patients too frail for immunosuppression. "
            "The same tolerance machinery is what fails in autoimmune "
            "disease and allergy - solving it here echoes everywhere. "
            "CURRENT STATE: mixed chimerism and regulatory T cell "
            "therapies have produced drug-free tolerance in subsets of "
            "patients, proving the goal is reachable. The field now hunts "
            "the minimal, safe protocol - the lightest conditioning that "
            "reliably teaches acceptance. The honest status: tolerance is "
            "achieved occasionally, unpredictably, and often harshly. A "
            "routine, safe path to drug-free transplantation does not yet "
            "exist."
        ),
        "key_points": [
            "Transplant recipients trade organ rejection for lifelong immunosuppression and its toxicities.",
            "Half of transplanted kidneys still fail within about a decade, often to chronic rejection.",
            "Pregnancy proves the immune system CAN tolerate half-foreign tissue - the machinery exists.",
            "Mixed chimerism has induced drug-free tolerance in small trials, but conditioning is harsh.",
            "Regulatory T cell therapies aim to infuse the immune system's own peacekeepers.",
        ],
        "requirements": [
            "Tolerance must be durable and drug-free - reduced drugs are progress, not the goal.",
            "Induction must be safe enough for routine use, not just desperate cases.",
            "It must preserve defense against infections and cancers - tolerance to the organ, vigilance to everything else.",
            "It must handle the sensitized patient: those with prior transplants or transfusions are hardest to tolerize.",
            "Success needs decades of organ survival data, not months of drug-free follow-up.",
        ],
        "standards": [
            "Tolerance claims require documented drug-free graft survival with protocol biopsies showing no rejection.",
            "Chimerism protocols need standardized conditioning with pre-registered toxicity stopping rules.",
            "Immune monitoring must prove donor-specific unresponsiveness with intact third-party responses.",
        ],
        "citations": [CIT_NEJM, CIT_JANEWAY, CIT_NATURE],
        "sig_lens": (
            "The Signature read: the transplanted organ is an honored "
            "guest the body's guards keep trying to evict - so medicine "
            "drugs the guards into stupor for life. Public science "
            "negotiates ceasefires; the Signature lens studies the "
            "mother's treaty: the natural tolerance of pregnancy, and how "
            "to draft the same peace for a kidney."
        ),
    },
    {
        "key": "anesthesia_mechanism",
        "name": "The Mechanism of General Anesthesia",
        "group": "Advanced",
        "ladder_rank": 32,
        "ladder_tier": "advanced",
        "description": (
            "THE PROBLEM: every day, millions of people are rendered "
            "unconscious by drugs whose mechanism remains mysterious. "
            "General anesthetics - from ether in 1846 to propofol and "
            "sevoflurane today - reliably erase consciousness, memory, "
            "and pain, then return them on command. How a small molecule "
            "switches off the most complex phenomenon in nature, and "
            "switches it back on, is still not fully explained. "
            "BACKGROUND: the Meyer-Overton rule (1899) noted anesthetic "
            "potency tracks lipid solubility - suggesting the drugs "
            "dissolve into neural membranes and gum up the works. Modern "
            "work found specific protein targets: most anesthetics enhance "
            "GABA (the brain's main inhibitory signal) or block NMDA "
            "glutamate receptors, among other targets. But these are "
            "descriptions of which knobs turn, not of why turning them "
            "extinguishes consciousness itself. The deeper theories reach "
            "for consciousness: that anesthetics disrupt integrated "
            "information flow across the cortex, collapse the brain's "
            "dynamic repertoire, or disconnect feedback loops - each with "
            "supporting evidence, none complete. Anesthesia awareness - "
            "patients conscious but paralyzed during surgery - proves the "
            "components (unconsciousness, amnesia, immobility) are "
            "separable, deepening the puzzle: the drug does several "
            "things, and we cannot fully say how any one of them works."
        ),
        "how_it_works": (
            "WHY IT MATTERS: beyond safer surgery, the anesthesia "
            "mechanism is the most experimentally tractable handle on "
            "consciousness itself - the one phenomenon we can switch off "
            "and on at will. Understanding it would illuminate coma, "
            "sleep, and the nature of awareness, while making anesthesia "
            "safer for the very young and very old, where cognitive side "
            "effects are a real concern. CURRENT STATE: neuroscience "
            "compares the awake, dreaming, anesthetized, and comatose "
            "brain with high-resolution recording, hunting the network "
            "property that vanishes when consciousness does. Theories of "
            "integrated information and global workspace make competing "
            "predictions that experiments are now testing. The honest "
            "status: anesthesiologists dose with exquisite practical "
            "skill guided by a century of experience, atop a mechanism "
            "that remains one of science's great open questions."
        ),
        "key_points": [
            "General anesthetics reliably switch consciousness off and on; the full mechanism remains unexplained.",
            "The 1899 Meyer-Overton rule linked potency to lipid solubility - a clue, not an explanation.",
            "Modern targets (GABA enhancement, NMDA blockade) describe which knobs turn, not why consciousness extinguishes.",
            "Anesthesia awareness proves unconsciousness, amnesia, and immobility are separable components.",
            "The mechanism is the most tractable experimental handle on consciousness itself.",
        ],
        "requirements": [
            "A mechanism must explain reversibility: the same brain, switched off and on without damage.",
            "It must explain the separability: why awareness without memory, or immobility without unconsciousness, can occur.",
            "It must connect molecular targets to network effects to the subjective loss of experience.",
            "It should predict which drug combinations achieve each component independently.",
            "Any consciousness theory it supports must also account for sleep, coma, and dreaming.",
        ],
        "standards": [
            "Depth-of-anesthesia claims require validated monitors correlated with explicit recall testing.",
            "Awareness studies need structured postoperative interviews (Brice protocol or equivalent).",
            "Consciousness-theory predictions must be pre-registered against competing theories' predictions.",
        ],
        "citations": [CIT_KANDEL, CIT_NATURE, CIT_NEJM],
        "sig_lens": (
            "The Signature read: anesthesia is the one proven off-switch "
            "for the most mysterious machine in existence - and we found "
            "the switch by accident, centuries before understanding the "
            "machine. Public science catalogs which wires the switch "
            "touches; the Signature lens traces the current: what pattern "
            "of flow IS the lights being on, such that interrupting it is "
            "oblivion and restoring it is return."
        ),
    },
    {
        "key": "aging_biology",
        "name": "The Biology of Aging",
        "group": "Advanced",
        "ladder_rank": 33,
        "ladder_tier": "advanced",
        "description": (
            "THE PROBLEM: aging is the largest cause of death and disease "
            "on earth - the master risk factor behind cancer, heart "
            "disease, Alzheimer, and frailty - yet biology still debates "
            "what aging fundamentally IS. Is it accumulated damage "
            "(mutations, worn proteins, broken mitochondria), a programmed "
            "process (genes that schedule decline), or an information "
            "problem (the epigenome - the cell's instruction annotations - "
            "losing its organization)? BACKGROUND: the hallmarks of aging "
            "paper (2013, updated 2023) catalogued the prime suspects: "
            "genomic instability, telomere shortening, epigenetic "
            "alterations, loss of proteostasis, disabled macroautophagy, "
            "deregulated nutrient sensing, mitochondrial dysfunction, "
            "cellular senescence, stem cell exhaustion, altered "
            "intercellular communication, chronic inflammation, and "
            "dysbiosis. Caloric restriction extends life in species from "
            "yeast to monkeys, proving aging's rate is adjustable. The "
            "discovery that aged cells can be reprogrammed to youth "
            "(Yamanaka factors, 2006; partial reprogramming rejuvenating "
            "aged mice tissues in the 2020s) suggests aging is at least "
            "partly an information state, not just accumulated damage - "
            "you cannot un-break a broken machine by rebooting its "
            "software, yet rebooting works. Senolytics - drugs that clear "
            "senescent 'zombie' cells - extend healthspan in mice. But "
            "whether these levers slow human aging, and what aging is "
            "beneath them all, remains open."
        ),
        "how_it_works": (
            "WHY IT MATTERS: aging underlies nearly every disease of later "
            "life; slowing it would delay them all at once - the "
            "geroscience hypothesis, medicine's highest-leverage idea. A "
            "true biology of aging would turn medicine from "
            "disease-by-disease firefighting to maintaining the building. "
            "CURRENT STATE: the field tests the levers in humans - "
            "metformin, rapamycin analogs, senolytics, and partial "
            "reprogramming are all in or approaching human trials - while "
            "the fundamental debate (damage vs. program vs. information "
            "loss) continues. Epigenetic clocks can now measure biological "
            "age from DNA methylation, giving trials a readout faster "
            "than waiting for death. The honest status: aging is "
            "measurable, partially adjustable in animals, and still "
            "theoretically unresolved - we have hallmarks, not a theory."
        ),
        "key_points": [
            "Aging is the master risk factor for cancer, heart disease, Alzheimer, and frailty - the largest cause of death.",
            "The hallmarks catalog (2013/2023) lists the suspects but not the culprit - hallmarks, not a theory.",
            "Caloric restriction extends lifespan from yeast to monkeys: aging's rate is adjustable.",
            "Partial reprogramming rejuvenates aged mouse tissues - suggesting aging is partly an information state.",
            "Epigenetic clocks now measure biological age from DNA methylation, giving trials a fast readout.",
        ],
        "requirements": [
            "A theory must choose among - or unify - damage accumulation, programmed decline, and information loss.",
            "It must explain the reprogramming result: why resetting epigenetic information rejuvenates without fixing 'damage.'",
            "Interventions must extend healthspan (healthy years), not just lifespan - extra frail years are not the goal.",
            "Human trials need validated surrogate endpoints (epigenetic clocks) proven to predict real outcomes.",
            "Any rejuvenation therapy must prove it does not raise cancer risk - youth signals and growth signals overlap.",
        ],
        "standards": [
            "Aging-intervention trials require pre-registered biological-age endpoints validated against hard outcomes.",
            "Lifespan claims in animals need multi-site replication with standardized husbandry.",
            "Reprogramming therapies need long-term tumor surveillance with pre-registered monitoring.",
        ],
        "citations": [CIT_NATURE, CIT_NEJM, CIT_LANCET],
        "sig_lens": (
            "The Signature read: aging is a library where the books are "
            "fine but the catalog is smudged - the information survives, "
            "the index decays. Public science debates whether the books "
            "are damaged; the Signature lens bets on the catalog: the "
            "epigenetic annotations, the software of the cell, and whether "
            "a careful reboot restores the reader without burning the "
            "library down."
        ),
    },
    {
        "key": "full_regeneration",
        "name": "The Full Regeneration Problem: Limbs and Whole Organs",
        "group": "Advanced",
        "ladder_rank": 34,
        "ladder_tier": "advanced",
        "description": (
            "THE PROBLEM: the ultimate prize of regenerative medicine - "
            "regrowing a lost human limb or a whole organ, on demand, in "
            "an adult - remains beyond reach. This record's sibling (rank "
            "30) covers the biology of regeneration; this record is the "
            "compounded summit: the full engineering problem of rebuilding "
            "complex structures in people. A limb is not one tissue but "
            "dozens - bone, muscle, tendon, nerve, vessel, skin - patterned "
            "in three dimensions, wired to the nervous system, plumbed to "
            "the circulation, all grown in the right proportions at the "
            "right time. BACKGROUND: the pieces are advancing separately. "
            "Decellularized organ scaffolds - donor organs washed of cells, "
            "leaving the structural matrix - can be reseeded with a "
            "patient's own cells; small clinical successes exist for "
            "trachea and bladder. Organoids - miniature lab-grown organs - "
            "model disease but are not transplantable wholes. 3D "
            "bioprinting builds tissue shapes layer by layer but cannot "
            "yet print the fine vascular and neural networks a real organ "
            "needs. Xenotransplantation (gene-edited pig organs) had its "
            "first human milestones in the 2020s, offering a parallel path "
            "that sidesteps regrowth entirely. The integration problem is "
            "the wall: growing cells is now feasible; growing a patterned, "
            "wired, plumbed, immune-accepted whole is not."
        ),
        "how_it_works": (
            "WHY IT MATTERS: full regeneration or whole-organ engineering "
            "would end the transplant waiting list (where thousands die "
            "yearly waiting), restore amputees completely, and make "
            "degenerative organ failure a solvable problem rather than a "
            "sentence. It is the capstone of the teaching ladder: every "
            "earlier record's lesson - immune tolerance, patterning, "
            "vascularization, growth control - must be mastered together. "
            "CURRENT STATE: the field advances on parallel tracks - "
            "scaffold reseeding, bioprinting, organoids, xenotransplantation "
            "- each solving part of the puzzle. The honest status: no "
            "approach has produced a complex, fully functional, "
            "patient-derived whole organ or limb. The problem stands as "
            "the summit because it demands every other hard problem in "
            "this database be solved simultaneously."
        ),
        "key_points": [
            "A limb or organ is dozens of tissues patterned in 3D, wired, plumbed, and proportioned - not just cells.",
            "Decellularized scaffolds, organoids, bioprinting, and xenotransplantation each solve part of the puzzle.",
            "3D bioprinting cannot yet print the fine vascular and neural networks a real organ needs.",
            "Thousands die yearly on transplant waiting lists - the cost of the unsolved problem.",
            "This is the ladder's summit: it demands immune tolerance, patterning, vascularization, and growth control together.",
        ],
        "requirements": [
            "A solution must deliver patterned multi-tissue structures with integrated nerves and vessels.",
            "The construct must be immune-accepted - patient-derived or tolerized - or rejection returns.",
            "Growth must stop at the right size and shape: patterning without control is a tumor.",
            "Function must be demonstrated under load: a heart that pumps, a limb that moves and feels.",
            "Manufacturing must be scalable and timely - a bespoke organ that takes a year helps few.",
        ],
        "standards": [
            "Whole-organ claims require demonstrated vascular perfusion, innervation, and organ-level function.",
            "Long-term studies must track growth control, immune acceptance, and durability over years.",
            "First-in-human trials need independent review proportionate to the irreversible nature of implantation.",
        ],
        "citations": [CIT_NATURE, CIT_NEJM, CIT_ROBBINS],
        "sig_lens": (
            "The Signature read: the body is a cathedral the builders "
            "abandoned mid-construction, the scaffolds still standing. "
            "Public science brings new stones one at a time; the Signature "
            "lens summons the master builder's plan - the developmental "
            "program that raised the cathedral once, and whether its "
            "orders can be reissued, in order, to raise it again."
        ),
    },
]
)
