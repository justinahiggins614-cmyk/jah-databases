#!/usr/bin/env python3
"""Entries for The Unsolved Veterinary Medicine Database (unsolved-veterinary-medicine)
and its Signature half (unsolved-veterinary-medicine-signature).

34 famous unsolved problems in veterinary medicine, ladder-ordered by accessibility
(rank 1 = most approachable, rank 34 = most complex/compounded).
Public half: real, fact-checked problems. Signature half: the same 34
problems through the Signature lens, with Signature-generated proposed
solutions that are ALWAYS labeled as proposals, never established science.

Honesty rule (enforced in every record): never claim proof, never imply
peer acceptance, never present speculation as settled. Signature proposals
are labeled speculation for research discussion only - never veterinary advice,
never a treatment recommendation, no cure claims.
"""

LABEL = "Signature-generated proposed solution \u2014 not established science."

SIG_TAIL = ("Signature editions carry the Signature system's proposed "
            "solution approaches to famous unsolved problems. Every "
            "solution is labeled a Signature-generated proposal, never "
            "established science, never peer-accepted, never proof, never "
            "veterinary advice.")

STD_COMMON = [
    "Problem statements verified against the published veterinary literature; open status confirmed as of 2026.",
    "Signature solution sections are labeled proposals: they state assumptions, a reasoning path, a proposed mechanism, what would confirm or kill them, and what they do not claim.",
    "Signature proposals are labeled speculation for research discussion only - never veterinary advice, never a treatment recommendation; no cure claims appear.",
]

