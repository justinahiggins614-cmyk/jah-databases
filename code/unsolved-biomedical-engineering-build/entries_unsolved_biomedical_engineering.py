#!/usr/bin/env python3
"""Entries for The Unsolved Biomedical Engineering Database (unsolved-biomedical-engineering)
and its Signature half (unsolved-biomedical-engineering-signature).

34 famous unsolved problems in biomedical engineering, ladder-ordered by accessibility
(rank 1 = most approachable, rank 34 = most complex/compounded).
Public half: real, fact-checked problems. Signature half: the same 34
problems through the Signature lens, with Signature-generated proposed
solutions that are ALWAYS labeled as proposals, never established science.

Honesty rule (enforced in every record): never claim proof, never imply
peer acceptance, never present speculation as settled. Signature proposals
are labeled speculation for research discussion only - never medical or
engineering advice, never a design recommendation; no cure claims.
"""

LABEL = "Signature-generated proposed solution \u2014 not established science."

SIG_TAIL = ("Signature editions carry the Signature system's proposed "
            "solution approaches to famous unsolved problems. Every "
            "solution is labeled a Signature-generated proposal, never "
            "established science, never peer-accepted, never proof, never "
            "medical or engineering advice.")

STD_COMMON = [
    "Problem statements verified against the published biomedical-engineering literature; open status confirmed as of 2026.",
    "Signature solution sections are labeled proposals: they state assumptions, a reasoning path, a proposed mechanism, what would confirm or kill them, and what they do not claim.",
    "Signature proposals are labeled speculation for research discussion only - never medical or engineering advice, never a design recommendation; no cure claims appear.",
]

