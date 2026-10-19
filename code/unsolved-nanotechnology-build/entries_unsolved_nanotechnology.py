#!/usr/bin/env python3
"""Entries for The Unsolved Nanotechnology Database (unsolved-nanotechnology)
and its Signature half (unsolved-nanotechnology-signature).

34 famous unsolved problems in nanotechnology, ladder-ordered by accessibility
(rank 1 = most approachable, rank 34 = most complex/compounded).
Public half: real, fact-checked problems. Signature half: the same 34
problems through the Signature lens, with Signature-generated proposed
solutions that are ALWAYS labeled as proposals, never established science.

Honesty rule (enforced in every record): never claim proof, never imply
peer acceptance, never present speculation as settled. Signature proposals
are labeled speculation for research discussion only - never engineering
advice, never a nanotechnology recommendation; no safety or performance
claims. Nanotoxicology content is labeled speculation, never safety advice.
"""

LABEL = "Signature-generated proposed solution \u2014 not established science."

SIG_TAIL = ("Signature editions carry the Signature system's proposed "
            "solution approaches to famous unsolved problems. Every "
            "solution is labeled a Signature-generated proposal, never "
            "established science, never peer-accepted, never proof, never "
            "engineering or safety advice.")

STD_COMMON = [
    "Problem statements verified against the published nanotechnology literature; open status confirmed as of 2026.",
    "Signature solution sections are labeled proposals: they state assumptions, a reasoning path, a proposed mechanism, what would confirm or kill them, and what they do not claim.",
    "Signature proposals are labeled speculation for research discussion only - never engineering or safety advice, never a nanotechnology recommendation; no safety or performance claims appear.",
]

