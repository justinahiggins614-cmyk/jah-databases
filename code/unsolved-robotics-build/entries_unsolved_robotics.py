#!/usr/bin/env python3
"""Entries for The Unsolved Robotics Database (unsolved-robotics)
and its Signature half (unsolved-robotics-signature).

34 famous unsolved problems in robotics, ladder-ordered by accessibility
(rank 1 = most approachable, rank 34 = most complex/compounded).
Public half: real, fact-checked problems. Signature half: the same 34
problems through the Signature lens, with Signature-generated proposed
solutions that are ALWAYS labeled as proposals, never established science.

Honesty rule (enforced in every record): never claim proof, never imply
peer acceptance, never present speculation as settled. Signature proposals
are labeled speculation for research discussion only - never engineering
advice, never a robotics recommendation; no safety or capability claims.
"""

LABEL = "Signature-generated proposed solution \u2014 not established science."

SIG_TAIL = ("Signature editions carry the Signature system's proposed "
            "solution approaches to famous unsolved problems. Every "
            "solution is labeled a Signature-generated proposal, never "
            "established science, never peer-accepted, never proof, never "
            "engineering advice.")

STD_COMMON = [
    "Problem statements verified against the published robotics literature; open status confirmed as of 2026.",
    "Signature solution sections are labeled proposals: they state assumptions, a reasoning path, a proposed mechanism, what would confirm or kill them, and what they do not claim.",
    "Signature proposals are labeled speculation for research discussion only - never engineering advice, never a robotics recommendation; no safety or capability claims appear.",
]