ENTRIES = [
# ------------------------------------------------------------------ rank 1
{
 "key": "artificial-pancreas",
 "name": "The Artificial Pancreas: Closing the Loop",
 "group": "Devices",
 "ladder_rank": 1, "ladder_tier": "foundations",
 "problem": "Automated insulin delivery works - but the fully closed loop, handling meals and exercise without user input, remains elusive. What's missing?",
 "description": "Hybrid closed-loop systems (Medtronic 670G/780G, Tandem Control-IQ) automate basal insulin; but meal boluses still need user input, exercise disrupts control, and sensor lag limits responsiveness. The fully closed loop - no carb counting, no announcements - is the goal.",
 "background": "The artificial-pancreas concept dates to the 1970s; continuous glucose monitors enabled the modern era; hybrid loops were approved in the late 2010s. Dual-hormone (insulin+glucagon) systems are in trials. As of 2026 hybrid loops are standard with full closure pending.",
 "why_it_matters": "Full closure would free type 1 diabetics from constant management: the device that thinks like a pancreas.",
 "sig_pointer": "The Signature system's proposed approach closes the loop fully, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that full closure needs meal-and-exercise prediction: the algorithms anticipating disturbances - with faster sensing closing the lag. "
  "Assumptions: (1) disturbances are predictable; (2) sensing can be faster; (3) algorithms handle them. "
  "Reasoning path: a prediction model explains hybrid limits and predicts full closure. "
  "Proposed mechanism: 'predictively-closed' loops - disturbance-anticipating control. "
  "What would confirm it: full-closure trials without user input. "
  "What would kill it: evidence that meals are unpredictable. "
  "What this does not claim: it does not claim full closure exists, offers no medical advice, and does not constitute a device recommendation."),
 "sig_lens": "The Signature lens reads hybrid loops as prediction-limited, and asks what anticipation would close.",
 "how_it_works": "Researchers study artificial pancreases through closed-loop trials, dual-hormone research, and algorithm development.",
 "key_points": [
  "Hybrid loops automate basal insulin.",
  "Meals still need user-announced boluses.",
  "Exercise disrupts glycemic control.",
  "Sensor lag limits responsiveness.",
  "Dual-hormone systems are in trials.",
 ],
 "requirements": [
  "Meal-and-exercise prediction algorithms.",
  "Faster glucose sensing.",
  "Full-closure trials without input.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Bergenstal RM et al. Hybrid closed-loop trials. Various; 2016-2021.",
  "Brown SA et al. Control-IQ studies. Various; 2019-2021.",
  "El-Khatib FH et al. Dual-hormone systems. Various; 2010-2017.",
  "Bekiari E et al. Artificial pancreas reviews. Various; 2018-2022.",
 ],
 "demo_data": {"a": ("time in range, hybrid loop, percent (approx)", 70.0),
               "b": ("percent scale", 100.0), "bounds": (0.6, 0.8),
               "step1": "seventy percent in range - with the remaining thirty needing the full loop",
               "confirm": "full-closure trials without user input",
               "refute": "meals prove unpredictable"},
},
# ------------------------------------------------------------------ rank 2
{
 "key": "neural-interfaces",
 "name": "Brain-Computer Interfaces: The Bandwidth Problem",
 "group": "Neuroengineering",
 "ladder_rank": 2, "ladder_tier": "foundations",
 "problem": "BCIs restore communication - but bandwidth is tiny compared to natural movement. Can neural interfaces scale?",
 "description": "Brain-computer interfaces (Utah arrays, Neuralink, Synchron) - decode movement and speech from neural signals; but channel counts (hundreds) are dwarfed by the brain's billions; long-term electrode stability is poor; and the decoding ceiling is unknown.",
 "background": "Motor BCIs (2000s-2010s, Hochberg, Donoghue) restored cursor control; speech decoding (2020s, Chang, Willett) advanced rapidly; Neuralink and Synchron pursue higher bandwidth. As of 2026 BCIs work clinically with scaling pending.",
 "why_it_matters": "Scaled BCIs would restore full communication and movement: the bandwidth to normalcy.",
 "sig_pointer": "The Signature system's proposed approach scales neural interfaces, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that BCI scaling needs stable high-channel interfaces: the electrode longevity and decoding that grow bandwidth - with biology cooperating. "
  "Assumptions: (1) stability is achievable; (2) decoding scales; (3) the brain adapts. "
  "Reasoning path: a scaling model explains current limits and predicts high-bandwidth BCIs. "
  "Proposed mechanism: 'stably-scaled' neural interfaces - durable high-channel recording. "
  "What would confirm it: long-term high-bandwidth clinical BCIs. "
  "What would kill it: evidence that electrodes inherently degrade. "
  "What this does not claim: it does not claim scaled BCIs exist, offers no medical advice, and does not constitute a device recommendation."),
 "sig_lens": "The Signature lens reads BCIs as stability-limited, and asks what durable interfaces would scale.",
 "how_it_works": "Researchers study BCIs through clinical trials, electrode-longevity research, and decoding advances.",
 "key_points": [
  "BCIs restore cursor control and speech.",
  "Channel counts are hundreds vs billions of neurons.",
  "Electrode stability degrades over years.",
  "Speech decoding advanced rapidly in the 2020s.",
  "The scaling path is unproven.",
 ],
 "requirements": [
  "Durable high-channel electrodes.",
  "Scaling decoding algorithms.",
  "Long-term clinical bandwidth.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Hochberg LR et al. Motor BCI trials. Various; 2006-2012.",
  "Willett FR et al. Speech decoding. Various; 2021-2023.",
  "Neuralink / Synchron programs. Various; 2019 onward.",
  "Lebedev MA et al. BCI reviews. Various; 2017-2022.",
 ],
 "demo_data": {"a": ("BCI channels (approx)", 1000.0),
               "b": ("cortical neurons (approx billions)", 16.0), "bounds": (40.0, 90.0),
               "step1": "a thousand channels against sixteen billion neurons - the bandwidth gap",
               "confirm": "long-term high-bandwidth clinical BCIs",
               "refute": "electrodes prove to inherently degrade"},
},
# ------------------------------------------------------------------ rank 3
{
 "key": "tissue-engineering",
 "name": "Tissue Engineering: Growing Organs",
 "group": "Regenerative",
 "ladder_rank": 3, "ladder_tier": "foundations",
 "problem": "Tissue engineering grows skin and cartilage - but vascularized solid organs remain out of reach. What blocks the organ?",
 "description": "Tissue engineering - scaffolds plus cells - succeeded for thin tissues (skin, cartilage, bladders); but solid organs need vasculature: diffusion limits thickness to millimeters. Bioprinting, decellularized scaffolds, and organoids each address pieces; no engineered solid organ transplants.",
 "background": "The field launched in the 1990s (Langer, Vacanti); bladder transplants (Atala, 2006) were the high-water mark; organoids (2010s) modeled development. As of 2026 vascularization is the barrier.",
 "why_it_matters": "Engineered organs would end transplant waiting lists: the regenerative prize.",
 "sig_pointer": "The Signature system's proposed approach vascularizes engineered tissue, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that organ engineering needs vasculature first: the perfusable vascular networks grown before parenchyma - with printing and biology combined. "
  "Assumptions: (1) vasculature is the barrier; (2) it is engineerable; (3) organs follow. "
  "Reasoning path: a vasculature-first model explains thin-tissue success and predicts solid organs. "
  "Proposed mechanism: 'vascularized-first' organ engineering - perfusable scaffolds. "
  "What would confirm it: transplanted vascularized engineered organs. "
  "What would kill it: evidence that vascularization is insurmountable. "
  "What this does not claim: it does not claim engineered organs exist, offers no medical advice, and does not constitute a research recommendation."),
 "sig_lens": "The Signature lens reads organ engineering as vasculature-limited, and asks what perfusable scaffolds would grow.",
 "how_it_works": "Researchers study tissue engineering through bioprinting, decellularization, and vascularization research.",
 "key_points": [
  "Thin tissues (skin, cartilage, bladder) succeeded.",
  "Diffusion limits thickness to millimeters.",
  "Vascularization is the barrier.",
  "Bioprinting and organoids address pieces.",
  "No engineered solid organ transplants.",
 ],
 "requirements": [
  "Perfusable vascular networks.",
  "Transplanted engineered organs.",
  "Scaled organ manufacturing.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Langer R, Vacanti JP. Tissue engineering. Science. 1993;260:920-926.",
  "Atala A et al. Engineered bladders. Lancet. 2006;367:1215-1216.",
  "Murphy SV, Atala A. Bioprinting reviews. Various; 2014-2020.",
  "Lancaster MA et al. Organoids. Various; 2013-2019.",
 ],
 "demo_data": {"a": ("organ-transplant waiting list, thousands (approx)", 100.0),
               "b": ("engineered solid-organ transplants", 0.5), "bounds": (150.0, 250.0),
               "step1": "a hundred thousand waiting, zero engineered organs - the vascularization gap",
               "confirm": "transplanted vascularized engineered organs",
               "refute": "vascularization proves insurmountable"},
},
# ------------------------------------------------------------------ rank 4
{
 "key": "drug-delivery",
 "name": "Targeted Drug Delivery: The Magic Bullet",
 "group": "Devices",
 "ladder_rank": 4, "ladder_tier": "foundations",
 "problem": "Drugs flood the body to reach one site - can delivery be targeted precisely enough to transform therapy?",
 "description": "Targeted drug delivery - nanoparticles, antibody-drug conjugates, implantable pumps - aims to concentrate drugs at disease sites; but targeting efficiency is low (most nanoparticles miss), barriers (blood-brain, tumor) resist, and the field advances incrementally.",
 "background": "Liposomal drugs (1990s) were the first success; antibody-drug conjugates (2010s) improved targeting; nanoparticle tumor delivery remains inefficient. As of 2026 targeting is improved but not transformative.",
 "why_it_matters": "Precise delivery would multiply drug efficacy while cutting side effects: the pharmacological revolution.",
 "sig_pointer": "The Signature system's proposed approach makes delivery truly targeted, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that drug delivery needs barrier-crossing targeting: the designs that reach brain, tumor core, and intracellular targets - with measured delivery efficiency. "
  "Assumptions: (1) barriers are crossable; (2) targeting is improvable; (3) efficiency is measurable. "
  "Reasoning path: a barrier model explains incremental progress and predicts transformative delivery. "
  "Proposed mechanism: 'barrier-crossing' targeted delivery - designed penetration. "
  "What would confirm it: measured high-efficiency targeted delivery in trials. "
  "What would kill it: evidence that barriers defeat targeting. "
  "What this does not claim: it does not claim transformative delivery exists, offers no medical advice, and does not constitute a design recommendation."),
 "sig_lens": "The Signature lens reads drug delivery as barrier-limited, and asks what designs would cross them.",
 "how_it_works": "Researchers study drug delivery through nanoparticle research, ADC development, and barrier-crossing studies.",
 "key_points": [
  "Most nanoparticles miss their targets.",
  "Blood-brain and tumor barriers resist.",
  "ADCs improved targeting incrementally.",
  "Targeting efficiency is low.",
  "Transformative delivery is pending.",
 ],
 "requirements": [
  "High-efficiency targeted delivery.",
  "Barrier-crossing designs proven.",
  "Clinical transformative outcomes.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Peer D et al. Nanoparticle delivery reviews. Various; 2007-2020.",
  "Beck A et al. Antibody-drug conjugates. Various; 2017-2022.",
  "Wilhelm S et al. Nanoparticle tumor delivery. Various; 2016-2021.",
  "Vargason AM et al. Delivery reviews. Various; 2021-2023.",
 ],
 "demo_data": {"a": ("injected nanoparticle dose reaching tumors, percent (approx)", 1.0),
               "b": ("percent scale", 100.0), "bounds": (0.005, 0.02),
               "step1": "one percent reaches the tumor - the targeting efficiency gap",
               "confirm": "measured high-efficiency targeted delivery in trials",
               "refute": "barriers prove to defeat targeting"},
},
# ------------------------------------------------------------------ rank 5
{
 "key": "prosthetics",
 "name": "Prosthetics: The Natural Limb",
 "group": "Devices",
 "ladder_rank": 5, "ladder_tier": "foundations",
 "problem": "Prosthetic limbs restore function - but not sensation, fine control, or embodiment. Can prosthetics become natural?",
 "description": "Advanced prosthetics (myoelectric arms, microprocessor knees) - restore remarkable function; but sensory feedback is absent, control is coarse, and embodiment (feeling the limb as self) is rare. Osseointegration and neural interfaces promise more.",
 "background": "Myoelectric control (1960s-70s) enabled arm prosthetics; microprocessor knees (1990s-2000s) transformed legs; targeted muscle reinnervation (Kuiken, 2000s) improved control. As of 2026 prosthetics are functional but not natural.",
 "why_it_matters": "Natural prosthetics would restore wholeness: the difference between tool and limb.",
 "sig_pointer": "The Signature system's proposed approach makes prosthetics natural, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that natural prosthetics need bidirectional interfaces: the motor control plus sensory feedback - with embodiment engineered. "
  "Assumptions: (1) bidirectionality is achievable; (2) it produces embodiment; (3) it is durable. "
  "Reasoning path: a bidirectional model explains current limits and predicts natural limbs. "
  "Proposed mechanism: 'bidirectional' prosthetics - control plus sensation. "
  "What would confirm it: embodied prosthetics in long-term use. "
  "What would kill it: evidence that embodiment can't be engineered. "
  "What this does not claim: it does not claim natural prosthetics exist, offers no medical advice, and does not constitute a device recommendation."),
 "sig_lens": "The Signature lens reads prosthetics as one-directional, and asks what feedback would naturalize.",
 "how_it_works": "Researchers study prosthetics through neural-interface trials, sensory-feedback research, and osseointegration studies.",
 "key_points": [
  "Myoelectric and microprocessor prosthetics restore function.",
  "Sensory feedback is largely absent.",
  "Control remains coarse versus natural limbs.",
  "Embodiment is rare.",
  "Bidirectional interfaces are the frontier.",
 ],
 "requirements": [
  "Durable bidirectional interfaces.",
  "Embodied prosthetics in long-term use.",
  "Natural-feeling control and sensation.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Kuiken TA et al. Targeted muscle reinnervation. Various; 2004-2009.",
  "Ortiz-Catalan M et al. Osseointegration. Various; 2014-2020.",
  "Raspopovic S et al. Sensory feedback. Various; 2014-2021.",
  "Farina D et al. Prosthetic control reviews. Various; 2017-2022.",
 ],
 "demo_data": {"a": ("upper-limb amputees with sensory feedback (approx)", 5.0),
               "b": ("upper-limb amputees with prosthetics, percent (approx)", 80.0), "bounds": (0.04, 0.1),
               "step1": "function without feeling - the sensory gap in modern prosthetics",
               "confirm": "embodied prosthetics in long-term use",
               "refute": "embodiment proves un-engineerable"},
},
# ------------------------------------------------------------------ rank 6
{
 "key": "biosensors",
 "name": "Continuous Biosensors: Beyond Glucose",
 "group": "Devices",
 "ladder_rank": 6, "ladder_tier": "foundations",
 "problem": "Continuous glucose monitors transformed diabetes - can continuous sensing extend to other molecules?",
 "description": "Continuous biosensors - real-time molecular monitoring - succeeded for glucose; but lactate, cortisol, drugs, and biomarkers lack continuous sensors. Biofouling, calibration drift, and biocompatibility challenge long-term implants.",
 "background": "CGM (2000s-2010s) proved the concept; microneedle and aptamer sensors are emerging; long-term implantables face foreign-body response. As of 2026 glucose stands nearly alone.",
 "why_it_matters": "Continuous molecular monitoring would transform medicine: the vital signs of biochemistry.",
 "sig_pointer": "The Signature system's proposed approach generalizes continuous sensing, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that continuous sensing generalizes: the anti-fouling, calibration-free platforms that extend CGM's success to other molecules. "
  "Assumptions: (1) platforms generalize; (2) fouling is solvable; (3) calibration drifts are correctable. "
  "Reasoning path: a platform model explains glucose's lonely success and predicts multi-analyte sensing. "
  "Proposed mechanism: 'platform-generalized' biosensors - multi-molecule continuous monitoring. "
  "What would confirm it: non-glucose continuous sensors in clinical use. "
  "What would kill it: evidence that each molecule needs bespoke solutions. "
  "What this does not claim: it does not claim multi-analyte sensors exist, offers no medical advice, and does not constitute a device recommendation."),
 "sig_lens": "The Signature lens reads biosensing as one-molecule success, and asks what platforms would generalize.",
 "how_it_works": "Researchers study biosensors through aptamer-sensor research, anti-fouling materials, and microneedle platforms.",
 "key_points": [
  "CGM transformed diabetes management.",
  "Other molecules lack continuous sensors.",
  "Biofouling and drift challenge implants.",
  "Aptamer and microneedle platforms are emerging.",
  "Glucose stands nearly alone.",
 ],
 "requirements": [
  "Generalized sensing platforms.",
  "Non-glucose sensors in clinical use.",
  "Long-term implantable stability.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Klonoff DC et al. CGM reviews. Various; 2017-2022.",
  "Arroyo-Mora LE et al. Aptamer sensors. Various; 2020-2023.",
  "Tehrani F et al. Microneedle sensors. Various; 2022-2024.",
  "Bandodkar AJ et al. Wearable biosensors. Various; 2019-2023.",
 ],
 "demo_data": {"a": ("molecules with continuous clinical sensors (approx)", 2.0),
               "b": ("clinically important molecules (approx)", 50.0), "bounds": (0.02, 0.08),
               "step1": "two sensed of fifty important - the unmonitored biochemistry",
               "confirm": "non-glucose continuous sensors in clinical use",
               "refute": "each molecule proves to need bespoke solutions"},
},
# ------------------------------------------------------------------ rank 7
{
 "key": "organ-chips",
 "name": "Organs on Chips: Replacing Animal Testing",
 "group": "Models",
 "ladder_rank": 7, "ladder_tier": "foundations",
 "problem": "Organ chips model human physiology - but can they predict drug responses well enough to replace animal testing?",
 "description": "Organs-on-chips - microfluidic human-tissue models - promise better drug testing; but validation against human outcomes is incomplete, multi-organ integration is early, and regulatory acceptance is growing slowly (FDA Modernization Act 2.0, 2022).",
 "background": "The Wyss Institute pioneered chips (2010s); the field grew rapidly; regulatory acceptance began. As of 2026 chips supplement but don't replace animal testing.",
 "why_it_matters": "Validated chips would make drug testing human-relevant: better predictions, fewer animals.",
 "sig_pointer": "The Signature system's proposed approach validates chips against human outcomes, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that chips need outcome validation: the predictions tested against human drug responses - with regulatory qualification. "
  "Assumptions: (1) chips predict human responses; (2) validation is feasible; (3) regulators qualify. "
  "Reasoning path: a validation model explains slow replacement and predicts chip-based testing. "
  "Proposed mechanism: 'outcome-validated' organs-on-chips - qualified predictive models. "
  "What would confirm it: chips predicting human outcomes in qualification. "
  "What would kill it: evidence that chips can't predict systemically. "
  "What this does not claim: it does not claim chips replace animals, offers no medical advice, and does not constitute a regulatory recommendation."),
 "sig_lens": "The Signature lens reads chips as unvalidated promise, and asks what outcome proof would qualify.",
 "how_it_works": "Researchers study organ chips through validation studies, multi-organ integration, and regulatory science.",
 "key_points": [
  "Chips model human tissue microenvironments.",
  "Validation against human outcomes is incomplete.",
  "Multi-organ integration is early.",
  "FDA Modernization Act 2.0 opened the door.",
  "Chips supplement, don't replace, animal testing.",
 ],
 "requirements": [
  "Outcome-validated predictions.",
  "Regulatory qualification.",
  "Multi-organ systemic modeling.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Huh D et al. Lung-on-a-chip. Science. 2010;328:1662-1668.",
  "Wyss Institute. Organ-chip program. Various; 2012 onward.",
  "FDA Modernization Act 2.0. 2022.",
  "Low LA et al. Chip validation reviews. Various; 2020-2023.",
 ],
 "demo_data": {"a": ("drugs tested on chips before animals, percent (approx)", 10.0),
               "b": ("percent scale", 100.0), "bounds": (0.05, 0.18),
               "step1": "one in ten drugs sees a chip first - the unvalidated alternative",
               "confirm": "chips predict human outcomes in qualification",
               "refute": "chips prove unable to predict systemically"},
},
# ------------------------------------------------------------------ rank 8
{
 "key": "biocompatibility",
 "name": "Biocompatibility: The Foreign-Body Problem",
 "group": "Materials",
 "ladder_rank": 8, "ladder_tier": "foundations",
 "problem": "Implants trigger foreign-body responses - fibrosis, rejection, failure. Can materials truly integrate with the body?",
 "description": "Biocompatibility - the body's acceptance of implants - remains imperfect: fibrous encapsulation degrades sensors and devices; the foreign-body response is incompletely understood; truly biointegrative materials are the goal.",
 "background": "Silicone and titanium proved biocompatible enough; the foreign-body response was characterized (Anderson, 2000s-2010s); zwitterionic and immunomodulatory materials promise better. As of 2026 encapsulation still limits devices.",
 "why_it_matters": "True biointegration would make implants permanent: the material foundation of all implantable medicine.",
 "sig_pointer": "The Signature system's proposed approach engineers biointegration, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that biointegration is engineerable: the immunomodulatory materials that instruct acceptance - not just tolerance. "
  "Assumptions: (1) the response is instructable; (2) materials can instruct; (3) integration is durable. "
  "Reasoning path: an instruction model explains encapsulation and predicts biointegrative implants. "
  "Proposed mechanism: 'instructional' biomaterials - immune-instructing implants. "
  "What would confirm it: long-term unencapsulated implants in trials. "
  "What would kill it: evidence that the foreign-body response is inevitable. "
  "What this does not claim: it does not claim biointegrative materials exist, offers no medical advice, and does not constitute a materials recommendation."),
 "sig_lens": "The Signature lens reads encapsulation as uninstructed immunity, and asks what materials would teach acceptance.",
 "how_it_works": "Researchers study biocompatibility through foreign-body research, immunomodulatory materials, and long-term implant studies.",
 "key_points": [
  "Fibrous encapsulation degrades implants.",
  "The foreign-body response is incompletely understood.",
  "Silicone and titanium are tolerated, not integrated.",
  "Immunomodulatory materials promise more.",
  "True biointegration is unachieved.",
 ],
 "requirements": [
  "Immunomodulatory materials proven.",
  "Long-term unencapsulated implants.",
  "Durable biointegration.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Anderson JM et al. Foreign-body response. Various; 2008-2016.",
  "Zhang L et al. Zwitterionic materials. Various; 2013-2019.",
  "Veiseh O et al. Immunomodulatory implants. Various; 2015-2020.",
  "Ratner BD et al. Biomaterials reviews. Various; 2004-2019.",
 ],
 "demo_data": {"a": ("implantable sensors failing from encapsulation, percent (approx)", 40.0),
               "b": ("percent scale", 100.0), "bounds": (0.28, 0.52),
               "step1": "two in five sensors lost to scar tissue - the body's rejection of the foreign",
               "confirm": "long-term unencapsulated implants in trials",
               "refute": "the foreign-body response proves inevitable"},
},
# ------------------------------------------------------------------ rank 9
{
 "key": "heart-valves",
 "name": "Heart Valves That Last a Lifetime",
 "group": "Devices",
 "ladder_rank": 9, "ladder_tier": "foundations",
 "problem": "Mechanical valves last but need anticoagulation; tissue valves don't but wear out. Can a valve do both?",
 "description": "Heart-valve prostheses - the tradeoff: mechanical (durable, thrombogenic) versus bioprosthetic (non-thrombogenic, degenerating). Tissue-engineered valves promise living replacements; polymer valves are in trials. No lifetime valve exists.",
 "background": "Mechanical valves (1960s) and bioprostheses (1970s) established the tradeoff; TAVR (2010s) transformed delivery; tissue-engineered valves are in early trials. As of 2026 the tradeoff persists.",
 "why_it_matters": "A lifetime valve would end reoperations: the definitive cardiac implant.",
 "sig_pointer": "The Signature system's proposed approach grows living valves, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that lifetime valves are living: the tissue-engineered valves that grow, repair, and last - proven in trials. "
  "Assumptions: (1) living valves are engineerable; (2) they last; (3) they are safe. "
  "Reasoning path: a living-valve model explains the tradeoff and predicts its end. "
  "Proposed mechanism: 'living' heart valves - tissue-engineered lifetime replacements. "
  "What would confirm it: tissue-engineered valves lasting decades. "
  "What would kill it: evidence that engineered valves degenerate. "
  "What this does not claim: it does not claim lifetime valves exist, offers no medical advice, and does not constitute a device recommendation."),
 "sig_lens": "The Signature lens reads valve choice as forced tradeoff, and asks what living tissue would resolve.",
 "how_it_works": "Researchers study heart valves through tissue-engineering trials, polymer-valve studies, and durability research.",
 "key_points": [
  "Mechanical valves need lifelong anticoagulation.",
  "Tissue valves degenerate in 10-15 years.",
  "TAVR transformed delivery.",
  "Tissue-engineered valves are in early trials.",
  "No lifetime valve exists.",
 ],
 "requirements": [
  "Tissue-engineered valves in trials.",
  "Decades-long durability proven.",
  "Living valves as standard care.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Yoganathan AP et al. Valve mechanics. Various; 2004-2019.",
  "Nishimura RA et al. Valve guidelines. Various; 2014-2021.",
  "Emmert MY et al. Tissue-engineered valves. Various; 2018-2022.",
  "Baumgartner H et al. Valve reviews. Various; 2017-2021.",
 ],
 "demo_data": {"a": ("tissue-valve lifespan, years (approx)", 12.0),
               "b": ("patient lifespan after implant, years (approx)", 25.0), "bounds": (0.35, 0.62),
               "step1": "valves lasting half the patient's remaining life - the reoperation guarantee",
               "confirm": "tissue-engineered valves last decades",
               "refute": "engineered valves prove to degenerate"},
},
# ------------------------------------------------------------------ rank 10
{
 "key": "dialysis",
 "name": "Beyond Dialysis: The Artificial Kidney",
 "group": "Devices",
 "ladder_rank": 10, "ladder_tier": "foundations",
 "problem": "Dialysis keeps millions alive but poorly - can an artificial kidney replace it?",
 "description": "Dialysis - life-sustaining but burdensome: 3x weekly sessions, poor quality of life, high mortality. Implantable bioartificial kidneys (UCSF), wearable devices, and xenotransplantation are the alternatives; all are developmental.",
 "background": "Dialysis (1960s) became standard; the Kidney Project (UCSF, 2010s-2020s) develops implantables; wearable artificial kidneys are in trials. As of 2026 dialysis remains dominant.",
 "why_it_matters": "An artificial kidney would free millions from dialysis: the most burdensome chronic therapy.",
 "sig_pointer": "The Signature system's proposed approach builds the implantable kidney, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that the artificial kidney is buildable: the bioartificial implantables proven - with hemofilter plus bioreactor. "
  "Assumptions: (1) the components work; (2) they integrate; (3) implants are safe. "
  "Reasoning path: a components model explains the development status and predicts implantable kidneys. "
  "Proposed mechanism: 'bioartificial' implantable kidneys - proven replacements. "
  "What would confirm it: implantable kidneys in clinical trials. "
  "What would kill it: evidence that bioartificial kidneys can't scale. "
  "What this does not claim: it does not claim artificial kidneys exist, offers no medical advice, and does not constitute a device recommendation."),
 "sig_lens": "The Signature lens reads dialysis as unreplaced burden, and asks what implantables would free.",
 "how_it_works": "Researchers study artificial kidneys through the Kidney Project, wearable trials, and xenotransplant research.",
 "key_points": [
  "Dialysis is burdensome with high mortality.",
  "Bioartificial kidneys are in development.",
  "Wearable devices are in trials.",
  "Xenotransplantation is an alternative path.",
  "Dialysis remains dominant.",
 ],
 "requirements": [
  "Implantable kidneys in trials.",
  "Proven safety and function.",
  "Dialysis replacement at scale.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "UCSF Kidney Project. Various; 2010 onward.",
  "Gura V et al. Wearable artificial kidney. Various; 2016-2020.",
  "Roy S et al. Bioartificial kidney. Various; 2015-2022.",
  "USRDS. Dialysis statistics. Annual.",
 ],
 "demo_data": {"a": ("dialysis patient 5-year survival, percent (approx)", 40.0),
               "b": ("percent scale", 100.0), "bounds": (0.3, 0.52),
               "step1": "fewer than half survive five years - the therapy that sustains but doesn't save",
               "confirm": "implantable kidneys in clinical trials",
               "refute": "bioartificial kidneys prove unable to scale"},
},
# ------------------------------------------------------------------ rank 11
{
 "key": "imaging-agents",
 "name": "Targeted Imaging Agents",
 "group": "Imaging",
 "ladder_rank": 11, "ladder_tier": "foundations",
 "problem": "Medical imaging sees anatomy - but targeted agents could reveal molecular disease. What's blocking molecular imaging's expansion?",
 "description": "Targeted imaging agents - molecular probes for PET, MRI, optical - promise disease-specific visualization; but development is slow, regulatory paths are hard, and most imaging remains anatomical. The agents exist for few targets.",
 "background": "FDG-PET was the breakthrough; targeted agents (PSMA, amyloid) followed slowly; optical agents are emerging. As of 2026 molecular imaging covers few targets.",
 "why_it_matters": "Molecular imaging would make diagnosis specific: seeing the disease, not its shadow.",
 "sig_pointer": "The Signature system's proposed approach expands targeted imaging systematically, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that targeted agents need systematic expansion: the target-to-agent pipelines industrialized - with regulatory paths streamlined. "
  "Assumptions: (1) pipelines are industrializable; (2) regulation can streamline; (3) expansion follows. "
  "Reasoning path: a pipeline model explains slow growth and predicts broad molecular imaging. "
  "Proposed mechanism: 'industrialized' imaging-agent development - systematic target coverage. "
  "What would confirm it: agents for many targets in clinical use. "
  "What would kill it: evidence that each agent is irreducibly bespoke. "
  "What this does not claim: it does not claim broad agents exist, offers no medical advice, and does not constitute a development recommendation."),
 "sig_lens": "The Signature lens reads molecular imaging as artisanal, and asks what industrialization would cover.",
 "how_it_works": "Researchers study imaging agents through probe chemistry, PSMA/amyloid translation, and regulatory science.",
 "key_points": [
  "Most imaging remains anatomical.",
  "Targeted agents exist for few targets.",
  "Development is slow and bespoke.",
  "Regulatory paths are difficult.",
  "PSMA and amyloid show the potential.",
 ],
 "requirements": [
  "Industrialized agent pipelines.",
  "Agents for many targets.",
  "Streamlined regulatory paths.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Gambhir SS et al. Imaging-agent reviews. Various; 2002-2015.",
  "Hofman MS et al. PSMA agents. Various; 2018-2021.",
  "Weissleder R et al. Molecular imaging. Various; 2010-2020.",
  "Kobayashi H et al. Optical agents. Various; 2018-2022.",
 ],
 "demo_data": {"a": ("molecular imaging targets in routine use (approx)", 10.0),
               "b": ("disease targets needing imaging (approx)", 200.0), "bounds": (0.03, 0.08),
               "step1": "ten targets imaged of two hundred needed - the molecular visibility gap",
               "confirm": "agents for many targets in clinical use",
               "refute": "each agent proves irreducibly bespoke"},
},
# ------------------------------------------------------------------ rank 12
{
 "key": "rehabilitation-robotics",
 "name": "Rehabilitation Robotics: Recovery Machines",
 "group": "Devices",
 "ladder_rank": 12, "ladder_tier": "compounded",
 "problem": "Robotic rehabilitation promises better stroke recovery - but the evidence is mixed. What makes rehab robots work?",
 "description": "Rehabilitation robots - exoskeletons, end-effector devices - deliver intensive therapy; but trials show mixed superiority to conventional therapy; the active ingredients (intensity, feedback, engagement) are debated.",
 "background": "Rehab robotics grew in the 2000s-2010s; large trials (VA ROBOTICS, 2010) showed equivalence more than superiority; engagement and intensity emerged as keys. As of 2026 robots assist but don't transform rehab.",
 "why_it_matters": "Effective rehab robots would scale stroke recovery: the workforce multiplier for rehabilitation.",
 "sig_pointer": "The Signature system's proposed approach identifies rehab robotics' active ingredients, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that rehab robots work through intensity and engagement: the active ingredients isolated - with robots optimized for them. "
  "Assumptions: (1) ingredients are identifiable; (2) they are optimizable; (3) optimization beats conventional. "
  "Reasoning path: an ingredients model explains mixed trials and predicts effective robots. "
  "Proposed mechanism: 'ingredient-optimized' rehab robotics - intensity and engagement maximized. "
  "What would confirm it: optimized robots beating conventional therapy. "
  "What would kill it: evidence that robots add nothing. "
  "What this does not claim: it does not claim robots transform rehab, offers no medical advice, and does not constitute a device recommendation."),
 "sig_lens": "The Signature lens reads rehab robots as unoptimized intensity, and asks what ingredients would make effective.",
 "how_it_works": "Researchers study rehab robotics through comparative trials, intensity research, and engagement studies.",
 "key_points": [
  "Rehab robots deliver intensive therapy.",
  "Trials show mixed superiority.",
  "Intensity and engagement are the candidate ingredients.",
  "Large trials showed equivalence.",
  "Robots assist but don't transform.",
 ],
 "requirements": [
  "Identified active ingredients.",
  "Optimized robots beating conventional therapy.",
  "Scaled deployment proven.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Lo AC et al. VA ROBOTICS trial. NEJM. 2010;362:1772-1783.",
  "Mehrholz J et al. Rehab robotics reviews. Various; 2018-2020.",
  "Lum PS et al. Intensity research. Various; 2002-2015.",
  "Veerbeek JM et al. Stroke rehab reviews. Various; 2017-2021.",
 ],
 "demo_data": {"a": ("rehab-robot trials showing superiority, percent (approx)", 30.0),
               "b": ("percent scale", 100.0), "bounds": (0.2, 0.42),
               "step1": "seven in ten trials show equivalence - the intensity without the ingredients",
               "confirm": "optimized robots beat conventional therapy",
               "refute": "robots prove to add nothing"},
},
# ------------------------------------------------------------------ rank 13
{
 "key": "heart-failure-devices",
 "name": "Heart-Failure Devices: The Mechanical Heart",
 "group": "Devices",
 "ladder_rank": 13, "ladder_tier": "compounded",
 "problem": "LVADs keep failing hearts alive - but as destination therapy they're imperfect. Can mechanical hearts replace transplantation?",
 "description": "Ventricular assist devices (HeartMate, HVAD) - bridge and destination therapy for heart failure; but complications (stroke, bleeding, infection) persist; the total artificial heart (Syncardia) is temporary. Destination mechanical hearts are the goal.",
 "background": "LVADs (2000s-2010s) improved dramatically; destination therapy was approved; the total artificial heart remains bridge-only. As of 2026 LVADs sustain but don't replace transplant.",
 "why_it_matters": "Mechanical hearts would end the donor shortage: the pump that replaces the organ.",
 "sig_pointer": "The Signature system's proposed approach builds the destination mechanical heart, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that mechanical hearts need complication-free design: the hemocompatible, infection-resistant systems - with destination outcomes. "
  "Assumptions: (1) complications are designable away; (2) destination is achievable; (3) outcomes match transplant. "
  "Reasoning path: a design model explains current limits and predicts mechanical replacement. "
  "Proposed mechanism: 'complication-free' mechanical hearts - destination devices. "
  "What would confirm it: destination mechanical hearts matching transplant outcomes. "
  "What would kill it: evidence that blood-device contact is inherently problematic. "
  "What this does not claim: it does not claim mechanical hearts replace transplant, offers no medical advice, and does not constitute a device recommendation."),
 "sig_lens": "The Signature lens reads LVADs as complicated bridges, and asks what design would make destination.",
 "how_it_works": "Researchers study heart-failure devices through LVAD trials, hemocompatibility research, and total-heart development.",
 "key_points": [
  "LVADs sustain failing hearts.",
  "Stroke, bleeding, and infection persist.",
  "Total artificial hearts are bridge-only.",
  "Destination therapy is approved but imperfect.",
  "Transplant remains the gold standard.",
 ],
 "requirements": [
  "Hemocompatible complication-free designs.",
  "Destination outcomes matching transplant.",
  "Total hearts as destination therapy.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Mehra MR et al. HeartMate trials. Various; 2017-2022.",
  "Rogers JG et al. LVAD reviews. Various; 2017-2021.",
  "Copeland JG et al. Total artificial heart. Various; 2004-2012.",
  "Goldstein DJ et al. Device complications. Various; 2015-2020.",
 ],
 "demo_data": {"a": ("heart-transplant waiting list, thousands (approx)", 3.5),
               "b": ("LVADs implanted yearly, thousands (approx)", 2.5), "bounds": (1.1, 1.8),
               "step1": "more waiting than implanted - the mechanical heart's unmet demand",
               "confirm": "destination mechanical hearts match transplant outcomes",
               "refute": "blood-device contact proves inherently problematic"},
},
# ------------------------------------------------------------------ rank 14
{
 "key": "neuroprosthetics",
 "name": "Neuroprosthetics: Restoring the Senses",
 "group": "Neuroengineering",
 "ladder_rank": 14, "ladder_tier": "compounded",
 "problem": "Cochlear implants restored hearing - can vision, touch, and other senses be neuroprosthetically restored?",
 "description": "Sensory neuroprosthetics - cochlear implants succeeded; retinal implants (Argus II) restored crude vision but the company folded; cortical visual prostheses are in trials. The encoding problem (what stimulation means) is the barrier.",
 "background": "Cochlear implants (1980s-90s) were the triumph; retinal prostheses (2010s) disappointed; cortical approaches (2020s) are early. As of 2026 hearing stands alone as restored.",
 "why_it_matters": "Sensory neuroprosthetics would restore the senses: the encoding that makes stimulation perception.",
 "sig_pointer": "The Signature system's proposed approach solves the neural encoding problem, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that sensory restoration needs neural coding: the stimulation patterns that the brain reads as perception - with plasticity cooperating. "
  "Assumptions: (1) codes are discoverable; (2) the brain adapts; (3) perception follows. "
  "Reasoning path: a coding model explains cochlear success and retinal failure and predicts restored senses. "
  "Proposed mechanism: 'code-cracked' neuroprosthetics - perceptually-meaningful stimulation. "
  "What would confirm it: neuroprosthetic vision or touch in clinical use. "
  "What would kill it: evidence that neural codes are unlearnable. "
  "What this does not claim: it does not claim restored senses exist, offers no medical advice, and does not constitute a device recommendation."),
 "sig_lens": "The Signature lens reads sensory prosthetics as encoding failures, and asks what codes would make perception.",
 "how_it_works": "Researchers study neuroprosthetics through cortical-prosthesis trials, encoding research, and plasticity studies.",
 "key_points": [
  "Cochlear implants restored hearing.",
  "Retinal implants restored only crude vision.",
  "The neural encoding problem is the barrier.",
  "Cortical prostheses are in early trials.",
  "Hearing stands alone as restored.",
 ],
 "requirements": [
  "Discovered neural codes.",
  "Perceptual restoration in trials.",
  "Clinical sensory neuroprosthetics.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Wilson BS et al. Cochlear implants. Various; 1991-2015.",
  "Humayun MS et al. Argus II. Various; 2012-2018.",
  "Beauchamp MS et al. Cortical visual prostheses. Various; 2020-2023.",
  "Flesher SN et al. Sensory feedback. Various; 2016-2021.",
 ],
 "demo_data": {"a": ("senses restored by neuroprosthetics (approx)", 1.0),
               "b": ("human senses (approx)", 5.0), "bounds": (0.12, 0.3),
               "step1": "one sense of five restored - the uncracked codes of perception",
               "confirm": "neuroprosthetic vision or touch in clinical use",
               "refute": "neural codes prove unlearnable"},
},
# ------------------------------------------------------------------ rank 15
{
 "key": "bioprinting",
 "name": "Bioprinting: Printing Living Tissue",
 "group": "Regenerative",
 "ladder_rank": 15, "ladder_tier": "compounded",
 "problem": "Bioprinters print cell-laden constructs - but printed tissues don't function like organs. What makes printing work biologically?",
 "description": "Bioprinting - layer-by-layer tissue fabrication - produces structured constructs from cell-laden bioinks; but cell viability during printing, vascularization of thick constructs, and biological maturation after printing all limit function. As a result printed tissues serve as drug-testing models and research tools rather than implantable replacements, and the path from printed construct to living organ remains one of the field's defining challenges.",
 "background": "Bioprinting (2000s-2010s, Mironov, Atala) advanced rapidly; commercial bioprinters spread; but functional implants remain distant. As of 2026 bioprinting makes models.",
 "why_it_matters": "Functional bioprinting would manufacture organs on demand: the printer as the transplant surgeon.",
 "sig_pointer": "The Signature system's proposed approach makes printed tissue functional, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that bioprinting needs maturation: the printed constructs matured biologically - with vascularization and function. "
  "Assumptions: (1) maturation is achievable; (2) printed vasculature works; (3) function follows. "
  "Reasoning path: a maturation model explains model-status and predicts functional printing. "
  "Proposed mechanism: 'maturation-driven' bioprinting - biologically-functional constructs. "
  "What would confirm it: implanted printed tissues with function. "
  "What would kill it: evidence that printing can't produce living function. "
  "What this does not claim: it does not claim functional printed organs exist, offers no medical advice, and does not constitute a research recommendation."),
 "sig_lens": "The Signature lens reads bioprinting as immature constructs, and asks what maturation would functionalize.",
 "how_it_works": "Researchers study bioprinting through bioink research, vascularization printing, and maturation bioreactors.",
 "key_points": [
  "Bioprinters print structured cell constructs.",
  "Cell viability and vascularization limit function.",
  "Printed tissues are models, not implants.",
  "Maturation is the missing step.",
  "Functional implants are distant.",
 ],
 "requirements": [
  "Matured printed constructs.",
  "Implanted printed tissues with function.",
  "On-demand organ printing.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Murphy SV, Atala A. Bioprinting reviews. Various; 2014-2020.",
  "Mironov V et al. Organ printing. Various; 2003-2009.",
  "Ozbolat IT et al. Bioprinting reviews. Various; 2016-2021.",
  "Gungor-Ozkerim PS et al. Bioinks. Various; 2018-2022.",
 ],
 "demo_data": {"a": ("printed tissues implanted with function (approx)", 1.0),
               "b": ("printed tissue constructs made (approx)", 100.0), "bounds": (0.004, 0.02),
               "step1": "one functional of a hundred printed - the maturation gap",
               "confirm": "implanted printed tissues with function",
               "refute": "printing proves unable to produce living function"},
},
# ------------------------------------------------------------------ rank 16
{
 "key": "gene-delivery",
 "name": "Gene-Delivery Engineering",
 "group": "Regenerative",
 "ladder_rank": 16, "ladder_tier": "compounded",
 "problem": "Gene therapies work - but delivery vectors are immunogenic, limited, and expensive. Can delivery be engineered better?",
 "description": "Gene-delivery engineering - AAV vectors, lipid nanoparticles - enabled gene therapy; but AAV immunogenicity, cargo limits, and manufacturing costs constrain it; engineered capsids and non-viral vectors are the frontier.",
 "background": "AAV gene therapy (2010s-2020s) succeeded clinically; LNPs delivered mRNA vaccines; capsid engineering (Gradinaru, Schaffer) improves targeting. As of 2026 delivery is the bottleneck.",
 "why_it_matters": "Better delivery would make gene therapy routine: the vector as the medicine's vehicle.",
 "sig_pointer": "The Signature system's proposed approach engineers superior gene delivery, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that gene delivery needs engineered vectors: the capsids and nanoparticles designed for targeting, evasion, and cargo - with manufacturing scaled. "
  "Assumptions: (1) vectors are engineerable; (2) they evade immunity; (3) manufacturing scales. "
  "Reasoning path: a vector model explains current limits and predicts routine gene therapy. "
  "Proposed mechanism: 'engineered' gene-delivery vectors - designed targeting and evasion. "
  "What would confirm it: engineered vectors in routine clinical use. "
  "What would kill it: evidence that delivery is inherently limited. "
  "What this does not claim: it does not claim superior vectors exist, offers no medical advice, and does not constitute a development recommendation."),
 "sig_lens": "The Signature lens reads gene therapy as delivery-limited, and asks what vectors would routine-ize.",
 "how_it_works": "Researchers study gene delivery through capsid engineering, LNP research, and non-viral vector development.",
 "key_points": [
  "AAV enabled clinical gene therapy.",
  "Immunogenicity and cargo limits constrain it.",
  "LNPs delivered mRNA vaccines.",
  "Engineered capsids improve targeting.",
  "Delivery is the bottleneck.",
 ],
 "requirements": [
  "Engineered targeting vectors.",
  "Immune-evading delivery proven.",
  "Scaled manufacturing.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Mendell JR et al. AAV gene therapy. Various; 2017-2021.",
  "Gradinaru V et al. Capsid engineering. Various; 2016-2022.",
  "Schaffer DV et al. Vector engineering. Various; 2008-2020.",
  "Hou X et al. LNP reviews. Various; 2021-2023.",
 ],
 "demo_data": {"a": ("gene-therapy doses deliverable per manufacturing run, thousands (approx)", 5.0),
               "b": ("patients needing gene therapy, thousands (approx)", 10000.0), "bounds": (0.0003, 0.0008),
               "step1": "thousands of doses against millions of patients - the delivery scale gap",
               "confirm": "engineered vectors in routine clinical use",
               "refute": "delivery proves inherently limited"},
},
# ------------------------------------------------------------------ rank 17
{
 "key": "wearable-diagnostics",
 "name": "Wearable Diagnostics: Medical-Grade Wearables",
 "group": "Devices",
 "ladder_rank": 17, "ladder_tier": "compounded",
 "problem": "Wearables track fitness - but medical-grade diagnosis from a watch remains mostly promise. What makes wearables clinical?",
 "description": "Wearable diagnostics - smartwatch ECG, PPG, SpO2 - detect atrial fibrillation and more; but most signals are wellness-grade; the validation, regulation, and clinical integration for true diagnostics are pending.",
 "background": "Apple Watch ECG (2018) was the milestone; AFib detection was validated; but broader diagnostics (glucose, blood pressure) remain elusive. As of 2026 wearables are wellness with clinical islands.",
 "why_it_matters": "Clinical wearables would make diagnosis continuous: the doctor on the wrist.",
 "sig_pointer": "The Signature system's proposed approach makes wearables clinical, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that wearables need clinical validation: the signals validated against gold standards - with regulatory clearance and clinical integration. "
  "Assumptions: (1) signals are validatable; (2) regulation follows; (3) clinicians adopt. "
  "Reasoning path: a validation model explains wellness-status and predicts clinical wearables. "
  "Proposed mechanism: 'clinically-validated' wearables - cleared diagnostics. "
  "What would confirm it: wearables diagnosing multiple conditions clinically. "
  "What would kill it: evidence that wearable signals are inherently wellness-grade. "
  "What this does not claim: it does not claim clinical wearables exist, offers no medical advice, and does not constitute a device recommendation."),
 "sig_lens": "The Signature lens reads wearables as unvalidated signals, and asks what proof would make clinical.",
 "how_it_works": "Researchers study wearable diagnostics through validation trials, sensor research, and regulatory pathways.",
 "key_points": [
  "Smartwatch ECG detects AFib.",
  "Most wearable signals are wellness-grade.",
  "Glucose and blood pressure remain elusive.",
  "Validation against gold standards is pending.",
  "Clinical integration is early.",
 ],
 "requirements": [
  "Validated multi-condition diagnostics.",
  "Regulatory clearance.",
  "Clinical adoption proven.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Perez MV et al. Apple Heart Study. NEJM. 2019;381:1909-1917.",
  "Turakhia MP et al. Wearable AFib. Various; 2019-2022.",
  "Lubitz SA et al. PPG validation. Various; 2022-2024.",
  "Bayoumy K et al. Wearable reviews. Various; 2021-2023.",
 ],
 "demo_data": {"a": ("conditions diagnosable by wearables (approx)", 3.0),
               "b": ("conditions needing diagnosis (approx)", 100.0), "bounds": (0.015, 0.05),
               "step1": "three conditions of a hundred - the clinical gap on the wrist",
               "confirm": "wearables diagnose multiple conditions clinically",
               "refute": "wearable signals prove inherently wellness-grade"},
},
# ------------------------------------------------------------------ rank 18
{
 "key": "brain-stimulation",
 "name": "Brain Stimulation: Precision Neuromodulation",
 "group": "Neuroengineering",
 "ladder_rank": 18, "ladder_tier": "compounded",
 "problem": "Deep-brain stimulation helps Parkinson's - but targeting is crude and mechanisms unclear. Can neuromodulation become precise?",
 "description": "Brain stimulation - DBS, TMS, focused ultrasound - treats neurological and psychiatric conditions; but DBS mechanisms are debated, targeting is millimeter-crude, and closed-loop adaptive stimulation is early.",
 "background": "DBS (1990s-2000s) transformed Parkinson's; adaptive DBS (2020s) senses and adjusts; focused ultrasound (2010s-2020s) offers noninvasive lesions. As of 2026 stimulation is effective but imprecise.",
 "why_it_matters": "Precise neuromodulation would treat brain disorders with surgical precision: the pacemaker for the mind.",
 "sig_pointer": "The Signature system's proposed approach makes neuromodulation precise, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that neuromodulation needs closed-loop precision: the sensing-stimulating systems that target circuits - with mechanisms understood. "
  "Assumptions: (1) circuits are targetable; (2) mechanisms are learnable; (3) closed-loop works. "
  "Reasoning path: a precision model explains crude effectiveness and predicts precise therapy. "
  "Proposed mechanism: 'closed-loop' neuromodulation - circuit-precise stimulation. "
  "What would confirm it: precise circuit-targeted therapies in trials. "
  "What would kill it: evidence that brain circuits resist precise targeting. "
  "What this does not claim: it does not claim precise neuromodulation exists, offers no medical advice, and does not constitute a device recommendation."),
 "sig_lens": "The Signature lens reads stimulation as effective-but-crude, and asks what closed loops would precise.",
 "how_it_works": "Researchers study brain stimulation through adaptive-DBS trials, circuit mapping, and ultrasound research.",
 "key_points": [
  "DBS transformed Parkinson's treatment.",
  "Mechanisms remain debated.",
  "Targeting is millimeter-crude.",
  "Adaptive DBS is early.",
  "Focused ultrasound is noninvasive.",
 ],
 "requirements": [
  "Circuit-precise targeting.",
  "Closed-loop systems proven.",
  "Mechanism-understood therapies.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Benabid AL et al. DBS history. Various; 1987-2009.",
  "Little S et al. Adaptive DBS. Various; 2013-2021.",
  "Elias WJ et al. Focused ultrasound. Various; 2016-2021.",
  "Lozano AM et al. Neuromodulation reviews. Various; 2019-2022.",
 ],
 "demo_data": {"a": ("DBS patients with optimized targeting, percent (approx)", 50.0),
               "b": ("percent scale", 100.0), "bounds": (0.38, 0.62),
               "step1": "half optimized, half not - the precision gap in brain stimulation",
               "confirm": "precise circuit-targeted therapies in trials",
               "refute": "brain circuits prove to resist precise targeting"},
},
# ------------------------------------------------------------------ rank 19
{
 "key": "tumor-imaging",
 "name": "Tumor-Margin Imaging: Seeing Cancer's Edge",
 "group": "Imaging",
 "ladder_rank": 19, "ladder_tier": "compounded",
 "problem": "Surgeons can't see tumor margins - positive margins mean reoperation. Can imaging reveal cancer's edge in real time?",
 "description": "Tumor-margin imaging - intraoperative fluorescence, Raman, mass-spec - aims to show surgeons the cancer boundary; but no modality is standard; positive-margin rates remain high in breast, brain, and other surgeries.",
 "background": "Fluorescence guidance (2010s, van Dam) showed promise; 5-ALA (glioma) is approved; but broad adoption is pending. As of 2026 surgeons still operate partially blind.",
 "why_it_matters": "Real-time margin imaging would make cancer surgery complete: the edge made visible.",
 "sig_pointer": "The Signature system's proposed approach makes tumor margins visible intraoperatively, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that margin imaging needs intraoperative proof: the modalities showing margins in real time - with reoperation rates falling. "
  "Assumptions: (1) modalities exist; (2) they are real-time; (3) surgeons adopt. "
  "Reasoning path: an adoption model explains the evidence-adoption gap and predicts standard margin imaging. "
  "Proposed mechanism: 'intraoperatively-proven' margin imaging - real-time cancer edges. "
  "What would confirm it: margin imaging standard with reduced reoperations. "
  "What would kill it: evidence that no modality works intraoperatively. "
  "What this does not claim: it does not claim margin imaging is standard, offers no medical advice, and does not constitute a device recommendation."),
 "sig_lens": "The Signature lens reads cancer surgery as partially blind, and asks what imaging would show the edge.",
 "how_it_works": "Researchers study margin imaging through fluorescence trials, Raman research, and outcome studies.",
 "key_points": [
  "Positive margins mean reoperation.",
  "No margin modality is standard.",
  "5-ALA is approved for glioma.",
  "Fluorescence guidance shows promise.",
  "Surgeons operate partially blind.",
 ],
 "requirements": [
  "Real-time intraoperative margin imaging.",
  "Reduced reoperation rates proven.",
  "Standard adoption in cancer surgery.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "van Dam GM et al. Fluorescence guidance. Various; 2011-2021.",
  "Stummer W et al. 5-ALA glioma. Various; 2006-2017.",
  "Zhang RR et al. Raman margin imaging. Various; 2017-2021.",
  "Nguyen QT et al. Margin reviews. Various; 2020-2023.",
 ],
 "demo_data": {"a": ("breast-conserving surgeries with positive margins, percent (approx)", 20.0),
               "b": ("percent scale", 100.0), "bounds": (0.12, 0.3),
               "step1": "one in five reoperated - the invisible edge's toll",
               "confirm": "margin imaging standard with reduced reoperations",
               "refute": "no modality proves to work intraoperatively"},
},
# ------------------------------------------------------------------ rank 20
{
 "key": "spinal-cord",
 "name": "Spinal-Cord Repair Engineering",
 "group": "Neuroengineering",
 "ladder_rank": 20, "ladder_tier": "compounded",
 "problem": "Spinal-cord injury paralyzes - can bioengineering bridge the cord and restore function?",
 "description": "Spinal-court repair - scaffolds, stem cells, epidural stimulation - aims to restore function after injury; epidural stimulation (Harkema, 2010s-2020s) restored some volitional movement; but regeneration remains limited and no therapy restores normal function.",
 "background": "Regeneration research (1980s-2000s) mapped the barriers; epidural stimulation trials (2010s-2020s) showed promise; combination therapies are emerging. As of 2026 restoration is partial.",
 "why_it_matters": "Spinal repair would restore movement after paralysis: the bridge across the broken cord.",
 "sig_pointer": "The Signature system's proposed approach bridges the injured cord, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that cord repair needs combination therapy: the scaffolds, cells, and stimulation combined - with function restored. "
  "Assumptions: (1) combinations work; (2) they are safe; (3) function restores. "
  "Reasoning path: a combination model explains single-therapy limits and predicts restored function. "
  "Proposed mechanism: 'combination' spinal repair - scaffold-cell-stimulation therapy. "
  "What would confirm it: restored volitional function in trials. "
  "What would kill it: evidence that the cord can't be bridged. "
  "What this does not claim: it does not claim cord repair works, offers no medical advice, and does not constitute a research recommendation."),
 "sig_lens": "The Signature lens reads cord injury as unbridged, and asks what combinations would restore.",
 "how_it_works": "Researchers study spinal repair through stimulation trials, scaffold research, and combination studies.",
 "key_points": [
  "Epidural stimulation restored some movement.",
  "Regeneration remains limited.",
  "No therapy restores normal function.",
  "Combination therapies are emerging.",
  "The barriers are mapped.",
 ],
 "requirements": [
  "Combination therapies in trials.",
  "Restored volitional function.",
  "Safe durable repair.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Harkema S et al. Epidural stimulation. Various; 2011-2022.",
  "Angeli CA et al. Stimulation trials. Various; 2014-2018.",
  "Courtine G et al. Spinal repair. Various; 2018-2023.",
  "Tuszynski MH et al. Regeneration reviews. Various; 2019-2022.",
 ],
 "demo_data": {"a": ("spinal-injury patients regaining volitional movement, percent (approx)", 15.0),
               "b": ("percent scale", 100.0), "bounds": (0.08, 0.25),
               "step1": "fifteen percent regain movement - the partial bridge",
               "confirm": "restored volitional function in trials",
               "refute": "the cord proves unbridgeable"},
},
# ------------------------------------------------------------------ rank 21
{
 "key": "microbiome-engineering",
 "name": "Microbiome Engineering",
 "group": "Regenerative",
 "ladder_rank": 21, "ladder_tier": "compounded",
 "problem": "The microbiome affects health - but can it be engineered precisely, or only perturbed bluntly?",
 "description": "Microbiome engineering - probiotics, FMT, engineered bacteria - aims to reshape gut communities; FMT works for C. difficile; but precision engineering (targeted strains, synthetic consortia) is early and the ecology is poorly understood.",
 "background": "FMT (2010s) proved the concept for C. diff; engineered probiotics (2010s-2020s) are in trials; the Human Microbiome Project mapped the terrain. As of 2026 engineering is blunt.",
 "why_it_matters": "Precise microbiome engineering would treat disease through ecology: the medicine of the inner ecosystem.",
 "sig_pointer": "The Signature system's proposed approach engineers microbiomes precisely, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that microbiome engineering needs ecological precision: the consortia designed for function - with engraftment proven. "
  "Assumptions: (1) ecology is engineerable; (2) consortia engraft; (3) function follows. "
  "Reasoning path: an ecology model explains blunt success and predicts precision. "
  "Proposed mechanism: 'ecologically-precise' microbiome engineering - designed consortia. "
  "What would confirm it: engineered consortia treating disease in trials. "
  "What would kill it: evidence that microbiomes resist engineering. "
  "What this does not claim: it does not claim precise engineering works, offers no medical advice, and does not constitute a research recommendation."),
 "sig_lens": "The Signature lens reads microbiome therapy as blunt perturbation, and asks what ecology would make precise.",
 "how_it_works": "Researchers study microbiome engineering through consortium trials, engraftment research, and ecological modeling.",
 "key_points": [
  "FMT works for C. difficile.",
  "Precision engineering is early.",
  "The gut ecology is poorly understood.",
  "Engineered probiotics are in trials.",
  "Current approaches are blunt.",
 ],
 "requirements": [
  "Designed consortia proven.",
  "Engraftment demonstrated.",
  "Disease treatment in trials.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "van Nood E et al. FMT for C. diff. NEJM. 2013;368:407-415.",
  "Human Microbiome Project. Various; 2012-2019.",
  "Isabella VM et al. Engineered probiotics. Various; 2018-2022.",
  "Mimee M et al. Microbiome engineering. Various; 2016-2021.",
 ],
 "demo_data": {"a": ("conditions treatable by microbiome engineering (approx)", 3.0),
               "b": ("conditions linked to microbiome (approx)", 50.0), "bounds": (0.03, 0.1),
               "step1": "three treated of fifty linked - the unengineered inner ecosystem",
               "confirm": "engineered consortia treat disease in trials",
               "refute": "microbiomes prove to resist engineering"},
},
# ------------------------------------------------------------------ rank 22
{
 "key": "blood-substitutes",
 "name": "Blood Substitutes: The Artificial Blood",
 "group": "Materials",
 "ladder_rank": 22, "ladder_tier": "compounded",
 "problem": "Blood transfusions depend on donors - can artificial oxygen carriers replace them?",
 "description": "Blood substitutes - hemoglobin-based oxygen carriers (HBOCs), perfluorocarbons - promise donor-free transfusion; but HBOC trials showed toxicity (vasoconstriction); no product is approved. The field persists with new approaches.",
 "background": "HBOC development (1980s-2000s) failed on safety; perfluorocarbons (Fluosol, 1989) were withdrawn; new HBOCs and approaches continue. As of 2026 no blood substitute is approved.",
 "why_it_matters": "Artificial blood would end transfusion shortages: the donor-free oxygen carrier.",
 "sig_pointer": "The Signature system's proposed approach builds safe oxygen carriers, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that blood substitutes need safe carriers: the oxygen carriers without vasoconstriction - proven in trials. "
  "Assumptions: (1) safe carriers are designable; (2) they oxygenate; (3) trials prove. "
  "Reasoning path: a safety model explains past failures and predicts approved substitutes. "
  "Proposed mechanism: 'safety-designed' oxygen carriers - non-toxic HBOCs. "
  "What would confirm it: approved blood substitutes in clinical use. "
  "What would kill it: evidence that hemoglobin carriers are inherently toxic. "
  "What this does not claim: it does not claim blood substitutes exist, offers no medical advice, and does not constitute a development recommendation."),
 "sig_lens": "The Signature lens reads blood substitutes as toxicity-limited, and asks what design would make safe.",
 "how_it_works": "Researchers study blood substitutes through HBOC redesign, perfluorocarbon research, and safety trials.",
 "key_points": [
  "HBOC trials showed vasoconstriction toxicity.",
  "No blood substitute is approved.",
  "Perfluorocarbons were withdrawn.",
  "New approaches continue.",
  "Donor dependence persists.",
 ],
 "requirements": [
  "Non-toxic oxygen carriers.",
  "Approved blood substitutes.",
  "Clinical transfusion replacement.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Natanson C et al. HBOC meta-analysis. JAMA. 2008;299:2304-2312.",
  "Fluosol-DA. Various; 1989-1994.",
  "Alayash AI et al. HBOC reviews. Various; 2014-2019.",
  "Modery-Pawlowski CL et al. Carrier reviews. Various; 2013-2020.",
 ],
 "demo_data": {"a": ("approved blood substitutes", 0.5),
               "b": ("decades of development (approx)", 4.0), "bounds": (0.08, 0.2),
               "step1": "zero approvals in four decades - the carrier that never cleared safety",
               "confirm": "approved blood substitutes in clinical use",
               "refute": "hemoglobin carriers prove inherently toxic"},
},
# ------------------------------------------------------------------ rank 23
{
 "key": "cryopreservation",
 "name": "Organ Cryopreservation",
 "group": "Regenerative",
 "ladder_rank": 23, "ladder_tier": "compounded",
 "problem": "Organs can't be banked - cryopreservation fails at organ scale. Can whole organs be frozen and revived?",
 "description": "Organ cryopreservation - banking transplantable organs - works for cells and small tissues; but ice formation and cryoprotectant toxicity defeat whole organs. Vitrification and nanowarming (Bischof) are the frontier.",
 "background": "Cryobiology (1950s-60s) enabled cell banking; organ vitrification is recent; nanowarming (2017) revived larger tissues. As of 2026 no organ is banked.",
 "why_it_matters": "Organ banking would end transplant logistics: the freezer as the waiting list's end.",
 "sig_pointer": "The Signature system's proposed approach banks whole organs, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that organ banking needs uniform vitrification: the ice-free preservation with nanowarming revival - proven in transplants. "
  "Assumptions: (1) vitrification scales; (2) nanowarming revives uniformly; (3) organs transplant. "
  "Reasoning path: a scaling model explains cell-success and predicts organ banking. "
  "Proposed mechanism: 'uniformly-vitrified' organs - banked transplantables. "
  "What would confirm it: banked organs transplanted successfully. "
  "What would kill it: evidence that organs can't be vitrified. "
  "What this does not claim: it does not claim organ banking exists, offers no medical advice, and does not constitute a research recommendation."),
 "sig_lens": "The Signature lens reads cryopreservation as scale-limited, and asks what vitrification would bank.",
 "how_it_works": "Researchers study cryopreservation through vitrification research, nanowarming studies, and organ trials.",
 "key_points": [
  "Cells and small tissues are bankable.",
  "Ice formation defeats whole organs.",
  "Nanowarming revived larger tissues.",
  "No organ is banked.",
  "Transplant logistics remain urgent.",
 ],
 "requirements": [
  "Uniform organ vitrification.",
  "Nanowarming revival proven.",
  "Banked organs transplanted.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Mazur P et al. Cryobiology foundations. Various; 1960s-1984.",
  "Manuchehrabadi N et al. Nanowarming. Various; 2017-2020.",
  "Fahy GM et al. Vitrification. Various; 1984-2010.",
  "Bischof JC et al. Organ preservation. Various; 2015-2022.",
 ],
 "demo_data": {"a": ("organs banked for transplant (approx)", 0.5),
               "b": ("organs transplanted yearly, thousands (approx)", 150.0), "bounds": (0.001, 0.008),
               "step1": "zero banked of a hundred fifty thousand transplanted - the unbankable organ",
               "confirm": "banked organs transplanted successfully",
               "refute": "organs prove unable to be vitrified"},
},
# ------------------------------------------------------------------ rank 24
{
 "key": "brain-decoding",
 "name": "Decoding the Brain: The Neural Code",
 "group": "Neuroengineering",
 "ladder_rank": 24, "ladder_tier": "advanced",
 "problem": "BCIs decode movement - but the brain's full neural code is unknown. Can neuroscience read the mind's language?",
 "description": "Neural decoding - inferring intention, perception, even speech from brain activity - works for trained tasks; but the general neural code (how populations represent the world) is unknown; decoding generalizes poorly across contexts.",
 "background": "Population decoding (2000s-2010s, Georgopoulos, Shenoy) enabled BCIs; speech decoding (2020s) advanced; but the code itself remains mysterious. As of 2026 decoding is task-specific.",
 "why_it_matters": "The neural code would unlock BCIs, brain understanding, and AI: the language of thought.",
 "sig_pointer": "The Signature system's proposed approach cracks the neural code, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that the neural code is crackable: the population representations mapped generally - with decoding across contexts. "
  "Assumptions: (1) a general code exists; (2) it is mappable; (3) it generalizes. "
  "Reasoning path: a code model explains task-specific success and predicts general decoding. "
  "Proposed mechanism: 'generally-mapped' neural codes - context-independent decoding. "
  "What would confirm it: decoders generalizing across tasks and contexts. "
  "What would kill it: evidence that no general code exists. "
  "What this does not claim: it does not claim the code is known, offers no medical advice, and does not constitute a research recommendation."),
 "sig_lens": "The Signature lens reads decoding as task-bound, and asks what general code would read.",
 "how_it_works": "Researchers study neural codes through population recordings, representation research, and generalization studies.",
 "key_points": [
  "Decoding works for trained tasks.",
  "The general neural code is unknown.",
  "Decoding generalizes poorly.",
  "Speech decoding advanced recently.",
  "The code itself is mysterious.",
 ],
 "requirements": [
  "Generally-mapped neural codes.",
  "Cross-context decoding.",
  "Code-based BCI advances.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Georgopoulos AP et al. Population vectors. Various; 1982-1988.",
  "Shenoy KV et al. Decoding reviews. Various; 2013-2021.",
  "Willett FR et al. Speech decoding. Various; 2021-2023.",
  "Kriegeskorte N et al. Representation research. Various; 2008-2018.",
 ],
 "demo_data": {"a": ("decoding contexts that generalize (approx)", 5.0),
               "b": ("decoding contexts tested (approx)", 100.0), "bounds": (0.03, 0.08),
               "step1": "five generalize of a hundred tested - the ungeneralized code",
               "confirm": "decoders generalize across tasks and contexts",
               "refute": "no general code proves to exist"},
},
# ------------------------------------------------------------------ rank 25
{
 "key": "synthetic-biology-devices",
 "name": "Synthetic-Biology Devices",
 "group": "Regenerative",
 "ladder_rank": 25, "ladder_tier": "advanced",
 "problem": "Engineered cells can sense and act - but living devices are unreliable. Can synthetic biology build dependable medical devices?",
 "description": "Synthetic-biology devices - engineered cells as sensors, drug factories, logic circuits - promise living medicine; but genetic circuits are noisy, evolution degrades them, and clinical translation is early.",
 "background": "Synthetic biology (2000s, Endy, Collins) built genetic circuits; therapeutic cells (2010s-2020s) are in trials; but reliability is the barrier. As of 2026 living devices are developmental.",
 "why_it_matters": "Dependable living devices would make medicine adaptive: the cell as the device.",
 "sig_pointer": "The Signature system's proposed approach makes living devices dependable, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that living devices need reliability engineering: the circuits stabilized against noise and evolution - with clinical dependability. "
  "Assumptions: (1) reliability is engineerable; (2) circuits stabilize; (3) translation follows. "
  "Reasoning path: a reliability model explains developmental status and predicts living devices. "
  "Proposed mechanism: 'reliability-engineered' synthetic devices - stable therapeutic cells. "
  "What would confirm it: dependable living devices in clinical use. "
  "What would kill it: evidence that biology resists reliability. "
  "What this does not claim: it does not claim living devices work clinically, offers no medical advice, and does not constitute a research recommendation."),
 "sig_lens": "The Signature lens reads synthetic biology as unreliable circuits, and asks what engineering would stabilize.",
 "how_it_works": "Researchers study synthetic devices through circuit-stabilization research, therapeutic-cell trials, and evolution studies.",
 "key_points": [
  "Engineered cells can sense and act.",
  "Genetic circuits are noisy.",
  "Evolution degrades engineered function.",
  "Clinical translation is early.",
  "Reliability is the barrier.",
 ],
 "requirements": [
  "Stabilized genetic circuits.",
  "Dependable living devices in trials.",
  "Clinical living-device medicine.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Endy D et al. Synthetic biology. Various; 2005-2015.",
  "Collins JJ et al. Therapeutic circuits. Various; 2016-2022.",
  "Danino T et al. Engineered bacteria. Various; 2015-2021.",
  "Elowitz MB et al. Circuit noise. Various; 2002-2015.",
 ],
 "demo_data": {"a": ("synthetic devices in clinical use (approx)", 2.0),
               "b": ("synthetic devices published (approx)", 100.0), "bounds": (0.01, 0.035),
               "step1": "two clinical of a hundred published - the unreliable living device",
               "confirm": "dependable living devices in clinical use",
               "refute": "biology proves to resist reliability"},
},
# ------------------------------------------------------------------ rank 26
{
 "key": "personalized-implants",
 "name": "Personalized Implants: The Patient-Specific Device",
 "group": "Devices",
 "ladder_rank": 26, "ladder_tier": "advanced",
 "problem": "Implants are one-size-fits-most - can patient-specific devices be manufactured at scale?",
 "description": "Personalized implants - 3D-printed, patient-matched devices - promise better fit and function; but manufacturing scale, regulatory paths, and cost challenge adoption; most implants remain standardized.",
 "background": "3D-printed implants (2010s-2020s) proved feasibility; cranial and orthopedic custom implants are used; but scale and cost limit spread. As of 2026 personalization is niche.",
 "why_it_matters": "Scaled personalization would make every implant fit: the end of one-size-fits-most medicine.",
 "sig_pointer": "The Signature system's proposed approach scales personalized implants, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that personalization scales: the design-to-implant pipelines automated - with regulatory clearance and cost control. "
  "Assumptions: (1) pipelines automate; (2) regulation adapts; (3) costs fall. "
  "Reasoning path: a pipeline model explains niche status and predicts scaled personalization. "
  "Proposed mechanism: 'pipeline-automated' personalized implants - scaled custom devices. "
  "What would confirm it: personalized implants as standard care. "
  "What would kill it: evidence that personalization can't scale economically. "
  "What this does not claim: it does not claim scaled personalization exists, offers no medical advice, and does not constitute a device recommendation."),
 "sig_lens": "The Signature lens reads implants as standardized compromise, and asks what pipelines would personalize.",
 "how_it_works": "Researchers study personalized implants through 3D-printing scale-up, regulatory science, and cost analyses.",
 "key_points": [
  "Most implants are standardized.",
  "3D printing enables customization.",
  "Custom implants are used in niche cases.",
  "Scale and cost limit spread.",
  "Regulatory paths are adapting.",
 ],
 "requirements": [
  "Automated design-to-implant pipelines.",
  "Personalized implants as standard care.",
  "Cost-competitive customization.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Morrison RJ et al. 3D-printed implants. Various; 2015-2020.",
  "FDA. 3D-printed device guidance. Various; 2016-2023.",
  "Javaid M et al. Personalized implant reviews. Various; 2020-2023.",
  "Mitsouras D et al. Medical 3D printing. Various; 2015-2020.",
 ],
 "demo_data": {"a": ("implants that are patient-specific, percent (approx)", 5.0),
               "b": ("percent scale", 100.0), "bounds": (0.03, 0.08),
               "step1": "five percent personalized - the standardized majority",
               "confirm": "personalized implants as standard care",
               "refute": "personalization proves unable to scale economically"},
},
# ------------------------------------------------------------------ rank 27
{
 "key": "point-of-care",
 "name": "Point-of-Care Diagnostics for Everything",
 "group": "Devices",
 "ladder_rank": 27, "ladder_tier": "advanced",
 "problem": "Lab tests take days - can point-of-care diagnostics match the central lab for every test?",
 "description": "Point-of-care diagnostics - rapid tests performed at the bedside or in the clinic - succeeded for glucose, pregnancy, and COVID; but most assays still need the central laboratory. Sensitivity gaps, limited multiplexing, and per-test cost challenge expansion, so while rapid tests proved the concept, the central lab remains dominant and the vision of lab-quality diagnosis at the point of care is still largely unrealized.",
 "background": "Lateral-flow tests proved the concept; COVID (2020-2022) scaled rapid testing; microfluidic platforms promise lab-quality POC. As of 2026 the lab remains dominant.",
 "why_it_matters": "Lab-quality POC would make diagnosis instant: the laboratory in the pocket.",
 "sig_pointer": "The Signature system's proposed approach brings the lab to the bedside, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that POC needs lab-equivalent platforms: the microfluidic systems matching central-lab sensitivity - with multiplexing and cost. "
  "Assumptions: (1) equivalence is achievable; (2) multiplexing works; (3) costs fall. "
  "Reasoning path: an equivalence model explains lab dominance and predicts POC expansion. "
  "Proposed mechanism: 'lab-equivalent' point-of-care - matched diagnostics. "
  "What would confirm it: POC matching labs across test menus. "
  "What would kill it: evidence that POC can't match lab sensitivity. "
  "What this does not claim: it does not claim lab-equivalent POC exists, offers no medical advice, and does not constitute a device recommendation."),
 "sig_lens": "The Signature lens reads diagnostics as lab-bound, and asks what platforms would liberate.",
 "how_it_works": "Researchers study POC through microfluidic platforms, sensitivity research, and multiplexing development.",
 "key_points": [
  "Rapid tests succeeded for few assays.",
  "Most tests need the central lab.",
  "Sensitivity and multiplexing are barriers.",
  "COVID scaled rapid testing.",
  "The lab remains dominant.",
 ],
 "requirements": [
  "Lab-equivalent POC platforms.",
  "Multiplexed rapid assays.",
  "POC matching labs across menus.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Luppa PB et al. POC reviews. Various; 2011-2016.",
  "St John A et al. POC evolution. Various; 2014-2020.",
  "COVID rapid-test literature. Various; 2020-2022.",
  "Sackmann EK et al. Microfluidic POC. Various; 2014-2019.",
 ],
 "demo_data": {"a": ("tests available at point of care, percent (approx)", 15.0),
               "b": ("percent scale", 100.0), "bounds": (0.1, 0.22),
               "step1": "fifteen percent at the bedside - the lab's enduring majority",
               "confirm": "POC matches labs across test menus",
               "refute": "POC proves unable to match lab sensitivity"},
},
# ------------------------------------------------------------------ rank 28
{
 "key": "digital-twins",
 "name": "Digital Twins of Patients",
 "group": "Models",
 "ladder_rank": 28, "ladder_tier": "advanced",
 "problem": "Digital twins model machines - can a patient be twinned well enough to guide treatment?",
 "description": "Patient digital twins - computational replicas for treatment planning - are conceptual; organ-level models (heart, liver) exist; but whole-patient twins need data integration, validation, and the modeling of individuality.",
 "background": "Engineering twins (2010s) proved the concept; cardiac models (2010s-2020s) personalize; but patient twins are aspirational. As of 2026 twins are organ-scale.",
 "why_it_matters": "Patient twins would make treatment predictive: trying the therapy on the twin first.",
 "sig_pointer": "The Signature system's proposed approach twins patients, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that patient twins need integrated modeling: the data-fused replicas validated against outcomes - with treatment guidance. "
  "Assumptions: (1) integration is feasible; (2) twins validate; (3) they guide treatment. "
  "Reasoning path: an integration model explains organ-scale status and predicts patient twins. "
  "Proposed mechanism: 'integrated' patient digital twins - validated replicas. "
  "What would confirm it: twins guiding treatment in trials. "
  "What would kill it: evidence that patients are untwinnable. "
  "What this does not claim: it does not claim patient twins exist, offers no medical advice, and does not constitute a modeling recommendation."),
 "sig_lens": "The Signature lens reads twins as organ-scale, and asks what integration would make patient.",
 "how_it_works": "Researchers study digital twins through cardiac modeling, data-integration research, and validation studies.",
 "key_points": [
  "Engineering twins proved the concept.",
  "Cardiac models personalize treatment.",
  "Patient twins are aspirational.",
  "Data integration is the barrier.",
  "Validation is pending.",
 ],
 "requirements": [
  "Integrated patient replicas.",
  "Outcome-validated twins.",
  "Treatment guidance in trials.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Grieves M et al. Digital twin concept. Various; 2014-2017.",
  "Trayanova NA et al. Cardiac twins. Various; 2016-2021.",
  "Corral-Acero J et al. Patient modeling. Various; 2020-2023.",
  "Viceconti M et al. In-silico trials. Various; 2021-2023.",
 ],
 "demo_data": {"a": ("patients with validated digital twins (approx)", 100.0),
               "b": ("patients treated yearly (approx)", 100000000.0), "bounds": (0.0000005, 0.000002),
               "step1": "a hundred twinned of a hundred million treated - the unreplicated patient",
               "confirm": "twins guide treatment in trials",
               "refute": "patients prove untwinnable"},
},
# ------------------------------------------------------------------ rank 29
{
 "key": "aging-engineering",
 "name": "Engineering Against Aging",
 "group": "Regenerative",
 "ladder_rank": 29, "ladder_tier": "advanced",
 "problem": "Aging is the biggest disease risk - can bioengineering intervene in aging itself?",
 "description": "Aging engineering - senolytics, partial reprogramming, engineered longevity - targets the biology of aging itself rather than its diseases; but human evidence is early and the field debates whether aging is treatable or inevitable. Mouse successes have not yet translated, and whether bioengineering can intervene in the fundamental process of aging remains the field's deepest open question.",
 "background": "Senolytics (2010s, Kirkland) cleared senescent cells; partial reprogramming (Ocampo, 2016) rejuvenated mice; human trials are early. As of 2026 aging intervention is preclinical-to-early-clinical.",
 "why_it_matters": "Aging intervention would prevent disease at its source: the engineering of longevity.",
 "sig_pointer": "The Signature system's proposed approach engineers against aging, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that aging is engineerable: the interventions (senolytics, reprogramming) proven safe and effective in humans. "
  "Assumptions: (1) aging mechanisms are targetable; (2) interventions are safe; (3) they extend healthspan. "
  "Reasoning path: an intervention model explains preclinical promise and predicts human longevity engineering. "
  "Proposed mechanism: 'intervention-proven' aging engineering - safe effective therapies. "
  "What would confirm it: aging interventions extending human healthspan. "
  "What would kill it: evidence that aging is untreatable. "
  "What this does not claim: it does not claim aging is treatable, offers no medical advice, and does not constitute a research recommendation."),
 "sig_lens": "The Signature lens reads aging as unengineered biology, and asks what interventions would make treatable.",
 "how_it_works": "Researchers study aging engineering through senolytic trials, reprogramming research, and longevity studies.",
 "key_points": [
  "Aging is the biggest disease risk factor.",
  "Senolytics cleared senescent cells in mice.",
  "Partial reprogramming rejuvenated mice.",
  "Human evidence is early.",
  "Treatability is debated.",
 ],
 "requirements": [
  "Safe human aging interventions.",
  "Extended healthspan proven.",
  "Aging as a treatable condition.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Kirkland JL et al. Senolytics. Various; 2015-2021.",
  "Ocampo A et al. Partial reprogramming. Cell. 2016;167:1719-1733.",
  "López-Otín C et al. Hallmarks of aging. Various; 2013-2023.",
  "Campisi J et al. Aging reviews. Various; 2019-2022.",
 ],
 "demo_data": {"a": ("aging interventions proven in humans (approx)", 1.0),
               "b": ("aging interventions in mice (approx)", 50.0), "bounds": (0.01, 0.035),
               "step1": "one human-proven of fifty mouse-proven - the translational gap in longevity",
               "confirm": "aging interventions extend human healthspan",
               "refute": "aging proves untreatable"},
},
# ------------------------------------------------------------------ rank 30
{
 "key": "xenotransplantation",
 "name": "Xenotransplantation: Animal Organs for Humans",
 "group": "Regenerative",
 "ladder_rank": 30, "ladder_tier": "advanced",
 "problem": "Genetically engineered pig organs are transplanted experimentally - can xenotransplantation become routine?",
 "description": "Xenotransplantation - pig organs for humans - advanced with gene-edited pigs (eGenesis, Revivicor); pig-heart transplants (2022-2023) survived months; but rejection, xenozoonosis, and ethics challenge routine use.",
 "background": "Xenotransplantation research (1990s-2000s) stalled on rejection; CRISPR-edited pigs (2010s-2020s) revived it; 2022 pig-heart transplants were milestones. As of 2026 it is experimental.",
 "why_it_matters": "Routine xenotransplantation would end the organ shortage: the unlimited organ supply.",
 "sig_pointer": "The Signature system's proposed approach makes xenotransplantation routine, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that xenotransplantation needs routine proof: the edited organs with durable survival - with safety and ethics addressed. "
  "Assumptions: (1) editing suffices; (2) survival is durable; (3) society accepts. "
  "Reasoning path: a proof model explains experimental status and predicts routine xeno-organs. "
  "Proposed mechanism: 'routinely-proven' xenotransplantation - durable edited organs. "
  "What would confirm it: routine xenotransplants with long survival. "
  "What would kill it: evidence that xeno-organs can't last. "
  "What this does not claim: it does not claim routine xenotransplantation exists, offers no medical advice, and does not constitute a research recommendation."),
 "sig_lens": "The Signature lens reads xeno-organs as experimental, and asks what proof would make routine.",
 "how_it_works": "Researchers study xenotransplantation through gene-edited pig trials, rejection research, and safety studies.",
 "key_points": [
  "Pig-heart transplants survived months.",
  "Gene-edited pigs reduced rejection.",
  "Xenozoonosis risk is monitored.",
  "Ethics are debated.",
  "Routine use is pending.",
 ],
 "requirements": [
  "Durable long-term xeno-organ survival.",
  "Safety proven at scale.",
  "Routine clinical xenotransplantation.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Griffith BP et al. Pig-heart transplant. Various; 2022-2023.",
  "eGenesis / Revivicor programs. Various; 2015 onward.",
  "Cooper DKC et al. Xeno reviews. Various; 2018-2022.",
  "Fishman JA et al. Xenozoonosis. Various; 2020-2023.",
 ],
 "demo_data": {"a": ("xenotransplant recipients surviving a year (approx)", 2.0),
               "b": ("xenotransplant recipients (approx)", 10.0), "bounds": (0.1, 0.35),
               "step1": "two of ten survive a year - the experimental organ's early record",
               "confirm": "routine xenotransplants with long survival",
               "refute": "xeno-organs prove unable to last"},
},
# ------------------------------------------------------------------ rank 31
{
 "key": "consciousness-monitoring",
 "name": "Monitoring Consciousness",
 "group": "Neuroengineering",
 "ladder_rank": 31, "ladder_tier": "advanced",
 "problem": "Anesthesia and coma hide consciousness - can brain monitoring reliably detect awareness?",
 "description": "Consciousness monitoring - detecting awareness under anesthesia or in disorders of consciousness - uses EEG and fMRI; but the measures are debated; awareness under anesthesia still occurs; the neural correlates are incompletely mapped.",
 "background": "BIS monitors (1990s-2000s) were imperfect; fMRI communication with vegetative patients (Owen, 2006) was a milestone; perturbational complexity (Massimini) is the leading measure. As of 2026 monitoring is imperfect.",
 "why_it_matters": "Reliable consciousness monitoring would prevent anesthesia awareness and find the locked-in: the awareness detector.",
 "sig_pointer": "The Signature system's proposed approach monitors consciousness reliably, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that consciousness is monitorable: the measures validated against awareness - with clinical reliability. "
  "Assumptions: (1) correlates exist; (2) they are measurable; (3) they are reliable. "
  "Reasoning path: a correlates model explains imperfect monitoring and predicts reliable detection. "
  "Proposed mechanism: 'reliably-measured' consciousness - validated awareness detection. "
  "What would confirm it: reliable awareness detection in clinical use. "
  "What would kill it: evidence that consciousness resists measurement. "
  "What this does not claim: it does not claim reliable monitoring exists, offers no medical advice, and does not constitute a device recommendation."),
 "sig_lens": "The Signature lens reads awareness as undetected, and asks what measures would make reliable.",
 "how_it_works": "Researchers study consciousness monitoring through PCI research, anesthesia-awareness studies, and DOC assessments.",
 "key_points": [
  "Awareness under anesthesia still occurs.",
  "BIS monitors are imperfect.",
  "fMRI found awareness in vegetative patients.",
  "Perturbational complexity is the leading measure.",
  "Reliable monitoring is pending.",
 ],
 "requirements": [
  "Validated awareness measures.",
  "Reliable clinical detection.",
  "Anesthesia awareness eliminated.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Owen AM et al. Vegetative-state awareness. Science. 2006;313:1402.",
  "Massimini M et al. Perturbational complexity. Various; 2005-2016.",
  "Sanders RD et al. Anesthesia awareness. Various; 2017-2021.",
  "Koch C et al. Consciousness reviews. Various; 2016-2022.",
 ],
 "demo_data": {"a": ("anesthesia-awareness cases per 10,000 (approx)", 1.0),
               "b": ("cases scale (per 10,000)", 10000.0), "bounds": (0.00005, 0.0002),
               "step1": "one in ten thousand wakes aware - the undetected consciousness",
               "confirm": "reliable awareness detection in clinical use",
               "refute": "consciousness proves to resist measurement"},
},
# ------------------------------------------------------------------ rank 32
{
 "key": "immune-engineering",
 "name": "Engineering Immunity: The Programmable Immune System",
 "group": "Regenerative",
 "ladder_rank": 32, "ladder_tier": "advanced",
 "problem": "CAR-T reprograms immunity against cancer - can the immune system be engineered programmably for any disease?",
 "description": "Immune engineering - CAR-T, engineered TCRs, tolerogenic therapies - reprograms immunity; CAR-T succeeded for blood cancers; but solid tumors resist; autoimmunity engineering is early; the programmable immune system is aspirational.",
 "background": "CAR-T (2010s, June) was the breakthrough; solid-tumor CAR-T struggles; engineered Tregs (2020s) target autoimmunity. As of 2026 programming is cancer-limited.",
 "why_it_matters": "Programmable immunity would treat cancer, autoimmunity, and infection: the immune system as software.",
 "sig_pointer": "The Signature system's proposed approach programs immunity generally, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that immunity is programmable: the engineered cells for solid tumors, autoimmunity, and beyond - with safety. "
  "Assumptions: (1) programming generalizes; (2) solid tumors yield; (3) it is safe. "
  "Reasoning path: a programming model explains blood-cancer success and predicts general immunity engineering. "
  "Proposed mechanism: 'generally-programmed' immunity - engineered for any disease. "
  "What would confirm it: engineered immunity treating solid tumors and autoimmunity. "
  "What would kill it: evidence that immunity resists programming. "
  "What this does not claim: it does not claim programmable immunity exists, offers no medical advice, and does not constitute a research recommendation."),
 "sig_lens": "The Signature lens reads immunity as narrowly programmed, and asks what engineering would generalize.",
 "how_it_works": "Researchers study immune engineering through solid-tumor CAR-T trials, Treg engineering, and safety research.",
 "key_points": [
  "CAR-T succeeded for blood cancers.",
  "Solid tumors resist engineered immunity.",
  "Engineered Tregs target autoimmunity.",
  "Programming is cancer-limited.",
  "The programmable system is aspirational.",
 ],
 "requirements": [
  "Solid-tumor engineered immunity.",
  "Autoimmunity engineering proven.",
  "Safe general immune programming.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Maude SL et al. CAR-T trials. NEJM. 2018;378:439-448.",
  "June CH et al. CAR-T reviews. Various; 2018-2022.",
  "Rafiq S et al. Solid-tumor CAR-T. Various; 2020-2023.",
  "Bluestone JA et al. Engineered Tregs. Various; 2015-2022.",
 ],
 "demo_data": {"a": ("diseases treatable by engineered immunity (approx)", 5.0),
               "b": ("diseases involving immunity (approx)", 200.0), "bounds": (0.015, 0.04),
               "step1": "five programmed of two hundred immune - the unprogrammed immune system",
               "confirm": "engineered immunity treats solid tumors and autoimmunity",
               "refute": "immunity proves to resist programming"},
},
# ------------------------------------------------------------------ rank 33
{
 "key": "whole-body-imaging",
 "name": "Whole-Body Molecular Imaging",
 "group": "Imaging",
 "ladder_rank": 33, "ladder_tier": "advanced",
 "problem": "Total-body PET scanners image the whole patient - but can whole-body molecular imaging transform medicine?",
 "description": "Whole-body molecular imaging - total-body PET scanners (EXPLORER, 2019) that image the entire patient at once - captures systemic disease in a single scan; but the scanners are rare and expensive, the data volumes are enormous, and the clinical transformation is still pending. Whether seeing the whole body's molecular state at once will change how medicine diagnoses and treats disease is the open question.",
 "background": "EXPLORER (2019) was the first total-body PET; systemic imaging revealed new biology; but adoption is slow. As of 2026 whole-body PET is research.",
 "why_it_matters": "Whole-body molecular imaging would make disease systemic: the body's molecular census.",
 "sig_pointer": "The Signature system's proposed approach makes whole-body imaging clinical, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that whole-body imaging needs clinical proof: the systemic diagnoses that change care - with scanners deployed. "
  "Assumptions: (1) systemic imaging changes care; (2) scanners deploy; (3) data is manageable. "
  "Reasoning path: a proof model explains research status and predicts clinical whole-body imaging. "
  "Proposed mechanism: 'clinically-proven' whole-body imaging - deployed systemic scanners. "
  "What would confirm it: whole-body PET changing care routinely. "
  "What would kill it: evidence that systemic imaging adds nothing. "
  "What this does not claim: it does not claim clinical whole-body imaging exists, offers no medical advice, and does not constitute a device recommendation."),
 "sig_lens": "The Signature lens reads imaging as organ-local, and asks what whole-body proof would systemic-ize.",
 "how_it_works": "Researchers study whole-body imaging through EXPLORER studies, systemic-disease research, and deployment analyses.",
 "key_points": [
  "EXPLORER was the first total-body PET.",
  "Systemic imaging revealed new biology.",
  "Scanners are rare.",
  "Data volumes are enormous.",
  "Clinical transformation is pending.",
 ],
 "requirements": [
  "Deployed total-body scanners.",
  "Care-changing systemic diagnoses.",
  "Clinical whole-body imaging.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Badawi RD et al. EXPLORER. Various; 2019-2022.",
  "Cherry SR et al. Total-body PET. Various; 2018-2021.",
  "Zhang X et al. Systemic imaging. Various; 2020-2023.",
  "Jones T et al. Whole-body reviews. Various; 2019-2022.",
 ],
 "demo_data": {"a": ("total-body PET scanners deployed (approx)", 5.0),
               "b": ("PET scanners worldwide (approx)", 5000.0), "bounds": (0.0005, 0.002),
               "step1": "five total-body of five thousand PET scanners - the unscaled systemic view",
               "confirm": "whole-body PET changes care routinely",
               "refute": "systemic imaging proves to add nothing"},
},
# ------------------------------------------------------------------ rank 34
{
 "key": "bme-future",
 "name": "The Future of Biomedical Engineering: A Century Ahead",
 "group": "Theory",
 "ladder_rank": 34, "ladder_tier": "advanced",
 "problem": "What will biomedical engineering become? The field extrapolates poorly - can its future be foreseen?",
 "description": "Biomedical-engineering futurology - predicting the field's century - is speculative: past predictions (artificial organs by 2000) failed; the field needs structured foresight; whether futures work improves decisions is the meta-question.",
 "background": "BME predictions have a poor record; scenario methods are used sporadically. As of 2026 the future is debated without discipline.",
 "why_it_matters": "Long-horizon decisions (research, infrastructure) need foresight: the discipline of BME futures.",
 "sig_pointer": "The Signature system's proposed approach builds disciplined BME foresight, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that BME futures need disciplined foresight: the scenario methods and roadmaps - with track records. "
  "Assumptions: (1) foresight is improvable; (2) methods exist; (3) they guide decisions. "
  "Reasoning path: a foresight model explains prediction failures and predicts better futures work. "
  "Proposed mechanism: 'disciplined' BME foresight - tracked scenario methods. "
  "What would confirm it: foresight with validated track records. "
  "What would kill it: evidence that BME futures are unforeseeable. "
  "What this does not claim: it does not claim any future, offers no medical advice, and does not constitute a prediction."),
 "sig_lens": "The Signature lens reads BME futures as undisciplined speculation, and asks what methods would foresee.",
 "how_it_works": "Researchers study BME futures through scenario methods, technology roadmapping, and prediction tracking.",
 "key_points": [
  "BME predictions have a poor record.",
  "Artificial organs were promised by 2000.",
  "Scenario methods are used sporadically.",
  "Long-horizon decisions need foresight.",
  "The discipline is undeveloped.",
 ],
 "requirements": [
  "Validated foresight methods.",
  "Track records for predictions.",
  "Decisions guided by foresight.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Bronzino JD et al. BME reviews. Various editions.",
  "Enderle JD et al. BME futures. Various; 2012-2022.",
  "Nerem RM et al. Field histories. Various; 2010-2020.",
  "NIH NIBIB. Strategic plans. Various.",
 ],
 "demo_data": {"a": ("BME predictions with validated track records (approx)", 5.0),
               "b": ("BME predictions made (approx)", 200.0), "bounds": (0.015, 0.04),
               "step1": "five tracked of two hundred made - the foresight without a record",
               "confirm": "foresight with validated track records",
               "refute": "BME futures prove unforeseeable"},
},
]
