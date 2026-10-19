#!/usr/bin/env python3
"""Entries for The Unsolved Dentistry Database (unsolved-dentistry) and its
Signature half (unsolved-dentistry-signature).

34 famous unsolved problems in dentistry, ladder-ordered by accessibility
(rank 1 = most approachable, rank 34 = most complex/compounded).
Public half: real, fact-checked problems. Signature half: the same 34
problems through the Signature lens, with Signature-generated proposed
solutions that are ALWAYS labeled as proposals, never established science.

Honesty rule (enforced in every record): never claim proof, never imply
peer acceptance, never present speculation as settled. Signature proposals
are labeled speculation for research discussion only - never dental advice,
never a treatment recommendation, no cure claims.
"""

LABEL = "Signature-generated proposed solution \u2014 not established science."

SIG_TAIL = ("Signature editions carry the Signature system's proposed "
            "solution approaches to famous unsolved problems. Every "
            "solution is labeled a Signature-generated proposal, never "
            "established science, never peer-accepted, never proof, never "
            "dental advice.")

STD_COMMON = [
    "Problem statements verified against the published dental literature; open status confirmed as of 2026.",
    "Signature solution sections are labeled proposals: they state assumptions, a reasoning path, a proposed mechanism, what would confirm or kill them, and what they do not claim.",
    "Signature proposals are labeled speculation for research discussion only - never dental advice, never a treatment recommendation; no cure claims appear.",
]

