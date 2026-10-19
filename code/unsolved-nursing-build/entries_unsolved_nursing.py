#!/usr/bin/env python3
"""Entries for The Unsolved Nursing Database (unsolved-nursing) and its
Signature half (unsolved-nursing-signature).

34 famous unsolved problems in nursing science, ladder-ordered by accessibility
(rank 1 = most approachable, rank 34 = most complex/compounded).
Public half: real, fact-checked problems. Signature half: the same 34
problems through the Signature lens, with Signature-generated proposed
solutions that are ALWAYS labeled as proposals, never established science.

Honesty rule (enforced in every record): never claim proof, never imply
peer acceptance, never present speculation as settled. Signature proposals
are labeled speculation for research discussion only - never clinical advice,
never a staffing or care recommendation, no cure claims.
"""

LABEL = "Signature-generated proposed solution \u2014 not established science."

SIG_TAIL = ("Signature editions carry the Signature system's proposed "
            "solution approaches to famous unsolved problems. Every "
            "solution is labeled a Signature-generated proposal, never "
            "established science, never peer-accepted, never proof, never "
            "clinical advice.")

STD_COMMON = [
    "Problem statements verified against the published nursing literature; open status confirmed as of 2026.",
    "Signature solution sections are labeled proposals: they state assumptions, a reasoning path, a proposed mechanism, what would confirm or kill them, and what they do not claim.",
    "Signature proposals are labeled speculation for research discussion only - never clinical advice, never a staffing or care recommendation; no cure claims appear.",
]

