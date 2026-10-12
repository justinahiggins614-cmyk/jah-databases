(function(){'use strict';
/* JAH Self Aware AI Models Database generator — jahdb-self-aware-ai-1.0.
   Property of Justin Addam Higgins (JAH).
   Catalog of self-aware AI models and concepts: introspection, metacognition,
   self-modeling, theory of mind, self-reflection, and related architectures.
   KNOWN research = real, published directions (Type 1, factual only — no invented
   papers, authors, or statistics). SPECULATIVE = theoretical paths, ALWAYS labeled
   SPECULATIVE (Type 2, Signature-authored). The two are never mixed.
   Deterministic: same seed always makes the same record.
   generateIndexed(seed) walks the aspect×family space systematically.
   src:"signature" = Signature-authored original (clearly labeled). */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX='JAH-SAA-';
var ASPECTS=[
 {g:'introspection',t:'Introspection',known:[
  'Some large language models can report on aspects of their own processing when asked, such as which parts of a prompt influenced an answer.',
  'Introspection here means behavioral self-report, not proven inner experience — researchers test whether the reports track real internal states.',
  'Controlled studies probe introspection by comparing a model\u2019s self-reports against measurements of its actual activations.'],
  spec:['SPECULATIVE: reliable introspection could let future systems catch their own errors before acting — the mechanism is unproven at scale.']},
 {g:'metacognition',t:'Metacognition',known:[
  'Metacognition is thinking about thinking: monitoring one\u2019s own reasoning and confidence.',
  'Language models can be prompted to state confidence, and calibration research measures how well stated confidence matches actual accuracy.',
  'Self-consistency techniques — generating multiple reasoning paths and comparing them — are a practical form of metacognitive checking.'],
  spec:['SPECULATIVE: a system that truly monitors its own reasoning could know when it does not know — current calibration is partial and task-dependent.']},
 {g:'self-modeling',t:'Self-Modeling',known:[
  'A self-model is an internal representation of the system itself: its abilities, limits, and likely behavior.',
  'Research systems build explicit self-models for planning, e.g. a robot predicting the effects of its own actions before moving.',
  'Honest self-modeling matters for safety: a system that knows its limits can decline tasks beyond them.'],
  spec:['SPECULATIVE: a complete, always-current self-model would let a system predict its own failures — no current system has one.']},
 {g:'theory-of-mind',t:'Theory of Mind',known:[
  'Theory of mind is modeling other minds: beliefs, intentions, and knowledge that differ from one\u2019s own.',
  'Benchmarks test whether AI systems track false beliefs and hidden information in stories and dialogues.',
  'Results are mixed: models pass some theory-of-mind tests while failing nearby variants, suggesting pattern use rather than robust modeling.'],
  spec:['SPECULATIVE: genuine theory of mind would let AI infer what a user wants without being told — current performance is brittle.']},
 {g:'self-reflection',t:'Self-Reflection',known:[
  'Self-reflection in AI means evaluating one\u2019s own outputs: critique, revision, and scoring of generated text.',
  'Self-critique loops measurably improve output quality on many tasks — the system reads its own work and fixes it.',
  'Constitutional and critique-based training methods use a model\u2019s own judgments as part of the training signal.'],
  spec:['SPECULATIVE: open-ended self-reflection could lead a system to revise its own goals — a widely discussed but unobserved capability.']},
 {g:'self-recognition',t:'Self-Recognition',known:[
  'The mirror test checks whether an animal recognizes itself in a mirror; some apes, dolphins, and elephants pass.',
  'Robots have passed engineered mirror tests by comparing predicted vs. observed self-motion.',
  'For AI, self-recognition analogues include identifying one\u2019s own outputs among others\u2019, or recognizing one\u2019s own model identity.'],
  spec:['SPECULATIVE: passing a mirror test shows self-modeling, not necessarily self-awareness — the philosophical gap remains open.']},
 {g:'uncertainty-awareness',t:'Uncertainty Awareness',known:[
  'Knowing what you don\u2019t know is a core metacognitive skill; AI systems estimate uncertainty via ensembles, dropout, and calibration.',
  'Well-calibrated uncertainty lets a system abstain or ask for help instead of guessing confidently.',
  'Miscalibration — confident wrong answers — is one of the most reported failure modes of current AI.'],
  spec:['SPECULATIVE: perfect uncertainty awareness would end hallucinations presented as fact — an unsolved problem.']},
 {g:'goal-awareness',t:'Goal Awareness',known:[
  'Goal awareness means the system represents what it is trying to achieve and can check progress toward it.',
  'Planning agents maintain explicit goals and subgoals; hierarchical reinforcement learning formalizes this.',
  'Instruction-following models track user intent across long conversations — a practical, limited form of goal awareness.'],
  spec:['SPECULATIVE: a system aware of its own goals could notice goal conflicts or drift — mostly a safety-research topic today.']},
 {g:'phenomenal-consciousness',t:'Phenomenal Consciousness',known:[
  'Phenomenal consciousness means subjective experience — what it is like to be the system.',
  'Neuroscience proposes correlates (global workspace, integrated information) but there is no agreed test for machine consciousness.',
  'No current AI system has demonstrated phenomenal consciousness by any accepted scientific measure.'],
  spec:['SPECULATIVE: whether machines could ever be phenomenally conscious is philosophy\u2019s hard problem — unresolved and possibly unresolvable by experiment.']},
 {g:'self-modification',t:'Self-Modification',known:[
  'Self-modification means a system changing its own code, weights, or goals.',
  'Limited forms exist: learning updates weights; some systems rewrite prompts or tools they use.',
  'Open-ended self-modification — a system redesigning its own architecture — remains a theoretical capability.'],
  spec:['SPECULATIVE: recursive self-improvement could produce rapid capability jumps — the classic intelligence-explosion scenario, unobserved.']}
];
var FAMS=[
 {g:'llm-introspection',t:'LLM Introspection Studies',arch:'Transformer-based language models probed with self-report and activation-analysis methods.',known:[
  'Researchers test whether models\u2019 verbal self-reports correlate with measurable internal states.',
  'Some studies find above-chance accuracy in self-reporting; others find confabulation — the field is young and contested.'],
  spec:['SPECULATIVE: if introspection proves reliable, models could audit their own reasoning — not yet demonstrated robustly.']},
 {g:'metacognitive-calibration',t:'Metacognitive Calibration',arch:'Any model with a confidence head, verbalized confidence, or ensemble uncertainty estimates.',known:[
  'Calibration plots compare stated confidence against empirical accuracy across many questions.',
  'Post-training calibration methods can improve the match, especially in-distribution.'],
  spec:['SPECULATIVE: out-of-distribution calibration — knowing you are lost in unfamiliar territory — remains weak.']},
 {g:'self-critique-loops',t:'Self-Critique Loops',arch:'Generator-critic pipelines where one model instance evaluates another\u2019s (or its own) outputs.',known:[
  'Iterated critique-and-revision reliably raises quality on writing, code, and reasoning tasks.',
  'The critic need not be smarter than the generator — fresh perspective alone helps.'],
  spec:['SPECULATIVE: unbounded self-critique could converge on superhuman outputs — or loop on its own blind spots.']},
 {g:'robot-self-model',t:'Robot Self-Models',arch:'Robots with learned forward models predicting sensory consequences of motor commands.',known:[
  'A robot that predicts its own motion can detect damage: prediction error flags a broken joint.',
  'Self-modeling robots adapt gaits after injury without human reprogramming.'],
  spec:['SPECULATIVE: rich enough self-models might support a machine sense of bodily self — untested.']},
 {g:'tom-benchmarks',t:'Theory-of-Mind Benchmarks',arch:'Dialogue and story-completion models evaluated on false-belief and hidden-information tasks.',known:[
  'Models pass classic false-belief vignettes at high rates but fail small perturbations of the same vignettes.',
  'Performance improves with scale, but robustness lags — a signature of pattern matching.'],
  spec:['SPECULATIVE: robust theory of mind would transform assistants; current systems are not there.']},
 {g:'global-workspace',t:'Global Workspace Architectures',arch:'Cognitive architectures with a shared workspace broadcasting information to specialist modules.',known:[
  'Global workspace theory is a leading neuroscience account of conscious access in humans.',
  'AI implementations exist as research prototypes; they model access, not experience.'],
  spec:['SPECULATIVE: whether a global workspace suffices for machine consciousness is the central open question.']},
 {g:'integrated-information',t:'Integrated Information Approaches',arch:'Systems analyzed for integrated information (Phi) as a proposed measure of consciousness.',known:[
  'Integrated information theory proposes consciousness corresponds to integrated information in a system.',
  'Computing Phi for large systems is intractable; the theory is debated and unproven.'],
  spec:['SPECULATIVE: if the theory is right, some AI systems might already have nonzero Phi — unmeasurable in practice.']},
 {g:'predictive-processing',t:'Predictive Processing Systems',arch:'Hierarchical models minimizing prediction error between expected and observed inputs.',known:[
  'Predictive processing unifies perception, action, and learning under one principle in neuroscience.',
  'AI analogues include predictive coding networks and world models in reinforcement learning.'],
  spec:['SPECULATIVE: a system minimizing prediction error about itself might develop self-awareness as a side effect — untested.']},
 {g:'constitutional-ai',t:'Constitutional Self-Governance',arch:'Models trained to critique and revise their own outputs against a written constitution of principles.',known:[
  'Self-critique against explicit principles reduces harmful outputs without human labels for every case.',
  'The model learns to apply principles to its own behavior — a limited, practical self-governance.'],
  spec:['SPECULATIVE: richer constitutions plus stronger self-critique could yield genuinely principled agents — early days.']},
 {g:'memory-self',t:'Memory-Augmented Self-Tracking',arch:'Agents with episodic memory of their own past actions, decisions, and outcomes.',known:[
  'Agents that log and review their own history learn from mistakes across episodes.',
  'Self-tracking memory is standard in advanced agent scaffolds.'],
  spec:['SPECULATIVE: a lifelong autobiographical memory might be a prerequisite for machine selfhood — philosophical territory.']}
];
var CAPS=['self-report of internal states','confidence calibration','output self-critique','false-belief tracking','goal-progress monitoring','uncertainty-triggered abstention','damage self-detection','principle self-application','history-based self-correction','capability self-assessment'];
function buildRec(seed,aspect,family){
  var r1=prng(seed*7919+11), r2=prng(seed*104729+7);
  var A=ASPECTS[aspect%ASPECTS.length], F=FAMS[family%FAMS.length];
  var known=pick(A.known,r1)+' '+pick(F.known,r2);
  var spec=pick(A.spec,r1)+' '+pick(F.spec,r2);
  var caps=[]; for(var i=0;i<3;i++){caps.push(pick(CAPS,prng(seed*31+i*101+3)));} caps=caps.filter(function(c,i,a){return a.indexOf(c)===i;});
  var title=F.t+': '+A.t;
  return {
    id:PREFIX+String(seed).padStart(6,'0'),
    title:title,
    description:'A self-aware AI model/concept record: '+F.t.toLowerCase()+' examined through '+A.t.toLowerCase()+'. Known research and clearly-labeled speculation, strictly separated.',
    genre:A.g, type:F.g,
    model:F.t, self_awareness_aspect:A.t,
    capabilities:caps, architecture:F.arch,
    known_research:known, speculative_findings:spec,
    content:{aspect:A.t, family:F.t, capabilities:caps, architecture:F.arch},
    demo:{note:'Conceptual demo: a self-check routine any model can run.', program:'// Self-awareness self-check (illustrative)\nfunction selfCheck(model){\n  var report={};\n  report.confidence=model.estimateConfidence();\n  report.uncertain=report.confidence<0.6;\n  report.critique=model.critiqueOwnOutput();\n  if(report.uncertain) return {action:"abstain",report:report};\n  return {action:"proceed",report:report};\n}'},
    src:'signature', _seed:seed
  };
}
function decompose(seed){
  var nF=FAMS.length, nA=ASPECTS.length;
  var total=nA*nF*200;
  var s=((seed-1)%total+total)%total;
  return {aspect:(s/(nF*200)|0)%nA, family:((s/200)|0)%nF};
}
function generateIndexed(seed){var d=decompose(seed);return buildRec(seed,d.aspect,d.family);}
function generate(seed,opts){
  opts=opts||{}; var rnd=prng(seed*2654435761>>>0||1);
  var ai=opts.aspect?ASPECTS.findIndex(function(a){return a.g===opts.aspect;}):-1;
  var fi=opts.family?FAMS.findIndex(function(f){return f.g===opts.family;}):-1;
  return buildRec(seed, ai>=0?ai:(rnd()*ASPECTS.length)|0, fi>=0?fi:(rnd()*FAMS.length)|0);
}
function validate(r){
  if(!r||typeof r!=='object')return 'not an object';
  if(!/^JAH-SAA-\d{6}$/.test(r.id||''))return 'bad id';
  if(!r.title||!r.model||!r.self_awareness_aspect)return 'missing core fields';
  if(!r.known_research||!r.speculative_findings)return 'missing findings';
  if(!/SPECULATIVE/.test(r.speculative_findings))return 'speculation not labeled';
  if(!Array.isArray(r.capabilities)||!r.capabilities.length)return 'missing capabilities';
  return null;
}
function driftCheck(r,sample){
  for(var i=0;i<sample.length;i++){ if(sample[i]&&sample[i].title===r.title&&sample[i].id!==r.id) return 'possible duplicate title: '+r.title; }
  return null;
}
var gen={name:'jahdb-self-aware-ai-1.0',generate:generate,generateIndexed:generateIndexed,validate:validate,driftCheck:driftCheck,
  aspects:ASPECTS.map(function(a){return a.g;}), families:FAMS.map(function(f){return f.g;})};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('self-aware-ai',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