ENTRIES = [
# ------------------------------------------------------------------ rank 1
{
 "key": "caries-resistance",
 "name": "Why Some People Resist Dental Caries",
 "group": "Cariology",
 "ladder_rank": 1, "ladder_tier": "foundations",
 "problem": "Some people never brush and never get cavities, while others brush diligently and decay - what makes a mouth caries-resistant?",
 "description": "Dental caries is the commonest chronic disease on earth, yet susceptibility varies enormously between individuals with similar habits. The resistant mouth has some combination of protective factors - saliva composition, enamel structure, microbiome ecology, immune factors - that science has not fully mapped. Understanding resistance would redirect prevention from fighting disease to cultivating protection.",
 "background": "Miller's chemoparasitic theory (1890) established acid-from-bacteria as the mechanism; Keyes (1960s) proved caries transmissible in animals. Fluoride (1940s-50s) cut population caries dramatically without explaining individual resistance. Research since has mapped pieces: salivary flow and buffering, enamel mineralization differences, Streptococcus mutans levels (Loesche), and more recently the ecological plaque hypothesis (Marsh) - caries as dysbiosis rather than single-pathogen infection. Twin studies show heritability of caries experience. As of 2026 no complete account of natural resistance exists.",
 "why_it_matters": "Caries causes pain, tooth loss, and billions in treatment costs, concentrated in the disadvantaged. Bottling natural resistance - as a rinse, a probiotic, a treatment - would prevent more disease than any restorative advance.",
 "sig_pointer": "The Signature system's proposed approach treats the resistant mouth as an ecology to be mapped and transplanted, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that caries resistance is an ecological property: the resistant mouth maintains a microbial community and salivary chemistry that never lets acid-producers dominate, even under sugar challenge. "
  "Assumptions: (1) resistance is community-level, not single-factor; (2) the protective ecology is transferable in principle; (3) saliva chemistry sets the ecological rules. "
  "Reasoning path: an ecology model explains why single factors (fluoride, S. mutans counts) predict poorly - the community compensates - and predicts that whole-ecology transfer will outperform single-probiotic approaches. "
  "Proposed mechanism: a 'resistance ecology' map of protective mouths (microbial networks plus salivary chemistry), developed into ecological therapeutics that establish the protective community. "
  "What would confirm it: ecological therapeutics reducing caries in trials beyond fluoride, with community profiles converging on resistant patterns. "
  "What would kill it: evidence that resistance is purely structural (enamel) with no ecological component, or that oral ecologies resist transplantation. "
  "What this does not claim: it does not claim a preventive product exists, does not advise against fluoride or brushing, and does not constitute dental advice."),
 "sig_lens": "The Signature lens reads the cavity-free mouth as a defended ecology, and asks what community rules keep the acid-producers losing.",
 "how_it_works": "Cariologists study resistance through twin and family studies, salivary proteomics, plaque microbiome sequencing, and longitudinal caries cohorts.",
 "key_points": [
  "Caries is the commonest chronic disease worldwide.",
  "Susceptibility varies enormously at similar hygiene levels.",
  "Miller (1890) and Keyes (1960s) established the bacterial mechanism.",
  "The ecological plaque hypothesis reframes caries as dysbiosis.",
  "Twin studies show caries experience is heritable.",
 ],
 "requirements": [
  "A complete ecological and chemical map of resistant mouths.",
  "Proof that protective ecologies are transferable.",
  "Therapeutics that establish resistance durably.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Miller WD. The Micro-Organisms of the Human Mouth. 1890.",
  "Keyes PH. Infectious and transmissible nature of experimental dental caries. Archives of Oral Biology. 1960;1:304-320.",
  "Marsh PD. Microbial ecology of dental plaque and its significance in health and disease. Advances in Dental Research. 1994;8(2):263-271.",
  "Selwitz RH et al. Dental caries. Lancet. 2007;369:51-59.",
 ],
 "demo_data": {"a": ("adults with untreated caries, percent worldwide (approx)", 35.0),
               "b": ("percent scale", 100.0), "bounds": (0.25, 0.45),
               "step1": "over a third of adults carry untreated decay - while some mouths never decay at all",
               "confirm": "ecological therapeutics beat fluoride with communities converging on resistant patterns",
               "refute": "resistance proves purely structural with oral ecologies untransplantable"},
},
# ------------------------------------------------------------------ rank 2
{
 "key": "caries-vaccine",
 "name": "Complete Caries Prevention: The Vaccine Dream",
 "group": "Cariology",
 "ladder_rank": 2, "ladder_tier": "foundations",
 "problem": "Caries is a bacterial disease - so why is there no vaccine, and what would it take to immunize against tooth decay?",
 "description": "A caries vaccine has been pursued since the 1960s: immunize against Streptococcus mutans adhesins or glucosyltransferases, block colonization, prevent decay. Animal trials showed promise; human trials showed the problems - the mouth is colonized early and persistently, mucosal immunity is short-lived, S. mutans is one player in a dysbiosis, and the commercial case for a vaccine against a non-lethal disease is weak. The dream persists because the prize is enormous.",
 "background": "Bowen's rhesus-monkey work (1969) proved immunization could reduce caries; human trials of S. mutans antigen vaccines (Taubman, Smith) showed salivary IgA responses but modest clinical effects. The field then confronted the ecology problem: targeting one species in a dysbiotic community. Passive immunization (antibodies in mouthwash, plantibodies) showed transient effects. Meanwhile fluoride, sealants, and silver diamine fluoride delivered practical prevention without immunology. As of 2026 no caries vaccine is in late-stage development.",
 "why_it_matters": "A working caries vaccine would be the single highest-leverage preventive intervention in dentistry: one course in childhood replacing a lifetime of drilling. Its absence is the field's most conspicuous failure.",
 "sig_pointer": "The Signature system's proposed approach treats the vaccine target as the dysbiotic shift, not the species, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that caries vaccines failed by targeting a species instead of a process: the disease is the ecological shift toward acid production, and immunity should target the shift's enablers - glucan-mediated adhesion and acid tolerance - across species. "
  "Assumptions: (1) the dysbiotic shift has conserved molecular enablers; (2) mucosal immunity can be made durable with the right platform; (3) blocking the shift prevents disease even with S. mutans present. "
  "Reasoning path: a process-target model explains species-vaccine failures and predicts that anti-dysbiosis immunity will outperform anti-S. mutans immunity. "
  "Proposed mechanism: a 'dysbiosis vaccine' targeting conserved adhesion and acid-tolerance factors, delivered on a durable mucosal platform, tested against caries increment in trials. "
  "What would confirm it: process-targeted immunization reducing caries beyond species-targeted approaches in trials. "
  "What would kill it: evidence that mucosal immunity in the mouth cannot be made durable, or that the dysbiotic shift has no conserved targets. "
  "What this does not claim: it does not claim a vaccine is near, does not advise against current prevention, and does not constitute dental advice."),
 "sig_lens": "The Signature lens reads the failed vaccine as aiming at the wrong target, and asks what process-level immunity would block the disease.",
 "how_it_works": "Researchers study caries vaccines through antigen discovery, mucosal immunology, animal caries models, and the small history of human trials.",
 "key_points": [
  "Caries vaccines have been pursued since the 1960s.",
  "Animal trials showed promise; human trials showed modest effects.",
  "S. mutans is one player in a dysbiotic community, not a lone pathogen.",
  "Mucosal immunity in the mouth is short-lived.",
  "No caries vaccine is in late-stage development.",
 ],
 "requirements": [
  "Conserved process-level targets of the dysbiotic shift.",
  "A durable mucosal immunity platform.",
  "Clinical proof of caries reduction in humans.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Bowen WH. Effects of immunization against Streptococcus mutans. British Dental Journal. 1969;126:159-162.",
  "Taubman MA, Nash DA. The scientific and public-health imperative for a vaccine against dental caries. Nature Reviews Immunology. 2006;6:555-563.",
  "Smith DJ. Dental caries vaccines: prospects and concerns. Critical Reviews in Oral Biology and Medicine. 2002;13(4):335-349.",
  "Russell MW et al. Mucosal immunology of the oral cavity. Various; 2000-2015.",
 ],
 "demo_data": {"a": ("years of caries-vaccine research (since 1960s)", 60.0),
               "b": ("licensed caries vaccines", 0.5), "bounds": (60.0, 240.0),
               "step1": "six decades of research, zero licensed vaccines - the longest dry run in dental prevention",
               "confirm": "process-targeted immunization beats species-targeted approaches in trials",
               "refute": "mucosal immunity proves undurable in the mouth regardless of platform"},
},
# ------------------------------------------------------------------ rank 3
{
 "key": "perio-systemic",
 "name": "Periodontal Disease Systemic Links",
 "group": "Periodontology",
 "ladder_rank": 3, "ladder_tier": "foundations",
 "problem": "Gum disease correlates with heart disease, diabetes, and preterm birth - but which links are causal, and does treating gums help the body?",
 "description": "Periodontitis - chronic inflammatory destruction of tooth-supporting tissues - affects roughly half of adults over 30. Epidemiologically it associates with cardiovascular disease, diabetes, adverse pregnancy outcomes, rheumatoid arthritis, and Alzheimer's. But association is not causation: shared risk factors (smoking, age, socioeconomic status) confound everything, and periodontal treatment trials show modest or no effects on systemic outcomes - except diabetes, where the signal is strongest.",
 "background": "The focal-infection theory (early 1900s) first linked mouth to body, then fell into disrepute from overreach. Modern links emerged in the 1990s: Offenbacher's pregnancy work, Beck's cardiovascular cohorts. Mechanistic pathways proposed: bacteremia, systemic inflammation (CRP, IL-6), and molecular mimicry (P. gingivalis citrullination in rheumatoid arthritis). Treatment trials disappointed: periodontal therapy doesn't clearly prevent heart attacks or preterm birth. The diabetes link is bidirectional and best supported - treating periodontitis modestly improves glycemic control (meta-analyses). As of 2026 causation is proven for almost nothing beyond the diabetes association.",
 "why_it_matters": "If gum treatment prevented heart attacks, dentistry would be cardiology's cheapest intervention. If the links are confounding, the field must stop promising systemic benefits. Honest causation matters for both medicine and dentistry.",
 "sig_pointer": "The Signature system's proposed approach separates the causal links from the confounded ones link by link, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that the perio-systemic literature conflates several distinct relationships - some causal, some confounded, some reverse-caused - and that only link-by-link causal analysis can sort them. "
  "Assumptions: (1) different systemic links have different causal structures; (2) Mendelian randomization and trial evidence can separate them; (3) the inflammatory burden is the most plausible causal pathway. "
  "Reasoning path: a link-by-link model explains why diabetes shows treatment effects while cardiovascular doesn't - the causal structures differ - and predicts targeted trials will confirm some links while burying others. "
  "Proposed mechanism: a 'causal atlas' of perio-systemic links using genetic instruments and designed trials, directing treatment recommendations only to proven-causal links. "
  "What would confirm it: the atlas confirming the diabetes link while falsifying others, with treatment trials matching predictions. "
  "What would kill it: evidence that even the diabetes link is confounded, collapsing the causal case entirely. "
  "What this does not claim: it does not claim gum treatment prevents systemic disease, does not advise treatment for systemic benefit, and does not constitute dental or medical advice."),
 "sig_lens": "The Signature lens reads the perio-systemic literature as several different relationships wearing one correlation, and asks which would survive a causal test.",
 "how_it_works": "Researchers study the links through prospective cohorts, Mendelian randomization, periodontal treatment trials with systemic endpoints, and mechanistic bacteremia/inflammation work.",
 "key_points": [
  "Periodontitis affects ~half of adults over 30.",
  "It associates with cardiovascular disease, diabetes, preterm birth, RA, Alzheimer's.",
  "Shared risk factors confound nearly every association.",
  "Treatment trials show little systemic benefit except modest glycemic improvement.",
  "Causation is unproven for almost every link.",
 ],
 "requirements": [
  "Link-by-link causal analysis separating causation from confounding.",
  "Treatment trials with systemic endpoints for the plausible links.",
  "Honest communication of which links are proven versus hoped.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Offenbacher S et al. Periodontal infection as a possible risk factor for preterm low birth weight. Journal of Periodontology. 1996;67(10 Suppl):1103-1113.",
  "Beck J et al. Periodontal disease and cardiovascular disease. Journal of Periodontology. 1996;67(10 Suppl):1123-1137.",
  "Teeuw WJ et al. Effect of periodontal treatment on glycemic control. Diabetes Care. 2010;33(2):421-427.",
  "Sanz M et al. Periodontitis and cardiovascular diseases: consensus report. Journal of Clinical Periodontology. 2020;47:268-288.",
 ],
 "demo_data": {"a": ("adults over 30 with periodontitis, percent (approx)", 47.0),
               "b": ("percent scale", 100.0), "bounds": (0.35, 0.6),
               "step1": "nearly half of adults carry the exposure - making every correlation suspect",
               "confirm": "the causal atlas confirms some links and falsifies others with trials matching predictions",
               "refute": "even the diabetes link proves fully confounded"},
},
# ------------------------------------------------------------------ rank 4
{
 "key": "pulp-regeneration",
 "name": "Pulp Regeneration: Bringing Dead Teeth Back to Life",
 "group": "Endodontics",
 "ladder_rank": 4, "ladder_tier": "foundations",
 "problem": "Root canal kills the tooth to save it - why can't the pulp be regenerated instead, and what would a living root-filled tooth require?",
 "description": "When pulp dies from decay or trauma, the standard is root canal: remove the pulp, fill the space with gutta-percha, and accept a dead, brittle tooth. Regenerative endodontics aims to regrow pulp instead - revascularization procedures in immature teeth show it is partially possible: bleeding induced into the canal brings stem cells that form vital-ish tissue. But the regenerated tissue is often bone-like rather than true pulp, and mature teeth with closed apices resist revascularization.",
 "background": "Revascularization was reported by Iwaya (2001) and systematized by Trope/Banchs (2004): disinfect the canal, induce apical bleeding, let the clot scaffold stem cells from the apical papilla (SCAP). Case series show continued root development in immature necrotic teeth. But histology reveals the ingrown tissue is often cementum/bone-like, not pulp with odontoblasts; disinfection sufficient to allow regrowth is hard to achieve without killing stem cells; and the technique fails in mature teeth. True pulp-dentin regeneration - odontoblasts lining dentin, innervated vascular pulp - remains unachieved. As of 2026 regenerative endodontics is a partial success awaiting its biology.",
 "why_it_matters": "A living tooth resists fracture, senses damage, and defends itself; a root-filled tooth does none of these and eventually fails. Regenerating pulp would convert endodontics from embalming to healing.",
 "sig_pointer": "The Signature system's proposed approach treats the canal as a scaffold awaiting the right cell instructions, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that revascularization underperforms because the blood clot is a poor scaffold and the canal lacks pulp-patterning signals: stem cells arrive but receive bone instructions from the dentin walls. "
  "Assumptions: (1) SCAP and similar cells are pulp-competent given correct signals; (2) dentin matrix releases instructive molecules when properly conditioned; (3) the missing element is patterning, not cells. "
  "Reasoning path: a patterning model explains why tissue forms but as bone-like - the cells are willing, the instructions are wrong - and predicts that signal-conditioned scaffolds will yield true pulp. "
  "Proposed mechanism: 'instructive scaffolds' that present pulp-patterning signals (dentin-derived growth factors, spatially organized) to incoming stem cells, tested histologically for true pulp-dentin complex. "
  "What would confirm it: scaffold-guided regeneration producing odontoblast-lined, innervated pulp in models and then humans. "
  "What would kill it: evidence that adult stem cells cannot form true pulp regardless of signals, or that disinfection and stem-cell survival are mutually exclusive. "
  "What this does not claim: it does not claim pulp can be regenerated today, does not advise against root canal, and does not constitute dental advice."),
 "sig_lens": "The Signature lens reads the revascularized canal as willing cells receiving wrong instructions, and asks what scaffold would teach pulp.",
 "how_it_works": "Endodontic researchers study regeneration through SCAP biology, scaffold trials, disinfection protocols balancing kill versus stem-cell survival, and histology of revascularized teeth.",
 "key_points": [
  "Root canal saves the tooth by killing its pulp.",
  "Revascularization (Iwaya 2001, Banchs/Trope 2004) regrows vital-ish tissue in immature teeth.",
  "The ingrown tissue is often bone-like, not true pulp.",
  "Mature teeth with closed apices resist revascularization.",
  "True pulp-dentin complex regeneration remains unachieved.",
 ],
 "requirements": [
  "Scaffolds presenting pulp-patterning signals, not just clots.",
  "Disinfection compatible with stem-cell survival.",
  "Histological proof of true pulp: odontoblasts, innervation, vasculature.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Iwaya SI et al. Revascularization of an immature permanent tooth with apical periodontitis. Journal of Endodontics. 2001;27(3):185-187.",
  "Banchs F, Trope M. Revascularization of immature permanent teeth with apical periodontitis. Journal of Endodontics. 2004;30(4):196-200.",
  "Sonoyama W et al. Characterization of the apical papilla and its residing stem cells (SCAP). Journal of Dental Research. 2008;87(7):661-666.",
  "Diogenes A et al. Regenerative endodontics: a way forward. Journal of Endodontics. 2016;42(5):645-658.",
 ],
 "demo_data": {"a": ("root canal treatments per year, US millions (approx)", 15.0),
               "b": ("regenerative pulp procedures per year, US millions (approx)", 0.005), "bounds": (2000.0, 5000.0),
               "step1": "millions of pulps are removed yearly while regeneration remains experimental",
               "confirm": "instructive scaffolds yield true pulp-dentin complex histologically",
               "refute": "adult stem cells prove pulp-incompetent regardless of signals"},
},
# ------------------------------------------------------------------ rank 5
{
 "key": "dentin-hypersensitivity",
 "name": "Dentin Hypersensitivity Mechanism",
 "group": "Cariology",
 "ladder_rank": 5, "ladder_tier": "foundations",
 "problem": "Exposed dentin can scream at cold air - what exactly transmits the pain, and why do desensitizing treatments work only partially?",
 "description": "Dentin hypersensitivity - sharp pain from exposed dentin to cold, air, or sweets - affects a large fraction of adults with gum recession or enamel loss. The hydrodynamic theory (Brannstrom, 1960s) says fluid movement in dentinal tubules triggers nerve endings. Desensitizing toothpastes (potassium nitrate, stannous fluoride, arginine) help many but not all, and the pain's neural basis - including the recent discovery of odontoblasts as sensory cells - remains under revision.",
 "background": "Brannstrom's hydrodynamic theory dominated for half a century: tubule fluid shifts mechanically activate pulpal nerves. Treatments followed the theory: tubule-occluding agents (fluorides, oxalates, arginine-calcium) and nerve-depolarizing potassium salts. Then 2021 brought a shock: Tu et al. (Science Advances) showed odontoblasts themselves express mechanosensitive channels and signal to nerves - the tooth's builders are also its sensors. This reframes hypersensitivity as a sensory-cell disorder, not just plumbing. As of 2026 treatments still follow the old theory while the new biology awaits translation.",
 "why_it_matters": "Hypersensitivity is among the commonest dental complaints and drives avoidance of cold foods, air, even smiling in winter. A mechanism-true treatment would relieve millions with a toothpaste that actually works.",
 "sig_pointer": "The Signature system's proposed approach targets the odontoblast sensory apparatus directly, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that hypersensitivity is odontoblast hyperexcitability: the sensory cells' mechanotransduction is upregulated by inflammation and exposure, making normal stimuli painful. "
  "Assumptions: (1) odontoblasts are the primary transducers (Tu 2021); (2) their excitability is modifiable; (3) tubule occlusion helps indirectly by reducing the stimulus, not by fixing the sensor. "
  "Reasoning path: a sensor model explains why occluding treatments partially work (less stimulus) but never fully (hyperexcitable sensor) and predicts sensor-targeted agents will outperform. "
  "Proposed mechanism: 'sensor-calming' agents targeting odontoblast mechanotransduction channels, tested against stimulus-evoked pain beyond occlusion-based controls. "
  "What would confirm it: sensor-targeted agents outperforming occlusion in trials, with excitability markers mediating the effect. "
  "What would kill it: evidence that the hydrodynamic mechanism suffices and odontoblast signaling is epiphenomenal. "
  "What this does not claim: it does not claim a product exists, does not advise on toothpaste choice, and does not constitute dental advice."),
 "sig_lens": "The Signature lens reads the aching tooth as a hyperexcitable sensor, and asks what would calm the sensor rather than plug the plumbing.",
 "how_it_works": "Researchers study hypersensitivity through tubule-fluid dynamics, odontoblast electrophysiology, desensitizer trials, and pain-report outcomes.",
 "key_points": [
  "The hydrodynamic theory (Brannstrom) ruled for 50 years.",
  "Odontoblasts were found to be sensory cells in 2021 (Tu et al.).",
  "Potassium nitrate, stannous fluoride, and arginine help partially.",
  "Treatments still follow the old plumbing theory.",
  "The new sensory biology awaits therapeutic translation.",
 ],
 "requirements": [
  "Confirmation of the odontoblast's causal role in human hypersensitivity.",
  "Sensor-targeted agents proven against occlusion controls.",
  "Understanding of what upregulates odontoblast excitability.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Brannstrom M. The hydrodynamic theory of dentinal pain. Journal of Endodontics. 1986;12(10):453-457.",
  "Tu YH et al. Odontoblasts as sensory receptors. Science Advances. 2021;7:eabf5567.",
  "Orchardson R, Gillam DG. Managing dentin hypersensitivity. Journal of the American Dental Association. 2006;137(7):990-998.",
  "West NX et al. Dentin hypersensitivity: consensus guidelines. Journal of Dentistry. 2017;57:1-10.",
 ],
 "demo_data": {"a": ("adults with dentin hypersensitivity, percent (approx)", 30.0),
               "b": ("percent scale", 100.0), "bounds": (0.2, 0.45),
               "step1": "nearly a third of adults wince at cold - the commonest dental pain few discuss",
               "confirm": "sensor-targeted agents beat occlusion controls with excitability markers mediating",
               "refute": "the hydrodynamic mechanism proves sufficient with odontoblast signaling epiphenomenal"},
},
# ------------------------------------------------------------------ rank 6
{
 "key": "tmd-etiology",
 "name": "Temporomandibular Disorder Etiology",
 "group": "Orofacial Pain",
 "ladder_rank": 6, "ladder_tier": "foundations",
 "problem": "Jaw pain afflicts millions, mostly women - yet after a century of theories (bite, stress, joints), what actually causes TMD?",
 "description": "Temporomandibular disorders - jaw pain, limited opening, joint noises - affect roughly 5-12% of adults, predominantly women. Theories cycled: malocclusion (1940s-80s, now largely discarded as a primary cause), bruxism, stress, joint degeneration. The OPPERA study (2000s-2010s) reframed TMD as a complex pain condition with genetic, psychological, and central-sensitization components - more like fibromyalgia than a dental problem. Treatments remain empirical and often irreversible (occlusal adjustments, surgery) despite the weak etiology.",
 "background": "Costen's 1934 'bite' theory launched decades of occlusal therapy; by the 1990s evidence had largely exonerated occlusion as a primary cause. OPPERA (Orofacial Pain: Prospective Evaluation and Risk Assessment) identified risk factors: prior pain conditions, somatic awareness, stress, and genetic variants - positioning TMD within chronic overlapping pain conditions. Imaging shows joint changes correlate poorly with pain. As of 2026 the field treats a biopsychosocial pain disorder with tools built for a mechanical bite problem.",
 "why_it_matters": "TMD disables working-age women disproportionately, and irreversible dental treatments are still sold for it. An honest etiology would end harmful overtreatment and direct care to what actually helps.",
 "sig_pointer": "The Signature system's proposed approach treats TMD as a central pain condition with a jaw location, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that most TMD is not a jaw disorder but a pain-processing disorder manifesting in the jaw: the same central sensitization underlying fibromyalgia and chronic headache, with the trigeminal system as its expression site. "
  "Assumptions: (1) OPPERA's risk profile generalizes; (2) joint pathology is usually consequence or coincidence, not cause; (3) central mechanisms are modifiable. "
  "Reasoning path: a central-pain model explains the female predominance, the comorbidity web, the poor bite-pain correlation, and why centrally acting treatments help - unifying the scattered findings. "
  "Proposed mechanism: 'central-first' TMD care - phenotyping patients by central versus peripheral drivers, directing central cases to pain-rehabilitation approaches and reserving mechanical treatment for proven peripheral cases. "
  "What would confirm it: phenotyped care outperforming mechanical-first care in trials, with central markers predicting response. "
  "What would kill it: evidence that peripheral joint pathology drives most cases after all, or that phenotyping doesn't predict treatment response. "
  "What this does not claim: it does not claim any patient's pain is 'all in the head,' does not advise against dental care, and does not constitute dental or medical advice."),
 "sig_lens": "The Signature lens reads jaw pain as a pain-system disorder with a jaw address, and asks what phenotyping would route each patient correctly.",
 "how_it_works": "Researchers study TMD through OPPERA-style cohorts, quantitative sensory testing, genetic association, imaging-pain correlation studies, and treatment trials.",
 "key_points": [
  "TMD affects ~5-12% of adults, predominantly women.",
  "Occlusion was largely exonerated as a primary cause by the 1990s.",
  "OPPERA reframed TMD as a complex biopsychosocial pain condition.",
  "Joint imaging correlates poorly with pain.",
  "Irreversible occlusal treatments are still sold on weak etiology.",
 ],
 "requirements": [
  "Validated phenotyping separating central from peripheral drivers.",
  "Proof that phenotyped care beats mechanical-first care.",
  "An end to irreversible treatments for central-dominant cases.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Slade GD et al. Study methods and baseline findings: OPPERA. Journal of Pain. 2011;12(11 Suppl):T12-T26.",
  "Dworkin SF, LeResche L. Research diagnostic criteria for temporomandibular disorders. Journal of Craniomandibular Disorders. 1992;6(4):301-355.",
  "Greene CS. The etiology of temporomandibular disorders: implications for treatment. Journal of Orofacial Pain. 2001;15(2):93-105.",
  "National Academies. Temporomandibular Disorders: Priorities for Research and Care. Washington, DC: NAP; 2020.",
 ],
 "demo_data": {"a": ("adults with TMD, percent (upper range)", 12.0),
               "b": ("percent scale", 100.0), "bounds": (0.05, 0.15),
               "step1": "up to one in eight adults has jaw pain - mostly women, mostly unexplained",
               "confirm": "phenotyped central-first care beats mechanical-first care in trials",
               "refute": "peripheral joint pathology proves to drive most cases after all"},
},
# ------------------------------------------------------------------ rank 7
{
 "key": "dental-anxiety",
 "name": "Dental Anxiety Mechanisms",
 "group": "Behavioral Dentistry",
 "ladder_rank": 7, "ladder_tier": "foundations",
 "problem": "Millions avoid the dentist from fear, arriving only in agony - what creates dental anxiety, and what actually dissolves it?",
 "description": "Dental anxiety affects a large minority of adults; dental phobia - avoidance causing health harm - affects roughly 5%. The anxious avoid care, deteriorate, then need the invasive treatment they feared: the vicious cycle. Causes blend conditioning (bad experiences), vicarious learning, personality, and the specific triggers of dentistry (loss of control, invasion of the mouth, pain expectation). Sedation helps individuals; it doesn't fix the population problem.",
 "background": "Dental fear was measured from the 1960s (Corah's Dental Anxiety Scale, 1969); Berggren's vicious-cycle model (1984) described avoidance-driven deterioration. Research identified the key dimensions: fear of pain, loss of control, embarrassment, and distrust. Interventions tested: tell-show-do, cognitive-behavioral therapy (strong evidence), sedation (effective but avoidance-maintaining), and control-restoring techniques (stop signals). Yet dental education barely teaches anxiety management, and the anxious still meet rushed, control-stripping care. As of 2026 the effective treatments exist and the delivery doesn't.",
 "why_it_matters": "Dental anxiety is a public-health problem wearing a personal face: it converts preventable disease into emergency suffering, concentrated in the already-disadvantaged. Dissolving it would do more for oral health than a new filling material.",
 "sig_pointer": "The Signature system's proposed approach treats dental anxiety as a control problem, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that dental anxiety is fundamentally about control: the mouth is intimate, the patient is supine and invaded, and the anxiety tracks perceived control more than expected pain. "
  "Assumptions: (1) control perception dominates pain expectation in driving avoidance; (2) control can be genuinely restored by design, not just promised; (3) restored control generalizes beyond single visits. "
  "Reasoning path: a control model explains why stop-signals and tell-show-do outperform reassurance, and why sedation maintains avoidance (it bypasses control rather than restoring it). "
  "Proposed mechanism: 'control-restoring' dental design - guaranteed stop signals, paced procedures, patient-controlled pauses - tested against avoidance and attendance. "
  "What would confirm it: control-restoring protocols outperforming reassurance-based care on attendance and anxiety in trials. "
  "What would kill it: evidence that pain expectation dominates regardless of control, or that control restoration doesn't generalize. "
  "What this does not claim: it does not claim anxiety is currently treatable at scale, prescribes no therapy, and does not constitute dental or psychological advice."),
 "sig_lens": "The Signature lens reads dental fear as control lost in a vulnerable position, and asks what design would genuinely return it.",
 "how_it_works": "Behavioral researchers study dental anxiety through fear surveys, vicious-cycle cohorts, CBT trials, and control-manipulation experiments.",
 "key_points": [
  "Dental phobia affects ~5% of adults; anxiety a much larger minority.",
  "Berggren's vicious cycle: fear, avoidance, deterioration, feared treatment.",
  "Corah's scale (1969) made dental anxiety measurable.",
  "CBT has strong evidence; sedation works but maintains avoidance.",
  "Dental education barely teaches anxiety management.",
 ],
 "requirements": [
  "Proof that control-restoring design beats reassurance at scale.",
  "Delivery models that reach the avoidant, not just the attending.",
  "Training that makes anxiety management routine, not specialty.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Corah NL. Development of a dental anxiety scale. Journal of Dental Research. 1969;48(4):596.",
  "Berggren U, Meynert G. Dental fear and avoidance: causes, symptoms, and consequences. Journal of the American Dental Association. 1984;109(2):247-251.",
  "Wide Boman U et al. Cognitive behavioral therapy for dental anxiety. Various; 2010-2020.",
  "Armfield JM. What does dental anxiety mean? Various; 2008-2013.",
 ],
 "demo_data": {"a": ("adults with dental phobia, percent (approx)", 5.0),
               "b": ("percent scale", 100.0), "bounds": (0.03, 0.08),
               "step1": "one in twenty adults is phobic - avoiding care until agony forces the feared visit",
               "confirm": "control-restoring protocols beat reassurance-based care on attendance",
               "refute": "pain expectation proves to dominate regardless of control restoration"},
},
# ------------------------------------------------------------------ rank 8
{
 "key": "early-childhood-caries",
 "name": "Early Childhood Caries Prevention",
 "group": "Pediatric Dentistry",
 "ladder_rank": 8, "ladder_tier": "foundations",
 "problem": "Toddlers still get rampant decay despite everything known about prevention - why does early childhood caries resist public-health efforts?",
 "description": "Early childhood caries (ECC) - decay in children under six - affects nearly half of young children globally, concentrated in poverty. It causes pain, infection, missed school, and treatment under general anesthesia. Prevention is 'known': fluoride, diet control, brushing. Yet ECC persists because the known prevention doesn't reach the families who need it: the problem is delivery and behavior, not biology.",
 "background": "ECC was recognized as baby-bottle tooth decay in the 1970s; the name changed as the understanding broadened beyond bottles. Fluoride varnish programs, motivational interviewing with mothers, and silver diamine fluoride (which arrests decay without drilling) all show efficacy in trials. But population ECC barely moves: sugary-drink environments, health-literacy gaps, dental deserts, and the difficulty of changing family behavior defeat programmatic prevention. As of 2026 the effective tools exist and the delivery science lags.",
 "why_it_matters": "ECC is the commonest chronic disease of childhood and a marker of inequality: poor children suffer, undergo general anesthesia for extractions, and carry the disadvantage into school. Solving delivery would protect the most vulnerable mouths.",
 "sig_pointer": "The Signature system's proposed approach treats ECC as a delivery problem with a family-behavior core, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that ECC prevention fails on the last mile: the interventions work, but they require sustained family behavior change that programs don't engineer - they inform rather than reshape. "
  "Assumptions: (1) efficacy is proven for varnish, SDF, and diet counseling; (2) the gap is sustained behavior, not knowledge; (3) behavior change is engineerable with the right design. "
  "Reasoning path: a last-mile model explains the trial-population gap and predicts that behavior-engineered delivery will outperform information-based programs. "
  "Proposed mechanism: 'behavior-engineered' ECC prevention - habit-formation design, default-structured choices, community delivery - tested against caries increment in high-risk populations. "
  "What would confirm it: engineered delivery outperforming standard programs on ECC rates in trials. "
  "What would kill it: evidence that structural factors (sugar environments, poverty) dominate regardless of delivery design. "
  "What this does not claim: it does not claim a program ready for deployment, does not blame families, and does not constitute dental advice."),
 "sig_lens": "The Signature lens reads the decayed toddler tooth as a delivery failure, and asks what last-mile design would carry prevention home.",
 "how_it_works": "Pediatric researchers study ECC through varnish and SDF trials, motivational-interviewing studies, sugar-environment research, and implementation trials in high-risk communities.",
 "key_points": [
  "ECC affects nearly half of young children globally.",
  "Fluoride varnish, SDF, and diet counseling are proven effective.",
  "Population ECC barely moves despite proven tools.",
  "The gap is delivery and sustained family behavior, not biology.",
  "ECC concentrates in poverty - an inequality marker.",
 ],
 "requirements": [
  "Delivery designs proven in high-risk populations, not just trials.",
  "Behavior-engineering that sustains change beyond program contact.",
  "Structural action on sugar environments alongside behavior.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "American Academy of Pediatric Dentistry. Policy on early childhood caries. Various.",
  "Weintraub JA et al. Fluoride varnish efficacy. Various; 2006-2018.",
  "Crystal YO, Niederman R. Silver diamine fluoride treatment. Various; 2016-2019.",
  "Tinanoff N et al. Early childhood caries epidemiology. Various; 2019.",
 ],
 "demo_data": {"a": ("young children with ECC worldwide, percent (approx)", 48.0),
               "b": ("percent scale", 100.0), "bounds": (0.35, 0.6),
               "step1": "nearly half of young children carry decay - the commonest chronic disease of childhood",
               "confirm": "behavior-engineered delivery beats standard programs on ECC rates",
               "refute": "structural factors prove to dominate regardless of delivery design"},
},
# ------------------------------------------------------------------ rank 9
{
 "key": "oral-biofilm",
 "name": "Oral Biofilm Control",
 "group": "Oral Microbiology",
 "ladder_rank": 9, "ladder_tier": "foundations",
 "problem": "Dental plaque is a biofilm that brushing barely dents - why is the oral biofilm so resilient, and what would control it without antibiotics?",
 "description": "Dental plaque is among the best-studied biofilms in nature: hundreds of species in structured communities, resistant to antimicrobials, reforming within hours of removal. Mechanical disruption (brushing, flossing) remains the mainstay because chemical control keeps failing: chlorhexidine stains and alters taste, essential oils help modestly, and antibiotics are inappropriate for daily use. The biofilm's resilience is ecological, not just chemical.",
 "background": "Plaque as organized biofilm was established by Listgarten and others in the 1970s-90s; the Human Microbiome Project-era sequencing revealed its diversity (700+ species). Anti-plaque chemistry cycled: chlorhexidine (the gold standard with side effects), triclosan (withdrawn over concerns), essential oils (modest). The ecological insight - that health is a balanced community, not sterility - reframed the goal from killing to managing. Probiotics, prebiotics, and quorum-sensing inhibitors are investigational. As of 2026 no chemical controls plaque like a toothbrush, and nothing maintains health without mechanical disruption.",
 "why_it_matters": "Plaque drives caries and periodontitis - the two great dental diseases. A true biofilm-management strategy would prevent both at the ecological root instead of drilling and scaling their consequences.",
 "sig_pointer": "The Signature system's proposed approach manages the biofilm as an ecology to be gardened, not an enemy to be killed, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that plaque control should be ecological gardening: the goal is a stable health-associated community, maintained by selective pressures rather than broad killing. "
  "Assumptions: (1) health-associated communities are stable attractors; (2) selective pressures (pH, nutrients, adhesion) can favor them; (3) broad antimicrobials destabilize toward dysbiosis. "
  "Reasoning path: an ecology model explains why chlorhexidine helps short-term but can't be used long-term, and predicts selective ecological pressures will outperform biocides. "
  "Proposed mechanism: 'ecological plaque management' - prebiotic substrates, pH modulation, and targeted anti-adhesion - tested against community profiles and disease endpoints. "
  "What would confirm it: ecological strategies maintaining health-associated communities and reducing disease beyond mechanical control alone. "
  "What would kill it: evidence that mechanical disruption is irreplaceable, or that ecological pressures can't shift established communities. "
  "What this does not claim: it does not claim a product exists, does not advise against brushing, and does not constitute dental advice."),
 "sig_lens": "The Signature lens reads plaque as a garden to be tended, and asks what selective pressures would keep the weeds from taking over.",
 "how_it_works": "Oral microbiologists study biofilms through sequencing, in vitro biofilm models, anti-plaque trials, and ecological intervention studies.",
 "key_points": [
  "Plaque contains 700+ species in structured biofilm communities.",
  "Biofilms resist antimicrobials and reform within hours.",
  "Chlorhexidine works but stains and alters taste; triclosan was withdrawn.",
  "Health is a balanced community, not sterility - the ecological insight.",
  "Nothing controls plaque like mechanical disruption.",
 ],
 "requirements": [
  "Selective ecological pressures proven to maintain health-associated communities.",
  "Disease-endpoint proof beyond plaque scores.",
  "Strategies compatible with daily life, not just trials.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Marsh PD. Dental plaque as a biofilm and a microbial community. Caries Research. 2004;38:264-269.",
  "Kolenbrander PE et al. Oral multispecies biofilm development. Various; 2002-2010.",
  "Teles RP, Teles FRF. Antimicrobial agents and plaque control. Various; 2009-2015.",
  "Human Microbiome Project Consortium. Structure, function and diversity of the healthy human microbiome. Nature. 2012;486:207-214.",
 ],
 "demo_data": {"a": ("oral bacterial species (approx)", 700.0),
               "b": ("species targeted by broad antimicrobials (all of them)", 700.0), "bounds": (0.9, 1.1),
               "step1": "seven hundred species share the mouth - broad killing cannot distinguish friend from foe",
               "confirm": "ecological strategies maintain health communities and cut disease beyond brushing alone",
               "refute": "mechanical disruption proves irreplaceable with ecology unshiftable"},
},
# ------------------------------------------------------------------ rank 10
{
 "key": "tooth-wear",
 "name": "Tooth Wear: Erosion, Attrition, Abrasion",
 "group": "Cariology",
 "ladder_rank": 10, "ladder_tier": "foundations",
 "problem": "Teeth are dissolving in acid and grinding away - why is tooth wear accelerating, and can lost enamel ever be rebuilt?",
 "description": "Tooth wear - erosion (acid), attrition (tooth-to-tooth), abrasion (foreign body) - is rising, driven by acidic drinks, reflux, eating disorders, and bruxism. Enamel doesn't regenerate: once lost, it's gone, and dentistry can only patch with composites or crowns. Prevention (diet counseling, fluoride, splints) is behavioral and weak; the wear continues silently until teeth are stumps.",
 "background": "Erosion was characterized as soft-drink consumption rose in the late 20th century; the BEWE index (2008) standardized scoring. Reflux-related erosion linked dentistry to gastroenterology; eating-disorder erosion to psychiatry. Attrition from bruxism affects a large fraction of adults, with splints protecting but not stopping the habit. Remineralization science (fluoride, CPP-ACP, hydroxyapatite) rebuilds early lesions but not lost bulk. As of 2026 no therapy regrows enamel, and wear management is damage control.",
 "why_it_matters": "Severe wear destroys the dentition of young adults - from energy drinks, reflux, or grinding - condemning them to a lifetime of crowns. Stopping wear early would save teeth that currently have no future but prosthetics.",
 "sig_pointer": "The Signature system's proposed approach treats wear as a chemistry problem with a remineralization ceiling, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that wear management fails by treating three diseases as one: erosion is chemistry, attrition is mechanics, abrasion is behavior - and each needs its own prevention while sharing only the endpoint. "
  "Assumptions: (1) the wear types have distinct mechanisms; (2) patients usually have a dominant type; (3) type-specific prevention outperforms generic advice. "
  "Reasoning path: a type-separation model explains why generic 'wear counseling' underperforms and predicts phenotyped prevention will work better. "
  "Proposed mechanism: 'wear phenotyping' - diagnosing the dominant wear mechanism per patient and applying type-specific prevention (acid control, bruxism management, abrasion elimination), tested against wear progression. "
  "What would confirm it: phenotyped prevention slowing wear beyond generic counseling in trials. "
  "What would kill it: evidence that wear types are inseparable in practice, or that prevention can't outpace modern acid exposure. "
  "What this does not claim: it does not claim enamel can be regrown, does not advise on diet or splints, and does not constitute dental advice."),
 "sig_lens": "The Signature lens reads the worn tooth as three diseases sharing an endpoint, and asks what phenotyping would separate them.",
 "how_it_works": "Researchers study wear through BEWE scoring cohorts, acid-exposure studies, bruxism trials, and remineralization science.",
 "key_points": [
  "Tooth wear is rising with acidic drinks, reflux, and bruxism.",
  "Enamel does not regenerate; lost bulk is irrecoverable.",
  "The BEWE index (2008) standardized wear scoring.",
  "Remineralization rebuilds early lesions, not lost enamel.",
  "Management is damage control: composites, then crowns.",
 ],
 "requirements": [
  "Validated wear phenotyping separating erosion, attrition, abrasion.",
  "Type-specific prevention proven against progression.",
  "Enamel-regeneration science beyond remineralization.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Bartlett D et al. Basic Erosive Wear Examination (BEWE). Clinical Oral Investigations. 2008;12(Suppl 1):S65-S68.",
  "Lussi A et al. Dental erosion. Various; 2006-2014.",
  "Shellis RP et al. Dental erosion: chemistry and biology. Various; 2011.",
  "Johansson AK et al. Dental erosion and reflux. Various; 2004-2012.",
 ],
 "demo_data": {"a": ("adults with measurable tooth wear, percent (approx)", 30.0),
               "b": ("percent scale", 100.0), "bounds": (0.2, 0.45),
               "step1": "nearly a third of adults show measurable wear - enamel's one-way loss is accelerating",
               "confirm": "phenotyped prevention beats generic counseling on wear progression",
               "refute": "wear types prove inseparable with prevention unable to outpace acid exposure"},
},
# ------------------------------------------------------------------ rank 11
{
 "key": "halitosis",
 "name": "Halitosis Origins",
 "group": "Oral Medicine",
 "ladder_rank": 11, "ladder_tier": "foundations",
 "problem": "Bad breath is mostly oral, sometimes systemic - but why do some cases resist every mouthwash, and what is the true source map?",
 "description": "Halitosis affects a large fraction of adults socially and a minority pathologically. About 90% of cases originate in the mouth - tongue coating, periodontal disease, tonsil stones - via volatile sulfur compounds from bacterial putrefaction. But the refractory cases hide elsewhere: nasal, reflux, metabolic (diabetic ketoacidosis, liver failure), and the rare but real halitophobia where no odor exists. Diagnosis remains nose-based and subjective.",
 "background": "Volatile sulfur compound measurement (Halimeter, 1990s; gas chromatography) objectified halitosis. Tonzetich's work mapped tongue-coating microbiology. The systemic causes - extra-oral halitosis - were catalogued but remain diagnosis-by-exclusion. Halitophobia (delusional halitosis) was characterized as a distinct entity needing psychological rather than dental care. As of 2026 diagnosis is still largely organoleptic (a trained nose), and refractory cases cycle through mouthwashes without source identification.",
 "why_it_matters": "Halitosis destroys confidence, relationships, and careers; the refractory sufferer spends fortunes on products that can't work because the source is elsewhere. A true source map would end the guessing.",
 "sig_pointer": "The Signature system's proposed approach maps halitosis by source with instrumented diagnosis, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that halitosis care fails on source attribution: treatments assume oral origin, so extra-oral and psychogenic cases are mistreated indefinitely. "
  "Assumptions: (1) sources are classifiable by volatile profiles; (2) instrumented breath analysis can separate them; (3) source-matched treatment resolves refractory cases. "
  "Reasoning path: a source-attribution model explains refractory cases and predicts that profiled diagnosis will outperform nose-based trial-and-error. "
  "Proposed mechanism: 'source-mapped' halitosis care - breath volatile profiling directing treatment to oral, nasal, systemic, or psychogenic pathways. "
  "What would confirm it: profiled diagnosis resolving refractory cases beyond standard care in trials. "
  "What would kill it: evidence that volatile profiles don't separate sources reliably, or that refractory cases are all psychogenic. "
  "What this does not claim: it does not claim a diagnostic device exists, does not advise on products, and does not constitute dental or medical advice."),
 "sig_lens": "The Signature lens reads bad breath as a source-attribution problem, and asks what breath profile would point to the true origin.",
 "how_it_works": "Researchers study halitosis through volatile sulfur measurement, tongue-coating microbiology, systemic-cause case series, and halitophobia psychology.",
 "key_points": [
  "~90% of halitosis originates in the mouth, mostly the tongue.",
  "Volatile sulfur compounds from bacterial putrefaction are the main culprits.",
  "Diagnosis remains largely organoleptic - a trained nose.",
  "Refractory cases hide in nasal, systemic, or psychogenic sources.",
  "Halitophobia needs psychological, not dental, care.",
 ],
 "requirements": [
  "Instrumented breath profiling validated against sources.",
  "Source-matched treatment protocols.",
  "Recognition and proper referral of halitophobia.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Tonzetich J. Production and origin of oral malodor. Journal of Periodontology. 1977;48(1):13-20.",
  "Rosenberg M. Clinical assessment of bad breath. Journal of Dental Research. 1996;75(5):1270-1275.",
  "Tangerman A, Winkel EG. Extra-oral halitosis. Various; 2007-2013.",
  "Yaegaki K, Coil JM. Examination, classification, and treatment of halitosis. Journal of the Canadian Dental Association. 2000;66(5):257-261.",
 ],
 "demo_data": {"a": ("halitosis cases of oral origin, percent (approx)", 90.0),
               "b": ("percent scale", 100.0), "bounds": (0.8, 0.95),
               "step1": "nine in ten cases start in the mouth - but the refractory tenth is mistreated as oral",
               "confirm": "profiled diagnosis resolves refractory cases beyond standard care",
               "refute": "volatile profiles prove unable to separate sources reliably"},
},
# ------------------------------------------------------------------ rank 12
{
 "key": "perio-regeneration",
 "name": "True Periodontal Regeneration",
 "group": "Periodontology",
 "ladder_rank": 12, "ladder_tier": "compounded",
 "problem": "Periodontal therapy stops destruction but rarely rebuilds - why does the periodontium heal with repair instead of regeneration, and what would regrow it?",
 "description": "Periodontitis destroys the attachment apparatus: cementum, periodontal ligament, alveolar bone. Conventional therapy (scaling, surgery) arrests disease but heals with a long junctional epithelium - repair, not regeneration. True regeneration - new cementum, functionally oriented ligament, new bone - is achieved only in narrow defects with guided tissue regeneration or enamel matrix proteins, unpredictably. The biology of why the periodontium won't regenerate remains the field's central question.",
 "background": "Melcher's 1976 compartment concept framed the problem: which cells repopulate the root determines the outcome - epithelium gives repair, ligament cells give regeneration. Guided tissue regeneration (Nyman, Lindhe, 1980s) used barrier membranes to exclude epithelium; enamel matrix derivative (Emdogain, Hammarstrom 1997) added signaling. Growth factors (PDGF, BMPs) showed promise but modest clinical gains. The frontier is cell-based: periodontal ligament stem cells (Seo 2004) can regenerate in animals. As of 2026 predictable regeneration of the full attachment apparatus remains elusive.",
 "why_it_matters": "Periodontitis is the leading cause of adult tooth loss: regeneration would save teeth now condemned to extraction or heroic maintenance. It is also the model for regenerating any complex tissue interface.",
 "sig_pointer": "The Signature system's proposed approach treats regeneration as a cell-competition problem to be rigged, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that periodontal healing is a race between cell populations for the root surface - and epithelium always wins because it's fastest, not because it's destined. "
  "Assumptions: (1) the repopulating cell type determines repair versus regeneration (Melcher); (2) the race is winnable by slowing epithelium and accelerating ligament cells; (3) signaling can bias the outcome beyond barriers. "
  "Reasoning path: a race model explains why barriers help partially (they slow epithelium) and predicts that combined slow-epithelium plus recruit-ligament strategies will outperform. "
  "Proposed mechanism: 'race-rigged' regeneration - barriers plus ligament-cell recruitment signals plus growth-factor guidance - tested histologically for true attachment apparatus. "
  "What would confirm it: combined strategies yielding predictable true regeneration beyond GTR/EMD in trials. "
  "What would kill it: evidence that adult ligament cells lack regenerative capacity regardless of recruitment, or that epithelium can't be sufficiently delayed. "
  "What this does not claim: it does not claim regeneration is achievable today, does not advise on therapy, and does not constitute dental advice."),
 "sig_lens": "The Signature lens reads the healing root as a race the wrong cells keep winning, and asks what would rig it for the ligament.",
 "how_it_works": "Periodontal researchers study regeneration through GTR/EMD trials, growth-factor studies, ligament stem-cell biology, and histological outcome measures.",
 "key_points": [
  "Melcher (1976): the repopulating cell type determines repair versus regeneration.",
  "GTR barriers (1980s) and Emdogain (1997) achieve regeneration narrowly and unpredictably.",
  "Conventional therapy heals with long junctional epithelium - repair.",
  "Periodontal ligament stem cells (Seo 2004) regenerate in animals.",
  "Predictable full attachment regeneration remains elusive.",
 ],
 "requirements": [
  "Strategies that reliably recruit ligament cells while excluding epithelium.",
  "Histological proof of new cementum, oriented ligament, and bone.",
  "Regeneration predictable across defect types, not just narrow ones.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Melcher AH. On the repair potential of periodontal tissues. Journal of Periodontology. 1976;47(5):256-260.",
  "Nyman S et al. New attachment following surgical treatment of human periodontal disease by guiding tissue regeneration. Journal of Periodontology. 1982;53(7):450-454.",
  "Hammarstrom L et al. Enamel matrix derivative (Emdogain). Various; 1997.",
  "Seo BM et al. Investigation of multipotent postnatal stem cells from human periodontal ligament. Lancet. 2004;364:149-155.",
 ],
 "demo_data": {"a": ("periodontitis as cause of adult tooth loss, percent (approx leading share)", 40.0),
               "b": ("percent scale", 100.0), "bounds": (0.3, 0.55),
               "step1": "gum disease leads adult tooth loss - yet therapy repairs where it should regenerate",
               "confirm": "combined race-rigged strategies beat GTR/EMD on true regeneration histologically",
               "refute": "adult ligament cells prove regeneratively incompetent regardless of recruitment"},
},
# ------------------------------------------------------------------ rank 13
{
 "key": "peri-implantitis",
 "name": "Peri-implantitis Treatment",
 "group": "Implantology",
 "ladder_rank": 13, "ladder_tier": "compounded",
 "problem": "Dental implants succeed brilliantly - until the bone around them melts away. Why does peri-implantitis resist treatment that works for gum disease?",
 "description": "Peri-implantitis - inflammatory bone loss around an osseointegrated implant - affects a significant minority of implants (estimates range 10-20% at patient level over time). Unlike periodontitis, it progresses faster, responds poorly to non-surgical therapy, and surgical treatment is unpredictable: decontaminating a threaded titanium surface without damaging it has no solved method, and re-osseointegration is unreliable.",
 "background": "Implant success was established by Branemark's osseointegration work (1960s-80s); peri-implantitis emerged as the late complication as implants aged in populations. Albrektsson and others characterized its rapid, nonlinear progression. Treatment trials cycled: non-surgical debridement (largely ineffective for established disease), surgical access with surface decontamination (lasers, air abrasion, chemical agents - none proven superior), and implantoplasty (smoothing threads, sacrificing design). The 2017 World Workshop classification formalized diagnosis. As of 2026 no treatment predictably arrests peri-implantitis or regrows lost bone.",
 "why_it_matters": "Millions of implants are aging into the risk window: a disease that was rare when implants were new is becoming common. Solving treatment would protect the largest investment most dental patients ever make.",
 "sig_pointer": "The Signature system's proposed approach treats the implant surface as the therapeutic target, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that peri-implantitis treatment fails on the surface problem: therapy cleans soft tissue while the disease lives on and in the threaded titanium, which no current method decontaminates without damage. "
  "Assumptions: (1) the implant surface is the disease reservoir; (2) current decontamination is either ineffective or destructive; (3) re-osseointegration requires a pristine surface. "
  "Reasoning path: a surface-reservoir model explains why soft-tissue therapy underperforms and why results vary with surface type - the target was never the tissue. "
  "Proposed mechanism: 'surface-restoring' therapy that decontaminates without altering topography (validated by surface analysis), followed by regenerative protocols, tested against disease arrest and re-osseointegration. "
  "What would confirm it: surface-restoring protocols arresting disease and regrowing bone beyond current surgical outcomes in trials. "
  "What would kill it: evidence that the disease is driven by host susceptibility regardless of surface state, or that pristine surfaces can't be achieved in situ. "
  "What this does not claim: it does not claim a treatment exists today, does not advise on implant care, and does not constitute dental advice."),
 "sig_lens": "The Signature lens reads the failing implant as a contaminated surface wearing a tissue disguise, and asks what would restore the surface in place.",
 "how_it_works": "Implant researchers study peri-implantitis through decontamination trials, surface-analysis studies, surgical treatment cohorts, and risk-factor research.",
 "key_points": [
  "Peri-implantitis affects ~10-20% of implant patients over time.",
  "It progresses faster and less predictably than periodontitis.",
  "Non-surgical therapy is largely ineffective for established disease.",
  "No decontamination method is proven superior; re-osseointegration is unreliable.",
  "The 2017 World Workshop formalized classification.",
 ],
 "requirements": [
  "In-situ surface decontamination that is effective and non-destructive.",
  "Proof of re-osseointegration after treatment.",
  "Prevention strategies for high-risk patients.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Albrektsson T et al. Peri-implantitis: a complication of a foreign body or a man-made disease. Various; 2016-2019.",
  "Berglundh T et al. Peri-implant diseases and conditions: consensus report of workgroup 4 of the 2017 World Workshop. Journal of Clinical Periodontology. 2018;45(Suppl 20):S286-S291.",
  "Mombelli A et al. Treatment of peri-implantitis. Various; 2002-2018.",
  "Heitz-Mayfield LJA, Mombelli A. The therapy of peri-implantitis. Periodontology 2000. 2014;65(1):167-182.",
 ],
 "demo_data": {"a": ("implant patients developing peri-implantitis, percent (approx)", 15.0),
               "b": ("percent scale", 100.0), "bounds": (0.1, 0.25),
               "step1": "up to one in five implant patients faces bone loss around the implant - the late complication arriving",
               "confirm": "surface-restoring protocols beat current surgery on arrest and re-osseointegration",
               "refute": "the disease proves host-driven regardless of surface state"},
},
# ------------------------------------------------------------------ rank 14
{
 "key": "osseointegration-failure",
 "name": "Osseointegration Failure Mechanisms",
 "group": "Implantology",
 "ladder_rank": 14, "ladder_tier": "compounded",
 "problem": "Most implants fuse with bone - but some never integrate or lose integration years later. What decides whether titanium becomes bone-anchored?",
 "description": "Osseointegration - direct bone-to-implant contact without fibrous interposition (Branemark's definition) - succeeds in the high 90s percent at five years. Early failures (no integration) trace to surgical trauma, infection, or loading; late failures trace to overload, peri-implantitis, or systemic factors. But the biology of the bone-implant interface - why some interfaces are robust and others fragile - remains incompletely mapped, and no test predicts failure before it happens.",
 "background": "Branemark's 1960s rabbit-chamber observations launched implantology; the 1982 Toronto conference brought it to North America. Success criteria (Albrektsson 1986) standardized reporting. Research mapped the healing sequence - clot, woven bone, remodeling - and the roles of surface topography (SLA surfaces), loading protocols, and systemic factors (smoking, diabetes, bisphosphonates, radiation). Immediate loading challenged the old unloaded-healing dogma successfully. As of 2026 the interface biology is described but not predictive: failures still surprise.",
 "why_it_matters": "Implant failure wastes the costliest dental procedure and destroys the bone needed for the next attempt. Predicting the failing interface would let clinicians intervene before the implant is lost.",
 "sig_pointer": "The Signature system's proposed approach treats the interface as a bone-remodeling equilibrium to be monitored, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that the bone-implant interface is a lifelong remodeling equilibrium, not a one-time fusion: late failures are equilibrium shifts, and early failures are equilibria never established. "
  "Assumptions: (1) interface stability requires continuous remodeling balance; (2) the balance has measurable markers; (3) shifts precede clinical failure by months. "
  "Reasoning path: an equilibrium model explains both early and late failures in one framework and predicts that interface monitoring will forecast failure. "
  "Proposed mechanism: 'interface monitoring' - resonance frequency, biomarker, or imaging markers tracking remodeling balance - triggering intervention when equilibrium degrades. "
  "What would confirm it: monitored interfaces showing predictive degradation before failure in cohorts, with interventions rescuing flagged implants. "
  "What would kill it: evidence that failures are sudden events without prodromal equilibrium shifts. "
  "What this does not claim: it does not claim a monitor exists today, does not advise on loading, and does not constitute dental advice."),
 "sig_lens": "The Signature lens reads the fused implant as a balance being continuously renegotiated, and asks what would reveal the negotiation failing.",
 "how_it_works": "Implant researchers study integration through histology, resonance-frequency analysis, loading-protocol trials, and failure-cohort analyses.",
 "key_points": [
  "Osseointegration succeeds in the high-90s percent at five years.",
  "Branemark's rabbit chambers (1960s) launched the field.",
  "Early failures trace to trauma, infection, loading; late to overload and disease.",
  "Surface topography (SLA) and loading protocols were the big advances.",
  "No test predicts failure before it happens.",
 ],
 "requirements": [
  "Measurable markers of interface remodeling equilibrium.",
  "Proof that monitoring forecasts failure in time to intervene.",
  "Rescue protocols for degrading interfaces.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Branemark PI et al. Osseointegrated implants in the treatment of the edentulous jaw. Scandinavian Journal of Plastic and Reconstructive Surgery. 1977;11(Suppl 16).",
  "Albrektsson T et al. The long-term efficacy of currently used dental implants. Australian Dental Journal. 2008;53(Suppl 1):S31-S41.",
  "Esposito M et al. Interventions for replacing missing teeth. Cochrane Database of Systematic Reviews. Various.",
  "Sennerby L, Meredith N. Implant stability measurements. Periodontology 2000. 2008;47:51-66.",
 ],
 "demo_data": {"a": ("implant five-year success, percent (approx)", 97.0),
               "b": ("percent scale", 100.0), "bounds": (0.9, 0.99),
               "step1": "implants succeed in the high nineties - making each failure a surprise worth predicting",
               "confirm": "interface monitoring forecasts failure with rescue of flagged implants",
               "refute": "failures prove sudden events without prodromal equilibrium shifts"},
},
# ------------------------------------------------------------------ rank 15
{
 "key": "orthodontic-biology",
 "name": "Orthodontic Tooth Movement Biology",
 "group": "Orthodontics",
 "ladder_rank": 15, "ladder_tier": "compounded",
 "problem": "Braces move teeth through bone over years - what is the actual biology, and why can't it be safely accelerated?",
 "description": "Orthodontic tooth movement works by sustained force: pressure-side bone resorbs, tension-side bone forms, and the tooth migrates through the alveolus. Treatment takes 18-36 months. Acceleration attempts - surgical (corticotomy, piezocision), vibratory devices, low-level laser, pharmacologic (prostaglandins, vitamin D) - show modest or unproven effects, and the biology of the rate limit is incompletely mapped.",
 "background": "The pressure-tension theory (Sandstedt 1904, Oppenheim 1911) framed the biology; the cellular mediators - RANKL/OPG, prostaglandins, cytokines - were mapped in the late 20th century. Frost's regional acceleratory phenomenon (RAP) explained why surgical injury speeds movement: injury triggers transient osteopenia. Acceleration trials proliferated in the 2010s with mixed results; vibration devices (AcceleDent) failed to show convincing benefit in independent trials. As of 2026 the rate limit is understood descriptively but not manipulably: no safe acceleration is proven.",
 "why_it_matters": "Years in braces mean years of decay risk, root resorption risk, and patient burden - especially for adults. Safe acceleration would transform orthodontics' cost-benefit for millions.",
 "sig_pointer": "The Signature system's proposed approach treats the rate limit as a bone-remodeling throttle, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that tooth-movement speed is throttled by the bone-remodeling cycle time, not by force magnitude: more force doesn't speed the cycle, it just risks damage. "
  "Assumptions: (1) the remodeling cycle has a minimum duration; (2) the cycle is locally acceleratable (RAP proves it); (3) acceleration must preserve the cycle's coordination. "
  "Reasoning path: a cycle-time model explains why force increases fail and why injury accelerates - injury restarts the cycle faster - and predicts that cycle-targeted (not force-targeted) interventions will work. "
  "Proposed mechanism: 'cycle-tuned' acceleration - interventions that shorten the remodeling cycle while preserving pressure-tension coordination, tested against movement rate and root safety. "
  "What would confirm it: cycle-targeted acceleration moving teeth faster without resorption in trials. "
  "What would kill it: evidence that the cycle time is biologically fixed, or that acceleration always trades against root integrity. "
  "What this does not claim: it does not claim acceleration is safe today, does not advise on devices, and does not constitute dental advice."),
 "sig_lens": "The Signature lens reads the slow tooth as throttled by a remodeling cycle, and asks what would shorten the cycle without breaking coordination.",
 "how_it_works": "Orthodontic researchers study movement through animal models, biomarker studies of crevicular fluid, acceleration trials, and root-resorption imaging.",
 "key_points": [
  "Tooth movement: pressure-side resorption, tension-side formation.",
  "Treatment takes 18-36 months typically.",
  "The RAP explains why surgical injury accelerates movement.",
  "Vibration devices failed independent validation.",
  "No safe acceleration is proven.",
 ],
 "requirements": [
  "Cycle-targeted acceleration preserving coordination.",
  "Proof of speed without root resorption cost.",
  "Understanding of the cycle's minimum duration.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Krishnan V, Davidovitch Z. Cellular, molecular, and tissue-level reactions to orthodontic force. American Journal of Orthodontics and Dentofacial Orthopedics. 2006;129(4):469.e1-469.e32.",
  "Frost HM. The regional acceleratory phenomenon. Henry Ford Hospital Medical Journal. 1983;31(1):3-9.",
  "Long H et al. Interventions for accelerating orthodontic tooth movement. Cochrane Database of Systematic Reviews. 2013;8:CD010988.",
  "Meikle MC. The tissue, cellular, and molecular regulation of orthodontic tooth movement. European Journal of Orthodontics. 2006;28(3):221-240.",
 ],
 "demo_data": {"a": ("typical orthodontic treatment, months (midpoint)", 27.0),
               "b": ("months per year", 12.0), "bounds": (1.5, 3.0),
               "step1": "braces take over two years on average - the remodeling cycle sets a slow speed limit",
               "confirm": "cycle-targeted acceleration moves teeth faster without resorption",
               "refute": "the remodeling cycle proves biologically fixed in duration"},
},
# ------------------------------------------------------------------ rank 16
{
 "key": "root-resorption",
 "name": "Root Resorption During Orthodontics",
 "group": "Orthodontics",
 "ladder_rank": 16, "ladder_tier": "compounded",
 "problem": "Orthodontic force can eat the tooth's own roots - why do some patients lose root length while others don't, and who is at risk?",
 "description": "External apical root resorption - shortening of tooth roots during orthodontic treatment - affects most patients mildly and a minority severely (over 4mm or a third of root length). Severe resorption threatens tooth longevity. Risk factors are partially known (treatment duration, force magnitude, root shape, genetics) but prediction is poor: the same mechanics resorb one patient's roots and spare another's.",
 "background": "Resorption was recognized with radiography's arrival; Brezniak and Wasserstein's reviews mapped the risk factors. Genetic studies implicated IL-1 polymorphisms (Al-Qawasmi 2003) with modest effect sizes. The biology - odontoclast activation at the apex under sustained force - parallels bone resorption but with cementum as the victim. Force magnitude matters but the dose-response is individual. As of 2026 no pre-treatment test identifies the high-risk patient, and monitoring is reactive: resorption found on mid-treatment radiographs, after the damage.",
 "why_it_matters": "Severe resorption shortens the useful life of the very teeth orthodontics aimed to save - a treatment harming its objective. Predicting susceptibility would let orthodontists modify force or decline risky movements.",
 "sig_pointer": "The Signature system's proposed approach treats resorption susceptibility as a measurable individual trait, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that resorption susceptibility is an individual odontoclast-activation threshold: the same force exceeds it in some patients and not others, and the threshold is measurable before treatment. "
  "Assumptions: (1) susceptibility is a stable individual trait; (2) it reflects odontoclast regulation, partly genetic; (3) early treatment response reveals the threshold. "
  "Reasoning path: a threshold model explains the individual variation and predicts that early-response monitoring plus genetic markers will identify high-risk patients. "
  "Proposed mechanism: 'susceptibility screening' - genetic plus early-biomarker profiling before/during initial alignment - guiding force modification for high-risk patients. "
  "What would confirm it: screened high-risk patients showing less resorption with modified mechanics in trials. "
  "What would kill it: evidence that susceptibility is stochastic rather than trait-like, or that force modification can't prevent it. "
  "What this does not claim: it does not claim a screening test exists today, does not advise on mechanics, and does not constitute dental advice."),
 "sig_lens": "The Signature lens reads the shortening root as a personal threshold crossed, and asks what would measure the threshold before treatment.",
 "how_it_works": "Orthodontic researchers study resorption through radiographic cohorts, genetic association studies, crevicular-fluid biomarker research, and force-magnitude trials.",
 "key_points": [
  "Most orthodontic patients show mild resorption; a minority severe.",
  "Severe resorption threatens the longevity of treated teeth.",
  "IL-1 polymorphisms associate with risk but predict weakly.",
  "Force magnitude matters; the dose-response is individual.",
  "Detection is reactive: found on radiographs after damage.",
 ],
 "requirements": [
  "A pre-treatment susceptibility test with real predictive power.",
  "Proof that modified mechanics prevent resorption in high-risk patients.",
  "Understanding of the odontoclast-activation threshold biology.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Brezniak N, Wasserstein A. Orthodontically induced inflammatory root resorption. Angle Orthodontist. 2002;72(3):180-184.",
  "Al-Qawasmi RA et al. Genetic predisposition to external apical root resorption. American Journal of Orthodontics and Dentofacial Orthopedics. 2003;123(3):242-252.",
  "Weltman B et al. Root resorption associated with orthodontic tooth movement: a systematic review. American Journal of Orthodontics and Dentofacial Orthopedics. 2010;137(4):462-476.",
  "Topkara A et al. External apical root resorption. Various; 2012-2018.",
 ],
 "demo_data": {"a": ("patients with severe resorption, percent (approx)", 5.0),
               "b": ("percent scale", 100.0), "bounds": (0.02, 0.1),
               "step1": "a small minority loses significant root length - unpredictably, under identical mechanics",
               "confirm": "screened high-risk patients show less resorption with modified mechanics",
               "refute": "susceptibility proves stochastic rather than trait-like"},
},
# ------------------------------------------------------------------ rank 17
{
 "key": "endo-failure",
 "name": "Endodontic Failure: The Persistent Infection",
 "group": "Endodontics",
 "ladder_rank": 17, "ladder_tier": "compounded",
 "problem": "Root canals fail in a stubborn minority - why do some infections survive disinfection, and what would sterilize the unsterilizable canal?",
 "description": "Root canal treatment succeeds in the 85-95% range; failures trace mostly to persistent intraradicular infection - bacteria surviving in isthmuses, lateral canals, and dentinal tubules that instruments and irrigants can't reach. Enterococcus faecalis is the classic persistent species. Retreatment or apical surgery can rescue many, but some teeth remain infected through every attempt.",
 "background": "The infection etiology of apical periodontitis was established by Kakehashi (1965, germ-free rats). Nair's work mapped the anatomical refuges: isthmuses, ramifications, tubules. Sodium hypochlorite remains the gold-standard irrigant after a century; activation methods (ultrasonic, laser, multisonic/GentleWave) improve penetration with debated clinical benefit. Single-visit versus multiple-visit disinfection was settled as roughly equivalent. As of 2026 the canal system's complexity still defeats complete disinfection in a minority of cases.",
 "why_it_matters": "Persistent infection means persistent disease: pain, abscess, bone loss, and eventual extraction of a tooth that endodontics promised to save. Sterilizing the canal system would close endodontics' main failure mode.",
 "sig_pointer": "The Signature system's proposed approach treats the canal as a 3D refuge map to be systematically cleared, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that endodontic failure is an anatomical refuge problem: disinfection fails where geometry defeats chemistry, and the refuges are mappable per tooth. "
  "Assumptions: (1) persistent bacteria occupy identifiable anatomical refuges; (2) refuge maps are obtainable (CBCT, microscopy); (3) refuge-targeted disinfection beats protocol disinfection. "
  "Reasoning path: a refuge-map model explains why better irrigants plateau - chemistry can't reach geometry - and predicts that mapped, targeted disinfection will outperform. "
  "Proposed mechanism: 'refuge-mapped' endodontics - imaging the canal system's hiding places and directing activation energy into them, verified by bacterial-load measures. "
  "What would confirm it: mapped disinfection outperforming standard protocols on persistent-disease rates in trials. "
  "What would kill it: evidence that persistent infection is biological (resistant biofilm states) rather than anatomical, defeating geometry-targeted approaches. "
  "What this does not claim: it does not claim sterilization is achievable today, does not advise on technique, and does not constitute dental advice."),
 "sig_lens": "The Signature lens reads the failed root canal as bacteria surviving in mapped refuges, and asks what targeted energy would clear them.",
 "how_it_works": "Endodontic researchers study failure through retreatment outcome cohorts, bacterial sampling of failed cases, irrigant-activation trials, and anatomical mapping.",
 "key_points": [
  "Root canal succeeds 85-95%; failures are mostly persistent infection.",
  "Kakehashi (1965) proved the infection etiology in germ-free rats.",
  "Isthmuses, lateral canals, and tubules harbor unreachable bacteria.",
  "E. faecalis is the classic persistent species.",
  "Anatomy still defeats chemistry in a minority of cases.",
 ],
 "requirements": [
  "Per-tooth refuge maps from clinical imaging.",
  "Disinfection reaching the mapped refuges.",
  "Proof of reduced persistent disease in trials.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Kakehashi S et al. The effects of surgical exposures of dental pulps in germ-free and conventional laboratory rats. Oral Surgery, Oral Medicine, Oral Pathology. 1965;20:340-349.",
  "Nair PNR et al. Microbial status of apical root canal system of human mandibular first molars with primary apical periodontitis. Oral Surgery, Oral Medicine, Oral Pathology. 2005;99(2):231-252.",
  "Sjogren U et al. Factors affecting the long-term results of endodontic treatment. Journal of Endodontics. 1990;16(10):498-504.",
  "Ng YL et al. Outcome of primary root canal treatment: systematic review. International Endodontic Journal. 2007;40(12):921-939.",
 ],
 "demo_data": {"a": ("root canal failure rate, percent (approx upper)", 10.0),
               "b": ("percent scale", 100.0), "bounds": (0.05, 0.15),
               "step1": "about one in ten root canals fails - mostly to infection hiding in unreachable anatomy",
               "confirm": "refuge-mapped disinfection beats standard protocols on persistent disease",
               "refute": "persistent infection proves biological rather than anatomical"},
},
# ------------------------------------------------------------------ rank 18
{
 "key": "cracked-tooth",
 "name": "Cracked Tooth Syndrome Diagnosis",
 "group": "Endodontics",
 "ladder_rank": 18, "ladder_tier": "compounded",
 "problem": "A cracked tooth hurts on biting but hides from X-rays - why is diagnosis still a guessing game, and what would reveal the crack?",
 "description": "Cracked tooth syndrome - incomplete fracture of a vital tooth causing sharp biting pain - is notoriously hard to diagnose: cracks are usually invisible on radiographs, symptoms mimic other conditions, and the crack's depth (restorable versus hopeless) can't be assessed until the tooth is opened. Dentists rely on bite tests, transillumination, and dyes - 19th-century tools for a 21st-century problem.",
 "background": "Cracked teeth were characterized by Cameron (1964, 1976); the diagnostic toolkit barely changed since: bite sticks, transillumination, methylene blue, and exploratory excavation. CBCT helps little (cracks below resolution, artifacts from restorations). Optical coherence tomography and near-infrared imaging show promise in vitro but aren't clinical. The prognostic question - will this crack stay coronal or split the root? - remains unanswerable preoperatively. As of 2026 diagnosis is still clinical art, and many cracked teeth are crowned hopefully or extracted unnecessarily.",
 "why_it_matters": "Cracked teeth are common, painful, and diagnostically treacherous: wrong calls waste crowns on hopeless teeth and extract savable ones. Revealing the crack would end one of dentistry's most frustrating guessing games.",
 "sig_pointer": "The Signature system's proposed approach images the crack directly instead of inferring it, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that cracked-tooth diagnosis fails because every current method infers the crack from symptoms while the crack itself is imageable with the right physics. "
  "Assumptions: (1) cracks have detectable physical signatures (optical, acoustic); (2) depth and trajectory determine prognosis; (3) direct imaging beats symptom inference. "
  "Reasoning path: an imaging-first model explains the diagnostic uncertainty and predicts that crack-visualizing technology will outperform the clinical toolkit. "
  "Proposed mechanism: 'crack-revealing' imaging (near-infrared, OCT, or acoustic methods adapted clinically) that shows the crack's path and depth before treatment decisions. "
  "What would confirm it: imaged crack paths predicting restorability better than clinical judgment in studies. "
  "What would kill it: evidence that crack behavior is unpredictable even when visualized, or that no clinical physics can resolve cracks in situ. "
  "What this does not claim: it does not claim an imaging device exists clinically, does not advise on cracked teeth, and does not constitute dental advice."),
 "sig_lens": "The Signature lens reads the aching tooth as a hidden fracture awaiting direct imaging, and asks what physics would reveal it.",
 "how_it_works": "Researchers study cracked teeth through bite-test cohorts, transillumination studies, OCT and near-infrared imaging research, and outcome studies of crowned cracked teeth.",
 "key_points": [
  "Cracks are usually invisible on radiographs.",
  "Diagnosis relies on bite tests, transillumination, dyes - little changed since the 1960s.",
  "Cameron characterized the syndrome (1964, 1976).",
  "CBCT rarely resolves cracks; artifacts interfere.",
  "Prognosis (restorable versus hopeless) is unknowable preoperatively.",
 ],
 "requirements": [
  "Clinical imaging resolving crack path and depth in situ.",
  "Proof that imaged cracks predict restorability.",
  "A diagnostic standard replacing the clinical guessing game.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Cameron CE. Cracked-tooth syndrome. Journal of the American Dental Association. 1964;68:405-411.",
  "Cameron CE. The cracked tooth syndrome: additional findings. Journal of the American Dental Association. 1976;93(5):971-975.",
  "Rivera EM, Walton RE. Cracking the cracked tooth code. Various; 2007-2015.",
  "Kahler B. Cracked tooth syndrome: diagnosis and management. Australian Dental Journal. 2008;53(Suppl 1):S10-S17.",
 ],
 "demo_data": {"a": ("cracked teeth correctly diagnosed at first visit, percent (approx)", 50.0),
               "b": ("percent scale", 100.0), "bounds": (0.35, 0.65),
               "step1": "about half of cracked teeth are missed at first presentation - the diagnosis is a coin flip",
               "confirm": "crack-revealing imaging beats clinical judgment on restorability prediction",
               "refute": "crack behavior proves unpredictable even when directly visualized"},
},
# ------------------------------------------------------------------ rank 19
{
 "key": "oral-cancer-detection",
 "name": "Oral Cancer Early Detection",
 "group": "Oral Medicine",
 "ladder_rank": 19, "ladder_tier": "compounded",
 "problem": "Oral cancer caught early is curable; caught late it kills - why is early detection still mostly luck, and what would find it in time?",
 "description": "Oral squamous cell carcinoma has a five-year survival around 50-60%, driven by late presentation: early lesions are painless and mimic benign conditions. Dentists screen visually, but visual screening misses subtle dysplasia; adjunctive tools (toluidine blue, fluorescence/VELscope, brush cytology) have imperfect accuracy. Salivary biomarkers are promising but unvalidated for screening.",
 "background": "The late-presentation problem was quantified in the 1990s-2000s: most oral cancers are stage III-IV at diagnosis. Screening trials are scarce (the Kerala trial showed visual screening reduced mortality in high-risk users). Adjunctive technologies cycled with enthusiasm and disappointment: VELscope's fluorescence, Identafi, brush biopsy (OralCDx) - each with sensitivity/specificity trade-offs that limit screening use. HPV's role in oropharyngeal cancer reframed risk. As of 2026 no validated early-detection test exists for general dental practice.",
 "why_it_matters": "The survival gap between early and late oral cancer is among the largest in oncology: early detection is nearly curative, late detection often fatal. A real screening test would save lives with the dentist's existing recall system.",
 "sig_pointer": "The Signature system's proposed approach detects the molecular field before the visible lesion, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that oral cancer detection fails by looking for lesions while the disease begins as a molecular field: field cancerization means the visible lesion is late, and the detectable event is earlier. "
  "Assumptions: (1) field cancerization precedes visible lesions; (2) the field has detectable molecular signatures in saliva or brush samples; (3) field-directed surveillance beats lesion-directed screening. "
  "Reasoning path: a field model explains why visual screening misses early disease and predicts that molecular field detection will find it. "
  "Proposed mechanism: 'field surveillance' - salivary or brush-sample molecular panels detecting the cancerized field, triggering targeted examination, validated in screening trials. "
  "What would confirm it: field panels detecting pre-lesional disease and improving stage at diagnosis in trials. "
  "What would kill it: evidence that the field lacks consistent early signatures, or that lead-time doesn't translate to survival. "
  "What this does not claim: it does not claim a screening test exists, does not advise on screening, and does not constitute dental or medical advice."),
 "sig_lens": "The Signature lens reads the late cancer as a field that was detectable before it was visible, and asks what molecular surveillance would find it.",
 "how_it_works": "Researchers study early detection through screening trials, adjunctive-technology accuracy studies, salivary biomarker discovery, and field-cancerization biology.",
 "key_points": [
  "Oral cancer five-year survival is ~50-60%, driven by late stage at diagnosis.",
  "Early lesions are painless and mimic benign conditions.",
  "The Kerala trial showed visual screening can reduce mortality in high-risk groups.",
  "Adjunctive tools (fluorescence, brush cytology) have imperfect accuracy.",
  "No validated molecular screening test exists for dental practice.",
 ],
 "requirements": [
  "Validated molecular field-detection panels.",
  "Screening trials proving stage shift and survival benefit.",
  "A test practical for general dental recall systems.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Sankaranarayanan R et al. Effect of screening on oral cancer mortality in Kerala, India. Lancet. 2005;365:1927-1933.",
  "Warnakulasuriya S. Global epidemiology of oral and oropharyngeal cancer. Oral Oncology. 2009;45(4-5):309-316.",
  "Lingen MW et al. Critical evaluation of diagnostic aids for the detection of oral cancer. Oral Oncology. 2008;44(1):10-22.",
  "Braakhuis BJM et al. A genetic explanation of Slaughter's concept of field cancerization. Cancer Research. 2003;63:1727-1730.",
 ],
 "demo_data": {"a": ("oral cancers diagnosed at late stage, percent (approx)", 65.0),
               "b": ("percent scale", 100.0), "bounds": (0.5, 0.8),
               "step1": "two-thirds of oral cancers are found late - when survival has already halved",
               "confirm": "field panels detect pre-lesional disease and improve stage at diagnosis",
               "refute": "the cancerized field proves to lack consistent early signatures"},
},
# ------------------------------------------------------------------ rank 20
{
 "key": "burning-mouth",
 "name": "Burning Mouth Syndrome",
 "group": "Orofacial Pain",
 "ladder_rank": 20, "ladder_tier": "compounded",
 "problem": "The mouth burns but looks normal - what causes burning mouth syndrome, and why does almost nothing treat it reliably?",
 "description": "Burning mouth syndrome (BMS) - chronic oral burning without visible lesions, mostly in postmenopausal women - is a diagnosis of exclusion with no agreed mechanism. Neuropathic theories dominate: small-fiber neuropathy of the tongue, central pain mechanisms, hormonal influences. Treatments (clonazepam, alpha-lipoic acid, capsaicin, CBT) show small inconsistent effects; most patients cycle through them.",
 "background": "BMS was characterized in the late 20th century; Lauria's 2005 finding of reduced tongue innervation density supported the small-fiber neuropathy theory. Hormonal links (postmenopausal predominance, estrogen) suggest endocrine contributions. But the evidence base is thin: small trials, heterogeneous criteria, large placebo responses. The 2018 World Workshop classification formalized BMS as a distinct entity while acknowledging the mechanistic vacuum. As of 2026 BMS remains a syndrome in search of a mechanism and a treatment.",
 "why_it_matters": "BMS causes relentless suffering in a definable population with no good answer: patients are told nothing is wrong while their mouth burns daily. A mechanism would end both the suffering and the dismissal.",
 "sig_pointer": "The Signature system's proposed approach treats BMS as a small-fiber neuropathy with central amplification, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that BMS is a two-hit disorder: peripheral small-fiber loss in the tongue plus central amplification, with hormones modulating the threshold - explaining the demographics and the treatment resistance. "
  "Assumptions: (1) tongue small-fiber density is reduced in BMS; (2) central mechanisms amplify the signal; (3) the two hits interact rather than acting alone. "
  "Reasoning path: a two-hit model explains why peripheral treatments alone underperform and predicts combined peripheral-central therapy will work better. "
  "Proposed mechanism: 'two-hit' BMS care - neuroprotective/regenerative strategies for the periphery plus central pain rehabilitation - tested against burning scores. "
  "What would confirm it: combined therapy outperforming single-target approaches in trials, with fiber density and central markers mediating. "
  "What would kill it: evidence that fiber loss is consequence not cause, or that central mechanisms dominate entirely. "
  "What this does not claim: it does not claim a treatment exists, does not advise on therapy, and does not constitute dental or medical advice."),
 "sig_lens": "The Signature lens reads the burning mouth as peripheral loss amplified centrally, and asks what two-hit therapy would quiet both.",
 "how_it_works": "Researchers study BMS through tongue-biopsy fiber counts, quantitative sensory testing, hormonal association studies, and small treatment trials.",
 "key_points": [
  "BMS is chronic oral burning without lesions, mostly postmenopausal women.",
  "Lauria (2005) found reduced tongue innervation - the neuropathy theory.",
  "Hormonal influences are suspected but unproven.",
  "Treatments show small, inconsistent effects; placebo responses are large.",
  "The 2018 World Workshop formalized BMS while acknowledging the vacuum.",
 ],
 "requirements": [
  "Proof of the causal role of small-fiber loss.",
  "Combined peripheral-central therapy proven in trials.",
  "Diagnostic criteria separating BMS from mimics reliably.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Lauria G et al. Trigeminal small-fiber sensory neuropathy causes burning mouth syndrome. Pain. 2005;115(3):332-337.",
  "Jääskeläinen SK. Pathophysiology of primary burning mouth syndrome. Clinical Neurophysiology. 2012;123(1):71-77.",
  "International Classification of Orofacial Pain. Burning mouth syndrome criteria. Cephalalgia. 2020;40(2):129-221.",
  "Zakrzewska JM et al. Interventions for burning mouth syndrome. Cochrane Database of Systematic Reviews. 2016;11:CD002779.",
 ],
 "demo_data": {"a": ("BMS patients who are postmenopausal women, percent (approx)", 80.0),
               "b": ("percent scale", 100.0), "bounds": (0.65, 0.9),
               "step1": "four in five sufferers are postmenopausal women - the demographics point at mechanism",
               "confirm": "combined therapy beats single-target approaches with markers mediating",
               "refute": "fiber loss proves to be consequence rather than cause"},
},
# ------------------------------------------------------------------ rank 21
{
 "key": "xerostomia",
 "name": "Xerostomia Management",
 "group": "Oral Medicine",
 "ladder_rank": 21, "ladder_tier": "compounded",
 "problem": "Dry mouth from medications, radiation, or Sjogren's causes rampant decay and misery - why is saliva so hard to replace, and what would truly relieve it?",
 "description": "Xerostomia - subjective dry mouth, often with objectively low salivary flow - affects a large fraction of the elderly (polypharmacy), head-and-neck radiation patients, and Sjogren's sufferers. Consequences: rampant caries, candidiasis, dysphagia, dysgeusia, speech difficulty. Saliva substitutes lubricate briefly; sialogogues (pilocarpine, cevimeline) help some with side effects; nothing replaces saliva's complex protective functions.",
 "background": "Saliva's functions - buffering, remineralization, antimicrobial, lubrication, digestion - were mapped in the 20th century; its complexity explains why substitutes fail. Radiation xerostomia research produced parotid-sparing IMRT and submandibular gland transfer, reducing but not eliminating the problem. Sjogren's therapies target the autoimmune cause with limited salivary recovery. Gene therapy and stem-cell approaches to regenerate irradiated glands are investigational. As of 2026 palliation is the standard and restoration the dream.",
 "why_it_matters": "Xerostomia condemns patients to rapid dental destruction and daily misery - eating, speaking, and swallowing all impaired. True salivary restoration would rescue quality of life for millions.",
 "sig_pointer": "The Signature system's proposed approach treats saliva as a multi-function fluid needing functional replacement, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that saliva substitutes fail because they replace one function (lubrication) of a dozen: the therapeutic target should be functional clusters, starting with the decay-driving ones. "
  "Assumptions: (1) saliva's functions are separable; (2) the highest-value cluster is mineral protection plus antimicrobial action; (3) functional replacement beats watery lubrication. "
  "Reasoning path: a functional-cluster model explains substitute failures and predicts that mineral-plus-antimicrobial formulations will outperform lubricants on caries endpoints. "
  "Proposed mechanism: 'functional saliva' - formulations replicating the protective clusters, plus regenerative approaches for glands with residual capacity. "
  "What would confirm it: functional formulations outperforming substitutes on caries and candidiasis in trials. "
  "What would kill it: evidence that saliva's functions are inseparable in practice, or that only gland regeneration can work. "
  "What this does not claim: it does not claim a product exists, does not advise on substitutes, and does not constitute dental or medical advice."),
 "sig_lens": "The Signature lens reads dry mouth as a dozen missing functions, and asks which cluster would matter most to replace.",
 "how_it_works": "Researchers study xerostomia through salivary flow trials, substitute comparisons, sialogogue studies, gland-sparing radiation techniques, and regenerative approaches.",
 "key_points": [
  "Xerostomia affects much of the elderly, radiation patients, Sjogren's sufferers.",
  "Consequences: rampant caries, candidiasis, dysphagia, speech difficulty.",
  "Substitutes lubricate briefly; sialogogues help some with side effects.",
  "Parotid-sparing IMRT reduced radiation xerostomia partially.",
  "Nothing replicates saliva's full protective functions.",
 ],
 "requirements": [
  "Functional-cluster formulations proven on caries endpoints.",
  "Gland-regeneration approaches for irradiated and autoimmune glands.",
  "Prevention of the polypharmacy-driven epidemic.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "von Bultzingslowen I et al. Salivary dysfunction associated with systemic diseases. Journal of Dental Research. 2007;86(3):242-257.",
  "Jensen SB et al. A systematic review of salivary gland hypofunction and xerostomia. Oral Oncology. 2010;46(2):106-111.",
  "Fox PC. Xerostomia: recognition and management. Various; 2008-2015.",
  "Nussle W et al. Gene therapy for salivary glands. Various; 2010-2020.",
 ],
 "demo_data": {"a": ("elderly on xerostomia-causing medications, percent (approx)", 40.0),
               "b": ("percent scale", 100.0), "bounds": (0.3, 0.55),
               "step1": "nearly half the elderly take drugs that dry the mouth - a prescribing-driven epidemic",
               "confirm": "functional formulations beat substitutes on caries and candidiasis",
               "refute": "saliva's functions prove inseparable with only gland regeneration viable"},
},
# ------------------------------------------------------------------ rank 22
{
 "key": "restoration-longevity",
 "name": "Dental Restoration Longevity",
 "group": "Restorative Dentistry",
 "ladder_rank": 22, "ladder_tier": "compounded",
 "problem": "Fillings fail - secondary caries at the margins, fracture, wear - why can't a restoration last as long as the tooth, and what is the true lifespan of modern materials?",
 "description": "Composite restorations last on average 7-10 years; amalgam lasted longer but is being phased out. Failure modes: secondary caries at the tooth-material interface, bulk fracture, marginal degradation. Each replacement removes more tooth, shrinking the tooth's lifespan with every cycle - the 'restorative death spiral.' Bioactive materials (releasing fluoride, calcium) promise to fight secondary caries but show modest clinical benefit so far.",
 "background": "Buonocore's 1955 acid-etch technique enabled adhesive dentistry; Bowen's Bis-GMA (1962) created composites. Longevity studies (Mjor, Opdam) established the 7-10 year composite average and the margin as the weak link. The Minamata Convention (2013) began amalgam's phase-down, making composite longevity the field's problem. Bioactive composites, self-healing materials, and antimicrobial monomers are investigational. As of 2026 the margin remains the failure point and the death spiral unbroken.",
 "why_it_matters": "Every filling is a future crown, every crown a future extraction: extending restoration life by even years would save teeth and billions across populations.",
 "sig_pointer": "The Signature system's proposed approach treats the margin as a living interface to be engineered, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that restoration failure is an interface disease: the margin is a dynamic gap colonized by biofilm and stressed mechanically, and materials fail there because the interface was never engineered as a system. "
  "Assumptions: (1) the margin microenvironment determines longevity; (2) biofilm at the margin drives secondary caries; (3) the interface can be made bioactive and self-sealing. "
  "Reasoning path: an interface model explains why bulk material improvements plateau - the margin dominates - and predicts interface-engineered restorations will outperform. "
  "Proposed mechanism: 'living-margin' restorations - bioactive, antimicrobial, remineralizing interfaces that seal dynamically - tested against secondary-caries endpoints. "
  "What would confirm it: interface-engineered restorations outlasting conventional ones on longevity in trials. "
  "What would kill it: evidence that patient factors (diet, hygiene) dominate regardless of interface engineering. "
  "What this does not claim: it does not claim a material exists today, does not advise on material choice, and does not constitute dental advice."),
 "sig_lens": "The Signature lens reads the failed filling as an interface disease, and asks what living margin would seal itself.",
 "how_it_works": "Restorative researchers study longevity through practice-based cohort studies, margin microleakage research, bioactive-material trials, and failure-mode analyses.",
 "key_points": [
  "Composites average 7-10 years; the margin is the weak link.",
  "Secondary caries at margins is the leading failure mode.",
  "Each replacement shrinks the tooth - the restorative death spiral.",
  "Amalgam's phase-down (Minamata 2013) made composite longevity critical.",
  "Bioactive materials show modest clinical benefit so far.",
 ],
 "requirements": [
  "Interface-engineered materials proven on longevity endpoints.",
  "Breaking the replacement cycle, not just delaying it.",
  "Materials matching amalgam's durability without its mercury.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Opdam NJM et al. Longevity of posterior composite restorations. Journal of Dental Research. 2010;89(10):1063-1067.",
  "Mjor IA et al. Failure patterns of restorations. Various; 1997-2005.",
  "Buonocore MG. A simple method of increasing the adhesion of acrylic filling materials to enamel surfaces. Journal of Dental Research. 1955;34(6):849-853.",
  "United Nations Environment Programme. Minamata Convention on Mercury. 2013.",
 ],
 "demo_data": {"a": ("composite restoration lifespan, years (approx average)", 8.0),
               "b": ("tooth lifespan needed, years (approx)", 60.0), "bounds": (0.08, 0.2),
               "step1": "a filling lasts years while the tooth must last decades - the longevity gap drives the death spiral",
               "confirm": "interface-engineered restorations beat conventional ones on longevity",
               "refute": "patient factors prove to dominate regardless of interface engineering"},
},
# ------------------------------------------------------------------ rank 23
{
 "key": "antibiotic-stewardship",
 "name": "Antibiotic Stewardship in Dentistry",
 "group": "Dental Pharmacology",
 "ladder_rank": 23, "ladder_tier": "compounded",
 "problem": "Dentists prescribe a tenth of all antibiotics, often unnecessarily - why does dental overprescribing persist, and what would make prophylaxis rational?",
 "description": "Dentistry accounts for roughly 10% of outpatient antibiotic prescribing, much of it for conditions where antibiotics don't help (irreversible pulpitis, localized abscesses needing drainage) or for prophylaxis with thin evidence (most joint replacements, many cardiac conditions after guideline narrowing). Overprescribing drives resistance and Clostridioides difficile; underprescribing risks spread of infection. The evidence-prophylaxis gap is dentistry's stewardship failure.",
 "background": "Antibiotic prophylaxis for endocarditis (AHA guidelines, narrowed 2007) and prosthetic joints (evolving AAOS guidance) created the prophylaxis culture; defensive prescribing filled the gaps. Studies show most dental antibiotic prescriptions lack indication (Suda 2019: the majority unnecessary). Stewardship programs - audit, feedback, guidelines - work in medicine but are rare in dentistry, where most prescribing happens in isolated private practices. As of 2026 dental stewardship is endorsed and barely implemented.",
 "why_it_matters": "Unnecessary dental antibiotics breed resistance and cause C. difficile - harms far beyond the dental chair. Rational prescribing would cut a tenth of outpatient antibiotics with no loss of care quality.",
 "sig_pointer": "The Signature system's proposed approach makes the right prescription the easy prescription, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that dental overprescribing is a decision-architecture problem: isolated practitioners facing uncertain diagnoses default to antibiotics because prescribing is easier and feels safer than not. "
  "Assumptions: (1) most overprescribing is defensive, not ignorant; (2) decision support at the prescribing moment changes behavior; (3) the safe default can be engineered. "
  "Reasoning path: a decision-architecture model explains why guidelines alone fail (they don't change the moment of decision) and predicts point-of-care stewardship tools will work. "
  "Proposed mechanism: 'stewardship-by-design' - prescribing workflows where the guideline-concordant choice is the default, tested against prescribing rates and outcomes. "
  "What would confirm it: designed workflows cutting unnecessary prescribing without harm signals in trials. "
  "What would kill it: evidence that overprescribing is patient-demand-driven regardless of architecture, or that defaults don't move dentists. "
  "What this does not claim: it does not claim any prescription is currently wrong, does not advise on antibiotics, and does not constitute dental or medical advice."),
 "sig_lens": "The Signature lens reads the unnecessary prescription as the easy choice winning, and asks what design would make the right choice easiest.",
 "how_it_works": "Researchers study dental stewardship through prescribing audits, prophylaxis-guideline evaluations, resistance surveillance, and implementation trials.",
 "key_points": [
  "Dentistry accounts for ~10% of outpatient antibiotic prescribing.",
  "Most dental prescriptions lack indication (Suda 2019).",
  "Prophylaxis guidelines narrowed (AHA 2007) but defensive prescribing persists.",
  "Stewardship programs are rare in private dental practice.",
  "Overprescribing drives resistance and C. difficile.",
 ],
 "requirements": [
  "Point-of-care stewardship tools proven in dental settings.",
  "Prescribing data infrastructure for dentistry.",
  "Prophylaxis evidence for the genuinely uncertain cases.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Suda KJ et al. Antibiotic prescriptions by dentists in the United States. JAMA Network Open. 2019;2(5):e193909.",
  "American Heart Association. Prevention of infective endocarditis guidelines. 2007 (updated 2021).",
  "American Association of Orthopaedic Surgeons. Antibiotic prophylaxis guidance. Various.",
  "World Health Organization. Global action plan on antimicrobial resistance. 2015.",
 ],
 "demo_data": {"a": ("dental antibiotic prescriptions lacking indication, percent (approx)", 70.0),
               "b": ("percent scale", 100.0), "bounds": (0.55, 0.85),
               "step1": "most dental antibiotic prescriptions lack indication - a stewardship emergency hiding in plain sight",
               "confirm": "designed workflows cut unnecessary prescribing without harm signals",
               "refute": "overprescribing proves patient-demand-driven regardless of architecture"},
},
# ------------------------------------------------------------------ rank 24
{
 "key": "tooth-regeneration",
 "name": "Whole-Tooth Regeneration",
 "group": "Regenerative Dentistry",
 "ladder_rank": 24, "ladder_tier": "advanced",
 "problem": "A bioengineered tooth that erupts, roots, and bites - is it possible, and what stands between organ-germ methods and a human tooth?",
 "description": "Whole-tooth regeneration - growing a complete tooth with enamel, dentin, pulp, and roots - works in mice: Nakao's 2007 bioengineered tooth germs erupted and functioned. Scaling to humans faces size, time (human tooth development takes years), innervation, and the need for the tooth to integrate with the jaw. No human trial has grown a tooth; the field advances through organoids and stem-cell approaches.",
 "background": "Tooth development biology (Thesleff's work on epithelial-mesenchymal signaling) provided the blueprint: recapitualate development. Nakao et al. (Nature Methods, 2007) grew functional teeth from dissociated cells in mice; Oshima (2011) showed innervated, erupted bioengineered teeth. Human translation stalls on: sourcing the right cells (dental epithelium is lost after development), the years-long timeline, and regulatory paths for a living organ. As of 2026 whole-tooth regeneration is a mouse success awaiting human biology.",
 "why_it_matters": "A regenerated tooth beats any implant: it has a periodontal ligament (shock absorption, proprioception), it remodels, it belongs. Growing teeth would end the implant era's compromises.",
 "sig_pointer": "The Signature system's proposed approach recapitulates development with human-compatible cell sources, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that tooth regeneration is a recapitulation problem: development already solved it, and the task is re-running the program with available cells. "
  "Assumptions: (1) the developmental program is re-runnable; (2) iPS-derived dental epithelium can substitute for embryonic sources; (3) the jaw will accept a developing germ. "
  "Reasoning path: a recapitulation model explains mouse success and predicts that human cell sourcing, not the program, is the barrier. "
  "Proposed mechanism: 'program re-run' - iPS-derived epithelial-mesenchymal germs implanted to develop in situ, with the jaw as the bioreactor. "
  "What would confirm it: human-cell germs developing into functional teeth in large animals. "
  "What would kill it: evidence that human cells can't re-run the program, or that the timeline is biologically fixed at years. "
  "What this does not claim: it does not claim teeth can be grown today, offers no therapy, and does not constitute dental advice."),
 "sig_lens": "The Signature lens reads the missing tooth as a developmental program awaiting re-run, and asks which cells could run it.",
 "how_it_works": "Researchers study tooth regeneration through developmental biology, organ-germ methods, iPS differentiation, and large-animal implantation.",
 "key_points": [
  "Bioengineered mouse teeth erupt and function (Nakao 2007).",
  "Oshima (2011) showed innervated bioengineered teeth.",
  "Human dental epithelium is lost after development - the cell-sourcing problem.",
  "Human tooth development takes years.",
  "No human trial has grown a tooth.",
 ],
 "requirements": [
  "Human-compatible dental epithelial cell sources.",
  "Proof of functional human-cell teeth in large animals.",
  "A regulatory path for a living replacement organ.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Nakao K et al. The development of a bioengineered organ germ method. Nature Methods. 2007;4:227-230.",
  "Oshima M et al. Functional tooth regeneration using a bioengineered tooth germ. PLoS One. 2011;6(6):e21531.",
  "Thesleff I. Epithelial-mesenchymal signalling regulating tooth morphogenesis. Journal of Cell Science. 2003;116:1647-1648.",
  "Sharpe PT. Dental mesenchymal stem cells. Development. 2016;143:2273-2280.",
 ],
 "demo_data": {"a": ("human tooth development time, years (approx)", 6.0),
               "b": ("mouse tooth development time, weeks (approx)", 4.0), "bounds": (1.0, 2.5),
               "step1": "a human tooth takes years to develop versus weeks in mice - the timeline is the translation barrier",
               "confirm": "human-cell germs develop into functional teeth in large animals",
               "refute": "human cells prove unable to re-run the developmental program"},
},
# ------------------------------------------------------------------ rank 25
{
 "key": "salivary-regeneration",
 "name": "Salivary Gland Regeneration",
 "group": "Regenerative Dentistry",
 "ladder_rank": 25, "ladder_tier": "advanced",
 "problem": "Radiation destroys salivary glands permanently - can a functional gland be regrown, and what would it take?",
 "description": "Head-and-neck radiation cures cancer and sacrifices saliva: glands don't regenerate, leaving lifelong xerostomia. Regenerative approaches - stem-cell transplantation, gene therapy (aquaporin-1), bioengineered glands - show signals in animals. The gland's branching architecture and innervation make it harder than it looks.",
 "background": "Salivary stem cells were identified in the 2000s (Lombaert); transplantation rescued irradiated mouse glands. Gene therapy delivering aquaporin-1 to surviving duct cells (Baum's group, NIDCR) reached human trials with modest benefit. Bioengineered glands (Ogawa 2013) functioned in mice. But human translation stalls: the irradiated gland bed is fibrotic and hostile, stem-cell sourcing is unsolved, and no approach restores normal flow. As of 2026 regeneration is preclinical.",
 "why_it_matters": "Radiation xerostomia is a lifelong sentence delivered with the cancer cure: regenerating glands would complete the cure.",
 "sig_pointer": "The Signature system's proposed approach treats the irradiated gland bed as the barrier, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that gland regeneration fails on the bed, not the cells: the irradiated, fibrotic gland bed can't support regrowth regardless of stem-cell quality. "
  "Assumptions: (1) stem cells are available or engineerable; (2) the fibrotic bed is the rate limiter; (3) bed conditioning enables engraftment. "
  "Reasoning path: a bed-first model explains animal success (healthy beds) versus human stalls (irradiated beds) and predicts bed-conditioning will unlock translation. "
  "Proposed mechanism: 'bed-conditioned' regeneration - anti-fibrotic preparation of the gland bed followed by stem-cell or bioengineered gland implantation. "
  "What would confirm it: conditioned beds supporting functional gland regrowth in models and then humans. "
  "What would kill it: evidence that irradiated beds are irreversibly hostile, or that innervation can't be restored. "
  "What this does not claim: it does not claim glands can be regrown today, offers no therapy, and does not constitute dental or medical advice."),
 "sig_lens": "The Signature lens reads the dead gland as good seeds on poisoned soil, and asks what would rehabilitate the soil.",
 "how_it_works": "Researchers study gland regeneration through stem-cell transplantation, aquaporin gene therapy trials, bioengineered glands, and fibrosis biology.",
 "key_points": [
  "Radiation destroys salivary glands permanently.",
  "Stem-cell transplantation rescues irradiated mouse glands.",
  "Aquaporin-1 gene therapy reached human trials with modest benefit.",
  "Bioengineered glands function in mice (Ogawa 2013).",
  "The irradiated human gland bed is fibrotic and hostile.",
 ],
 "requirements": [
  "Bed-conditioning that makes irradiated tissue receptive.",
  "Stem-cell sources or bioengineered glands for humans.",
  "Restoration of innervation and regulated secretion.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Lombaert IMA et al. Combined KIT and FGFR2b signaling. Various; 2008-2013.",
  "Baum BJ et al. Aquaporin-1 gene therapy. Various NIDCR trials; 2012-2020.",
  "Ogawa M et al. Functional salivary gland regeneration by transplantation of a bioengineered organ germ. Nature Communications. 2013;4:2498.",
  "Jensen DH et al. Radiation-induced salivary gland damage. Various; 2015-2020.",
 ],
 "demo_data": {"a": ("head-and-neck radiation patients with permanent xerostomia, percent (approx)", 80.0),
               "b": ("percent scale", 100.0), "bounds": (0.6, 0.95),
               "step1": "most irradiated patients lose saliva permanently - the cure's lifelong tax",
               "confirm": "conditioned beds support functional gland regrowth",
               "refute": "irradiated beds prove irreversibly hostile to regrowth"},
},
# ------------------------------------------------------------------ rank 26
{
 "key": "tmj-regeneration",
 "name": "TMJ Disc Regeneration",
 "group": "Regenerative Dentistry",
 "ladder_rank": 26, "ladder_tier": "advanced",
 "problem": "The jaw joint's disc displaces, perforates, and degenerates - can it be regenerated, or is the TMJ doomed to prosthetics?",
 "description": "The temporomandibular joint's fibrocartilaginous disc cushions the condyle; displacement and degeneration cause pain and dysfunction. Current care is conservative (splints, physiotherapy) or destructive (discectomy, prosthetic joint replacement). Disc regeneration - tissue-engineered fibrocartilage that integrates and loads - is preclinical: the disc's avascularity, complex loading, and poor healing mirror the knee meniscus problem.",
 "background": "TMJ tissue engineering grew from orthopedic meniscus work: scaffold-based fibrocartilage, growth-factor stimulation, mechanical conditioning in bioreactors. Animal studies show partial regeneration; human translation faces the joint's complex biomechanics and the difficulty of delivering constructs arthroscopically. As of 2026 no regenerated disc functions in a human jaw.",
 "why_it_matters": "TMJ degeneration disables young patients for decades; prosthetic joints wear and fail. A regenerated disc would restore the joint biologically instead of replacing it mechanically.",
 "sig_pointer": "The Signature system's proposed approach engineers the disc for the joint's specific loading, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that disc regeneration must be load-driven: fibrocartilage engineered without the TMJ's specific mechanical conditioning won't survive the joint. "
  "Assumptions: (1) mechanical conditioning determines fibrocartilage phenotype; (2) the TMJ's loading is mappable and reproducible in bioreactors; (3) integration requires the native rim. "
  "Reasoning path: a load-driven model explains why generic cartilage constructs fail in joints and predicts TMJ-conditioned constructs will succeed. "
  "Proposed mechanism: 'joint-conditioned' disc engineering - scaffolds matured under TMJ-specific loading profiles before implantation. "
  "What would confirm it: conditioned constructs integrating and loading in large-animal TMJs. "
  "What would kill it: evidence that the disc's avascularity defeats any construct, or that loading can't be reproduced. "
  "What this does not claim: it does not claim a disc can be regrown today, offers no therapy, and does not constitute dental advice."),
 "sig_lens": "The Signature lens reads the failed disc as needing its specific mechanical education, and asks what bioreactor would teach it.",
 "how_it_works": "Researchers study disc regeneration through scaffold engineering, bioreactor conditioning, large-animal TMJ models, and meniscus-translation research.",
 "key_points": [
  "The TMJ disc is fibrocartilage with poor healing, like the meniscus.",
  "Current care: conservative management or destructive surgery.",
  "Tissue-engineered discs show partial regeneration in animals.",
  "The joint's complex loading defeats generic constructs.",
  "No regenerated disc functions in a human jaw.",
 ],
 "requirements": [
  "TMJ-specific mechanical conditioning protocols.",
  "Constructs integrating with the native disc rim.",
  "Arthroscopic delivery methods.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Almarza AJ, Athanasiou KA. Design characteristics for the tissue engineering of cartilaginous tissues. Annals of Biomedical Engineering. 2004;32(1):2-17.",
  "Kalpakci KN et al. Tissue engineering of the TMJ disc. Various; 2011-2018.",
  "Willard VP et al. Tissue engineering of the TMJ. Various; 2012-2020.",
  "Detamore MS, Athanasiou KA. Motivation, characterization, and strategy for tissue engineering the temporomandibular joint disc. Tissue Engineering. 2003;9(6):1065-1087.",
 ],
 "demo_data": {"a": ("TMJ disc regenerations functioning in humans", 0.5),
               "b": ("prosthetic TMJ replacements performed yearly, approximate thousands", 2.0), "bounds": (0.1, 0.6),
               "step1": "zero regenerated discs versus thousands of prosthetic joints - the biological option doesn't exist yet",
               "confirm": "conditioned constructs integrate and load in large-animal TMJs",
               "refute": "disc avascularity proves to defeat any engineered construct"},
},
# ------------------------------------------------------------------ rank 27
{
 "key": "craniofacial-regeneration",
 "name": "Craniofacial Bone Regeneration",
 "group": "Regenerative Dentistry",
 "ladder_rank": 27, "ladder_tier": "advanced",
 "problem": "Large jaw defects from trauma, cancer, or congenital conditions need bone - why can't large craniofacial defects be reliably regenerated?",
 "description": "Small bone defects heal; large ones (from tumor resection, trauma, osteoradionecrosis) don't. Current reconstruction uses vascularized free flaps (fibula) - effective but morbid, and the bone never quite matches. Bone tissue engineering - scaffolds plus growth factors (BMP-2) plus cells - works for small defects but fails at scale: the center dies without vasculature, BMP-2 causes swelling and ectopic bone, and irradiated beds resist.",
 "background": "Distraction osteogenesis (Ilizarov, McCarthy for craniofacial) grew bone by gradual separation. BMP-2 (FDA 2002 for spine, used off-label craniofacially) showed both promise and complications. Scaffold vascularization strategies - prevascularization, growth-factor gradients - advance slowly. As of 2026 large-defect regeneration remains unsolved; free flaps remain the standard.",
 "why_it_matters": "Facial bone loss disfigures and disables: eating, speaking, and identity all live in the craniofacial skeleton. Reliable regeneration would replace morbid flap surgery with true restoration.",
 "sig_pointer": "The Signature system's proposed approach treats large-defect regeneration as a vascularization problem first, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that large-defect bone regeneration fails on vascularization before biology: the construct's center dies while its edges heal, regardless of growth factors. "
  "Assumptions: (1) diffusion limits viable construct thickness; (2) vascular ingrowth is too slow for large defects; (3) prevascularization changes the equation. "
  "Reasoning path: a vascularization-first model explains the small-versus-large defect divide and predicts prevascularized constructs will succeed where factor-loaded ones fail. "
  "Proposed mechanism: 'vasculature-first' craniofacial constructs - perfusable scaffolds verified before cell loading - tested in large-defect models. "
  "What would confirm it: prevascularized constructs healing large defects beyond current best in models. "
  "What would kill it: evidence that irradiated or scarred beds defeat even vascularized constructs, or that prevascularization can't scale. "
  "What this does not claim: it does not claim large defects are regenerable today, offers no therapy, and does not constitute dental or medical advice."),
 "sig_lens": "The Signature lens reads the dead construct center as a plumbing failure, and asks what pre-built vasculature would change.",
 "how_it_works": "Researchers study craniofacial regeneration through scaffold trials, BMP studies, prevascularization strategies, and large-animal defect models.",
 "key_points": [
  "Large craniofacial defects don't heal spontaneously.",
  "Free flaps work but are morbid and imperfect.",
  "BMP-2 helps small defects with significant complications.",
  "Construct centers die without vasculature.",
  "Irradiated beds resist all regenerative approaches.",
 ],
 "requirements": [
  "Prevascularized constructs proven in large defects.",
  "Growth-factor strategies without BMP-2's complications.",
  "Regeneration in irradiated and scarred beds.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "McCarthy JG et al. Lengthening the human mandible by gradual distraction. Plastic and Reconstructive Surgery. 1992;89(1):1-8.",
  "Warnke PH et al. Growth and transplantation of a custom vascularised bone graft. Lancet. 2004;364:766-770.",
  "Cancedda R et al. Tissue engineering and cell therapy of cartilage and bone. Matrix Biology. 2003;22(1):81-91.",
  "Kaigler D et al. Bone engineering. Various; 2010-2020.",
 ],
 "demo_data": {"a": ("critical-size defect threshold, micrometers (approx)", 20000.0),
               "b": ("diffusion limit for viable tissue, micrometers (approx)", 200.0), "bounds": (80.0, 150.0),
               "step1": "defects beyond millimeters can't heal while tissue dies beyond micrometers - a hundredfold gap",
               "confirm": "prevascularized constructs heal large defects beyond current best",
               "refute": "irradiated beds prove to defeat even vascularized constructs"},
},
# ------------------------------------------------------------------ rank 28
{
 "key": "dental-stem-cells",
 "name": "Dental Stem Cell Therapies",
 "group": "Regenerative Dentistry",
 "ladder_rank": 28, "ladder_tier": "advanced",
 "problem": "Teeth harbor potent stem cells - dental pulp, apical papilla, periodontal ligament, exfoliated deciduous teeth (SHED). Why has none become a therapy?",
 "description": "Dental stem cells are accessible, multipotent, and immunomodulatory: DPSCs, SHED, SCAP, PDLSCs, DFSCs. Preclinical work shows promise for pulp regeneration, periodontal repair, even non-dental uses (neural, bone). But no dental stem-cell therapy is approved: cell sourcing, expansion, delivery, and regulation stall translation, and tooth banking remains a consumer product awaiting a use.",
 "background": "Gronthos identified DPSCs in 2000; Miura found SHED in 2003; Seo characterized PDLSCs in 2004. The field expanded rapidly with preclinical successes. Translation barriers emerged: GMP expansion at scale, delivery that keeps cells where placed, and the regulatory path for cell therapies. Early human trials (pulp regeneration with mobilized DPSCs, Nakashima's group) show feasibility signals. As of 2026 dental stem cells are a preclinical promise with early clinical footholds.",
 "why_it_matters": "Millions of extracted teeth - wisdom teeth, baby teeth - are discarded stem-cell sources. Realizing their therapeutic potential would convert dental waste into regenerative medicine.",
 "sig_pointer": "The Signature system's proposed approach treats delivery and retention as the translation barrier, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that dental stem-cell translation fails on delivery: cells work in vitro and in models but don't stay where placed or survive the hostile defect environment in humans. "
  "Assumptions: (1) the cells are therapeutically competent; (2) the defect environment kills or disperses them; (3) delivery vehicles change outcomes. "
  "Reasoning path: a delivery model explains preclinical-clinical gaps and predicts that engineered delivery will unlock translation. "
  "Proposed mechanism: 'retentive delivery' - scaffolds and signals that keep cells viable and localized - tested against cell-free controls. "
  "What would confirm it: delivered cells outperforming cell-free scaffolds in human trials. "
  "What would kill it: evidence that the cells lack human therapeutic potency regardless of delivery. "
  "What this does not claim: it does not claim stem-cell therapy works today, does not advise on tooth banking, and does not constitute dental advice."),
 "sig_lens": "The Signature lens reads the stalled therapy as a delivery failure, and asks what vehicle would keep the cells alive and in place.",
 "how_it_works": "Researchers study dental stem cells through characterization, preclinical defect models, delivery-vehicle engineering, and early human trials.",
 "key_points": [
  "DPSCs (2000), SHED (2003), PDLSCs (2004): a rich stem-cell family.",
  "Preclinical promise spans pulp, periodontal, neural, and bone repair.",
  "No dental stem-cell therapy is approved.",
  "Translation stalls on expansion, delivery, and regulation.",
  "Tooth banking sells a future without a present use.",
 ],
 "requirements": [
  "Retentive delivery proven in human defects.",
  "GMP expansion at clinical scale.",
  "Regulatory paths for dental cell therapies.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Gronthos S et al. Postnatal human dental pulp stem cells (DPSCs) in vitro and in vivo. PNAS. 2000;97(25):13625-13630.",
  "Miura M et al. SHED: stem cells from human exfoliated deciduous teeth. PNAS. 2003;100(10):5807-5812.",
  "Seo BM et al. Investigation of multipotent postnatal stem cells from human periodontal ligament. Lancet. 2004;364:149-155.",
  "Nakashima M et al. Pulp regeneration by transplantation of dental pulp stem cells. Various; 2017-2022.",
 ],
 "demo_data": {"a": ("dental stem-cell types characterized (DPSCs, SHED, SCAP, PDLSCs, DFSCs)", 5.0),
               "b": ("approved dental stem-cell therapies", 0.5), "bounds": (6.0, 20.0),
               "step1": "five characterized stem-cell families, zero approved therapies - the translation gap is total",
               "confirm": "delivered cells beat cell-free scaffolds in human trials",
               "refute": "the cells prove to lack human therapeutic potency regardless of delivery"},
},
# ------------------------------------------------------------------ rank 29
{
 "key": "microbiome-caries",
 "name": "Microbiome-Targeted Caries Therapy",
 "group": "Oral Microbiology",
 "ladder_rank": 29, "ladder_tier": "advanced",
 "problem": "If caries is dysbiosis, the cure is ecological - what would a microbiome-targeted caries therapy look like, and why doesn't one exist?",
 "description": "The ecological plaque hypothesis reframes caries as community dysfunction: acid-producers dominate when sugar is frequent and pH drops. A microbiome-targeted therapy would reshape the community - prebiotics favoring health-associated species, probiotics (S. dentisani, engineered S. mutans), arginine metabolism boosters - instead of killing everything. Early candidates show signals; none is a product.",
 "background": "Marsh's ecological hypothesis (1994, refined 2000s) provided the framework. Candidate effectors emerged: arginine (raises pH via alkali production, clinically validated in toothpaste), probiotic streptococci (S. dentisani, Lopez-Lopez), and engineered S. mutans (Hillman's BCS3-L1, abandoned over regulatory concerns). The challenge: the mouth is an open ecosystem, constantly reseeded, and interventions wash out. As of 2026 arginine toothpaste is the only ecological therapy in wide use.",
 "why_it_matters": "An ecological caries therapy would prevent disease without antimicrobials, without resistance risk, and durably - the post-antibiotic answer to the commonest human disease.",
 "sig_pointer": "The Signature system's proposed approach engineers lasting ecological shifts, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that microbiome therapies fail on persistence: the mouth reseeds from the environment, washing out introduced species within weeks. "
  "Assumptions: (1) introduced species are competent but transient; (2) persistence requires a niche advantage, not just dosing; (3) niche engineering beats repeated dosing. "
  "Reasoning path: a persistence model explains trial washout and predicts that niche-engineered colonizers will outperform dosed probiotics. "
  "Proposed mechanism: 'niche-engineered' colonizers - health-associated strains given durable adhesion or metabolic advantages - tested for persistence and caries endpoints. "
  "What would confirm it: engineered colonizers persisting months and reducing caries in trials. "
  "What would kill it: evidence that the oral ecosystem resists all engineered colonization, or that persistence requires unacceptable genetic modification. "
  "What this does not claim: it does not claim a therapy exists, does not advise on probiotics, and does not constitute dental advice."),
 "sig_lens": "The Signature lens reads the washed-out probiotic as a colonist without a niche, and asks what engineered advantage would let it stay.",
 "how_it_works": "Researchers study microbiome therapy through probiotic trials, arginine studies, engineered-strain research, and colonization-persistence measurement.",
 "key_points": [
  "The ecological plaque hypothesis reframes caries as dysbiosis (Marsh).",
  "Arginine toothpaste is the only widely used ecological therapy.",
  "Probiotic candidates wash out within weeks.",
  "Hillman's engineered S. mutans was abandoned over regulatory concerns.",
  "The mouth is an open ecosystem, constantly reseeded.",
 ],
 "requirements": [
  "Colonizers with engineered persistence advantages.",
  "Caries-endpoint proof, not just colonization proof.",
  "Regulatory paths for engineered oral microbes.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Marsh PD. Dental plaque as a biofilm and a microbial community. Caries Research. 2004;38:264-269.",
  "Nascimento MM et al. Arginine metabolism in oral biofilms. Various; 2009-2018.",
  "Lopez-Lopez A et al. Streptococcus dentisani. Various; 2017-2022.",
  "Hillman JD et al. Genetically modified Streptococcus mutans. Various; 2000-2010.",
 ],
 "demo_data": {"a": ("probiotic oral colonizer persistence, weeks (typical)", 3.0),
               "b": ("persistence needed for durable therapy, months (approx)", 6.0), "bounds": (0.3, 0.8),
               "step1": "introduced species vanish in weeks while therapy needs months - the persistence gap",
               "confirm": "engineered colonizers persist months and cut caries in trials",
               "refute": "the oral ecosystem proves to resist all engineered colonization"},
},
# ------------------------------------------------------------------ rank 30
{
 "key": "precision-dentistry",
 "name": "Precision Dentistry: Genomic Risk Prediction",
 "group": "Precision Dentistry",
 "ladder_rank": 30, "ladder_tier": "advanced",
 "problem": "Medicine has polygenic risk scores; dentistry has checkups every six months for everyone. Can genomic risk prediction personalize dental care?",
 "description": "Caries and periodontitis are heritable (~50% for caries experience, significant for aggressive periodontitis), with GWAS loci emerging. But polygenic scores explain little variance, clinical use is nil, and dentistry's risk assessment remains behavioral. The promise: high-risk patients get intensive prevention, low-risk patients get longer recall - precision allocation of preventive effort.",
 "background": "Heritability studies (twin studies for caries; family studies for aggressive periodontitis) established the genetic component. GWAS identified loci (e.g. for caries, periodontitis) with small effects. Polygenic risk scores in medicine show the path but also the limits: modest discrimination, ancestry bias, unclear clinical utility. Dental precision medicine is conceptual: no validated risk-stratified protocol exists. As of 2026 genomic dentistry is a research program, not a practice.",
 "why_it_matters": "Uniform six-month recalls waste prevention on the resistant and under-serve the susceptible: risk-stratified care would allocate effort where it prevents disease.",
 "sig_pointer": "The Signature system's proposed approach combines genomic, microbial, and behavioral risk into one score, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that genomic risk alone will never suffice for dentistry: caries and periodontitis are gene-environment-microbiome diseases, and the predictive score must integrate all three. "
  "Assumptions: (1) each risk domain adds independent information; (2) the integrated score outperforms any single domain; (3) risk-stratified care beats uniform care. "
  "Reasoning path: an integration model explains why genomic scores alone disappoint and predicts multi-domain risk tools will succeed. "
  "Proposed mechanism: 'integrated risk' scores (genomic plus microbial plus behavioral) directing recall intervals and preventive intensity, tested against disease endpoints. "
  "What would confirm it: integrated scores outperforming single-domain ones with risk-stratified care reducing disease in trials. "
  "What would kill it: evidence that risk is dominated by behavior regardless of biology, defeating stratification. "
  "What this does not claim: it does not claim a risk tool exists, does not advise on recall intervals, and does not constitute dental advice."),
 "sig_lens": "The Signature lens reads dental risk as three domains awaiting integration, and asks what combined score would allocate prevention wisely.",
 "how_it_works": "Researchers study precision dentistry through GWAS, polygenic-score development, risk-model validation, and stratified-care trials.",
 "key_points": [
  "Caries experience is ~50% heritable; aggressive periodontitis strongly familial.",
  "GWAS loci have small individual effects.",
  "Polygenic scores show modest discrimination with ancestry bias.",
  "No validated risk-stratified dental protocol exists.",
  "Recall remains uniform despite heterogeneous risk.",
 ],
 "requirements": [
  "Multi-domain risk scores with real discrimination.",
  "Proof that stratified care beats uniform care.",
  "Equity: scores valid across ancestries.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Shungin D et al. Genome-wide association study of dental caries. Nature Communications. 2019;10:2548.",
  "Munz M et al. Genome-wide association study of periodontitis. Various; 2017-2019.",
  "Divaris K. Precision dentistry. Various; 2017-2022.",
  "Werneck R et al. Heritability of caries. Various twin studies; 2010-2020.",
 ],
 "demo_data": {"a": ("caries heritability, percent (approx)", 50.0),
               "b": ("percent scale", 100.0), "bounds": (0.35, 0.65),
               "step1": "half of caries experience is heritable - yet recalls ignore genetics entirely",
               "confirm": "integrated scores beat single-domain ones with stratified care cutting disease",
               "refute": "risk proves behavior-dominated regardless of biological stratification"},
},
# ------------------------------------------------------------------ rank 31
{
 "key": "nerve-repair-dental",
 "name": "Nerve Repair After Dental Nerve Injury",
 "group": "Neurosensory Dentistry",
 "ladder_rank": 31, "ladder_tier": "advanced",
 "problem": "Wisdom-tooth surgery and implants can damage the lingual or inferior alveolar nerve, leaving numbness or burning pain - why is recovery unpredictable, and can injured trigeminal nerves be repaired?",
 "description": "Iatrogenic trigeminal nerve injury - from third-molar extraction, implant placement, or endodontic overfill - causes anesthesia, paresthesia, or dysesthesia of lip, chin, or tongue. Most recover spontaneously; a minority suffer permanent deficit or neuropathic pain. Microsurgical repair (nerve grafting) helps selected cases if done early, but outcomes are variable and the window is debated.",
 "background": "Trigeminal nerve repair borrowed from peripheral-nerve microsurgery (Sunderland, Millesi). Case series show grafting can restore sensation when performed within months, but results are inconsistent and pain outcomes worse than sensory ones. The biology - why some injured nerves recover and others form painful neuromas - mirrors general nerve-regeneration problems with trigeminal specifics (the lingual nerve's anatomy, the inferior alveolar's bony canal). As of 2026 repair is an art practiced in few centers with unpredictable results.",
 "why_it_matters": "A numb lip or burning tongue after routine dental surgery devastates quality of life: eating, kissing, speaking altered permanently. Reliable repair would remove dentistry's most feared complication.",
 "sig_pointer": "The Signature system's proposed approach treats trigeminal repair as a timing-and-guidance problem, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that trigeminal repair outcomes hinge on two variables: intervention timing (before central changes lock in) and guidance quality (the bony canal constrains grafting). "
  "Assumptions: (1) central sensitization after trigeminal injury has a window; (2) the canal anatomy limits conventional grafting; (3) early, guided repair beats late repair. "
  "Reasoning path: a timing-guidance model explains outcome variability and predicts that early-intervention protocols with canal-specific techniques will outperform. "
  "Proposed mechanism: 'timed guided' trigeminal repair - early assessment protocols plus canal-adapted grafting - tested against sensory and pain outcomes. "
  "What would confirm it: early guided repair outperforming current practice in cohorts. "
  "What would kill it: evidence that outcomes are determined at injury regardless of repair, or that central changes are immediate. "
  "What this does not claim: it does not claim repair works reliably today, does not advise on nerve injuries, and does not constitute dental or medical advice."),
 "sig_lens": "The Signature lens reads the injured trigeminal nerve as a race against central lock-in, and asks what early guided repair would change.",
 "how_it_works": "Researchers study trigeminal repair through injury cohorts, microsurgical case series, neuroma biology, and timing-outcome analyses.",
 "key_points": [
  "Third-molar and implant surgery can injure lingual and inferior alveolar nerves.",
  "Most injuries recover; a minority cause permanent deficit or pain.",
  "Microsurgical grafting helps selected early cases inconsistently.",
  "The repair window and technique are debated.",
  "Few centers practice trigeminal microsurgery.",
 ],
 "requirements": [
  "Early-assessment protocols identifying repairable injuries.",
  "Canal-adapted grafting techniques proven in trials.",
  "Understanding of the central lock-in window.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Robinson PP et al. Trigeminal nerve injuries. Various; 2000-2015.",
  "Ziccardi VB, Zuniga JR. Nerve injuries after third molar removal. Oral and Maxillofacial Surgery Clinics. 2007;19(1):105-115.",
  "Bagheri SC et al. Microsurgical repair of the inferior alveolar nerve. Journal of Oral and Maxillofacial Surgery. 2010;68(11):2770-2777.",
  "Renton T et al. Trigeminal nerve injuries. Various; 2005-2020.",
 ],
 "demo_data": {"a": ("permanent trigeminal deficit after high-risk extractions, percent (approx)", 2.0),
               "b": ("percent scale", 100.0), "bounds": (0.005, 0.05),
               "step1": "a small percent suffer permanent numbness or pain - rare, devastating, unpredictable",
               "confirm": "early guided repair beats current practice on sensory and pain outcomes",
               "refute": "outcomes prove determined at injury regardless of repair timing"},
},
# ------------------------------------------------------------------ rank 32
{
 "key": "amelogenesis",
 "name": "Amelogenesis Imperfecta Treatments",
 "group": "Dental Genetics",
 "ladder_rank": 32, "ladder_tier": "advanced",
 "problem": "Children born with defective enamel face a lifetime of crowns - can the genetic enamel defects be treated biologically instead of prosthetically?",
 "description": "Amelogenesis imperfecta (AI) - genetic defects of enamel formation (AMELX, ENAM, MMP20, and other genes) - produces thin, soft, or absent enamel. Management is prosthetic: full-coverage crowns in childhood, repeated through life. The biology is well mapped but the therapy gap is total: no treatment addresses the genetic defect, and gene therapy for a developmental process that completes in childhood faces a narrow window.",
 "background": "AI genetics were mapped in the 2000s-2010s: X-linked (AMELX), autosomal dominant/recessive forms, with genotype-phenotype correlations. The developmental biology of amelogenesis (ameloblast life cycle, matrix processing) is among the best understood in dentistry. But translation stalls: enamel forms once, in childhood, so therapy must act during development - a gene-therapy window that is narrow and ethically complex. As of 2026 management remains prosthetic.",
 "why_it_matters": "AI condemns children to a lifetime of dental reconstruction starting in early childhood: biological treatment would spare them decades of prosthetics.",
 "sig_pointer": "The Signature system's proposed approach treats AI as a developmental window problem, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that AI therapy must act during the ameloblast window: the target is not the erupted tooth but the developing enamel organ, and the delivery challenge is reaching it in childhood. "
  "Assumptions: (1) the genetic defects are correctable in principle; (2) the ameloblast window is accessible; (3) partial correction suffices functionally. "
  "Reasoning path: a window model explains why adult gene therapy can't help (enamel is done) and focuses innovation on developmental delivery. "
  "Proposed mechanism: 'window-targeted' genetic correction delivered to the developing enamel organ, tested in models for enamel quality. "
  "What would confirm it: corrected enamel formation in AI models with functional quality. "
  "What would kill it: evidence that the window is inaccessible or that correction must be complete to matter. "
  "What this does not claim: it does not claim gene therapy is near, offers no treatment, and does not constitute dental or medical advice."),
 "sig_lens": "The Signature lens reads defective enamel as a missed developmental window, and asks what delivery would reach the ameloblasts in time.",
 "how_it_works": "Researchers study AI through genetics, ameloblast developmental biology, mouse models, and prosthetic management cohorts.",
 "key_points": [
  "AI genes mapped: AMELX, ENAM, MMP20, and others.",
  "Enamel forms once, in childhood - the therapeutic window is narrow.",
  "Management is lifelong prosthetic reconstruction.",
  "Ameloblast developmental biology is well understood.",
  "No biological therapy addresses the genetic defect.",
 ],
 "requirements": [
  "Delivery to the developing enamel organ in childhood.",
  "Proof of functional enamel correction in models.",
  "Ethical frameworks for developmental gene therapy.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Wright JT et al. Amelogenesis imperfecta: genotype-phenotype studies. Various; 2000-2015.",
  "Lacruz RS et al. Dental enamel formation. Various; 2010-2017.",
  "Smith CEL et al. Amelogenesis imperfecta genetics. Various; 2017-2022.",
  "Hu JCC et al. Enamel formation genetics. Various; 2005-2015.",
 ],
 "demo_data": {"a": ("AI prevalence, per 14,000 (approx midpoint)", 14000.0),
               "b": ("people per 14,000 (scale)", 14000.0), "bounds": (0.9, 1.1),
               "step1": "amelogenesis imperfecta is rare per person but lifelong per patient - decades of crowns",
               "confirm": "window-targeted correction yields functional enamel in AI models",
               "refute": "the developmental window proves inaccessible to therapy"},
},
# ------------------------------------------------------------------ rank 33
{
 "key": "cleft-protocols",
 "name": "Cleft Lip and Palate: Optimal Protocols",
 "group": "Craniofacial Surgery",
 "ladder_rank": 33, "ladder_tier": "advanced",
 "problem": "Cleft repair timing, technique, and sequencing vary worldwide - what is the optimal protocol, and why hasn't one been proven?",
 "description": "Cleft lip and palate - among the commonest birth defects - requires years of coordinated care: lip repair, palate repair, speech therapy, orthodontics, bone grafting. Protocols vary enormously: lip repair at 3 months versus neonatal, palate at 6 versus 12 months, one-stage versus two-stage. The evidence is weak because randomization is hard, outcomes take decades (facial growth, speech), and centers defend their traditions.",
 "background": "Cleft care protocols evolved by center tradition (Eurocleft, Americleft studies documented the variation). The timing debates: early palate repair helps speech but may restrict facial growth; late repair reverses the trade-off. Scandcleft randomized trials provided rare high-quality evidence on surgical technique. As of 2026 no optimal protocol is proven; care remains center-tradition-driven with decades-long outcome horizons.",
 "why_it_matters": "Cleft children live with the consequences of protocol choices for life: speech, appearance, hearing, and psychosocial outcomes all hang on decisions made in infancy. An optimal protocol would standardize the best start in life.",
 "sig_pointer": "The Signature system's proposed approach treats protocol optimization as a long-horizon learning problem, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that cleft protocol optimization fails on the outcome horizon: choices made in infancy pay off over decades, defeating conventional trials. "
  "Assumptions: (1) protocol differences have real long-term effects; (2) intermediate markers (growth trajectories, speech milestones) predict final outcomes; (3) registry learning can substitute for decades-long trials. "
  "Reasoning path: a horizon model explains the evidence vacuum and predicts that marker-validated registry learning will optimize protocols faster than trials. "
  "Proposed mechanism: 'horizon-bridged' optimization - international registries with validated intermediate markers, iteratively refining protocols. "
  "What would confirm it: registry-optimized protocols outperforming traditional ones on long-term outcomes. "
  "What would kill it: evidence that intermediate markers don't predict final outcomes, or that center effects dominate protocols. "
  "What this does not claim: it does not claim any protocol is optimal today, does not advise on cleft care, and does not constitute dental or medical advice."),
 "sig_lens": "The Signature lens reads cleft protocols as traditions awaiting long-horizon proof, and asks what markers would bridge the decades.",
 "how_it_works": "Cleft researchers study protocols through center comparisons (Eurocleft/Americleft), Scandcleft trials, growth and speech outcome cohorts, and registries.",
 "key_points": [
  "Cleft lip/palate is among the commonest birth defects.",
  "Protocols vary by center tradition: timing, technique, sequencing.",
  "Early palate repair helps speech but may restrict growth.",
  "Scandcleft provided rare randomized evidence.",
  "Outcomes take decades; no optimal protocol is proven.",
 ],
 "requirements": [
  "Validated intermediate markers bridging to long-term outcomes.",
  "International registry learning at scale.",
  "Proof that optimized protocols beat traditional ones.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Shaw WC et al. The Eurocleft study. Various; 2000-2005.",
  "Long RE et al. The Americleft study. Various; 2011-2017.",
  "Rautio J et al. Scandcleft randomised trials. Journal of Plastic Surgery and Hand Surgery. 2017;51(1):1-10.",
  "Mossey PA et al. Cleft lip and palate. Lancet. 2009;374:1773-1785.",
 ],
 "demo_data": {"a": ("cleft births, per 700 (approx)", 700.0),
               "b": ("births per 700 (scale)", 700.0), "bounds": (0.9, 1.1),
               "step1": "about one in seven hundred babies is born with a cleft - each entering a protocol lottery",
               "confirm": "registry-optimized protocols beat traditional ones on long-term outcomes",
               "refute": "intermediate markers prove unable to predict final outcomes"},
},
# ------------------------------------------------------------------ rank 34
{
 "key": "dental-fear-scale",
 "name": "Eliminating Dental Fear at Population Scale",
 "group": "Behavioral Dentistry",
 "ladder_rank": 34, "ladder_tier": "advanced",
 "problem": "We know how to treat dental anxiety in individuals - so why does population dental fear never decline, and what would move it?",
 "description": "Dental fear is stable or rising at population level despite effective individual treatments (CBT) and better anesthesia. The population drivers - cultural narratives, media portrayals, intergenerational transmission, and the reality that dental care still sometimes hurts - operate above the individual. No public-health campaign has moved dental fear; the field treats the fearful one by one while the population replenishes them.",
 "background": "Population dental-fear surveillance (Australia's Armfield, UK Adult Dental Health Surveys) shows stability across decades. Intergenerational transmission is documented: fearful parents raise fearful children. Media portrayals remain negative. The paradox: dentistry is objectively less painful than ever, yet fear persists - suggesting the drivers are cultural and narrative, not experiential. As of 2026 no population-level intervention has reduced dental fear.",
 "why_it_matters": "Population fear is the upstream of the vicious cycle: it fills emergency rooms with preventable dental agony and concentrates disease in the fearful. Moving it would be public health's cheapest oral-health win.",
 "sig_pointer": "The Signature system's proposed approach treats dental fear as a cultural narrative to be rewritten, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that population dental fear is a narrative problem: the cultural story of dentistry (pain, helplessness) transmits across generations faster than individual treatment can counter it. "
  "Assumptions: (1) narratives drive population fear more than experience; (2) narratives are rewritable through media, education, and care experience; (3) the rewrite must reach children before transmission. "
  "Reasoning path: a narrative model explains the individual-treatment/population-stability paradox and predicts that narrative interventions will move population fear where CBT cannot scale. "
  "Proposed mechanism: 'narrative rewriting' - coordinated media, school, and care-experience interventions targeting the cultural story, tested against population fear surveillance. "
  "What would confirm it: population fear declining in intervention regions versus controls. "
  "What would kill it: evidence that fear is experientially determined regardless of narrative, or that narratives resist intervention. "
  "What this does not claim: it does not claim a campaign exists, does not blame media, and does not constitute dental or psychological advice."),
 "sig_lens": "The Signature lens reads population fear as a story retold across generations, and asks what new story would replace it.",
 "how_it_works": "Researchers study population fear through surveillance surveys, intergenerational transmission studies, media-content analyses, and narrative intervention trials.",
 "key_points": [
  "Population dental fear is stable across decades despite better anesthesia.",
  "Fear transmits intergenerationally: fearful parents, fearful children.",
  "Media portrayals of dentistry remain negative.",
  "Individual CBT works but can't scale to populations.",
  "No population-level intervention has reduced dental fear.",
 ],
 "requirements": [
  "Narrative interventions proven against population surveillance.",
  "Childhood-targeted prevention of transmission.",
  "Care experiences that confirm the new narrative.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Armfield JM. Population dental fear surveillance. Various; 2008-2013.",
  "Milgrom P et al. Dental fear transmission. Various; 1988-2010.",
  "UK Adult Dental Health Survey. Various years.",
  "Beaton L et al. The impact of media on dental fear. Various; 2010-2020.",
 ],
 "demo_data": {"a": ("decades of stable population dental fear (approx)", 4.0),
               "b": ("effective individual treatments available (CBT, anesthesia advances)", 2.0), "bounds": (1.5, 3.0),
               "step1": "decades of stable fear despite effective treatments - the population problem is not the individual problem",
               "confirm": "narrative interventions cut population fear in intervention regions",
               "refute": "fear proves experientially determined regardless of narrative"},
},
]