ENTRIES = [
# ------------------------------------------------------------------ rank 1
{
 "key": "nurse-staffing",
 "name": "Nurse Staffing Ratios and Patient Outcomes",
 "group": "Workforce",
 "ladder_rank": 1, "ladder_tier": "foundations",
 "problem": "More nurses per patient means fewer deaths - but what is the causal mechanism, and what is the optimal ratio for each unit type?",
 "description": "Decades of observational research link richer nurse staffing to lower mortality, fewer complications, and shorter stays: Aiken's landmark 2002 JAMA study found each additional patient per nurse raised the odds of death by 7%. California legislated ratios in 2004. Yet the mechanism - surveillance, rescue, missed care - remains inferred rather than proven, optimal ratios per unit type are unknown, and hospitals still staff largely by budget rather than evidence.",
 "background": "The staffing-outcomes link was built through the 1990s-2000s: Aiken, Needleman (NEJM 2002), and others showed consistent associations across countries. California's 2004 ratio law (AB 394) became the natural experiment; studies showed mortality improvements but also unintended consequences (reduced ancillary staff, ED crowding debates). The 'missed care' framework (Kalisch) proposed the mechanism: thin staffing forces rationing of surveillance, ambulation, and teaching. But observational data cannot fully separate staffing from everything else good hospitals do, and randomized staffing trials are considered infeasible. As of 2026 no health system staffs by a proven optimal ratio.",
 "why_it_matters": "Staffing is the most expensive and most consequential input in hospital care: too thin kills, too rich bankrupts. Finding the causal mechanism and the optimal ratio would save lives at sustainable cost - the central management question of inpatient care.",
 "sig_pointer": "The Signature system's proposed approach treats staffing as a surveillance-capacity problem with measurable missed-care signals, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that staffing works through surveillance bandwidth: each nurse can track only so many patient trajectories, and harm occurs when trajectory count exceeds tracking capacity. "
  "Assumptions: (1) the active ingredient is timely detection of deterioration, not task completion; (2) tracking capacity is finite and measurable per nurse per shift; (3) missed surveillance, not missed tasks, drives mortality. "
  "Reasoning path: reframing staffing as surveillance capacity explains why ratios matter most on high-acuity units and why adding nurses helps more than adding assistants - only licensed surveillance scales. "
  "Proposed mechanism: a 'surveillance load' metric combining patient acuity, turnover, and trajectory volatility, with staffing set to keep load within measured nurse capacity - tested against mortality and rescue rates. "
  "What would confirm it: load-based staffing outperforming fixed ratios on outcomes in trials, with missed-surveillance events mediating the effect. "
  "What would kill it: evidence that staffing effects come from task completion (medications, turning) rather than surveillance, or that capacity cannot be measured reliably. "
  "What this does not claim: it does not claim a ratio ready for policy, does not recommend staffing levels, and does not constitute clinical advice."),
 "sig_lens": "The Signature lens reads the nurse as a surveillance instrument with finite bandwidth, and asks what load metric would keep every patient watched.",
 "how_it_works": "Nurse researchers study staffing through large observational cohorts, natural experiments from ratio laws, missed-care surveys, and workload measurement studies.",
 "key_points": [
  "Each additional patient per nurse raised mortality odds ~7% (Aiken 2002).",
  "California legislated ratios in 2004; mortality improved with debated side effects.",
  "The 'missed care' framework proposes surveillance rationing as the mechanism.",
  "Optimal ratios per unit type remain unknown; staffing follows budgets.",
  "Randomized staffing trials are considered infeasible, limiting causal proof.",
 ],
 "requirements": [
  "A causal mechanism separating staffing from other hospital quality factors.",
  "A measurable surveillance-capacity metric per nurse per shift.",
  "Evidence-based optimal ratios by unit type and acuity.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Aiken LH et al. Hospital nurse staffing and patient mortality, nurse burnout, and job dissatisfaction. JAMA. 2002;288(16):1987-1993.",
  "Needleman J et al. Nurse-staffing levels and the quality of care in hospitals. New England Journal of Medicine. 2002;346:1715-1722.",
  "Kalisch BJ et al. Missed nursing care: a concept analysis. Journal of Advanced Nursing. 2009;65(7):1509-1517.",
  "Serratt T. California's nurse-to-patient ratios, part 1-3. Policy, Politics, and Nursing Practice. 2013;14.",
 ],
 "demo_data": {"a": ("mortality odds rise per added patient per nurse, percent (Aiken)", 7.0),
               "b": ("percent scale", 100.0), "bounds": (0.05, 0.1),
               "step1": "each extra patient per nurse raises the odds of death by seven percent",
               "confirm": "load-based staffing beats fixed ratios with missed surveillance mediating the effect",
               "refute": "staffing effects prove driven by task completion with surveillance capacity unmeasurable"},
},
# ------------------------------------------------------------------ rank 2
{
 "key": "failure-to-rescue",
 "name": "Predicting Patient Deterioration",
 "group": "Acute Care",
 "ladder_rank": 2, "ladder_tier": "foundations",
 "problem": "Patients rarely die without warning - vital signs drift for hours first. Why do deteriorating patients still go unnoticed until crisis?",
 "description": "Failure to rescue - death after a treatable complication - is among the largest sources of preventable hospital mortality. Studies of vital-sign records show abnormalities precede cardiac arrest and ICU transfer by hours, yet recognition fails: rapid response teams (pioneered by Lee at Liverpool Hospital, 1990s) help but depend on someone calling them, and early warning scores (NEWS, MEWS) suffer alarm fatigue and poor sensitivity in real wards.",
 "background": "Silber's 'failure to rescue' concept (1992) reframed surgical mortality as a rescue problem, not just a complication problem. Rapid response systems spread after the 2005 Institute for Healthcare Improvement campaign; the MERIT trial (2005) showed mixed results, later attributed to implementation. Early warning scores standardized the call criteria, but validation shows modest discrimination and nurses override them frequently - often correctly. Continuous monitoring and AI deterioration prediction are the current frontier, with algorithms showing promise retrospectively but struggling prospectively with false alarms. As of 2026 the gap between detectable drift and reliable rescue remains open.",
 "why_it_matters": "Rescue is nursing's core acute function: catching the falling patient in time. Closing the recognition gap would prevent thousands of arrests, ICU transfers, and deaths yearly - the purest expression of surveillance saving lives.",
 "sig_pointer": "The Signature system's proposed approach treats deterioration as a trajectory deviation with a personal baseline, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that warning scores fail because they use population thresholds while deterioration is personal: a heart rate of 110 means different things in different patients, and the signal is deviation from the patient's own trajectory. "
  "Assumptions: (1) each patient has a learnable baseline trajectory; (2) deterioration announces itself as deviation from that baseline hours before crisis; (3) nurses already sense this intuitively, which is why they override scores. "
  "Reasoning path: reframing detection as personal-trajectory deviation explains both score failures and nurse override accuracy - the proposal formalizes what experienced nurses do tacitly. "
  "Proposed mechanism: a 'personal trajectory monitor' that learns each patient's baseline in the first hours and alerts on deviation patterns, tuned to nurse-validated true deteriorations. "
  "What would confirm it: trajectory-deviation alerts outperforming NEWS on time-to-rescue in trials, with nurse agreement as validation. "
  "What would kill it: evidence that deterioration has no consistent pre-crisis signature even personally, or that personal baselines cannot be learned fast enough to matter. "
  "What this does not claim: it does not claim a monitor ready for wards, does not recommend overriding scores, and does not constitute clinical advice."),
 "sig_lens": "The Signature lens reads deterioration as a personal trajectory bending, and asks what would detect the bend hours before the break.",
 "how_it_works": "Researchers study rescue through vital-sign trajectory analysis, rapid-response outcome studies, early-warning-score validation, nurse decision-making research, and AI prediction trials.",
 "key_points": [
  "Failure to rescue (Silber 1992) reframes mortality as a rescue problem.",
  "Vital-sign abnormalities precede arrest by hours in most cases.",
  "Rapid response teams help but depend on timely activation.",
  "Early warning scores have modest real-world discrimination.",
  "Nurses frequently - and often correctly - override the scores.",
 ],
 "requirements": [
  "Detection based on personal trajectories, not population thresholds.",
  "Alerts with a false-alarm rate nurses will actually answer.",
  "Proof that earlier recognition converts to saved lives, not just earlier ICU transfer.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Silber JH et al. Hospital and patient characteristics associated with death after surgery. Medical Care. 1992;30(7):615-629.",
  "Lee A et al. The medical emergency team. Anaesthesia and Intensive Care. 1995;23:183-186.",
  "Hillman K et al. Introduction of the medical emergency team (MERIT) study. Lancet. 2005;365:2091-2097.",
  "Smith MEB et al. Early warning systems for adults. Annals of Internal Medicine. 2014;160:19-29.",
 ],
 "demo_data": {"a": ("hours of vital-sign drift before most arrests (typical)", 6.0),
               "b": ("hours in a nursing shift", 12.0), "bounds": (0.3, 0.7),
               "step1": "the warning usually exists for half a shift before the crisis it predicts",
               "confirm": "trajectory-deviation alerts beat NEWS on time-to-rescue in trials",
               "refute": "deterioration proves to have no consistent pre-crisis signature even personally"},
},
# ------------------------------------------------------------------ rank 3
{
 "key": "pressure-injury",
 "name": "Pressure Injury Prevention",
 "group": "Wound Care",
 "ladder_rank": 3, "ladder_tier": "foundations",
 "problem": "Pressure injuries still develop in immobile patients despite turning schedules - why does prevention fail, and what actually protects skin under load?",
 "description": "Pressure injuries (pressure ulcers) form when sustained pressure - especially over bony prominences - cuts off tissue perfusion, causing ischemia and necrosis. They affect millions of hospitalized and nursing-home patients yearly, cause pain and sepsis, and cost billions. Prevention rests on repositioning, support surfaces, and risk scales (Braden), yet injuries still occur in well-staffed units, and deep-tissue injuries can begin before any skin change is visible.",
 "background": "The pressure-ischemia mechanism was established in the mid-20th century; the Braden scale (1987) standardized risk assessment. Support-surface technology advanced from alternating-pressure mattresses to low-air-loss and microclimate control. But trials keep showing residual injuries: turning every two hours is the standard of care with surprisingly thin direct evidence, deep tissue injury (recognized as a distinct entity in the 2000s) starts in muscle under intact skin, and dark skin tones hide early changes, creating equity gaps in detection. As of 2026 no bundle prevents all pressure injuries, and 'unavoidable' remains a contested category.",
 "why_it_matters": "Pressure injuries are considered largely preventable, which makes each one a quality failure with legal and financial consequences. They cause real suffering in the most vulnerable patients - the immobile elderly - and solving prevention would protect millions.",
 "sig_pointer": "The Signature system's proposed approach treats tissue tolerance as a personal, time-varying budget, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that pressure injury is a budget problem: each patient's tissues tolerate a personal integral of pressure over time, and injury occurs when the budget is spent - which is why fixed turning schedules both over- and under-protect. "
  "Assumptions: (1) tissue tolerance varies between patients and within a patient over time; (2) the budget can be estimated from perfusion signals under load; (3) deep-tissue injury is the same budget spent faster in muscle. "
  "Reasoning path: reframing prevention as budget management explains why two-hour turning works on average but fails individuals - the schedule ignores the budget - and predicts personalized repositioning will outperform fixed schedules. "
  "Proposed mechanism: a 'tissue tolerance budget' estimated from interface pressure plus perfusion monitoring, triggering repositioning when the individual's budget nears exhaustion rather than on the clock. "
  "What would confirm it: budget-triggered repositioning outperforming scheduled turning on injury rates in trials, with perfusion markers mediating the effect. "
  "What would kill it: evidence that tolerance has no measurable personal component, or that continuous monitoring adds nothing to scheduled care. "
  "What this does not claim: it does not claim a device ready for units, does not recommend abandoning turning schedules, and does not constitute clinical advice."),
 "sig_lens": "The Signature lens reads skin under load as spending a personal tolerance budget, and asks what would show the balance before it empties.",
 "how_it_works": "Nurse researchers study pressure injuries through support-surface trials, repositioning studies, interface-pressure mapping, deep-tissue-injury imaging research, and risk-scale validation across skin tones.",
 "key_points": [
  "Pressure injuries stem from sustained pressure causing tissue ischemia.",
  "The Braden scale (1987) standardized risk assessment worldwide.",
  "Two-hour turning is standard with surprisingly thin direct evidence.",
  "Deep tissue injury begins in muscle under intact skin.",
  "Early changes are harder to detect in dark skin tones - an equity gap.",
 ],
 "requirements": [
  "A measurable personal tissue-tolerance budget.",
  "Proof that personalized repositioning beats fixed schedules.",
  "Detection methods that work across all skin tones.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Bergstrom N et al. The Braden Scale for predicting pressure sore risk. Nursing Research. 1987;36(4):205-210.",
  "National Pressure Ulcer Advisory Panel. Prevention and treatment of pressure ulcers: clinical practice guideline. 2014.",
  "Defloor T. The risk of pressure sores: a conceptual scheme. Journal of Clinical Nursing. 1999;8(2):206-216.",
  "Bates-Jensen BM et al. Subepidermal moisture and pressure injury detection. Various; 2017-2020.",
 ],
 "demo_data": {"a": ("standard repositioning interval, hours", 2.0),
               "b": ("hours in a day", 24.0), "bounds": (0.05, 0.15),
               "step1": "the two-hour standard means twelve repositionings a day - a clock, not a patient",
               "confirm": "budget-triggered repositioning beats scheduled turning on injury rates",
               "refute": "tissue tolerance proves to have no measurable personal component"},
},
# ------------------------------------------------------------------ rank 4
{
 "key": "nurse-burnout",
 "name": "Nurse Burnout Mechanisms",
 "group": "Workforce",
 "ladder_rank": 4, "ladder_tier": "foundations",
 "problem": "Nurses burn out at alarming rates - but is burnout caused by workload, moral injury, or something structural, and what actually prevents it?",
 "description": "Burnout - emotional exhaustion, depersonalization, and reduced efficacy (Maslach's formulation) - affects a large fraction of nurses, worsened by the pandemic. It predicts turnover, errors, and worse patient outcomes. Interventions abound: resilience training, mindfulness, staffing improvements, magnet-hospital programs. Yet burnout persists at scale, suggesting the causes are structural rather than individual - and resilience programs that blame the nurse remain controversial.",
 "background": "Maslach's burnout inventory (1981) gave the syndrome a measure; Aiken's work linked nurse burnout to patient mortality. The pandemic years (2020-2022) produced the worst workforce crisis in modern nursing, with turnover spiking and travel-nurse markets exploding. Research distinguishes individual factors (coping, resilience) from structural ones (staffing, autonomy, leadership, electronic health record burden). Magnet hospital research (Aiken, McHugh) shows organizational features predict both burnout and outcomes. But causal evidence for specific interventions is thin: most burnout trials are small, short, and measure self-report rather than turnover. As of 2026 the structural drivers are mapped but largely unaddressed.",
 "why_it_matters": "Burnout empties the profession: experienced nurses leave, novices inherit impossible loads, patients suffer. The global nursing shortage means every burned-out nurse who quits deepens the crisis for those who remain - a vicious cycle needing a structural exit.",
 "sig_pointer": "The Signature system's proposed approach treats burnout as a resource-depletion process with measurable early markers, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that burnout is a depletion process with stages - and that interventions fail because they target the wrong stage: resilience training treats late-stage depletion as an individual deficit while the cause is structural drain. "
  "Assumptions: (1) burnout progresses through detectable stages from engagement erosion to exhaustion to exit; (2) structural factors (load, autonomy, recognition) dominate individual ones; (3) early stages are reversible by structural change, late stages only by exit and recovery. "
  "Reasoning path: a staged depletion model explains why individual interventions underperform (wrong stage, wrong target) and why magnet hospitals succeed (structural features at every stage). "
  "Proposed mechanism: a 'depletion staging' instrument that locates each nurse and unit on the trajectory, directing structural interventions to the stage where they can still work. "
  "What would confirm it: staged structural interventions reducing turnover beyond generic wellness programs, with stage markers predicting who benefits. "
  "What would kill it: evidence that burnout is dominated by individual vulnerability regardless of structure, or that stages cannot be distinguished prospectively. "
  "What this does not claim: it does not claim burnout is any individual's fault, prescribes no program, and does not constitute clinical or management advice."),
 "sig_lens": "The Signature lens reads burnout as staged resource depletion, and asks what would catch each nurse at the stage where help still works.",
 "how_it_works": "Researchers study burnout through longitudinal workforce cohorts, Maslach inventory surveys, magnet-hospital comparisons, intervention trials, and turnover linkage studies.",
 "key_points": [
  "Burnout comprises emotional exhaustion, depersonalization, reduced efficacy (Maslach).",
  "Nurse burnout predicts turnover, errors, and patient mortality.",
  "The pandemic produced the worst nursing workforce crisis in modern history.",
  "Magnet hospitals show organizational features predict burnout and outcomes.",
  "Most intervention trials are small, short, and measure self-report.",
 ],
 "requirements": [
  "A staged model distinguishing reversible from late-stage burnout.",
  "Structural interventions proven against turnover, not just self-report.",
  "Evidence on which organizational features matter most.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Maslach C, Jackson SE. The measurement of experienced burnout. Journal of Occupational Behaviour. 1981;2:99-113.",
  "Aiken LH et al. Hospital nurse staffing and patient mortality, nurse burnout, and job dissatisfaction. JAMA. 2002;288(16):1987-1993.",
  "McHugh MD et al. Better nurse staffing and nurse work environments associated with increased survival. Medical Care. 2016;54(1):14-20.",
  "National Academies. Taking Action Against Clinician Burnout. Washington, DC: NAP; 2019.",
 ],
 "demo_data": {"a": ("nurses reporting burnout symptoms, percent (pandemic peak surveys, approx)", 60.0),
               "b": ("percent scale", 100.0), "bounds": (0.4, 0.8),
               "step1": "at the pandemic peak, most nurses reported burnout symptoms - a structural signal",
               "confirm": "staged structural interventions cut turnover beyond generic wellness programs",
               "refute": "burnout proves dominated by individual vulnerability regardless of structure"},
},
# ------------------------------------------------------------------ rank 5
{
 "key": "med-errors",
 "name": "Medication Administration Error Prevention",
 "group": "Patient Safety",
 "ladder_rank": 5, "ladder_tier": "foundations",
 "problem": "Nurses administer most hospital medications, and errors remain stubbornly common - why do smart, careful nurses make medication errors, and what system would make them rare?",
 "description": "Medication administration errors - wrong drug, dose, patient, time, or route - are among the commonest preventable harms in hospitals, implicated in thousands of deaths yearly. Nurses are the last line of defense and also the sharp end: interruptions, look-alike packaging, confusing orders, and fatigue conspire. Barcode medication administration (BCMA) and smart pumps cut some error types but introduced workarounds and new failure modes.",
 "background": "The 'five rights' (right patient, drug, dose, time, route) framed the problem individually for decades. Systems thinking (Reason, Leape, the 1999 'To Err Is Human' report) reframed errors as system outputs. Technology followed: computerized prescriber order entry cut prescribing errors; BCMA (Poon et al., NEJM 2010) cut administration errors substantially; smart infusion pumps added dose-error reduction. But each technology created workarounds - nurses bypass scanning when it slows emergencies - and the residual error rate persists. Second-victim research shows errors also wound the nurses who make them. As of 2026 the system is safer but errors remain common and workarounds are endemic.",
 "why_it_matters": "Medication errors injure the patients nurses most want to protect and traumatize the nurses involved. A system that made errors structurally rare - rather than relying on vigilance - would be among the highest-value safety advances in nursing.",
 "sig_pointer": "The Signature system's proposed approach treats errors as the output of interruption-shaped work, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that medication errors are shaped less by knowledge than by interruption: the med pass is a fragile cognitive sequence, and each interruption forces a restart that invites slips. "
  "Assumptions: (1) most administration errors are slips in well-understood sequences, not knowledge gaps; (2) interruption frequency predicts error rate; (3) technology that adds steps without protecting the sequence increases workaround-driven risk. "
  "Reasoning path: an interruption model explains why BCMA helps (it hardens the sequence) yet workarounds persist (it lengthens the sequence under time pressure) - the design target is sequence protection, not more checks. "
  "Proposed mechanism: 'sequence-protecting' medication workflow design that minimizes interruptions during the med pass and makes the safe path the fastest path, measured against error and workaround rates. "
  "What would confirm it: redesigned workflows cutting both errors and workarounds in trials, with interruption counts mediating the effect. "
  "What would kill it: evidence that errors are dominated by knowledge gaps or that interruption reduction does not move error rates. "
  "What this does not claim: it does not claim errors are currently preventable, blames no nurse, and does not constitute clinical advice."),
 "sig_lens": "The Signature lens reads the medication pass as a fragile sequence under siege by interruption, and asks what would protect the sequence.",
 "how_it_works": "Safety researchers study med errors through direct-observation studies, BCMA workaround ethnography, interruption research, incident-report analysis, and human-factors workflow redesign trials.",
 "key_points": [
  "Medication errors are among the commonest preventable hospital harms.",
  "The 'five rights' framed errors individually; systems thinking reframed them.",
  "'To Err Is Human' (1999) made medication safety a national priority.",
  "BCMA cut errors (Poon 2010) but introduced workarounds.",
  "Errors wound nurses too - the 'second victim' phenomenon.",
 ],
 "requirements": [
  "Workflow designs that protect the medication sequence from interruption.",
  "Technology where the safe path is the fastest path.",
  "Error measurement that captures workarounds, not just reported events.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Institute of Medicine. To Err Is Human. Washington, DC: NAP; 1999.",
  "Poon EG et al. Effect of bar-code technology on the safety of medication administration. New England Journal of Medicine. 2010;362:1698-1707.",
  "Reason J. Human error: models and management. BMJ. 2000;320:768-770.",
  "Keers RN et al. Causes of medication administration errors in hospitals. Drug Safety. 2013;36:1045-1067.",
 ],
 "demo_data": {"a": ("medication administrations per nurse per shift (typical, approx)", 30.0),
               "b": ("interruptions per med pass (observed, approx)", 3.0), "bounds": (5.0, 20.0),
               "step1": "a nurse may administer dozens of medications while interrupted repeatedly - the sequence never rests",
               "confirm": "redesigned workflows cut errors and workarounds with interruptions mediating the effect",
               "refute": "errors prove dominated by knowledge gaps with interruption reduction changing nothing"},
},
# ------------------------------------------------------------------ rank 6
{
 "key": "handoffs",
 "name": "Handoff Communication Failures",
 "group": "Patient Safety",
 "ladder_rank": 6, "ladder_tier": "foundations",
 "problem": "Patients are most vulnerable when their care changes hands - why do handoffs keep losing critical information, and what makes one stick?",
 "description": "Handoffs - shift changes, unit transfers, discharge - are discontinuity points where information degrades: the Joint Commission has long attributed a large share of sentinel events to communication failures. Structured tools (SBAR, I-PASS) help, and the I-PASS trial (Starmer et al., NEJM 2014) cut preventable adverse events by 23%. Yet handoffs still fail daily, especially across settings (hospital to home) where no shared tool exists.",
 "background": "Aviation's crew-resource-management inspired healthcare handoff work in the 2000s. SBAR (Situation, Background, Assessment, Recommendation) spread via the IHI; I-PASS (Illness severity, Patient summary, Action list, Situation awareness, Synthesis) was validated in the landmark 2014 multi-site trial showing real harm reduction. But adoption is uneven, night and weekend handoffs remain thinner, and the hospital-to-home handoff - discharge - is the least standardized and most consequential, driving readmissions. Electronic handoff tools promise continuity but often become copy-paste repositories. As of 2026 the structured handoff works where implemented, and implementation remains the problem.",
 "why_it_matters": "Every patient experiences handoffs; every handoff is a chance to lose the thread that keeps them safe. The discharge handoff alone drives a large share of readmissions. Making handoffs reliable is among the cheapest high-yield safety interventions available.",
 "sig_pointer": "The Signature system's proposed approach treats handoffs as knowledge transfer with a verification loop, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that handoffs fail on verification, not transmission: the sender speaks, the receiver nods, and neither confirms the mental model transferred - which is why structured tools help (they standardize content) but still leak (they don't verify receipt). "
  "Assumptions: (1) the failure mode is unverified transfer, not missing content; (2) receivers construct incomplete mental models under time pressure; (3) a brief verification loop catches most gaps. "
  "Reasoning path: a verification model explains why I-PASS's 'synthesis by receiver' element may be its active ingredient and predicts that adding verification to any handoff tool will outperform content standardization alone. "
  "Proposed mechanism: 'verified handoffs' requiring receiver synthesis plus sender confirmation of the synthesis, embedded in existing tools, measured against information-loss audits and adverse events. "
  "What would confirm it: verified handoffs outperforming standard structured handoffs in trials, with synthesis accuracy predicting safety. "
  "What would kill it: evidence that content standardization captures all the benefit, or that verification loops cost more time than they save in safety. "
  "What this does not claim: it does not claim a tool ready for units, prescribes no protocol, and does not constitute clinical advice."),
 "sig_lens": "The Signature lens reads the handoff as a transfer awaiting confirmation, and asks what verification loop would close it.",
 "how_it_works": "Researchers study handoffs through direct observation, information-loss audits, I-PASS implementation trials, discharge communication studies, and readmission linkage.",
 "key_points": [
  "Communication failures contribute to a large share of sentinel events.",
  "I-PASS cut preventable adverse events 23% in a multi-site trial (2014).",
  "SBAR standardized content; verification of receipt remains the gap.",
  "Discharge - the hospital-to-home handoff - is least standardized.",
  "Electronic handoff tools risk becoming copy-paste repositories.",
 ],
 "requirements": [
  "Handoff designs with built-in verification loops.",
  "Standardization of the discharge handoff across settings.",
  "Measurement of information loss, not just tool use.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Starmer AJ et al. Changes in medical errors after implementation of a handoff program (I-PASS). New England Journal of Medicine. 2014;371:1948-1955.",
  "The Joint Commission. Sentinel event data on communication failures. Various.",
  "Friesen MA et al. Handoffs: implications for nurses. In: Patient Safety and Quality. AHRQ; 2008.",
  "Kripalani S et al. Deficits in communication and information transfer between hospital-based and primary care physicians. JAMA. 2007;297(8):831-841.",
 ],
 "demo_data": {"a": ("preventable adverse events cut by I-PASS, percent", 23.0),
               "b": ("percent scale", 100.0), "bounds": (0.15, 0.35),
               "step1": "a structured handoff cut preventable harm by nearly a quarter - communication is treatment",
               "confirm": "verified handoffs beat standard structured handoffs with synthesis accuracy predicting safety",
               "refute": "content standardization proves to capture all handoff benefit with verification adding nothing"},
},
# ------------------------------------------------------------------ rank 7
{
 "key": "nonverbal-pain",
 "name": "Pain Assessment in Nonverbal Patients",
 "group": "Assessment",
 "ladder_rank": 7, "ladder_tier": "foundations",
 "problem": "Pain is what the patient says it is - but what about patients who cannot speak? How can nurses reliably assess pain in the nonverbal?",
 "description": "Self-report is the gold standard for pain, which excludes infants, the severely cognitively impaired, the intubated, and advanced dementia patients - exactly those at high risk of unrelieved pain. Behavioral scales exist (FLACC for children, PAINAD for dementia, CPOT/BPS for critical care), but they infer pain from agitation, grimacing, and vital signs - all confounded by delirium, fear, and illness itself. Under-treatment and over-sedation both follow.",
 "background": "The undertreatment of pain in nonverbal populations was documented from the 1980s (Anand's work showing neonates feel pain and benefit from analgesia). Behavioral scales proliferated: FLACC (1997), PAINAD (2003), CPOT (2006), each validated against situations assumed painful. But validation is circular - there is no ground truth to validate against - and interrater reliability is modest. Physiologic approaches (pupillometry, skin conductance, EEG signatures, AI facial analysis) promise objectivity but remain research tools. As of 2026 no method reliably measures pain in those who cannot report it.",
 "why_it_matters": "Unrelieved pain in the voiceless is a silent epidemic: neonates undergoing procedures, dementia patients with fractures, intubated ICU patients. And over-sedation from guessing wrong carries its own harms. An objective measure would end the guessing.",
 "sig_pointer": "The Signature system's proposed approach treats pain as a pattern across multiple weak signals, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that no single signal measures nonverbal pain, but the pattern across many weak signals does: behavior, physiology, and context each carry partial information, and their convergence is the measure. "
  "Assumptions: (1) pain produces a characteristic multi-signal pattern distinct from fear, delirium, and hunger; (2) the pattern is learnable from situations with known pain states; (3) individual baselines matter - deviation, not absolute value. "
  "Reasoning path: a convergence model explains why single scales underperform (each captures one slice) and predicts that fused multi-signal assessment will outperform any single scale. "
  "Proposed mechanism: a 'pain convergence' assessment fusing behavioral, physiologic, and contextual signals against personal baselines, validated in known-pain versus known-comfort situations. "
  "What would confirm it: fused assessment outperforming the best single scale on discrimination in validation studies. "
  "What would kill it: evidence that the signals carry no pain-specific information beyond arousal, or that convergence adds nothing to the best single scale. "
  "What this does not claim: it does not claim a device ready for bedsides, does not recommend analgesic decisions, and does not constitute clinical advice."),
 "sig_lens": "The Signature lens reads voiceless pain as a pattern hiding across weak signals, and asks what fusion would make it legible.",
 "how_it_works": "Researchers study nonverbal pain through behavioral scale validation, physiologic signal research (pupillometry, EEG, skin conductance), facial-action AI, and analgesic-trial response as a proxy ground truth.",
 "key_points": [
  "Self-report is the gold standard, excluding the most vulnerable patients.",
  "FLACC, PAINAD, CPOT/BPS infer pain from behavior - all confounded.",
  "Validation is circular: no ground truth exists for nonverbal pain.",
  "Anand's neonatal work proved the voiceless feel pain and need analgesia.",
  "Pupillometry, EEG, and facial AI remain research tools.",
 ],
 "requirements": [
  "A multi-signal measure validated against known pain states.",
  "Proof that fused signals beat the best single scale.",
  "Bedside practicality for routine nursing assessment.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Anand KJS, Hickey PR. Pain and its effects in the human neonate and fetus. New England Journal of Medicine. 1987;317:1321-1329.",
  "Merkel SI et al. The FLACC: a behavioral scale for scoring postoperative pain in young children. Pediatric Nursing. 1997;23(3):293-297.",
  "Warden V et al. The PAINAD scale. Journal of the American Medical Directors Association. 2003;4(1):9-15.",
  "Gelinas C et al. Validation of the critical-care pain observation tool in adult patients. American Journal of Critical Care. 2006;15(4):420-427.",
 ],
 "demo_data": {"a": ("behavioral pain scales in common use (FLACC, PAINAD, CPOT, BPS)", 4.0),
               "b": ("objective pain measures validated for nonverbal patients", 0.5), "bounds": (4.0, 16.0),
               "step1": "four behavioral scales compete while zero objective measures exist - the gap is total",
               "confirm": "fused multi-signal assessment beats the best single scale in validation studies",
               "refute": "the signals prove to carry no pain-specific information beyond general arousal"},
},
# ------------------------------------------------------------------ rank 8
{
 "key": "delirium-prevention",
 "name": "Delirium Prevention in Hospitalized Elderly",
 "group": "Geriatric Nursing",
 "ladder_rank": 8, "ladder_tier": "foundations",
 "problem": "Delirium strikes hospitalized elders, prolongs stays, and predicts dementia - why do prevention programs work in trials but fade in practice?",
 "description": "Delirium - acute confusion and inattention - affects up to half of elderly inpatients and is associated with longer stays, institutionalization, and death. The Hospital Elder Life Program (HELP, Inouye 1990s) proved multicomponent prevention works: orientation, mobilization, hydration, sleep, vision/hearing optimization. Yet HELP and its descendants struggle to survive in routine practice: they need dedicated staff, and hospitals fund them until budgets tighten.",
 "background": "Inouye's HELP trials (1999, Annals of Internal Medicine) showed delirium incidence could be cut by targeting six risk factors with protocols delivered by trained staff and volunteers. The Confusion Assessment Method (1990) gave delirium a bedside definition. Implementation science then documented the fade: programs work where funded, wither where not. Pharmacologic prevention (antipsychotics, melatonin, dexmedetomidine) shows modest or inconsistent effects; the 2019 NICE-influenced guidance emphasizes non-pharmacologic care. As of 2026 the effective intervention exists but the sustainable delivery model does not.",
 "why_it_matters": "Delirium is the commonest complication of hospitalization in the elderly and a pipeline to dementia and nursing homes. A prevention model that survives contact with real budgets would protect millions of aging patients.",
 "sig_pointer": "The Signature system's proposed approach treats delirium prevention as ambient care design rather than a program, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that delirium prevention fails in practice because it is organized as a program - extra people doing extra tasks - instead of as the ambient design of the unit itself. "
  "Assumptions: (1) HELP's components work; the failure is delivery economics; (2) ambient design (light, noise, mobilization cues, orientation architecture) delivers the components without dedicated staff; (3) nurses will sustain what is built into workflow, not what is added to it. "
  "Reasoning path: reframing prevention as environment design explains the trial-practice gap - trials fund programs, practice cannot - and predicts that units redesigned for delirium prevention will sustain gains without ongoing program budgets. "
  "Proposed mechanism: 'delirium-proof' unit design standards - circadian lighting, noise control, mobilization architecture, orientation cues - evaluated against delirium incidence like a drug trial. "
  "What would confirm it: redesigned units sustaining delirium reductions without dedicated program staff. "
  "What would kill it: evidence that the active ingredient is human attention (which design cannot replace), or that ambient changes move no outcomes. "
  "What this does not claim: it does not claim design replaces nursing care, prescribes no program, and does not constitute clinical advice."),
 "sig_lens": "The Signature lens reads delirium prevention as an environment problem wearing a program costume, and asks what unit design would prevent by default.",
 "how_it_works": "Geriatric nurse researchers study delirium through HELP trials, implementation studies, ambient intervention trials (light, noise, mobilization), and pharmacologic prevention trials.",
 "key_points": [
  "Delirium affects up to half of elderly inpatients.",
  "HELP proved multicomponent non-pharmacologic prevention works (Inouye 1999).",
  "Programs fade when dedicated funding ends - the implementation gap.",
  "Drugs prevent delirium modestly at best; guidelines emphasize non-pharmacologic care.",
  "Delirium predicts institutionalization, dementia, and death.",
 ],
 "requirements": [
  "A delivery model that survives without dedicated program budgets.",
  "Proof that ambient design prevents delirium as well as staffed programs.",
  "Equity: prevention that reaches non-academic, under-resourced hospitals.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Inouye SK et al. A multicomponent intervention to prevent delirium in hospitalized older patients. New England Journal of Medicine. 1999;340:669-676.",
  "Inouye SK et al. Clarifying confusion: the confusion assessment method. Annals of Internal Medicine. 1990;113(12):941-948.",
  "Hshieh TT et al. Effectiveness of multicomponent nonpharmacological delirium interventions. JAMA Internal Medicine. 2015;175(4):512-520.",
  "National Institute for Health and Care Excellence. Delirium: prevention, diagnosis and management. NG103; 2019.",
 ],
 "demo_data": {"a": ("delirium incidence cut by HELP, percent (approx)", 40.0),
               "b": ("percent scale", 100.0), "bounds": (0.3, 0.5),
               "step1": "prevention can cut delirium by nearly half - where the program survives",
               "confirm": "redesigned units sustain delirium cuts without dedicated program staff",
               "refute": "the active ingredient proves to be human attention that design cannot replace"},
},
# ------------------------------------------------------------------ rank 9
{
 "key": "fall-prevention",
 "name": "Fall Prevention in Hospitals",
 "group": "Patient Safety",
 "ladder_rank": 9, "ladder_tier": "foundations",
 "problem": "Hospital falls injure patients and are deemed preventable - yet decades of alarms, sitters, and assessments have not eliminated them. What actually stops a fall?",
 "description": "Falls are the commonest adverse event in hospitals: hundreds of thousands yearly in the US, a fraction causing fracture, head injury, or death. Prevention rests on risk assessment (Morse, Hendrich II), bed/chair alarms, sitters, and hourly rounding. Yet falls persist - and the cruelest finding is that alarms often don't prevent falls, they just announce them; restraints reduce falls but are unethical and illegal in most settings.",
 "background": "Fall prevention became a regulatory priority in the 2000s (CMS stopped paying for fall-related injuries in 2008). Research showed risk scales predict poorly - most fallers were already flagged high-risk - and that universal precautions may beat targeted ones. Bed alarms proliferated despite weak evidence; sitters are effective but expensive and in short supply. The most honest finding: toileting-related falls dominate, implicating the basic mismatch between patient need and nurse availability. As of 2026 falls remain common, alarms remain ubiquitous, and the evidence base remains thin.",
 "why_it_matters": "A fall can turn a recoverable admission into a hip fracture, a head bleed, or a death - and 'preventable' falls carry moral and financial weight. Solving falls means solving the availability gap at the bedside.",
 "sig_pointer": "The Signature system's proposed approach treats falls as an availability problem with a toileting core, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that hospital falls are fundamentally a response-time problem: most falls happen when patients need the toilet and help does not come fast enough, so they go alone. "
  "Assumptions: (1) toileting urgency drives the majority of inpatient falls; (2) the causal chain is need-recognition delay plus response delay; (3) alarms fail because they detect the fall's beginning, not the need's beginning. "
  "Reasoning path: an availability model explains why risk scales underperform (they predict who, not when) and why sitters work (they collapse response time) - the target is need-to-help latency. "
  "Proposed mechanism: 'need-anticipating' rounding driven by toileting patterns and mobility data, plus latency measurement as the quality metric, tested against fall rates. "
  "What would confirm it: latency-targeted protocols outperforming alarm-based ones in trials, with response-time data mediating the effect. "
  "What would kill it: evidence that falls are dominated by intrinsic patient factors (syncope, weakness) regardless of response time. "
  "What this does not claim: it does not claim falls are currently preventable, prescribes no protocol, and does not constitute clinical advice."),
 "sig_lens": "The Signature lens reads the fall as a race between a full bladder and a busy nurse, and asks what would shorten the nurse's arrival.",
 "how_it_works": "Researchers study falls through incident analysis, alarm-effectiveness trials, sitter studies, rounding trials, and risk-scale validation.",
 "key_points": [
  "Falls are the commonest adverse event in hospitals.",
  "CMS stopped paying for fall injuries in 2008.",
  "Risk scales predict poorly; most fallers were already flagged.",
  "Bed alarms announce falls more than they prevent them.",
  "Toileting-related falls dominate the incident reports.",
 ],
 "requirements": [
  "Proof of what actually prevents falls, not just what predicts them.",
  "A response-time metric for toileting need.",
  "Prevention that works without restraints or one-to-one sitters.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Oliver D et al. Strategies to prevent falls and fractures in hospitals and care homes. BMJ. 2007;334:82-85.",
  "Hempel S et al. Review of the evidence on falls prevention in hospitals. JAMA Internal Medicine. 2013;173(7):483-492.",
  "Morse JM et al. Development of a scale to identify the fall-prone patient. Canadian Journal on Aging. 1989;8(4):366-377.",
  "Centers for Medicare and Medicaid Services. Hospital-acquired conditions policy; 2008.",
 ],
 "demo_data": {"a": ("US hospital falls per year, approximate thousands", 800.0),
               "b": ("thousands scale", 1000.0), "bounds": (0.5, 1.2),
               "step1": "nearly a million hospital falls yearly - the commonest adverse event",
               "confirm": "latency-targeted protocols beat alarm-based ones with response times mediating the effect",
               "refute": "falls prove dominated by intrinsic patient factors regardless of response time"},
},
# ------------------------------------------------------------------ rank 10
{
 "key": "adherence",
 "name": "Patient Adherence Mechanisms",
 "group": "Chronic Care",
 "ladder_rank": 10, "ladder_tier": "foundations",
 "problem": "Half of chronic-disease medications go untaken - why do patients not follow regimens they agreed to, and what actually changes behavior?",
 "description": "Medication non-adherence in chronic disease averages around 50%, driving treatment failures, hospitalizations, and billions in costs. The reasons are manifold: cost, side effects, complexity, forgetfulness, disbelief in the diagnosis, depression. Interventions - education, reminders, pill organizers, motivational interviewing - show small average effects that fade. Nurses do most adherence counseling, yet the science of what changes adherence remains primitive.",
 "background": "The adherence problem was quantified in the 1970s-90s (Sackett, Haynes); the WHO's 2003 report declared improving adherence would outperform any new drug. Research cycled through explanations: knowledge deficits (disproven - informed patients still don't adhere), then behavioral economics (present bias, defaults), then the recognition that adherence is a behavior embedded in life circumstances. Single interventions show small effects; multicomponent ones do better but are hard to scale. Digital adherence tools (smart bottles, ingestible sensors like Abilify MyCite) promise measurement but not behavior change. As of 2026 no intervention reliably produces large, durable adherence gains.",
 "why_it_matters": "Non-adherence wastes the entire medical enterprise: perfect drugs, perfect diagnoses, unused. Nurses counsel adherence daily with weak tools. Cracking adherence would improve outcomes more than most new pharmaceuticals.",
 "sig_pointer": "The Signature system's proposed approach treats adherence as friction to be designed away, not motivation to be supplied, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that adherence fails on friction, not motivation: each dose is a small task competing with life, and regimens accumulate friction until behavior collaps as a rational response to cost. "
  "Assumptions: (1) most non-adherence is passive (forgetting, complexity, cost) not active refusal; (2) friction is measurable per regimen; (3) reducing friction beats increasing motivation. "
  "Reasoning path: a friction model explains why education underperforms (it adds motivation to a friction problem) and why simplification and defaults outperform reminders. "
  "Proposed mechanism: 'friction auditing' of regimens - measuring and minimizing the daily behavioral cost of each prescription - tested against adherence and outcomes. "
  "What would confirm it: friction-reduced regimens outperforming motivation-based counseling in trials, with friction scores predicting adherence. "
  "What would kill it: evidence that non-adherence is dominated by active belief-based refusal, or that friction reduction does not move behavior. "
  "What this does not claim: it does not claim patients should take drugs they judge harmful, prescribes no counseling method, and does not constitute clinical advice."),
 "sig_lens": "The Signature lens reads the untaken pill as friction winning over intention, and asks what regimen design would make taking it effortless.",
 "how_it_works": "Researchers study adherence through electronic monitoring, claims-based refill analyses, behavioral trials, qualitative work on patient reasoning, and digital-tool evaluations.",
 "key_points": [
  "Chronic-disease medication adherence averages ~50%.",
  "WHO (2003): improving adherence would outperform any new drug.",
  "Knowledge deficits don't explain it - informed patients still don't adhere.",
  "Single interventions show small, fading effects.",
  "Digital tools measure adherence better than they change it.",
 ],
 "requirements": [
  "A measurable friction model of regimen burden.",
  "Interventions with large, durable effects on behavior.",
  "Respect for informed refusal as distinct from passive non-adherence.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "World Health Organization. Adherence to Long-Term Therapies: Evidence for Action. Geneva: WHO; 2003.",
  "Haynes RB et al. Interventions for helping patients to follow prescriptions. Cochrane Database of Systematic Reviews. 2008;2:CD000011.",
  "Osterberg L, Blaschke T. Adherence to medication. New England Journal of Medicine. 2005;353:487-497.",
  "Nieuwlaat R et al. Interventions for enhancing medication adherence. Cochrane Database of Systematic Reviews. 2014;11:CD000011.",
 ],
 "demo_data": {"a": ("chronic-disease medications untaken, percent (approx)", 50.0),
               "b": ("percent scale", 100.0), "bounds": (0.3, 0.7),
               "step1": "half of chronic-disease medications go untaken - the system's largest leak",
               "confirm": "friction-reduced regimens beat motivation-based counseling with friction scores predicting adherence",
               "refute": "non-adherence proves dominated by active belief-based refusal"},
},
# ------------------------------------------------------------------ rank 11
{
 "key": "moral-distress",
 "name": "Moral Distress in Nurses",
 "group": "Workforce",
 "ladder_rank": 11, "ladder_tier": "foundations",
 "problem": "Nurses often know the right thing but cannot do it - what is moral distress, and why does it drive good nurses out of the profession?",
 "description": "Moral distress - Jameton's 1984 concept - is the anguish of knowing the ethically right action while institutional constraints block it: futile care demanded by families, unsafe staffing accepted by management, pain undertreated by policy. It predicts burnout and exit, yet it is routinely mislabeled as burnout and treated with resilience programs that miss the point: the nurse is not broken, the situation is.",
 "background": "Jameton defined moral distress in 1984; Corley's measurement scale (2001) made it researchable. Studies linked it to futile-care situations, short staffing, and hierarchical silencing. The pandemic intensified it: crisis standards, visitation bans nurses had to enforce, resource triage. Interventions - ethics rounds, moral-distress debriefing, structural empowerment - show promise but are rarely systematic. The conceptual frontier distinguishes moral distress (blocked right action) from moral injury (participation in wrong action), borrowed from military psychiatry. As of 2026 moral distress is measured but rarely addressed structurally.",
 "why_it_matters": "Moral distress selects against conscience: the nurses who feel it most are often the best, and they leave. Addressing it structurally would retain exactly the nurses the profession cannot afford to lose.",
 "sig_pointer": "The Signature system's proposed approach treats moral distress as a signal about the institution, not the nurse, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that moral distress is an organizational diagnostic: its patterns reveal where institutional constraints systematically block right action, and aggregating it maps the institution's ethical failure points. "
  "Assumptions: (1) distress episodes cluster at specific constraint types; (2) nurses can report constraints reliably; (3) removing the constraint resolves the distress (unlike burnout, which lingers). "
  "Reasoning path: treating distress as signal reframes the response from supporting the nurse to fixing the constraint - explaining why resilience programs fail it and predicting that constraint-removal will outperform counseling. "
  "Proposed mechanism: 'moral-distress surveillance' that aggregates episodes into constraint maps, directing leadership to remove the top blockers, measured against distress scores and retention. "
  "What would confirm it: constraint-removal outperforming resilience programs on distress and retention in trials. "
  "What would kill it: evidence that distress is dominated by individual sensitivity regardless of constraints, or that constraint maps do not predict distress. "
  "What this does not claim: it does not claim any constraint should be removed, prescribes no policy, and does not constitute clinical advice."),
 "sig_lens": "The Signature lens reads moral distress as the institution's conscience speaking through its nurses, and asks what the signal is pointing at.",
 "how_it_works": "Researchers study moral distress through Corley's scale surveys, qualitative work on constraint types, ethics-intervention trials, and linkage to turnover.",
 "key_points": [
  "Jameton defined moral distress in 1984; Corley made it measurable in 2001.",
  "It is the anguish of blocked right action - distinct from burnout.",
  "Futile care, unsafe staffing, and hierarchical silencing are top triggers.",
  "It predicts exit; resilience programs misdiagnose it.",
  "Moral injury (participation in wrong action) is the deeper frontier concept.",
 ],
 "requirements": [
  "Surveillance that maps constraints, not just scores distress.",
  "Structural interventions proven against distress and retention.",
  "Distinction of distress from injury in measurement and response.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Jameton A. Nursing Practice: The Ethical Issues. Englewood Cliffs: Prentice-Hall; 1984.",
  "Corley MC et al. Development and evaluation of a moral distress scale. Journal of Advanced Nursing. 2001;33(2):250-256.",
  "Epstein EG, Hamric AB. Moral distress, moral residue, and the crescendo effect. Journal of Clinical Ethics. 2009;20(4):330-342.",
  "Rushton CH et al. Moral distress: a catalyst for action. American Journal of Nursing. 2017;117(2):52-56.",
 ],
 "demo_data": {"a": ("years since Jameton defined moral distress (1984)", 42.0),
               "b": ("decades scale", 10.0), "bounds": (3.5, 5.0),
               "step1": "four decades after naming it, the profession still treats the signal as the nurse's problem",
               "confirm": "constraint-removal beats resilience programs on distress and retention",
               "refute": "distress proves dominated by individual sensitivity regardless of constraints"},
},
# ------------------------------------------------------------------ rank 12
{
 "key": "alarm-fatigue",
 "name": "Alarm Fatigue",
 "group": "Technology",
 "ladder_rank": 12, "ladder_tier": "compounded",
 "problem": "Monitors alarm hundreds of times per shift, almost all falsely - why do nurses stop hearing them, and what would make alarms trustworthy?",
 "description": "Physiologic monitors generate hundreds of alarms per patient per day; studies find 85-99% are false or clinically insignificant. Nurses habituate - alarm fatigue - and true alarms get missed: the Joint Commission made alarm safety a National Patient Safety Goal after deaths from missed alarms. The engineering irony: monitors are designed to never miss, which guarantees they cry wolf.",
 "background": "Alarm fatigue was characterized in the 2000s-2010s (Cvach's Johns Hopkins work showed alarm burden and the effect of alarm-management interventions). The Joint Commission's 2013-2014 sentinel alerts on alarm-related deaths forced action. Technical responses: alarm-delay algorithms, smart alarm integration, middleware that routes alarms to the right nurse's phone. But the sensitivity-specificity trade-off is fundamental: no threshold catches every true event without false ones, and liability fears push manufacturers toward sensitivity. As of 2026 alarm burden is reduced in showcase units but endemic elsewhere.",
 "why_it_matters": "Missed true alarms kill; false alarms exhaust nurses and desensitize the very vigilance monitors are meant to support. Trustworthy alarming would restore the monitor as a safety net instead of background noise.",
 "sig_pointer": "The Signature system's proposed approach treats alarming as a signal-detection problem to be personalized, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that alarms fail because thresholds are population-set while physiology is personal: the same heart-rate limit is simultaneously too lax for one patient and too strict for another, guaranteeing both misses and wolf-cries. "
  "Assumptions: (1) each patient's normal range is learnable; (2) the clinically meaningful event is deviation from personal normal, not threshold crossing; (3) nurses trust alarms they have seen be right. "
  "Reasoning path: personalization reframes the sensitivity-specificity trade-off - the trade-off is harsh for populations but mild for individuals - explaining why default limits fail everywhere. "
  "Proposed mechanism: 'personal alarm envelopes' learned per patient in the first hours, with deviation-based alarming and nurse-validated true events as training signal. "
  "What would confirm it: personalized alarming cutting false alarms while preserving or improving true-event capture in trials. "
  "What would kill it: evidence that true events lack personal prodromes, or that personalization cannot be learned fast enough in short stays. "
  "What this does not claim: it does not claim a monitor ready for units, does not recommend changing alarm settings, and does not constitute clinical advice."),
 "sig_lens": "The Signature lens reads the alarm as a population threshold shouting at personal physiology, and asks what personal envelope would earn trust.",
 "how_it_works": "Researchers study alarm fatigue through alarm-burden audits, intervention trials (delays, middleware, smart alarms), human-factors studies of response, and sentinel-event analyses.",
 "key_points": [
  "85-99% of physiologic alarms are false or clinically insignificant.",
  "Alarm fatigue contributed to deaths; the Joint Commission made it a safety goal.",
  "Cvach's Johns Hopkins work quantified burden and management effects.",
  "The sensitivity-specificity trade-off is fundamental to threshold alarming.",
  "Liability fears push manufacturers toward sensitivity - more false alarms.",
 ],
 "requirements": [
  "Alarming based on personal deviation, not population thresholds.",
  "Proof that false-alarm reduction preserves true-event capture.",
  "Alarm designs nurses trust enough to answer.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Cvach M. Monitor alarm fatigue: an integrative review. Biomedical Instrumentation and Technology. 2012;46(4):268-277.",
  "The Joint Commission. Sentinel Event Alert 50: Medical device alarm safety in hospitals. 2013.",
  "Drew BJ et al. Insights into the problem of alarm fatigue. PLoS One. 2014;9(10):e110274.",
  "Sowan AK et al. Alarm fatigue and nursing. Various; 2015-2017.",
 ],
 "demo_data": {"a": ("false or insignificant alarms, percent (upper range)", 99.0),
               "b": ("percent scale", 100.0), "bounds": (0.85, 1.0),
               "step1": "up to ninety-nine percent of alarms are noise - the monitor cries wolf by design",
               "confirm": "personalized alarming cuts false alarms while preserving true-event capture",
               "refute": "true events prove to lack personal prodromes detectable in time"},
},
# ------------------------------------------------------------------ rank 13
{
 "key": "sepsis-recognition",
 "name": "Sepsis Early Recognition by Nurses",
 "group": "Acute Care",
 "ladder_rank": 13, "ladder_tier": "compounded",
 "problem": "Sepsis kills more hospital patients than any other condition, and every hour of delayed antibiotics raises mortality - why is early recognition still unreliable at the bedside?",
 "description": "Sepsis - life-threatening organ dysfunction from infection - affects tens of millions yearly and kills roughly one in five of its victims worldwide. The evidence is brutal on timing: each hour of antibiotic delay in septic shock raises mortality. Nurses are positioned to catch it first, armed with screening tools (qSOFA, SIRS, NEWS) and now AI alerts - yet recognition still fails, especially in the elderly and immunocompromised whose presentations are atypical.",
 "background": "The Surviving Sepsis Campaign (2004, updated regularly) bundled early recognition with timely antibiotics and fluids; Kumar's 2006 study quantified the hourly mortality cost of delay. Screening tools proliferated: SIRS was sensitive but nonspecific, qSOFA (Sepsis-3, 2016) was specific but insensitive, NEWS sits between. AI sepsis predictors (notably the Epic model, externally validated as poorly performing by Wong et al., JAMA Internal Medicine 2021) showed the gap between retrospective promise and prospective reality. Nurse-driven sepsis screening protocols help where implemented. As of 2026 no screening approach reliably catches sepsis early without drowning nurses in false alerts.",
 "why_it_matters": "Sepsis is the leading killer in hospitals and the most time-sensitive common emergency: recognition is the therapy's gatekeeper. Reliable early recognition would save more lives than any new sepsis drug.",
 "sig_pointer": "The Signature system's proposed approach treats sepsis as a host-response trajectory, not a threshold crossing, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that sepsis screens fail because they test for infection plus generic abnormality, while sepsis is specifically a dysregulated host response - and the dysregulation has a trajectory signature distinct from ordinary infection. "
  "Assumptions: (1) the host response to sepsis diverges from the response to uncomplicated infection early; (2) the divergence is visible in vital-sign and mentation trajectories before organ failure; (3) nurses sense the divergence tacitly ('the patient looks septic'). "
  "Reasoning path: a trajectory model explains why threshold screens underperform and why experienced nurses outperform them - the proposal formalizes the tacit pattern. "
  "Proposed mechanism: 'host-response trajectory' screening that tracks the shape of deterioration rather than threshold crossings, trained on nurse-validated sepsis cases. "
  "What would confirm it: trajectory screening beating qSOFA/NEWS on time-to-antibiotics in trials without alert fatigue. "
  "What would kill it: evidence that septic and non-septic infection trajectories are indistinguishable until organ failure. "
  "What this does not claim: it does not claim a screen ready for wards, does not recommend antibiotic timing, and does not constitute clinical advice."),
 "sig_lens": "The Signature lens reads sepsis as a host response going wrong in a recognizable shape, and asks what trajectory would reveal it first.",
 "how_it_works": "Researchers study sepsis recognition through screening-tool validation, AI alert trials, nurse intuition studies, biomarker research (lactate, procalcitonin), and bundle-compliance implementation science.",
 "key_points": [
  "Each hour of antibiotic delay in septic shock raises mortality measurably.",
  "Sepsis-3 (2016) redefined sepsis as dysregulated host response with organ dysfunction.",
  "qSOFA is specific but insensitive; SIRS sensitive but nonspecific.",
  "The Epic sepsis AI model performed poorly on external validation (2021).",
  "Atypical presentations in elderly and immunocompromised patients evade screens.",
 ],
 "requirements": [
  "Recognition based on host-response trajectories, not thresholds.",
  "Alerts accurate enough to act on without fatigue.",
  "Proof that faster recognition converts to survival, not just faster antibiotics.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Kumar A et al. Duration of hypotension before initiation of effective antimicrobial therapy is the critical determinant of survival in human septic shock. Critical Care Medicine. 2006;34(6):1589-1596.",
  "Singer M et al. The third international consensus definitions for sepsis and septic shock (Sepsis-3). JAMA. 2016;315(8):801-810.",
  "Wong A et al. External validation of a widely implemented proprietary sepsis prediction model. JAMA Internal Medicine. 2021;181(8):1065-1070.",
  "Rhodes A et al. Surviving Sepsis Campaign: international guidelines. Critical Care Medicine. 2017;45(3):486-552.",
 ],
 "demo_data": {"a": ("mortality rise per hour of antibiotic delay, percent (approx)", 8.0),
               "b": ("percent scale", 100.0), "bounds": (0.05, 0.12),
               "step1": "each hour of delay costs roughly eight percent more mortality - recognition is the therapy",
               "confirm": "trajectory screening beats threshold screens on time-to-antibiotics without fatigue",
               "refute": "septic and non-septic trajectories prove indistinguishable until organ failure"},
},
# ------------------------------------------------------------------ rank 14
{
 "key": "cauti",
 "name": "Catheter-Associated UTI Prevention",
 "group": "Infection Prevention",
 "ladder_rank": 14, "ladder_tier": "compounded",
 "problem": "Urinary catheters are indispensable and infection-prone - why do catheter-associated urinary tract infections persist despite decades of prevention bundles?",
 "description": "CAUTI is among the commonest healthcare-associated infections: bacteria ascend the catheter, form biofilm, and infect the bladder. Each catheter-day adds risk; catheters are often left in for convenience long after need passes. Prevention bundles - aseptic insertion, securement, closed drainage, daily necessity review, nurse-driven removal protocols - cut rates substantially, yet CAUTI persists, and asymptomatic bacteriuria is over-treated with antibiotics.",
 "background": "The pathogenesis (biofilm on the catheter surface, ascending infection) was mapped in the 1970s-80s. Saint's work showed a large fraction of catheters lack a documented indication. The key intervention proved to be removal: nurse-driven discontinuation protocols and electronic reminders cut catheter-days and infections (Meddings' systematic reviews). CMS non-payment for CAUTI (2008) drove attention. Antimicrobial catheters (silver, nitrofurazone) show modest benefit at cost. As of 2026 the residual CAUTI burden concentrates where catheters are truly necessary and cannot simply be removed - the unsolved core.",
 "why_it_matters": "CAUTI causes suffering, antibiotic use, longer stays, and occasional bacteremia and death - largely in patients catheterized for convenience. Eliminating the residual would remove one of the commonest preventable hospital infections.",
 "sig_pointer": "The Signature system's proposed approach treats the catheter as a temporary guest whose stay must be minimized and monitored, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that CAUTI prevention has two distinct problems with different solutions: unnecessary catheter-days (solved by removal) and necessary catheter-days (unsolved) - and that conflating them stalls progress on the second. "
  "Assumptions: (1) infection risk per catheter-day is roughly constant after the first days; (2) biofilm formation is inevitable on current materials within days; (3) the necessary-catheter population is identifiable. "
  "Reasoning path: separating the problems explains why removal protocols plateau - they solved problem one - and focuses innovation on problem two: materials and monitoring for catheters that must stay. "
  "Proposed mechanism: a two-track program - automated necessity review eliminating avoidable days, plus biofilm-resistant materials and early-bacteriuria sensing for necessary catheters. "
  "What would confirm it: two-track programs driving CAUTI below removal-protocol plateaus in trials. "
  "What would kill it: evidence that necessary-catheter CAUTI is irreducible with current materials, or that sensing adds nothing to scheduled changes. "
  "What this does not claim: it does not claim a catheter recommendation, does not advise removal timing, and does not constitute clinical advice."),
 "sig_lens": "The Signature lens reads the catheter as two problems - the avoidable days and the unavoidable ones - and asks what would solve the second.",
 "how_it_works": "Researchers study CAUTI through catheter-necessity audits, removal-protocol trials, antimicrobial catheter trials, biofilm materials science, and bacteriuria management studies.",
 "key_points": [
  "CAUTI risk rises with each catheter-day; biofilm forms within days.",
  "Many catheters lack a documented indication (Saint).",
  "Nurse-driven removal protocols cut catheter-days and infections.",
  "CMS non-payment (2008) drove prevention attention.",
  "Residual CAUTI concentrates in catheters that cannot be removed.",
 ],
 "requirements": [
  "Materials resisting biofilm for the necessary-catheter population.",
  "Early bacteriuria sensing that distinguishes colonization from infection.",
  "An end to treating asymptomatic bacteriuria with antibiotics.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Saint S et al. Urinary catheters: what type do men and their nurses prefer? Journal of the American Geriatrics Society. 1999;47(12):1453-1457.",
  "Meddings J et al. Systematic review of interventions to reduce urinary tract infection. BMJ Quality and Safety. 2014;23:277-289.",
  "Lo E et al. Strategies to prevent catheter-associated urinary tract infections in acute care hospitals. Infection Control and Hospital Epidemiology. 2014;35:464-479.",
  "Gould CV et al. Guideline for prevention of catheter-associated urinary tract infections. Infection Control and Hospital Epidemiology. 2010;31(4):319-326.",
 ],
 "demo_data": {"a": ("catheter-days cut by nurse-driven removal protocols, percent (approx)", 30.0),
               "b": ("percent scale", 100.0), "bounds": (0.2, 0.4),
               "step1": "removal protocols cut catheter-days by nearly a third - then hit the necessary-catheter wall",
               "confirm": "two-track programs beat removal-only protocols on residual CAUTI",
               "refute": "necessary-catheter CAUTI proves irreducible with current materials"},
},
# ------------------------------------------------------------------ rank 15
{
 "key": "clabsi",
 "name": "Central Line Infection Prevention",
 "group": "Infection Prevention",
 "ladder_rank": 15, "ladder_tier": "compounded",
 "problem": "Central-line bloodstream infections were once thought inevitable - bundles proved they weren't. So why do they still occur, and what eliminates the remainder?",
 "description": "CLABSI - bloodstream infection from a central venous catheter - was a leading ICU killer until Pronovost's Keystone project (2006) showed a five-element bundle (hand hygiene, maximal barriers, chlorhexidine skin prep, optimal site selection, daily review) could nearly eliminate it. Yet CLABSI persists: in long-term catheters, in emergency insertions, in immunocompromised patients - and surveillance definitions keep shifting underneath the data.",
 "background": "The bundle era began with Pronovost et al., NEJM 2006: Michigan ICUs cut CLABSI dramatically with checklist discipline. CDC guidelines codified the elements; CMS non-payment (2008) spread adoption. Success bred complacency and then the residual problem: infections in lines that cannot follow the bundle (emergency placements, femoral sites in crashing patients), in prolonged-dwell devices, and from intraluminal colonization that skin prep cannot reach. Antimicrobial locks and impregnated catheters help in niches. As of 2026 the bundle prevents most CLABSI, and the remainder is harder, more heterogeneous, and less responsive to checklists.",
 "why_it_matters": "CLABSI still kills: attributable mortality estimates run to double-digit percentages. The bundle's triumph proved infections are preventable; the residual is the next frontier of that proof.",
 "sig_pointer": "The Signature system's proposed approach treats the residual as a set of distinct failure modes needing distinct solutions, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that residual CLABSI is not one problem but several - extraluminal colonization despite prep, intraluminal colonization over time, emergency-placement compromises - and that bundle thinking (one checklist for all) cannot address failure modes the bundle was never designed for. "
  "Assumptions: (1) each residual failure mode has a distinct mechanism; (2) the modes are identifiable from line and patient characteristics; (3) mode-specific countermeasures exist or are engineerable. "
  "Reasoning path: a failure-mode taxonomy explains the plateau - the bundle solved its modes, leaving others - and directs innovation mode by mode instead of bundle-tweaking. "
  "Proposed mechanism: a 'failure-mode' prevention program that classifies each line's risk profile and applies mode-matched countermeasures (locks for intraluminal risk, site strategies for extraluminal, protocols for emergency placements). "
  "What would confirm it: mode-matched prevention outperforming bundle-plus in trials on residual CLABSI. "
  "What would kill it: evidence that residual CLABSI is dominated by a single mechanism after all, or that mode classification adds nothing. "
  "What this does not claim: it does not claim a line-care recommendation, does not advise on placement, and does not constitute clinical advice."),
 "sig_lens": "The Signature lens reads the remaining infections as distinct failure modes hiding inside one bundle, and asks what taxonomy would separate them.",
 "how_it_works": "Researchers study CLABSI through bundle-compliance studies, failure-mode analyses of residual infections, antimicrobial device trials, and surveillance-definition research.",
 "key_points": [
  "Pronovost's Keystone bundle (2006) nearly eliminated CLABSI in Michigan ICUs.",
  "Five elements: hygiene, barriers, chlorhexidine, site selection, daily review.",
  "CMS non-payment (2008) spread bundle adoption nationally.",
  "Residual CLABSI concentrates in emergency, long-dwell, and immunocompromised contexts.",
  "Intraluminal colonization over time evades skin-prep-based prevention.",
 ],
 "requirements": [
  "A failure-mode taxonomy of residual CLABSI.",
  "Mode-matched countermeasures proven in trials.",
  "Stable surveillance definitions for honest tracking.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Pronovost P et al. An intervention to decrease catheter-related bloodstream infections in the ICU. New England Journal of Medicine. 2006;355:2725-2732.",
  "O'Grady NP et al. Guidelines for the prevention of intravascular catheter-related infections. Clinical Infectious Diseases. 2011;52(9):e162-e193.",
  "Marschall J et al. Strategies to prevent central line-associated bloodstream infections in acute care hospitals. Infection Control and Hospital Epidemiology. 2014;35:753-771.",
  "Wichmann D et al. Long-term central line infections. Various; 2018-2022.",
 ],
 "demo_data": {"a": ("CLABSI reduction in Keystone ICUs, percent (approx)", 66.0),
               "b": ("percent scale", 100.0), "bounds": (0.5, 0.8),
               "step1": "the bundle cut CLABSI by two-thirds - proof that 'inevitable' infections are preventable",
               "confirm": "mode-matched prevention beats bundle-plus on residual CLABSI",
               "refute": "residual CLABSI proves dominated by a single mechanism after all"},
},
# ------------------------------------------------------------------ rank 16
{
 "key": "chronic-wounds",
 "name": "Chronic Wound Healing",
 "group": "Wound Care",
 "ladder_rank": 16, "ladder_tier": "compounded",
 "problem": "Some wounds - diabetic foot ulcers, venous leg ulcers, pressure injuries - stall for months despite good care. What keeps a wound chronic, and what restarts healing?",
 "description": "Chronic wounds affect millions, especially diabetics and the elderly: diabetic foot ulcers precede most non-traumatic amputations, venous ulcers recur relentlessly. These wounds stall in the inflammatory phase - colonized by biofilm, starved of perfusion, trapped in a protease-rich environment that destroys growth factors as fast as they arrive. Advanced therapies (growth factors, skin substitutes, negative-pressure, hyperbaric oxygen) help some wounds; none reliably restarts the stalled ones.",
 "background": "Wound-healing biology (inflammation, proliferation, remodeling) was mapped in the 20th century; chronic wounds were recognized as inflammation-arrested in the 1990s-2000s. Biofilm's role in chronicity was established (James et al., 2008: 60% of chronic wounds contain biofilm versus 6% of acute). Becaplermin (PDGF) was the first growth factor approved, with modest effects; bioengineered skin substitutes help venous and diabetic ulcers in trials. But healing rates plateaued: the wounds that don't respond to advanced therapy remain mysterious, and recurrence rates are dismal. As of 2026 the stalled wound's restart signal is unknown.",
 "why_it_matters": "Chronic wounds cause amputations, sepsis, and misery on a massive scale - and consume enormous nursing time in dressing changes. Restarting stalled healing would prevent amputations and liberate wound-care nursing.",
 "sig_pointer": "The Signature system's proposed approach treats chronicity as a trapped inflammatory state needing an exit signal, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that chronic wounds are trapped in a stable inflammatory attractor: biofilm, proteases, and senescent cells reinforce each other, and the wound cannot leave the state without a coordinated push on all three. "
  "Assumptions: (1) chronicity is a stable state, not a slow version of normal healing; (2) the three reinforcers (biofilm, protease excess, cellular senescence) must be addressed together; (3) the exit signal is a state transition, measurable in wound fluid. "
  "Reasoning path: an attractor model explains why single therapies underperform (they push one reinforcer while two hold the state) and predicts combined biofilm-protease-senescence therapy will outperform. "
  "Proposed mechanism: a 'state-exit' protocol sequencing biofilm disruption, protease modulation, and senescent-cell clearance, with wound-fluid markers confirming the transition out of chronicity. "
  "What would confirm it: combined protocols healing wounds that failed single advanced therapies, with markers tracking the state change. "
  "What would kill it: evidence that chronicity has no stable-state structure, or that the three reinforcers are independent rather than mutually reinforcing. "
  "What this does not claim: it does not claim a therapy ready for clinics, does not recommend products, and does not constitute clinical advice."),
 "sig_lens": "The Signature lens reads the stalled wound as trapped in an inflammatory attractor, and asks what coordinated push would spring it.",
 "how_it_works": "Wound researchers study chronicity through biofilm imaging, wound-fluid proteomics, senescence markers, and trials of advanced therapies and combination protocols.",
 "key_points": [
  "Chronic wounds stall in the inflammatory phase for months.",
  "Biofilm is present in ~60% of chronic wounds versus ~6% of acute ones.",
  "Diabetic foot ulcers precede most non-traumatic amputations.",
  "Advanced therapies help some wounds; the stalled ones resist all.",
  "Recurrence rates after healing remain dismal.",
 ],
 "requirements": [
  "A measurable definition of the chronic inflammatory state.",
  "Proof that combined multi-target therapy beats single therapies.",
  "Recurrence prevention, not just initial healing.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "James GA et al. Biofilms in chronic wounds. Wound Repair and Regeneration. 2008;16(1):37-44.",
  "Mustoe TA et al. Chronic wound pathogenesis and current treatment strategies. Lancet. 2004;363:1463-1464.",
  "Eming SA et al. Wound repair and regeneration: mechanisms, signaling, and translation. Science Translational Medicine. 2014;6(265):265sr6.",
  "Armstrong DG et al. Diabetic foot ulcers and their recurrence. New England Journal of Medicine. 2017;376:2367-2375.",
 ],
 "demo_data": {"a": ("chronic wounds containing biofilm, percent (approx)", 60.0),
               "b": ("acute wounds containing biofilm, percent (approx)", 6.0), "bounds": (6.0, 15.0),
               "step1": "chronic wounds carry ten times the biofilm burden of acute ones - chronicity has a signature",
               "confirm": "combined protocols heal wounds that failed single advanced therapies",
               "refute": "chronicity proves to have no stable-state structure"},
},
# ------------------------------------------------------------------ rank 17
{
 "key": "eol-symptoms",
 "name": "End-of-Life Symptom Management",
 "group": "Palliative Care",
 "ladder_rank": 17, "ladder_tier": "compounded",
 "problem": "Dying patients suffer pain, breathlessness, agitation, and secretions - why does excellent symptom control remain uneven, and what would make a good death reliable?",
 "description": "Nurses provide most end-of-life bedside care, managing pain, dyspnea, terminal agitation, and noisy secretions. The pharmacology exists - opioids, anxiolytics, antisecretories - but symptom control is uneven: pain is undertreated in minorities and the elderly, dyspnea is under-recognized, and terminal delirium is often misread as pain. Prognostication is poor, so the dying phase is recognized late.",
 "background": "The modern hospice movement (Saunders, 1960s) and palliative care (Mount, 1970s) made dying a clinical discipline. Evidence accumulated: early palliative care improves quality of life and even survival (Temel, NEJM 2010, in lung cancer). But integration lags - palliative care reaches a minority of dying patients, often in the final days. Symptom science advanced (dyspnea mechanisms, delirium subtypes) without fully reaching bedside practice. Cultural and clinician barriers - the conflation of palliative care with giving up - persist. As of 2026 a good death remains a matter of luck and geography.",
 "why_it_matters": "Everyone dies; most will need end-of-life nursing. Reliable symptom control is the most humane deliverable in all of healthcare - and its unevenness is an injustice to the dying.",
 "sig_pointer": "The Signature system's proposed approach treats the dying phase as recognizable earlier and manageable by protocol, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that end-of-life suffering concentrates in two gaps: late recognition of dying (so comfort measures start late) and symptom-specific undertreatment (pain treated, dyspnea missed). "
  "Assumptions: (1) the dying phase has recognizable prodromes; (2) each symptom has an effective protocol; (3) the barrier is recognition and activation, not pharmacology. "
  "Reasoning path: a recognition-activation model explains why the drugs exist but the suffering persists - the system fails to switch goals from cure to comfort in time. "
  "Proposed mechanism: 'comfort-switch' criteria - validated prodromes triggering automatic palliative activation - plus symptom-specific protocols with nurse-driven titration. "
  "What would confirm it: comfort-switch systems improving time-to-symptom-control and family-rated quality of death in trials. "
  "What would kill it: evidence that dying prodromes are too variable to recognize prospectively, or that protocols add nothing to clinician judgment. "
  "What this does not claim: it does not claim dying is predictable in individuals, prescribes no drugs, and does not constitute clinical advice."),
 "sig_lens": "The Signature lens reads end-of-life suffering as a late switch from cure to comfort, and asks what prodromes would flip the switch in time.",
 "how_it_works": "Palliative nurse researchers study dying through symptom-prevalence cohorts, prognostication studies, early-integration trials, and family-rated quality-of-death measures.",
 "key_points": [
  "Nurses deliver most end-of-life bedside symptom care.",
  "Early palliative care improves quality of life and even survival (Temel 2010).",
  "Palliative care reaches a minority, often only in final days.",
  "Dyspnea and delirium are under-recognized versus pain.",
  "Prognostication remains poor; the dying phase is recognized late.",
 ],
 "requirements": [
  "Validated prodromes of the dying phase.",
  "Symptom protocols with nurse-driven titration authority.",
  "Integration models that reach patients months, not days, before death.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Temel JS et al. Early palliative care for patients with metastatic non-small-cell lung cancer. New England Journal of Medicine. 2010;363:733-742.",
  "Saunders C. The evolution of palliative care. Journal of the Royal Society of Medicine. 2001;94(9):430-432.",
  "Hui D et al. Prognostication in advanced cancer. Nature Reviews Clinical Oncology. 2019;16:402-412.",
  "National Academies. Dying in America. Washington, DC: NAP; 2015.",
 ],
 "demo_data": {"a": ("dying patients receiving timely palliative care, percent (approx minority)", 30.0),
               "b": ("percent scale", 100.0), "bounds": (0.2, 0.45),
               "step1": "a minority of dying patients receive timely palliative care - the best care arrives last",
               "confirm": "comfort-switch systems improve time-to-control and family-rated quality of death",
               "refute": "dying prodromes prove too variable to recognize prospectively"},
},
# ------------------------------------------------------------------ rank 18
{
 "key": "family-icu",
 "name": "Family-Centered Care in ICU",
 "group": "Critical Care",
 "ladder_rank": 18, "ladder_tier": "compounded",
 "problem": "ICU families suffer anxiety, depression, and PTSD at high rates - what does family-centered nursing actually change, and how should families be integrated into critical care?",
 "description": "Critical illness traumatizes families: post-intensive-care syndrome-family (PICS-F) describes the anxiety, depression, and PTSD in relatives. Open visitation, family presence on rounds, and structured communication (VALUE, NURSE frameworks) help, but ICUs vary wildly: some still restrict visiting, family meetings happen late or not at all, and nurses mediate between teams and families without training or time.",
 "background": "Family-centered ICU care grew from the 1990s-2000s: open visitation studies showed benefits without the feared harms (infection, interference). Azoulay's work quantified family burden and tested communication interventions; the 2007 Lautrette trial showed a structured family conference with a bereavement brochure reduced PTSD and anxiety. Yet implementation lags: staffing models don't fund family time, cultural and language barriers complicate communication, and the pandemic's visitation bans set the field back years. As of 2026 family-centered care is endorsed everywhere and delivered unevenly.",
 "why_it_matters": "Families are the patient's memory, advocate, and post-ICU caregiver: their trauma becomes the patient's discharge environment. Integrating families well improves decisions, satisfaction, and long-term outcomes for everyone in the room.",
 "sig_pointer": "The Signature system's proposed approach treats the family as part of the care team with defined roles, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that family-centered care fails on role ambiguity: families are told they matter but given no defined role, so integration depends on individual nurse heroics rather than system design. "
  "Assumptions: (1) families can perform real care functions (orientation, mobilization encouragement, history provision); (2) defined roles reduce both family anxiety and nurse burden; (3) role clarity must survive shift changes and team turnover. "
  "Reasoning path: a role-design model explains why visitation alone underperforms - presence without purpose - and predicts that structured family roles will outperform open doors alone. "
  "Proposed mechanism: 'family role prescriptions' - defined, documented family functions integrated into the care plan, with nurse coaching and handoff of the family role across shifts. "
  "What would confirm it: role-prescribed families showing better PICS-F outcomes and nurse workload measures than visitation-only controls. "
  "What would kill it: evidence that family presence itself carries all the benefit, or that defined roles add burden without gain. "
  "What this does not claim: it does not claim families should provide clinical care, prescribes no policy, and does not constitute clinical advice."),
 "sig_lens": "The Signature lens reads the ICU family as an untrained team member awaiting a job description, and asks what defined role would help everyone.",
 "how_it_works": "ICU nurse researchers study families through PICS-F cohorts, communication intervention trials, visitation policy studies, and qualitative work on family needs.",
 "key_points": [
  "PICS-F: families suffer anxiety, depression, PTSD after ICU.",
  "Open visitation proved safe but insufficient alone.",
  "Structured family conferences reduce PTSD and anxiety (Lautrette 2007).",
  "Nurses mediate family-team communication without dedicated time or training.",
  "Pandemic visitation bans set family integration back years.",
 ],
 "requirements": [
  "Defined family roles integrated into care plans.",
  "Communication training and time funded in staffing models.",
  "Equity: family integration across language and culture barriers.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Azoulay E et al. Risk of post-traumatic stress symptoms in family members of ICU patients. American Journal of Respiratory and Critical Care Medicine. 2005;171:987-994.",
  "Lautrette A et al. A communication strategy and brochure for relatives of patients dying in the ICU. New England Journal of Medicine. 2007;356:469-478.",
  "Davidson JE et al. Guidelines for family-centered care in the neonatal, pediatric, and adult ICU. Critical Care Medicine. 2017;45(1):103-128.",
  "Needham DM et al. Post-intensive care syndrome. Various; 2012-2020.",
 ],
 "demo_data": {"a": ("family members with PTSD symptoms after ICU (approx percent)", 30.0),
               "b": ("percent scale", 100.0), "bounds": (0.2, 0.45),
               "step1": "nearly a third of ICU families carry PTSD symptoms - the unit wounds witnesses too",
               "confirm": "role-prescribed families beat visitation-only controls on PICS-F and workload",
               "refute": "family presence alone proves to carry all the benefit with roles adding nothing"},
},
# ------------------------------------------------------------------ rank 19
{
 "key": "retention",
 "name": "Nursing Workforce Retention",
 "group": "Workforce",
 "ladder_rank": 19, "ladder_tier": "compounded",
 "problem": "Nurses leave the bedside in droves - what actually keeps them, and why do retention programs keep missing the mark?",
 "description": "Nurse turnover is expensive (tens of thousands per departure) and dangerous (inexperience predicts harm). The pandemic exodus hollowed out experienced ranks; travel nursing offered an exit that became a career. Retention programs - sign-on bonuses, residency programs, shared governance - show mixed results: bonuses attract but don't retain, residencies help novices but not veterans, and the experienced nurses who left rarely return.",
 "background": "Turnover research (Hayes, O'Brien-Pallas) quantified costs and predictors: workload, leadership, autonomy, and pay. Nurse residency programs (Versant, Vizient/AACN) cut first-year turnover substantially. Magnet recognition correlates with retention. But the pandemic revealed the limits: even well-regarded systems hemorrhaged staff when conditions broke, and the travel-nurse market repriced bedside labor permanently. Recent work focuses on the experienced nurse - flexible scheduling, reduced physical burden, late-career roles - with thin evidence. As of 2026 retention remains the workforce's unsolved equation.",
 "why_it_matters": "Experience is a safety intervention: units lose it faster than they can rebuild it. Every retained veteran nurse prevents the errors of three novices; retention is patient safety by other means.",
 "sig_pointer": "The Signature system's proposed approach treats retention as a career-stage problem with different levers per stage, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that retention fails because programs target 'nurses' while turnover has different causes at different career stages: novices leave from overwhelm, mid-career from moral injury and pay, veterans from physical burden and disrespect. "
  "Assumptions: (1) turnover drivers are stage-specific; (2) stage can be identified from tenure and role data; (3) stage-matched interventions outperform generic ones. "
  "Reasoning path: a career-stage model explains why residencies (novice-targeted) don't retain veterans and why bonuses (generic) attract without retaining - the lever must match the stage. "
  "Proposed mechanism: 'stage-matched retention' - overwhelm reduction for novices, autonomy and pay repair for mid-career, physical-burden reduction and respect roles for veterans - tested against stage-specific turnover. "
  "What would confirm it: stage-matched programs outperforming generic retention spending on turnover and experience mix. "
  "What would kill it: evidence that turnover is dominated by system-wide factors affecting all stages equally. "
  "What this does not claim: it does not claim any program works today, prescribes no management action, and does not constitute clinical advice."),
 "sig_lens": "The Signature lens reads turnover as different exits at different career stages, and asks what lever matches each door.",
 "how_it_works": "Workforce researchers study retention through turnover cohorts, residency outcome studies, exit-interview analyses, travel-nurse market research, and magnet comparisons.",
 "key_points": [
  "Turnover costs tens of thousands per nurse and predicts harm.",
  "Residency programs cut first-year turnover substantially.",
  "The pandemic exodus hollowed out experienced ranks permanently in many systems.",
  "Sign-on bonuses attract without retaining.",
  "Evidence on retaining experienced nurses specifically is thin.",
 ],
 "requirements": [
  "Stage-specific turnover models validated prospectively.",
  "Interventions proven against experienced-nurse retention.",
  "Economic models comparing retention spending to turnover costs.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Hayes LJ et al. Nurse turnover: a literature review. International Journal of Nursing Studies. 2006;43(2):237-263.",
  "Goode CJ et al. Nurse residency programs. Journal for Nurses in Professional Development. 2013;29(2):71-77.",
  "Buerhaus PI et al. The nursing workforce. Various; 2020-2023.",
  "National Academies. The Future of Nursing 2020-2030. Washington, DC: NAP; 2021.",
 ],
 "demo_data": {"a": ("cost per nurse turnover, thousands of dollars (approx)", 50.0),
               "b": ("thousands scale", 1000.0), "bounds": (0.03, 0.08),
               "step1": "each departing nurse costs tens of thousands - turnover is a budget line and a safety line",
               "confirm": "stage-matched programs beat generic retention spending on turnover and experience mix",
               "refute": "turnover proves dominated by system-wide factors affecting all stages equally"},
},
# ------------------------------------------------------------------ rank 20
{
 "key": "health-equity",
 "name": "Health Equity in Nursing Care Delivery",
 "group": "Population Health",
 "ladder_rank": 20, "ladder_tier": "compounded",
 "problem": "Outcomes differ by race, income, and zip code even inside the same hospital - how much of inequity is nursing care delivery, and what closes it?",
 "description": "Disparities pervade: Black mothers die at multiples of white mothers' rates, pain is undertreated in Black patients, pulse oximeters overread in dark skin. Nurses are the most numerous clinicians and deliver most bedside care - yet equity research in nursing focuses on workforce diversity more than on whether care delivery itself is equitable, and interventions that close gaps are scarce.",
 "background": "The 2003 Institute of Medicine report 'Unequal Treatment' documented disparities; nursing's response emphasized cultural competence, then structural competency. Evidence of delivery gaps accumulated: pain management disparities (Hoffman 2016 showed false beliefs about Black pain tolerance among trainees), maternal mortality disparities, oximetry bias (Sjoding 2020, NEJM). Workforce diversity correlates with better outcomes for minority patients. But few trials test whether specific nursing care-delivery changes close outcome gaps, and equity dashboards remain rare. As of 2026 nursing knows inequity exists in its care and lacks proven delivery-level fixes.",
 "why_it_matters": "Nurses see every patient: if care delivery is inequitable, nurses are positioned to be the largest corrective force in healthcare - or its largest blind spot. Closing delivery gaps would save lives that are currently lost to bias.",
 "sig_pointer": "The Signature system's proposed approach treats equity as a measurable delivery property, not a training topic, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that equity efforts fail because they target attitudes while disparities live in delivery: which patients get believed about pain, whose deterioration is caught, who gets the experienced nurse. "
  "Assumptions: (1) delivery disparities are measurable in routine data; (2) they cluster at specific decision points; (3) standardizing those decision points closes gaps without requiring attitude change. "
  "Reasoning path: a delivery-measurement model explains why cultural-competence training underperforms - it doesn't touch the decision points - and predicts that instrumented, standardized decision points will close gaps. "
  "Proposed mechanism: 'equity instrumentation' - routine measurement of care delivery by patient group at key decision points (pain treatment, rescue, assignment), with standardized protocols triggered by disparity signals. "
  "What would confirm it: instrumented units showing narrowing delivery gaps versus controls in trials. "
  "What would kill it: evidence that disparities are dominated by factors outside nursing care delivery, or that measurement alone changes nothing. "
  "What this does not claim: it does not claim any unit is currently inequitable, prescribes no policy, and does not constitute clinical advice."),
 "sig_lens": "The Signature lens reads inequity as delivery decisions differing by patient group, and asks what instrumentation would make the difference visible and fixable.",
 "how_it_works": "Nurse researchers study equity through disparities cohorts, pain-treatment audits, workforce-diversity outcome studies, oximetry-bias research, and structural-competency trials.",
 "key_points": [
  "'Unequal Treatment' (2003) documented systemic healthcare disparities.",
  "Pain is undertreated in Black patients; false beliefs about pain tolerance persist.",
  "Pulse oximeters overread oxygen in dark skin (Sjoding 2020).",
  "Nursing equity work emphasizes workforce diversity over delivery measurement.",
  "Proven delivery-level interventions that close gaps are scarce.",
 ],
 "requirements": [
  "Routine delivery measurement stratified by patient group.",
  "Standardized decision points proven to close gaps.",
  "Workforce diversity evidence linked to delivery outcomes.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Institute of Medicine. Unequal Treatment. Washington, DC: NAP; 2003.",
  "Hoffman KM et al. Racial bias in pain assessment and treatment recommendations. PNAS. 2016;113(16):4296-4301.",
  "Sjoding MW et al. Racial bias in pulse oximetry measurement. New England Journal of Medicine. 2020;383:2477-2478.",
  "National Academies. The Future of Nursing 2020-2030. Washington, DC: NAP; 2021.",
 ],
 "demo_data": {"a": ("Black maternal mortality multiple versus white mothers (approx)", 3.0),
               "b": ("parity baseline (multiple scale)", 1.0), "bounds": (2.0, 5.0),
               "step1": "Black mothers die at multiples of the rate of white mothers - inside the same system",
               "confirm": "instrumented units narrow delivery gaps versus controls in trials",
               "refute": "disparities prove dominated by factors outside nursing care delivery"},
},
# ------------------------------------------------------------------ rank 21
{
 "key": "telehealth",
 "name": "Telehealth Nursing Efficacy",
 "group": "Technology",
 "ladder_rank": 21, "ladder_tier": "compounded",
 "problem": "Nursing went virtual in the pandemic - but which nursing care actually works through a screen, and what is lost without touch?",
 "description": "Telenursing - triage, chronic-disease coaching, post-discharge follow-up, remote monitoring - expanded explosively after 2020. Evidence is mixed: remote monitoring helps heart failure, virtual triage sorts safely, but the therapeutic relationship, the physical assessment, and the subtle deterioration cues of bedside nursing don't obviously translate. Reimbursement and licensure remain unsettled.",
 "background": "Telenursing predates the pandemic (telephone triage, early remote monitoring trials), but 2020 made it mainstream overnight. Trials show remote monitoring reduces heart-failure readmissions; virtual urgent-care triage performs comparably for sorting. But the evidence thins for complex care: wound assessment by photo, mental-health counseling, and the 'presence' functions of nursing lack rigorous comparison. The digital divide means virtual care may worsen equity. As of 2026 telenursing is widespread with a thin evidence base for what it replaces versus what it merely supplements.",
 "why_it_matters": "Virtual care is not retreating: workforce shortages make it structurally necessary. Knowing what nursing survives the screen - and what doesn't - determines whether telenursing extends care or hollows it.",
 "sig_pointer": "The Signature system's proposed approach sorts nursing functions by their screen-translatability, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that telenursing debates stall because 'nursing' is treated as one thing: in reality it bundles functions with wildly different screen-translatability - data review translates perfectly, therapeutic touch not at all. "
  "Assumptions: (1) nursing functions can be decomposed and scored for virtualizability; (2) outcomes differ by function, not by modality globally; (3) hybrid models can assign each function to its best channel. "
  "Reasoning path: a function-decomposition model explains the mixed evidence - studies test different function bundles - and predicts hybrid assignment will outperform all-virtual or all-in-person. "
  "Proposed mechanism: a 'function-channel map' scoring nursing activities by virtualizability, with hybrid care models assigning each function optimally, tested against outcomes and equity. "
  "What would confirm it: hybrid models outperforming single-channel care in trials, with the map predicting which functions drive the difference. "
  "What would kill it: evidence that outcomes depend on the relationship holistically rather than on functions, defeating decomposition. "
  "What this does not claim: it does not claim virtual care equals bedside care, prescribes no model, and does not constitute clinical advice."),
 "sig_lens": "The Signature lens reads nursing as a bundle of functions with different screen fates, and asks what map would route each to its best channel.",
 "how_it_works": "Researchers study telenursing through remote-monitoring trials, virtual-triage safety studies, telehealth equity research, and qualitative work on therapeutic presence.",
 "key_points": [
  "Telenursing expanded explosively after 2020 and is not retreating.",
  "Remote monitoring reduces heart-failure readmissions in trials.",
  "Physical assessment and therapeutic presence translate poorly.",
  "The digital divide threatens to make virtual care inequitable.",
  "Evidence is thin for which functions virtual care can replace.",
 ],
 "requirements": [
  "A validated function-by-function virtualizability map.",
  "Hybrid models proven against single-channel care.",
  "Equity guardrails for the digitally excluded.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Inglis SC et al. Structured telephone support or telemonitoring for heart failure. Cochrane Database of Systematic Reviews. 2015;8:CD007228.",
  "Schlachta-Fairchild L et al. Telenursing. Various; 2008-2020.",
  "American Telemedicine Association. Telehealth nursing guidelines. Various.",
  "Totten AM et al. Telehealth for acute and chronic care. AHRQ; 2019-2022.",
 ],
 "demo_data": {"a": ("heart-failure readmissions cut by remote monitoring, percent (approx)", 20.0),
               "b": ("percent scale", 100.0), "bounds": (0.1, 0.3),
               "step1": "remote monitoring cuts heart-failure readmissions by a fifth - some functions clearly translate",
               "confirm": "hybrid models beat single-channel care with the map predicting the difference",
               "refute": "outcomes prove to depend on the relationship holistically, defeating decomposition"},
},
# ------------------------------------------------------------------ rank 22
{
 "key": "nurse-led-chronic",
 "name": "Nurse-Led Chronic Disease Management",
 "group": "Chronic Care",
 "ladder_rank": 22, "ladder_tier": "compounded",
 "problem": "Nurses manage diabetes, heart failure, and hypertension well in trials - so why hasn't nurse-led chronic care scaled, and what are its true limits?",
 "description": "Randomized trials show nurse-led clinics achieve diabetes, hypertension, and heart-failure outcomes equal to or better than physician-led care, often with higher satisfaction and lower cost. Yet scale-up stalls: scope-of-practice laws restrict prescribing and titration, reimbursement favors physician visits, and health systems underinvest in the model despite the evidence.",
 "background": "Nurse-led chronic care trials accumulated from the 1990s-2000s (notably in the UK and Netherlands): nurse-run diabetes and heart-failure clinics matched physician outcomes. The evidence strengthened with systematic reviews showing equivalent clinical outcomes. But the implementation gap is structural: prescriptive authority varies by jurisdiction, fee-for-service rewards visits over outcomes, and physician organizations resist scope expansion. Value-based payment models are beginning to change the economics. As of 2026 the evidence says scale it; the system says not yet.",
 "why_it_matters": "Chronic disease is the bulk of healthcare need and the nursing workforce is its largest untapped capacity. Scaling nurse-led management would expand access, cut costs, and improve control of the diseases that actually kill most people.",
 "sig_pointer": "The Signature system's proposed approach treats scale-up as a protocol-authority problem, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that nurse-led chronic care is blocked less by competence than by authority: the model works where nurses can titrate by protocol, and stalls where every adjustment needs physician sign-off. "
  "Assumptions: (1) protocol-driven titration is the active ingredient; (2) authority, not knowledge, is the rate limiter; (3) outcomes hold at scale if protocols hold. "
  "Reasoning path: an authority model explains the trial-practice gap - trials grant protocol authority, practice withholds it - and predicts that authority-expanding jurisdictions will show better scale-up. "
  "Proposed mechanism: 'protocol-authority' scale-up - standardized titration protocols with defined nurse authority, tested for outcomes, safety, and cost at system scale. "
  "What would confirm it: authority-expanded systems outperforming restricted ones on chronic-disease control in natural experiments. "
  "What would kill it: evidence that trial results don't survive scale-up even with authority, implicating selection or Hawthorne effects. "
  "What this does not claim: it does not claim nurses should prescribe independently, takes no scope-of-practice position, and does not constitute clinical advice."),
 "sig_lens": "The Signature lens reads the chronic-care gap as an authority gap wearing a competence costume, and asks what protocol authority would unlock.",
 "how_it_works": "Researchers study nurse-led care through clinic trials, scope-of-practice natural experiments, cost-effectiveness analyses, and implementation studies.",
 "key_points": [
  "Nurse-led clinics match or beat physician outcomes in chronic-disease trials.",
  "Protocol-driven titration is the model's active ingredient.",
  "Scope-of-practice laws restrict the authority the model needs.",
  "Reimbursement favors physician visits over nurse-led outcomes.",
  "Value-based payment is beginning to change the economics.",
 ],
 "requirements": [
  "Proof that trial results survive real-world scale-up.",
  "Authority models that are safe, standardized, and accepted.",
  "Payment models rewarding outcomes over visit types.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Laurant M et al. Nurses as substitutes for doctors in primary care. Cochrane Database of Systematic Reviews. 2018;7:CD001271.",
  "Martinez-Gonzalez NA et al. Task-shifting from physicians to nurses in primary care. British Journal of General Practice. 2014;64(629):e652-e661.",
  "National Academies. The Future of Nursing 2020-2030. Washington, DC: NAP; 2021.",
  "Newhouse RP et al. Advanced practice nurse outcomes. Nursing Economics. 2011;29(5):230-250.",
 ],
 "demo_data": {"a": ("chronic-disease trials showing nurse-led equivalence or better, percent (approx)", 80.0),
               "b": ("percent scale", 100.0), "bounds": (0.6, 0.95),
               "step1": "most trials find nurse-led chronic care matches or beats physician-led - the evidence is lopsided",
               "confirm": "authority-expanded systems beat restricted ones on chronic-disease control",
               "refute": "trial results prove not to survive scale-up even with full protocol authority"},
},
# ------------------------------------------------------------------ rank 23
{
 "key": "workplace-violence",
 "name": "Workplace Violence Against Nurses",
 "group": "Workforce",
 "ladder_rank": 23, "ladder_tier": "compounded",
 "problem": "Nurses are assaulted at work at alarming rates - why does healthcare tolerate violence its workers would never accept elsewhere, and what actually prevents it?",
 "description": "Healthcare workers face workplace violence at rates far exceeding other industries: emergency and psychiatric nurses are hit, kicked, bitten, and threatened regularly. Underreporting is endemic - violence is normalized as 'part of the job.' Prevention programs (de-escalation training, security, environmental design) show modest effects; the deeper drivers - wait times, understaffing, substance use, psychiatric boarding in EDs - are structural.",
 "background": "Workplace-violence surveillance (Bureau of Labor Statistics, OSHA) documented healthcare's outlier status in the 2000s-2010s. Research identified high-risk settings (ED, psychiatry, geriatrics with dementia) and the normalization culture. Interventions tested: de-escalation training (modest effects), security presence, panic buttons, and California's 2014 workplace-violence prevention law for hospitals (SB 1299) mandating plans. But rigorous trials are scarce, reporting remains incomplete, and the structural drivers - boarding, waits, staffing - persist. As of 2026 violence prevention is mandated in some jurisdictions and measured almost nowhere rigorously.",
 "why_it_matters": "Violence injures nurses, drives them from the profession, and degrades care for everyone. A workforce that expects assault cannot sustain the compassion its patients need.",
 "sig_pointer": "The Signature system's proposed approach treats violence as a predictable system output, not a random event, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that healthcare violence is largely predictable from system states: long waits, boarding, understaffing, and substance-use presentations combine into high-risk configurations that can be forecast. "
  "Assumptions: (1) most incidents follow recognizable escalations, not sudden attacks; (2) system-state variables predict risk windows; (3) early de-escalation resources can be pre-positioned. "
  "Reasoning path: a predictability model reframes prevention from training individuals to managing system states - explaining why training alone underperforms and why structural fixes matter more. "
  "Proposed mechanism: 'violence forecasting' - real-time risk scoring from system states triggering pre-positioned de-escalation resources, tested against incident rates. "
  "What would confirm it: forecasting-based prevention outperforming training-only approaches in trials. "
  "What would kill it: evidence that violence is dominated by unpredictable individual factors regardless of system state. "
  "What this does not claim: it does not claim violence is currently predictable, blames no patient group, and does not constitute clinical or management advice."),
 "sig_lens": "The Signature lens reads the assault as the end of a forecastable escalation, and asks what system-state signal would summon help in time.",
 "how_it_works": "Researchers study violence through incident surveillance, risk-factor studies, intervention evaluations, and policy analyses of prevention mandates.",
 "key_points": [
  "Healthcare workplace-violence rates far exceed other industries.",
  "ED, psychiatry, and dementia care are the highest-risk settings.",
  "Underreporting is endemic; violence is normalized as 'part of the job.'",
  "California's SB 1299 (2014) mandated hospital prevention plans.",
  "Structural drivers - waits, boarding, staffing - persist unaddressed.",
 ],
 "requirements": [
  "Rigorous trials of prevention strategies, not just mandates.",
  "Complete reporting to measure the true burden.",
  "Structural fixes to waits, boarding, and staffing.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Bureau of Labor Statistics. Workplace violence in healthcare. Various years.",
  "Speroni KG et al. Incidence and cost of nurse workplace violence. Journal of Emergency Nursing. 2014;40(3):218-228.",
  "California SB 1299. Hospital workplace violence prevention; 2014.",
  "OSHA. Guidelines for preventing workplace violence for healthcare and social service workers. 2016.",
 ],
 "demo_data": {"a": ("healthcare violence rate multiple versus other industries (approx)", 5.0),
               "b": ("baseline multiple scale", 1.0), "bounds": (3.0, 8.0),
               "step1": "healthcare workers face violence at multiples of other industries' rates - an outlier industry",
               "confirm": "forecasting-based prevention beats training-only approaches in trials",
               "refute": "violence proves dominated by unpredictable individual factors regardless of system state"},
},
# ------------------------------------------------------------------ rank 24
{
 "key": "ai-workflow",
 "name": "AI Clinical Decision Support in Nursing Workflow",
 "group": "Technology",
 "ladder_rank": 24, "ladder_tier": "advanced",
 "problem": "AI can predict deterioration, sepsis, and falls - but nurses override or ignore most alerts. What would make AI a trusted partner instead of another alarm?",
 "description": "Hospitals are deploying AI decision support for deterioration, sepsis, pressure injury, and staffing - yet adoption is the graveyard: the Epic sepsis model's poor external validation (2021) is emblematic, alert fatigue transfers to AI alerts, and nurses report that models don't understand workflow context. The technical frontier (better models) races ahead of the integration frontier (trusted, usable, workflow-fitted AI).",
 "background": "Clinical AI in nursing began with early-warning scores, then machine-learning deterioration models (2010s). Prospective failures accumulated: models trained on biased data, validated retrospectively, failing live. Human-factors research showed the problem is sociotechnical - alert timing, actionability, explanation, and liability. Successful integrations are narrow: a few deterioration models with careful implementation. As of 2026 the gap between model capability and bedside usefulness remains the field's central problem.",
 "why_it_matters": "AI will be embedded in nursing workflow whether or not it works well: the question is whether it becomes a cognitive partner or an expensive distraction. Getting integration right determines whether AI helps or harms the nurses it claims to assist.",
 "sig_pointer": "The Signature system's proposed approach treats AI adoption as a trust-calibration problem, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that clinical AI fails on trust calibration: nurses need to know when to trust the model and when to override it, and current systems provide neither calibrated confidence nor override guidance. "
  "Assumptions: (1) trust is calibratable - nurses can learn a model's competence boundaries; (2) explanations must be workflow-relevant, not technically complete; (3) the liability of following versus overriding must be explicit. "
  "Reasoning path: a trust-calibration model explains both alert fatigue (uncalibrated distrust) and automation bias (uncalibrated trust) - the design target is appropriate reliance, not maximum use. "
  "Proposed mechanism: 'calibrated AI' presenting confidence, competence boundaries, and recommended reliance level per alert, with nurse override as a designed input rather than a failure mode. "
  "What would confirm it: calibrated systems showing appropriate reliance (high agreement on correct alerts, overrides on wrong ones) and better outcomes than black-box alerts. "
  "What would kill it: evidence that nurses cannot calibrate trust to models regardless of design, or that calibration adds no outcome benefit. "
  "What this does not claim: it does not claim any AI is ready for bedsides, endorses no product, and does not constitute clinical advice."),
 "sig_lens": "The Signature lens reads the ignored alert as uncalibrated trust, and asks what would teach each nurse exactly when to listen.",
 "how_it_works": "Researchers study clinical AI through prospective implementation trials, human-factors studies of alert response, trust-calibration experiments, and bias audits of models.",
 "key_points": [
  "The Epic sepsis model's poor external validation (2021) is emblematic of the gap.",
  "Nurses override or ignore most AI alerts - alert fatigue transfers.",
  "The problem is sociotechnical: timing, actionability, explanation, liability.",
  "Successful integrations are narrow and carefully implemented.",
  "Model capability races ahead of bedside usefulness.",
 ],
 "requirements": [
  "Calibrated confidence and competence boundaries per alert.",
  "Workflow-fitted explanations, not technical dumps.",
  "Prospective proof of outcome benefit, not retrospective accuracy.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Wong A et al. External validation of a widely implemented proprietary sepsis prediction model. JAMA Internal Medicine. 2021;181(8):1065-1070.",
  "Sendak MP et al. Sepsis Watch: implementation science. Various; 2019-2022.",
  "Topol EJ. High-performance medicine: the convergence of human and artificial intelligence. Nature Medicine. 2019;25:44-56.",
  "National Academies. Artificial Intelligence in Health Care. Various; 2022.",
 ],
 "demo_data": {"a": ("AI alerts overridden or ignored, percent (typical, approx)", 90.0),
               "b": ("percent scale", 100.0), "bounds": (0.7, 0.97),
               "step1": "nurses override the vast majority of AI alerts - the technology has a trust problem",
               "confirm": "calibrated systems show appropriate reliance and better outcomes than black-box alerts",
               "refute": "nurses prove unable to calibrate trust to models regardless of design"},
},
# ------------------------------------------------------------------ rank 25
{
 "key": "genomics-nursing",
 "name": "Genomics-Informed Nursing Care",
 "group": "Precision Health",
 "ladder_rank": 25, "ladder_tier": "advanced",
 "problem": "Genomic medicine is here - drug-gene interactions, cancer risk, pharmacogenomics - but nursing practice hasn't absorbed it. What is the nurse's role in the genomic era?",
 "description": "Pharmacogenomic variants affect drug response (clopidogrel, codeine, antidepressants); hereditary cancer syndromes need family-history triage; polygenic risk scores loom. Yet most nurses report low genomic confidence, curricula barely cover it, and no standard defines genomic nursing competencies in practice. The science exists; the nursing translation does not.",
 "background": "The Human Genome Project (2003) launched the era; CPIC guidelines (2009 onward) made pharmacogenomics actionable. Nursing's genomic pioneers (Calzone, Jenkins) documented the competency gap and built the Essential Nursing Competencies in Genomics (2009). Implementation crawls: a few centers offer pharmacogenomic testing with nurse navigation, but routine practice is untouched. Polygenic scores and direct-to-consumer testing are arriving faster than the profession's readiness. As of 2026 genomics-informed nursing is a competency framework awaiting a workforce.",
 "why_it_matters": "Nurses administer the drugs genomics personalizes and take the family histories genomics needs: without genomic nursing, precision medicine's benefits pool among the already-advantaged and its risks (misinterpreted results) fall on the unprepared.",
 "sig_pointer": "The Signature system's proposed approach treats genomic nursing as a triage-and-translation function, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that genomic nursing doesn't require every nurse to be a geneticist - it requires a defined triage-and-translation function: recognizing when genomics matters, collecting the right history, and connecting patients to expertise. "
  "Assumptions: (1) most genomic value in nursing comes from a small set of high-yield actions (family history, pharmacogenomic flags); (2) these actions are definable and teachable; (3) specialist referral handles the rest. "
  "Reasoning path: a triage model explains why broad genomic education underperforms - it teaches too much to too many - and predicts that focused competency in high-yield actions will outperform. "
  "Proposed mechanism: 'genomic triage' competencies embedded in routine assessment (family-history red flags, drug-gene alerts in the med pass), with referral pathways, tested against appropriate testing and counseling rates. "
  "What would confirm it: triage-trained nurses outperforming broadly educated ones on high-yield genomic actions in trials. "
  "What would kill it: evidence that genomic actions require specialist depth that triage cannot provide, or that the high-yield set is too small to matter. "
  "What this does not claim: it does not claim nurses should interpret genomes, takes no testing position, and does not constitute clinical advice."),
 "sig_lens": "The Signature lens reads genomic nursing as triage awaiting definition, and asks which few actions would capture most of the value.",
 "how_it_works": "Researchers study genomic nursing through competency surveys, family-history intervention trials, pharmacogenomic implementation studies, and curriculum evaluations.",
 "key_points": [
  "CPIC guidelines (2009+) made pharmacogenomics clinically actionable.",
  "Essential Nursing Competencies in Genomics were defined in 2009.",
  "Most nurses report low genomic confidence; curricula barely cover it.",
  "Family history remains the highest-yield genomic tool in nursing.",
  "Direct-to-consumer testing arrives faster than professional readiness.",
 ],
 "requirements": [
  "A defined, teachable genomic triage function for generalist nurses.",
  "Proof that triage training changes testing and counseling behavior.",
  "Referral pathways that actually absorb the triaged patients.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Calzone KA et al. Essential nursing competencies and curricula guidelines for genetics and genomics. Nursing Outlook. 2009;57(2):90-96.",
  "Relling MV, Evans WE. Pharmacogenomics in the clinic. Nature. 2015;526:343-350.",
  "Clinical Pharmacogenetics Implementation Consortium (CPIC). Guidelines; 2009 onward.",
  "Jenkins J, Calzone KA. Genomic nursing. Various; 2010-2020.",
 ],
 "demo_data": {"a": ("nurses reporting genomic confidence, percent (surveys, approx)", 20.0),
               "b": ("percent scale", 100.0), "bounds": (0.1, 0.35),
               "step1": "a minority of nurses feel genomically confident - the workforce trails the science",
               "confirm": "triage-trained nurses beat broadly educated ones on high-yield genomic actions",
               "refute": "genomic actions prove to require specialist depth that triage cannot provide"},
},
# ------------------------------------------------------------------ rank 26
{
 "key": "nursing-attribution",
 "name": "Nursing's Independent Contribution to Outcomes",
 "group": "Outcomes Science",
 "ladder_rank": 26, "ladder_tier": "advanced",
 "problem": "Everyone agrees nursing matters - but how much of a patient's outcome is independently attributable to nursing care, separate from medicine, luck, and the hospital?",
 "description": "The attribution problem is nursing science's deepest methodologic challenge: patients receive nursing, medicine, pharmacy, therapy simultaneously, and outcomes reflect all of it. Staffing studies show associations; the independent causal contribution of nursing interventions - surveillance, education, comfort, coordination - remains largely unquantified. Without attribution, nursing can't prove its value in the currency administrators understand.",
 "background": "Outcomes research in nursing grew from the 1990s (the nursing minimum data set, NDNQI indicators). Staffing-outcome associations are the strongest attribution evidence, but they attribute the nurse's presence, not specific nursing work. Intervention trials (discharge education, transitional care - Naylor's transitional care model shows readmission reductions) attribute specific models. But the field lacks a general attribution science: most nursing work is bundled, unmeasured, and invisible in data. As of 2026 nursing's value is asserted more than demonstrated.",
 "why_it_matters": "What can't be attributed can't be funded: nursing budgets are cut because nursing value is invisible in outcome data. Solving attribution would let nursing claim its share of outcomes - and protect the staffing that produces them.",
 "sig_pointer": "The Signature system's proposed approach treats nursing work as measurable through its absence, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that nursing's contribution is best measured through structured absence: comparing outcomes across natural variation in nursing inputs (missed care, staffing shocks, strike periods) while holding other inputs constant. "
  "Assumptions: (1) natural experiments in nursing input provide causal leverage; (2) missed-care data reveals which nursing functions move outcomes; (3) the contribution is heterogeneous across functions. "
  "Reasoning path: an absence-based attribution science explains why presence-associations plateau - they can't separate functions - and predicts that missed-care gradients will attribute specific nursing work to specific outcomes. "
  "Proposed mechanism: 'attribution through absence' - systematic measurement of missed nursing care linked to outcomes, plus natural-experiment analyses, building a function-by-function value map. "
  "What would confirm it: absence gradients attributing specific functions (surveillance, education) to specific outcomes in replicated analyses. "
  "What would kill it: evidence that nursing inputs can't be separated from correlated medical inputs even in natural experiments. "
  "What this does not claim: it does not claim any specific value for nursing, prescribes no staffing, and does not constitute clinical advice."),
 "sig_lens": "The Signature lens reads nursing value as visible in its absence, and asks what the missing care reveals about the care that matters.",
 "how_it_works": "Outcomes researchers study attribution through missed-care linkage studies, natural experiments, transitional-care trials, and nursing-sensitive indicator development.",
 "key_points": [
  "Staffing studies attribute presence, not specific nursing work.",
  "Naylor's transitional care model proves specific nursing models cut readmissions.",
  "Most nursing work is bundled, unmeasured, and invisible in data.",
  "The nursing minimum data set and NDNQI standardized some indicators.",
  "Nursing's value is asserted more than demonstrated in causal terms.",
 ],
 "requirements": [
  "Causal attribution of specific nursing functions to outcomes.",
  "Missed-care measurement standardized and linked to outcomes.",
  "A value map administrators can fund against.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Naylor MD et al. Transitional care of older adults hospitalized with heart failure. Annals of Internal Medicine. 2004;140(11):910-920.",
  "Needleman J et al. Nurse-staffing levels and the quality of care in hospitals. New England Journal of Medicine. 2002;346:1715-1722.",
  "Doran DM. Nursing Outcomes: The State of the Science. 2nd ed. Jones and Bartlett; 2011.",
  "Aiken LH et al. Effects of nurse staffing and nurse education on patient deaths. Lancet. 2014;383:1824-1830.",
 ],
 "demo_data": {"a": ("nursing-sensitive indicators in routine use (approx)", 15.0),
               "b": ("nursing functions performed daily (approx hundreds)", 200.0), "bounds": (0.05, 0.12),
               "step1": "a handful of indicators tries to capture hundreds of daily nursing functions",
               "confirm": "absence gradients attribute specific functions to specific outcomes in replication",
               "refute": "nursing inputs prove inseparable from correlated medical inputs"},
},
# ------------------------------------------------------------------ rank 27
{
 "key": "global-shortage",
 "name": "Global Nursing Shortage Solutions",
 "group": "Workforce",
 "ladder_rank": 27, "ladder_tier": "advanced",
 "problem": "The world is short millions of nurses, and the shortage is growing - what would actually close the gap, given that training pipelines take years?",
 "description": "The WHO estimated a global shortfall of nearly 6 million nurses in 2020, concentrated in Africa and Southeast Asia; high-income countries fill gaps by recruiting from the very countries that can least afford to lose nurses. Training pipelines are slow and expensive, educators are themselves in short supply, and migration - while a lifeline for destination countries - deepens source-country crises. No country has solved its shortage sustainably.",
 "background": "The global shortage was quantified in WHO's State of the World's Nursing reports (2020, with updates). High-income recruitment from low-income countries - the 'brain drain' - prompted the WHO Global Code of Practice on health-worker recruitment (2010), widely ignored. Pipeline research shows educator shortages bottleneck training expansion; task-shifting to community health workers helps but has limits. The pandemic worsened everything: burnout-driven exits plus training disruptions. As of 2026 the shortage grows faster than pipelines, and ethical recruitment remains aspirational.",
 "why_it_matters": "Nursing shortages kill: understaffed systems deliver worse care everywhere, and the poorest countries lose the nurses they trained to the richest. Solving the shortage is the largest workforce problem in global health.",
 "sig_pointer": "The Signature system's proposed approach treats the shortage as a pipeline-plus-retention equation, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that shortage debates over-focus on training new nurses while the faster lever is retention: every experienced nurse kept equals years of pipeline output, and the shortage equation must optimize both. "
  "Assumptions: (1) retention gains are faster than pipeline gains; (2) educator shortages cap pipeline expansion; (3) migration flows respond to incentives and can be made ethical. "
  "Reasoning path: a pipeline-plus-retention model explains why training expansions disappoint (they leak through turnover and migration) and predicts retention-first strategies will close gaps faster. "
  "Proposed mechanism: 'shortage equation' planning that jointly optimizes training throughput, educator supply, retention, and ethical migration compacts, tested against national shortage trajectories. "
  "What would confirm it: countries adopting retention-first strategies bending their shortage curves faster than pipeline-only peers. "
  "What would kill it: evidence that retention is as slow as training, or that migration flows are unresponsive to compacts. "
  "What this does not claim: it does not claim any country's policy works, takes no migration position, and does not constitute clinical advice."),
 "sig_lens": "The Signature lens reads the shortage as a leaky bucket, and asks whether plugging the leaks beats pouring faster.",
 "how_it_works": "Workforce researchers study the shortage through WHO surveillance, migration-flow analyses, pipeline modeling, and natural experiments in retention policy.",
 "key_points": [
  "WHO estimated a ~6 million nurse shortfall in 2020.",
  "Shortages concentrate in Africa and Southeast Asia.",
  "High-income recruitment deepens source-country crises ('brain drain').",
  "The WHO recruitment code (2010) is widely ignored.",
  "Educator shortages bottleneck training expansion.",
 ],
 "requirements": [
  "Joint optimization of training, retention, and migration.",
  "Ethical migration compacts that actually bind.",
  "Educator-pipeline solutions to unblock training.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "World Health Organization. State of the World's Nursing 2020. Geneva: WHO; 2020.",
  "World Health Organization. Global Code of Practice on the International Recruitment of Health Personnel. 2010.",
  "Buchan J et al. Health worker migration. Various; 2010-2022.",
  "Drennan VM, Ross F. Global nurse shortages. British Medical Bulletin. 2019;130(1):25-38.",
 ],
 "demo_data": {"a": ("global nurse shortfall, millions (WHO 2020)", 6.0),
               "b": ("years to train a nurse (approx)", 4.0), "bounds": (1.0, 2.5),
               "step1": "millions short, years to train each one - the pipeline arithmetic cannot close the gap alone",
               "confirm": "retention-first countries bend shortage curves faster than pipeline-only peers",
               "refute": "retention proves as slow as training with migration unresponsive to compacts"},
},
# ------------------------------------------------------------------ rank 28
{
 "key": "climate-health",
 "name": "Climate Change Health Response in Nursing",
 "group": "Population Health",
 "ladder_rank": 28, "ladder_tier": "advanced",
 "problem": "Heat waves, wildfire smoke, floods, and vector spread are nursing problems now - but what is nursing's defined role in climate-health response?",
 "description": "Climate change already drives nursing workload: heat illness in elders, asthma from wildfire smoke, trauma from extreme weather, expanding vector-borne disease. Nurses are trusted messengers and frontline responders, yet climate-health nursing lacks defined competencies, curricula, and practice models. Disaster nursing exists but climate is chronic, not episodic.",
 "background": "The Lancet Countdown (2015 onward) quantified health impacts; nursing organizations (ANA, ICN) issued climate position statements. Disaster nursing has a literature (INCMCE competencies), but slow-onset climate health - heat, air quality, food and water insecurity - lacks a nursing practice model. Early work focuses on heat-action plans for homebound elders, wildfire-smoke counseling, and facility resilience. Education lags: few programs teach climate-health. As of 2026 climate-health nursing is a call to action awaiting a practice science.",
 "why_it_matters": "Nurses will absorb climate's health burden whether or not the profession prepares: heat kills elders quietly, smoke chokes children, floods displace the frail. A defined nursing role would convert improvisation into readiness.",
 "sig_pointer": "The Signature system's proposed approach treats climate-health nursing as anticipatory community care, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that climate-health nursing is fundamentally anticipatory: the harms are forecastable (heat waves, smoke events, flood seasons), so the nursing function is pre-positioning protection for the vulnerable before events, not just responding after. "
  "Assumptions: (1) climate health harms concentrate in known vulnerable populations; (2) events are forecastable days ahead; (3) anticipatory outreach prevents more harm than reactive care. "
  "Reasoning path: an anticipatory model reframes climate nursing from disaster response to community prevention - explaining why disaster competencies underfit and what new competencies are needed. "
  "Proposed mechanism: 'climate anticipatory care' - vulnerability registries plus forecast-triggered outreach (cooling, filtration, evacuation support), tested against event-period morbidity. "
  "What would confirm it: anticipatory programs reducing heat and smoke morbidity versus reactive care in trials. "
  "What would kill it: evidence that vulnerable populations can't be reached anticipatorily, or that forecasts lack actionable precision. "
  "What this does not claim: it does not claim climate outcomes are currently preventable, prescribes no program, and does not constitute clinical advice."),
 "sig_lens": "The Signature lens reads climate harm as forecastable and concentrated, and asks what anticipatory nursing would protect before the event.",
 "how_it_works": "Researchers study climate-health nursing through heat-morbidity cohorts, wildfire-smoke counseling trials, vulnerability mapping, and disaster-nursing competency work.",
 "key_points": [
  "Climate change already drives nursing workload: heat, smoke, floods, vectors.",
  "The Lancet Countdown quantifies health impacts yearly since 2015.",
  "Nursing lacks defined climate-health competencies and curricula.",
  "Disaster nursing exists but climate harm is chronic, not episodic.",
  "Harms concentrate in the elderly, children, and the already-ill.",
 ],
 "requirements": [
  "Defined anticipatory competencies for climate-health nursing.",
  "Vulnerability registries linked to forecast-triggered outreach.",
  "Proof that anticipatory care beats reactive care in events.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Watts N et al. The Lancet Countdown on health and climate change. Lancet. 2015-2023 series.",
  "American Nurses Association. Climate change position statements. Various.",
  "Leffers J et al. Climate change and nursing. Various; 2017-2022.",
  "International Council of Nurses. Position statements on climate. Various.",
 ],
 "demo_data": {"a": ("heat-wave mortality rise in elders, percent (typical event, approx)", 15.0),
               "b": ("percent scale", 100.0), "bounds": (0.08, 0.25),
               "step1": "heat waves raise elder mortality by double digits - a forecastable nursing emergency",
               "confirm": "anticipatory programs beat reactive care on event-period morbidity",
               "refute": "vulnerable populations prove unreachable anticipatorily or forecasts lack precision"},
},
# ------------------------------------------------------------------ rank 29
{
 "key": "pandemic-surge",
 "name": "Pandemic-Ready Nursing Surge Models",
 "group": "Emergency Preparedness",
 "ladder_rank": 29, "ladder_tier": "advanced",
 "problem": "The next pandemic will need multiples of current nursing capacity overnight - what surge model actually works, given that COVID-19 broke every plan?",
 "description": "Pandemic surge planning assumed tiered staffing, team nursing, and retired-nurse recall; COVID-19 revealed the gaps: team models diluted expertise dangerously, travel markets priced out public hospitals, and the workforce that surged in 2020 burned out by 2021. No validated surge staffing model exists, and the nurses who would surge are fewer than before.",
 "background": "Surge planning grew after SARS (2003) and H1N1 (2009): tiered models, just-in-time training, Medical Reserve Corps. COVID-19 stress-tested them: team nursing (one ICU nurse supervising several non-ICU nurses) kept units open but with debated safety; crisis standards of care were invoked; the workforce contracted afterward. Research now focuses on sustainable surge - models that don't consume the workforce they deploy - and on equity (safety-net hospitals couldn't compete for travelers). As of 2026 surge readiness is lower than in 2019 by most measures.",
 "why_it_matters": "Pandemics are recurring; nursing is the binding constraint on hospital capacity. A surge model that works without breaking the workforce is the difference between a managed crisis and a collapse.",
 "sig_pointer": "The Signature system's proposed approach treats surge as a sustainability problem, not just a capacity problem, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that surge models fail by optimizing peak capacity while ignoring workforce consumption: a model that staffs the surge by burning out its nurses has no second wave. "
  "Assumptions: (1) pandemics come in waves, so sustainability dominates peak capacity; (2) expertise dilution has safety costs that compound; (3) the pre-pandemic workforce is the surge workforce - there is no reserve army. "
  "Reasoning path: a sustainability model reframes surge planning around workforce preservation - rotation, recovery, and expertise protection - explaining why 2020's heroics couldn't be repeated in 2021. "
  "Proposed mechanism: 'sustainable surge' models with built-in rotation and recovery, expertise-protection ratios, and pre-negotiated crisis compensation, tested in exercises and real events. "
  "What would confirm it: sustainable models maintaining safety and staffing across multi-wave events better than peak-capacity models. "
  "What would kill it: evidence that any surge model consumes the workforce equally, or that expertise protection is unaffordable. "
  "What this does not claim: it does not claim any model is ready, prescribes no staffing, and does not constitute clinical advice."),
 "sig_lens": "The Signature lens reads surge as a multi-wave problem, and asks what model would still be standing for the second wave.",
 "how_it_works": "Preparedness researchers study surge through after-action analyses, team-nursing safety studies, exercise evaluations, and workforce-trajectory modeling.",
 "key_points": [
  "COVID-19 broke pre-pandemic surge plans: team models, recall, reserves.",
  "Team nursing kept units open with debated safety costs.",
  "The workforce contracted after 2020; readiness is lower than 2019.",
  "Travel markets priced safety-net hospitals out of surge staffing.",
  "No validated sustainable surge model exists.",
 ],
 "requirements": [
  "Surge models validated for safety across multi-wave events.",
  "Workforce-preservation metrics built into surge planning.",
  "Equity: surge capacity for safety-net hospitals, not just wealthy ones.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "National Academies. Rapid Expert Consultation on surge staffing. 2020.",
  "American Nurses Association. COVID-19 surveys. 2020-2022.",
  "Hick JL et al. Crisis standards of care. Various; 2009-2021.",
  "Buerhaus PI et al. The nursing workforce after COVID-19. Various; 2021-2023.",
 ],
 "demo_data": {"a": ("surge capacity multiple needed in pandemic peaks (approx)", 3.0),
               "b": ("baseline capacity (multiple scale)", 1.0), "bounds": (2.0, 5.0),
               "step1": "pandemics demand multiples of normal capacity from a workforce with no reserve",
               "confirm": "sustainable models beat peak-capacity models across multi-wave events",
               "refute": "all surge models prove equally workforce-consuming"},
},
# ------------------------------------------------------------------ rank 30
{
 "key": "nurse-primary-care",
 "name": "Nurse-Led Primary Care at Scale",
 "group": "Chronic Care",
 "ladder_rank": 30, "ladder_tier": "advanced",
 "problem": "Primary care is collapsing under demand while nurses could fill the gap - what would it take to scale nurse-led primary care without losing quality?",
 "description": "Primary-care physician shortages grow while nurse practitioners deliver primary care with equivalent outcomes in trials and observational studies. Yet scale-up faces scope battles, uneven NP education quality concerns, and payment models built around physicians. The question is no longer whether NPs can do primary care but how to scale it safely and equitably.",
 "background": "NP primary-care outcomes research (Mundinger 2000 JAMA randomized trial showing equivalence; subsequent observational studies) built the evidence base. Scope-of-practice liberalization spread state by state; the VA granted full practice authority in 2016. Concerns persist about variable NP program quality and the adequacy of clinical hours. International models (UK, Netherlands, Canada) show scaled nurse-led primary care working. As of 2026 the evidence supports scale-up; politics and payment lag.",
 "why_it_matters": "Millions lack primary care access; the physician pipeline cannot close the gap in time. Scaled nurse-led primary care is the most plausible path to universal primary-care access.",
 "sig_pointer": "The Signature system's proposed approach treats scale-up as a quality-assurance problem, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that nurse-led primary care scale-up hinges on quality assurance, not scope debates: the model works where competence is verified, and the valid concern is variable preparation, not the role itself. "
  "Assumptions: (1) outcomes depend on preparation quality, which varies; (2) quality is assurable through standardized competency verification; (3) scale without assurance risks the model's legitimacy. "
  "Reasoning path: a quality-assurance model reframes the debate from turf to standards - explaining why the evidence is strong (studies sample well-prepared NPs) and what could break it (scaling the underprepared). "
  "Proposed mechanism: 'assured scale-up' - competency verification, outcome monitoring, and tiered autonomy tied to demonstrated performance, tested against access and quality. "
  "What would confirm it: assured scale-up maintaining outcomes while expanding access in natural experiments. "
  "What would kill it: evidence that quality can't be assured at scale, or that outcomes degrade with rapid expansion regardless. "
  "What this does not claim: it does not claim all NPs are equivalently prepared, takes no scope position, and does not constitute clinical advice."),
 "sig_lens": "The Signature lens reads the primary-care gap as a quality-assurance challenge, and asks what verification would let scale proceed safely.",
 "how_it_works": "Researchers study NP primary care through outcomes comparisons, scope natural experiments, education-quality studies, and international scale-up analyses.",
 "key_points": [
  "NP primary-care outcomes match physicians' in trials and observational studies.",
  "Mundinger's 2000 randomized trial showed equivalence.",
  "The VA granted full practice authority in 2016.",
  "Scope battles and payment models lag the evidence.",
  "Variable NP program quality is the legitimate concern.",
 ],
 "requirements": [
  "Standardized competency verification for scaled practice.",
  "Outcome monitoring that catches quality degradation early.",
  "Payment models that reward primary-care access and outcomes.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Mundinger MO et al. Primary care outcomes in patients treated by nurse practitioners or physicians. JAMA. 2000;283(1):59-68.",
  "Newhouse RP et al. Advanced practice nurse outcomes. Nursing Economics. 2011;29(5):230-250.",
  "Laurant M et al. Nurses as substitutes for doctors in primary care. Cochrane Database of Systematic Reviews. 2018;7:CD001271.",
  "U.S. Department of Veterans Affairs. Full practice authority for APRNs; 2016.",
 ],
 "demo_data": {"a": ("primary-care shortage, millions lacking access (US, approx)", 100.0),
               "b": ("physician pipeline years to close gap (approx)", 10.0), "bounds": (5.0, 20.0),
               "step1": "a hundred million lack primary care while the physician pipeline needs a decade - the arithmetic demands nurses",
               "confirm": "assured scale-up maintains outcomes while expanding access",
               "refute": "quality proves unassurable at scale with outcomes degrading on expansion"},
},
# ------------------------------------------------------------------ rank 31
{
 "key": "compassion-fatigue",
 "name": "Compassion Fatigue Mechanisms",
 "group": "Workforce",
 "ladder_rank": 31, "ladder_tier": "advanced",
 "problem": "Nurses who care the most sometimes lose the ability to care - what is compassion fatigue mechanistically, and how does it differ from burnout?",
 "description": "Compassion fatigue (Figley) - the cost of caring, secondary traumatic stress from absorbing patients' suffering - is distinct from burnout's exhaustion: it strikes the empathic, can arrive suddenly, and responds to different interventions. Yet measurement conflates the two, most studies are cross-sectional, and the neurobiology (empathy circuits, oxytocin, trauma physiology) is barely mapped in nurses.",
 "background": "Figley defined compassion fatigue in the 1990s from trauma-therapy work; Stamm's ProQOL scale (measuring compassion satisfaction versus fatigue) made it researchable in nursing. Studies show it predicts intent to leave and varies by specialty (oncology, palliative, emergency highest). Interventions - mindfulness, resilience, Schwartz rounds - show small effects. The mechanistic frontier distinguishes empathic distress (feeling with) from empathic concern (feeling for), with different neural correlates and different remedies. As of 2026 the construct is measured but mechanistically shallow.",
 "why_it_matters": "Compassion fatigue takes out the nurses patients need most - the deeply empathic ones. Understanding its mechanism would let the profession protect empathy instead of watching it burn.",
 "sig_pointer": "The Signature system's proposed approach treats empathic distress and empathic concern as distinct targets, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that 'compassion fatigue' conflates two processes: empathic distress (absorbing suffering, depleting) and empathic concern (caring action, sustaining) - and that interventions fail by treating both as one. "
  "Assumptions: (1) distress and concern have different neural correlates; (2) concern is protective while distress is depleting; (3) the balance is trainable. "
  "Reasoning path: a two-process model explains why some empathic nurses thrive (concern-dominant) while others deplete (distress-dominant) and predicts that shifting the balance beats generic resilience. "
  "Proposed mechanism: 'empathy retraining' that builds concern-dominant responding (compassion training paradigms from contemplative science), tested against ProQOL trajectories and retention. "
  "What would confirm it: retraining shifting nurses toward concern-dominance with better fatigue outcomes than generic programs. "
  "What would kill it: evidence that distress and concern can't be separated in practice, or that the balance isn't trainable. "
  "What this does not claim: it does not claim empathy is currently trainable at scale, prescribes no program, and does not constitute clinical advice."),
 "sig_lens": "The Signature lens reads compassion fatigue as two processes wearing one name, and asks what would shift the balance toward the sustaining one.",
 "how_it_works": "Researchers study compassion fatigue through ProQOL surveys, contemplative-science training trials, neuroimaging of empathy, and specialty comparisons.",
 "key_points": [
  "Compassion fatigue is secondary traumatic stress from absorbing suffering (Figley).",
  "It differs from burnout: it strikes the empathic, can arrive suddenly.",
  "Stamm's ProQOL measures compassion satisfaction versus fatigue.",
  "Empathic distress (depleting) differs neurally from empathic concern (sustaining).",
  "The construct is measured but mechanistically shallow.",
 ],
 "requirements": [
  "Separation of distress from concern in measurement.",
  "Proof that the balance is trainable in working nurses.",
  "Interventions beating generic resilience on fatigue trajectories.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Figley CR. Compassion Fatigue: Coping with Secondary Traumatic Stress Disorder. Brunner/Mazel; 1995.",
  "Stamm BH. The Concise ProQOL Manual. 2nd ed.; 2010.",
  "Singer T, Klimecki OM. Empathy and compassion. Current Biology. 2014;24(18):R875-R878.",
  "Cocker F, Joss N. Compassion fatigue among healthcare workers. PLoS One. 2016;11(6):e0157239.",
 ],
 "demo_data": {"a": ("nurses in high-empathy specialties reporting fatigue, percent (approx)", 40.0),
               "b": ("percent scale", 100.0), "bounds": (0.25, 0.55),
               "step1": "the most empathic specialties report the most fatigue - caring has a measurable cost",
               "confirm": "retraining shifts nurses toward concern-dominance beating generic programs",
               "refute": "distress and concern prove inseparable in practice"},
},
# ------------------------------------------------------------------ rank 32
{
 "key": "interprofessional",
 "name": "Interprofessional Collaboration Measurement",
 "group": "Teamwork",
 "ladder_rank": 32, "ladder_tier": "advanced",
 "problem": "Everyone endorses teamwork, but can collaboration itself be measured - and does better-measured teamwork produce better outcomes?",
 "description": "Interprofessional collaboration - nurses, physicians, pharmacists, therapists working as a team - is endorsed universally and measured poorly. Instruments exist (team climate, collaboration scales) but link weakly to outcomes; team training (TeamSTEPPS) shows mixed effects; and the structural barriers (hierarchy, rounding practices, EHR silos) persist regardless of training.",
 "background": "Teamwork science entered healthcare from aviation in the 2000s (TeamSTEPPS, AHRQ/DoD). Instruments proliferated: the Team Climate Inventory, Jefferson Scale of Attitudes, collaborative-practice scales. But the measurement-outcome link is thin: most studies measure attitudes, not behaviors, and behavior-outcome studies are scarce. Structural research shows hierarchy and communication architecture matter more than training. As of 2026 collaboration is preached, trained sporadically, and rarely measured as behavior.",
 "why_it_matters": "Care is delivered by teams but managed as individuals: without measuring collaboration, the largest determinant of safety culture stays invisible and unimprovable.",
 "sig_pointer": "The Signature system's proposed approach treats collaboration as observable communication behavior, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that collaboration measurement fails because it surveys attitudes while collaboration is behavior: who speaks to whom, when, about what - and the behavior is observable in communication data. "
  "Assumptions: (1) collaborative behavior leaves traces (consult patterns, rounding participation, message networks); (2) the traces predict outcomes better than attitude surveys; (3) behavior is modifiable through structure. "
  "Reasoning path: a behavioral model explains the attitude-outcome gap and predicts that communication-trace metrics will outperform surveys - and that structural changes (joint rounding, shared EHR views) will move behavior where training doesn't. "
  "Proposed mechanism: 'collaboration telemetry' - measuring team communication behavior from routine data, linked to outcomes, with structural interventions tested against the telemetry. "
  "What would confirm it: telemetry metrics predicting outcomes better than surveys, and structural interventions moving telemetry and outcomes together. "
  "What would kill it: evidence that communication traces don't predict outcomes, or that behavior is unmodifiable by structure. "
  "What this does not claim: it does not claim any team is currently dysfunctional, prescribes no training, and does not constitute clinical advice."),
 "sig_lens": "The Signature lens reads teamwork as behavior leaving traces, and asks what telemetry would make collaboration visible.",
 "how_it_works": "Team researchers study collaboration through communication-network analysis, TeamSTEPPS trials, ethnography of rounds, and hierarchy-structure studies.",
 "key_points": [
  "Collaboration is endorsed universally and measured poorly.",
  "Instruments measure attitudes; behavior-outcome studies are scarce.",
  "TeamSTEPPS training shows mixed effects on outcomes.",
  "Hierarchy and communication architecture matter more than training.",
  "EHR silos structurally separate the professions.",
 ],
 "requirements": [
  "Behavioral collaboration metrics validated against outcomes.",
  "Proof that structural changes move collaboration behavior.",
  "Measurement integrated into routine quality systems.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "King HB et al. TeamSTEPPS: team strategies and tools to enhance performance and patient safety. AHRQ; 2008.",
  "Reeves S et al. Interprofessional teamwork for health and social care. Wiley-Blackwell; 2010.",
  "Weaver SJ et al. Teamwork and patient safety. Various; 2010-2018.",
  "Zwarenstein M et al. Interprofessional collaboration: effects on practice and outcomes. Cochrane Database of Systematic Reviews. 2009;3:CD000072.",
 ],
 "demo_data": {"a": ("team-training studies measuring behavior versus attitudes (percent behavioral, approx)", 20.0),
               "b": ("percent scale", 100.0), "bounds": (0.1, 0.35),
               "step1": "a minority of teamwork studies measure behavior - the field surveys attitudes about teamwork",
               "confirm": "telemetry metrics beat surveys on outcome prediction with structural fixes moving both",
               "refute": "communication traces prove not to predict outcomes"},
},
# ------------------------------------------------------------------ rank 33
{
 "key": "theory-practice",
 "name": "Theory-to-Practice Translation Gap",
 "group": "Education",
 "ladder_rank": 33, "ladder_tier": "advanced",
 "problem": "Nursing students learn theory, then meet the ward - and the theory evaporates. Why does nursing knowledge fail to transfer, and what closes the gap?",
 "description": "The theory-practice gap is nursing education's oldest complaint: students master pathophysiology and care plans in classrooms, then can't apply them under clinical load. Preceptorship, simulation, and competency-based education each promise to close it; each helps partially. The deeper issue may be that classroom knowledge is organized for exams while clinical knowledge is organized for action - a transfer problem, not a teaching problem.",
 "background": "The gap was named in the 1970s-80s as nursing moved into universities. Responses cycled: more clinical hours, then simulation (high-fidelity manikins, now VR), then competency-based education and entrustable professional activities. Evidence shows simulation transfers to performance, but the ward's cognitive load - interruptions, time pressure, emotional labor - defeats classroom organization. Cognitive-load theory and situated cognition reframed the problem: knowledge must be learned in its use context. As of 2026 the gap persists wherever education and practice are organizationally separated.",
 "why_it_matters": "The gap produces the novice's dangerous first year: knowledge without judgment, theory without timing. Closing it would make new graduates safe faster and reduce the preceptorship burden on experienced nurses.",
 "sig_pointer": "The Signature system's proposed approach treats clinical knowledge as organized for action, not for exams, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that the theory-practice gap is a knowledge-organization mismatch: classroom knowledge is indexed by disease while clinical knowledge must be indexed by situation - and transfer fails because the indexes don't align. "
  "Assumptions: (1) expert nurses organize knowledge situationally; (2) novices inherit disease-indexed knowledge; (3) re-indexing is teachable through situated practice. "
  "Reasoning path: an indexing model explains why more clinical hours help (they build the situational index) and why simulation transfers partially (it simulates situations) - the target is the index, not the hours. "
  "Proposed mechanism: 'situational indexing' curricula that teach theory already organized by clinical situation, tested against transfer measures and time-to-competence. "
  "What would confirm it: situationally indexed curricula outperforming traditional ones on transfer and time-to-competence. "
  "What would kill it: evidence that the gap is purely experiential (only hours close it), not organizational. "
  "What this does not claim: it does not claim curricula are currently failing, prescribes no pedagogy, and does not constitute clinical advice."),
 "sig_lens": "The Signature lens reads the gap as mismatched indexes - disease versus situation - and asks what re-indexing would let knowledge arrive on time.",
 "how_it_works": "Education researchers study transfer through simulation-effectiveness trials, cognitive-load studies, preceptorship models, and competency-based education evaluations.",
 "key_points": [
  "The theory-practice gap is nursing education's oldest complaint.",
  "Simulation transfers to performance but partially.",
  "Classroom knowledge is indexed by disease; clinical knowledge by situation.",
  "Cognitive-load theory reframed the problem as situated, not just taught.",
  "Competency-based education and EPAs are the current reform wave.",
 ],
 "requirements": [
  "Curricula teaching theory indexed by clinical situation.",
  "Transfer measures beyond exam scores.",
  "Proof of faster time-to-competence without more clinical hours.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Benner P. From Novice to Expert. Addison-Wesley; 1984.",
  "Cook DA et al. Technology-enhanced simulation for health professions education. JAMA. 2011;306(9):978-988.",
  "van Merrienboer JJG, Sweller J. Cognitive load theory in health professional education. Medical Education. 2010;44(1):85-89.",
  "Frank JR et al. Competency-based medical education: theory to practice. Medical Teacher. 2010;32(8):638-645.",
 ],
 "demo_data": {"a": ("novice nurses reporting theory-practice shock, percent (approx)", 70.0),
               "b": ("percent scale", 100.0), "bounds": (0.5, 0.85),
               "step1": "most novices report the classroom did not prepare them for the ward - the gap is the norm",
               "confirm": "situationally indexed curricula beat traditional ones on transfer and time-to-competence",
               "refute": "the gap proves purely experiential with only hours closing it"},
},
# ------------------------------------------------------------------ rank 34
{
 "key": "nursing-presence",
 "name": "Quantifying Nursing Presence",
 "group": "Caring Science",
 "ladder_rank": 34, "ladder_tier": "advanced",
 "problem": "Patients say the nurse's presence healed them - but what is presence, can it be measured, and does it change outcomes?",
 "description": "Nursing presence - being attentively, intentionally with the patient - is caring science's central concept (Parse, Watson, Benner): patients consistently rate it among the most healing aspects of care. Yet it resists measurement: time-in-room proxies miss the quality, patient ratings conflate it with satisfaction, and no trial has shown presence interventions moving clinical outcomes. The most valued thing nurses do may be the least measurable.",
 "background": "Presence was theorized in the 1980s-90s (Gardner's concept analysis; Watson's caritas processes; Benner's novice-to-expert). Qualitative research richly describes it; quantitative research stalls on operationalization. Time-motion studies show nurses spend a minority of shifts in direct patient contact - the 'presence deficit' - but more time doesn't equal more presence. Early measurement attempts (presence scales) show reliability without outcome linkage. As of 2026 presence is nursing's most cherished and least scientific concept.",
 "why_it_matters": "If presence heals, then staffing, technology, and workflow designs that destroy it are harming patients invisibly. Measuring presence would let the profession defend its most human work in the language of outcomes.",
 "sig_pointer": "The Signature system's proposed approach treats presence as attentional quality measurable through its effects, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that presence is attentional quality - sustained, patient-directed attention - and that it is measurable through convergent effects: patient physiological calming, recall of the encounter, and nurse attentional markers. "
  "Assumptions: (1) presence is a real attentional state, not just kindness; (2) it produces measurable patient effects; (3) the effects converge on a presence construct distinct from satisfaction. "
  "Reasoning path: an attentional model explains why time-in-room fails as a proxy (attention varies within time) and predicts that effect-convergence measurement will succeed where proxies failed. "
  "Proposed mechanism: 'presence measurement' fusing patient physiological response, encounter recall, and attentional markers into a validated presence instrument, tested against outcomes. "
  "What would confirm it: the instrument predicting outcomes (anxiety, pain, satisfaction-with-care distinctions) beyond time and satisfaction measures. "
  "What would kill it: evidence that presence has no measurable effects beyond satisfaction, or that the construct can't be separated from general quality. "
  "What this does not claim: it does not claim presence is currently measurable, prescribes no practice, and does not constitute clinical advice."),
 "sig_lens": "The Signature lens reads presence as attention with healing effects, and asks what convergence of effects would make it visible.",
 "how_it_works": "Caring-science researchers study presence through qualitative inquiry, presence-scale development, time-motion studies, and patient-rated healing-factor research.",
 "key_points": [
  "Presence is caring science's central concept (Parse, Watson, Benner).",
  "Patients rate it among the most healing aspects of care.",
  "Time-in-room proxies miss attentional quality.",
  "Presence scales show reliability without outcome linkage.",
  "Nurses spend a minority of shifts in direct patient contact.",
 ],
 "requirements": [
  "A validated presence instrument distinct from satisfaction.",
  "Proof that presence moves clinical outcomes.",
  "Workflow designs that protect presence from erosion.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Watson J. Nursing: The Philosophy and Science of Caring. Rev. ed. University Press of Colorado; 2008.",
  "Benner P. From Novice to Expert. Addison-Wesley; 1984.",
  "Gardner DL. Presence. In: Nursing Interventions Classification. Various.",
  "Finfgeld-Connett D. Meta-synthesis of presence in nursing. Journal of Advanced Nursing. 2006;55(6):708-714.",
 ],
 "demo_data": {"a": ("nurse shift spent in direct patient contact, percent (approx)", 30.0),
               "b": ("percent scale", 100.0), "bounds": (0.2, 0.45),
               "step1": "nurses spend a minority of shifts with patients - the presence deficit is structural",
               "confirm": "the instrument predicts outcomes beyond time and satisfaction measures",
               "refute": "presence proves to have no measurable effects beyond satisfaction"},
},
]