ENTRIES = [
# ------------------------------------------------------------------ rank 1
{
 "key": "nanomanufacturing",
 "name": "Nanomanufacturing: Building at Scale",
 "group": "Fabrication",
 "ladder_rank": 1, "ladder_tier": "foundations",
 "problem": "Nanostructures are made one at a time - can nanomanufacturing scale like silicon?",
 "description": "Nanomanufacturing - building at scale: electron-beam lithography makes exquisite structures slowly; self-assembly is fast but imperfect; and no nanomanufacturing method combines precision, speed, and cost. The nanofactory remains aspirational.",
 "background": "Nanofabrication (1970s-80s) enabled the field; the NNI (2000) funded manufacturing research; but scale-up lagged. As of 2026 nanomanufacturing is still artisanal.",
 "why_it_matters": "Scaled nanomanufacturing would make nanotech real: the factory for the nanoworld.",
 "sig_pointer": "The Signature system's proposed approach scales nanomanufacturing, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that nanomanufacturing needs hybrid methods: the top-down precision combined with bottom-up speed - with defect control. "
  "Assumptions: (1) hybrids work; (2) defects are controllable; (3) scale follows. "
  "Reasoning path: a hybrid model explains artisanal status and predicts scaled nanomanufacturing. "
  "Proposed mechanism: 'hybrid-scaled' nanomanufacturing - precision plus speed. "
  "What would confirm it: nanomanufactured products at scale. "
  "What would kill it: evidence that nanoscale can't be manufactured. "
  "What this does not claim: it does not claim scaled nanomanufacturing exists, offers no engineering advice, and does not constitute a manufacturing recommendation."),
 "sig_lens": "The Signature lens reads nanofabrication as artisanal, and asks what hybrids would scale.",
 "how_it_works": "Researchers study nanomanufacturing through nanoimprint lithography, directed self-assembly, and roll-to-roll research.",
 "key_points": [
  "E-beam lithography is precise but slow.",
  "Self-assembly is fast but imperfect.",
  "No method combines precision, speed, cost.",
  "The NNI funded manufacturing research.",
  "Nanomanufacturing is still artisanal.",
 ],
 "requirements": [
  "Hybrid precision-speed methods.",
  "Defect-controlled nanomanufacturing.",
  "Products at scale.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "NNI. Manufacturing research. Various; 2000 onward.",
  "Chou SY et al. Nanoimprint. Various; 1995-2015.",
  "Ross CA et al. Directed self-assembly. Various; 2008-2018.",
  "Rogers JA et al. Nanomanufacturing reviews. Various; 2013-2021.",
 ],
 "demo_data": {"a": ("nanoproducts made at scale (approx)", 5.0),
               "b": ("nanoproducts demonstrated (approx)", 200.0), "bounds": (0.015, 0.04),
               "step1": "five scaled of two hundred demonstrated - the artisanal nanoworld",
               "confirm": "nanomanufactured products at scale",
               "refute": "nanoscale proves unable to be manufactured"},
},
# ------------------------------------------------------------------ rank 2
{
 "key": "nanotoxicology",
 "name": "Nanotoxicology: Are Nanomaterials Safe?",
 "group": "Safety",
 "ladder_rank": 2, "ladder_tier": "foundations",
 "problem": "Nanomaterials are everywhere - but their long-term safety is incompletely understood. Are they safe?",
 "description": "Nanotoxicology - the safety question: nanoparticles' small size enables novel biological interactions; but long-term studies are incomplete; regulation lags; and the field debates whether nanomaterials need special rules.",
 "background": "Nanotoxicology (2000s) emerged with the NNI; studies found effects; but the evidence base is thin. As of 2026 safety is still being assessed.",
 "why_it_matters": "Understood nanosafety would enable confident nanotech: the safety the nanoworld needs.",
 "sig_pointer": "The Signature system's proposed approach assesses nanosafety systematically, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that nanosafety needs systematic assessment: the long-term studies completed - with regulation grounded. "
  "Assumptions: (1) studies are feasible; (2) they complete; (3) regulation follows. "
  "Reasoning path: an assessment model explains the evidence gap and predicts grounded safety. "
  "Proposed mechanism: 'systematically-assessed' nanosafety - completed evidence. "
  "What would confirm it: comprehensive nanosafety assessments. "
  "What would kill it: evidence that nanosafety can't be assessed. "
  "What this does not claim: it makes no safety claims about any nanomaterial, offers no safety advice, and does not constitute a regulatory recommendation."),
 "sig_lens": "The Signature lens reads nanosafety as evidence-thin, and asks what studies would ground.",
 "how_it_works": "Researchers study nanotoxicology through long-term exposure studies, characterization research, and regulatory science.",
 "key_points": [
  "Nanoparticles enable novel bio-interactions.",
  "Long-term studies are incomplete.",
  "Regulation lags the science.",
  "The evidence base is thin.",
  "Special rules are debated.",
 ],
 "requirements": [
  "Completed long-term studies.",
  "Comprehensive safety assessments.",
  "Grounded regulation.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Oberdörster G et al. Nanotoxicology. Various; 2005-2015.",
  "Nel A et al. Nano-bio interactions. Various; 2006-2016.",
  "Maynard AD et al. Safety reviews. Various; 2006-2016.",
  "Krug HF et al. Toxicology reviews. Various; 2011-2020.",
 ],
 "demo_data": {"a": ("nanomaterials with complete safety data, percent (approx)", 10.0),
               "b": ("percent scale", 100.0), "bounds": (0.05, 0.18),
               "step1": "nine in ten lack complete data - the unassessed nanoworld",
               "confirm": "comprehensive nanosafety assessments",
               "refute": "nanosafety proves unable to be assessed"},
},
# ------------------------------------------------------------------ rank 3
{
 "key": "molecular-assemblers",
 "name": "Molecular Assemblers: Drexler's Dream",
 "group": "Fabrication",
 "ladder_rank": 3, "ladder_tier": "foundations",
 "problem": "Can molecular assemblers build anything atom by atom - or is Drexler's dream impossible?",
 "description": "Molecular assemblers - Drexler's dream (1986, Engines of Creation): machines that build atom by atom; but the Smalley-Drexler debate (2003) questioned feasibility; and no assembler exists. The dream is still debated.",
 "background": "Drexler (1986) proposed assemblers; Smalley (2003) argued 'fat fingers' defeat them; the debate never resolved. As of 2026 assemblers are conceptual.",
 "why_it_matters": "Molecular assemblers would end manufacturing: building anything from atoms.",
 "sig_pointer": "The Signature system's proposed approach assesses molecular assembly, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that assembly needs feasibility proof: the atom-by-atom construction demonstrated - with the debate settled. "
  "Assumptions: (1) feasibility is testable; (2) demos are possible; (3) the debate settles. "
  "Reasoning path: a proof model explains the stalemate and predicts resolved assembly. "
  "Proposed mechanism: 'feasibility-proven' molecular assembly - demonstrated construction. "
  "What would confirm it: demonstrated molecular assemblers. "
  "What would kill it: evidence that assemblers are impossible. "
  "What this does not claim: it does not claim assemblers exist, offers no engineering advice, and does not constitute a feasibility claim."),
 "sig_lens": "The Signature lens reads assemblers as debated dream, and asks what proof would settle.",
 "how_it_works": "Researchers study molecular assembly through STM manipulation, DNA origami, and feasibility analyses.",
 "key_points": [
  "Drexler proposed assemblers (1986).",
  "Smalley argued impossibility (2003).",
  "The debate never resolved.",
  "No assembler exists.",
  "STM manipulates atoms singly.",
 ],
 "requirements": [
  "Feasibility demonstrations.",
  "Atom-by-atom construction.",
  "Settled debate.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Drexler KE. Engines of Creation. 1986.",
  "Smalley RE. Drexler-Smalley debate. Various; 2001-2003.",
  "Eigler DM et al. STM manipulation. Various; 1990-2000.",
  "Merkle RC et al. Assembly analyses. Various; 1997-2015.",
 ],
 "demo_data": {"a": ("atoms placed by assemblers (approx)", 1.0),
               "b": ("atoms in a product (approx)", 100000000000000000000000.0), "bounds": (0.0, 0.0000000000000000001),
               "step1": "atoms placed one STM-tip at a time - the unbuilt assembler",
               "confirm": "demonstrated molecular assemblers",
               "refute": "assemblers prove impossible"},
},
# ------------------------------------------------------------------ rank 4
{
 "key": "nanorobotics",
 "name": "Nanorobotics: Machines at the Nanoscale",
 "group": "Devices",
 "ladder_rank": 4, "ladder_tier": "foundations",
 "problem": "Can robots work at the nanoscale - swimming, sensing, and acting inside the body?",
 "description": "Nanorobotics - machines at the nanoscale: DNA nanorobots (Douglas, 2012) demonstrated logic; magnetic swimmers navigate; but true nanorobots (sensing, deciding, acting) are primitive; and the body is a hostile environment.",
 "background": "Nanorobotics (1990s-2000s) was conceptual; DNA origami (2006, Rothemund) enabled structures; DNA nanorobots (2012) showed logic. As of 2026 nanorobots are primitive.",
 "why_it_matters": "Working nanorobots would transform medicine: the surgeon at the nanoscale.",
 "sig_pointer": "The Signature system's proposed approach builds working nanorobots, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that nanorobots need integrated function: the sensing, deciding, and acting combined - with in-vivo operation. "
  "Assumptions: (1) integration is possible; (2) the body tolerates; (3) function works. "
  "Reasoning path: an integration model explains primitive status and predicts working nanorobots. "
  "Proposed mechanism: 'function-integrated' nanorobots - sensing-deciding-acting machines. "
  "What would confirm it: nanorobots operating in vivo. "
  "What would kill it: evidence that nanorobots can't function. "
  "What this does not claim: it does not claim working nanorobots exist, offers no medical advice, and does not constitute a device recommendation."),
 "sig_lens": "The Signature lens reads nanorobots as unintegrated parts, and asks what integration would make machine.",
 "how_it_works": "Researchers study nanorobotics through DNA-origami robots, magnetic swimmers, and in-vivo trials.",
 "key_points": [
  "DNA nanorobots demonstrated logic.",
  "Magnetic swimmers navigate fluids.",
  "True nanorobots are primitive.",
  "The body is hostile.",
  "Integration is the challenge.",
 ],
 "requirements": [
  "Integrated sensing-deciding-acting.",
  "In-vivo nanorobot operation.",
  "Working medical nanorobots.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Douglas SM et al. DNA nanorobots. Science. 2012;335:831-834.",
  "Rothemund PWK. DNA origami. Various; 2006-2012.",
  "Nelson BJ et al. Microrobotics. Various; 2010-2020.",
  "Li J et al. Nanorobot reviews. Various; 2017-2022.",
 ],
 "demo_data": {"a": ("nanorobots operating in vivo (approx)", 2.0),
               "b": ("nanorobot designs published (approx)", 200.0), "bounds": (0.004, 0.02),
               "step1": "two in vivo of two hundred designed - the unintegrated machine",
               "confirm": "nanorobots operate in vivo",
               "refute": "nanorobots prove unable to function"},
},
# ------------------------------------------------------------------ rank 5
{
 "key": "nanoelectronics",
 "name": "Nanoelectronics: Beyond Silicon",
 "group": "Devices",
 "ladder_rank": 5, "ladder_tier": "foundations",
 "problem": "Silicon scaling ends - can nanoelectronics (nanotubes, nanowires) continue Moore's law?",
 "description": "Nanoelectronics - beyond silicon: carbon nanotubes and nanowires promise continued scaling; but placement, purity, and contacts challenge; and no nanoelectronic technology has displaced silicon. The industry's bet remains extending silicon - EUV, gate-all-around, 3D stacking - while nanotube computers like Shulaker's 2019 16-bit RISC-V demo stay laboratory milestones.",
 "background": "Nanoelectronics (1990s-2000s) promised post-silicon; nanotube transistors (1998-2010s) were demonstrated; but manufacturing lagged. As of 2026 silicon still rules.",
 "why_it_matters": "Post-silicon nanoelectronics would continue computing's progress: the transistor after silicon.",
 "sig_pointer": "The Signature system's proposed approach builds post-silicon nanoelectronics, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that nanoelectronics needs manufacturing: the placement and purity solved - with silicon displaced. "
  "Assumptions: (1) manufacturing is solvable; (2) devices perform; (3) displacement happens. "
  "Reasoning path: a manufacturing model explains silicon's persistence and predicts nanoelectronic computing. "
  "Proposed mechanism: 'manufacturing-solved' nanoelectronics - placed pure devices. "
  "What would confirm it: nanoelectronic chips in products. "
  "What would kill it: evidence that nanoelectronics can't be manufactured. "
  "What this does not claim: it does not claim post-silicon chips exist, offers no engineering advice, and does not constitute a technology recommendation."),
 "sig_lens": "The Signature lens reads nanoelectronics as unmanufacturable promise, and asks what placement would displace.",
 "how_it_works": "Researchers study nanoelectronics through nanotube placement, purity research, and device prototyping.",
 "key_points": [
  "Silicon scaling is ending.",
  "Nanotubes promise continued scaling.",
  "Placement and purity are hard.",
  "No technology displaced silicon.",
  "Manufacturing is the barrier.",
 ],
 "requirements": [
  "Solved placement and purity.",
  "Nanoelectronic chips in products.",
  "Post-silicon computing.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Tans SJ et al. Nanotube transistors. Various; 1998-2005.",
  "Franklin AD et al. Nanotube devices. Various; 2012-2020.",
  "Shulaker MM et al. Nanotube computers. Various; 2013-2019.",
  "Cauchois R et al. Nanoelectronics reviews. Various; 2015-2021.",
 ],
 "demo_data": {"a": ("nanoelectronic chips in products (approx)", 1.0),
               "b": ("silicon chips shipped, billions (approx)", 30.0), "bounds": (0.015, 0.06),
               "step1": "one against thirty billion - the undisplaced silicon",
               "confirm": "nanoelectronic chips in products",
               "refute": "nanoelectronics prove unable to be manufactured"},
},
# ------------------------------------------------------------------ rank 6
{
 "key": "nanomedicine",
 "name": "Nanomedicine: The Promise and the Delivery",
 "group": "Devices",
 "ladder_rank": 6, "ladder_tier": "foundations",
 "problem": "Nanomedicine promises targeted therapy - but delivery efficiency is dismal. Can it deliver?",
 "description": "Nanomedicine - the promise and the delivery: nanoparticles target tumors; but ~1% reach the target; the EPR effect is debated; and clinical translation is slow. The promise outruns the delivery. Liposomal drugs like Doxil proved nanoparticles can work clinically, yet the field's central embarrassment - that targeting efficiency barely beats passive accumulation - remains unresolved.",
 "background": "Nanomedicine (2000s) promised targeting; Doxil (1995) was the early success; but the delivery problem persisted. As of 2026 translation is slow.",
 "why_it_matters": "Delivering nanomedicine would transform therapy: the targeted treatment made real.",
 "sig_pointer": "The Signature system's proposed approach makes nanomedicine deliver, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that nanomedicine needs delivery science: the targeting mechanisms understood - with efficiency proven. "
  "Assumptions: (1) mechanisms are learnable; (2) efficiency is improvable; (3) translation follows. "
  "Reasoning path: a delivery model explains the promise gap and predicts working nanomedicine. "
  "Proposed mechanism: 'delivery-proven' nanomedicine - efficient targeting. "
  "What would confirm it: efficient nanomedicine in clinical use. "
  "What would kill it: evidence that delivery can't be efficient. "
  "What this does not claim: it does not claim efficient nanomedicine exists, offers no medical advice, and does not constitute a development recommendation."),
 "sig_lens": "The Signature lens reads nanomedicine as undelivered promise, and asks what science would target.",
 "how_it_works": "Researchers study nanomedicine through delivery research, EPR debates, and translation studies.",
 "key_points": [
  "Only ~1% of nanoparticles reach tumors.",
  "The EPR effect is debated.",
  "Clinical translation is slow.",
  "Doxil was the early success.",
  "Promise outruns delivery.",
 ],
 "requirements": [
  "Understood delivery mechanisms.",
  "Proven targeting efficiency.",
  "Clinical nanomedicine.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Wilhelm S et al. Delivery efficiency. Various; 2016-2021.",
  "Doxil / liposomal drugs. Various; 1995 onward.",
  "Danhier F et al. EPR debate. Various; 2010-2018.",
  "Shi J et al. Nanomedicine reviews. Various; 2017-2021.",
 ],
 "demo_data": {"a": ("injected dose reaching tumors, percent (approx)", 1.0),
               "b": ("percent scale", 100.0), "bounds": (0.005, 0.02),
               "step1": "one percent delivered - the undelivered promise",
               "confirm": "efficient nanomedicine in clinical use",
               "refute": "delivery proves unable to be efficient"},
},
# ------------------------------------------------------------------ rank 7
{
 "key": "quantum-dots",
 "name": "Quantum Dots: The Tunable Nanocrystals",
 "group": "Devices",
 "ladder_rank": 7, "ladder_tier": "foundations",
 "problem": "Quantum dots are tunable and bright - but can they be made safe and scaled?",
 "description": "Quantum dots - tunable nanocrystals: the optics are superb; but cadmium toxicity concerns; InP alternatives are inferior; and the display market is the main success. Broader applications need safe scaled dots.",
 "background": "Quantum dots (1980s-90s, Ekimov, Brus) were discovered; displays (2010s) commercialized; but toxicity limited spread. As of 2026 dots are display-deep.",
 "why_it_matters": "Safe scaled quantum dots would transform displays, solar, and bioimaging: the tunable crystal everywhere.",
 "sig_pointer": "The Signature system's proposed approach makes quantum dots safe and scaled, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that quantum dots need safe scaling: the cadmium-free compositions matching performance - with manufacturing scaled. "
  "Assumptions: (1) alternatives match; (2) manufacturing scales; (3) applications spread. "
  "Reasoning path: a materials model explains display-only status and predicts ubiquitous dots. "
  "Proposed mechanism: 'safely-scaled' quantum dots - cadmium-free production. "
  "What would confirm it: safe quantum dots in broad applications. "
  "What would kill it: evidence that safe dots can't match. "
  "What this does not claim: it makes no safety claims, offers no engineering advice, and does not constitute a materials recommendation."),
 "sig_lens": "The Signature lens reads quantum dots as toxic success, and asks what compositions would make safe.",
 "how_it_works": "Researchers study quantum dots through InP development, cadmium-free research, and scale-up studies.",
 "key_points": [
  "Quantum dots are tunable and bright.",
  "Cadmium toxicity concerns.",
  "Displays are the main success.",
  "InP alternatives are inferior.",
  "Broader use needs safe dots.",
 ],
 "requirements": [
  "Cadmium-free matching performance.",
  "Scaled safe manufacturing.",
  "Broad quantum-dot applications.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Ekimov AI et al. Quantum dots. Various; 1980s-1990s.",
  "Brus LE et al. Nanocrystals. Various; 1983-1998.",
  "Nobel Prize in Chemistry. 2023.",
  "Shirasaki Y et al. Display applications. Various; 2013-2020.",
 ],
 "demo_data": {"a": ("quantum-dot applications beyond displays (approx)", 5.0),
               "b": ("potential quantum-dot applications (approx)", 50.0), "bounds": (0.05, 0.18),
               "step1": "five beyond displays of fifty potential - the toxic limitation",
               "confirm": "safe quantum dots in broad applications",
               "refute": "safe dots prove unable to match"},
},
# ------------------------------------------------------------------ rank 8
{
 "key": "nanocomposites",
 "name": "Nanocomposites: The Promise of the Filler",
 "group": "Materials",
 "ladder_rank": 8, "ladder_tier": "foundations",
 "problem": "Nanofillers promise super-materials - but dispersion is hard and the gains are modest. Can nanocomposites deliver?",
 "description": "Nanocomposites - the filler promise: nanotubes and graphene in polymers promise strength; but agglomeration defeats dispersion; the gains are incremental; and the super-material is pending. Carbon-fiber composites succeeded without nano, which sharpens the question: what does the nanofiller add that microfillers don't, and is it worth the dispersion fight?",
 "background": "Nanocomposites (1990s-2000s) promised much; dispersion proved hard; but incremental gains accumulated. As of 2026 the super-material is still pending.",
 "why_it_matters": "Delivering nanocomposites would transform structures: the filler that fortifies.",
 "sig_pointer": "The Signature system's proposed approach disperses nanofillers perfectly, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that nanocomposites need perfect dispersion: the fillers uniformly distributed - with interface engineering. "
  "Assumptions: (1) dispersion is achievable; (2) interfaces bond; (3) properties follow. "
  "Reasoning path: a dispersion model explains modest gains and predicts super-materials. "
  "Proposed mechanism: 'perfectly-dispersed' nanocomposites - uniform fillers. "
  "What would confirm it: nanocomposites with transformative properties. "
  "What would kill it: evidence that dispersion is inherently limited. "
  "What this does not claim: it does not claim super-nanocomposites exist, offers no engineering advice, and does not constitute a materials recommendation."),
 "sig_lens": "The Signature lens reads nanocomposites as agglomerated promise, and asks what dispersion would deliver.",
 "how_it_works": "Researchers study nanocomposites through dispersion research, interface engineering, and property testing.",
 "key_points": [
  "Nanofillers promise super-materials.",
  "Agglomeration defeats dispersion.",
  "Gains are incremental.",
  "Interface engineering helps.",
  "The super-material is pending.",
 ],
 "requirements": [
  "Uniform filler dispersion.",
  "Engineered interfaces.",
  "Transformative nanocomposites.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Ajayan PM et al. Nanocomposites. Various; 2003-2015.",
  "Moniruzzaman M et al. Dispersion reviews. Various; 2006-2012.",
  "Potts JR et al. Graphene composites. Various; 2011-2016.",
  "Coleman JN et al. Filler research. Various; 2006-2015.",
 ],
 "demo_data": {"a": ("nanocomposites with transformative properties (approx)", 5.0),
               "b": ("nanocomposites developed (approx)", 200.0), "bounds": (0.015, 0.04),
               "step1": "five transformative of two hundred developed - the agglomerated promise",
               "confirm": "nanocomposites with transformative properties",
               "refute": "dispersion proves inherently limited"},
},
# ------------------------------------------------------------------ rank 9
{
 "key": "nanosensors",
 "name": "Nanosensors: The Ultimate Detectors",
 "group": "Devices",
 "ladder_rank": 9, "ladder_tier": "foundations",
 "problem": "Nanosensors can detect single molecules - but can they work reliably outside the lab?",
 "description": "Nanosensors - ultimate detectors: nanowire and nanotube sensors detect single molecules; but drift, fouling, and calibration defeat field use; and the lab-to-field gap is wide. Lieber's nanowire sensors set the sensitivity bar two decades ago; the field has been trying to make them leave the laboratory ever since.",
 "background": "Nanosensors (2000s-2010s, Lieber) demonstrated sensitivity; but real-world deployment lagged. As of 2026 nanosensors are lab-bound.",
 "why_it_matters": "Field-ready nanosensors would transform diagnostics and environment: the detector everywhere.",
 "sig_pointer": "The Signature system's proposed approach makes nanosensors field-ready, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that nanosensors need field robustness: the drift and fouling solved - with calibration maintained. "
  "Assumptions: (1) robustness is achievable; (2) calibration holds; (3) deployment follows. "
  "Reasoning path: a robustness model explains lab-bound status and predicts field sensors. "
  "Proposed mechanism: 'field-robust' nanosensors - drift-free detectors. "
  "What would confirm it: nanosensors deployed in diagnostics and environment. "
  "What would kill it: evidence that nanosensors can't leave the lab. "
  "What this does not claim: it does not claim field nanosensors exist, offers no engineering advice, and does not constitute a device recommendation."),
 "sig_lens": "The Signature lens reads nanosensors as lab-bound sensitivity, and asks what robustness would deploy.",
 "how_it_works": "Researchers study nanosensors through anti-fouling research, drift correction, and field trials.",
 "key_points": [
  "Nanosensors detect single molecules.",
  "Drift and fouling defeat field use.",
  "Calibration is hard.",
  "The lab-to-field gap is wide.",
  "Deployment lags sensitivity.",
 ],
 "requirements": [
  "Drift-free field operation.",
  "Anti-fouling proven.",
  "Deployed nanosensors.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Lieber CM et al. Nanowire sensors. Various; 2001-2015.",
  "Cui Y et al. Single-molecule detection. Various; 2001-2010.",
  "Stern E et al. Field challenges. Various; 2007-2015.",
  "Zhang A et al. Sensor reviews. Various; 2016-2021.",
 ],
 "demo_data": {"a": ("nanosensors deployed in the field (approx)", 10.0),
               "b": ("nanosensor designs published (approx)", 500.0), "bounds": (0.01, 0.035),
               "step1": "ten deployed of five hundred designed - the lab-bound detector",
               "confirm": "nanosensors deployed in diagnostics and environment",
               "refute": "nanosensors prove unable to leave the lab"},
},
# ------------------------------------------------------------------ rank 10
{
 "key": "dna-origami",
 "name": "DNA Origami: Programming Matter",
 "group": "Fabrication",
 "ladder_rank": 10, "ladder_tier": "foundations",
 "problem": "DNA origami folds matter programmably - but can it scale beyond the lab bench?",
 "description": "DNA origami - programming matter: Rothemund (2006) showed DNA folds into shapes; but the structures are small, expensive, and fragile; and scaling to useful devices is the challenge. The structures fold beautifully and cheaply at microgram scale; the jump to grams, devices, and dollars is the entire problem.",
 "background": "DNA origami (2006) launched the field; 3D origami (2009) expanded; but scale and cost limited. As of 2026 origami is still bench-scale.",
 "why_it_matters": "Scaled DNA origami would program matter: the fold that builds.",
 "sig_pointer": "The Signature system's proposed approach scales DNA origami, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that origami needs scaled synthesis: the DNA produced cheaply - with structures enlarged. "
  "Assumptions: (1) synthesis scales; (2) costs fall; (3) devices follow. "
  "Reasoning path: a synthesis model explains bench status and predicts scaled origami. "
  "Proposed mechanism: 'synthesis-scaled' DNA origami - cheap large structures. "
  "What would confirm it: DNA-origami devices in applications. "
  "What would kill it: evidence that origami can't scale. "
  "What this does not claim: it does not claim scaled origami exists, offers no engineering advice, and does not constitute a manufacturing recommendation."),
 "sig_lens": "The Signature lens reads origami as bench-scale programming, and asks what synthesis would scale.",
 "how_it_works": "Researchers study DNA origami through scaled synthesis, 3D design, and application prototyping.",
 "key_points": [
  "DNA folds into programmable shapes.",
  "Structures are small and expensive.",
  "3D origami expanded the field.",
  "Scaling is the challenge.",
  "Origami is bench-scale.",
 ],
 "requirements": [
  "Cheap scaled DNA synthesis.",
  "Enlarged robust structures.",
  "Origami devices in applications.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Rothemund PWK. DNA origami. Various; 2006-2012.",
  "Douglas SM et al. 3D origami. Various; 2009-2012.",
  "Dietz H et al. Origami advances. Various; 2009-2020.",
  "Seeman NC et al. Structural DNA. Various; 1982-2016.",
 ],
 "demo_data": {"a": ("DNA-origami devices in applications (approx)", 3.0),
               "b": ("origami structures published (approx)", 300.0), "bounds": (0.005, 0.018),
               "step1": "three applied of three hundred folded - the bench-scale program",
               "confirm": "DNA-origami devices in applications",
               "refute": "origami proves unable to scale"},
},
# ------------------------------------------------------------------ rank 11
{
 "key": "plasmonics",
 "name": "Plasmonics: Light at the Nanoscale",
 "group": "Devices",
 "ladder_rank": 11, "ladder_tier": "foundations",
 "problem": "Plasmonics concentrates light below diffraction - but losses are high. Can plasmonics be practical?",
 "description": "Plasmonics - light at the nanoscale: surface plasmons beat diffraction; but metal losses are severe; and applications (sensing, SERS) are niche. Low-loss plasmonics is the goal. Sensing applications like SERS work because enhancement matters more than loss; everything else in plasmonics is still waiting on materials that don't yet exist.",
 "background": "Plasmonics (1990s-2000s, Ebbesen, Atwater) grew rapidly; but losses limited; SERS succeeded. As of 2026 plasmonics is still loss-limited.",
 "why_it_matters": "Practical plasmonics would transform optics: light controlled at the nanoscale.",
 "sig_pointer": "The Signature system's proposed approach makes plasmonics practical, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that plasmonics needs low-loss materials: the losses engineered away - with devices practical. "
  "Assumptions: (1) losses are reducible; (2) materials exist; (3) devices follow. "
  "Reasoning path: a materials model explains niche status and predicts practical plasmonics. "
  "Proposed mechanism: 'low-loss' plasmonics - engineered materials. "
  "What would confirm it: plasmonic devices in broad use. "
  "What would kill it: evidence that plasmonic losses are fundamental. "
  "What this does not claim: it does not claim practical plasmonics exists, offers no engineering advice, and does not constitute a device recommendation."),
 "sig_lens": "The Signature lens reads plasmonics as loss-limited light, and asks what materials would make practical.",
 "how_it_works": "Researchers study plasmonics through low-loss materials, SERS applications, and device prototyping.",
 "key_points": [
  "Plasmons beat the diffraction limit.",
  "Metal losses are severe.",
  "SERS is the main success.",
  "Applications are niche.",
  "Low-loss materials are the goal.",
 ],
 "requirements": [
  "Low-loss plasmonic materials.",
  "Practical plasmonic devices.",
  "Broad plasmonic applications.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Ebbesen TW et al. Extraordinary transmission. Various; 1998-2005.",
  "Atwater HA et al. Plasmonics. Various; 2007-2015.",
  "Maier SA et al. Reviews. Various; 2007-2015.",
  "Knight MW et al. Loss research. Various; 2013-2019.",
 ],
 "demo_data": {"a": ("plasmonic devices in broad use (approx)", 5.0),
               "b": ("plasmonic concepts demonstrated (approx)", 200.0), "bounds": (0.015, 0.04),
               "step1": "five broad of two hundred demonstrated - the lossy light",
               "confirm": "plasmonic devices in broad use",
               "refute": "plasmonic losses prove fundamental"},
},
# ------------------------------------------------------------------ rank 12
{
 "key": "nanophotonics",
 "name": "Nanophotonics: Controlling Light",
 "group": "Devices",
 "ladder_rank": 12, "ladder_tier": "compounded",
 "problem": "Nanophotonics controls light at the nanoscale - but can it displace electronics?",
 "description": "Nanophotonics - controlling light: photonic crystals, metasurfaces, and integrated photonics promise optical computing; but the electronics displacement is distant; and nanophotonics is still mostly interconnect.",
 "background": "Nanophotonics (1990s-2000s) grew; silicon photonics (2010s) commercialized interconnect; but computing is pending. As of 2026 photonics connects; it doesn't compute.",
 "why_it_matters": "Computing nanophotonics would transform information: light instead of electrons.",
 "sig_pointer": "The Signature system's proposed approach makes nanophotonics compute, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that nanophotonics needs computing architectures: the optical logic demonstrated - with electronics displaced. "
  "Assumptions: (1) architectures exist; (2) they compute; (3) displacement happens. "
  "Reasoning path: an architecture model explains interconnect-only status and predicts optical computing. "
  "Proposed mechanism: 'computing' nanophotonics - optical logic. "
  "What would confirm it: nanophotonic processors in use. "
  "What would kill it: evidence that photonics can't compute. "
  "What this does not claim: it does not claim optical computing exists, offers no engineering advice, and does not constitute a technology recommendation."),
 "sig_lens": "The Signature lens reads photonics as interconnect-only, and asks what architectures would compute.",
 "how_it_works": "Researchers study nanophotonics through optical-logic research, metasurface computing, and integration studies.",
 "key_points": [
  "Silicon photonics commercialized interconnect.",
  "Optical computing is pending.",
  "Metasurfaces promise new functions.",
  "Photonics connects; it doesn't compute.",
  "Displacement is distant.",
 ],
 "requirements": [
  "Demonstrated optical logic.",
  "Nanophotonic processors.",
  "Electronics displacement.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Joannopoulos JD et al. Photonic crystals. Various; 1995-2008.",
  "Thomson D et al. Silicon photonics. Various; 2016-2021.",
  "Miller DAB et al. Optical computing. Various; 2017-2023.",
  "Shainline JM et al. Photonic processors. Various; 2017-2022.",
 ],
 "demo_data": {"a": ("optical processors in use (approx)", 2.0),
               "b": ("electronic processors shipped, billions (approx)", 5.0), "bounds": (0.2, 0.7),
               "step1": "two optical against five billion electronic - the uncomputed light",
               "confirm": "nanophotonic processors in use",
               "refute": "photonics proves unable to compute"},
},
# ------------------------------------------------------------------ rank 13
{
 "key": "nanofluidics",
 "name": "Nanofluidics: Fluids at the Nanoscale",
 "group": "Devices",
 "ladder_rank": 13, "ladder_tier": "compounded",
 "problem": "Fluids behave strangely at the nanoscale - can nanofluidics be engineered into devices?",
 "description": "Nanofluidics - fluids at the nanoscale: slip flow, ion selectivity, and desalination promise; but the physics is incompletely understood; and devices are mostly lab demos. Desalination membranes and osmotic power are the prize applications, but both need the transport physics nailed down first.",
 "background": "Nanofluidics (2000s-2010s) revealed strange transport; desalination membranes were proposed; but engineering lagged. As of 2026 nanofluidics is still emerging.",
 "why_it_matters": "Engineered nanofluidics would transform filtration and energy: the fluid at the nanoscale.",
 "sig_pointer": "The Signature system's proposed approach engineers nanofluidics, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that nanofluidics needs understood transport: the nanoscale flows modeled - with devices engineered. "
  "Assumptions: (1) transport is modelable; (2) devices are engineerable; (3) applications follow. "
  "Reasoning path: a transport model explains demo-status and predicts nanofluidic devices. "
  "Proposed mechanism: 'transport-understood' nanofluidics - engineered flows. "
  "What would confirm it: nanofluidic devices in applications. "
  "What would kill it: evidence that nanofluidics can't be engineered. "
  "What this does not claim: it does not claim nanofluidic devices exist at scale, offers no engineering advice, and does not constitute a device recommendation."),
 "sig_lens": "The Signature lens reads nanofluidics as unmodeled flow, and asks what transport would engineer.",
 "how_it_works": "Researchers study nanofluidics through transport modeling, membrane prototyping, and desalination research.",
 "key_points": [
  "Nanoscale fluids behave strangely.",
  "Slip flow and ion selectivity promise.",
  "The physics is incompletely understood.",
  "Devices are mostly lab demos.",
  "Engineering lags the science.",
 ],
 "requirements": [
  "Modeled nanoscale transport.",
  "Engineered nanofluidic devices.",
  "Applications in filtration and energy.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Bocquet L et al. Nanofluidics. Various; 2007-2020.",
  "Schoch RB et al. Transport reviews. Various; 2008-2015.",
  "Elimelech M et al. Desalination membranes. Various; 2011-2019.",
  "Secchi E et al. Slip flow. Various; 2016-2021.",
 ],
 "demo_data": {"a": ("nanofluidic devices in applications (approx)", 5.0),
               "b": ("nanofluidic concepts demonstrated (approx)", 150.0), "bounds": (0.02, 0.05),
               "step1": "five applied of a hundred fifty demonstrated - the unengineered flow",
               "confirm": "nanofluidic devices in applications",
               "refute": "nanofluidics prove unable to be engineered"},
},
# ------------------------------------------------------------------ rank 14
{
 "key": "nanocatalysis",
 "name": "Nanocatalysis: Catalysts at the Nanoscale",
 "group": "Materials",
 "ladder_rank": 14, "ladder_tier": "compounded",
 "problem": "Nanocatalysts are active - but can they be designed rather than discovered?",
 "description": "Nanocatalysis - catalysts at the nanoscale: size effects boost activity; but the active sites are debated; design is empirical; and the field still discovers more than designs. Single-atom catalysts were the 2011 breakthrough; a decade later the field still argues about what the active site actually is.",
 "background": "Nanocatalysis (2000s-2010s) grew; single-atom catalysts (2011) were the frontier; but design lags. As of 2026 discovery still dominates.",
 "why_it_matters": "Designed nanocatalysts would transform chemistry: the catalyst by design.",
 "sig_pointer": "The Signature system's proposed approach designs nanocatalysts, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that nanocatalysis needs site design: the active sites predicted - with catalysts designed. "
  "Assumptions: (1) sites are predictable; (2) design works; (3) industry adopts. "
  "Reasoning path: a design model explains empirical status and predicts designed catalysts. "
  "Proposed mechanism: 'site-designed' nanocatalysis - predicted active sites. "
  "What would confirm it: designed nanocatalysts in industrial use. "
  "What would kill it: evidence that nanocatalysis resists design. "
  "What this does not claim: it does not claim designed nanocatalysts exist, offers no engineering advice, and does not constitute a materials recommendation."),
 "sig_lens": "The Signature lens reads nanocatalysis as empirical discovery, and asks what sites would design.",
 "how_it_works": "Researchers study nanocatalysis through single-atom research, site characterization, and design modeling.",
 "key_points": [
  "Size effects boost catalytic activity.",
  "Active sites are debated.",
  "Design is empirical.",
  "Single-atom catalysts are the frontier.",
  "Discovery still dominates.",
 ],
 "requirements": [
  "Predicted active sites.",
  "Designed nanocatalysts.",
  "Industrial designed catalysts.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Qiao B et al. Single-atom catalysts. Various; 2011-2016.",
  "Liu L et al. Nanocatalysis reviews. Various; 2016-2021.",
  "Schauermann S et al. Site studies. Various; 2013-2019.",
  "Corma A et al. Design perspectives. Various; 2016-2022.",
 ],
 "demo_data": {"a": ("nanocatalysts designed computationally (approx)", 10.0),
               "b": ("nanocatalysts in use (approx)", 200.0), "bounds": (0.03, 0.08),
               "step1": "one in twenty designed - the empirical catalyst",
               "confirm": "designed nanocatalysts in industrial use",
               "refute": "nanocatalysis proves to resist design"},
},
# ------------------------------------------------------------------ rank 15
{
 "key": "nanodiamonds",
 "name": "Nanodiamonds: The Quantum Sensors",
 "group": "Devices",
 "ladder_rank": 15, "ladder_tier": "compounded",
 "problem": "NV centers in nanodiamonds sense fields at the nanoscale - but can they become practical quantum sensors?",
 "description": "Nanodiamonds - quantum sensors: nitrogen-vacancy centers detect magnetic fields with nanoscale resolution; but the sensors are lab-bound; biocompatibility is promising; and practical deployment is pending.",
 "background": "NV sensing (2000s-2010s) was demonstrated; nanodiamond biocompatibility was shown; but devices lag. As of 2026 quantum sensing is still emerging.",
 "why_it_matters": "Practical nanodiamond sensors would transform measurement: the quantum sensor everywhere.",
 "sig_pointer": "The Signature system's proposed approach deploys nanodiamond sensors, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that nanodiamonds need device engineering: the NV centers integrated - with sensors deployed. "
  "Assumptions: (1) integration works; (2) sensors are practical; (3) deployment follows. "
  "Reasoning path: a device model explains lab-bound status and predicts deployed sensors. "
  "Proposed mechanism: 'device-integrated' nanodiamond sensors - practical quantum measurement. "
  "What would confirm it: nanodiamond sensors in applications. "
  "What would kill it: evidence that NV sensing can't be practical. "
  "What this does not claim: it does not claim practical sensors exist, offers no engineering advice, and does not constitute a device recommendation."),
 "sig_lens": "The Signature lens reads NV centers as lab-bound physics, and asks what integration would deploy.",
 "how_it_works": "Researchers study nanodiamonds through NV integration, biocompatibility studies, and sensor prototyping.",
 "key_points": [
  "NV centers sense at the nanoscale.",
  "The sensors are lab-bound.",
  "Biocompatibility is promising.",
  "Practical deployment is pending.",
  "Quantum sensing is still emerging.",
 ],
 "requirements": [
  "Integrated NV sensors.",
  "Practical quantum measurement.",
  "Deployed nanodiamond sensors.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Maze JR et al. NV sensing. Various; 2008-2011.",
  "Rondin L et al. Magnetometry reviews. Various; 2014-2019.",
  "Mochalin VN et al. Nanodiamond reviews. Various; 2012-2020.",
  "Schirhagl R et al. Bio-applications. Various; 2014-2021.",
 ],
 "demo_data": {"a": ("nanodiamond sensors deployed (approx)", 5.0),
               "b": ("NV-sensing papers (approx)", 1000.0), "bounds": (0.002, 0.01),
               "step1": "five deployed of a thousand published - the lab-bound quantum",
               "confirm": "nanodiamond sensors in applications",
               "refute": "NV sensing proves unable to be practical"},
},
# ------------------------------------------------------------------ rank 16
{
 "key": "nanotubes",
 "name": "Carbon Nanotubes: The Unfulfilled Promise",
 "group": "Materials",
 "ladder_rank": 16, "ladder_tier": "compounded",
 "problem": "Carbon nanotubes are the strongest material known - but can they be made long, pure, and placed?",
 "description": "Carbon nanotubes - the unfulfilled promise: Iijima (1991) revealed them; the properties are extraordinary; but long, pure, placed nanotubes are still hard; and the space elevator remains a joke. The space-elevator joke persists because the gap between a nanotube's theoretical strength and a spun fiber's actual strength refuses to close.",
 "background": "Nanotubes (1991) were the sensation; the field grew enormously; but manufacturing lagged. As of 2026 nanotubes are still mostly promise.",
 "why_it_matters": "Controlled nanotubes would transform materials: the strongest fiber made useful.",
 "sig_pointer": "The Signature system's proposed approach controls nanotube growth, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that nanotubes need controlled growth: the length, purity, and placement engineered - with applications following. "
  "Assumptions: (1) growth is controllable; (2) properties follow; (3) applications spread. "
  "Reasoning path: a growth model explains the promise gap and predicts controlled nanotubes. "
  "Proposed mechanism: 'growth-controlled' nanotubes - long pure placed fibers. "
  "What would confirm it: controlled nanotubes in structural use. "
  "What would kill it: evidence that nanotubes can't be controlled. "
  "What this does not claim: it does not claim controlled nanotubes exist, offers no engineering advice, and does not constitute a materials recommendation."),
 "sig_lens": "The Signature lens reads nanotubes as uncontrolled wonder, and asks what growth would make useful.",
 "how_it_works": "Researchers study nanotubes through CVD growth control, purity research, and placement methods.",
 "key_points": [
  "Nanotubes are the strongest known material.",
  "Iijima revealed them (1991).",
  "Long pure placed tubes are hard.",
  "Manufacturing lagged the science.",
  "The promise is still unfulfilled.",
 ],
 "requirements": [
  "Controlled long pure growth.",
  "Placed nanotube architectures.",
  "Structural nanotube use.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Iijima S. Nanotubes. Various; 1991-2002.",
  "Baughman RH et al. Nanotube reviews. Various; 2002-2015.",
  "Zhang Q et al. Growth control. Various; 2017-2022.",
  "De Volder MFL et al. Applications. Various; 2013-2020.",
 ],
 "demo_data": {"a": ("nanotube fiber strength achieved, GPa (approx)", 5.0),
               "b": ("theoretical nanotube strength, GPa (approx)", 100.0), "bounds": (0.03, 0.08),
               "step1": "a twentieth of theoretical - the uncontrolled wonder",
               "confirm": "controlled nanotubes in structural use",
               "refute": "nanotubes prove unable to be controlled"},
},
# ------------------------------------------------------------------ rank 17
{
 "key": "graphene-applications",
 "name": "Graphene Applications: The Wonder Material's Wait",
 "group": "Materials",
 "ladder_rank": 17, "ladder_tier": "compounded",
 "problem": "Graphene won the Nobel - but where are the revolutionary applications?",
 "description": "Graphene applications - the wonder material's wait: the properties are miraculous; but the killer app is still debated; composites and inks are incremental; and the revolution is pending. Conductive inks and composite additives sell modestly; the revolutionary application - the one that justifies the Nobel hype - hasn't arrived.",
 "background": "Graphene (2004, Nobel 2010) was isolated; hype followed; but applications lagged. As of 2026 the revolution is still awaited.",
 "why_it_matters": "Realized graphene applications would justify the hype: the wonder material made useful.",
 "sig_pointer": "The Signature system's proposed approach finds graphene's killer apps, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that graphene needs application engineering: the properties matched to needs - with killer apps proven. "
  "Assumptions: (1) matches exist; (2) engineering works; (3) apps prove. "
  "Reasoning path: an applications model explains the wait and predicts graphene's uses. "
  "Proposed mechanism: 'application-engineered' graphene - matched killer apps. "
  "What would confirm it: revolutionary graphene products. "
  "What would kill it: evidence that graphene has no killer app. "
  "What this does not claim: it does not claim killer apps exist, offers no engineering advice, and does not constitute a materials recommendation."),
 "sig_lens": "The Signature lens reads graphene as application-waiting, and asks what matching would make revolutionary.",
 "how_it_works": "Researchers study graphene applications through composite development, ink formulation, and market analyses.",
 "key_points": [
  "Graphene won the 2010 Nobel.",
  "Properties are miraculous.",
  "The killer app is debated.",
  "Current uses are incremental.",
  "The revolution is pending.",
 ],
 "requirements": [
  "Property-need matching.",
  "Proven killer applications.",
  "Revolutionary graphene products.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Geim AK, Novoselov KS. Graphene. Various; 2004-2010.",
  "Nobel Prize in Physics. 2010.",
  "Novoselov KS et al. Application roadmaps. Various; 2012-2020.",
  "Ferrari AC et al. Graphene reviews. Various; 2015-2021.",
 ],
 "demo_data": {"a": ("revolutionary graphene products (approx)", 3.0),
               "b": ("graphene products launched (approx)", 100.0), "bounds": (0.015, 0.05),
               "step1": "three revolutionary of a hundred launched - the waiting wonder",
               "confirm": "revolutionary graphene products",
               "refute": "graphene proves to have no killer app"},
},
# ------------------------------------------------------------------ rank 18
{
 "key": "nano-energy",
 "name": "Nano-Energy: Harvesting at the Nanoscale",
 "group": "Devices",
 "ladder_rank": 18, "ladder_tier": "compounded",
 "problem": "Nanogenerators harvest ambient energy - but can they power anything useful?",
 "description": "Nano-energy - harvesting at the nanoscale: piezoelectric nanogenerators (Wang, 2006) promised self-powered devices; but the power is tiny; and useful applications are limited. Wang's nanogenerators work as physics; as power supplies they remain orders of magnitude short of what even the tiniest IoT sensor needs.",
 "background": "Nanogenerators (2006) launched the field; triboelectric versions followed; but power stayed small. As of 2026 nano-energy is still weak.",
 "why_it_matters": "Useful nano-energy would power the IoT: the ambient harvest made practical.",
 "sig_pointer": "The Signature system's proposed approach makes nano-energy useful, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that nano-energy needs power scaling: the harvested energy increased - with useful devices powered. "
  "Assumptions: (1) scaling is possible; (2) devices are powered; (3) applications follow. "
  "Reasoning path: a scaling model explains weak status and predicts useful harvesters. "
  "Proposed mechanism: 'power-scaled' nano-energy - useful ambient harvesting. "
  "What would confirm it: self-powered useful devices. "
  "What would kill it: evidence that nano-energy is inherently tiny. "
  "What this does not claim: it does not claim useful nano-energy exists, offers no engineering advice, and does not constitute a device recommendation."),
 "sig_lens": "The Signature lens reads nano-energy as tiny harvest, and asks what scaling would power.",
 "how_it_works": "Researchers study nano-energy through piezoelectric scaling, triboelectric research, and device integration.",
 "key_points": [
  "Nanogenerators harvest ambient energy.",
  "The power is tiny.",
  "Self-powered devices were promised.",
  "Useful applications are limited.",
  "Nano-energy is still weak.",
 ],
 "requirements": [
  "Scaled harvested power.",
  "Self-powered useful devices.",
  "Practical ambient harvesting.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Wang ZL et al. Nanogenerators. Various; 2006-2020.",
  "Fan FR et al. Triboelectric. Various; 2012-2018.",
  "Wang ZL et al. Reviews. Various; 2017-2023.",
  "Zi Y et al. Power analyses. Various; 2016-2021.",
 ],
 "demo_data": {"a": ("nanogenerator power, microwatts (approx)", 100.0),
               "b": ("IoT device power need, milliwatts (approx)", 10.0), "bounds": (5.0, 15.0),
               "step1": "a hundred microwatts against ten milliwatts needed - the weak harvest",
               "confirm": "self-powered useful devices",
               "refute": "nano-energy proves inherently tiny"},
},
# ------------------------------------------------------------------ rank 19
{
 "key": "nanoscale-heat",
 "name": "Heat at the Nanoscale",
 "group": "Theory",
 "ladder_rank": 19, "ladder_tier": "compounded",
 "problem": "Heat behaves strangely at the nanoscale - can thermal transport be understood and controlled?",
 "description": "Nanoscale heat - thermal transport puzzles: ballistic phonons, interface resistance, and size effects complicate; but understanding is incomplete; and thermal management needs the science. Chip hotspots already live in the ballistic-phonon regime, which makes this not an academic puzzle but a thermal wall the industry is hitting.",
 "background": "Nanoscale heat (1990s-2000s) revealed puzzles; phonon engineering emerged; but control lags. As of 2026 the science is still developing.",
 "why_it_matters": "Controlled nanoscale heat would transform electronics cooling: the thermal managed.",
 "sig_pointer": "The Signature system's proposed approach understands nanoscale heat, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that nanoscale heat needs transport theory: the phonon behaviors understood - with thermal designed. "
  "Assumptions: (1) theory is achievable; (2) it predicts; (3) design follows. "
  "Reasoning path: a theory model explains the puzzles and predicts thermal control. "
  "Proposed mechanism: 'theory-understood' nanoscale heat - designed thermal transport. "
  "What would confirm it: engineered nanoscale thermal devices. "
  "What would kill it: evidence that nanoscale heat resists understanding. "
  "What this does not claim: it does not claim understood nanoscale heat exists, offers no engineering advice, and does not constitute a device recommendation."),
 "sig_lens": "The Signature lens reads nanoscale heat as puzzling transport, and asks what theory would control.",
 "how_it_works": "Researchers study nanoscale heat through phonon research, interface studies, and thermal engineering.",
 "key_points": [
  "Ballistic phonons complicate transport.",
  "Interface resistance dominates.",
  "Understanding is incomplete.",
  "Thermal management needs the science.",
  "Control lags the puzzles.",
 ],
 "requirements": [
  "Understood phonon transport.",
  "Designed thermal materials.",
  "Engineered nanoscale thermal devices.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Cahill DG et al. Nanoscale heat. Various; 2003-2014.",
  "Maldovan M et al. Phonon engineering. Various; 2013-2019.",
  "Chen G et al. Thermal reviews. Various; 2005-2021.",
  "Pop E et al. Interface heat. Various; 2010-2018.",
 ],
 "demo_data": {"a": ("nanoscale thermal phenomena understood, percent (approx)", 40.0),
               "b": ("percent scale", 100.0), "bounds": (0.28, 0.52),
               "step1": "three in five phenomena puzzling - the unmanaged heat",
               "confirm": "engineered nanoscale thermal devices",
               "refute": "nanoscale heat proves to resist understanding"},
},
# ------------------------------------------------------------------ rank 20
{
 "key": "molecular-electronics",
 "name": "Molecular Electronics: The Single-Molecule Circuit",
 "group": "Devices",
 "ladder_rank": 20, "ladder_tier": "compounded",
 "problem": "Can single molecules be circuits - or is molecular electronics a beautiful dead end?",
 "description": "Molecular electronics - single-molecule circuits: Aviram-Ratner (1974) proposed; break junctions measured; but reproducibility is poor; and the field debates whether it's a path or a dead end. Break junctions measure single molecules beautifully and irreproducibly; until the same junction gives the same answer twice, there is no technology here.",
 "background": "Molecular electronics (1970s-2000s) promised circuits; measurements were made; but reproducibility failed. As of 2026 the field is still debated.",
 "why_it_matters": "Working molecular electronics would be the ultimate miniaturization: the circuit of molecules.",
 "sig_pointer": "The Signature system's proposed approach makes molecular electronics reproducible, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that molecular electronics needs reproducibility: the junctions made reliable - with circuits built. "
  "Assumptions: (1) reproducibility is achievable; (2) circuits are buildable; (3) the field revives. "
  "Reasoning path: a reproducibility model explains the dead-end debate and predicts molecular circuits. "
  "Proposed mechanism: 'reproducibly-built' molecular electronics - reliable junctions. "
  "What would confirm it: reproducible molecular circuits. "
  "What would kill it: evidence that molecular electronics is a dead end. "
  "What this does not claim: it does not claim molecular circuits exist, offers no engineering advice, and does not constitute a device recommendation."),
 "sig_lens": "The Signature lens reads molecular electronics as irreproducible promise, and asks what reliability would build.",
 "how_it_works": "Researchers study molecular electronics through break-junction research, reproducibility studies, and circuit attempts.",
 "key_points": [
  "Aviram-Ratner proposed (1974).",
  "Single molecules were measured.",
  "Reproducibility is poor.",
  "The field debates dead-end status.",
  "Ultimate miniaturization is the prize.",
 ],
 "requirements": [
  "Reproducible molecular junctions.",
  "Built molecular circuits.",
  "Revived molecular electronics.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Aviram A, Ratner MA. Molecular rectifiers. Various; 1974-1998.",
  "Reed MA et al. Break junctions. Various; 1997-2005.",
  "Tao NJ et al. Measurement reviews. Various; 2006-2015.",
  "Xiang D et al. Reproducibility. Various; 2016-2021.",
 ],
 "demo_data": {"a": ("molecular junctions reproducible, percent (approx)", 20.0),
               "b": ("percent scale", 100.0), "bounds": (0.12, 0.3),
               "step1": "four in five junctions irreproducible - the beautiful dead end",
               "confirm": "reproducible molecular circuits",
               "refute": "molecular electronics proves a dead end"},
},
# ------------------------------------------------------------------ rank 21
{
 "key": "nanoporous",
 "name": "Nanoporous Materials: The Designed Void",
 "group": "Materials",
 "ladder_rank": 21, "ladder_tier": "compounded",
 "problem": "Nanoporous materials filter and store - but can the pores be designed for each application?",
 "description": "Nanoporous materials - the designed void: MOFs, zeolites, and membranes promise selective filtration; but pore design is still partly empirical; and application-specific pores are the goal. Zeolites run the world's refineries on empirical pore design; MOFs promised rational design and have mostly delivered beautiful crystals instead.",
 "background": "Nanoporous materials (1990s-2000s) grew; MOFs (Yaghi, 1990s-2000s) expanded the space; but design lags. As of 2026 pores are still partly empirical.",
 "why_it_matters": "Designed pores would transform separation: the void made selective.",
 "sig_pointer": "The Signature system's proposed approach designs nanopores, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that pores need application design: the structures predicted for each separation - with materials made. "
  "Assumptions: (1) design is possible; (2) materials are makable; (3) separations transform. "
  "Reasoning path: a design model explains empirical status and predicts designed pores. "
  "Proposed mechanism: 'application-designed' nanopores - selective voids. "
  "What would confirm it: designed pores in industrial separations. "
  "What would kill it: evidence that pores resist design. "
  "What this does not claim: it does not claim designed pores exist, offers no engineering advice, and does not constitute a materials recommendation."),
 "sig_lens": "The Signature lens reads pores as empirical voids, and asks what design would make selective.",
 "how_it_works": "Researchers study nanoporous materials through MOF design, pore characterization, and separation testing.",
 "key_points": [
  "MOFs expanded the porous space.",
  "Pore design is partly empirical.",
  "Selective filtration is the promise.",
  "Application-specific pores are the goal.",
  "Zeolites are the industrial standard.",
 ],
 "requirements": [
  "Predicted application pores.",
  "Made designed materials.",
  "Industrial designed separations.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Yaghi OM et al. MOFs. Various; 1995-2015.",
  "Davis ME et al. Zeolites. Various; 2002-2015.",
  "Furukawa H et al. Porous reviews. Various; 2013-2020.",
  "Dechnik J et al. Membrane MOFs. Various; 2017-2022.",
 ],
 "demo_data": {"a": ("pores designed for applications, percent (approx)", 20.0),
               "b": ("percent scale", 100.0), "bounds": (0.12, 0.3),
               "step1": "four in five pores empirical - the undesigned void",
               "confirm": "designed pores in industrial separations",
               "refute": "pores prove to resist design"},
},
# ------------------------------------------------------------------ rank 22
{
 "key": "nanoscale-assembly",
 "name": "Directed Nanoscale Assembly",
 "group": "Fabrication",
 "ladder_rank": 22, "ladder_tier": "compounded",
 "problem": "Can nanoscale components be assembled into devices - directed, not random?",
 "description": "Directed nanoscale assembly - the assembly problem: self-assembly is random; pick-and-place is slow; and the directed assembly of nanocomponents into devices is the manufacturing bottleneck. The semiconductor industry places atoms with EUV; directed assembly of arbitrary nanocomponents at device scale has no equivalent tool.",
 "background": "Self-assembly (1990s-2000s) was random; directed methods (2010s) emerged; but device assembly lags. As of 2026 assembly is still the bottleneck.",
 "why_it_matters": "Directed assembly would manufacture nanodevices: the placement that builds.",
 "sig_pointer": "The Signature system's proposed approach directs nanoscale assembly, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that assembly needs direction: the fields, templates, and robotics that place nanocomponents - with devices built. "
  "Assumptions: (1) direction works; (2) placement is precise; (3) devices follow. "
  "Reasoning path: a direction model explains the bottleneck and predicts assembled nanodevices. "
  "Proposed mechanism: 'directedly-assembled' nanodevices - placed components. "
  "What would confirm it: directed-assembled nanodevices in products. "
  "What would kill it: evidence that nanoscale can't be directed. "
  "What this does not claim: it does not claim directed assembly exists at scale, offers no engineering advice, and does not constitute a manufacturing recommendation."),
 "sig_lens": "The Signature lens reads assembly as random-or-slow, and asks what direction would place.",
 "how_it_works": "Researchers study directed assembly through field-directed methods, template assembly, and nanorobotics.",
 "key_points": [
  "Self-assembly is random.",
  "Pick-and-place is slow.",
  "Directed methods are emerging.",
  "Assembly is the bottleneck.",
  "Device assembly lags.",
 ],
 "requirements": [
  "Precise directed placement.",
  "Assembled nanodevices.",
  "Products with directed assembly.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Whitesides GM et al. Self-assembly. Various; 1991-2005.",
  "Mastrangeli M et al. Directed assembly. Various; 2017-2022.",
  "Grzelczak M et al. Assembly reviews. Various; 2010-2019.",
  "Demers SME et al. Placement methods. Various; 2015-2021.",
 ],
 "demo_data": {"a": ("nanodevices assembled by directed methods (approx)", 10.0),
               "b": ("nanodevices assembled (approx)", 200.0), "bounds": (0.03, 0.08),
               "step1": "one in twenty directed - the random assembly",
               "confirm": "directed-assembled nanodevices in products",
               "refute": "nanoscale proves unable to be directed"},
},
# ------------------------------------------------------------------ rank 23
{
 "key": "nano-bio-interface",
 "name": "The Nano-Bio Interface",
 "group": "Safety",
 "ladder_rank": 23, "ladder_tier": "compounded",
 "problem": "Nanoparticles meet biology unpredictably - can the nano-bio interface be understood and designed?",
 "description": "The nano-bio interface - protein coronas, cellular uptake, and immune response: the interactions are complex; prediction is poor; and design is empirical. Understanding would enable safe nanomedicine. Every injected nanoparticle acquires a protein corona within seconds, becoming something the designer never made - and the field still can't predict what.",
 "background": "Nano-bio research (2000s-2010s) characterized coronas; but prediction lagged. As of 2026 the interface is still surprising.",
 "why_it_matters": "Understood nano-bio interfaces would make nanomedicine safe: the meeting designed.",
 "sig_pointer": "The Signature system's proposed approach understands the nano-bio interface, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that the interface needs predictive understanding: the corona and uptake modeled - with safe design. "
  "Assumptions: (1) understanding is achievable; (2) it predicts; (3) design follows. "
  "Reasoning path: an understanding model explains the surprises and predicts safe interfaces. "
  "Proposed mechanism: 'predictively-understood' nano-bio interfaces - designed meetings. "
  "What would confirm it: predicted nano-bio outcomes in trials. "
  "What would kill it: evidence that the interface resists understanding. "
  "What this does not claim: it makes no safety claims, offers no medical advice, and does not constitute a design recommendation."),
 "sig_lens": "The Signature lens reads the interface as surprising complexity, and asks what prediction would design.",
 "how_it_works": "Researchers study the nano-bio interface through corona characterization, uptake modeling, and immune studies.",
 "key_points": [
  "Protein coronas complicate interactions.",
  "Cellular uptake is unpredictable.",
  "Prediction is poor.",
  "Design is empirical.",
  "The interface still surprises.",
 ],
 "requirements": [
  "Predictive interface models.",
  "Designed safe interfaces.",
  "Predicted outcomes in trials.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Walkey CD et al. Protein corona. Various; 2012-2016.",
  "Monopoli MP et al. Corona reviews. Various; 2012-2020.",
  "Nel A et al. Nano-bio. Various; 2009-2016.",
  "Mahmoudi M et al. Interface reviews. Various; 2011-2020.",
 ],
 "demo_data": {"a": ("nano-bio outcomes predictable, percent (approx)", 30.0),
               "b": ("percent scale", 100.0), "bounds": (0.2, 0.42),
               "step1": "seven in ten surprising - the undesigned meeting",
               "confirm": "predicted nano-bio outcomes in trials",
               "refute": "the interface proves to resist understanding"},
},
# ------------------------------------------------------------------ rank 24
{
 "key": "nanolubrication",
 "name": "Nanolubrication: Friction at the Nanoscale",
 "group": "Theory",
 "ladder_rank": 24, "ladder_tier": "advanced",
 "problem": "Friction behaves strangely at the nanoscale - can it be understood and controlled?",
 "description": "Nanolubrication - friction at the nanoscale: superlubricity was observed; but the mechanisms are debated; and engineering applications are limited. Understanding would transform MEMS and machines. Superlubricity - friction coefficients near zero - has been observed repeatedly and explained never quite to everyone's satisfaction.",
 "background": "Nanotribology (1990s-2000s) revealed puzzles; superlubricity (2004) was observed; but control lags. As of 2026 the science is still developing.",
 "why_it_matters": "Controlled nanofriction would transform machines: the friction engineered.",
 "sig_pointer": "The Signature system's proposed approach understands nanofriction, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that nanofriction needs mechanism understanding: the superlubricity explained - with friction engineered. "
  "Assumptions: (1) mechanisms are learnable; (2) they are engineerable; (3) applications follow. "
  "Reasoning path: a mechanism model explains the puzzles and predicts controlled friction. "
  "Proposed mechanism: 'mechanism-understood' nanolubrication - engineered friction. "
  "What would confirm it: engineered superlubricity in devices. "
  "What would kill it: evidence that nanofriction resists understanding. "
  "What this does not claim: it does not claim understood nanofriction exists, offers no engineering advice, and does not constitute a device recommendation."),
 "sig_lens": "The Signature lens reads nanofriction as puzzling, and asks what mechanisms would control.",
 "how_it_works": "Researchers study nanolubrication through AFM friction, superlubricity research, and mechanism modeling.",
 "key_points": [
  "Superlubricity was observed.",
  "Mechanisms are debated.",
  "Engineering applications are limited.",
  "Understanding is incomplete.",
  "MEMS need the science.",
 ],
 "requirements": [
  "Understood friction mechanisms.",
  "Engineered superlubricity.",
  "Nanolubrication in devices.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Hirano M et al. Superlubricity. Various; 1991-2004.",
  "Müser MH et al. Friction theory. Various; 2003-2015.",
  "Berman D et al. Nanolubrication reviews. Various; 2014-2020.",
  "Carpick RW et al. Nanotribology. Various; 1997-2018.",
 ],
 "demo_data": {"a": ("friction mechanisms understood, percent (approx)", 40.0),
               "b": ("percent scale", 100.0), "bounds": (0.28, 0.52),
               "step1": "three in five mechanisms debated - the puzzling friction",
               "confirm": "engineered superlubricity in devices",
               "refute": "nanofriction proves to resist understanding"},
},
# ------------------------------------------------------------------ rank 25
{
 "key": "nano-standards",
 "name": "Nanometrology: Measuring the Nanoworld",
 "group": "Theory",
 "ladder_rank": 25, "ladder_tier": "advanced",
 "problem": "Can the nanoworld be measured with standards - or is every measurement bespoke?",
 "description": "Nanometrology - measuring the nanoworld: AFM and TEM measure; but traceability is hard; standards are few; and the field debates whether nanomeasurement can be standardized. NIST and ISO have been writing nano-standards for two decades; the instruments keep outrunning the standards.",
 "background": "Nanometrology (2000s) grew with the NNI; standards efforts (NIST, ISO) progressed; but gaps remain. As of 2026 measurement is still partly bespoke.",
 "why_it_matters": "Standardized nanomeasurement would enable nanomanufacturing: the ruler for the nanoworld.",
 "sig_pointer": "The Signature system's proposed approach standardizes nanomeasurement, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that nanometrology needs standards: the traceable measurements - with the field standardized. "
  "Assumptions: (1) standards are achievable; (2) they are adopted; (3) manufacturing follows. "
  "Reasoning path: a standards model explains bespoke status and predicts measured nanoworlds. "
  "Proposed mechanism: 'standardized' nanometrology - traceable measurement. "
  "What would confirm it: nanomanufacturing with standard metrology. "
  "What would kill it: evidence that nanomeasurement resists standardization. "
  "What this does not claim: it does not claim standardized nanometrology exists, offers no engineering advice, and does not constitute a standards recommendation."),
 "sig_lens": "The Signature lens reads nanomeasurement as bespoke, and asks what standards would measure.",
 "how_it_works": "Researchers study nanometrology through NIST/ISO standards, traceability research, and instrument development.",
 "key_points": [
  "AFM and TEM measure the nanoworld.",
  "Traceability is hard.",
  "Standards are few.",
  "Measurement is partly bespoke.",
  "Manufacturing needs the ruler.",
 ],
 "requirements": [
  "Traceable nanomeasurements.",
  "Adopted standards.",
  "Standard-metrology manufacturing.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "NIST nanometrology program. Various; 2000s onward.",
  "ISO nano-standards. Various; 2005 onward.",
  "Postek MT et al. Metrology reviews. Various; 2008-2018.",
  "Koenders L et al. Traceability. Various; 2013-2020.",
 ],
 "demo_data": {"a": ("nanomeasurements with standards, percent (approx)", 30.0),
               "b": ("percent scale", 100.0), "bounds": (0.2, 0.42),
               "step1": "seven in ten bespoke - the unruled nanoworld",
               "confirm": "nanomanufacturing with standard metrology",
               "refute": "nanomeasurement proves to resist standardization"},
},
# ------------------------------------------------------------------ rank 26
{
 "key": "nano-architectures",
 "name": "Nano-Architected Materials",
 "group": "Materials",
 "ladder_rank": 26, "ladder_tier": "advanced",
 "problem": "Architected nanolattices are strong and light - but can they be manufactured at scale?",
 "description": "Nano-architected materials - the strong and light: nanolattices achieve record strength-to-weight; but fabrication is slow and small; and the scale-up is the challenge. Greer's nanolattices are stronger per weight than anything else made; they're also made one tiny lattice at a time.",
 "background": "Nano-architected materials (2010s, Greer, Bauer) were demonstrated; but manufacturing lagged. As of 2026 they are still lab-scale.",
 "why_it_matters": "Scaled nano-architectures would transform structures: the strongest lightest materials made real.",
 "sig_pointer": "The Signature system's proposed approach scales nano-architected materials, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that nano-architectures need scaled fabrication: the lattices built at scale - with properties retained. "
  "Assumptions: (1) fabrication scales; (2) properties retain; (3) structures follow. "
  "Reasoning path: a fabrication model explains lab status and predicts scaled architectures. "
  "Proposed mechanism: 'fabrication-scaled' nano-architectures - built lattices. "
  "What would confirm it: nano-architected structures in use. "
  "What would kill it: evidence that architectures can't scale. "
  "What this does not claim: it does not claim scaled architectures exist, offers no engineering advice, and does not constitute a materials recommendation."),
 "sig_lens": "The Signature lens reads nanolattices as lab-scale strength, and asks what fabrication would scale.",
 "how_it_works": "Researchers study nano-architectures through two-photon fabrication, scale-up research, and property testing.",
 "key_points": [
  "Nanolattices are record strong-to-weight.",
  "Fabrication is slow and small.",
  "Scale-up is the challenge.",
  "Properties are extraordinary.",
  "They are still lab-scale.",
 ],
 "requirements": [
  "Scaled lattice fabrication.",
  "Retained extraordinary properties.",
  "Nano-architected structures in use.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Greer JR et al. Nanolattices. Various; 2014-2020.",
  "Bauer J et al. Architected materials. Various; 2017-2022.",
  "Meza LR et al. Strength studies. Various; 2014-2018.",
  "Montemayor LC et al. Fabrication. Various; 2014-2019.",
 ],
 "demo_data": {"a": ("nano-architected parts at scale (approx)", 2.0),
               "b": ("architected designs published (approx)", 100.0), "bounds": (0.01, 0.035),
               "step1": "two scaled of a hundred designed - the lab-scale strength",
               "confirm": "nano-architected structures in use",
               "refute": "architectures prove unable to scale"},
},
# ------------------------------------------------------------------ rank 27
{
 "key": "nano-environment",
 "name": "Nanomaterials in the Environment",
 "group": "Safety",
 "ladder_rank": 27, "ladder_tier": "advanced",
 "problem": "Nanomaterials enter the environment - but their fate and effects are poorly understood. What happens?",
 "description": "Environmental nanotechnology - the fate question: nanoparticles are released; but transport, transformation, and ecosystem effects are incompletely studied; and the field is still characterizing. Silver nanoparticles from consumer products already flow through wastewater; the field is still arguing about what they become downstream.",
 "background": "Environmental nano research (2000s-2010s) began; but the evidence base is thin. As of 2026 the fate is still being mapped.",
 "why_it_matters": "Understood environmental fate would enable safe nanotech: the nanoworld's footprint known.",
 "sig_pointer": "The Signature system's proposed approach maps nanomaterial environmental fate, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that environmental fate needs mapping: the transport and transformation studied - with effects assessed. "
  "Assumptions: (1) mapping is feasible; (2) it completes; (3) assessment follows. "
  "Reasoning path: a mapping model explains the evidence gap and predicts known footprints. "
  "Proposed mechanism: 'fate-mapped' environmental nanotech - studied footprints. "
  "What would confirm it: comprehensive environmental assessments. "
  "What would kill it: evidence that fate can't be mapped. "
  "What this does not claim: it makes no safety claims, offers no environmental advice, and does not constitute a regulatory recommendation."),
 "sig_lens": "The Signature lens reads environmental nano as unmapped fate, and asks what studies would map.",
 "how_it_works": "Researchers study environmental nano through fate-and-transport research, ecosystem studies, and monitoring.",
 "key_points": [
  "Nanoparticles are released.",
  "Transport and transformation are understudied.",
  "Ecosystem effects are incompletely known.",
  "The evidence base is thin.",
  "The fate is still being mapped.",
 ],
 "requirements": [
  "Mapped environmental fate.",
  "Assessed ecosystem effects.",
  "Comprehensive assessments.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Klaine SJ et al. Environmental nano. Various; 2008-2016.",
  "Lowry GV et al. Fate reviews. Various; 2012-2020.",
  "Petersen EJ et al. Ecosystem studies. Various; 2015-2021.",
  "Gottschalk F et al. Release modeling. Various; 2009-2015.",
 ],
 "demo_data": {"a": ("nanomaterials with fate data, percent (approx)", 20.0),
               "b": ("percent scale", 100.0), "bounds": (0.12, 0.3),
               "step1": "four in five unmapped - the unknown footprint",
               "confirm": "comprehensive environmental assessments",
               "refute": "fate proves unable to be mapped"},
},
# ------------------------------------------------------------------ rank 28
{
 "key": "nano-quantum",
 "name": "Nanoscale Quantum Devices",
 "group": "Devices",
 "ladder_rank": 28, "ladder_tier": "advanced",
 "problem": "Quantum effects dominate at the nanoscale - can they be engineered into devices?",
 "description": "Nanoscale quantum devices - the quantum engineered: single-electron transistors, quantum dots, and spin qubits exploit quantum effects; but coherence is fragile; and the devices are still mostly physics.",
 "background": "Quantum devices (1990s-2000s) were demonstrated; spin qubits (2010s-2020s) advanced; but engineering lags. As of 2026 quantum devices are still physics-rich.",
 "why_it_matters": "Engineered quantum devices would transform computing and sensing: the quantum made practical.",
 "sig_pointer": "The Signature system's proposed approach engineers nanoscale quantum devices, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that quantum devices need coherence engineering: the fragile states protected - with devices practical. "
  "Assumptions: (1) coherence is protectable; (2) devices are engineerable; (3) applications follow. "
  "Reasoning path: a coherence model explains physics-status and predicts quantum devices. "
  "Proposed mechanism: 'coherence-engineered' quantum devices - protected states. "
  "What would confirm it: practical nanoscale quantum devices. "
  "What would kill it: evidence that coherence can't be engineered. "
  "What this does not claim: it does not claim practical quantum devices exist, offers no engineering advice, and does not constitute a device recommendation."),
 "sig_lens": "The Signature lens reads quantum devices as fragile physics, and asks what engineering would protect.",
 "how_it_works": "Researchers study quantum devices through coherence research, qubit development, and device engineering.",
 "key_points": [
  "Quantum effects dominate at the nanoscale.",
  "Coherence is fragile.",
  "Single-electron devices were demonstrated.",
  "Spin qubits advanced.",
  "Devices are still mostly physics.",
 ],
 "requirements": [
  "Protected quantum coherence.",
  "Engineered practical devices.",
  "Quantum devices in applications.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Kastner MA et al. Single-electron devices. Various; 1992-2000.",
  "Hanson R et al. Spin qubits. Various; 2007-2015.",
  "Awschalom DD et al. Quantum reviews. Various; 2013-2021.",
  "Burkard G et al. Coherence research. Various; 2023-2024.",
 ],
 "demo_data": {"a": ("quantum devices in applications (approx)", 5.0),
               "b": ("quantum device concepts (approx)", 200.0), "bounds": (0.015, 0.04),
               "step1": "five applied of two hundred conceived - the fragile quantum",
               "confirm": "practical nanoscale quantum devices",
               "refute": "coherence proves unable to be engineered"},
},
# ------------------------------------------------------------------ rank 29
{
 "key": "nano-theory",
 "name": "A Theory of the Nanoscale",
 "group": "Theory",
 "ladder_rank": 29, "ladder_tier": "advanced",
 "problem": "Nanoscience is fragmented - can there be a unified theory of the nanoscale?",
 "description": "Nanoscale theory - the unified question: quantum, classical, and statistical descriptions meet at the nanoscale; but no unified framework connects them; the field is still piecemeal. The nanoscale is where quantum mechanics, classical mechanics, and statistical mechanics all claim jurisdiction and none fully rules.",
 "background": "Nanoscale theory (1990s-2000s) was piecemeal; multiscale methods helped; but unification is absent. As of 2026 the nanoscale is still theoretically fragmented.",
 "why_it_matters": "Unified nanoscale theory would predict everything: the equation of the small.",
 "sig_pointer": "The Signature system's proposed approach unifies nanoscale theory, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that nanoscale theory unifies through multiscale frameworks: the quantum-classical-statistical connected - with predictions. "
  "Assumptions: (1) connection is possible; (2) it predicts; (3) theory unifies. "
  "Reasoning path: a multiscale model explains fragmentation and predicts unified theory. "
  "Proposed mechanism: 'multiscale-unified' nanoscale theory - connected prediction. "
  "What would confirm it: unified predictions across nanoscale phenomena. "
  "What would kill it: evidence that the nanoscale resists unification. "
  "What this does not claim: it does not claim a unified theory exists, offers no engineering advice, and does not constitute a theoretical claim."),
 "sig_lens": "The Signature lens reads the nanoscale as theoretically fragmented, and asks what multiscale would unify.",
 "how_it_works": "Researchers study nanoscale theory through multiscale modeling, quantum-classical methods, and theory development.",
 "key_points": [
  "Quantum, classical, statistical meet at the nanoscale.",
  "No unified framework exists.",
  "Multiscale methods help partially.",
  "The field is piecemeal.",
  "Unification is absent.",
 ],
 "requirements": [
  "Connected multiscale frameworks.",
  "Unified cross-phenomena predictions.",
  "Accepted unified theory.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Ratner M et al. Nanoscale theory. Various; 2003-2015.",
  "Schatz GC et al. Multiscale methods. Various; 2005-2018.",
  "Fermi-level reviews. Various.",
  "Lindsay SM et al. Theory perspectives. Various; 2010-2020.",
 ],
 "demo_data": {"a": ("nanoscale phenomena with unified theory (approx)", 10.0),
               "b": ("nanoscale phenomena (approx)", 100.0), "bounds": (0.05, 0.18),
               "step1": "nine in ten ununified - the fragmented small",
               "confirm": "unified predictions across nanoscale phenomena",
               "refute": "the nanoscale proves to resist unification"},
},
# ------------------------------------------------------------------ rank 30
{
 "key": "nano-future",
 "name": "The Future of Nanotechnology: A Century Ahead",
 "group": "Theory",
 "ladder_rank": 30, "ladder_tier": "advanced",
 "problem": "What will nanotechnology become? The field extrapolates poorly - can its future be foreseen?",
 "description": "Nanotechnology futurology - predicting the field's century - is speculative: past predictions (nanobots by 2020) failed; but structured foresight is absent; whether futures work improves decisions is the meta-question.",
 "background": "Nano predictions have a poor record; scenario methods are unused. As of 2026 the future is debated without discipline.",
 "why_it_matters": "Long-horizon decisions (research, safety) need foresight: the discipline of nano futures.",
 "sig_pointer": "The Signature system's proposed approach builds disciplined nano foresight, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that nano futures need disciplined foresight: the scenario methods and roadmaps - with track records. "
  "Assumptions: (1) foresight is improvable; (2) methods exist; (3) they guide decisions. "
  "Reasoning path: a foresight model explains prediction failures and predicts better futures work. "
  "Proposed mechanism: 'disciplined' nano foresight - tracked scenario methods. "
  "What would confirm it: foresight with validated track records. "
  "What would kill it: evidence that nano futures are unforeseeable. "
  "What this does not claim: it does not claim any future, offers no engineering advice, and does not constitute a prediction."),
 "sig_lens": "The Signature lens reads nano futures as undisciplined speculation, and asks what methods would foresee.",
 "how_it_works": "Researchers study nano futures through scenario methods, technology roadmapping, and prediction tracking.",
 "key_points": [
  "Nano predictions have a poor record.",
  "Nanobots were promised by 2020.",
  "Scenario methods are unused.",
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
  "Roco MC et al. Nano roadmaps. Various; 2000-2020.",
  "Foresight methodology literature. Various.",
  "NNI strategic plans. Various.",
  "Berube DM et al. Nano futures. Various; 2006-2015.",
 ],
 "demo_data": {"a": ("nano predictions with validated track records (approx)", 5.0),
               "b": ("nano predictions made (approx)", 200.0), "bounds": (0.015, 0.04),
               "step1": "five tracked of two hundred made - the foresight without a record",
               "confirm": "foresight with validated track records",
               "refute": "nano futures prove unforeseeable"},
},
# ------------------------------------------------------------------ rank 31
{
 "key": "grey-goo",
 "name": "The Grey-Goo Question",
 "group": "Safety",
 "ladder_rank": 31, "ladder_tier": "advanced",
 "problem": "Could self-replicating nanobots consume the world - or is grey goo a myth?",
 "description": "The grey-goo question - Drexler's warning (1986): self-replicating assemblers could run amok; but most experts consider it implausible; and the debate is more philosophical than technical. The debate peaked in the early 2000s and ended with most experts filing goo under implausible; the culture never got the memo.",
 "background": "Drexler (1986) raised the concern; the debate (2000s) largely dismissed it; but the question persists culturally. As of 2026 grey goo is considered implausible.",
 "why_it_matters": "Settling grey goo would clarify nanotech risk: the myth addressed.",
 "sig_pointer": "The Signature system's proposed approach settles the grey-goo question, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that grey goo needs risk analysis: the replication scenarios assessed - with the myth addressed. "
  "Assumptions: (1) scenarios are assessable; (2) analysis convinces; (3) the debate settles. "
  "Reasoning path: a risk model explains the persistence and predicts settled goo. "
  "Proposed mechanism: 'risk-assessed' grey goo - analyzed scenarios. "
  "What would confirm it: accepted risk assessments. "
  "What would kill it: evidence that goo is plausible. "
  "What this does not claim: it makes no safety claims, offers no safety advice, and does not constitute a risk assessment."),
 "sig_lens": "The Signature lens reads grey goo as cultural myth, and asks what analysis would settle.",
 "how_it_works": "Researchers study grey goo through replication analyses, risk literature, and expert surveys.",
 "key_points": [
  "Drexler raised the concern (1986).",
  "Most experts consider it implausible.",
  "The debate is philosophical.",
  "The question persists culturally.",
  "No replicators exist.",
 ],
 "requirements": [
  "Assessed replication scenarios.",
  "Accepted risk analyses.",
  "Settled public debate.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Drexler KE. Engines of Creation. 1986.",
  "Phoenix C et al. Goo analyses. Various; 2003-2008.",
  "Seeman NC et al. Expert views. Various; 2004-2015.",
  "Umbrello S et al. Risk ethics. Various; 2021-2024.",
 ],
 "demo_data": {"a": ("experts considering goo plausible, percent (approx)", 10.0),
               "b": ("percent scale", 100.0), "bounds": (0.05, 0.18),
               "step1": "nine in ten dismiss it - the implausible myth",
               "confirm": "accepted risk assessments",
               "refute": "goo proves plausible"},
},
# ------------------------------------------------------------------ rank 32
{
 "key": "nano-consciousness",
 "name": "Nanotechnology and Mind",
 "group": "Theory",
 "ladder_rank": 32, "ladder_tier": "advanced",
 "problem": "Could nanotechnology interface with the mind - and should it?",
 "description": "Nano-neural interfaces - the mind question: nanoparticles and nanodevices could interface with neurons; but the science is early; and the ethics are unaddressed. Tian's silicon-nanowire neural interfaces showed the hardware path; the ethics conversation hasn't started in earnest.",
 "background": "Neural interfaces (2000s-2010s) were micro-scale; nano interfaces (2010s-2020s) are emerging; but the field is early. As of 2026 the mind is still micro-interfaced.",
 "why_it_matters": "Nano-mind interfaces would transform neuroscience: the brain at the nanoscale.",
 "sig_pointer": "The Signature system's proposed approach addresses nano-neural interfaces, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that nano-neural interfaces need careful science: the devices developed - with ethics addressed. "
  "Assumptions: (1) science is achievable; (2) ethics are addressable; (3) the field proceeds. "
  "Reasoning path: a careful model explains early status and predicts addressed interfaces. "
  "Proposed mechanism: 'carefully-developed' nano-neural interfaces - ethical science. "
  "What would confirm it: working nano-neural interfaces with ethical frameworks. "
  "What would kill it: evidence that nano-neural is impossible or unacceptable. "
  "What this does not claim: it takes no ethical positions, offers no medical advice, and does not constitute a research recommendation."),
 "sig_lens": "The Signature lens reads nano-mind as unaddressed frontier, and asks what care would develop.",
 "how_it_works": "Researchers study nano-neural interfaces through device research, ethics literature, and neuroscience collaboration.",
 "key_points": [
  "Nano interfaces could reach neurons.",
  "The science is early.",
  "Ethics are unaddressed.",
  "Neural interfaces are micro-scale.",
  "The frontier is unaddressed.",
 ],
 "requirements": [
  "Working nano-neural devices.",
  "Addressed ethical frameworks.",
  "Careful scientific development.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Tian B et al. Nano-neural. Various; 2015-2022.",
  "Parameswaran N et al. Interfaces. Various; 2018-2023.",
  "Neuroethics literature. Various; 2018-2024.",
  "Spira ME et al. Neural nano. Various; 2016-2021.",
 ],
 "demo_data": {"a": ("nano-neural interfaces in use (approx)", 1.0),
               "b": ("neural interfaces in use (approx)", 50.0), "bounds": (0.01, 0.035),
               "step1": "one nano of fifty neural - the unaddressed frontier",
               "confirm": "working nano-neural interfaces with ethical frameworks",
               "refute": "nano-neural proves impossible or unacceptable"},
},
# ------------------------------------------------------------------ rank 33
{
 "key": "nanotech-governance",
 "name": "Governing Nanotechnology",
 "group": "Safety",
 "ladder_rank": 33, "ladder_tier": "advanced",
 "problem": "Nanotechnology outruns governance - can it be governed wisely?",
 "description": "Nanotech governance - the outrun question: the technology advances; regulation lags; and the field debates whether governance can be wise rather than reactive. The NNI's ELSI program was supposed to keep governance apace; two decades on, the technology still laps the rules.",
 "background": "Nano governance (2000s-2010s) was reactive; the NNI included ELSI; but gaps persist. As of 2026 governance still lags.",
 "why_it_matters": "Wise governance would guide nanotech safely: the rules that work.",
 "sig_pointer": "The Signature system's proposed approach governs nanotechnology wisely, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that nanotech needs anticipatory governance: the rules developed ahead - with wisdom. "
  "Assumptions: (1) anticipation is possible; (2) rules work; (3) wisdom guides. "
  "Reasoning path: a governance model explains reactive status and predicts wise rules. "
  "Proposed mechanism: 'anticipatorily-governed' nanotech - ahead rules. "
  "What would confirm it: governance guiding nanotech safely. "
  "What would kill it: evidence that governance can't anticipate. "
  "What this does not claim: it takes no policy positions, offers no regulatory advice, and does not constitute a governance recommendation."),
 "sig_lens": "The Signature lens reads nano governance as reactive lag, and asks what anticipation would rule.",
 "how_it_works": "Researchers study nano governance through policy research, ELSI studies, and regulatory analyses.",
 "key_points": [
  "Technology outruns regulation.",
  "Governance is reactive.",
  "ELSI was included in the NNI.",
  "Gaps persist.",
  "Wisdom is the goal.",
 ],
 "requirements": [
  "Anticipatory governance frameworks.",
  "Rules guiding safely.",
  "Wise nanotech governance.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "NNI ELSI program. Various; 2000 onward.",
  "Roco MC et al. Governance. Various; 2005-2015.",
  "Kuzma J et al. Regulatory reviews. Various; 2016-2022.",
  "Marchant GE et al. Anticipatory governance. Various; 2011-2020.",
 ],
 "demo_data": {"a": ("nano-governance frameworks anticipatory, percent (approx)", 20.0),
               "b": ("percent scale", 100.0), "bounds": (0.12, 0.3),
               "step1": "four in five reactive - the outrun rules",
               "confirm": "governance guides nanotech safely",
               "refute": "governance proves unable to anticipate"},
},
# ------------------------------------------------------------------ rank 34
{
 "key": "nano-singularity",
 "name": "The Nanotech Singularity",
 "group": "Theory",
 "ladder_rank": 34, "ladder_tier": "advanced",
 "problem": "Could nanotechnology trigger a singularity - abundance or catastrophe?",
 "description": "The nanotech singularity - Drexler's vision: molecular manufacturing could create abundance or catastrophe; but the singularity is speculative; and the field debates whether to take it seriously. Drexler's Radical Abundance (2013) restated the case; the mainstream field politely declined to engage.",
 "background": "Drexler (1986, 2013) envisioned the singularity; the debate (2000s) was heated; but the field moved on. As of 2026 the singularity is still speculative.",
 "why_it_matters": "The singularity question shapes nanotech's ambitions: the future taken seriously.",
 "sig_pointer": "The Signature system's proposed approach addresses the nanotech singularity, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that the singularity needs serious analysis: the scenarios assessed - with the field deciding. "
  "Assumptions: (1) analysis is possible; (2) it informs; (3) the field decides. "
  "Reasoning path: an analysis model explains the speculation and predicts addressed futures. "
  "Proposed mechanism: 'seriously-analyzed' nano futures - assessed scenarios. "
  "What would confirm it: accepted singularity analyses. "
  "What would kill it: evidence that the singularity is incoherent. "
  "What this does not claim: it does not claim any singularity, offers no engineering advice, and does not constitute a prediction."),
 "sig_lens": "The Signature lens reads the singularity as unserious speculation, and asks what analysis would address.",
 "how_it_works": "Researchers study the nano singularity through scenario analyses, Drexler's later work, and futures literature.",
 "key_points": [
  "Drexler envisioned abundance or catastrophe.",
  "The singularity is speculative.",
  "The field debates seriousness.",
  "Molecular manufacturing is the trigger.",
  "The question shapes ambitions.",
 ],
 "requirements": [
  "Serious scenario analyses.",
  "Accepted singularity assessments.",
  "Informed field decisions.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Drexler KE. Radical Abundance. 2013.",
  "Phoenix C et al. Singularity analyses. Various; 2003-2010.",
  "Kurzweil R et al. Singularity literature. Various; 2005-2024.",
  "Umbrello S et al. Nano futures ethics. Various; 2021-2024.",
 ],
 "demo_data": {"a": ("serious nano-singularity analyses (approx)", 10.0),
               "b": ("nano futures papers (approx)", 500.0), "bounds": (0.01, 0.035),
               "step1": "ten serious of five hundred speculative - the unaddressed singularity",
               "confirm": "accepted singularity analyses",
               "refute": "the singularity proves incoherent"},
},
]