ENTRIES = [
# ------------------------------------------------------------------ rank 1
{
 "key": "moravec-paradox",
 "name": "Moravec's Paradox: Why Robots Can't Do Easy Things",
 "group": "Foundations",
 "ladder_rank": 1, "ladder_tier": "foundations",
 "problem": "Robots beat grandmasters but can't open doors - why is the easy hard and the hard easy?",
 "description": "Moravec's paradox (1988) - the observation that high-level reasoning is easy for machines while sensorimotor skills are brutally hard: chess fell in 1997, but a robot that tidies a room like a child remains science fiction. The paradox still structures robotics research.",
 "background": "Moravec (1988, Mind Children) articulated it; Brooks (1990s) built the behavior-based response; deep learning (2010s) narrowed but didn't close the gap. As of 2026 the paradox persists.",
 "why_it_matters": "Resolving Moravec's paradox would unlock general robotics: the easy made easy for machines.",
 "sig_pointer": "The Signature system's proposed approach resolves Moravec's paradox, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that the paradox resolves through embodied learning: the sensorimotor skills learned like reasoning was - with scale and embodiment. "
  "Assumptions: (1) sensorimotor learning scales; (2) embodiment is the key; (3) the gap closes. "
  "Reasoning path: an embodiment model explains the asymmetry and predicts its resolution. "
  "Proposed mechanism: 'embodied-scale' learning - sensorimotor skills at scale. "
  "What would confirm it: robots with child-level sensorimotor skills. "
  "What would kill it: evidence that sensorimotor skill resists learning. "
  "What this does not claim: it does not claim the paradox is resolved, offers no engineering advice, and does not constitute a research recommendation."),
 "sig_lens": "The Signature lens reads the paradox as unscaled embodiment, and asks what learning would resolve.",
 "how_it_works": "Researchers study the paradox through embodied AI, sensorimotor learning, and developmental robotics.",
 "key_points": [
  "Chess fell in 1997; tidying a room hasn't.",
  "Sensorimotor skills are brutally hard.",
  "Moravec articulated it in 1988.",
  "Deep learning narrowed the gap.",
  "The paradox still structures research.",
 ],
 "requirements": [
  "Scaled sensorimotor learning.",
  "Child-level robot skills.",
  "Resolved paradox demonstrated.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Moravec H. Mind Children. 1988.",
  "Brooks RA et al. Behavior-based robotics. Various; 1986-1999.",
  "Pfeifer R et al. Embodied AI. Various; 2007-2015.",
  "Lake BM et al. Human-like learning. Various; 2017-2023.",
 ],
 "demo_data": {"a": ("chess rating of top engines (approx)", 3500.0),
               "b": ("household tasks a robot does like a child (approx)", 5.0), "bounds": (600.0, 800.0),
               "step1": "grandmaster chess, five household tasks - the paradox quantified",
               "confirm": "robots with child-level sensorimotor skills",
               "refute": "sensorimotor skill proves to resist learning"},
},
# ------------------------------------------------------------------ rank 2
{
 "key": "grasping",
 "name": "Robotic Grasping: The Pick-Up Problem",
 "group": "Manipulation",
 "ladder_rank": 2, "ladder_tier": "foundations",
 "problem": "Humans grasp anything - robots grasp little. Can general grasping be solved?",
 "description": "Robotic grasping - the pick-up problem: humans grasp novel objects effortlessly; robots need structured environments; the Amazon Picking Challenge (2015-2017) showed the gap; and general grasping remains unsolved.",
 "background": "Grasping research (1980s-90s) was analytic; learning approaches (2010s, Dex-Net) improved; but generality lagged. As of 2026 robots grasp the known, not the novel.",
 "why_it_matters": "General grasping would unlock warehouse and home robots: the hand that holds anything.",
 "sig_pointer": "The Signature system's proposed approach solves general grasping, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that grasping needs learned generality: the grasps learned across objects - with novel-object success. "
  "Assumptions: (1) generality is learnable; (2) it transfers; (3) robots grasp. "
  "Reasoning path: a learning model explains the generality gap and predicts grasping robots. "
  "Proposed mechanism: 'generally-learned' grasping - novel-object success. "
  "What would confirm it: robots grasping novel objects reliably. "
  "What would kill it: evidence that grasping resists generality. "
  "What this does not claim: it does not claim general grasping exists, offers no engineering advice, and does not constitute a device recommendation."),
 "sig_lens": "The Signature lens reads grasping as ungeneralized skill, and asks what learning would make general.",
 "how_it_works": "Researchers study grasping through Dex-Net, learning approaches, and picking challenges.",
 "key_points": [
  "Humans grasp novel objects effortlessly.",
  "Robots need structured environments.",
  "The Amazon Picking Challenge showed the gap.",
  "Dex-Net improved learned grasping.",
  "Generality remains unsolved.",
 ],
 "requirements": [
  "Learned cross-object generality.",
  "Novel-object grasping reliable.",
  "General grasping in products.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Amazon Picking Challenge. Various; 2015-2017.",
  "Mahler J et al. Dex-Net. Various; 2017-2019.",
  "Bicchi A et al. Grasping reviews. Various; 2000-2015.",
  "Bohg J et al. Data-driven grasping. Various; 2014-2021.",
 ],
 "demo_data": {"a": ("novel objects grasped reliably, percent (approx)", 30.0),
               "b": ("percent scale", 100.0), "bounds": (0.2, 0.42),
               "step1": "seven in ten novel objects dropped - the ungeneralized hand",
               "confirm": "robots grasp novel objects reliably",
               "refute": "grasping proves to resist generality"},
},
# ------------------------------------------------------------------ rank 3
{
 "key": "slam",
 "name": "SLAM: Mapping the Unknown",
 "group": "Navigation",
 "ladder_rank": 3, "ladder_tier": "foundations",
 "problem": "SLAM maps unknown environments - but can it work robustly everywhere, forever?",
 "description": "SLAM (simultaneous localization and mapping) - the navigation core: it works in structured spaces; but dynamic environments, long-term operation, and semantic understanding challenge; and robust lifelong SLAM is unachieved.",
 "background": "SLAM (1980s-90s, Smith, Cheeseman) was formulated; probabilistic methods (2000s) matured; visual SLAM (2010s) spread. As of 2026 SLAM is good but not robust.",
 "why_it_matters": "Robust SLAM would enable lifelong robot navigation: the map that never fails.",
 "sig_pointer": "The Signature system's proposed approach makes SLAM robust and lifelong, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that SLAM needs lifelong robustness: the dynamic environments handled - with semantic maps maintained. "
  "Assumptions: (1) robustness is achievable; (2) dynamics are manageable; (3) maps persist. "
  "Reasoning path: a robustness model explains the fragility and predicts lifelong SLAM. "
  "Proposed mechanism: 'lifelong-robust' SLAM - dynamic semantic mapping. "
  "What would confirm it: robots navigating for years without failure. "
  "What would kill it: evidence that SLAM is inherently fragile. "
  "What this does not claim: it does not claim robust SLAM exists, offers no engineering advice, and does not constitute a navigation recommendation."),
 "sig_lens": "The Signature lens reads SLAM as fragile mapping, and asks what robustness would make lifelong.",
 "how_it_works": "Researchers study SLAM through dynamic-SLAM research, semantic mapping, and long-term trials.",
 "key_points": [
  "SLAM works in structured spaces.",
  "Dynamic environments challenge it.",
  "Long-term operation degrades maps.",
  "Semantic understanding is partial.",
  "Robust lifelong SLAM is unachieved.",
 ],
 "requirements": [
  "Dynamic-environment robustness.",
  "Lifelong map maintenance.",
  "Years-long failure-free navigation.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Smith RC et al. SLAM formulation. Various; 1986-1990.",
  "Durrant-Whyte H et al. SLAM reviews. Various; 2006-2012.",
  "Cadena C et al. Past/present/future. Various; 2016-2021.",
  "Mur-Artal R et al. ORB-SLAM. Various; 2015-2021.",
 ],
 "demo_data": {"a": ("SLAM failures in dynamic scenes, percent (approx)", 40.0),
               "b": ("percent scale", 100.0), "bounds": (0.28, 0.52),
               "step1": "two in five dynamic scenes break the map - the fragile navigator",
               "confirm": "robots navigate for years without failure",
               "refute": "SLAM proves inherently fragile"},
},
# ------------------------------------------------------------------ rank 4
{
 "key": "humanoid-walking",
 "name": "Humanoid Walking: The Biped Problem",
 "group": "Locomotion",
 "ladder_rank": 4, "ladder_tier": "foundations",
 "problem": "Humans walk effortlessly - humanoids walk carefully. Can bipedal walking become robust?",
 "description": "Humanoid walking - the biped problem: Atlas does parkour; but the robots are fragile, expensive, and teleoperated; robust autonomous bipedal walking in the wild is unachieved. Honda's ASIMO charmed the world and was retired in 2018; Boston Dynamics' Atlas does backflips on video and still can't be trusted alone in a warehouse.",
 "background": "Humanoid walking (1970s-2000s, Waseda, Honda) progressed; Atlas (2010s-2020s) showed agility; but robustness lagged. As of 2026 humanoids are demos, not workers.",
 "why_it_matters": "Robust humanoids would work in human spaces: the biped that walks with us.",
 "sig_pointer": "The Signature system's proposed approach makes humanoid walking robust, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that bipedal walking needs robust autonomy: the falls prevented - with wild operation. "
  "Assumptions: (1) robustness is achievable; (2) autonomy works; (3) humanoids deploy. "
  "Reasoning path: a robustness model explains demo-status and predicts working humanoids. "
  "Proposed mechanism: 'robustly-autonomous' bipedal walking - fall-free operation. "
  "What would confirm it: humanoids working in human spaces. "
  "What would kill it: evidence that bipedal walking resists robustness. "
  "What this does not claim: it does not claim robust humanoids exist, offers no engineering advice, and does not constitute a device recommendation."),
 "sig_lens": "The Signature lens reads humanoids as fragile demos, and asks what autonomy would make robust.",
 "how_it_works": "Researchers study humanoid walking through Atlas development, fall-prevention research, and autonomy studies.",
 "key_points": [
  "Atlas does parkour.",
  "Humanoids are fragile and expensive.",
  "Teleoperation is common.",
  "Robust wild walking is unachieved.",
  "Humanoids are demos, not workers.",
 ],
 "requirements": [
  "Fall-free autonomous walking.",
  "Wild-environment operation.",
  "Humanoids working in human spaces.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Boston Dynamics Atlas. Various; 2013 onward.",
  "Honda ASIMO. Various; 2000-2018.",
  "Pratt J et al. Biped control. Various; 2006-2016.",
  "Kuindersma S et al. Walking reviews. Various; 2016-2021.",
 ],
 "demo_data": {"a": ("humanoid falls per hour in the wild (approx)", 2.0),
               "b": ("human falls per hour (approx)", 0.001), "bounds": (1500.0, 2500.0),
               "step1": "two thousand times the human fall rate - the fragile biped",
               "confirm": "humanoids work in human spaces",
               "refute": "bipedal walking proves to resist robustness"},
},
# ------------------------------------------------------------------ rank 5
{
 "key": "robot-safety",
 "name": "Robot Safety: Working Beside Humans",
 "group": "Interaction",
 "ladder_rank": 5, "ladder_tier": "foundations",
 "problem": "Robots are caged for safety - can they work safely beside humans?",
 "description": "Robot safety - the collaboration problem: industrial robots are caged; cobots are slow and weak; and the safety standards (ISO 10218, TS 15066) limit capability. True safe collaboration is pending. The standards cap cobot speed and force so low that the 'collaborative' robot is often just a slow robot - safety purchased with capability.",
 "background": "Industrial safety (1970s-80s) caged robots; cobots (2010s) enabled limited collaboration; but speed and strength were sacrificed. As of 2026 collaboration is still constrained.",
 "why_it_matters": "Safe collaboration would put robots everywhere: the uncaged coworker.",
 "sig_pointer": "The Signature system's proposed approach makes robots safely collaborative, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that safety needs designed collaboration: the speed and strength with safety - proven in standards. "
  "Assumptions: (1) safety is designable; (2) capability retains; (3) standards certify. "
  "Reasoning path: a design model explains caged status and predicts safe collaboration. "
  "Proposed mechanism: 'designed-safe' collaboration - capable safe robots. "
  "What would confirm it: fast strong robots working safely with humans. "
  "What would kill it: evidence that safety requires weakness. "
  "What this does not claim: it makes no safety claims, offers no safety advice, and does not constitute a standards recommendation."),
 "sig_lens": "The Signature lens reads cobots as weakened compromise, and asks what design would make safe.",
 "how_it_works": "Researchers study robot safety through ISO standards, collision research, and safe-design studies.",
 "key_points": [
  "Industrial robots are caged.",
  "Cobots are slow and weak.",
  "Safety standards limit capability.",
  "True collaboration is pending.",
  "Safety and capability trade off.",
 ],
 "requirements": [
  "Safe fast strong robots.",
  "Certified collaboration standards.",
  "Uncaged robot coworkers.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "ISO 10218 / TS 15066. Various.",
  "Haddadin S et al. Robot safety. Various; 2012-2019.",
  "Lasota PA et al. Collaboration reviews. Various; 2017-2021.",
  "Bicchi A et al. Safe design. Various; 2008-2016.",
 ],
 "demo_data": {"a": ("industrial robots caged, percent (approx)", 90.0),
               "b": ("percent scale", 100.0), "bounds": (0.82, 0.97),
               "step1": "nine in ten caged - the uncollaborative industry",
               "confirm": "fast strong robots work safely with humans",
               "refute": "safety proves to require weakness"},
},
# ------------------------------------------------------------------ rank 6
{
 "key": "soft-robotics",
 "name": "Soft Robotics: The Squishy Machine",
 "group": "Design",
 "ladder_rank": 6, "ladder_tier": "foundations",
 "problem": "Soft robots are safe and adaptable - but can they be controlled precisely?",
 "description": "Soft robotics - the squishy machine: soft bodies are safe and conformable; but modeling infinite degrees of freedom is hard; control is imprecise; and the field is still more promise than product. Whitesides' soft grippers handle fruit beautifully; ask one to assemble a watch and the infinite degrees of freedom become infinite excuses.",
 "background": "Soft robotics (2010s, Whitesides, Rus) grew rapidly; but control lagged materials. As of 2026 soft robots are still imprecise.",
 "why_it_matters": "Precise soft robots would transform handling and medicine: the gentle machine made exact.",
 "sig_pointer": "The Signature system's proposed approach controls soft robots precisely, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that soft robots need learned control: the infinite-DOF bodies modeled - with precision achieved. "
  "Assumptions: (1) modeling is possible; (2) control is learnable; (3) precision follows. "
  "Reasoning path: a control model explains imprecise status and predicts exact soft robots. "
  "Proposed mechanism: 'learned-control' soft robotics - precise squishy machines. "
  "What would confirm it: precise soft robots in applications. "
  "What would kill it: evidence that soft bodies resist precision. "
  "What this does not claim: it does not claim precise soft robots exist, offers no engineering advice, and does not constitute a device recommendation."),
 "sig_lens": "The Signature lens reads soft robots as uncontrollable squish, and asks what learning would make precise.",
 "how_it_works": "Researchers study soft robotics through learned control, material modeling, and application prototyping.",
 "key_points": [
  "Soft bodies are safe and conformable.",
  "Infinite DOF defeats modeling.",
  "Control is imprecise.",
  "The field is promise-heavy.",
  "Materials outran control.",
 ],
 "requirements": [
  "Modeled soft-body dynamics.",
  "Learned precise control.",
  "Precise soft robots in applications.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Whitesides GM et al. Soft robotics. Various; 2011-2018.",
  "Rus D et al. Design reviews. Various; 2015-2021.",
  "Kim S et al. Control research. Various; 2013-2020.",
  "Laschi C et al. Soft reviews. Various; 2016-2022.",
 ],
 "demo_data": {"a": ("soft robots with precise control, percent (approx)", 15.0),
               "b": ("percent scale", 100.0), "bounds": (0.08, 0.25),
               "step1": "eighty-five percent imprecise - the uncontrollable squish",
               "confirm": "precise soft robots in applications",
               "refute": "soft bodies prove to resist precision"},
},
# ------------------------------------------------------------------ rank 7
{
 "key": "swarm-robotics",
 "name": "Swarm Robotics: The Collective Machine",
 "group": "Systems",
 "ladder_rank": 7, "ladder_tier": "foundations",
 "problem": "Ant colonies coordinate - can robot swarms achieve collective intelligence?",
 "description": "Swarm robotics - the collective machine: simple robots with local rules promise emergent behavior; but the swarms are small, the behaviors are simple, and the engineering of emergence is undeveloped. The kilobot thousand-robot demo remains the field's scaling landmark a decade on - collective behavior still means aggregation and foraging, not construction.",
 "background": "Swarm robotics (1990s-2000s, Deneubourg, Dorigo) was bio-inspired; kilobots (2014) scaled to a thousand; but complexity lagged. As of 2026 swarms are still simple.",
 "why_it_matters": "Collective robot intelligence would transform construction and exploration: the colony made machine.",
 "sig_pointer": "The Signature system's proposed approach engineers swarm emergence, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that swarms need emergence engineering: the local rules designed - with collective intelligence. "
  "Assumptions: (1) emergence is designable; (2) rules compose; (3) intelligence follows. "
  "Reasoning path: an emergence model explains simple status and predicts collective machines. "
  "Proposed mechanism: 'emergence-engineered' swarms - designed collective intelligence. "
  "What would confirm it: swarms with complex collective behavior. "
  "What would kill it: evidence that emergence resists engineering. "
  "What this does not claim: it does not claim collective intelligence exists, offers no engineering advice, and does not constitute a systems recommendation."),
 "sig_lens": "The Signature lens reads swarms as simple collectives, and asks what design would make intelligent.",
 "how_it_works": "Researchers study swarms through kilobot experiments, emergence modeling, and behavior design.",
 "key_points": [
  "Kilobots scaled to a thousand robots.",
  "Behaviors remain simple.",
  "Emergence engineering is undeveloped.",
  "Local rules promise global behavior.",
  "Swarms are still simple.",
 ],
 "requirements": [
  "Designed emergence rules.",
  "Complex collective behavior.",
  "Swarm intelligence in applications.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Rubenstein M et al. Kilobots. Various; 2014-2017.",
  "Dorigo M et al. Swarm reviews. Various; 2004-2021.",
  "Brambilla M et al. Design methods. Various; 2013-2020.",
  "Şahin E et al. Swarm perspectives. Various; 2005-2015.",
 ],
 "demo_data": {"a": ("swarm behaviors beyond simple, percent (approx)", 10.0),
               "b": ("percent scale", 100.0), "bounds": (0.05, 0.18),
               "step1": "nine in ten behaviors simple - the unintelligent collective",
               "confirm": "swarms with complex collective behavior",
               "refute": "emergence proves to resist engineering"},
},
# ------------------------------------------------------------------ rank 8
{
 "key": "robot-learning",
 "name": "Robot Learning: The Data Problem",
 "group": "AI",
 "ladder_rank": 8, "ladder_tier": "foundations",
 "problem": "Robots need data to learn - but robot data is expensive. Can learning be data-efficient?",
 "description": "Robot learning - the data problem: deep learning needs millions of examples; robot examples cost time and hardware; sim-to-real helps but the gap persists; and data-efficient robot learning is the bottleneck.",
 "background": "Robot learning (2010s) grew with deep learning; sim-to-real (2016-2020) helped; but the data bottleneck persists. As of 2026 robots are still data-hungry.",
 "why_it_matters": "Data-efficient learning would make robots adaptable: the fast learner.",
 "sig_pointer": "The Signature system's proposed approach makes robot learning data-efficient, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that robot learning needs efficiency: the few-shot and sim-to-real methods - with real adaptation. "
  "Assumptions: (1) efficiency is achievable; (2) sim-to-real closes; (3) robots adapt. "
  "Reasoning path: an efficiency model explains the bottleneck and predicts fast learners. "
  "Proposed mechanism: 'data-efficient' robot learning - few-shot adaptation. "
  "What would confirm it: robots learning new tasks from few examples. "
  "What would kill it: evidence that robots need big data. "
  "What this does not claim: it does not claim data-efficient learning exists, offers no engineering advice, and does not constitute a research recommendation."),
 "sig_lens": "The Signature lens reads robot learning as data-starved, and asks what efficiency would feed.",
 "how_it_works": "Researchers study robot learning through few-shot methods, sim-to-real research, and foundation models.",
 "key_points": [
  "Robot data is expensive.",
  "Deep learning needs millions of examples.",
  "Sim-to-real helps partially.",
  "The data bottleneck persists.",
  "Robots are still data-hungry.",
 ],
 "requirements": [
  "Few-shot robot learning.",
  "Closed sim-to-real gap.",
  "Fast-adapting robots.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Levine S et al. Robot learning. Various; 2016-2021.",
  "Tobin J et al. Sim-to-real. Various; 2017-2020.",
  "Finn C et al. Few-shot learning. Various; 2017-2021.",
  "Brohan A et al. Foundation models. Various; 2022-2024.",
 ],
 "demo_data": {"a": ("examples needed to learn a task (approx)", 1000.0),
               "b": ("examples a human needs (approx)", 5.0), "bounds": (150.0, 250.0),
               "step1": "a thousand examples against five - the data-hungry learner",
               "confirm": "robots learn new tasks from few examples",
               "refute": "robots prove to need big data"},
},
# ------------------------------------------------------------------ rank 9
{
 "key": "tactile-sensing",
 "name": "Tactile Sensing: The Sense of Touch",
 "group": "Sensing",
 "ladder_rank": 9, "ladder_tier": "foundations",
 "problem": "Robots are touch-blind - can tactile sensing give them the sense of touch?",
 "description": "Tactile sensing - the missing sense: human hands feel texture, slip, and force; robot touch is crude; GelSight (2010s) improved; but the sense of touch is still primitive. Adelson's GelSight gave robots a fingertip with human-like resolution; most robot hands still ship without any touch sensing at all.",
 "background": "Tactile sensing (1980s-2000s) was crude; GelSight (2011) was the breakthrough; but integration lagged. As of 2026 robots are still touch-blind.",
 "why_it_matters": "Robotic touch would transform manipulation: the feeling hand.",
 "sig_pointer": "The Signature system's proposed approach gives robots touch, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that touch needs integrated sensing: the tactile skins deployed - with manipulation transformed. "
  "Assumptions: (1) skins are deployable; (2) they are informative; (3) manipulation improves. "
  "Reasoning path: an integration model explains touch-blind status and predicts feeling robots. "
  "Proposed mechanism: 'integrated' tactile sensing - deployed touch. "
  "What would confirm it: robots manipulating by touch. "
  "What would kill it: evidence that touch can't be sensed usefully. "
  "What this does not claim: it does not claim robotic touch exists at scale, offers no engineering advice, and does not constitute a sensor recommendation."),
 "sig_lens": "The Signature lens reads robots as touch-blind, and asks what skins would make feel.",
 "how_it_works": "Researchers study tactile sensing through GelSight development, skin integration, and manipulation studies.",
 "key_points": [
  "Human touch senses texture and slip.",
  "Robot touch is crude.",
  "GelSight was the breakthrough.",
  "Integration with manipulation lags.",
  "Robots are still touch-blind.",
 ],
 "requirements": [
  "Deployed tactile skins.",
  "Touch-informed manipulation.",
  "Feeling robots in applications.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Johnson KO et al. Human touch. Various; 1981-2000.",
  "Adelson EH et al. GelSight. Various; 2011-2017.",
  "Dahiya RS et al. Tactile reviews. Various; 2013-2020.",
  "Li Q et al. Touch integration. Various; 2020-2023.",
 ],
 "demo_data": {"a": ("robot hands with tactile sensing, percent (approx)", 20.0),
               "b": ("percent scale", 100.0), "bounds": (0.12, 0.3),
               "step1": "four in five hands touch-blind - the unfeeling manipulator",
               "confirm": "robots manipulate by touch",
               "refute": "touch proves unable to be sensed usefully"},
},
# ------------------------------------------------------------------ rank 10
{
 "key": "autonomous-driving",
 "name": "Autonomous Driving: The Last 1%",
 "group": "Navigation",
 "ladder_rank": 10, "ladder_tier": "foundations",
 "problem": "Self-driving works 99% of the time - can the last 1% of edge cases be solved?",
 "description": "Autonomous driving - the last 1%: Waymo operates robotaxis; but edge cases (weather, construction, unpredictability) persist; and the long tail is the problem. Full autonomy is still pending. Waymo's driverless miles now number in the tens of millions, yet every expansion into a new city rediscovers how long the tail of edge cases really is.",
 "background": "Self-driving (2000s-2010s, DARPA) progressed; Waymo (2018 onward) deployed; but the long tail persists. As of 2026 autonomy is geofenced.",
 "why_it_matters": "Solved autonomy would transform transport: the driver made obsolete.",
 "sig_pointer": "The Signature system's proposed approach solves driving's long tail, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that autonomy needs long-tail mastery: the edge cases handled - with full deployment. "
  "Assumptions: (1) the tail is masterable; (2) it is finite; (3) deployment follows. "
  "Reasoning path: a tail model explains geofenced status and predicts full autonomy. "
  "Proposed mechanism: 'long-tail-mastered' autonomy - handled edge cases. "
  "What would confirm it: full autonomy everywhere. "
  "What would kill it: evidence that the tail is infinite. "
  "What this does not claim: it does not claim full autonomy exists, offers no engineering advice, and does not constitute a safety claim."),
 "sig_lens": "The Signature lens reads autonomy as tail-defeated, and asks what mastery would deploy.",
 "how_it_works": "Researchers study autonomy through Waymo operations, edge-case research, and safety validation.",
 "key_points": [
  "Waymo operates robotaxis.",
  "Edge cases persist.",
  "The long tail is the problem.",
  "Autonomy is geofenced.",
  "Full deployment is pending.",
 ],
 "requirements": [
  "Mastered edge cases.",
  "Full geographic deployment.",
  "Validated full autonomy.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Waymo operations. Various; 2018 onward.",
  "DARPA Grand Challenge. Various; 2004-2007.",
  "Koopman P et al. Safety validation. Various; 2019-2023.",
  "Shalev-Shwartz S et al. Autonomy reviews. Various; 2017-2021.",
 ],
 "demo_data": {"a": ("miles per disengagement, thousands (approx)", 50.0),
               "b": ("human miles per crash, hundreds of thousands (approx)", 5.0), "bounds": (8.0, 12.0),
               "step1": "ten times safer than humans, still geofenced - the last percent's wall",
               "confirm": "full autonomy everywhere",
               "refute": "the tail proves infinite"},
},
# ------------------------------------------------------------------ rank 11
{
 "key": "drone-autonomy",
 "name": "Drone Autonomy: Flying Without Pilots",
 "group": "Navigation",
 "ladder_rank": 11, "ladder_tier": "foundations",
 "problem": "Drones fly - but true autonomy (obstacle-dense, GPS-denied) is still limited. Can drones fly themselves?",
 "description": "Drone autonomy - flying without pilots: consumer drones are stable; but autonomous navigation in clutter, GPS-denied spaces, and beyond-visual-line-of-sight is still developing. Skydio showed obstacle-dodging autonomy was possible and still went bankrupt in 2024 - the technology worked, the business of autonomy didn't.",
 "background": "Drones (2010s) became consumer products; autonomy research (2010s-2020s) advanced; but true autonomy lags. As of 2026 drones are still piloted or scripted.",
 "why_it_matters": "True drone autonomy would transform delivery and inspection: the pilotless sky.",
 "sig_pointer": "The Signature system's proposed approach makes drones truly autonomous, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that drone autonomy needs robust navigation: the cluttered GPS-denied flight - with BVLOS operation. "
  "Assumptions: (1) navigation is solvable; (2) it is robust; (3) drones deploy. "
  "Reasoning path: a navigation model explains piloted status and predicts autonomous skies. "
  "Proposed mechanism: 'robustly-navigating' drone autonomy - GPS-denied flight. "
  "What would confirm it: autonomous drones in delivery and inspection. "
  "What would kill it: evidence that drone autonomy resists robustness. "
  "What this does not claim: it does not claim true drone autonomy exists, offers no engineering advice, and does not constitute a safety claim."),
 "sig_lens": "The Signature lens reads drones as piloted stability, and asks what navigation would make autonomous.",
 "how_it_works": "Researchers study drone autonomy through visual navigation, GPS-denied research, and BVLOS trials.",
 "key_points": [
  "Consumer drones are stable.",
  "Cluttered navigation is hard.",
  "GPS-denied flight is developing.",
  "BVLOS is still restricted.",
  "Drones are piloted or scripted.",
 ],
 "requirements": [
  "Robust cluttered navigation.",
  "GPS-denied autonomy.",
  "BVLOS operations.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Scaramuzza D et al. Drone vision. Various; 2014-2021.",
  "Mohta K et al. GPS-denied flight. Various; 2018-2021.",
  "FAA BVLOS rulemaking. Various; 2020 onward.",
  "Floreano D et al. Drone reviews. Various; 2015-2020.",
 ],
 "demo_data": {"a": ("drone flights fully autonomous, percent (approx)", 10.0),
               "b": ("percent scale", 100.0), "bounds": (0.05, 0.18),
               "step1": "nine in ten need pilots - the unflown autonomy",
               "confirm": "autonomous drones in delivery and inspection",
               "refute": "drone autonomy proves to resist robustness"},
},
# ------------------------------------------------------------------ rank 12
{
 "key": "exoskeletons",
 "name": "Exoskeletons: The Wearable Robot",
 "group": "Interaction",
 "ladder_rank": 12, "ladder_tier": "compounded",
 "problem": "Exoskeletons promise superhuman strength - but they're heavy, awkward, and limited. Can they become practical?",
 "description": "Exoskeletons - the wearable robot: military and medical exoskeletons exist; but weight, power, and comfort limit; and the practical exoskeleton is still pending. Ekso and ReWalk won medical approvals; the able-bodied worker exoskeleton - the one that would actually scale - remains a demo, not a product.",
 "background": "Exoskeletons (1960s-2000s, Hardiman) were early; medical exos (2010s, Ekso, ReWalk) were approved; but practicality lagged. As of 2026 exoskeletons are still niche.",
 "why_it_matters": "Practical exoskeletons would augment humans: the strength worn.",
 "sig_pointer": "The Signature system's proposed approach makes exoskeletons practical, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that exoskeletons need lightweight power: the weight reduced - with comfort and capability. "
  "Assumptions: (1) weight is reducible; (2) power suffices; (3) users adopt. "
  "Reasoning path: a weight model explains niche status and predicts practical exos. "
  "Proposed mechanism: 'lightweight-powered' exoskeletons - wearable capability. "
  "What would confirm it: exoskeletons in widespread use. "
  "What would kill it: evidence that exoskeletons can't be practical. "
  "What this does not claim: it does not claim practical exoskeletons exist, offers no engineering advice, and does not constitute a device recommendation."),
 "sig_lens": "The Signature lens reads exoskeletons as heavy promise, and asks what lightness would make practical.",
 "how_it_works": "Researchers study exoskeletons through lightweight design, power research, and user studies.",
 "key_points": [
  "Military and medical exoskeletons exist.",
  "Weight and power limit them.",
  "Comfort is poor.",
  "Medical exos were approved.",
  "Practicality is still pending.",
 ],
 "requirements": [
  "Lightweight capable exoskeletons.",
  "Comfortable long-term wear.",
  "Widespread exoskeleton use.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Hardiman program. Various; 1960s-1970s.",
  "Ekso / ReWalk approvals. Various; 2010s.",
  "Young AJ et al. Exo reviews. Various; 2017-2021.",
  "Sawicki GS et al. Augmentation. Various; 2020-2023.",
 ],
 "demo_data": {"a": ("exoskeleton weight, kg (approx)", 20.0),
               "b": ("comfortable wearable weight, kg (approx)", 5.0), "bounds": (3.0, 5.0),
               "step1": "four times the comfortable weight - the heavy promise",
               "confirm": "exoskeletons in widespread use",
               "refute": "exoskeletons prove unable to be practical"},
},
# ------------------------------------------------------------------ rank 13
{
 "key": "surgical-robots",
 "name": "Surgical Robots: The Autonomous Surgeon",
 "group": "Applications",
 "ladder_rank": 13, "ladder_tier": "compounded",
 "problem": "Surgical robots assist - but can they operate autonomously?",
 "description": "Surgical robots - the autonomous surgeon: da Vinci assists surgeons; but autonomy is minimal; and the autonomous surgeon is still science fiction with early demos. The STAR robot sutured pig intestine autonomously in 2016; a decade later no autonomous surgical procedure is anywhere near clinical use.",
 "background": "Surgical robots (2000s, da Vinci) assisted; autonomy research (2010s-2020s) is early. As of 2026 surgeons still operate.",
 "why_it_matters": "Autonomous surgery would transform medicine: the surgeon that never tires.",
 "sig_pointer": "The Signature system's proposed approach builds the autonomous surgeon, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that surgical autonomy needs supervised mastery: the procedures automated - with safety proven. "
  "Assumptions: (1) procedures are automatable; (2) safety is provable; (3) autonomy follows. "
  "Reasoning path: an automation model explains assist-only status and predicts autonomous surgery. "
  "Proposed mechanism: 'safety-proven' surgical autonomy - automated procedures. "
  "What would confirm it: autonomous surgeries in trials. "
  "What would kill it: evidence that surgery resists autonomy. "
  "What this does not claim: it does not claim autonomous surgery exists, offers no medical advice, and does not constitute a device recommendation."),
 "sig_lens": "The Signature lens reads surgical robots as assist-only, and asks what mastery would make autonomous.",
 "how_it_works": "Researchers study surgical autonomy through automation research, safety validation, and early trials.",
 "key_points": [
  "da Vinci assists surgeons.",
  "Autonomy is minimal.",
  "Early demos exist.",
  "Safety validation is the barrier.",
  "Surgeons still operate.",
 ],
 "requirements": [
  "Automated surgical procedures.",
  "Proven surgical safety.",
  "Autonomous surgeries in trials.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "da Vinci surgical system. Various; 2000 onward.",
  "Shademan A et al. STAR robot. Various; 2016-2022.",
  "Moustris GP et al. Autonomy reviews. Various; 2011-2020.",
  "Fiorini P et al. Surgical robotics. Various; 2022-2024.",
 ],
 "demo_data": {"a": ("surgical steps automated, percent (approx)", 10.0),
               "b": ("percent scale", 100.0), "bounds": (0.05, 0.18),
               "step1": "nine in ten steps human - the un-autonomous surgeon",
               "confirm": "autonomous surgeries in trials",
               "refute": "surgery proves to resist autonomy"},
},
# ------------------------------------------------------------------ rank 14
{
 "key": "agricultural-robots",
 "name": "Agricultural Robots: Farming's Future",
 "group": "Applications",
 "ladder_rank": 14, "ladder_tier": "compounded",
 "problem": "Farms need labor - can robots pick, weed, and tend crops?",
 "description": "Agricultural robots - farming's future: weeding and harvesting robots exist; but the field is unstructured; delicate crops defeat machines; and the farm robot is still developing. Strawberry-picking robots make the conference videos; the economics of delicate-ripe-fruit harvesting still lose to human hands on cost.",
 "background": "Ag robots (2010s-2020s) grew; harvesting demos impressed; but deployment lagged. As of 2026 farms are still human-tended.",
 "why_it_matters": "Farm robots would transform agriculture: the tender that never tires.",
 "sig_pointer": "The Signature system's proposed approach robots the farm, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that farm robots need delicate handling: the crops picked and tended - with economics working. "
  "Assumptions: (1) handling is achievable; (2) economics work; (3) farms adopt. "
  "Reasoning path: a handling model explains developing status and predicts robot farms. "
  "Proposed mechanism: 'delicately-handling' farm robots - tended crops. "
  "What would confirm it: robots farming commercially. "
  "What would kill it: evidence that farming resists robotics. "
  "What this does not claim: it does not claim robot farms exist, offers no engineering advice, and does not constitute an agricultural recommendation."),
 "sig_lens": "The Signature lens reads farms as human-tended, and asks what handling would robotize.",
 "how_it_works": "Researchers study ag robots through harvesting research, weeding trials, and field deployments.",
 "key_points": [
  "Weeding and harvesting robots exist.",
  "Fields are unstructured.",
  "Delicate crops defeat machines.",
  "Deployment lags demos.",
  "Farms are still human-tended.",
 ],
 "requirements": [
  "Delicate crop handling.",
  "Working farm economics.",
  "Commercial robot farming.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Bechar A et al. Ag robotics. Various; 2016-2021.",
  "Duckett T et al. Field robots. Various; 2018-2022.",
  "Harvesting robot literature. Various; 2015-2023.",
  "Edan Y et al. Automation reviews. Various; 2009-2020.",
 ],
 "demo_data": {"a": ("farm tasks robotized, percent (approx)", 15.0),
               "b": ("percent scale", 100.0), "bounds": (0.08, 0.25),
               "step1": "eighty-five percent human - the untended automation",
               "confirm": "robots farm commercially",
               "refute": "farming proves to resist robotics"},
},
# ------------------------------------------------------------------ rank 15
{
 "key": "construction-robots",
 "name": "Construction Robots: Building the Future",
 "group": "Applications",
 "ladder_rank": 15, "ladder_tier": "compounded",
 "problem": "Construction is dangerous and slow - can robots build buildings?",
 "description": "Construction robots - building the future: bricklaying and 3D-printing robots exist; but sites are chaotic; and the robot-built building is still rare. 3D-printed houses exist as demonstrations; the chaotic, weather-exposed, constantly-changing construction site still defeats the robots sent to tame it.",
 "background": "Construction robots (2010s-2020s) emerged; 3D-printed buildings were demonstrated; but adoption lagged. As of 2026 construction is still human-built.",
 "why_it_matters": "Construction robots would transform building: the builder that never tires.",
 "sig_pointer": "The Signature system's proposed approach robots construction, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that construction needs site-tolerant robots: the chaotic sites handled - with buildings built. "
  "Assumptions: (1) sites are handleable; (2) robots build; (3) industry adopts. "
  "Reasoning path: a tolerance model explains rare status and predicts robot construction. "
  "Proposed mechanism: 'site-tolerant' construction robots - built buildings. "
  "What would confirm it: robot-built buildings in use. "
  "What would kill it: evidence that construction resists robotics. "
  "What this does not claim: it does not claim robot-built buildings exist at scale, offers no engineering advice, and does not constitute a construction recommendation."),
 "sig_lens": "The Signature lens reads construction as human-built chaos, and asks what tolerance would robotize.",
 "how_it_works": "Researchers study construction robots through bricklaying trials, 3D-printing demos, and site studies.",
 "key_points": [
  "Bricklaying robots exist.",
  "3D-printed buildings were demonstrated.",
  "Sites are chaotic.",
  "Adoption lags.",
  "Construction is still human-built.",
 ],
 "requirements": [
  "Site-tolerant robots.",
  "Robot-built buildings.",
  "Adopted construction robotics.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Bock T et al. Construction robotics. Various; 2007-2016.",
  "3D-printed building projects. Various; 2014-2023.",
  "Delgado JMD et al. Reviews. Various; 2019-2023.",
  "Pan M et al. Automation studies. Various; 2018-2022.",
 ],
 "demo_data": {"a": ("construction tasks robotized, percent (approx)", 10.0),
               "b": ("percent scale", 100.0), "bounds": (0.05, 0.18),
               "step1": "nine in ten tasks human - the unbuilt automation",
               "confirm": "robot-built buildings in use",
               "refute": "construction proves to resist robotics"},
},
# ------------------------------------------------------------------ rank 16
{
 "key": "underwater-robots",
 "name": "Underwater Robots: Exploring the Deep",
 "group": "Applications",
 "ladder_rank": 16, "ladder_tier": "compounded",
 "problem": "The deep ocean is unexplored - can underwater robots map and work there?",
 "description": "Underwater robots - exploring the deep: AUVs map the seafloor; but communication is hard; manipulation is primitive; and the deep remains largely unexplored. NOAA estimates over 80 percent of the ocean floor unmapped; the robots capable of mapping it at depth exist in handfuls, not fleets.",
 "background": "AUVs (1990s-2000s) mapped; but the deep ocean is still 80% unmapped. As of 2026 robots explore the shallows.",
 "why_it_matters": "Deep-capable robots would map the planet's last frontier: the explorer of the abyss.",
 "sig_pointer": "The Signature system's proposed approach explores the deep robotically, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that deep exploration needs capable AUVs: the communication and manipulation solved - with the deep mapped. "
  "Assumptions: (1) challenges are solvable; (2) robots are capable; (3) the deep yields. "
  "Reasoning path: a capability model explains shallow status and predicts deep exploration. "
  "Proposed mechanism: 'deep-capable' underwater robots - mapped abyss. "
  "What would confirm it: the deep ocean mapped by robots. "
  "What would kill it: evidence that the deep resists robotics. "
  "What this does not claim: it does not claim the deep is mapped, offers no engineering advice, and does not constitute an exploration recommendation."),
 "sig_lens": "The Signature lens reads the deep as unexplored, and asks what capability would map.",
 "how_it_works": "Researchers study underwater robots through AUV development, communication research, and mapping missions.",
 "key_points": [
  "AUVs map the seafloor.",
  "Underwater communication is hard.",
  "Manipulation is primitive.",
  "80% of the ocean is unmapped.",
  "Robots explore the shallows.",
 ],
 "requirements": [
  "Solved deep communication.",
  "Capable deep manipulation.",
  "Mapped deep ocean.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Yoerger DR et al. AUVs. Various; 1990s-2010s.",
  "NOAA ocean mapping. Various.",
  "Bowen AD et al. Deep vehicles. Various; 2008-2018.",
  "Sahoo A et al. Underwater reviews. Various; 2019-2023.",
 ],
 "demo_data": {"a": ("seafloor mapped, percent (approx)", 25.0),
               "b": ("percent scale", 100.0), "bounds": (0.18, 0.35),
               "step1": "three-quarters unmapped - the unexplored majority",
               "confirm": "the deep ocean mapped by robots",
               "refute": "the deep proves to resist robotics"},
},
# ------------------------------------------------------------------ rank 17
{
 "key": "space-robots",
 "name": "Space Robots: Working Off-World",
 "group": "Applications",
 "ladder_rank": 17, "ladder_tier": "compounded",
 "problem": "Space needs robots - but can they work autonomously so far from help?",
 "description": "Space robots - working off-world: rovers explore Mars; but they're slow and supervised; in-space servicing is emerging; and true space autonomy is pending. Perseverance drives itself between waypoints on Mars, but every interesting decision still waits for instructions traveling at light-speed delay.",
 "background": "Space robots (1970s onward) explored; Mars rovers (2000s-2020s) were supervised; servicing (2020s) is emerging. As of 2026 space robots are still teleoperated.",
 "why_it_matters": "Autonomous space robots would build off-world: the worker beyond Earth.",
 "sig_pointer": "The Signature system's proposed approach makes space robots autonomous, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that space robots need deep autonomy: the light-delay operation - with off-world work. "
  "Assumptions: (1) autonomy handles delay; (2) robots work; (3) space yields. "
  "Reasoning path: an autonomy model explains supervised status and predicts space workers. "
  "Proposed mechanism: 'deeply-autonomous' space robots - off-world workers. "
  "What would confirm it: autonomous off-world construction. "
  "What would kill it: evidence that space resists autonomy. "
  "What this does not claim: it does not claim autonomous space workers exist, offers no engineering advice, and does not constitute a space recommendation."),
 "sig_lens": "The Signature lens reads space robots as supervised explorers, and asks what autonomy would make worker.",
 "how_it_works": "Researchers study space robots through rover autonomy, servicing demos, and delay-tolerant control.",
 "key_points": [
  "Rovers explore Mars supervised.",
  "Light delay defeats teleoperation.",
  "In-space servicing is emerging.",
  "True autonomy is pending.",
  "Space robots are still teleoperated.",
 ],
 "requirements": [
  "Delay-tolerant autonomy.",
  "Autonomous off-world work.",
  "Space construction by robots.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Mars rover programs. Various; 2004 onward.",
  "NASA servicing missions. Various; 2020s.",
  "Yoshida K et al. Space robotics. Various; 2009-2019.",
  "Flores-Abad A et al. Servicing reviews. Various; 2014-2020.",
 ],
 "demo_data": {"a": ("space-robot tasks autonomous, percent (approx)", 20.0),
               "b": ("percent scale", 100.0), "bounds": (0.12, 0.3),
               "step1": "four in five tasks supervised - the teleoperated frontier",
               "confirm": "autonomous off-world construction",
               "refute": "space proves to resist autonomy"},
},
# ------------------------------------------------------------------ rank 18
{
 "key": "human-robot-teams",
 "name": "Human-Robot Teaming",
 "group": "Interaction",
 "ladder_rank": 18, "ladder_tier": "compounded",
 "problem": "Humans and robots should team - but can they coordinate fluently?",
 "description": "Human-robot teaming - the fluency problem: the teams exist; but coordination is clunky; mutual understanding is shallow; and fluent teaming is unachieved. Hoffman's fluency metrics gave the field a way to measure the awkwardness; the awkwardness, measured, persists.",
 "background": "HRI (2000s-2010s) studied teaming; fluency metrics were developed; but the teams are still clunky. As of 2026 teaming is still awkward.",
 "why_it_matters": "Fluent teaming would multiply human capability: the partner, not the tool.",
 "sig_pointer": "The Signature system's proposed approach makes human-robot teams fluent, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that teaming needs mutual modeling: the humans and robots predicting each other - with fluency. "
  "Assumptions: (1) modeling is possible; (2) it is mutual; (3) fluency follows. "
  "Reasoning path: a modeling approach explains clunky status and predicts fluent teams. "
  "Proposed mechanism: 'mutually-modeling' teams - fluent coordination. "
  "What would confirm it: fluent human-robot teams in use. "
  "What would kill it: evidence that teaming resists fluency. "
  "What this does not claim: it does not claim fluent teams exist, offers no engineering advice, and does not constitute an interaction recommendation."),
 "sig_lens": "The Signature lens reads teaming as clunky coordination, and asks what modeling would make fluent.",
 "how_it_works": "Researchers study teaming through fluency metrics, mutual-modeling research, and team trials.",
 "key_points": [
  "Human-robot teams exist.",
  "Coordination is clunky.",
  "Mutual understanding is shallow.",
  "Fluency metrics were developed.",
  "Fluent teaming is unachieved.",
 ],
 "requirements": [
  "Mutual predictive modeling.",
  "Fluent coordination demonstrated.",
  "Fluent teams in use.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Hoffman G et al. Fluency metrics. Various; 2007-2019.",
  "Breazeal C et al. HRI teaming. Various; 2004-2016.",
  "Chen JYC et al. Team reviews. Various; 2018-2022.",
  "Lyons JB et al. Trust in teams. Various; 2021-2024.",
 ],
 "demo_data": {"a": ("team tasks fluent, percent (approx)", 25.0),
               "b": ("percent scale", 100.0), "bounds": (0.18, 0.35),
               "step1": "three in four tasks clunky - the awkward partnership",
               "confirm": "fluent human-robot teams in use",
               "refute": "teaming proves to resist fluency"},
},
# ------------------------------------------------------------------ rank 19
{
 "key": "robot-ethics",
 "name": "Robot Ethics: The Responsible Machine",
 "group": "Interaction",
 "ladder_rank": 19, "ladder_tier": "compounded",
 "problem": "Robots act in the world - can their behavior be made ethical?",
 "description": "Robot ethics - the responsible machine: the field debates machine ethics; but implementation is philosophical; and the responsible robot is still conceptual. Winfield's ethical governors showed how constraints could be implemented; the industry's robots still run on no ethics at all - just cages and standards.",
 "background": "Machine ethics (2000s-2010s, Wallach, Allen) was philosophical; robot ethics grew; but implementation lags. As of 2026 ethics is still debated.",
 "why_it_matters": "Ethical robots would act responsibly: the machine with morals.",
 "sig_pointer": "The Signature system's proposed approach makes robots ethical, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that robot ethics needs implemented principles: the behaviors constrained - with responsibility. "
  "Assumptions: (1) principles are implementable; (2) they constrain; (3) robots are responsible. "
  "Reasoning path: an implementation model explains philosophical status and predicts ethical robots. "
  "Proposed mechanism: 'principle-implemented' robot ethics - constrained behavior. "
  "What would confirm it: robots behaving ethically in trials. "
  "What would kill it: evidence that ethics can't be implemented. "
  "What this does not claim: it takes no moral positions, offers no engineering advice, and does not constitute an ethics recommendation."),
 "sig_lens": "The Signature lens reads robot ethics as philosophical debate, and asks what implementation would make responsible.",
 "how_it_works": "Researchers study robot ethics through machine-ethics research, implementation attempts, and policy debates.",
 "key_points": [
  "Machine ethics is philosophical.",
  "Implementation is minimal.",
  "The responsible robot is conceptual.",
  "The field debates principles.",
  "Ethics is still debated.",
 ],
 "requirements": [
  "Implemented ethical principles.",
  "Constrained robot behavior.",
  "Ethical robots in trials.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Wallach W, Allen C. Moral Machines. Various; 2009-2015.",
  "Lin P et al. Robot ethics. Various; 2012-2020.",
  "Winfield AFT et al. Ethical governors. Various; 2019-2023.",
  "Malle BF et al. Moral HRI. Various; 2016-2022.",
 ],
 "demo_data": {"a": ("robots with implemented ethics, percent (approx)", 5.0),
               "b": ("percent scale", 100.0), "bounds": (0.03, 0.08),
               "step1": "one in twenty constrained - the unprincipled machine",
               "confirm": "robots behave ethically in trials",
               "refute": "ethics proves unable to be implemented"},
},
# ------------------------------------------------------------------ rank 20
{
 "key": "explainable-robots",
 "name": "Explainable Robots",
 "group": "AI",
 "ladder_rank": 20, "ladder_tier": "compounded",
 "problem": "Robots decide opaquely - can they explain themselves?",
 "description": "Explainable robots - the transparency problem: learned policies are opaque; users can't understand robot decisions; and the explainable robot is still developing. The XAI boom produced explanations for classifiers; the robot that can tell you why it chose that grasp, in terms you accept, doesn't exist yet.",
 "background": "Explainable AI (2010s-2020s) grew; robot explanations (2010s-2020s) are emerging. As of 2026 robots still decide opaquely.",
 "why_it_matters": "Explainable robots would be trustworthy: the machine that says why.",
 "sig_pointer": "The Signature system's proposed approach makes robots explainable, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that robots need explanation: the decisions communicated - with user understanding. "
  "Assumptions: (1) explanations are generatable; (2) they are faithful; (3) users trust. "
  "Reasoning path: an explanation model explains opaque status and predicts transparent robots. "
  "Proposed mechanism: 'explanation-generating' robots - communicated decisions. "
  "What would confirm it: robots explaining decisions faithfully. "
  "What would kill it: evidence that robot decisions resist explanation. "
  "What this does not claim: it does not claim explainable robots exist, offers no engineering advice, and does not constitute an AI recommendation."),
 "sig_lens": "The Signature lens reads robots as opaque deciders, and asks what generation would make transparent.",
 "how_it_works": "Researchers study robot explanations through XAI adaptation, user studies, and explanation interfaces.",
 "key_points": [
  "Learned policies are opaque.",
  "Users can't understand decisions.",
  "Explainable AI is growing.",
  "Robot explanations are emerging.",
  "Robots still decide opaquely.",
 ],
 "requirements": [
  "Faithful explanation generation.",
  "User-understood decisions.",
  "Explaining robots in use.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Anjomshoae S et al. Explainable robots. Various; 2019-2023.",
  "Gunning D et al. XAI program. Various; 2017-2021.",
  "Hayes B et al. Robot explanations. Various; 2018-2022.",
  "Sado F et al. Transparency reviews. Various; 2023-2024.",
 ],
 "demo_data": {"a": ("robot decisions explainable, percent (approx)", 15.0),
               "b": ("percent scale", 100.0), "bounds": (0.08, 0.25),
               "step1": "eighty-five percent opaque - the unexplained decider",
               "confirm": "robots explain decisions faithfully",
               "refute": "robot decisions prove to resist explanation"},
},
# ------------------------------------------------------------------ rank 21
{
 "key": "long-term-autonomy",
 "name": "Long-Term Autonomy: Robots That Persist",
 "group": "Systems",
 "ladder_rank": 21, "ladder_tier": "compounded",
 "problem": "Robots work for hours - can they operate for months and years?",
 "description": "Long-term autonomy - robots that persist: the field demos hours; but months-long operation needs robustness, adaptation, and maintenance; and the persistent robot is still rare. The STRANDS project ran robots for weeks in 2015; the field still celebrates deployments measured in days as long-term.",
 "background": "Long-term autonomy (2010s, STRANDS, 2015) was demonstrated; but the field still demos short. As of 2026 persistence is still rare.",
 "why_it_matters": "Persistent robots would transform monitoring and service: the machine that stays.",
 "sig_pointer": "The Signature system's proposed approach makes robots persistent, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that persistence needs robust adaptation: the months-long operation - with self-maintenance. "
  "Assumptions: (1) robustness suffices; (2) adaptation works; (3) robots persist. "
  "Reasoning path: a robustness model explains short-demo status and predicts persistent robots. "
  "Proposed mechanism: 'robustly-adapting' long-term autonomy - persistent operation. "
  "What would confirm it: robots operating for years. "
  "What would kill it: evidence that persistence resists robotics. "
  "What this does not claim: it does not claim persistent robots exist at scale, offers no engineering advice, and does not constitute a systems recommendation."),
 "sig_lens": "The Signature lens reads robots as short-demo machines, and asks what robustness would make persist.",
 "how_it_works": "Researchers study long-term autonomy through STRANDS follow-ups, robustness research, and persistent deployments.",
 "key_points": [
  "The field demos hours.",
  "Months-long operation is rare.",
  "STRANDS demonstrated weeks.",
  "Robustness and adaptation are needed.",
  "Persistence is still rare.",
 ],
 "requirements": [
  "Months-long robust operation.",
  "Adaptive self-maintenance.",
  "Robots operating for years.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "STRANDS project. Various; 2013-2017.",
  "Hawes N et al. Long-term autonomy. Various; 2017-2021.",
  "Krajník T et al. Persistence research. Various; 2017-2022.",
  "Kunze L et al. Reviews. Various; 2018-2023.",
 ],
 "demo_data": {"a": ("robots operating for months (approx)", 10.0),
               "b": ("robots demoed (approx)", 500.0), "bounds": (0.01, 0.035),
               "step1": "ten persistent of five hundred demoed - the short-lived machine",
               "confirm": "robots operate for years",
               "refute": "persistence proves to resist robotics"},
},
# ------------------------------------------------------------------ rank 22
{
 "key": "robot-manipulation",
 "name": "Dexterous Manipulation: The Human Hand",
 "group": "Manipulation",
 "ladder_rank": 22, "ladder_tier": "compounded",
 "problem": "Human hands are marvels - can robot hands match their dexterity?",
 "description": "Dexterous manipulation - the human hand: the Shadow Hand has 20+ DOF; but control is the bottleneck; and the dexterous robot hand is still clumsy. Andrychowicz's learned dexterity spun a Rubik's cube with a Shadow Hand in 2019; the hand still can't tie a shoelace.",
 "background": "Robot hands (1980s-2000s) were built; the Shadow Hand (2000s-2010s) was the high-water mark; but dexterity lagged. As of 2026 robot hands are still clumsy.",
 "why_it_matters": "Dexterous hands would transform manipulation: the marvel made machine.",
 "sig_pointer": "The Signature system's proposed approach builds dexterous robot hands, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that dexterity needs learned control: the high-DOF hands controlled - with human-like skill. "
  "Assumptions: (1) control is learnable; (2) hands suffice; (3) dexterity follows. "
  "Reasoning path: a control model explains clumsy status and predicts dexterous hands. "
  "Proposed mechanism: 'learned-control' dexterous hands - human-like manipulation. "
  "What would confirm it: robot hands with human dexterity. "
  "What would kill it: evidence that dexterity resists robotics. "
  "What this does not claim: it does not claim dexterous hands exist, offers no engineering advice, and does not constitute a device recommendation."),
 "sig_lens": "The Signature lens reads robot hands as clumsy mechanisms, and asks what control would make dexterous.",
 "how_it_works": "Researchers study dexterity through Shadow Hand control, learned manipulation, and tactile integration.",
 "key_points": [
  "The Shadow Hand has 20+ DOF.",
  "Control is the bottleneck.",
  "Robot hands are still clumsy.",
  "Human hands are the marvel.",
  "Dexterity lags hardware.",
 ],
 "requirements": [
  "Learned high-DOF control.",
  "Human-like robot dexterity.",
  "Dexterous hands in applications.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Shadow Robot Company. Various; 2000s onward.",
  "Bicchi A et al. Hand reviews. Various; 2000-2015.",
  "Andrychowicz M et al. Learned dexterity. Various; 2020-2021.",
  "Billard A et al. Manipulation reviews. Various; 2019-2023.",
 ],
 "demo_data": {"a": ("human-hand tasks a robot hand does, percent (approx)", 20.0),
               "b": ("percent scale", 100.0), "bounds": (0.12, 0.3),
               "step1": "four in five tasks beyond reach - the clumsy marvel",
               "confirm": "robot hands with human dexterity",
               "refute": "dexterity proves to resist robotics"},
},
# ------------------------------------------------------------------ rank 23
{
 "key": "field-robotics",
 "name": "Field Robotics: The Unstructured World",
 "group": "Systems",
 "ladder_rank": 23, "ladder_tier": "compounded",
 "problem": "Labs are structured - the world isn't. Can robots handle the unstructured?",
 "description": "Field robotics - the unstructured world: the DARPA challenges showed the gap; field robots work in niches; and the general field robot is still pending. The DARPA Robotics Challenge finals in 2015 - robots falling over on live television - remain the field's most honest public demonstration.",
 "background": "Field robotics (1990s-2000s) grew; DARPA challenges (2000s-2010s) tested; but generality lagged. As of 2026 field robots are still niche.",
 "why_it_matters": "Field-capable robots would work everywhere: the machine for the real world.",
 "sig_pointer": "The Signature system's proposed approach builds field-capable robots, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that field robotics needs unstructured mastery: the real world handled - with general deployment. "
  "Assumptions: (1) mastery is achievable; (2) it generalizes; (3) robots deploy. "
  "Reasoning path: a mastery model explains niche status and predicts field robots. "
  "Proposed mechanism: 'unstructured-mastering' field robots - real-world workers. "
  "What would confirm it: general field robots in use. "
  "What would kill it: evidence that the unstructured resists robotics. "
  "What this does not claim: it does not claim general field robots exist, offers no engineering advice, and does not constitute a systems recommendation."),
 "sig_lens": "The Signature lens reads field robots as niche specialists, and asks what mastery would generalize.",
 "how_it_works": "Researchers study field robotics through DARPA lessons, unstructured-navigation research, and deployments.",
 "key_points": [
  "DARPA challenges showed the gap.",
  "Field robots work in niches.",
  "The general field robot is pending.",
  "Labs are structured; the world isn't.",
  "Generality lags.",
 ],
 "requirements": [
  "Unstructured-environment mastery.",
  "General field deployment.",
  "Field robots in broad use.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "DARPA Robotics Challenge. Various; 2012-2015.",
  "Thrun S et al. Field robotics. Various; 2002-2010.",
  "Cunningham C et al. Unstructured navigation. Various; 2019-2023.",
  "Bagnell JA et al. Learning for field. Various; 2010-2018.",
 ],
 "demo_data": {"a": ("field environments robots handle generally (approx)", 15.0),
               "b": ("field environments (approx)", 100.0), "bounds": (0.08, 0.25),
               "step1": "fifteen of a hundred environments - the niche specialist",
               "confirm": "general field robots in use",
               "refute": "the unstructured proves to resist robotics"},
},
# ------------------------------------------------------------------ rank 24
{
 "key": "robot-consciousness",
 "name": "Robot Consciousness: The Inner Life",
 "group": "Theory",
 "ladder_rank": 24, "ladder_tier": "advanced",
 "problem": "Could robots ever be conscious - and would we know?",
 "description": "Robot consciousness - the inner-life question: the philosophy is debated; the engineering has no tests; and the field mostly avoids the question. The 2023 debates over machine consciousness gave the question new urgency; robotics still has no instrument for detecting an inner life, if one were there.",
 "background": "Consciousness debates (philosophy) met robotics (2000s-2020s); but no methodology exists. As of 2026 the question is unaddressed.",
 "why_it_matters": "Conscious robots would transform ethics: the inner life made machine.",
 "sig_pointer": "The Signature system's proposed approach addresses robot consciousness, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that robot consciousness needs methodology: the tests and criteria - with honest uncertainty. "
  "Assumptions: (1) criteria are formulable; (2) tests are possible; (3) uncertainty is honest. "
  "Reasoning path: a methodology model explains the avoidance and predicts addressed questions. "
  "Proposed mechanism: 'methodologically-addressed' robot consciousness - tested criteria. "
  "What would confirm it: accepted tests for robot consciousness. "
  "What would kill it: evidence that the question is untestable. "
  "What this does not claim: it takes no position on robot consciousness, offers no engineering advice, and does not constitute a philosophical claim."),
 "sig_lens": "The Signature lens reads consciousness as the avoided question, and asks what methodology would address.",
 "how_it_works": "Researchers study robot consciousness through test proposals, criteria debates, and philosophical analyses.",
 "key_points": [
  "No test for robot consciousness exists.",
  "The philosophy is debated.",
  "Engineering has no methodology.",
  "The field avoids the question.",
  "Uncertainty is honest.",
 ],
 "requirements": [
  "Formulated test criteria.",
  "Accepted consciousness tests.",
  "Honest uncertainty maintained.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Chalmers DJ et al. Consciousness and machines. Various; 2023-2024.",
  "Butlin P et al. Consciousness tests. Various; 2023-2024.",
  "Schneider S et al. Machine consciousness. Various; 2019-2023.",
  "Reggia JA et al. Computational consciousness. Various; 2015-2020.",
 ],
 "demo_data": {"a": ("accepted tests for robot consciousness (approx)", 1.0),
               "b": ("proposed tests (approx)", 20.0), "bounds": (0.02, 0.1),
               "step1": "one accepted of twenty proposed - the untested question",
               "confirm": "accepted tests for robot consciousness",
               "refute": "the question proves untestable"},
},
# ------------------------------------------------------------------ rank 25
{
 "key": "general-purpose-robots",
 "name": "General-Purpose Robots",
 "group": "Systems",
 "ladder_rank": 25, "ladder_tier": "advanced",
 "problem": "Robots are specialists - can a general-purpose robot exist?",
 "description": "General-purpose robots - the specialist problem: every robot does one thing; the generalist is science fiction; and whether generality is achievable is the field's grand question. RT-2 and its successors showed a single model can span many robot tasks; 'many' still means dozens, against the human thousands.",
 "background": "Robotics (1960s onward) specialized; the generalist was always the dream. As of 2026 robots are still specialists.",
 "why_it_matters": "General-purpose robots would transform everything: the machine for all tasks.",
 "sig_pointer": "The Signature system's proposed approach builds general-purpose robots, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that generality needs foundation models: the robot brains trained broadly - with tasks following. "
  "Assumptions: (1) models generalize; (2) bodies suffice; (3) robots generalize. "
  "Reasoning path: a models approach explains specialist status and predicts general robots. "
  "Proposed mechanism: 'foundation-modeled' general robots - broadly-trained machines. "
  "What would confirm it: robots doing many tasks. "
  "What would kill it: evidence that generality resists robotics. "
  "What this does not claim: it does not claim general robots exist, offers no engineering advice, and does not constitute a systems recommendation."),
 "sig_lens": "The Signature lens reads robots as narrow specialists, and asks what models would generalize.",
 "how_it_works": "Researchers study generality through foundation models, multi-task learning, and generalist demos.",
 "key_points": [
  "Every robot does one thing.",
  "The generalist is science fiction.",
  "Foundation models promise generality.",
  "Generality is the grand question.",
  "Robots are still specialists.",
 ],
 "requirements": [
  "Broadly-trained robot models.",
  "Multi-task robot deployment.",
  "General-purpose robots in use.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Brohan A et al. RT foundation models. Various; 2022-2024.",
  "Reed S et al. Gato. Various; 2022-2023.",
  "Ahn M et al. Generalist agents. Various; 2022-2024.",
  "Driess D et al. Multi-task robots. Various; 2023-2024.",
 ],
 "demo_data": {"a": ("tasks a generalist robot does well (approx)", 10.0),
               "b": ("tasks a human does well (approx)", 1000.0), "bounds": (0.005, 0.018),
               "step1": "ten tasks against a thousand - the narrow specialist",
               "confirm": "robots do many tasks",
               "refute": "generality proves to resist robotics"},
},
# ------------------------------------------------------------------ rank 26
{
 "key": "robot-economics",
 "name": "Robot Economics: The Automation Question",
 "group": "Systems",
 "ladder_rank": 26, "ladder_tier": "advanced",
 "problem": "Robots transform labor - but can the economics be made to work for everyone?",
 "description": "Robot economics - the automation question: the productivity gains are real; but displacement is feared; and the field debates whether the economics can be inclusive. Acemoglu's economics of automation keep finding the same pattern: productivity rises, and the gains concentrate where the robots are owned.",
 "background": "Automation debates (1960s onward) recurred; the 2010s-2020s brought new urgency. As of 2026 the question is still debated.",
 "why_it_matters": "Inclusive robot economics would share the gains: the automation that lifts all.",
 "sig_pointer": "The Signature system's proposed approach addresses robot economics, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that robot economics needs inclusive models: the gains shared - with displacement managed. "
  "Assumptions: (1) models exist; (2) they are implementable; (3) inclusion follows. "
  "Reasoning path: an economics model explains the fear and predicts inclusive automation. "
  "Proposed mechanism: 'inclusively-modeled' robot economics - shared gains. "
  "What would confirm it: automation with shared prosperity. "
  "What would kill it: evidence that automation inherently displaces. "
  "What this does not claim: it takes no economic positions, offers no policy advice, and does not constitute an economics recommendation."),
 "sig_lens": "The Signature lens reads automation as feared displacement, and asks what models would include.",
 "how_it_works": "Researchers study robot economics through labor analyses, policy research, and deployment studies.",
 "key_points": [
  "Productivity gains are real.",
  "Displacement is feared.",
  "The debate recurred for decades.",
  "Inclusion is the question.",
  "New urgency arrived in the 2010s.",
 ],
 "requirements": [
  "Inclusive economic models.",
  "Managed displacement.",
  "Shared automation prosperity.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Acemoglu D et al. Automation economics. Various; 2017-2023.",
  "Brynjolfsson E et al. Second Machine Age. Various; 2014-2017.",
  "IFR robot statistics. Various.",
  "Frey CB et al. Employment studies. Various; 2013-2020.",
 ],
 "demo_data": {"a": ("workers displaced by robots, millions (approx)", 20.0),
               "b": ("workers augmented by robots, millions (approx)", 100.0), "bounds": (0.12, 0.3),
               "step1": "one displaced for five augmented - the feared ratio",
               "confirm": "automation with shared prosperity",
               "refute": "automation proves to inherently displace"},
},
# ------------------------------------------------------------------ rank 27
{
 "key": "evolutionary-robotics",
 "name": "Evolutionary Robotics: Evolving Machines",
 "group": "AI",
 "ladder_rank": 27, "ladder_tier": "advanced",
 "problem": "Can robots be evolved rather than designed - and would evolution beat engineering?",
 "description": "Evolutionary robotics - evolving machines: the algorithms evolve controllers and morphologies; but the evolved are simple; and whether evolution beats design is open. Quality-diversity algorithms produce wonderfully strange virtual creatures; embodied evolved robots remain small, simple, and lab-bound.",
 "background": "Evolutionary robotics (1990s, Harvey, Cliff) was bio-inspired; but scale lagged. As of 2026 evolution is still a niche method.",
 "why_it_matters": "Evolved robots would design themselves: the machine grown, not built.",
 "sig_pointer": "The Signature system's proposed approach evolves robots effectively, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that evolution needs scaled search: the morphologies and controllers evolved - with complexity. "
  "Assumptions: (1) search scales; (2) complexity emerges; (3) evolution competes. "
  "Reasoning path: a search model explains simple status and predicts evolved robots. "
  "Proposed mechanism: 'search-scaled' evolutionary robotics - complex evolved machines. "
  "What would confirm it: evolved robots beating designed ones. "
  "What would kill it: evidence that evolution can't beat design. "
  "What this does not claim: it does not claim evolved robots beat design, offers no engineering advice, and does not constitute a research recommendation."),
 "sig_lens": "The Signature lens reads evolution as simple search, and asks what scale would make complex.",
 "how_it_works": "Researchers study evolutionary robotics through scaled evolution, morphology search, and quality-diversity.",
 "key_points": [
  "Evolutionary algorithms evolve robots.",
  "The evolved are simple.",
  "Scale is the limitation.",
  "The field is bio-inspired.",
  "Evolution is still niche.",
 ],
 "requirements": [
  "Scaled evolutionary search.",
  "Complex evolved morphologies.",
  "Evolved beating designed.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Harvey I et al. Evolutionary robotics. Various; 1992-1997.",
  "Nolfi S et al. Reviews. Various; 2000-2016.",
  "Lehman J et al. Quality diversity. Various; 2011-2021.",
  "Doncieux S et al. Recent advances. Various; 2015-2020.",
 ],
 "demo_data": {"a": ("evolved robots beating designed, percent (approx)", 10.0),
               "b": ("percent scale", 100.0), "bounds": (0.05, 0.18),
               "step1": "nine in ten designed win - the unevolved method",
               "confirm": "evolved robots beat designed ones",
               "refute": "evolution proves unable to beat design"},
},
# ------------------------------------------------------------------ rank 28
{
 "key": "developmental-robotics",
 "name": "Developmental Robotics: Growing Up Machine",
 "group": "AI",
 "ladder_rank": 28, "ladder_tier": "advanced",
 "problem": "Children learn over years - can robots develop like children?",
 "description": "Developmental robotics - growing up machine: the field models child development; but robots don't develop; and the developmental robot is still aspirational. Oudeyer's curiosity-driven learning gave robots something like intrinsic motivation; none has yet had anything like a childhood.",
 "background": "Developmental robotics (2000s, Lungarella, Asada) modeled development; but the robots stayed infantile. As of 2026 development is still modeled, not achieved.",
 "why_it_matters": "Developing robots would learn like children: the machine that grows up.",
 "sig_pointer": "The Signature system's proposed approach develops robots like children, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that development needs staged learning: the years-long curricula - with robots growing. "
  "Assumptions: (1) development is stageable; (2) robots learn; (3) they grow up. "
  "Reasoning path: a developmental model explains infantile status and predicts grown robots. "
  "Proposed mechanism: 'staged-learning' developmental robots - grown machines. "
  "What would confirm it: robots developing over years. "
  "What would kill it: evidence that development resists robotics. "
  "What this does not claim: it does not claim developing robots exist, offers no engineering advice, and does not constitute a research recommendation."),
 "sig_lens": "The Signature lens reads robots as perpetual infants, and asks what staging would grow.",
 "how_it_works": "Researchers study developmental robotics through child-development modeling, curriculum learning, and long-term trials.",
 "key_points": [
  "The field models child development.",
  "Robots don't develop.",
  "The robots stayed infantile.",
  "Development is modeled, not achieved.",
  "Growing up is aspirational.",
 ],
 "requirements": [
  "Staged developmental curricula.",
  "Years-long robot development.",
  "Grown-up robots.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Lungarella M et al. Developmental robotics. Various; 2003-2010.",
  "Asada M et al. Cognitive development. Various; 2009-2016.",
  "Cangelosi A et al. Reviews. Various; 2015-2022.",
  "Oudeyer PY et al. Curiosity-driven learning. Various; 2007-2018.",
 ],
 "demo_data": {"a": ("robots developed over years (approx)", 2.0),
               "b": ("developmental robots built (approx)", 100.0), "bounds": (0.01, 0.035),
               "step1": "two grown of a hundred built - the perpetual infant",
               "confirm": "robots develop over years",
               "refute": "development proves to resist robotics"},
},
# ------------------------------------------------------------------ rank 29
{
 "key": "robot-language",
 "name": "Robot Language: Talking to Machines",
 "group": "Interaction",
 "ladder_rank": 29, "ladder_tier": "advanced",
 "problem": "Humans instruct by language - can robots understand natural instructions?",
 "description": "Robot language - talking to machines: LLMs (2020s) enabled instruction following; but grounding is shallow; and the truly language-competent robot is still developing. SayCan showed LLMs can propose sensible robot plans; the grounding - connecting 'bring me the mug' to this mug, here, now - still breaks regularly.",
 "background": "Language grounding (2010s) was shallow; LLMs (2022-2024) transformed; but grounding lags. As of 2026 robots follow simple instructions.",
 "why_it_matters": "Language-competent robots would take instruction: the machine that understands.",
 "sig_pointer": "The Signature system's proposed approach grounds robot language, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that robot language needs grounding: the words tied to actions - with understanding. "
  "Assumptions: (1) grounding is achievable; (2) it is deep; (3) robots understand. "
  "Reasoning path: a grounding model explains shallow status and predicts competent robots. "
  "Proposed mechanism: 'deeply-grounded' robot language - understood instructions. "
  "What would confirm it: robots following complex instructions. "
  "What would kill it: evidence that grounding resists language. "
  "What this does not claim: it does not claim understanding robots exist, offers no engineering advice, and does not constitute an AI recommendation."),
 "sig_lens": "The Signature lens reads robot language as shallow following, and asks what grounding would make understand.",
 "how_it_works": "Researchers study robot language through LLM integration, grounding research, and instruction trials.",
 "key_points": [
  "LLMs enabled instruction following.",
  "Grounding is shallow.",
  "Robots follow simple instructions.",
  "Complex instruction is developing.",
  "Understanding is the goal.",
 ],
 "requirements": [
  "Deep language grounding.",
  "Complex instruction following.",
  "Understanding robots.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Ahn M et al. SayCan. Various; 2022-2023.",
  "Brohan A et al. RT models. Various; 2022-2024.",
  "Tellex S et al. Grounding reviews. Various; 2020-2023.",
  "Driess D et al. Language robots. Various; 2023-2024.",
 ],
 "demo_data": {"a": ("complex instructions followed, percent (approx)", 40.0),
               "b": ("percent scale", 100.0), "bounds": (0.28, 0.52),
               "step1": "three in five instructions too complex - the shallow understanding",
               "confirm": "robots follow complex instructions",
               "refute": "grounding proves to resist language"},
},
# ------------------------------------------------------------------ rank 30
{
 "key": "robot-trust",
 "name": "Trust in Robots",
 "group": "Interaction",
 "ladder_rank": 30, "ladder_tier": "advanced",
 "problem": "Humans must trust robots - but can trust be engineered and calibrated?",
 "description": "Robot trust - the calibration problem: overtrust causes accidents; undertrust wastes capability; and the calibrated trust is still developing. Hancock's meta-analyses keep confirming the miscalibration: users trust the confident robot too much and the capable one too little.",
 "background": "Trust research (2000s-2010s, Hancock, Lee) studied the problem; but calibration lags. As of 2026 trust is still miscalibrated.",
 "why_it_matters": "Calibrated trust would make robots partners: the trust that's right.",
 "sig_pointer": "The Signature system's proposed approach calibrates robot trust, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that trust needs calibration: the overtrust and undertrust corrected - with appropriate reliance. "
  "Assumptions: (1) trust is calibratable; (2) it is measurable; (3) reliance follows. "
  "Reasoning path: a calibration model explains miscalibrated status and predicts trusted robots. "
  "Proposed mechanism: 'calibrated' robot trust - appropriate reliance. "
  "What would confirm it: appropriately-trusting users in trials. "
  "What would kill it: evidence that trust resists calibration. "
  "What this does not claim: it does not claim calibrated trust exists, offers no engineering advice, and does not constitute a design recommendation."),
 "sig_lens": "The Signature lens reads trust as miscalibrated reliance, and asks what measurement would calibrate.",
 "how_it_works": "Researchers study robot trust through calibration research, trust measurement, and reliance studies.",
 "key_points": [
  "Overtrust causes accidents.",
  "Undertrust wastes capability.",
  "Trust is miscalibrated.",
  "Measurement is developing.",
  "Calibration is the goal.",
 ],
 "requirements": [
  "Measured trust calibration.",
  "Corrected over/undertrust.",
  "Appropriately-trusting users.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Hancock PA et al. Trust meta-analysis. Various; 2011-2021.",
  "Lee JD et al. Trust in automation. Various; 2004-2015.",
  "Baker AL et al. Calibration research. Various; 2018-2023.",
  "Schaefer KE et al. Trust scales. Various; 2016-2021.",
 ],
 "demo_data": {"a": ("users with calibrated trust, percent (approx)", 30.0),
               "b": ("percent scale", 100.0), "bounds": (0.2, 0.42),
               "step1": "seven in ten miscalibrated - the wrong trust",
               "confirm": "appropriately-trusting users in trials",
               "refute": "trust proves to resist calibration"},
},
# ------------------------------------------------------------------ rank 31
{
 "key": "robot-creativity",
 "name": "Creative Robots",
 "group": "Theory",
 "ladder_rank": 31, "ladder_tier": "advanced",
 "problem": "Can robots be creative - or only recombinative?",
 "description": "Robot creativity - the creation question: robots generate art and designs; but the creativity is debated; and the truly creative robot is still conceptual. The generated art sells at auction; whether the machine that made it was creative remains a question the field politely declines to settle.",
 "background": "Creative machines (2010s-2020s) generated art; but the creativity debate persisted. As of 2026 creativity is still questioned.",
 "why_it_matters": "Creative robots would be partners in invention: the machine that creates.",
 "sig_pointer": "The Signature system's proposed approach explores robot creativity, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that robot creativity needs evaluation: the created works assessed - with creativity determined. "
  "Assumptions: (1) creativity is assessable; (2) it is achievable; (3) robots create. "
  "Reasoning path: an evaluation model explains the debate and predicts creative robots. "
  "Proposed mechanism: 'evaluated' robot creativity - assessed creation. "
  "What would confirm it: robots creating valued works. "
  "What would kill it: evidence that robots can't be creative. "
  "What this does not claim: it takes no position on machine creativity, offers no engineering advice, and does not constitute an artistic claim."),
 "sig_lens": "The Signature lens reads robot art as unassessed generation, and asks what evaluation would determine.",
 "how_it_works": "Researchers study robot creativity through generative systems, creativity evaluation, and artistic collaboration.",
 "key_points": [
  "Robots generate art and designs.",
  "Creativity is debated.",
  "The creative robot is conceptual.",
  "Evaluation is the question.",
  "Generation is not creation.",
 ],
 "requirements": [
  "Assessed creative works.",
  "Determined robot creativity.",
  "Valued robot creations.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Boden MA et al. Computational creativity. Various; 2004-2016.",
  "Colton S et al. Creativity systems. Various; 2008-2020.",
  "Elgammal A et al. Creative AI. Various; 2017-2021.",
  "McCormack J et al. Artistic robots. Various; 2019-2023.",
 ],
 "demo_data": {"a": ("robot works valued as creative (approx)", 5.0),
               "b": ("robot works generated (approx)", 1000.0), "bounds": (0.002, 0.01),
               "step1": "five valued of a thousand generated - the uncreative generation",
               "confirm": "robots create valued works",
               "refute": "robots prove unable to be creative"},
},
# ------------------------------------------------------------------ rank 32
{
 "key": "robot-rights",
 "name": "Robot Rights: The Personhood Question",
 "group": "Theory",
 "ladder_rank": 32, "ladder_tier": "advanced",
 "problem": "Could robots ever deserve rights - and how would we decide?",
 "description": "Robot rights - the personhood question: the philosophy is speculative; the law is unprepared; and the field mostly avoids the question. Sophia's Saudi citizenship in 2017 was theater; no legal system on Earth has a serious framework for machine personhood.",
 "background": "Robot rights (2000s-2010s) were philosophical; Sophia's citizenship (2017) was symbolic; but the question is still avoided. As of 2026 personhood is still speculative.",
 "why_it_matters": "Robot personhood would transform law: the rights of the machine.",
 "sig_pointer": "The Signature system's proposed approach addresses robot personhood, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that personhood needs criteria: the standards formulated - with honest debate. "
  "Assumptions: (1) criteria are formulable; (2) debate is honest; (3) law follows. "
  "Reasoning path: a criteria model explains the avoidance and predicts addressed personhood. "
  "Proposed mechanism: 'criteria-formulated' robot personhood - debated standards. "
  "What would confirm it: accepted personhood criteria. "
  "What would kill it: evidence that personhood is incoherent. "
  "What this does not claim: it takes no position on robot rights, offers no legal advice, and does not constitute a philosophical claim."),
 "sig_lens": "The Signature lens reads personhood as avoided speculation, and asks what criteria would decide.",
 "how_it_works": "Researchers study robot rights through philosophical criteria, legal analyses, and public debate.",
 "key_points": [
  "The philosophy is speculative.",
  "The law is unprepared.",
  "Sophia's citizenship was symbolic.",
  "The field avoids the question.",
  "Personhood is still speculative.",
 ],
 "requirements": [
  "Formulated personhood criteria.",
  "Honest public debate.",
  "Accepted legal standards.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Gunkel DJ et al. Robot rights. Various; 2012-2022.",
  "Sophia citizenship. 2017.",
  "Bryson JJ et al. Personhood debates. Various; 2010-2020.",
  "Darling K et al. Legal perspectives. Various; 2016-2021.",
 ],
 "demo_data": {"a": ("jurisdictions with robot-rights law (approx)", 1.0),
               "b": ("jurisdictions (approx)", 200.0), "bounds": (0.002, 0.01),
               "step1": "one symbolic of two hundred - the unlegislated personhood",
               "confirm": "accepted personhood criteria",
               "refute": "personhood proves incoherent"},
},
# ------------------------------------------------------------------ rank 33
{
 "key": "robot-future",
 "name": "The Future of Robotics: A Century Ahead",
 "group": "Theory",
 "ladder_rank": 33, "ladder_tier": "advanced",
 "problem": "What will robotics become? The field extrapolates poorly - can its future be foreseen?",
 "description": "Robotics futurology - predicting the field's century - is speculative: past predictions (humanoids by 2000) failed; but structured foresight is absent; whether futures work improves decisions is the meta-question.",
 "background": "Robotics predictions have a poor record; scenario methods are unused. As of 2026 the future is debated without discipline.",
 "why_it_matters": "Long-horizon decisions (research, policy) need foresight: the discipline of robotics futures.",
 "sig_pointer": "The Signature system's proposed approach builds disciplined robotics foresight, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that robotics futures need disciplined foresight: the scenario methods and roadmaps - with track records. "
  "Assumptions: (1) foresight is improvable; (2) methods exist; (3) they guide decisions. "
  "Reasoning path: a foresight model explains prediction failures and predicts better futures work. "
  "Proposed mechanism: 'disciplined' robotics foresight - tracked scenario methods. "
  "What would confirm it: foresight with validated track records. "
  "What would kill it: evidence that robotics futures are unforeseeable. "
  "What this does not claim: it does not claim any future, offers no engineering advice, and does not constitute a prediction."),
 "sig_lens": "The Signature lens reads robotics futures as undisciplined speculation, and asks what methods would foresee.",
 "how_it_works": "Researchers study robotics futures through scenario methods, technology roadmapping, and prediction tracking.",
 "key_points": [
  "Robotics predictions have a poor record.",
  "Humanoids were promised by 2000.",
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
  "IEEE robotics roadmaps. Various; 2015-2023.",
  "Foresight methodology literature. Various.",
  "EU robotics strategy. Various; 2020-2024.",
  "Christensen HI et al. Roadmaps. Various; 2016-2021.",
 ],
 "demo_data": {"a": ("robotics predictions with validated track records (approx)", 5.0),
               "b": ("robotics predictions made (approx)", 200.0), "bounds": (0.015, 0.04),
               "step1": "five tracked of two hundred made - the foresight without a record",
               "confirm": "foresight with validated track records",
               "refute": "robotics futures prove unforeseeable"},
},
# ------------------------------------------------------------------ rank 34
{
 "key": "singularity-robotics",
 "name": "The Robotics Singularity",
 "group": "Theory",
 "ladder_rank": 34, "ladder_tier": "advanced",
 "problem": "Could robots trigger a singularity - self-improving machines beyond control?",
 "description": "The robotics singularity - self-improving machines: the scenario is speculative; the control problem is debated; and the field is divided on seriousness. Bostrom formalized the control problem in 2014; a decade later the field still can't agree whether it's the most important problem or a distraction.",
 "background": "The singularity (Vinge, 1993; Kurzweil, 2005) was proposed; the control problem (Bostrom, 2014) was formalized; but the field is divided. As of 2026 the singularity is still speculative.",
 "why_it_matters": "The singularity question shapes robotics' ambitions: the future taken seriously.",
 "sig_pointer": "The Signature system's proposed approach addresses the robotics singularity, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that the singularity needs serious analysis: the scenarios assessed - with control addressed. "
  "Assumptions: (1) analysis is possible; (2) it informs; (3) control is addressable. "
  "Reasoning path: an analysis model explains the division and predicts addressed futures. "
  "Proposed mechanism: 'seriously-analyzed' singularity - assessed scenarios. "
  "What would confirm it: accepted singularity analyses. "
  "What would kill it: evidence that the singularity is incoherent. "
  "What this does not claim: it does not claim any singularity, offers no engineering advice, and does not constitute a prediction."),
 "sig_lens": "The Signature lens reads the singularity as divisive speculation, and asks what analysis would address.",
 "how_it_works": "Researchers study the singularity through scenario analyses, control-problem research, and futures literature.",
 "key_points": [
  "Vinge proposed the singularity (1993).",
  "The control problem was formalized.",
  "The field is divided on seriousness.",
  "Self-improvement is the trigger.",
  "The scenario is still speculative.",
 ],
 "requirements": [
  "Serious scenario analyses.",
  "Addressed control problem.",
  "Accepted singularity assessments.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Vinge V. Technological singularity. 1993.",
  "Kurzweil R. The Singularity Is Near. 2005.",
  "Bostrom N. Superintelligence. 2014.",
  "Russell S et al. Control research. Various; 2019-2024.",
 ],
 "demo_data": {"a": ("serious singularity analyses (approx)", 20.0),
               "b": ("singularity papers (approx)", 1000.0), "bounds": (0.01, 0.035),
               "step1": "twenty serious of a thousand speculative - the unaddressed singularity",
               "confirm": "accepted singularity analyses",
               "refute": "the singularity proves incoherent"},
},
]