ENTRIES = [
# ------------------------------------------------------------------ rank 1
{
 "key": "breed-cancer",
 "name": "Why Some Dog Breeds Are Cancer-Prone",
 "group": "Genetics",
 "ladder_rank": 1, "ladder_tier": "foundations",
 "problem": "A Bernese Mountain Dog is far likelier to die of cancer than a mixed-breed - what genetic architecture makes entire breeds cancer-prone?",
 "description": "Cancer is the leading cause of death in many dog breeds: Bernese Mountain Dogs (histiocytic sarcoma), Boxers, Golden Retrievers (hemangiosarcoma, lymphoma), Scottish Terriers (bladder cancer) face breed-specific risks an order of magnitude above average. Centuries of inbreeding concentrated both desired traits and disease alleles. The genetic architecture - which loci, how they interact - is mapped only in fragments.",
 "background": "Breed-specific cancer risk was quantified epidemiologically in the 1990s-2000s (Dobson; Adams' UK breed mortality survey, 2010). The canine genome (Lindblad-Toh, 2005) enabled mapping: loci for histiocytic sarcoma in Bernese (Shearin 2012), bladder cancer risk in Scotties, osteosarcoma regions in Greyhounds and Rottweilers. But most breed risks remain unmapped, the alleles found explain fractions of risk, and breeding away from cancer without losing breed identity is unproven. As of 2026 the genetic architecture of breed cancer risk is fragmentary.",
 "why_it_matters": "Dogs are humans' cancer model and companion: breed cancer kills beloved animals young and offers a genetic shortcut to human cancer biology. Mapping breed risk would enable screening, breeding reform, and comparative oncology breakthroughs.",
 "sig_pointer": "The Signature system's proposed approach maps breed risk as concentrated haplotype blocks, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that breed cancer risk lives in long haplotype blocks fixed by inbreeding: the same selective sweeps that made the breed also fixed cancer alleles, and the blocks are mappable by comparing affected breeds. "
  "Assumptions: (1) risk alleles hitchhiked with selected traits; (2) affected breeds share risk haplotypes; (3) the blocks are identifiable by cross-breed comparison. "
  "Reasoning path: a hitchhiking model explains breed-specificity and predicts that mapping across breeds will find shared risk blocks faster than within-breed GWAS. "
  "Proposed mechanism: 'sweep-mapped' risk panels - haplotype blocks associated with breed cancers - used for screening and breeding decisions. "
  "What would confirm it: cross-breed mapping finding shared risk blocks that predict cancer in validation cohorts. "
  "What would kill it: evidence that breed risk is polygenic background rather than mappable blocks, defeating panel approaches. "
  "What this does not claim: it does not claim a test exists, does not advise on breeding, and does not constitute veterinary advice."),
 "sig_lens": "The Signature lens reads the breed's cancer as the price of its pedigree, and asks which hitchhiking blocks carry the bill.",
 "how_it_works": "Veterinary geneticists study breed cancer through mortality surveys, GWAS within and across breeds, haplotype mapping, and comparative oncology.",
 "key_points": [
  "Cancer leads mortality in many breeds; breed risks exceed average by multiples.",
  "Bernese (histiocytic sarcoma), Goldens (hemangiosarcoma), Scotties (bladder) are extremes.",
  "The canine genome (2005) enabled risk mapping.",
  "Found loci explain fractions of breed risk.",
  "Breeding away from cancer without losing breed identity is unproven.",
 ],
 "requirements": [
  "Cross-breed mapping of shared risk haplotypes.",
  "Validated risk panels predicting individual cancer risk.",
  "Breeding strategies reducing risk while preserving breeds.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Adams VJ et al. Results of a survey of UK purebred dogs. Journal of Small Animal Practice. 2010;51(10):512-521.",
  "Lindblad-Toh K et al. Genome sequence, comparative analysis and haplotype structure of the domestic dog. Nature. 2005;438:803-819.",
  "Shearin AL et al. The MTAP-CDKN2A locus confers susceptibility to histiocytic sarcoma in Bernese Mountain Dogs. PLoS One. 2012;7(1):e29950.",
  "Dobson JM. Breed-predispositions to cancer in pedigree dogs. ISRN Veterinary Science. 2013;2013:941275.",
 ],
 "demo_data": {"a": ("Bernese Mountain Dog cancer mortality, percent (approx)", 50.0),
               "b": ("percent scale", 100.0), "bounds": (0.35, 0.65),
               "step1": "half of Bernese Mountain Dogs die of cancer - breed concentrated risk at its extreme",
               "confirm": "cross-breed mapping finds shared risk blocks predicting cancer in validation",
               "refute": "breed risk proves polygenic background defeating haplotype panels"},
},
# ------------------------------------------------------------------ rank 2
{
 "key": "feline-ckd",
 "name": "Feline Chronic Kidney Disease: The Missing Cause",
 "group": "Feline Medicine",
 "ladder_rank": 2, "ladder_tier": "foundations",
 "problem": "A huge fraction of old cats die with failing kidneys - but what actually causes feline chronic kidney disease?",
 "description": "Chronic kidney disease affects roughly a third of geriatric cats and is a leading cause of death. Yet its etiology is unknown: unlike dogs (often glomerular) or humans (diabetic/hypertensive), feline CKD is typically tubulointerstitial with no identified trigger. Theories include chronic pyelonephritis, dental-disease bacteremia, diet, genetics, and environmental nephrotoxins - none proven.",
 "background": "Feline CKD was characterized clinically in the late 20th century; IRIS staging (2006) standardized it. The cause hunt cycled: infectious theories (feline morbillivirus was proposed in 2012, then largely discounted), dental-disease links (associational), diet (phosphorus, protein debates), and breed predispositions (Persians, Abyssinians suggesting genetics). Early-detection markers (SDMA, 2015) improved diagnosis without illuminating cause. As of 2026 the etiology remains unknown and treatment is supportive.",
 "why_it_matters": "CKD kills a third of old cats slowly: weight loss, nausea, suffering over months to years. Finding the cause would convert palliative management into prevention - the largest therapeutic prize in feline medicine.",
 "sig_pointer": "The Signature system's proposed approach treats feline CKD as a lifetime exposure disease, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that feline CKD is a cumulative-exposure disease: decades of low-grade insults (subclinical infections, dietary phosphorus, environmental toxins) accrete until the kidney's reserve is spent. "
  "Assumptions: (1) no single cause dominates; (2) the insults are individually subclinical; (3) lifetime exposure is measurable retrospectively. "
  "Reasoning path: an accretion model explains the age distribution, the tubulointerstitial pattern, and why single-cause hunts fail - and predicts that exposure-reduction will prevent disease. "
  "Proposed mechanism: 'exposome' studies of cats - lifetime diet, environment, infection history - identifying the accreting insults for targeted prevention. "
  "What would confirm it: exposome studies finding exposure burdens predicting CKD, with reduction trials preventing it. "
  "What would kill it: evidence of a single dominant cause after all, or that exposures don't predict disease. "
  "What this does not claim: it does not claim a cause is known, does not advise on diet, and does not constitute veterinary advice."),
 "sig_lens": "The Signature lens reads the failing feline kidney as a ledger of lifetime insults, and asks which entries add up to disease.",
 "how_it_works": "Feline researchers study CKD through IRIS-staged cohorts, biomarker studies (SDMA), renal biopsy series, and exposure-association research.",
 "key_points": [
  "CKD affects ~a third of geriatric cats.",
  "Feline CKD is typically tubulointerstitial with unknown trigger.",
  "Feline morbillivirus was proposed (2012) then largely discounted.",
  "IRIS staging (2006) and SDMA (2015) improved management, not etiology.",
  "Treatment remains supportive: diet, fluids, phosphorus control.",
 ],
 "requirements": [
  "Lifetime exposome studies identifying accreting insults.",
  "Proof that exposure reduction prevents CKD.",
  "Early causal markers, not just damage markers.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "International Renal Interest Society. IRIS staging of CKD. 2006 (updated).",
  "Hall JA et al. Serum symmetric dimethylarginine (SDMA). Various; 2014-2016.",
  "Woo PCY et al. Feline morbillivirus. PNAS. 2012;109(14):5435-5440.",
  "Brown SA et al. Feline chronic kidney disease. Various reviews; 2010-2020.",
 ],
 "demo_data": {"a": ("geriatric cats with CKD, percent (approx)", 33.0),
               "b": ("percent scale", 100.0), "bounds": (0.25, 0.45),
               "step1": "a third of old cats develop kidney disease with no known cause - medicine's largest feline mystery",
               "confirm": "exposome studies find exposure burdens predicting CKD with reduction preventing it",
               "refute": "a single dominant cause emerges or exposures prove non-predictive"},
},
# ------------------------------------------------------------------ rank 3
{
 "key": "equine-laminitis",
 "name": "Equine Laminitis Mechanism",
 "group": "Equine Medicine",
 "ladder_rank": 3, "ladder_tier": "foundations",
 "problem": "A horse eats too much grain and its hooves can fall apart from the inside - what is the actual mechanism of laminitis?",
 "description": "Laminitis - inflammation and failure of the lamellar attachment between hoof wall and coffin bone - is among the most dreaded equine diseases: the bone can rotate or sink through the sole, and severe cases end in euthanasia. It follows grain overload, endotoxemia, equine metabolic syndrome, and supporting-limb overload. But the mechanistic chain from trigger to lamellar failure remains contested after decades of research.",
 "background": "Theories cycled: vascular (ischemia-reperfusion), enzymatic (matrix metalloproteinases digesting the lamellae), inflammatory, and metabolic (insulin dysregulation - the endocrinopathic laminitis model, validated by de Laat's insulin-infusion work showing hyperinsulinemia alone induces laminitis). Each trigger may use a different pathway, or converge on one. Treatments - cryotherapy, vasodilators, anti-inflammatories, mechanical support - are supportive. As of 2026 no unifying mechanism is proven and no targeted therapy exists.",
 "why_it_matters": "Laminitis kills and cripples horses across disciplines: founders end careers and lives. A mechanism would convert supportive care into targeted prevention - the holy grail of equine podiatry.",
 "sig_pointer": "The Signature system's proposed approach treats laminitis as convergent lamellar failure with trigger-specific entries, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that laminitis is several diseases converging on lamellar failure: endocrinopathic, septic, and mechanical triggers enter through different doors but break the same attachment. "
  "Assumptions: (1) the lamellar attachment has multiple failure modes; (2) triggers map to modes; (3) mode-specific prevention works where generic therapy fails. "
  "Reasoning path: a convergence model explains the theory wars - each camp studied a different trigger - and predicts trigger-mapped prevention. "
  "Proposed mechanism: 'trigger-mapped' laminitis care - classifying risk by trigger pathway (insulin, inflammatory, mechanical) with pathway-specific prevention. "
  "What would confirm it: pathway-specific prevention outperforming generic care in trials, with lamellar biomarkers tracking each pathway. "
  "What would kill it: evidence of a single final common pathway making trigger-mapping moot. "
  "What this does not claim: it does not claim a treatment exists, does not advise on management, and does not constitute veterinary advice."),
 "sig_lens": "The Signature lens reads the failing hoof as several roads to one collapse, and asks which road each horse is on.",
 "how_it_works": "Equine researchers study laminitis through experimental induction models, lamellar biology, insulin-dynamics research, and support-therapy trials.",
 "key_points": [
  "Laminitis can rotate or sink the coffin bone through the sole.",
  "Triggers: grain overload, endotoxemia, metabolic syndrome, limb overload.",
  "Hyperinsulinemia alone can induce laminitis (de Laat).",
  "Theories (vascular, enzymatic, inflammatory, metabolic) remain contested.",
  "Treatment is supportive; no targeted therapy exists.",
 ],
 "requirements": [
  "Trigger-to-failure-mode mapping validated biologically.",
  "Pathway-specific prevention proven in trials.",
  "Early lamellar-distress markers before structural failure.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "de Laat MA et al. Hyperinsulinemia causes laminitis. Various; 2010-2013.",
  "Pollitt CC. Equine laminitis: a review. Various; 1996-2008.",
  "Katz LM, Bailey SR. A review of recent advances and current hypotheses on the pathogenesis of acute laminitis. Equine Veterinary Journal. 2012;44(6):752-761.",
  "van Eps AW, Pollitt CC. Equine laminitis: cryotherapy. Various; 2004-2009.",
 ],
 "demo_data": {"a": ("laminitis cases ending in euthanasia, percent severe (approx)", 25.0),
               "b": ("percent scale", 100.0), "bounds": (0.15, 0.4),
               "step1": "a quarter of severe cases end in euthanasia - the hoof's failure is the horse's death sentence",
               "confirm": "pathway-specific prevention beats generic care with biomarkers tracking pathways",
               "refute": "a single final common pathway emerges making trigger-mapping moot"},
},
# ------------------------------------------------------------------ rank 4
{
 "key": "hip-dysplasia",
 "name": "Canine Hip Dysplasia Prevention",
 "group": "Orthopedics",
 "ladder_rank": 4, "ladder_tier": "foundations",
 "problem": "Hip dysplasia cripples large-breed dogs - why can't breeding programs eliminate it, and what would prevention actually require?",
 "description": "Canine hip dysplasia - malformation of the hip joint causing laxity, arthritis, and pain - is polygenic and common in large breeds. Decades of radiographic screening (OFA, PennHIP, BVA) and selective breeding reduced prevalence modestly but never eliminated it. The genetics are complex, the environmental modifiers (growth rate, nutrition, exercise) matter, and the phenotype takes months to assess.",
 "background": "Hip dysplasia was characterized in the 1930s-60s; screening programs began in the 1960s-70s (OFA 1966). PennHIP's distraction index (Smith, 1990s) improved phenotype measurement. Genomic studies found associated loci with small effects - the trait is highly polygenic. Breeding programs using estimated breeding values (as in some European programs) outperform phenotype-only selection. But progress is slow: generation intervals are years, popular sires spread risk alleles, and the phenotype's heritability (~0.3-0.5) limits selection response. As of 2026 dysplasia persists in every large breed.",
 "why_it_matters": "Hip dysplasia causes lifelong pain and disability in millions of dogs and drives expensive surgeries (total hip replacement, FHO). Eliminating it would be the largest welfare win in canine orthopedics.",
 "sig_pointer": "The Signature system's proposed approach combines genomic selection with developmental management, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that dysplasia elimination needs two levers together: genomic selection (breeding values, not just phenotypes) and developmental management (growth rate, nutrition, exercise in puppyhood). "
  "Assumptions: (1) the trait is polygenic but selectable; (2) development modifies genetic risk substantially; (3) the levers are multiplicative. "
  "Reasoning path: a two-lever model explains slow progress - programs pull one lever - and predicts combined programs will outperform. "
  "Proposed mechanism: 'dual-lever' dysplasia programs - genomic breeding values plus standardized developmental protocols - tested against dysplasia prevalence. "
  "What would confirm it: dual-lever programs reducing prevalence faster than selection-only programs. "
  "What would kill it: evidence that environmental modification adds nothing to genomic selection, or that the trait resists selection regardless. "
  "What this does not claim: it does not claim dysplasia is eliminable today, does not advise on breeding, and does not constitute veterinary advice."),
 "sig_lens": "The Signature lens reads the dysplastic hip as genes plus growth, and asks what combined program would straighten both.",
 "how_it_works": "Orthopedic researchers study dysplasia through screening programs, genomic association, growth-rate trials, and breeding-value analyses.",
 "key_points": [
  "Hip dysplasia is polygenic with heritability ~0.3-0.5.",
  "OFA (1966) and PennHIP (1990s) standardized screening.",
  "Selective breeding reduced prevalence modestly over decades.",
  "Estimated breeding values outperform phenotype-only selection.",
  "Popular sires and long generations slow progress.",
 ],
 "requirements": [
  "Genomic breeding values adopted across major programs.",
  "Developmental protocols proven to modify risk.",
  "Proof that dual-lever programs accelerate elimination.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Smith GK et al. Coxofemoral joint laxity from distraction radiography (PennHIP). Various; 1990-2001.",
  "Orthopedic Foundation for Animals. Hip dysplasia database. 1966 onward.",
  "Malm S et al. Estimated breeding values for hip dysplasia. Various; 2008-2013.",
  "Lewis TW et al. Genetic evaluation of hip score. Various; 2010-2013.",
 ],
 "demo_data": {"a": ("decades of selective breeding against dysplasia", 6.0),
               "b": ("decades scale", 10.0), "bounds": (0.4, 0.8),
               "step1": "six decades of selection, dysplasia persists in every large breed - one lever is not enough",
               "confirm": "dual-lever programs beat selection-only programs on prevalence reduction",
               "refute": "developmental management proves to add nothing to genomic selection"},
},
# ------------------------------------------------------------------ rank 5
{
 "key": "livestock-amr",
 "name": "Antimicrobial Resistance in Livestock",
 "group": "Population Medicine",
 "ladder_rank": 5, "ladder_tier": "foundations",
 "problem": "Farm antibiotic use breeds resistance that reaches humans - how much livestock use is truly necessary, and what replaces growth promotion?",
 "description": "Antimicrobials in livestock - for treatment, prevention, and (historically) growth promotion - select resistant bacteria that reach humans through food, environment, and workers. The EU banned growth promoters in 2006; the US restricted them in 2017. But therapeutic and preventive mass medication continues, alternatives (vaccines, biosecurity, husbandry) are incompletely adopted, and the resistance burden attributable to livestock versus human medicine remains contested.",
 "background": "The Swann report (1969, UK) first flagged farm antibiotic risks; decades of debate followed. Denmark's DANMAP surveillance (1995 onward) showed bans could work without production collapse. The mcr-1 colistin-resistance gene (Liu 2016, from Chinese pigs) proved last-resort resistance moves through livestock. Alternatives - improved biosecurity, vaccination, reduced stocking density - show promise but cost more. As of 2026 the necessary-versus-replaceable use boundary is still drawn by economics more than evidence.",
 "why_it_matters": "Antimicrobial resistance kills over a million yearly; livestock is a major driver. Rationalizing farm use is among the highest-leverage resistance interventions available - and a One Health test case.",
 "sig_pointer": "The Signature system's proposed approach separates necessary from replaceable use with alternatives matched per indication, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that livestock antimicrobial use divides into necessary (individual treatment), replaceable (mass prevention with alternatives), and legacy (growth promotion) - and that policy fails by treating them as one. "
  "Assumptions: (1) the categories have different resistance costs and replacement options; (2) alternatives exist for most mass use; (3) the economics can be restructured. "
  "Reasoning path: a category model explains why blanket bans work partially (they hit legacy use) and predicts targeted replacement will cut the rest. "
  "Proposed mechanism: 'category-targeted' reduction - alternatives matched per use category, with resistance surveillance verifying the effect. "
  "What would confirm it: targeted programs cutting resistance without production loss in trials. "
  "What would kill it: evidence that alternatives can't match antimicrobials for mass prevention, or that resistance is dominated by human use. "
  "What this does not claim: it does not claim any use is currently unnecessary, takes no policy position, and does not constitute veterinary advice."),
 "sig_lens": "The Signature lens reads farm antibiotics as three different uses wearing one prescription, and asks what would replace each.",
 "how_it_works": "Researchers study livestock AMR through surveillance (DANMAP, NARMS), use-reduction trials, alternative-intervention studies, and resistance-attribution modeling.",
 "key_points": [
  "The Swann report (1969) first flagged farm antibiotic risks.",
  "The EU banned growth promoters in 2006; the US restricted them in 2017.",
  "mcr-1 colistin resistance emerged from livestock (2016).",
  "Denmark showed bans need not collapse production.",
  "The necessary-versus-replaceable boundary is drawn by economics.",
 ],
 "requirements": [
  "Category-specific alternatives proven at scale.",
  "Resistance surveillance linking use to human health outcomes.",
  "Economic models making alternatives competitive.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Swann MM et al. Report of the Joint Committee on the Use of Antibiotics in Animal Husbandry. HMSO; 1969.",
  "Liu YY et al. Emergence of plasmid-mediated colistin resistance mechanism MCR-1. Lancet Infectious Diseases. 2016;16(2):161-168.",
  "DANMAP. Danish Integrated Antimicrobial Resistance Monitoring and Research Programme. 1995 onward.",
  "World Health Organization. Global action plan on antimicrobial resistance. 2015.",
 ],
 "demo_data": {"a": ("AMR deaths yearly, millions (approx)", 1.3),
               "b": ("deaths scale, millions", 10.0), "bounds": (0.08, 0.2),
               "step1": "resistance kills over a million yearly - livestock use is a major, modifiable driver",
               "confirm": "targeted programs cut resistance without production loss",
               "refute": "alternatives prove unable to match antimicrobials for mass prevention"},
},
# ------------------------------------------------------------------ rank 6
{
 "key": "mastitis",
 "name": "Mastitis in Dairy Cattle",
 "group": "Production Medicine",
 "ladder_rank": 6, "ladder_tier": "foundations",
 "problem": "Mastitis is the costliest dairy disease - why can't it be prevented, and what would end it?",
 "description": "Bovine mastitis - udder inflammation, usually bacterial - costs the dairy industry billions yearly in lost milk, treatment, and culling. Contagious (Staph. aureus, Strep. agalactiae) and environmental (E. coli, Strep. uberis) forms need different control. Five-point plans (teat disinfection, dry-cow therapy, culling, milking hygiene, equipment maintenance) cut contagious mastitis dramatically; environmental mastitis resists control.",
 "background": "The five-point plan (Neave, 1960s-70s, UK) tamed contagious mastitis. But environmental pathogens - living in bedding and manure - can't be eradicated by hygiene alone. Dry-cow therapy (blanket versus selective) is now contested on stewardship grounds. Vaccines show partial efficacy. Genetic selection for mastitis resistance (somatic cell score) progresses slowly. As of 2026 environmental mastitis remains the unsolved core.",
 "why_it_matters": "Mastitis is the dairy industry's largest disease cost and a major antibiotic-use driver: solving it would improve animal welfare, farm economics, and milk safety simultaneously.",
 "sig_pointer": "The Signature system's proposed approach treats environmental mastitis as an exposure-management problem, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that environmental mastitis is an exposure-dose disease: the udder's defenses handle background exposure but fail above a threshold, and control means managing the dose, not sterilizing the environment. "
  "Assumptions: (1) exposure dose predicts infection risk; (2) the dose is manageable through bedding, housing, and milking design; (3) host resistance is the second lever. "
  "Reasoning path: a dose model explains why hygiene helps but plateaus and predicts that exposure-engineered environments plus genetic resistance will outperform. "
  "Proposed mechanism: 'exposure-engineered' dairy environments with monitored bacterial loads, plus selection for resistance, tested against mastitis incidence. "
  "What would confirm it: engineered environments beating standard hygiene on environmental mastitis in trials. "
  "What would kill it: evidence that exposure dose doesn't predict infection, or that host factors dominate entirely. "
  "What this does not claim: it does not claim a protocol exists, does not advise on therapy, and does not constitute veterinary advice."),
 "sig_lens": "The Signature lens reads the infected udder as overwhelmed defenses, and asks what exposure level the defenses could handle.",
 "how_it_works": "Dairy researchers study mastitis through pathogen surveillance, bedding trials, dry-cow therapy comparisons, vaccine studies, and genetic selection.",
 "key_points": [
  "Mastitis is the costliest dairy disease, billions yearly.",
  "The five-point plan tamed contagious mastitis.",
  "Environmental mastitis resists hygiene-based control.",
  "Blanket dry-cow therapy faces stewardship pressure.",
  "Genetic selection for resistance progresses slowly.",
 ],
 "requirements": [
  "Exposure-dose thresholds validated prospectively.",
  "Environments engineered below the threshold.",
  "Selective dry-cow therapy proven safe.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Neave FK et al. Control of mastitis in the dairy herd by hygiene and management. Journal of Dairy Science. 1969;52:696-707.",
  "Halasa T et al. Economic effects of bovine mastitis. Veterinary Quarterly. 2007;29(1):18-31.",
  "Ruegg PL. A 100-year review: mastitis detection, management, and prevention. Journal of Dairy Science. 2017;100(12):10381-10397.",
  "Bradley AJ. Bovine mastitis: an evolving disease. Veterinary Journal. 2002;164(2):116-128.",
 ],
 "demo_data": {"a": ("dairy disease costs from mastitis, share (approx leading)", 1.0),
               "b": ("disease cost rank scale (first of many)", 3.0), "bounds": (0.2, 0.5),
               "step1": "mastitis leads dairy disease costs - the industry's most expensive unsolved problem",
               "confirm": "engineered environments beat standard hygiene on environmental mastitis",
               "refute": "exposure dose proves non-predictive with host factors dominating"},
},
# ------------------------------------------------------------------ rank 7
{
 "key": "equine-colic",
 "name": "Colic Prediction in Horses",
 "group": "Equine Medicine",
 "ladder_rank": 7, "ladder_tier": "foundations",
 "problem": "Colic kills horses suddenly - why can't the surgical case be distinguished from the medical one early, and what predicts the outcome?",
 "description": "Colic - abdominal pain in horses, usually gastrointestinal - ranges from mild gas to strangulating lesions needing emergency surgery. The critical decision (operate now versus treat medically) must be made early, but the signs overlap: pain scores, heart rate, reflux, and ultrasound help yet misclassify. Delayed surgery kills; unnecessary surgery risks.",
 "background": "Colic decision-making was systematized in the late 20th century (White, Mair): pain assessment, cardiovascular parameters, nasogastric reflux, rectal and ultrasound findings. Biomarkers (lactate, SAA) refined prognosis. But the early strangulating lesion still hides among medical colics, and referral decisions depend on clinician experience as much as protocol. As of 2026 no test reliably separates surgical from medical colic in the first hours.",
 "why_it_matters": "Colic is the leading killer of horses after old age: every hour of delayed surgery worsens strangulation outcomes. Reliable early triage would save horses that currently die waiting.",
 "sig_pointer": "The Signature system's proposed approach treats colic triage as a trajectory problem, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that single-timepoint colic assessment misses the signal: strangulating lesions declare themselves in trajectories (rising lactate, worsening pain despite analgesia), not snapshots. "
  "Assumptions: (1) surgical lesions have characteristic trajectories; (2) trajectories are detectable within the decision window; (3) serial assessment beats single assessment. "
  "Reasoning path: a trajectory model explains why experienced clinicians outperform protocols - they read trends - and predicts formalized trajectory monitoring will work. "
  "Proposed mechanism: 'trajectory triage' - standardized serial assessment with trend-based surgical triggers, tested against time-to-surgery and survival. "
  "What would confirm it: trajectory protocols beating single-assessment protocols on surgical timing and survival. "
  "What would kill it: evidence that trajectories don't separate within the window, or that serial assessment delays decisions. "
  "What this does not claim: it does not claim a triage tool exists, does not advise on colic, and does not constitute veterinary advice."),
 "sig_lens": "The Signature lens reads the colicky horse as a trajectory, not a snapshot, and asks what trend would declare surgery.",
 "how_it_works": "Equine clinicians study colic through surgical-versus-medical cohorts, biomarker validation, pain-scale research, and referral-timing analyses.",
 "key_points": [
  "Colic is the leading killer of horses after old age.",
  "Surgical-versus-medical triage must happen early; signs overlap.",
  "Lactate and SAA refined prognosis without solving triage.",
  "Experienced clinicians outperform protocols by reading trends.",
  "Delayed surgery for strangulation is often fatal.",
 ],
 "requirements": [
  "Trajectory-based triggers validated prospectively.",
  "Proof of faster correct triage without excess surgery.",
  "Field-usable monitoring for the critical first hours.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "White NA. Epidemiology and etiology of colic. Various; 1990-2006.",
  "Mair TS et al. Decision making in colic. Various; 2002-2016.",
  "Johnston JK et al. Prognostic indicators in colic. Various; 2007-2015.",
  "Curtis L et al. Systematic review of risk factors for colic. Equine Veterinary Journal. 2015;47(6):715-722.",
 ],
 "demo_data": {"a": ("colic surgeries with strangulating lesions, percent (approx)", 15.0),
               "b": ("percent scale", 100.0), "bounds": (0.08, 0.25),
               "step1": "a minority of colics need surgery - but missing one is fatal, operating unnecessarily is risky",
               "confirm": "trajectory protocols beat single-assessment on timing and survival",
               "refute": "trajectories prove unable to separate within the decision window"},
},
# ------------------------------------------------------------------ rank 8
{
 "key": "fip",
 "name": "Feline Infectious Peritonitis",
 "group": "Infectious Disease",
 "ladder_rank": 8, "ladder_tier": "foundations",
 "problem": "FIP was a death sentence - then an unapproved drug cured it. What is FIP's true biology, and why did the cure come from outside the system?",
 "description": "Feline infectious peritonitis - fatal immune-mediated vasculitis from mutated feline coronavirus - killed nearly all diagnosed cats. Then GS-441524 (a nucleoside analog, unapproved for animals) proved dramatically effective through field studies (Pedersen 2019), forcing regulatory reckoning: the UK and others eventually moved toward legal access. The biology - why the coronavirus mutates to the FIP form in some cats - remains incompletely mapped.",
 "background": "FIP was described in the 1960s; the coronavirus-mutation theory (Pedersen) explained why the ubiquitous enteric virus turns lethal in some cats. Immunity research showed cell-mediated response determines outcome. GS-441524's efficacy was demonstrated in field trials published 2019; the drug's unapproved status created a black market that saved cats while regulators deliberated. Legal access expanded from 2021 onward in several countries. As of 2026 the treatment works but the mutation biology and access equity remain open.",
 "why_it_matters": "FIP's story is a landmark: a fatal disease cured by a drug the system wouldn't approve, delivered by owners through gray channels. Understanding it fully matters for feline medicine and for drug-access ethics.",
 "sig_pointer": "The Signature system's proposed approach maps the mutation trigger to prevent the lethal form, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that the FIP mutation is a within-host evolution event with identifiable triggers: the enteric coronavirus mutates under specific immune pressures, and the triggers are mappable. "
  "Assumptions: (1) the mutation is not random but pressure-driven; (2) the pressures are measurable; (3) interrupting them prevents FIP. "
  "Reasoning path: an evolution model explains why some cats and not others, and predicts that trigger-targeted prevention will work. "
  "Proposed mechanism: 'mutation-trigger' mapping - identifying the immune and viral conditions preceding the FIP shift - enabling prevention. "
  "What would confirm it: trigger mapping predicting FIP cases prospectively, with interruption preventing them. "
  "What would kill it: evidence that the mutation is truly stochastic, defeating prediction. "
  "What this does not claim: it does not claim prevention exists, does not advise on treatment access, and does not constitute veterinary advice."),
 "sig_lens": "The Signature lens reads FIP as evolution happening inside the cat, and asks what pressure drives the lethal turn.",
 "how_it_works": "Researchers study FIP through coronavirus sequencing, immunology of outcome, GS-441524 field data, and regulatory-access research.",
 "key_points": [
  "FIP was nearly always fatal before GS-441524.",
  "Pedersen (2019) field studies proved the drug's dramatic efficacy.",
  "The drug was long unapproved, creating gray-market treatment.",
  "Legal access expanded from 2021 in several countries.",
  "The mutation trigger biology remains unmapped.",
 ],
 "requirements": [
  "Mapping of the within-host mutation triggers.",
  "Prevention targeting the triggers.",
  "Equitable legal access to effective treatment.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Pedersen NC et al. Efficacy and safety of the nucleoside analog GS-441524 for treatment of cats with FIP. Journal of Feline Medicine and Surgery. 2019;21(4):271-281.",
  "Pedersen NC. A review of feline infectious peritonitis virus infection. Journal of Feline Medicine and Surgery. 2009;11(3):225-258.",
  "Addie DD et al. Feline infectious peritonitis. ABCD guidelines. Journal of Feline Medicine and Surgery. 2009;11(7):594-604.",
  "Tasker S et al. FIP treatment guidelines updates. Various; 2021-2024.",
 ],
 "demo_data": {"a": ("FIP survival before GS-441524, percent (approx)", 5.0),
               "b": ("FIP survival with GS-441524, percent (approx)", 85.0), "bounds": (0.03, 0.1),
               "step1": "survival went from near zero to the large majority - the most dramatic reversal in feline medicine",
               "confirm": "trigger mapping predicts FIP prospectively with interruption preventing it",
               "refute": "the mutation proves truly stochastic and unpredictable"},
},
# ------------------------------------------------------------------ rank 9
{
 "key": "canine-cognitive",
 "name": "Canine Cognitive Dysfunction",
 "group": "Geriatrics",
 "ladder_rank": 9, "ladder_tier": "foundations",
 "problem": "Old dogs get lost in their own homes - what is canine cognitive dysfunction, and can the aging dog brain be protected?",
 "description": "Canine cognitive dysfunction syndrome (CDS) - disorientation, altered sleep, house-soiling, anxiety - affects a large fraction of dogs over 11. It parallels Alzheimer's: beta-amyloid deposition, oxidative damage. Interventions (diets enriched with antioxidants, selegiline, environmental enrichment) show modest effects; the pathology's drivers and any true prevention remain unknown.",
 "background": "CDS was characterized in the 1990s (Ruehl, Head); the amyloid parallel with Alzheimer's was established neuropathologically. The DISHAA assessment tool standardized diagnosis. Dietary trials (Hill's b/d, enriched with antioxidants and L-carnitine) showed cognitive benefit; selegiline is licensed with modest effects. As of 2026 no intervention prevents or reverses CDS, and the amyloid's causal role is unproven.",
 "why_it_matters": "Dogs live long enough now to dement: CDS erodes the human-animal bond in the final years and drives euthanasia decisions. Protecting the aging dog brain would also illuminate human Alzheimer's.",
 "sig_pointer": "The Signature system's proposed approach treats CDS as a preventable aging trajectory, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that CDS is a trajectory, not a fate: cognitive aging has modifiable drivers (vascular, metabolic, enrichment) and the decline curve can be bent. "
  "Assumptions: (1) the drivers are identifiable mid-life; (2) intervention windows precede symptoms; (3) the trajectory is measurable. "
  "Reasoning path: a trajectory model explains why late interventions underperform and predicts mid-life prevention will work. "
  "Proposed mechanism: 'cognitive trajectory' management - mid-life risk profiling with targeted diet, enrichment, and vascular care - tested against CDS incidence. "
  "What would confirm it: trajectory-managed dogs showing less CDS than controls in longitudinal trials. "
  "What would kill it: evidence that CDS is an inevitable aging program, unmodifiable. "
  "What this does not claim: it does not claim prevention exists today, does not advise on diet or drugs, and does not constitute veterinary advice."),
 "sig_lens": "The Signature lens reads the confused old dog as a trajectory that bent too far, and asks what mid-life intervention would straighten it.",
 "how_it_works": "Researchers study CDS through aging-dog cohorts, amyloid pathology, dietary trials, DISHAA validation, and comparative Alzheimer's research.",
 "key_points": [
  "CDS affects a large fraction of dogs over 11.",
  "It parallels Alzheimer's: amyloid, oxidative damage.",
  "DISHAA standardized the clinical assessment.",
  "Antioxidant diets and selegiline show modest effects.",
  "No intervention prevents or reverses CDS.",
 ],
 "requirements": [
  "Mid-life predictors of CDS trajectory.",
  "Prevention trials starting before symptoms.",
  "Proof of amyloid's causal role (or its refutation).",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Head E et al. Canine cognitive dysfunction. Various; 1997-2005.",
  "Ruehl WW et al. Canine cognitive dysfunction. Various; 1990s.",
  "Milgram NW et al. Dietary enrichment and cognition in aging dogs. Various; 2002-2006.",
  "Landsberg GM et al. Cognitive dysfunction syndrome. Various reviews; 2010-2020.",
 ],
 "demo_data": {"a": ("dogs over 11 with CDS signs, percent (approx)", 60.0),
               "b": ("percent scale", 100.0), "bounds": (0.45, 0.75),
               "step1": "most very old dogs show cognitive signs - dementia is the price of the longer canine life",
               "confirm": "trajectory-managed dogs show less CDS than controls longitudinally",
               "refute": "CDS proves an inevitable, unmodifiable aging program"},
},
# ------------------------------------------------------------------ rank 10
{
 "key": "pet-obesity",
 "name": "Obesity in Companion Animals",
 "group": "Nutrition",
 "ladder_rank": 10, "ladder_tier": "foundations",
 "problem": "Half of pets are overweight - why do weight-loss programs fail, and what would actually slim the pet population?",
 "description": "Overweight and obesity affect roughly half of dogs and cats in developed countries, driving arthritis, diabetes (especially cats), and shortened lifespan. Weight-loss programs work in clinics and fail at home: owner compliance collapses, begging defeats diets, and multi-pet households can't control intake. The problem is human behavior, not animal physiology.",
 "background": "Pet obesity was quantified in the 2000s (German, Lund); the lifespan cost was proven (Kealy's Labrador study: lean dogs lived ~2 years longer). Interventions - prescription diets, feeding guidelines, owner counseling - show clinic efficacy and home failure. Research identified the human factors: owner misperception of body condition, food as love, treat culture. As of 2026 no population-level intervention has slimmed pets.",
 "why_it_matters": "Obesity shortens pets' lives by years and causes preventable suffering: solving it is the largest welfare intervention in companion-animal practice.",
 "sig_pointer": "The Signature system's proposed approach treats pet obesity as an owner-behavior design problem, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that pet weight loss fails on owner behavior architecture: the feeding environment (free-feeding, treats, table scraps) defeats intentions, and counseling doesn't redesign environments. "
  "Assumptions: (1) owner behavior, not pet physiology, is the rate limiter; (2) environments are redesignable; (3) redesigned environments sustain weight loss. "
  "Reasoning path: a behavior-architecture model explains clinic-home gaps and predicts environment-redesign will outperform counseling. "
  "Proposed mechanism: 'feeding-environment redesign' - measured portions, treat budgets, multi-pet management systems - tested against weight trajectories. "
  "What would confirm it: redesigned environments outperforming counseling on sustained weight loss in trials. "
  "What would kill it: evidence that owner behavior resists environmental redesign, or that physiology dominates. "
  "What this does not claim: it does not claim a diet works, does not advise on feeding, and does not constitute veterinary advice."),
 "sig_lens": "The Signature lens reads the fat pet as an environment problem wearing a willpower costume, and asks what redesigned feeding would change.",
 "how_it_works": "Nutrition researchers study pet obesity through body-condition surveys, weight-loss trials, owner-behavior research, and lifespan cohorts.",
 "key_points": [
  "~Half of dogs and cats in developed countries are overweight.",
  "Lean Labradors lived ~2 years longer (Kealy).",
  "Clinic programs work; home compliance collapses.",
  "Owner misperception of body condition is widespread.",
  "No population intervention has worked.",
 ],
 "requirements": [
  "Environment-redesign interventions proven at home.",
  "Sustained weight loss, not just clinic loss.",
  "Owner-behavior models that actually change feeding.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "German AJ. The growing problem of obesity in dogs and cats. Journal of Nutrition. 2006;136(7 Suppl):1940S-1946S.",
  "Kealy RD et al. Effects of diet restriction on life span and age-related changes in dogs. JAVMA. 2002;220(9):1315-1320.",
  "Lund EM et al. Prevalence and risk factors for obesity in adult dogs. Various; 2006.",
  "Courcier EA et al. Feline obesity risk factors. Various; 2010-2013.",
 ],
 "demo_data": {"a": ("lifespan gained by lean Labradors, years (approx)", 2.0),
               "b": ("Labrador lifespan, years (approx)", 12.0), "bounds": (0.12, 0.22),
               "step1": "lean dogs lived two years longer - obesity steals a sixth of a dog's life",
               "confirm": "redesigned environments beat counseling on sustained weight loss",
               "refute": "owner behavior proves resistant to environmental redesign"},
},
# ------------------------------------------------------------------ rank 11
{
 "key": "animal-pain",
 "name": "Pain Assessment in Animals",
 "group": "Welfare",
 "ladder_rank": 11, "ladder_tier": "foundations",
 "problem": "Animals can't report pain - how can pain be reliably recognized across species, and what is missed?",
 "description": "Pain assessment in animals relies on behavior: grimace scales (mice, rats, rabbits, cats, horses, sheep), composite pain scales (Glasgow, UNESP-Botucatu), and facial-action AI. But prey species hide pain, scales are validated narrowly, and inter-observer reliability is modest. Undertreated pain remains endemic in veterinary practice.",
 "background": "Grimace scales began with Langford's mouse grimace scale (2010), then spread across species: rat, rabbit, cat (Evangelista 2019), horse, sheep. Composite scales (Glasgow Composite Pain Scale, 2007) structured clinical assessment. Automated facial-expression AI promises objectivity. But validation is behavior-against-behavior, prey-species masking defeats observation, and production animals receive the least assessment. As of 2026 no universal, objective pain measure exists for any species.",
 "why_it_matters": "Unrecognized pain is untreated suffering on a massive scale: every unassessed animal is a potential silent sufferer. Reliable assessment is the foundation of veterinary welfare.",
 "sig_pointer": "The Signature system's proposed approach fuses behavioral, physiological, and contextual signals per species, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that no single signal measures animal pain, but species-specific signal fusion does: behavior, physiology, and context each carry partial information. "
  "Assumptions: (1) pain has multi-signal signatures per species; (2) the signatures are learnable; (3) fusion beats any single scale. "
  "Reasoning path: a fusion model explains why single scales underperform and predicts multi-signal assessment will work. "
  "Proposed mechanism: 'pain fusion' assessment per species - grimace plus physiology plus context against baselines - validated against analgesic response. "
  "What would confirm it: fused assessment outperforming the best single scale on analgesic-response prediction. "
  "What would kill it: evidence that prey-species masking defeats all signals, or that fusion adds nothing. "
  "What this does not claim: it does not claim a device exists, does not advise on analgesia, and does not constitute veterinary advice."),
 "sig_lens": "The Signature lens reads hidden animal pain as a signal awaiting fusion, and asks what combination would reveal it.",
 "how_it_works": "Welfare researchers study pain through grimace-scale validation, composite-scale trials, facial AI, and analgesic-response studies.",
 "key_points": [
  "Grimace scales exist for mice, rats, rabbits, cats, horses, sheep.",
  "Langford's mouse scale (2010) launched the field.",
  "Prey species evolutionarily hide pain.",
  "Validation is behavior-against-behavior - circular.",
  "Production animals receive the least pain assessment.",
 ],
 "requirements": [
  "Species-specific fused pain measures validated prospectively.",
  "Proof of beating the best single scale.",
  "Assessment practical for production settings.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Langford DJ et al. Coding of facial expressions of pain in the laboratory mouse. Nature Methods. 2010;7:447-449.",
  "Evangelista MC et al. Feline grimace scale. Scientific Reports. 2019;9:19128.",
  "Reid J et al. Glasgow composite pain scale. Various; 2007.",
  "Sneddon LU et al. Fish pain and welfare. Various; 2003-2019.",
 ],
 "demo_data": {"a": ("species with validated grimace scales (approx)", 8.0),
               "b": ("vertebrate species under veterinary care (approx thousands)", 50.0), "bounds": (0.1, 0.25),
               "step1": "grimace scales cover a handful of species while thousands go unassessed",
               "confirm": "fused assessment beats the best single scale on analgesic-response prediction",
               "refute": "prey-species masking proves to defeat all measurable signals"},
},
# ------------------------------------------------------------------ rank 12
{
 "key": "osteosarcoma",
 "name": "Osteosarcoma in Dogs: Why So Aggressive",
 "group": "Oncology",
 "ladder_rank": 12, "ladder_tier": "compounded",
 "problem": "Canine osteosarcoma metastasizes with terrifying speed - why is the dog's bone cancer so much more aggressive than the human's?",
 "description": "Osteosarcoma strikes large and giant breeds (Greyhounds, Rottweilers, Great Danes) at rates far above humans, and metastasizes to lungs in the large majority, usually within months even with amputation and chemotherapy. Median survival with treatment is under a year. The dog's cancer is biologically more aggressive - and a model for the human disease's worst forms.",
 "background": "Canine osteosarcoma was characterized as a spontaneous model in the 1980s-90s; its metastatic propensity exceeds human osteosarcoma's. Genomic studies found shared drivers (TP53, RB1) plus dog-specific features. Immunotherapy trials (including the landmark Listeria-based approaches) show signals. But the aggression's basis - why micrometastases are nearly universal at diagnosis - remains unmapped. As of 2026 treatment extends life by months, not years.",
 "why_it_matters": "Osteosarcoma kills large dogs young and models human pediatric bone cancer: cracking its aggression would save dogs and illuminate the human disease.",
 "sig_pointer": "The Signature system's proposed approach treats metastatic propensity as the therapeutic target, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that canine osteosarcoma's aggression is a metastatic-competence program: the primary tumor is treatable, but dissemination is programmed early and universally. "
  "Assumptions: (1) micrometastases are present at diagnosis in most cases; (2) the program has identifiable drivers; (3) targeting dissemination beats targeting the primary. "
  "Reasoning path: a dissemination-first model explains why amputation plus chemo extends life only months and predicts anti-metastatic therapy will outperform. "
  "Proposed mechanism: 'dissemination-targeted' therapy - agents blocking the metastatic program - tested against metastasis-free survival. "
  "What would confirm it: anti-dissemination therapy extending metastasis-free survival beyond current best. "
  "What would kill it: evidence that metastases are seeded too early for any intervention, or that the program lacks druggable drivers. "
  "What this does not claim: it does not claim a treatment exists, does not advise on therapy, and does not constitute veterinary advice."),
 "sig_lens": "The Signature lens reads the bone tumor as a dissemination program wearing a lump costume, and asks what would block the spread.",
 "how_it_works": "Oncologists study osteosarcoma through genomic comparison, metastasis biology, immunotherapy trials, and limb-sparing outcome cohorts.",
 "key_points": [
  "Canine osteosarcoma metastasizes in the large majority, usually within months.",
  "Median survival with amputation plus chemo is under a year.",
  "Large and giant breeds are disproportionately affected.",
  "Shared drivers (TP53, RB1) plus dog-specific features.",
  "Immunotherapy shows early signals.",
 ],
 "requirements": [
  "Drivers of the metastatic program identified.",
  "Anti-dissemination therapy proven in trials.",
  "Early detection before micrometastatic spread.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Withrow SJ et al. Canine osteosarcoma. Various editions; 1980s-2020s.",
  "Mueller F et al. Canine osteosarcoma genomics. Various; 2007-2015.",
  "Paoloni M et al. Comparative oncology. Various; 2009-2015.",
  "Mason NJ et al. Immunotherapy for osteosarcoma. Various; 2016-2022.",
 ],
 "demo_data": {"a": ("dogs developing lung metastases, percent (approx)", 90.0),
               "b": ("percent scale", 100.0), "bounds": (0.8, 0.97),
               "step1": "nine in ten cases metastasize - dissemination is the rule, not the exception",
               "confirm": "anti-dissemination therapy beats current best on metastasis-free survival",
               "refute": "metastases prove seeded too early for any intervention"},
},
# ------------------------------------------------------------------ rank 13
{
 "key": "equine-uveitis",
 "name": "Equine Recurrent Uveitis",
 "group": "Ophthalmology",
 "ladder_rank": 13, "ladder_tier": "compounded",
 "problem": "Moon blindness strikes horses in blinding episodes - what drives equine recurrent uveitis, and why does it keep coming back?",
 "description": "Equine recurrent uveitis (ERU, 'moon blindness') - episodic intraocular inflammation - is the leading cause of blindness in horses worldwide. Episodes damage the eye cumulatively; many horses lose vision in one or both eyes. Leptospira is implicated in many cases (molecular mimicry with lens proteins), but not all; Appaloosas are genetically predisposed. Treatment is anti-inflammatory and ultimately often enucleation.",
 "background": "Leptospiral association was established in the late 20th century (antibodies and DNA in affected eyes); the mimicry theory (leptospiral proteins resembling lens crystallins) explained recurrence. Genetic predisposition in Appaloosas was mapped (MHC region). Cyclosporine implants (Gilger) provided local sustained therapy with partial success. But the trigger of each episode, the full etiologic spectrum, and any cure remain unknown. As of 2026 management is episodic suppression.",
 "why_it_matters": "ERU blinds working and sport horses globally: understanding recurrence would convert blinding episodes into a manageable or curable condition.",
 "sig_pointer": "The Signature system's proposed approach treats ERU as an autoimmune memory problem, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that ERU recurrence is immunologic memory: each episode trains the response, and the eye's immune privilege - once broken - can't be restored by suppressing inflammation alone. "
  "Assumptions: (1) recurrence reflects memory, not re-infection; (2) the privilege breach is the key event; (3) memory is erasable or bypassable. "
  "Reasoning path: a memory model explains why episodes escalate and why suppression doesn't cure - and predicts that memory-targeted therapy will. "
  "Proposed mechanism: 'memory-reset' therapy - approaches that delete or bypass the ocular immune memory - tested against episode recurrence. "
  "What would confirm it: memory-targeted therapy preventing recurrence beyond suppression in trials. "
  "What would kill it: evidence that each episode is new infection or that memory is unerasable. "
  "What this does not claim: it does not claim a cure exists, does not advise on therapy, and does not constitute veterinary advice."),
 "sig_lens": "The Signature lens reads the blinding episodes as immune memory misfiring, and asks what would make the eye forget.",
 "how_it_works": "Ophthalmologists study ERU through leptospiral testing, MHC genetics, cyclosporine-implant trials, and episode-pattern analyses.",
 "key_points": [
  "ERU is the leading cause of blindness in horses.",
  "Leptospira is implicated via molecular mimicry.",
  "Appaloosas carry MHC-linked predisposition.",
  "Cyclosporine implants provide partial local control.",
  "Management is episodic suppression; no cure exists.",
 ],
 "requirements": [
  "Proof of the memory mechanism and its triggers.",
  "Memory-targeted therapy preventing recurrence.",
  "Early identification of at-risk horses.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Gilger BC et al. Cyclosporine implants for ERU. Various; 2000-2010.",
  "Deeg CA et al. Leptospiral mimicry in ERU. Various; 2002-2008.",
  "Fritz KL et al. Genetic risk for ERU in Appaloosas. Various; 2014.",
  "Gerding JC, Gilger BC. Prognosis and impact of ERU. Animals. 2016;6(3):18.",
 ],
 "demo_data": {"a": ("horses losing vision to ERU, percent of severe cases (approx)", 40.0),
               "b": ("percent scale", 100.0), "bounds": (0.25, 0.55),
               "step1": "nearly half of severe cases lose vision - the commonest blinding disease of horses",
               "confirm": "memory-targeted therapy beats suppression on recurrence",
               "refute": "each episode proves new infection with memory unerasable"},
},
# ------------------------------------------------------------------ rank 14
{
 "key": "brd",
 "name": "Bovine Respiratory Disease Complex",
 "group": "Production Medicine",
 "ladder_rank": 14, "ladder_tier": "compounded",
 "problem": "Shipping fever kills feedlot cattle by the thousand - why does bovine respiratory disease resist vaccines and metaphylaxis?",
 "description": "Bovine respiratory disease (BRD) - the multifactorial pneumonia of stressed cattle - is the leading cause of feedlot morbidity and mortality. Viruses (BHV-1, BRSV, PI3, BVDV) plus bacteria (Mannheimia, Pasteurella, Histophilus, Mycoplasma) plus stress interact. Vaccines exist for components; metaphylaxis (mass treatment on arrival) works but drives resistance. The complex keeps winning.",
 "background": "BRD's multifactorial nature was established in the 1980s-90s; the stress-immunosuppression link (transport, weaning, commingling) explained outbreaks. Vaccines reduced but never eliminated disease - the pathogen mix shifts. Metaphylaxis proved effective and controversial. As of 2026 BRD remains the feedlot's costliest disease with no integrated solution.",
 "why_it_matters": "BRD costs the cattle industry billions and drives mass antibiotic use: solving it would improve welfare, economics, and stewardship simultaneously.",
 "sig_pointer": "The Signature system's proposed approach treats BRD as a stress-immune-pathogen interaction, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that BRD is a three-factor interaction - pathogens, stress immunosuppression, and timing - and that single-factor interventions (vaccines alone, antibiotics alone) can't solve interactions. "
  "Assumptions: (1) the factors interact multiplicatively; (2) stress timing is manipulable; (3) integrated protocols beat single interventions. "
  "Reasoning path: an interaction model explains partial successes and predicts integrated stress-pathogen management will work. "
  "Proposed mechanism: 'interaction-managed' BRD control - stress-reduced handling plus timed vaccination plus targeted (not mass) therapy. "
  "What would confirm it: integrated protocols beating current best on morbidity in trials. "
  "What would kill it: evidence that pathogen mix defeats any management, or that stress is unmodifiable at scale. "
  "What this does not claim: it does not claim a protocol exists, does not advise on therapy, and does not constitute veterinary advice."),
 "sig_lens": "The Signature lens reads shipping fever as three factors colliding, and asks what integrated management would separate them.",
 "how_it_works": "Researchers study BRD through pathogen surveillance, stress-immunology, vaccine trials, and metaphylaxis comparisons.",
 "key_points": [
  "BRD is the leading feedlot disease by morbidity and mortality.",
  "Viruses plus bacteria plus stress interact multifactorially.",
  "Vaccines reduce but never eliminate disease.",
  "Metaphylaxis works but drives resistance concerns.",
  "No integrated solution exists.",
 ],
 "requirements": [
  "Interaction models validated prospectively.",
  "Integrated protocols proven against current best.",
  "Stress-reduction methods practical at feedlot scale.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Griffin D et al. Bovine respiratory disease. Various; 1997-2014.",
  "Taylor JD et al. BRD: current understanding. Veterinary Clinics of North America. 2010;26(2):209-229.",
  "Nickell JS, White BJ. Metaphylactic antimicrobial therapy. Veterinary Clinics of North America. 2010;26(2):285-301.",
  "Edwards TA. Control methods for BRD. Veterinary Clinics of North America. 2010;26(2):273-284.",
 ],
 "demo_data": {"a": ("feedlot morbidity from BRD, percent (approx)", 20.0),
               "b": ("percent scale", 100.0), "bounds": (0.12, 0.3),
               "step1": "a fifth of feedlot cattle sicken - the costliest disease of the beef industry",
               "confirm": "integrated protocols beat current best on morbidity",
               "refute": "pathogen mix proves to defeat any management approach"},
},
# ------------------------------------------------------------------ rank 15
{
 "key": "asf",
 "name": "African Swine Fever: The Vaccine Gap",
 "group": "Infectious Disease",
 "ladder_rank": 15, "ladder_tier": "compounded",
 "problem": "African swine fever kills nearly every pig it infects and has no vaccine - why is this virus so hard to vaccinate against?",
 "description": "African swine fever virus (ASFV) - a large DNA virus - causes hemorrhagic fever with near-100% mortality in domestic pigs. It swept through China (2018-2019), killing hundreds of millions of pigs, and persists in Europe and Asia. No vaccine is licensed: the virus's immune evasion is sophisticated, inactivated vaccines don't protect, and live-attenuated candidates risk reversion and spread.",
 "background": "ASF was described in Kenya (1921, Montgomery); it smoldered in Africa and Sardinia before the 2007 Georgia outbreak launched the Eurasian pandemic. China's 2018-2019 epidemic halved its pig herd - the largest animal-disease economic shock in history. Vaccine research cycled: inactivated (no protection), subunit (partial), gene-deleted live-attenuated (promising but safety-flagged). Vietnam licensed early candidates with debated field performance. As of 2026 no widely accepted safe effective vaccine exists.",
 "why_it_matters": "ASF threatens global pork production and food security: a safe vaccine would end the largest ongoing animal-disease pandemic.",
 "sig_pointer": "The Signature system's proposed approach targets the virus's immune-evasion program, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that ASFV's vaccine resistance comes from its immune-evasion gene program: the virus disables the very responses vaccines need, so the target must be the evasion genes themselves. "
  "Assumptions: (1) evasion genes are identifiable and deletable; (2) deletion yields safe attenuation; (3) the attenuated virus still immunizes. "
  "Reasoning path: an evasion-target model explains inactivated-vaccine failures and predicts rationally deleted live vaccines will work. "
  "Proposed mechanism: 'evasion-deleted' vaccines - ASFV with immune-evasion genes removed - tested for safety and efficacy. "
  "What would confirm it: deleted candidates protecting without reversion in trials. "
  "What would kill it: evidence that evasion is too redundant to delete safely, or that deletion destroys immunogenicity. "
  "What this does not claim: it does not claim a vaccine exists, does not advise on control, and does not constitute veterinary advice."),
 "sig_lens": "The Signature lens reads the unvaccinatable virus as defending itself with deleted-able genes, and asks which deletions would disarm it.",
 "how_it_works": "Researchers study ASF through evasion-gene mapping, attenuated-candidate trials, and outbreak epidemiology.",
 "key_points": [
  "ASFV kills nearly 100% of infected domestic pigs.",
  "China's 2018-2019 epidemic halved its herd - hundreds of millions dead.",
  "Inactivated vaccines don't protect; the virus evades immunity.",
  "Gene-deleted live candidates show promise with safety flags.",
  "No widely accepted safe effective vaccine exists.",
 ],
 "requirements": [
  "Evasion-gene maps enabling rational deletion.",
  "Deleted candidates proven safe and effective.",
  "DIVA-compatible vaccines for surveillance.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Montgomery RE. On a form of swine fever occurring in British East Africa. Journal of Comparative Pathology. 1921;34:159-191.",
  "Dixon LK et al. African swine fever virus: evasion mechanisms. Annual Review of Animal Biosciences. 2019;7:221-240.",
  "Sánchez EG et al. Vaccine approaches. Vaccines. 2019;7(2):35.",
  "Penrith ML et al. ASF epidemiology. Various; 2009-2021.",
 ],
 "demo_data": {"a": ("ASF mortality in domestic pigs, percent (approx)", 95.0),
               "b": ("percent scale", 100.0), "bounds": (0.9, 0.99),
               "step1": "near-total lethality with no vaccine - the most dangerous pig disease known",
               "confirm": "evasion-deleted candidates protect without reversion",
               "refute": "evasion proves too redundant to delete safely"},
},
# ------------------------------------------------------------------ rank 16
{
 "key": "avian-flu",
 "name": "Avian Influenza Control",
 "group": "Infectious Disease",
 "ladder_rank": 16, "ladder_tier": "compounded",
 "problem": "H5N1 keeps evolving, spreading to mammals, and threatening humans - why can't avian influenza be controlled, and what would stop the next spillover?",
 "description": "Highly pathogenic avian influenza (H5N1 and relatives) has caused the largest poultry losses in history (2020-2024 panzootic), spilled into wild birds, marine mammals, and US dairy cattle (2024), with sporadic human cases. Control by culling is economically devastating; vaccination is contested (trade barriers); the virus's evolution in wild-bird reservoirs defeats eradication.",
 "background": "HPAI H5N1 emerged in Guangdong (1996); the 2000s saw spread across Asia, Europe, Africa. The 2020-2024 panzootic was unprecedented in wild-bird mortality and mammalian spillover. The 2024 US dairy-cattle outbreak showed mammary tropism and cow-to-cow spread. Human cases remain mostly mild but the pandemic potential keeps experts alert. Control debates: culling versus vaccination (France began duck vaccination 2023 with promising results). As of 2026 the virus circulates in wild birds beyond control.",
 "why_it_matters": "Avian influenza is the most watched pandemic threat: controlling it in birds is pandemic prevention in humans.",
 "sig_pointer": "The Signature system's proposed approach treats wild-bird reservoirs as the control frontier, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that avian influenza control fails at the wild-bird reservoir: poultry measures can't touch the migratory source, so control must shift to reservoir-interface management. "
  "Assumptions: (1) wild birds are the ineradicable reservoir; (2) spillover interfaces (poultry-wild contact, cattle) are manageable; (3) vaccination can break poultry amplification. "
  "Reasoning path: a reservoir model explains why culling fails long-term and predicts interface management plus vaccination will work. "
  "Proposed mechanism: 'interface control' - biosecurity at wild-domestic interfaces plus strategic poultry vaccination - tested against outbreak frequency. "
  "What would confirm it: interface-managed regions showing fewer spillovers than cull-only regions. "
  "What would kill it: evidence that interfaces are unmanageable at scale, or that vaccination drives dangerous evolution. "
  "What this does not claim: it does not claim control is achievable today, takes no trade-policy position, and does not constitute veterinary advice."),
 "sig_lens": "The Signature lens reads the panzootic as a reservoir problem wearing a poultry costume, and asks what interface control would contain it.",
 "how_it_works": "Researchers study avian flu through wild-bird surveillance, spillover genomics, vaccine trials, and pandemic-risk assessment.",
 "key_points": [
  "H5N1's 2020-2024 panzootic was the largest in history.",
  "Spillover reached marine mammals and US dairy cattle (2024).",
  "Wild migratory birds are the ineradicable reservoir.",
  "Culling is economically devastating; vaccination is trade-contested.",
  "France's 2023 duck vaccination showed promise.",
 ],
 "requirements": [
  "Wild-domestic interface management proven at scale.",
  "Vaccines that don't trigger trade barriers.",
  "Early warning for mammalian adaptation.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "World Organisation for Animal Health. Avian influenza reports. 1996 onward.",
  "USDA. HPAI in dairy cattle. 2024 reports.",
  "European Food Safety Authority. Avian influenza overviews. 2020-2024.",
  "Peacock TP et al. Mammalian adaptation of H5N1. Various; 2023-2024.",
 ],
 "demo_data": {"a": ("poultry lost in the 2020-2024 panzootic, millions (approx)", 500.0),
               "b": ("millions scale", 1000.0), "bounds": (0.3, 0.8),
               "step1": "hundreds of millions of birds lost - the largest animal-disease event recorded",
               "confirm": "interface-managed regions beat cull-only regions on spillover frequency",
               "refute": "interfaces prove unmanageable with vaccination driving dangerous evolution"},
},
# ------------------------------------------------------------------ rank 17
{
 "key": "johnes",
 "name": "Johne's Disease",
 "group": "Infectious Disease",
 "ladder_rank": 17, "ladder_tier": "compounded",
 "problem": "Mycobacterium avium paratuberculosis causes untreatable wasting in cattle - why can't Johne's disease be cured or reliably diagnosed early?",
 "description": "Johne's disease - chronic granulomatous enteritis from MAP - causes progressive weight loss and diarrhea in cattle (and other ruminants), with long subclinical shedding. No treatment exists; control is test-and-cull with imperfect tests (fecal culture slow, ELISA insensitive early). The Crohn's disease link in humans remains debated and unsettling.",
 "background": "Johne's was described in 1895; MAP's slow growth defeated culture-based control. The long latency (years) means infected animals spread before detection. Control programs (USDA, various national) reduced prevalence slowly. The MAP-Crohn's hypothesis (Chiodini) persists without proof, complicating the public-health picture. Vaccines exist in some countries with partial efficacy. As of 2026 Johne's is managed, not solved.",
 "why_it_matters": "Johne's drains dairy productivity silently and raises unresolved food-safety questions: solving diagnosis would enable real control.",
 "sig_pointer": "The Signature system's proposed approach detects the subclinical shedder, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that Johne's control fails on the subclinical shedder: animals spread MAP for years before tests turn positive, so control must detect shedding, not disease. "
  "Assumptions: (1) shedding precedes detectability by current tests; (2) shedding is measurable with better methods; (3) removing shedders breaks transmission. "
  "Reasoning path: a shedder-first model explains slow control progress and predicts shedder-targeted programs will work. "
  "Proposed mechanism: 'shedder surveillance' - sensitive early-shedding detection directing removal before spread. "
  "What would confirm it: shedder-targeted programs outperforming test-and-cull on prevalence. "
  "What would kill it: evidence that shedding is undetectable until late, or that environmental persistence defeats removal. "
  "What this does not claim: it does not claim a test exists, does not advise on control, and does not constitute veterinary advice."),
 "sig_lens": "The Signature lens reads Johne's as spread by the undetectable, and asks what would make the shedder visible.",
 "how_it_works": "Researchers study Johne's through MAP genomics, test evaluations, control-program analyses, and Crohn's-link investigations.",
 "key_points": [
  "Johne's causes progressive wasting with no treatment.",
  "Subclinical shedding lasts years before detection.",
  "Fecal culture is slow; ELISA is insensitive early.",
  "Control programs reduce prevalence slowly.",
  "The MAP-Crohn's link remains unproven and debated.",
 ],
 "requirements": [
  "Early-shedding detection with real sensitivity.",
  "Proof that shedder removal breaks transmission.",
  "Resolution of the Crohn's question.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Johne HA, Frothingham L. Ein eigenthumlicher Fall von Tuberculose beim Rind. Deutsche Zeitschrift fur Thiermedizin. 1895;21:438-454.",
  "Chiodini RJ et al. MAP and Crohn's disease. Various; 1984-2020.",
  "Nielsen SS, Toft N. Ante mortem diagnosis of paratuberculosis. Veterinary Microbiology. 2008;129(3-4):217-231.",
  "USDA. Johne's disease control programs. Various.",
 ],
 "demo_data": {"a": ("subclinical shedding before detection, years (approx)", 2.0),
               "b": ("detection delay that would enable control, months (approx)", 6.0), "bounds": (0.2, 0.5),
               "step1": "years of silent shedding precede detection - the control gap is measured in years",
               "confirm": "shedder-targeted programs beat test-and-cull on prevalence",
               "refute": "shedding proves undetectable until late disease"},
},
# ------------------------------------------------------------------ rank 18
{
 "key": "strangles",
 "name": "Strangles: The Ancient Scourge",
 "group": "Infectious Disease",
 "ladder_rank": 18, "ladder_tier": "compounded",
 "problem": "Streptococcus equi causes strangles - known since the 13th century, still undefeated. Why can't this ancient disease be eradicated?",
 "description": "Strangles - lymph-node abscessation from Streptococcus equi - is the commonest infectious equine disease globally. It spreads through nasal discharge and fomites, with carrier horses (guttural-pouch carriers) sustaining transmission. Vaccines exist but are imperfect; eradication is thwarted by carriers, imperfect diagnostics, and the horse industry's movement patterns.",
 "background": "Strangles was described in the 1200s; the bacteriology was settled in the 1880s-90s. The carrier state (guttural pouch chondroids) was characterized in the late 20th century, explaining persistence. Vaccines - live-attenuated intranasal and killed - offer partial protection with safety trade-offs. Molecular typing tracks outbreaks. As of 2026 strangles remains endemic worldwide.",
 "why_it_matters": "Strangles disrupts the horse industry constantly: quarantines, canceled events, suffering animals. Eradication would remove equine medicine's most persistent infectious burden.",
 "sig_pointer": "The Signature system's proposed approach targets the carrier state, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that strangles persists through carriers: guttural-pouch carriers sustain transmission between outbreaks, and eradication means finding and clearing them. "
  "Assumptions: (1) carriers are the reservoir; (2) carriers are identifiable (endoscopy, PCR); (3) clearance is achievable. "
  "Reasoning path: a carrier model explains endemicity despite vaccines and predicts carrier-targeted eradication will work. "
  "Proposed mechanism: 'carrier-clearing' eradication - systematic identification and treatment of guttural-pouch carriers. "
  "What would confirm it: carrier-cleared populations staying strangles-free. "
  "What would kill it: evidence that environmental persistence or subclinical spread defeats carrier targeting. "
  "What this does not claim: it does not claim eradication is feasible today, does not advise on management, and does not constitute veterinary advice."),
 "sig_lens": "The Signature lens reads the ancient scourge as sustained by hidden carriers, and asks what would find and clear them.",
 "how_it_works": "Researchers study strangles through carrier-state research, vaccine trials, molecular epidemiology, and outbreak management.",
 "key_points": [
  "Strangles was described in the 1200s; still globally endemic.",
  "S. equi spreads via discharge and fomites.",
  "Guttural-pouch carriers sustain transmission.",
  "Vaccines are partially protective with trade-offs.",
  "Eradication is thwarted by carriers and horse movement.",
 ],
 "requirements": [
  "Reliable carrier identification at scale.",
  "Clearance protocols proven effective.",
  "Industry coordination on movement and quarantine.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Sweeney CR et al. Streptococcus equi. Various; 1987-2005.",
  "Newton JR et al. Guttural pouch carriers. Various; 1997-2004.",
  "Waller AS et al. Strangles genomics and vaccines. Various; 2011-2021.",
  "Boyle AG et al. Strangles consensus. Various; 2018.",
 ],
 "demo_data": {"a": ("centuries since strangles was described (1200s)", 8.0),
               "b": ("centuries scale", 10.0), "bounds": (0.6, 1.0),
               "step1": "eight centuries described, still undefeated - the oldest unsolved equine infection",
               "confirm": "carrier-cleared populations stay strangles-free",
               "refute": "environmental persistence proves to defeat carrier targeting"},
},
# ------------------------------------------------------------------ rank 19
{
 "key": "canine-epilepsy",
 "name": "Canine Epilepsy Genetics",
 "group": "Neurology",
 "ladder_rank": 19, "ladder_tier": "compounded",
 "problem": "Idiopathic epilepsy strikes up to 5% of dogs in some breeds - why is the genetics so elusive, and what would enable precision treatment?",
 "description": "Canine idiopathic epilepsy - recurrent seizures without identified cause - is among the commonest neurologic diseases of dogs, with breed predispositions (Border Collies, Belgian Shepherds, Rhodesian Ridgebacks). Treatment (phenobarbital, bromide, levetiracetam) controls many but not all; drug-resistant cases suffer. The genetics are complex: few Mendelian forms found, most risk polygenic and unmapped.",
 "background": "Breed predispositions were quantified in the 1990s-2000s; the canine genome enabled mapping. Successes are few: LGI2 in Lagotto Romagnolo (Seppala 2011), DIRAS1 in Rhodesian Ridgebacks. Most idiopathic epilepsy remains genetically unexplained - likely polygenic with environmental triggers. Drug-resistance mechanisms mirror human epilepsy partially. As of 2026 genetic testing guides few treatment decisions.",
 "why_it_matters": "Epilepsy devastates dogs and owners: seizures, drug side effects, euthanasia for refractory cases. Genetic understanding would enable breeding away from risk and precision therapy.",
 "sig_pointer": "The Signature system's proposed approach maps the polygenic architecture breed by breed, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that canine epilepsy genetics is breed-specific polygenicity: each predisposed breed carries its own risk architecture, so mapping must be breed-by-breed. "
  "Assumptions: (1) risk architectures differ between breeds; (2) within-breed mapping has power; (3) risk loci guide treatment and breeding. "
  "Reasoning path: a breed-specific model explains why cross-breed GWAS underperforms and predicts within-breed mapping will succeed. "
  "Proposed mechanism: 'breed-mapped' epilepsy genetics - within-breed risk panels guiding breeding and drug choice. "
  "What would confirm it: within-breed panels predicting risk and drug response in validation. "
  "What would kill it: evidence that risk is too polygenic even within breeds for useful panels. "
  "What this does not claim: it does not claim a test exists, does not advise on breeding or drugs, and does not constitute veterinary advice."),
 "sig_lens": "The Signature lens reads breed epilepsy as separate genetic puzzles, and asks what each breed's map would reveal.",
 "how_it_works": "Neurologists study epilepsy through breed cohorts, within-breed GWAS, drug-response pharmacogenetics, and seizure monitoring.",
 "key_points": [
  "Idiopathic epilepsy affects up to ~5% in predisposed breeds.",
  "Few Mendelian forms found (LGI2, DIRAS1); most risk unmapped.",
  "Drug resistance affects a significant minority.",
  "Breed predispositions are strong and specific.",
  "Genetic testing rarely guides treatment today.",
 ],
 "requirements": [
  "Within-breed risk maps with predictive power.",
  "Pharmacogenetic guides for drug choice.",
  "Breeding strategies reducing risk.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Seppala EH et al. LGI2 truncation causes epilepsy in Lagotto Romagnolo dogs. PLoS Genetics. 2011;7(8):e1002194.",
  "Wielaender F et al. DIRAS1 variant in Rhodesian Ridgeback epilepsy. Various; 2017.",
  "Berendt M et al. Canine epilepsy genetics. Various; 2004-2015.",
  "Ekenstedt KJ, Oberbauer AM. Inherited epilepsy in dogs. Various; 2013-2020.",
 ],
 "demo_data": {"a": ("epilepsy prevalence in predisposed breeds, percent (approx)", 5.0),
               "b": ("percent scale", 100.0), "bounds": (0.02, 0.08),
               "step1": "one in twenty dogs seizes in predisposed breeds - with genetics mostly unmapped",
               "confirm": "within-breed panels predict risk and drug response in validation",
               "refute": "risk proves too polygenic even within breeds for useful panels"},
},
# ------------------------------------------------------------------ rank 20
{
 "key": "feline-asthma",
 "name": "Feline Asthma",
 "group": "Respiratory Medicine",
 "ladder_rank": 20, "ladder_tier": "compounded",
 "problem": "Cats wheeze like asthmatic children - but what triggers feline asthma, and why is long-term control so difficult?",
 "description": "Feline asthma - reversible airway inflammation and hyperresponsiveness - affects a few percent of cats, with coughing, wheezing, and life-threatening bronchoconstriction. Allergens are suspected but rarely identified; treatment (inhaled steroids via mask, bronchodilators) manages but doesn't cure. The immunology parallels human asthma incompletely.",
 "background": "Feline asthma was characterized in the 1990s-2000s (Moise, Reinero); the house-dust-mite and Bermuda-grass models established allergic mechanisms experimentally. Inhaled therapy (fluticasone via AeroKat) revolutionized management. But trigger identification in pet cats usually fails, environmental control is impractical, and some cats remain poorly controlled. As of 2026 management is chronic suppression without cure.",
 "why_it_matters": "Asthma attacks terrify owners and can kill cats: better control would convert a frightening chronic disease into a background condition.",
 "sig_pointer": "The Signature system's proposed approach identifies the individual cat's triggers, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that feline asthma control fails on trigger ignorance: therapy suppresses inflammation while unknown triggers keep driving it. "
  "Assumptions: (1) triggers are individual and identifiable; (2) trigger avoidance beats suppression; (3) indoor environments are modifiable. "
  "Reasoning path: a trigger model explains why some cats control easily and others don't, and predicts trigger-mapped management will outperform. "
  "Proposed mechanism: 'trigger-mapped' asthma care - individual allergen profiling with environmental modification - tested against control scores. "
  "What would confirm it: trigger-mapped cats achieving better control with less drug in trials. "
  "What would kill it: evidence that triggers are unidentifiable in most pet cats, or that avoidance is impractical. "
  "What this does not claim: it does not claim a cure exists, does not advise on therapy, and does not constitute veterinary advice."),
 "sig_lens": "The Signature lens reads the wheezing cat as reacting to something specific, and asks what trigger map would reveal it.",
 "how_it_works": "Researchers study feline asthma through allergen models, inhaled-therapy trials, trigger-identification studies, and airway-remodeling research.",
 "key_points": [
  "Feline asthma affects a few percent of cats.",
  "Allergic mechanisms established experimentally (dust mite, grass models).",
  "Inhaled steroids via mask revolutionized management.",
  "Triggers in pet cats are rarely identified.",
  "Treatment suppresses; it doesn't cure.",
 ],
 "requirements": [
  "Practical individual trigger identification.",
  "Proof that trigger avoidance beats suppression alone.",
  "Understanding of airway remodeling in chronic cases.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Reinero CR et al. Feline asthma models and management. Various; 2004-2012.",
  "Moise NS et al. Clinical and immunological characteristics of feline asthma. Various; 1990s-2000s.",
  "Cohn LA et al. Inhaled therapy for feline asthma. Various; 2010.",
  "Garrity S et al. Feline allergic airway disease. Various; 2015-2020.",
 ],
 "demo_data": {"a": ("asthmatic cats with identified triggers, percent (approx)", 20.0),
               "b": ("percent scale", 100.0), "bounds": (0.1, 0.35),
               "step1": "most asthmatic cats never learn their trigger - therapy suppresses blindly",
               "confirm": "trigger-mapped cats beat suppression-only on control with less drug",
               "refute": "triggers prove unidentifiable in most pet cats"},
},
# ------------------------------------------------------------------ rank 21
{
 "key": "ibd-pets",
 "name": "Chronic GI Disease in Dogs and Cats",
 "group": "Gastroenterology",
 "ladder_rank": 21, "ladder_tier": "compounded",
 "problem": "Chronic vomiting and diarrhea plague dogs and cats - IBD, food-responsive, or lymphoma? Why is the distinction so hard, and what drives the disease?",
 "description": "Chronic enteropathy in dogs and cats - persistent GI signs - divides into food-responsive, antibiotic-responsive, immunosuppressant-responsive (IBD), and intestinal lymphoma. Distinguishing them requires invasive biopsies; histopathology correlates poorly with response; and the drivers (microbiome, diet, immune dysregulation) are unmapped. Treatment is empirical stepping.",
 "background": "The classification (Allenspach, Washabau) organized the field in the 2000s-2010s; the microbiome's role emerged with sequencing. Fecal transplant shows promise anecdotally. But biopsy-response mismatch persists, lymphoma versus IBD distinction challenges pathologists, and no biomarker predicts which therapy will work. As of 2026 treatment remains trial-and-error.",
 "why_it_matters": "Chronic GI disease causes long suffering and expensive workups: predictive biomarkers would replace empirical stepping with targeted therapy.",
 "sig_pointer": "The Signature system's proposed approach predicts treatment response from the microbiome-immune profile, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that chronic enteropathy treatment fails for lack of response prediction: the disease categories are treatment-defined, so predicting the effective treatment from biology would collapse the trial-and-error. "
  "Assumptions: (1) microbiome-immune profiles predict response; (2) the profiles are measurable noninvasively; (3) prediction beats stepping. "
  "Reasoning path: a prediction model explains biopsy-response mismatch and predicts profile-guided therapy will work. "
  "Proposed mechanism: 'response-predicted' enteropathy care - fecal and blood profiling directing first-line therapy. "
  "What would confirm it: profile-guided therapy outperforming empirical stepping in trials. "
  "What would kill it: evidence that profiles don't predict response, or that categories are truly treatment-defined only. "
  "What this does not claim: it does not claim a test exists, does not advise on therapy, and does not constitute veterinary advice."),
 "sig_lens": "The Signature lens reads the vomiting pet as awaiting the right first therapy, and asks what profile would predict it.",
 "how_it_works": "Gastroenterologists study enteropathy through biopsy-response cohorts, microbiome sequencing, fecal-transplant reports, and biomarker discovery.",
 "key_points": [
  "Chronic enteropathy divides by treatment response, not clean biology.",
  "Biopsy findings correlate poorly with which therapy works.",
  "IBD versus intestinal lymphoma challenges pathologists.",
  "The microbiome's role is emerging but unmapped.",
  "Treatment is empirical stepping: diet, antibiotics, immunosuppression.",
 ],
 "requirements": [
  "Noninvasive response-prediction profiles.",
  "Proof that profile-guided therapy beats stepping.",
  "Reliable IBD-versus-lymphoma distinction.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Allenspach K et al. Chronic enteropathies classification. Various; 2007-2016.",
  "Washabau RJ et al. Endoscopic biopsy guidelines. Various; 2010.",
  "Suchodolski JS et al. Gut microbiome in canine enteropathy. Various; 2012-2020.",
  "Jergens AE et al. IBD versus lymphoma. Various; 2005-2015.",
 ],
 "demo_data": {"a": ("enteropathy cases needing biopsy for classification, percent (approx)", 60.0),
               "b": ("percent scale", 100.0), "bounds": (0.45, 0.75),
               "step1": "most cases need invasive biopsy - yet biopsies poorly predict which therapy works",
               "confirm": "profile-guided therapy beats empirical stepping in trials",
               "refute": "profiles prove unable to predict treatment response"},
},
# ------------------------------------------------------------------ rank 22
{
 "key": "exotic-anesthesia",
 "name": "Anesthesia Risk in Exotic Species",
 "group": "Anesthesia",
 "ladder_rank": 22, "ladder_tier": "compounded",
 "problem": "Anesthetizing a rabbit, bird, or reptile is far riskier than a dog - why is exotic anesthesia so dangerous, and what would make it safe?",
 "description": "Exotic pets - rabbits, guinea pigs, birds, reptiles - suffer anesthesia mortality orders of magnitude above dogs and cats. Their physiology (small size, high metabolic rate, stress responses, unique airways) defeats dog-and-cat protocols. Drug dosing is extrapolated, monitoring is miniaturized inadequately, and the evidence base is case series, not trials.",
 "background": "Exotic anesthesia grew as a specialty in the 1990s-2000s (Longley, Hawkins); rabbit anesthesia mortality was quantified as ~1-2% versus ~0.1-0.2% in dogs/cats. Advances - sevoflurane, better monitoring, species-specific protocols - helped but the gap persists. The fundamental problem: physiology varies wildly between species, and each species is a small market for drug and equipment development. As of 2026 exotic anesthesia remains high-risk art.",
 "why_it_matters": "Exotic pets are family members too: their anesthesia risk limits the care they can receive. Safe protocols would extend modern veterinary care to all species.",
 "sig_pointer": "The Signature system's proposed approach builds species-specific physiologic models, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that exotic anesthesia fails on extrapolation: dog-and-cat protocols scaled down can't capture species-specific physiology. "
  "Assumptions: (1) each species needs its own physiologic model; (2) the models are buildable from first principles plus data; (3) model-based protocols beat extrapolated ones. "
  "Reasoning path: a species-model approach explains the persistent mortality gap and predicts model-based protocols will close it. "
  "Proposed mechanism: 'species-modeled' anesthesia - physiologic models per common exotic species driving dosing and monitoring protocols. "
  "What would confirm it: modeled protocols showing lower mortality than extrapolated ones in cohorts. "
  "What would kill it: evidence that stress responses dominate regardless of protocol precision. "
  "What this does not claim: it does not claim safe protocols exist today, does not advise on anesthesia, and does not constitute veterinary advice."),
 "sig_lens": "The Signature lens reads the exotic patient as a unique physiology, not a small dog, and asks what model would dose it correctly.",
 "how_it_works": "Anesthetists study exotic risk through mortality audits, species-specific drug studies, monitoring miniaturization, and protocol comparisons.",
 "key_points": [
  "Rabbit anesthesia mortality is ~10x dog/cat rates.",
  "Drug dosing is extrapolated across wildly different physiologies.",
  "Monitoring equipment is miniaturized inadequately.",
  "The evidence base is case series, not trials.",
  "Each species is a small market for development.",
 ],
 "requirements": [
  "Species-specific physiologic models for common exotics.",
  "Protocols proven against extrapolated ones.",
  "Monitoring designed for small patients, not scaled down.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Longley L. Anaesthesia of Exotic Pets. Saunders; 2008.",
  "Brodbelt DC et al. Anesthesia mortality in rabbits. Various; 2006-2008.",
  "Hawkins MG et al. Exotic anesthesia. Various; 2010-2020.",
  "Lichtenberger M. Small mammal anesthesia. Various; 2004-2012.",
 ],
 "demo_data": {"a": ("rabbit anesthesia mortality, percent (approx)", 1.5),
               "b": ("dog/cat anesthesia mortality, percent (approx)", 0.15), "bounds": (6.0, 15.0),
               "step1": "rabbits die under anesthesia ten times more often than dogs - the extrapolation gap kills",
               "confirm": "modeled protocols beat extrapolated ones on mortality",
               "refute": "stress responses prove to dominate regardless of protocol precision"},
},
# ------------------------------------------------------------------ rank 23
{
 "key": "spillover",
 "name": "Zoonotic Spillover Prediction",
 "group": "One Health",
 "ladder_rank": 23, "ladder_tier": "compounded",
 "problem": "Most human pandemics start in animals - can the next spillover be predicted before it happens?",
 "description": "HIV, Ebola, SARS, COVID-19, H5N1: the major human pandemics are zoonotic. Spillover prediction - identifying which animal viruses will jump, where, and when - is the holy grail of pandemic prevention. Viral discovery catalogs threats; the jump itself depends on ecology, contact, and viral evolution in ways that resist prediction.",
 "background": "PREDICT (USAID, 2009-2020) discovered thousands of animal viruses and built spillover-risk frameworks. The COVID-19 origin debate intensified spillover science. Risk models combine viral traits (receptor use, host range), ecological factors (land-use change, wildlife trade), and human factors (contact intensity). But no model has prospectively predicted a spillover, and the highest-risk interfaces (live-animal markets, deforestation fronts) persist. As of 2026 prediction remains retrospective.",
 "why_it_matters": "Predicting spillover would enable prevention at the source - the cheapest pandemic intervention imaginable, measured against COVID-19's tens of trillions.",
 "sig_pointer": "The Signature system's proposed approach monitors spillover interfaces, not just viruses, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that spillover prediction fails by cataloging viruses while the jump is an interface event: the same virus is harmless without contact and catastrophic with it. "
  "Assumptions: (1) interfaces are mappable and monitorable; (2) viral risk is conditional on interface intensity; (3) interface surveillance predicts jumps. "
  "Reasoning path: an interface model explains why virus catalogs don't predict and predicts that interface monitoring will. "
  "Proposed mechanism: 'interface surveillance' - monitoring high-risk human-animal contact zones for viral traffic, triggering intervention. "
  "What would confirm it: interface surveillance prospectively flagging spillover events. "
  "What would kill it: evidence that jumps are too stochastic for interface prediction, or that interfaces are unmonitorable. "
  "What this does not claim: it does not claim prediction works today, takes no origin position, and does not constitute veterinary or public-health advice."),
 "sig_lens": "The Signature lens reads the pandemic as an interface event, and asks what surveillance of the contact zone would foresee it.",
 "how_it_works": "One Health researchers study spillover through viral discovery, interface ecology, risk modeling, and market and land-use surveillance.",
 "key_points": [
  "Most major human pandemics are zoonotic in origin.",
  "PREDICT (2009-2020) cataloged thousands of animal viruses.",
  "No model has prospectively predicted a spillover.",
  "Risk concentrates at live-animal markets and deforestation fronts.",
  "Viral catalogs don't predict; interfaces might.",
 ],
 "requirements": [
  "Interface surveillance proven to flag jumps prospectively.",
  "Intervention triggers that actually prevent spillover.",
  "Political will to act on predictions.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "USAID PREDICT. Viral discovery program reports. 2009-2020.",
  "Jones KE et al. Global trends in emerging infectious diseases. Nature. 2008;451:990-993.",
  "Allen T et al. Global hotspots and correlates of emerging zoonotic diseases. Nature Communications. 2017;8:1124.",
  "Carlson CJ et al. Climate change and zoonotic spillover. Various; 2022.",
 ],
 "demo_data": {"a": ("human pandemics with zoonotic origin, percent (approx)", 75.0),
               "b": ("percent scale", 100.0), "bounds": (0.6, 0.9),
               "step1": "three-quarters of pandemics start in animals - yet prediction remains retrospective",
               "confirm": "interface surveillance prospectively flags spillover events",
               "refute": "jumps prove too stochastic for interface prediction"},
},
# ------------------------------------------------------------------ rank 24
{
 "key": "novel-species",
 "name": "Veterinary Care for Novel and De-extinct Species",
 "group": "Conservation Medicine",
 "ladder_rank": 24, "ladder_tier": "advanced",
 "problem": "De-extinction and novel-species conservation create patients with no medical literature - how do you practice medicine on a species that never existed?",
 "description": "De-extinction efforts (mammoth, thylacine, dodo projects) and novel conservation hybrids will produce animals with no veterinary baseline: unknown normal physiology, unknown drug responses, unknown diseases. Veterinary medicine has no framework for the unprecedented patient.",
 "background": "De-extinction moved from speculation to funded programs in the 2010s-2020s (Colossal Biosciences and others); the first de-extinct or proxy animals are projected within years. Conservation already manages novel situations (cloned endangered species, hybrids). But veterinary pharmacology, anesthesia, and disease knowledge are species-specific - and the new species will be, by definition, without precedent. As of 2026 no framework exists.",
 "why_it_matters": "The first de-extinct animals will need medical care immediately: building the framework now prevents improvisation later - and the methods will serve every poorly known wild species.",
 "sig_pointer": "The Signature system's proposed approach builds medicine from phylogenetic bracketing, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that novel-species medicine can be built by phylogenetic bracketing: the new animal's physiology is bounded by its nearest relatives, and care protocols can be interpolated. "
  "Assumptions: (1) bracketing relatives are known; (2) physiology interpolates predictably; (3) interpolation beats improvisation. "
  "Reasoning path: a bracketing model provides day-one care protocols for unprecedented patients. "
  "Proposed mechanism: 'bracket-built' formularies - drug doses, anesthetic protocols, and disease expectations interpolated from relatives - refined with each case. "
  "What would confirm it: bracket-built protocols proving safe in the first novel patients. "
  "What would kill it: evidence that novel genomes produce unpredictable physiologies defeating interpolation. "
  "What this does not claim: it does not claim de-extinction will succeed, offers no protocols, and does not constitute veterinary advice."),
 "sig_lens": "The Signature lens reads the unprecedented patient as bracketable, and asks what its relatives would prescribe.",
 "how_it_works": "Conservation vets study novel-species medicine through phylogenetic methods, proxy-species trials, and de-extinction program planning.",
 "key_points": [
  "De-extinction programs are funded and advancing.",
  "The first novel animals will need immediate medical care.",
  "Veterinary knowledge is species-specific; novel species have none.",
  "Cloned endangered species already pose mini-versions of the problem.",
  "No framework exists for the unprecedented patient.",
 ],
 "requirements": [
  "Validated phylogenetic bracketing methods for medicine.",
  "Day-one protocols for the first novel patients.",
  "Learning systems capturing each novel case.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Shapiro B. How to Clone a Mammoth. Princeton University Press; 2015.",
  "Seddon PJ et al. Reversing defaunation and de-extinction. Various; 2014-2020.",
  "Colossal Biosciences. Program reports. 2021 onward.",
  "IUCN. Guiding principles on de-extinction. 2016.",
 ],
 "demo_data": {"a": ("de-extinction projects funded (approx)", 5.0),
               "b": ("veterinary frameworks for novel species", 0.5), "bounds": (6.0, 20.0),
               "step1": "multiple de-extinction projects advance with zero medical frameworks awaiting their patients",
               "confirm": "bracket-built protocols prove safe in the first novel patients",
               "refute": "novel genomes prove to produce unpredictable physiologies"},
},
# ------------------------------------------------------------------ rank 25
{
 "key": "xenotransplant-donor",
 "name": "Xenotransplantation Donor Animal Health",
 "group": "One Health",
 "ladder_rank": 25, "ladder_tier": "advanced",
 "problem": "Pig organs for humans need pathogen-free pigs - what does donor-herd health require, and what are the veterinary challenges?",
 "description": "Xenotransplantation's pig donors must be free of zoonotic pathogens: designated pathogen-free (DPF) herds, PERV-inactivated genetics, lifelong surveillance. The veterinary challenge - maintaining DPF herds at clinical scale, managing the welfare of organ-donor animals, and monitoring for novel pathogens - is a new discipline.",
 "background": "DPF pig facilities were built in the 2010s-2020s (eGenesis, Revivicor and others); PERV inactivation (Niu 2017) removed the headline retrovirus risk. The 2022-2024 pig-to-human transplants used DPF organs. But scale-up needs herds of thousands, welfare standards for donor animals are debated, and surveillance for unknown pathogens is inherently incomplete. As of 2026 donor-herd veterinary medicine is a small, critical specialty.",
 "why_it_matters": "Every xenotransplant depends on its donor herd: herd health is transplant safety, and the veterinary discipline behind it is as important as the surgery.",
 "sig_pointer": "The Signature system's proposed approach treats donor herds as the transplant's first sterile field, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that donor-herd health is transplant safety upstream: the organ's pathogen status is set by herd management, not just final testing. "
  "Assumptions: (1) herd-level exclusion beats organ-level testing; (2) DPF status is maintainable at scale; (3) welfare and sterility are compatible. "
  "Reasoning path: a herd-first model directs investment to facilities and surveillance rather than testing alone. "
  "Proposed mechanism: 'herd-as-sterile-field' standards - facility design, surveillance, and welfare protocols for clinical-scale DPF herds. "
  "What would confirm it: scaled herds maintaining DPF status with transplant safety records. "
  "What would kill it: evidence that DPF status can't be maintained at scale, or that unknown pathogens defeat surveillance. "
  "What this does not claim: it does not claim xenotransplantation is safe, takes no ethical position, and does not constitute veterinary advice."),
 "sig_lens": "The Signature lens reads the donor herd as the operation's first sterile field, and asks what standards would keep it so.",
 "how_it_works": "Researchers study donor-herd health through DPF facility design, PERV monitoring, welfare assessments, and transplant-outcome linkage.",
 "key_points": [
  "DPF herds are the foundation of xenotransplant safety.",
  "PERV inactivation (2017) removed the headline retrovirus risk.",
  "2022-2024 transplants used DPF organs.",
  "Scale-up needs herds of thousands with lifelong surveillance.",
  "Welfare standards for donor animals are debated.",
 ],
 "requirements": [
  "DPF maintenance proven at clinical scale.",
  "Surveillance catching unknown pathogens.",
  "Welfare standards compatible with sterility.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Niu D et al. Inactivation of porcine endogenous retrovirus in pigs using CRISPR-Cas9. Science. 2017;357:1303-1307.",
  "Cooper DKC et al. Xenotransplantation. Various; 2017-2024.",
  "Griffith BP et al. Pig heart transplant. NEJM. 2022;387:35-44.",
  "Fishman JA. Infection in xenotransplantation. Various; 2001-2020.",
 ],
 "demo_data": {"a": ("DPF pigs needed per thousand xenotransplants (approx)", 1000.0),
               "b": ("pigs per thousand (scale)", 1000.0), "bounds": (0.9, 1.1),
               "step1": "each transplant needs its pathogen-free pig - herd scale equals transplant scale",
               "confirm": "scaled herds maintain DPF status with clean transplant safety records",
               "refute": "DPF status proves unmaintainable at clinical scale"},
},
# ------------------------------------------------------------------ rank 26
{
 "key": "cloning-health",
 "name": "Cloning Health Abnormalities",
 "group": "Genetics",
 "ladder_rank": 26, "ladder_tier": "advanced",
 "problem": "Cloned animals suffer high rates of abnormalities - large offspring syndrome, placental defects, premature aging. What goes wrong in cloning, and can it be fixed?",
 "description": "Somatic cell nuclear transfer (SCNT) - Dolly, 1996 - produces live clones at low efficiency with high abnormality rates: large offspring syndrome in ruminants, placental abnormalities, perinatal mortality, and debated premature aging. The cause is epigenetic: the donor nucleus isn't fully reprogrammed, leaving imprinting errors. Efficiency improved but the biology remains incompletely fixed.",
 "background": "Dolly (Wilmut 1997) proved SCNT possible; the abnormalities were catalogued in the 2000s (Hill, Chavatte-Palmer). Epigenetic reprogramming errors - incomplete demethylation, imprinting defects - were identified as the mechanism. Improvements (better oocyte handling, epigenetic modifiers like HDAC inhibitors) raised efficiency modestly. As of 2026 cloning remains inefficient with significant abnormality rates.",
 "why_it_matters": "Cloning serves conservation (endangered species), agriculture (elite genetics), and research: fixing reprogramming would make it reliable - and illuminate epigenetic regulation broadly.",
 "sig_pointer": "The Signature system's proposed approach treats reprogramming as the fixable bottleneck, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that cloning abnormalities are reprogramming failures with identifiable marks: the donor nucleus carries epigenetic memories that specific modifiers can erase. "
  "Assumptions: (1) the failures are epigenetic, not genetic; (2) the marks are mappable; (3) targeted erasure fixes them. "
  "Reasoning path: a reprogramming model explains the abnormality spectrum and predicts that epigenetic conditioning of donor nuclei will work. "
  "Proposed mechanism: 'reprogramming-conditioned' SCNT - donor nuclei epigenetically reset before transfer - tested against abnormality rates. "
  "What would confirm it: conditioned clones showing normal development at higher efficiency. "
  "What would kill it: evidence that reprogramming errors are stochastic and unmappable, or that conditioning doesn't improve outcomes. "
  "What this does not claim: it does not claim cloning is safe today, takes no ethical position, and does not constitute veterinary advice."),
 "sig_lens": "The Signature lens reads the abnormal clone as a nucleus that remembered too much, and asks what erasure would let it start fresh.",
 "how_it_works": "Researchers study cloning through SCNT efficiency trials, epigenetic profiling of clones, and modifier studies.",
 "key_points": [
  "Dolly (1996) proved SCNT; abnormalities were catalogued in the 2000s.",
  "Large offspring syndrome and placental defects are common in ruminant clones.",
  "Incomplete epigenetic reprogramming is the mechanism.",
  "HDAC inhibitors and better handling improved efficiency modestly.",
  "Cloning remains inefficient with significant abnormalities.",
 ],
 "requirements": [
  "Mappable reprogramming-failure marks.",
  "Conditioning protocols proven to normalize development.",
  "Efficiency gains that make cloning reliable.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Wilmut I et al. Viable offspring derived from fetal and adult mammalian cells. Nature. 1997;385:810-813.",
  "Hill JR et al. Clinical and pathologic features of cloned cattle. Various; 2000-2002.",
  "Chavatte-Palmer P et al. Epigenetics and cloning. Various; 2004-2012.",
  "Gurdon JB, Melton DA. Nuclear reprogramming in cells. Science. 2008;322:1811-1815.",
 ],
 "demo_data": {"a": ("cloning efficiency, live births per transfer percent (approx)", 5.0),
               "b": ("percent scale", 100.0), "bounds": (0.02, 0.1),
               "step1": "one in twenty transfers yields a live clone - with abnormalities common among survivors",
               "confirm": "conditioned clones show normal development at higher efficiency",
               "refute": "reprogramming errors prove stochastic and unmappable"},
},
# ------------------------------------------------------------------ rank 27
{
 "key": "chytrid",
 "name": "Chytrid Fungus in Amphibians",
 "group": "Wildlife Disease",
 "ladder_rank": 27, "ladder_tier": "advanced",
 "problem": "A fungus has driven hundreds of amphibian species toward extinction - can chytridiomycosis be stopped in the wild?",
 "description": "Batrachochytrium dendrobatidis (Bd) - the chytrid fungus - has caused the largest disease-driven biodiversity loss in recorded history: hundreds of amphibian declines and extinctions. It disrupts skin osmoregulation, killing frogs. In captivity, antifungals and probiotics (Janthinobacterium) work; in the wild, nothing scales.",
 "background": "Bd was identified as the culprit in 1998 (Berger); its global spread was mapped in the 2000s (Skerratt, Fisher). Mitigation research: antifungal treatment for captive assurance colonies, probiotic bioaugmentation (Harris), environmental manipulation. Some species evolve resistance; others vanish. As of 2026 no wild-scale intervention exists.",
 "why_it_matters": "Amphibians are ecosystem linchpins and the most threatened vertebrate class: stopping Bd would prevent the largest ongoing extinction event.",
 "sig_pointer": "The Signature system's proposed approach treats wild mitigation as an ecological intervention, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that wild Bd mitigation must be ecological: treating individuals can't scale, but shifting pond microbiomes or amphibian resistance might. "
  "Assumptions: (1) environmental reservoirs sustain Bd; (2) microbiome shifts can suppress it; (3) landscape-scale intervention is feasible. "
  "Reasoning path: an ecological model explains captive-wild gaps and predicts bioaugmentation at habitat scale. "
  "Proposed mechanism: 'habitat bioaugmentation' - seeding environments with Bd-suppressive microbes - tested against amphibian survival. "
  "What would confirm it: treated habitats showing amphibian recovery versus controls. "
  "What would kill it: evidence that Bd can't be suppressed environmentally, or that bioaugmentation disrupts ecosystems. "
  "What this does not claim: it does not claim a field intervention exists, takes no conservation position, and does not constitute veterinary advice."),
 "sig_lens": "The Signature lens reads the dying frogs as an ecosystem missing its defenders, and asks what habitat-scale seeding would restore them.",
 "how_it_works": "Wildlife researchers study Bd through surveillance, probiotic trials, resistance-genetics, and captive-assurance programs.",
 "key_points": [
  "Bd caused the largest disease-driven biodiversity loss recorded.",
  "It kills by disrupting skin osmoregulation.",
  "Captivity treatments (antifungals, probiotics) work; wild ones don't scale.",
  "Some species evolve resistance; others go extinct.",
  "No wild-scale intervention exists.",
 ],
 "requirements": [
  "Habitat-scale suppression proven safe and effective.",
  "Understanding of natural resistance evolution.",
  "Interventions that don't disrupt ecosystems further.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Berger L et al. Chytridiomycosis causes amphibian mortality. PNAS. 1998;95(15):9031-9036.",
  "Skerratt LF et al. Spread of chytridiomycosis. Various; 2007.",
  "Fisher MC et al. Global emergence of Bd. Various; 2009-2021.",
  "Harris RN et al. Probiotic bioaugmentation. Various; 2009-2017.",
 ],
 "demo_data": {"a": ("amphibian species in decline from Bd (approx)", 500.0),
               "b": ("amphibian species total (approx thousands)", 8.0), "bounds": (40.0, 90.0),
               "step1": "hundreds of species declining - the worst disease-driven extinction event known",
               "confirm": "treated habitats show amphibian recovery versus controls",
               "refute": "Bd proves environmentally unsuppressible"},
},
# ------------------------------------------------------------------ rank 28
{
 "key": "marine-mammal",
 "name": "Marine Mammal Medicine",
 "group": "Wildlife Medicine",
 "ladder_rank": 28, "ladder_tier": "advanced",
 "problem": "Whales, dolphins, and seals strand, sicken, and die - but marine mammal medicine lacks the diagnostics, drugs, and baselines of land practice. What would close the gap?",
 "description": "Marine mammals present unique challenges: massive size, aquatic physiology (dive responses, blubber pharmacokinetics), stranding emergencies, and diseases (morbillivirus, domoic acid, brucella) with thin evidence bases. Drug dosing is extrapolated; normal blood values are missing for most species; rehabilitation medicine is art.",
 "background": "Marine mammal medicine grew with aquaria and stranding networks (1970s-90s); morbillivirus epizootics (1980s-2000s) drove disease research. Domoic-acid poisoning (sea lions) linked ocean health to neurology. But the evidence base remains thin: few controlled trials, extrapolated pharmacology, and baselines for a fraction of species. As of 2026 the field is expert-driven art.",
 "why_it_matters": "Marine mammals are ecosystem sentinels and conservation icons: their medicine is ocean health made clinical - and strandings demand immediate answers.",
 "sig_pointer": "The Signature system's proposed approach builds the missing baselines systematically, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that marine mammal medicine's gap is baselines: without normal values, drug data, and disease definitions per species, every case is improvisation. "
  "Assumptions: (1) baselines are collectable from healthy managed and wild populations; (2) they transfer to clinical decisions; (3) systematic collection beats case-by-case accumulation. "
  "Reasoning path: a baseline-first model directs the field's limited research capacity at the highest-leverage data. "
  "Proposed mechanism: 'baseline atlases' - systematic physiologic, pharmacologic, and disease references per species - built collaboratively. "
  "What would confirm it: atlas-guided care outperforming expert improvisation on outcomes. "
  "What would kill it: evidence that species variation defeats atlases, or that data can't be collected at scale. "
  "What this does not claim: it does not claim baselines exist today, offers no protocols, and does not constitute veterinary advice."),
 "sig_lens": "The Signature lens reads the stranded whale as a patient without a chart, and asks what atlas would give it one.",
 "how_it_works": "Marine-mammal vets study through stranding networks, managed-population baselines, disease surveillance, and rehabilitation outcome tracking.",
 "key_points": [
  "Drug dosing is extrapolated; normal values missing for most species.",
  "Morbillivirus and domoic acid are major disease threats.",
  "Blubber pharmacokinetics complicate every drug.",
  "The evidence base is case series and expert opinion.",
  "Strandings demand immediate answers without data.",
 ],
 "requirements": [
  "Systematic baseline atlases per species.",
  "Pharmacokinetic data for common drugs.",
  "Disease definitions and diagnostic criteria.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Gulland FMD et al. Marine mammal medicine. Various; 2001-2018.",
  "Van Bonn W. Morbillivirus epizootics. Various; 2000-2015.",
  "Brodie EC et al. Domoic acid poisoning. Various; 2006-2015.",
  "Moore M et al. Stranding medicine. Various; 2010-2020.",
 ],
 "demo_data": {"a": ("marine mammal species with published drug formularies (approx)", 20.0),
               "b": ("marine mammal species (approx)", 130.0), "bounds": (0.1, 0.25),
               "step1": "a fraction of marine mammals have drug data - the rest are dosed by guess",
               "confirm": "atlas-guided care beats expert improvisation on outcomes",
               "refute": "species variation proves to defeat systematic atlases"},
},
# ------------------------------------------------------------------ rank 29
{
 "key": "equine-tendon",
 "name": "Regenerative Medicine for Equine Tendon",
 "group": "Regenerative Medicine",
 "ladder_rank": 29, "ladder_tier": "advanced",
 "problem": "Tendon injuries end racehorses - can stem cells and biologics regenerate tendon, or do they just make expensive scar?",
 "description": "Superficial digital flexor tendon injury is the commonest career-ending injury in racehorses. Healing produces scar with inferior mechanics and high re-injury rates. Regenerative approaches - mesenchymal stem cells, PRP, growth factors - are widely used with thin evidence: some trials show reduced re-injury, others show no benefit over controlled exercise.",
 "background": "Stem-cell tendon therapy began in the 2000s (Smith, Goodship); early case series were promising. Controlled trials since show mixed results: BMAC and cultured MSCs may reduce re-injury versus conventional care, but the regenerated tissue's quality is debated. The biology - tenocyte differentiation, scaffold integration - remains incompletely mapped. As of 2026 regenerative tendon therapy is widely sold on thin evidence.",
 "why_it_matters": "Tendon injury ends athletic careers and often lives: true regeneration would save horses and validate the entire regenerative-medicine enterprise.",
 "sig_pointer": "The Signature system's proposed approach treats tendon regeneration as a mechanics-plus-biology problem, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that tendon regeneration fails without mechanical guidance: cells need the tendon's loading environment to become tendon, and injections without loading protocols make scar. "
  "Assumptions: (1) tenogenesis is mechano-driven; (2) rehabilitation loading is the missing co-therapy; (3) combined cell-plus-loading beats cells alone. "
  "Reasoning path: a mechano-biology model explains mixed trial results - loading wasn't controlled - and predicts combined protocols will work. "
  "Proposed mechanism: 'loaded regeneration' - cell therapy plus defined mechanical loading protocols - tested against re-injury and tissue quality. "
  "What would confirm it: combined protocols beating cells-alone and rehab-alone in trials. "
  "What would kill it: evidence that regenerated tendon can't match native mechanics regardless of loading. "
  "What this does not claim: it does not claim regeneration works today, does not advise on therapy, and does not constitute veterinary advice."),
 "sig_lens": "The Signature lens reads the healing tendon as cells awaiting mechanical instruction, and asks what loading would teach tendon.",
 "how_it_works": "Equine researchers study tendon regeneration through MSC/PRP trials, biomechanical testing, and re-injury cohorts.",
 "key_points": [
  "Tendon injury is the commonest career-ending racehorse injury.",
  "Healing produces inferior scar with high re-injury.",
  "Stem cells and PRP are widely used on thin evidence.",
  "Trials show mixed results versus controlled exercise.",
  "Tissue quality of 'regenerated' tendon is debated.",
 ],
 "requirements": [
  "Combined cell-plus-loading protocols proven in trials.",
  "Tissue-quality measures beyond re-injury rates.",
  "Understanding of tenogenic mechanical signaling.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Smith RKW et al. Stem cell therapy for tendon injury. Various; 2003-2013.",
  "Goodship AE et al. Tendon biology and repair. Various; 2005-2015.",
  "Godwin EE et al. Implantation of bone marrow-derived MSCs. Equine Veterinary Journal. 2012;44(4):382-388.",
  "Dahlgren LA. Regenerative medicine for tendon. Various; 2009-2019.",
 ],
 "demo_data": {"a": ("tendon re-injury rate with conventional care, percent (approx)", 50.0),
               "b": ("percent scale", 100.0), "bounds": (0.35, 0.65),
               "step1": "half of healed tendons re-injure - scar is not tendon",
               "confirm": "combined cell-plus-loading beats either alone on re-injury and tissue quality",
               "refute": "regenerated tendon proves unable to match native mechanics"},
},
# ------------------------------------------------------------------ rank 30
{
 "key": "gene-therapy-animals",
 "name": "Gene Therapy in Animals",
 "group": "Genetics",
 "ladder_rank": 30, "ladder_tier": "advanced",
 "problem": "Gene therapy cures human diseases - why is veterinary gene therapy years behind, and what would bring it to animals?",
 "description": "Veterinary gene therapy lags human: a few successes (RPE65 for canine blindness - the basis of Luxturna; hemophilia dogs), but no broad pipeline. Barriers: smaller markets, species-specific vectors, regulatory paths built for humans, and the ethics of germline versus somatic in breeding animals.",
 "background": "Canine RPE65 gene therapy (Acland, Aguirre, 2001) restored vision and led directly to Luxturna - veterinary research curing human disease. Hemophilia dog models advanced factor-gene therapy. But commercial veterinary gene therapy barely exists: the economics don't support development, and each species needs its own work. As of 2026 the science is proven and the pipeline is empty.",
 "why_it_matters": "Animals suffer genetic diseases too - and veterinary gene therapy would both relieve them and accelerate human translation bidirectionally.",
 "sig_pointer": "The Signature system's proposed approach treats veterinary gene therapy as a platform problem, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that veterinary gene therapy needs platforms, not products: species-adaptable vectors and manufacturing that make each indication affordable. "
  "Assumptions: (1) the biology transfers across species; (2) platform economics beat product economics; (3) regulators will accept platform data. "
  "Reasoning path: a platform model explains why human successes don't translate - each was a bespoke product - and predicts platform approaches will. "
  "Proposed mechanism: 'platform gene therapy' - validated vector-manufacturing platforms adapted per species and indication. "
  "What would confirm it: platform-derived therapies reaching animals at sustainable cost. "
  "What would kill it: evidence that species differences defeat platforms, or that economics can't work at any scale. "
  "What this does not claim: it does not claim therapies exist today, takes no ethical position, and does not constitute veterinary advice."),
 "sig_lens": "The Signature lens reads the empty pipeline as an economics problem wearing a biology costume, and asks what platform would make each cure affordable.",
 "how_it_works": "Researchers study veterinary gene therapy through model-organism successes, vector development, and translational economics.",
 "key_points": [
  "Canine RPE65 therapy (2001) led directly to Luxturna.",
  "Hemophilia dog models advanced human factor therapy.",
  "No broad veterinary gene-therapy pipeline exists.",
  "Each species needs its own vector work.",
  "Economics, not biology, is the main barrier.",
 ],
 "requirements": [
  "Species-adaptable vector platforms.",
  "Manufacturing economics that work for animal markets.",
  "Regulatory paths for veterinary gene therapy.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Acland GM et al. Gene therapy restores vision in a canine model of childhood blindness. Nature Genetics. 2001;28:92-95.",
  "Nathwani AC et al. Hemophilia gene therapy (canine models). Various; 2001-2011.",
  "Miyadera K et al. Veterinary gene therapy reviews. Various; 2012-2020.",
  "Pease A et al. Gene therapy in veterinary medicine. Various; 2015-2022.",
 ],
 "demo_data": {"a": ("approved veterinary gene therapies (approx)", 1.0),
               "b": ("approved human gene therapies (approx)", 10.0), "bounds": (0.05, 0.2),
               "step1": "veterinary gene therapy trails human by an order of magnitude - the science transfers, the economics don't",
               "confirm": "platform-derived therapies reach animals at sustainable cost",
               "refute": "species differences prove to defeat platform approaches"},
},
# ------------------------------------------------------------------ rank 31
{
 "key": "microbiome-animals",
 "name": "Microbiome Transplants in Animals",
 "group": "Microbiology",
 "ladder_rank": 31, "ladder_tier": "advanced",
 "problem": "Fecal transplant works anecdotally in animals - but what is the science, and what would make microbiome therapy reliable?",
 "description": "Fecal microbiota transplant (FMT) is used empirically in horses (colitis), dogs (chronic enteropathy), and ruminants (rumen transfaunation, an old practice). Anecdotes abound; controlled evidence is thin. Donor screening, dosing, delivery, and mechanism are all unstandardized - yet the practice spreads.",
 "background": "Rumen transfaunation is centuries old; modern FMT followed human C. difficile success (2013). Veterinary case series report benefit in equine colitis and canine enteropathy. But no standardized protocols, no donor banks, no dose-response data, and the mechanism (which microbes, which functions) is unknown. As of 2026 veterinary FMT is empirical art.",
 "why_it_matters": "The microbiome drives GI, immune, and metabolic health: reliable transplant therapy would treat diseases that currently defeat medicine.",
 "sig_pointer": "The Signature system's proposed approach defines the transplant by function, not feces, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that FMT works through functions, not species: the therapeutic unit is metabolic capability (fiber fermentation, bile-acid transformation), and defined function-matched consortia will beat raw feces. "
  "Assumptions: (1) functions are identifiable; (2) consortia can be assembled; (3) function-matched beats raw. "
  "Reasoning path: a function model explains anecdotal successes and predicts defined consortia will be reliable. "
  "Proposed mechanism: 'function-defined' microbiome therapy - consortia assembled for specific metabolic functions - tested against raw FMT. "
  "What would confirm it: defined consortia outperforming raw FMT in trials. "
  "What would kill it: evidence that whole-community complexity is irreducible, defeating defined consortia. "
  "What this does not claim: it does not claim FMT works today, does not advise on its use, and does not constitute veterinary advice."),
 "sig_lens": "The Signature lens reads the transplant as functions awaiting definition, and asks which metabolic capabilities carry the cure.",
 "how_it_works": "Researchers study microbiome therapy through FMT case series, consortium assembly, and functional metagenomics.",
 "key_points": [
  "Rumen transfaunation is centuries old; modern FMT follows human success.",
  "Anecdotes support equine colitis and canine enteropathy use.",
  "No standardized protocols, donor banks, or dosing exist.",
  "The therapeutic mechanism is unknown.",
  "Practice spreads ahead of evidence.",
 ],
 "requirements": [
  "Function-defined consortia proven against raw FMT.",
  "Donor screening and dosing standards.",
  "Mechanistic understanding of which functions matter.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Weese JS et al. Fecal transplant in animals. Various; 2013-2020.",
  "Suchodolski JS. Gut microbiome and FMT. Various; 2016-2022.",
  "Mullen KA et al. Equine FMT. Various; 2018-2022.",
  "Pereira AM et al. Rumen transfaunation. Various; 2015-2020.",
 ],
 "demo_data": {"a": ("veterinary FMT protocols standardized", 0.5),
               "b": ("veterinary FMT case series published (approx)", 50.0), "bounds": (0.005, 0.02),
               "step1": "dozens of case series, zero standardized protocols - practice without a science",
               "confirm": "defined consortia beat raw FMT in trials",
               "refute": "whole-community complexity proves irreducible"},
},
# ------------------------------------------------------------------ rank 32
{
 "key": "one-health",
 "name": "One Health Integration Models",
 "group": "One Health",
 "ladder_rank": 32, "ladder_tier": "advanced",
 "problem": "One Health - human, animal, environmental health as one - is endorsed everywhere and integrated nowhere. What would real integration look like?",
 "description": "One Health is official doctrine (WHO, OIE, FAO tripartite): zoonoses, AMR, food safety need integrated surveillance and response. But institutions remain siloed: veterinary and medical surveillance don't share data, funding streams are separate, and 'One Health' is often a label on unchanged programs. No country has a truly integrated system.",
 "background": "One Health's modern form dates to the 2000s (Wildlife Conservation Society's Manhattan Principles, 2004); the tripartite formalized it. Successes are piecemeal: integrated rabies programs, joint outbreak investigations. But surveillance integration - the core - barely exists: animal and human disease data live in incompatible systems. As of 2026 One Health is doctrine without infrastructure.",
 "why_it_matters": "The next pandemic will be zoonotic: integrated surveillance is the difference between catching it in animals and counting it in humans.",
 "sig_pointer": "The Signature system's proposed approach builds integration around shared data infrastructure, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that One Health fails on infrastructure, not will: without shared data systems, integration is exhortation. "
  "Assumptions: (1) data-sharing is the binding constraint; (2) technical integration is feasible; (3) integrated data changes decisions. "
  "Reasoning path: an infrastructure model explains the doctrine-practice gap and predicts that shared surveillance platforms will deliver integration. "
  "Proposed mechanism: 'shared-platform' One Health - interoperable human-animal-environmental surveillance with joint analytics. "
  "What would confirm it: platform regions detecting zoonotic threats earlier than siloed regions. "
  "What would kill it: evidence that institutional incentives defeat technical integration, or that shared data doesn't change decisions. "
  "What this does not claim: it does not claim integration exists today, takes no institutional position, and does not constitute veterinary or public-health advice."),
 "sig_lens": "The Signature lens reads One Health as doctrine awaiting plumbing, and asks what shared infrastructure would make it real.",
 "how_it_works": "One Health researchers study integration through surveillance pilots, institutional analyses, and joint outbreak evaluations.",
 "key_points": [
  "One Health is official WHO/OIE/FAO doctrine.",
  "Veterinary and medical surveillance remain siloed.",
  "Successes (rabies, joint investigations) are piecemeal.",
  "No country has truly integrated surveillance.",
  "'One Health' often labels unchanged programs.",
 ],
 "requirements": [
  "Interoperable surveillance platforms proven in practice.",
  "Joint analytics that change response decisions.",
  "Funding models spanning the silos.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Wildlife Conservation Society. Manhattan Principles. 2004.",
  "WHO/OIE/FAO. Tripartite One Health agreements. Various; 2010-2022.",
  "Zinsstag J et al. One Health economics. Various; 2007-2015.",
  "Gibbs EPJ. The evolution of One Health. Veterinary Record. 2014;174(4):85-91.",
 ],
 "demo_data": {"a": ("countries with integrated One Health surveillance", 0.5),
               "b": ("countries endorsing One Health (approx)", 180.0), "bounds": (0.001, 0.01),
               "step1": "nearly every country endorses One Health; essentially none has integrated surveillance",
               "confirm": "platform regions detect zoonotic threats earlier than siloed regions",
               "refute": "institutional incentives prove to defeat technical integration"},
},
# ------------------------------------------------------------------ rank 33
{
 "key": "pandemic-prediction",
 "name": "Predicting the Next Pandemic from Animal Reservoirs",
 "group": "One Health",
 "ladder_rank": 33, "ladder_tier": "advanced",
 "problem": "COVID-19 cost tens of trillions - can the next animal-origin pandemic be predicted in time to prevent it?",
 "description": "Pandemic prediction from animal reservoirs combines viral discovery, risk ranking, and surveillance: knowing which viruses threaten, where they circulate, and when they move toward humans. The science advanced enormously (PREDICT, risk models), yet COVID-19 wasn't predicted, and no system exists that would predict the next one.",
 "background": "Post-SARS investments built the science: viral discovery catalogs, host-range models, ecological risk maps. But prediction requires the jump's timing - an evolutionary and ecological event - which models can't foresee. The policy question (shut the markets? surveil the farms?) outruns the science. As of 2026 the field can rank risks but not predict events.",
 "why_it_matters": "The next pandemic's cost dwarfs any prediction investment: even imperfect foresight would pay for itself thousands of times over.",
 "sig_pointer": "The Signature system's proposed approach predicts the conditions, not the virus, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that pandemic prediction should target conditions, not viruses: the jump needs a virus plus an interface plus amplification, and the conditions are more predictable than the evolution. "
  "Assumptions: (1) pandemic conditions are identifiable; (2) they precede jumps by actionable time; (3) acting on conditions prevents jumps. "
  "Reasoning path: a conditions model accepts viral unpredictability and predicts on the predictable components. "
  "Proposed mechanism: 'conditions forecasting' - monitoring the convergence of viral presence, interface intensity, and amplification potential. "
  "What would confirm it: conditions forecasts prospectively preceding spillover events. "
  "What would kill it: evidence that conditions add nothing to viral surveillance, or that lead times are unactionable. "
  "What this does not claim: it does not claim prediction works today, takes no origin position, and does not constitute public-health advice."),
 "sig_lens": "The Signature lens reads the pandemic as conditions converging, and asks what forecast would see the convergence coming.",
 "how_it_works": "Researchers study pandemic prediction through risk modeling, interface surveillance, and conditions-monitoring pilots.",
 "key_points": [
  "COVID-19 wasn't predicted despite massive viral-discovery investment.",
  "Risk models rank threats but don't predict events.",
  "The jump's timing is evolutionary and ecological - hard to foresee.",
  "Policy (markets, farms) outruns the science.",
  "Conditions may be more predictable than viruses.",
 ],
 "requirements": [
  "Conditions forecasts validated prospectively.",
  "Actionable lead times from forecast to intervention.",
  "Interventions that work on conditions.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Jones KE et al. Global trends in emerging infectious diseases. Nature. 2008;451:990-993.",
  "Allen T et al. Global hotspots of emerging zoonotic diseases. Nature Communications. 2017;8:1124.",
  "Carlson CJ et al. Climate change increases cross-species viral transmission risk. Nature. 2022;610:510-516.",
  "Holmes EC et al. The ecology of viral emergence. Various; 2021-2023.",
 ],
 "demo_data": {"a": ("COVID-19 cost, trillions of dollars (approx)", 15.0),
               "b": ("trillions scale", 100.0), "bounds": (0.08, 0.25),
               "step1": "tens of trillions lost to an unpredicted pandemic - the cost of no foresight",
               "confirm": "conditions forecasts prospectively precede spillover events",
               "refute": "conditions prove to add nothing to viral surveillance"},
},
# ------------------------------------------------------------------ rank 34
{
 "key": "wildlife-vaccine",
 "name": "Wildlife Disease Vaccination at Scale",
 "group": "Conservation Medicine",
 "ladder_rank": 34, "ladder_tier": "advanced",
 "problem": "Rabies, plague, and chytrid kill wildlife at landscape scale - can wild populations be vaccinated, and what would it take?",
 "description": "Wildlife vaccination works in pockets: oral rabies baits eliminated fox rabies in Western Europe, sylvatic plague vaccine protects prairie dogs (and the ferrets that eat them). But most wildlife diseases lack any scalable intervention: delivery (baits, drones, self-disseminating vaccines), safety, and ecosystem effects are unsolved. Self-spreading vaccines are theoretically powerful and practically alarming.",
 "background": "Oral rabies vaccination (1970s-90s, Europe and North America) is the landmark success. Sylvatic plague vaccine (SPV, 2010s) showed field efficacy for prairie dogs. Chytrid and other threats lack delivery solutions. Self-disseminating vaccines (transmissible) are debated: they could protect inaccessible populations but risk uncontrolled spread. As of 2026 wildlife vaccination is a set of special cases, not a discipline.",
 "why_it_matters": "Wildlife disease drives extinctions and spills over to humans and livestock: scalable vaccination would protect biodiversity and public health together.",
 "sig_pointer": "The Signature system's proposed approach builds a delivery science for wild populations, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that wildlife vaccination is a delivery science: the immunology mostly exists, and the unsolved part is reaching wild populations safely at scale. "
  "Assumptions: (1) delivery is the binding constraint; (2) bait, drone, and vectored delivery can scale; (3) ecosystem safety is assessable. "
  "Reasoning path: a delivery-first model directs investment to the actual bottleneck. "
  "Proposed mechanism: 'wild-delivery' platforms - thermostable baits, drone dispersal, validated safety assessment - tested per disease system. "
  "What would confirm it: delivered vaccines protecting wild populations at landscape scale. "
  "What would kill it: evidence that delivery can't reach sufficient coverage, or that ecosystem risks are unacceptable. "
  "What this does not claim: it does not claim a platform exists, takes no position on transmissible vaccines, and does not constitute veterinary advice."),
 "sig_lens": "The Signature lens reads wildlife disease as a delivery problem, and asks what platform would reach the unreachable.",
 "how_it_works": "Wildlife researchers study vaccination through bait trials, SPV field studies, delivery-technology research, and ecosystem-risk assessment.",
 "key_points": [
  "Oral rabies baits eliminated fox rabies in Western Europe.",
  "Sylvatic plague vaccine protects prairie dogs in field trials.",
  "Most wildlife diseases lack any scalable intervention.",
  "Self-disseminating vaccines are powerful and alarming.",
  "Delivery, not immunology, is usually the barrier.",
 ],
 "requirements": [
  "Delivery platforms proven at landscape scale.",
  "Ecosystem safety assessment frameworks.",
  "Governance for transmissible-vaccine decisions.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Cliquet F et al. Oral rabies vaccination in Europe. Various; 1990-2010.",
  "Rocke TE et al. Sylvatic plague vaccine. Various; 2010-2017.",
  "Basinski AJ et al. Self-disseminating vaccines. Various; 2018-2022.",
  "Cross ML et al. Wildlife vaccination reviews. Various; 2000-2015.",
 ],
 "demo_data": {"a": ("wildlife diseases with landscape-scale vaccination (approx)", 2.0),
               "b": ("wildlife diseases needing it (approx dozens)", 50.0), "bounds": (0.02, 0.08),
               "step1": "two diseases controlled at scale versus dozens needing it - the delivery science barely exists",
               "confirm": "delivered vaccines protect wild populations at landscape scale",
               "refute": "delivery proves unable to reach sufficient coverage"},
},
]


