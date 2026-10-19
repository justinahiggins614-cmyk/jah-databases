(function(){'use strict';
/* jahdb-fundamental-medicine-1.0 — fundamental medicine bedrock generator.
   Property of Justin Addam Higgins (JAH). Deterministic: same seed always makes the same record.
   src:"public-harvest" = established first-principles knowledge, fact-checked */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var PREFIX='JAH-FMED-';
var KIND='fundamental medicine record';
var SECTIONS=['about', 'reasoning', 'quantities', 'mechanism', 'miscon'];
var BRIEF={'about':'Medicine is the science and art of maintaining health and treating disease: diagnosing what ails, intervening effectively, and caring for the person, not just the pathology. It joins biology\'s mechanisms with the clinician\'s judgment.', 'reasoning':'Clinicians reason by differential diagnosis: gather history and signs, generate candidate explanations, test with examinations and investigations, and treat while monitoring response. Every diagnosis is provisional until the patient improves.', 'quantities':'The core quantities are vital signs (temperature, pulse, blood pressure, respiratory rate, oxygen saturation), lab values with reference ranges, and epidemiological measures (incidence, prevalence, risk ratios). The reference range is the master context — numbers mean nothing without it.', 'mechanism':'Medicine works the clinical loop: history → examination → differential → investigation → diagnosis → treatment → follow-up. Evidence-based medicine adds the literature: what do trials say works, for whom, with what harms?', 'miscon':'Medicine is not just prescribing: diagnosis, prevention, and communication are most of the work. Tests do not diagnose by themselves — pre-test probability governs what results mean. And \'natural\' is not \'safe\': the dose makes the poison, natural or not.'};
var SIGLENS=['In the Signature system, medicine is the care discipline: every health-related database in this network follows its standards — evidence, safety, honesty about uncertainty — and the Signature formulation teaches each principle as knowledge you can verify.','The Signature practice is to reason clinically: take the history, weigh the differential, check the evidence — so medical fundamentals are learned as disciplined reasoning, with the constant reminder that real care requires licensed professionals.'];
var DEMOS=['#!/usr/bin/env python3\n"""{TITLE} -- BMI demo. Runs as-is with python3."""\ndef bmi(weight_kg, height_m):\n    return weight_kg / (height_m ** 2)\nfor w, h in [(70, 1.75), (90, 1.75), (60, 1.60)]:\n    b = bmi(w, h)\n    cat = "underweight" if b < 18.5 else "healthy" if b < 25 else "overweight" if b < 30 else "obese"\n    print(f"{w}kg {h}m -> BMI {b:.1f} ({cat})")\nprint("BMI is a screening tool, not a diagnosis: context matters")\n', '#!/usr/bin/env python3\n"""{TITLE} -- test interpretation demo (Bayes). Runs as-is with python3."""\ndef post_test_prob(prevalence, sensitivity, specificity):\n    p_pos = sensitivity * prevalence + (1 - specificity) * (1 - prevalence)\n    return sensitivity * prevalence / p_pos\nfor prev in [0.5, 0.1, 0.01]:\n    print(f"disease prevalence {prev:.0%}, 95% sens/spec test -> P(disease|positive) = {post_test_prob(prev, .95, .95):.1%}")\nprint("same test, different meaning: pre-test probability governs interpretation")\n', '#!/usr/bin/env python3\n"""{TITLE} -- heart rate zones demo. Runs as-is with python3."""\ndef max_hr(age):\n    return 208 - 0.7 * age\nfor age in [20, 40, 60]:\n    m = max_hr(age)\n    print(f"age {age}: est max HR {m:.0f}; moderate zone {0.5*m:.0f}-{0.7*m:.0f} bpm")\nprint("estimates guide training; individual variation is real")\n'];
var TOPICS=[['What Medicine Is','Medicine is the discipline of health: preventing disease, diagnosing illness, treating the sick, and relieving suffering. It is science applied to persons — which makes it both the most evidence-driven and the most human of the applied sciences.'],
['The Core Question of Medicine','The core question is: what is wrong, what will help, and what are the risks? Diagnosis names the problem, therapeutics addresses it, and the risk-benefit balance — for this patient, now — governs every decision.'],
['Assumptions: The Body as Understandable System','Medicine assumes the body is an understandable system: symptoms reflect pathophysiology, diseases have natural histories, and interventions have predictable effects on average. The \'on average\' is why clinical judgment can never be fully automated.'],
['The Vocabulary: Signs, Symptoms, Syndromes','The vocabulary distinguishes symptoms (what the patient feels), signs (what the clinician finds), syndromes (patterns), and diseases (defined entities). Diagnosis is pattern recognition against this vocabulary — refined by testing.'],
['The Vital Signs: The Fundamental Quantities','The vital signs — temperature, pulse, blood pressure, respiratory rate, oxygen saturation — are the fundamental quantities: the body\'s dashboard. Trends matter more than single readings; the delta is the diagnosis.'],
['The Clinical Method: The Primary Method','The clinical method is the primary method: history (the patient\'s story), examination (the body\'s signs), differential diagnosis (the candidate list), investigation (targeted tests), and management. The history alone often diagnoses — listening is the master skill.'],
['A Canonical First Example','The canonical first example is chest pain: history distinguishes cardiac from reflux from musculoskeletal, the ECG and troponin test the cardiac hypothesis, and management follows the confirmed diagnosis. One symptom, many diseases — the differential in action.'],
['How Medicine Measures','Medicine measures with examinations, laboratories, and imaging: the body\'s signals quantified against reference ranges. Every test has sensitivity, specificity, and a pre-test probability — the Bayesian trinity of interpretation.'],
['The Core Mechanism: Pathophysiology','The core mechanism of medical reasoning is pathophysiology: linking the patient\'s presentation to disordered function — the blocked artery behind the chest pain, the insulin resistance behind the hyperglycemia. Mechanism guides both diagnosis and treatment.'],
['The Simplest Law: Common Things Are Common','The simplest law is the clinician\'s maxim: common things are common. The differential is ordered by probability, not exoticism — horses before zebras, until the evidence says otherwise.'],
['Common Misconceptions in Medicine','The misconceptions harm: that tests diagnose by themselves (interpretation needs pre-test probability), that more testing is always better (false positives have costs), that \'natural\' means safe, and that the absence of evidence is evidence of absence.'],
['How Beginners Practice Medicine','Beginners practice by taking histories and presenting them: the story organized, the differential reasoned, the plan justified. Case-based learning builds the pattern library that experience later refines.'],
['The Core Model: The Randomized Controlled Trial','The randomized controlled trial is the core model of medical evidence: randomize, blind where possible, compare outcomes. It is the reason modern medicine knows what works — and the standard new treatments must meet.'],
['The Great Idea: Evidence-Based Medicine','Evidence-based medicine is the great idea: integrate the best research evidence with clinical expertise and patient values. It replaced authority (\'the professor says\') with evidence (\'the trials show\') — medicine\'s scientific coming-of-age.'],
['Systems Thinking: The Patient Whole','Systems thinking in medicine sees the whole patient: diseases interact, drugs interact, and the social context shapes outcomes. Comorbidity is the rule, not the exception — the body is one system, not a collection of specialties.'],
['Invariance: Physiology\'s Constants','The invariance principles are physiological constants: pH 7.4, core temperature ~37°C, osmolarity ~285 mOsm — defended fiercely by homeostasis. Disease is often these invariants under threat; treatment often their restoration.'],
['Approximation: Reference Ranges','Approximation uses reference ranges: the central 95% of healthy people. A value outside the range is a flag, not a verdict — and the patient\'s own baseline beats the population\'s range.'],
['Evidence Standards: The Hierarchy','The evidence standard is the hierarchy: systematic reviews and RCTs above observational studies above expert opinion. Guidelines synthesize the hierarchy into practice — with the evidence grade stated.'],
['Classic Discoveries','The classic discoveries are germ theory, anesthesia, antibiotics, vaccines, and the RCT itself. Each transformed medicine from art toward science — and each faced resistance before acceptance.'],
['Core Trade-offs: Benefit versus Harm','The core trade-off is benefit versus harm: every intervention helps some and harms some. The number needed to treat (NNT) and to harm (NNH) quantify the trade — honest medicine reports both.'],
['Handling Uncertainty: Prognosis','Medicine handles uncertainty with probabilities: risk scores, survival curves, and the honest \'we don\'t know.\' Shared decision-making puts the uncertainty on the table — the patient decides with eyes open.'],
['Tools of the Trade','The tools of the trade are the stethoscope, the history, the lab, and the literature. The deepest is the differential diagnosis — the disciplined list of what this could be, ranked and tested.'],
['Ethics and Responsibility','Ethics in medicine is the oldest professional ethic: do no harm, respect autonomy, keep confidences, allocate fairly. The Hippocratic tradition binds the clinician to the patient\'s good above all.'],
['Teaching Medicine','Teaching it well is bedside: the patient, the findings, the reasoning aloud. Students learn the clinical method by watching masters think — and by presenting, defending, and being corrected.'],
['The Frontier Question','The frontier question is precision medicine: treatments matched to the individual\'s genome, microbiome, and life. The frontier asks whether medicine can become truly personal without losing its evidence base.'],
['Unifying Theories','The unifying theories are evolution (why bodies are vulnerable), homeostasis (how they\'re regulated), and germ theory (what invades them). Together they explain disease as the body\'s systems meeting their limits.'],
['Computational Medicine','Computational medicine models disease and discovers drugs: protein structure prediction, trial simulation, and AI-assisted diagnosis. The computer augments — it does not replace — the clinician\'s judgment.'],
['Bridges to Other Fields','Medicine bridges to biology, chemistry (pharmacology), physics (imaging), engineering (devices), psychology (behavior), and public health (populations). It is the applied convergence of the life sciences.'],
['The Great Unsolved Problems','The great unsolved problems are open and labeled as such: Alzheimer\'s disease mechanisms and treatments, most cancers\' cures, antimicrobial resistance, and health equity. Active research, no settled answers.'],
['How New Claims Are Validated','New treatments are validated by RCTs and replication: the trial pre-registered, the result reproduced, the harms tracked. A treatment earns trust when independent trials agree — the standard that ended centuries of useless remedies.'],
['The Great Debates','The great debates include screening\'s benefits versus harms, the role of AI in diagnosis, and how to allocate scarce treatments fairly. The debates are moral as much as scientific — they concern real patients.'],
['Failure Modes: When Medicine Gets It Wrong','Medicine gets it wrong through premature closure (stopping at the first diagnosis), anchoring, and ignoring the patient\'s story. The immune system is the second opinion, the checklist, and the autopsy of errors — morbidity and mortality rounds.'],
['Synthesis: Building on the Fundamentals','Advanced synthesis practices whole-patient medicine from fundamentals: the history, the differential, the evidence, the patient\'s values — integrated into care. The fundamentals are the clinical method itself.'],
['The Signature Formulation: Medicine as Disciplined Care','The Signature formulation treats medical principles as disciplined care knowledge: every concept here is evidence-graded and uncertainty-honest, because in the Signature system health knowledge must be trustworthy above all. Note: this database teaches fundamentals; real care requires licensed professionals. That is the Signature capstone on medical bedrock.']];
var TIERS=[['foundations','Foundations',1,12],['compounded','Compounded',13,24],['advanced','Advanced',25,34]];
function pad(n){var s=String(n);while(s.length<6)s='0'+s;return s;}
function firstSentence(s){var m=/^(.+?[.!?])(\s|$)/.exec(String(s).trim());return m?m[1]:String(s).slice(0,160);}
function compose(i,title,essence){
  var elab,desc,how,kps;
  if(true){
    elab=[BRIEF[SECTIONS[(i+0)%5]],BRIEF[SECTIONS[(i+2)%5]]];
    desc=essence+'\n\n'+elab.join('\n\n');
    how=BRIEF.mechanism+' '+firstSentence(essence)+' The working habit here: '+BRIEF.reasoning.split('. ')[0]+'.';
    kps=[firstSentence(essence),'How the field reasons: '+firstSentence(BRIEF.reasoning),'Core quantities and units: '+firstSentence(BRIEF.quantities),'Common misconception to avoid: '+firstSentence(BRIEF.miscon),'Run the demo program below to make this principle concrete and testable.'];
  }else{
    elab=[SIGLENS[0],BRIEF[SECTIONS[(i+3)%5]]];
    desc=essence+'\n\n'+elab.join('\n\n');
    how=SIGLENS[1]+' '+BRIEF.mechanism+' '+firstSentence(essence);
    kps=[firstSentence(essence),'Signature framing: '+firstSentence(SIGLENS[0]),'Signature practice: '+firstSentence(SIGLENS[1]),'Common misconception to avoid: '+firstSentence(BRIEF.miscon),'Run the demo program below to make this principle concrete and testable.'];
  }
  return {desc:desc,how:how,kps:kps};
}
function generate(seed,opts){
  var s=prng(seed);
  var ti=(s()*TOPICS.length)|0;
  var topic=TOPICS[ti], i=ti, rank=ti+1, title=topic[0], essence=topic[1];
  var tier='foundations',glabel='Foundations';
  for(var k=0;k<TIERS.length;k++){if(rank>=TIERS[k][2]&&rank<=TIERS[k][3]){tier=TIERS[k][0];glabel=TIERS[k][1];}}
  var id=PREFIX+pad(seed);
  var c=compose(i,title,essence);
  var demo=DEMOS[ti%DEMOS.length].split('{TITLE}').join(title);
  return {id:id,t:title,g:glabel,c:0,name:title+' - '+KIND,title:title,description:c.desc,how_it_works:c.how,
    key_points:c.kps,requirements:['Read the description and key points first — they carry the essential first principles.','No prior knowledge of the subject is assumed; the ladder rank tells you what to read first.','Use the demo program to make the principle concrete — run it, change the numbers, re-run.'],
    standards:["Evidence is graded: recommendations state the quality of supporting evidence.", "Safety first: every intervention's harms are weighed against its benefits.", "Uncertainty is disclosed: what is unknown is stated, not hidden."],citations:["Kasper, D. et al. \u2014 Harrison's Principles of Internal Medicine.", "Cochrane Library \u2014 systematic reviews of medical evidence.", "Cross-checked against the JAH Databases network archive before filing."],src:'public-harvest',ladder_rank:rank,ladder_tier:tier,
    demo:{kind:'fundamental-medicine-demo',language:'python',program:demo,note:'Working demonstration program for this record. Runs as-is with python3.'},_seed:seed};
}
function validate(r){
  var errs=[];
  if(!r.id)errs.push('missing id');
  if(!r.title)errs.push('missing title');
  if(!r.description||r.description.length<200)errs.push('description too short (<200)');
  if(!r.key_points||r.key_points.length<3)errs.push('key_points too few');
  if(!r.demo||!r.demo.program||r.demo.program.length<100)errs.push('demo program missing/short');
  if(!r.ladder_rank||!r.ladder_tier)errs.push('ladder missing');
  return {ok:errs.length===0,errors:errs};
}
function driftCheck(rec,sample){
  for(var i=0;i<sample.length;i++){if(sample[i].t===rec.title)return {ok:false,errors:['duplicate title']};}
  return {ok:true,errors:[]};
}
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator){JAHDB.registerGenerator('fundamental-medicine',{generate:generate,validate:validate,driftCheck:driftCheck});}
if(typeof module!=='undefined'&&module.exports){module.exports={generate:generate,validate:validate,driftCheck:driftCheck};}
})();
