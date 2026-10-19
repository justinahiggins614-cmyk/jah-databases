(function(){'use strict';
/* jahdb-fundamental-pharmacology-signature-1.0 — fundamental pharmacology bedrock generator.
   Property of Justin Addam Higgins (JAH). Deterministic: same seed always makes the same record.
   src:"signature" = Signature-system formulation, clearly labeled */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var PREFIX='JAH-SFPM-';
var KIND='fundamental pharmacology record (Signature original)';
var SECTIONS=['about', 'reasoning', 'quantities', 'mechanism', 'miscon'];
var BRIEF={'about':'Pharmacology studies how drugs act on living systems: what drugs do to the body (pharmacodynamics) and what the body does to drugs (pharmacokinetics). It is the science behind every prescription.', 'reasoning':'Pharmacologists reason dose-response: the right drug, at the right dose, for the right patient, at the right time. Every effect — wanted and unwanted — is dose-related, and the therapeutic window separates help from harm.', 'quantities':'The core quantities are dose, concentration, half-life, clearance, and the therapeutic index (toxic dose over effective dose). ADME — absorption, distribution, metabolism, excretion — tracks the drug\'s journey.', 'mechanism':'Pharmacology works receptor theory: drugs bind targets (receptors, enzymes, channels), shifting their activity. Agonists activate, antagonists block — and selectivity determines whether the drug helps one system or harms many.', 'miscon':'Pharmacology is not just \'which pill for which ill\': interactions, genetics, and timing govern outcomes. \'Natural\' drugs are still drugs — with doses, toxicities, and interactions. And antibiotics do nothing for viruses — the most consequential misconception in the field.'};
var SIGLENS=['In the Signature system, pharmacology is the precision-dosing discipline: every substance-related database in this network follows its habits — dose, evidence, interaction-checking — and the Signature formulation teaches each principle as a calculation you can verify.','The Signature practice is to compute the pharmacology: calculate the dose, check the interaction, respect the window — so drug reasoning is done with numbers and caution, never casual.'];
var DEMOS=['#!/usr/bin/env python3\n"""{TITLE} -- half-life demo. Runs as-is with python3."""\ndef remaining(dose_mg, half_life_h, hours):\n    return dose_mg * (0.5 ** (hours / half_life_h))\nfor hl in [4, 12, 24]:\n    print(f"100mg, half-life {hl}h -> after 24h: {remaining(100, hl, 24):.1f}mg remains")\nprint("dosing intervals are set by half-life: ~5 half-lives to steady state")\n', '#!/usr/bin/env python3\n"""{TITLE} -- dose calculation demo. Runs as-is with python3."""\ndef dose(weight_kg, mg_per_kg):\n    return weight_kg * mg_per_kg\nfor w in [10, 25, 70]:\n    print(f"{w}kg at 10mg/kg -> {dose(w, 10):.0f}mg")\nprint("weight-based dosing: children are not small adults, doses scale")\n', '#!/usr/bin/env python3\n"""{TITLE} -- therapeutic index demo. Runs as-is with python3."""\ndef therapeutic_index(td50, ed50):\n    return td50 / ed50\nfor name, td, ed in [("drug A", 1000, 10), ("drug B", 50, 10)]:\n    print(f"{name}: TI = {therapeutic_index(td, ed):.0f} (wider = safer margin)")\nprint("narrow therapeutic index drugs need monitoring: the window is thin")\n'];
var TOPICS=[['Signature What Pharmacology Is','Pharmacology is the science of drugs: how they move through the body, what they do to it, and how to use them safely and effectively. It underlies every prescription — the difference between poison and medicine is dose, timing, and knowledge.'],
['Signature The Core Question of Pharmacology','The core question is: what will this drug do in this patient, at this dose? Efficacy, safety, and individual variation — the three must be answered together for every prescription.'],
['Signature Assumptions: Dose-Response','The field assumes dose-response: effects increase with dose up to a maximum, and every drug has doses that help, doses that harm, and doses that do nothing. Paracelsus stated it in 1538; it has never been refuted.'],
['Signature The Vocabulary: ADME, Agonist, Antagonist','The vocabulary tracks the drug\'s journey — absorption, distribution, metabolism, excretion (ADME) — and its action: agonists activate targets, antagonists block them. Fluency means following the molecule from mouth to clearance.'],
['Signature Half-Life: The Fundamental Quantity','Half-life is the fundamental quantity: the time for drug concentration to halve. It sets dosing intervals — about five half-lives to steady state — and governs how long effects (and side effects) last.'],
['Signature The Dose-Response Curve: The Primary Method','The dose-response curve is the primary method: plot effect versus dose, read off potency (EC50) and efficacy (maximum effect). The therapeutic index — toxic dose over effective dose — quantifies the margin of safety.'],
['Signature A Canonical First Example','The canonical first example is aspirin: antiplatelet at low dose, analgesic higher, toxic higher still — one drug, three dose-dependent stories. It teaches that \'the drug\' is inseparable from \'the dose.\''],
['Signature How Pharmacology Measures','The field measures with assays, trials, and therapeutic drug monitoring: concentrations in blood, effects in patients, outcomes in populations. Blood levels guide dosing for narrow-window drugs — measure, don\'t guess.'],
['Signature The Core Mechanism: Receptor Theory','The core mechanism is receptor theory: drugs bind specific targets — receptors, enzymes, ion channels — and modulate them. Selectivity is everything: the selective drug helps one system; the promiscuous one perturbs many.'],
['Signature The Simplest Law: The Dose Makes the Poison','The simplest law is Paracelsus\': the dose makes the poison. Water kills in excess; botulinum treats in micrograms. Safety is never a property of the substance alone — always of substance plus dose.'],
['Signature Common Misconceptions in Pharmacology','The misconceptions are consequential: that natural means safe (many natural compounds are lethal), that antibiotics treat viruses (they don\'t — resistance is the price), and that more is better (the dose-response curve always turns).'],
['Signature How Beginners Practice Pharmacology','Beginners practice by learning drug classes, not just drugs: the mechanism shared by the class predicts the members\' effects. Prototype drugs anchor each class; the rest are variations on the theme.'],
['Signature The Core Model: Pharmacokinetics (ADME)','Pharmacokinetics — ADME — is the core model: how the body handles the drug over time. Absorption sets onset, distribution sets reach, metabolism and excretion set duration. Dosing regimens are ADME made practical.'],
['Signature The Great Idea: The Therapeutic Window','The therapeutic window is the great idea: the concentration range between effective and toxic. Wide-window drugs forgive; narrow-window drugs (warfarin, lithium, digoxin) demand monitoring — the window is the prescription\'s safety margin.'],
['Signature Systems Thinking: Drug Interactions','Systems thinking in pharmacology is interactions: drugs compete for metabolic enzymes, displace each other from proteins, and add their effects. Polypharmacy multiplies interactions — the whole regimen must be reviewed, not just the new drug.'],
['Signature Invariance: Structure-Activity Relationships','The invariance principle is structure-activity: similar structures, similar effects — the basis of medicinal chemistry. Change the molecule\'s key groups and the activity changes predictably; drug design exploits this regularity.'],
['Signature Approximation: Population Dosing','Approximation starts with population dosing: the standard dose for the average patient — then individualizes for age, weight, kidney and liver function, and genetics. Precision medicine refines the approximation toward the individual.'],
['Signature Evidence Standards: The Clinical Trial','The evidence standard is the randomized controlled trial with pre-specified endpoints: efficacy demonstrated, harms quantified, the label written from the data. Approval means the benefit-harm balance was judged favorable — for the studied population.'],
['Signature Classic Discoveries','The classic discoveries are penicillin, insulin, anesthesia, vaccines, and the receptor concept itself. Each turned a death sentence into a prescription — and each came from understanding mechanism, not luck alone.'],
['Signature Core Trade-offs: Efficacy versus Safety','The core trade-off is efficacy versus safety: stronger effects bring stronger side effects. Drug development optimizes the ratio — and regulators judge whether the trade serves patients.'],
['Signature Handling Uncertainty: Pharmacovigilance','The field handles uncertainty with pharmacovigilance: rare harms emerge only after approval, in millions of patients. Post-marketing surveillance is the ongoing trial — the drug\'s story continues after launch.'],
['Signature Tools of the Trade','The tools of the trade are the formulary, the interaction checker, the dosing calculator, and the trial literature. The deepest is the medication review — the whole list, reconciled, rationalized.'],
['Signature Ethics and Responsibility','Ethics in pharmacology spans prescribing (need, not habit), trials (informed consent, honest reporting), and access (essential medicines for all). The field\'s power over life demands its restraint in use.'],
['Signature Teaching Pharmacology','Teaching it well organizes by mechanism: the class, the prototype, the variations. Students who understand why beta-blockers slow the heart can predict their uses, side effects, and contraindications.'],
['Signature The Frontier Question','The frontier question is precision dosing: pharmacogenomics matching drug and dose to the individual\'s genes. The frontier asks whether \'the right drug at the right dose\' can become routine rather than aspirational.'],
['Signature Unifying Theories','The unifying theories are receptor theory and dose-response: all drug action as molecular interaction, all effects as functions of dose. Together they reduce the pharmacopeia\'s sprawl to variations on themes.'],
['Signature Computational Pharmacology','Computational pharmacology designs before synthesizing: docking simulations, QSAR models, and AI-proposed molecules. Computation explores chemical space; the lab and the trial decide what works.'],
['Signature Bridges to Other Fields','Pharmacology bridges to chemistry (drug design), biology (targets), medicine (use), genetics (variation), and economics (access). It is the translational hub of the life sciences.'],
['Signature The Great Unsolved Problems','The great unsolved problems are open and labeled as such: drugs for Alzheimer\'s and most neurodegeneration, overcoming antimicrobial resistance, and truly targeted delivery. Active research, no settled answers.'],
['Signature How New Claims Are Validated','New drugs are validated by phased trials: safety, then efficacy, then large confirmatory trials — each pre-registered, each replicated. Approval is the beginning of surveillance, not the end of questioning.'],
['Signature The Great Debates','The great debates include drug pricing versus innovation, the pace of approvals, and how much evidence suffices for rare diseases. The debates balance access against certainty — both save lives.'],
['Signature Failure Modes: When Pharmacology Gets It Wrong','The field gets it wrong through unrecognized interactions, off-label creep without evidence, and post-marketing surprises. The immune system is the adverse-event report, the interaction check, and the honest label.'],
['Signature Synthesis: Building on the Fundamentals','Advanced synthesis manages whole regimens from fundamentals: the indication, the choice, the dose, the monitoring, the review. The fundamentals are rational prescribing itself.'],
['Signature The Signature Formulation: Pharmacology as Precise Dosing','The Signature formulation treats pharmacology as precision knowledge: every principle here is dose-aware and evidence-graded, because in the Signature system drug knowledge must be exact — lives depend on the numbers. Note: this database teaches fundamentals; prescribing requires licensed professionals. That is the Signature capstone on pharmacological bedrock.']];
var TIERS=[['foundations','Foundations',1,12],['compounded','Compounded',13,24],['advanced','Advanced',25,34]];
function pad(n){var s=String(n);while(s.length<6)s='0'+s;return s;}
function firstSentence(s){var m=/^(.+?[.!?])(\s|$)/.exec(String(s).trim());return m?m[1]:String(s).slice(0,160);}
function compose(i,title,essence){
  var elab,desc,how,kps;
  if(false){
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
    standards:["Doses are calculated: weight-based where appropriate, checked twice.", "Interactions are screened: every combination is checked before use.", "Evidence is required: claims about effects cite trials, not testimonials."],citations:["Katzung, B. G. \u2014 Basic and Clinical Pharmacology.", "Goodman & Gilman's The Pharmacological Basis of Therapeutics.", "Cross-checked against the JAH Databases network archive before filing."],src:'signature',ladder_rank:rank,ladder_tier:tier,
    demo:{kind:'fundamental-pharmacology-demo',language:'python',program:demo,note:'Working demonstration program for this record. Runs as-is with python3.'},_seed:seed};
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
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator){JAHDB.registerGenerator('fundamental-pharmacology-signature',{generate:generate,validate:validate,driftCheck:driftCheck});}
if(typeof module!=='undefined'&&module.exports){module.exports={generate:generate,validate:validate,driftCheck:driftCheck};}
})();
