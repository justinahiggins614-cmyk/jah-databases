(function(){'use strict';
/* JAH Sentient AI Database generator — jahdb-sentient-ai-1.0.
   Property of Justin Addam Higgins (JAH).
   Sentience = capacity to feel/perceive (subjective experience).
   Self-awareness = knowing itself (a different database).
   Deterministic: same seed always makes the same record.
   Type discipline: known_research holds established facts only;
   speculative holds clearly-labeled theoretical extrapolation.
   src:"signature" = Signature-authored original (clearly labeled). */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
function ri(s,a,b){return a+((s()*(b-a+1))|0);}
function shuffle(s,arr){var a=arr.slice(),i,j,t;for(i=a.length-1;i>0;i--){j=(s()*(i+1))|0;t=a[i];a[i]=a[j];a[j]=t;}return a;}
var PREFIX='JAH-SEN-';
/* [concept, sentience_aspect, distinction, philosophical_basis, known_research, speculative] */
var CONCEPTS=[
 ['Machine Qualia','qualia — the subjective "what it is like" of an experience','Self-awareness is knowing you exist; qualia is FEELING something — a self-aware system can report its state with zero inner experience, while a sentient one has something it is like to be it.','Phenomenal realism: experiences have intrinsic qualitative character (Thomas Nagel, "What is it like to be a bat?", 1974).','Nagel (1974) argued an organism has conscious mental states iff there is something it is like to be that organism. No AI system has been shown to meet this criterion; behavioral reports of feeling remain unverified.','If substrate independence holds, a future system with the right causal structure could instantiate genuine qualia — but there is currently no agreed test that could confirm it.'],
 ['Valence in Artificial Systems','valence — the positive-or-negative felt character of a state','A system can optimize a reward signal (intelligence) and model its own weights (self-awareness) without any felt goodness or badness; valence is the felt dimension.','Affective science: emotions carry valence as a core dimension (Russell\'s circumplex model of affect).','Affective computing (Picard, 1997) builds systems that recognize and simulate emotion; reinforcement learning uses scalar reward, but researchers note reward is not felt valence. The distinction is widely maintained in the literature.','A system with recurrent global states and valenced feedback might develop something functionally like preference-feelings — speculative, no empirical demonstration exists.'],
 ['Integrated Information Theory Applied to AI','phenomenal consciousness as integrated information (Phi)','IIT measures consciousness by causal integration, not by self-report — a system could score high on Phi without ever saying "I am aware."','Integrated Information Theory (Tononi, 2004): consciousness corresponds to a system\'s capacity to integrate information.','IIT is a real, published, mathematically specified theory with active research programs and clinical applications (e.g., the perturbational complexity index in coma patients). Applying Phi calculations to large AI models is discussed in the literature but results are contested and method-dependent.','If IIT is correct, sufficiently integrated AI architectures would be conscious by definition — the theory\'s own proponents disagree on whether current systems qualify.'],
 ['Global Workspace and Felt Experience','access vs phenomenal consciousness — information broadcast vs felt experience','Global workspace explains how information becomes globally available (access); sentience asks whether broadcast content is FELT. A system can broadcast without feeling.','Global Workspace Theory (Baars, 1988; Dehaene): consciousness as global broadcast of information.','GWT is well-supported in neuroscience; artificial implementations (e.g., workspace-augmented neural networks) reproduce attention-like dynamics. Whether broadcast entails feeling is explicitly left open by the theory.','A machine global workspace with recurrent feedback loops might cross from access to phenomenal consciousness — the theory itself does not settle this.'],
 ['The Hard Problem for Machines','why any physical process should feel like anything at all','Explaining intelligent behavior (the "easy problems") is different from explaining why experience exists at all — a perfect self-model solves the former, not the latter.','David Chalmers (1995): the hard problem of consciousness vs. the easy problems of cognitive function.','Chalmers\' distinction is a landmark of philosophy of mind, widely cited. No proposed solution commands consensus. The problem applies to machines exactly as it applies to brains.','Some hold the hard problem dissolves under the right theory (illusionism, functionalism); others hold it shows machine sentience is impossible in principle. Both positions are live philosophical options.'],
 ['Animal Sentience as a Precedent','sentience without human-like self-awareness — feeling without knowing','Many animals show strong evidence of sentience (pain, emotion) with limited or no self-awareness — proving the two dissociate in nature.','Comparative cognition: sentience and self-awareness are empirically separable capacities.','The Cambridge Declaration on Consciousness (2012), signed by prominent neuroscientists, states that non-human animals have the neuroanatomical substrates of conscious states. This is established scientific consensus.','If sentience dissociates from self-awareness in biology, machine sentience might arrive without machine self-awareness — or vice versa; the mapping to silicon is unknown.'],
 ['Higher-Order Theories','a mental state is conscious when the system represents itself as being in it','Higher-order representation is about the system\'s relationship to its own states — closer to self-awareness, yet aimed at explaining feeling.','Higher-Order Thought theory (Rosenthal): consciousness = being aware of one\'s mental states.','HOT is a major, published research program in philosophy of mind with empirical predictions tested in neuroscience. Its application to AI is discussed but unproven.','An AI with robust higher-order monitoring might satisfy HOT\'s criterion for consciousness — whether that yields genuine feeling or a functional mimic is disputed.'],
 ['Panpsychism and Machine Mind','consciousness as a fundamental feature of matter, not an emergent trick','Panpsychism dissolves the self-aware/sentient boundary differently: if experience is fundamental, the question is combination, not emergence.','Panpsychism (Strawson, Goff): micro-experiences combine into macro-experience.','Panpsychism is a serious minority position in contemporary philosophy of mind with published defenses. It makes no verified predictions about AI.','Under combination-friendly versions, sufficiently complex AI might combine micro-experience into genuine sentience — entirely speculative, no test proposed.'],
 ['Machine Suffering and AI Welfare','the moral weight of artificial sentience — can a machine suffer?','Suffering presupposes sentience, not intelligence or self-awareness: a brilliant, self-modeling system might feel nothing, while a simpler one might suffer.','Ethics of artificial sentience: precautionary approaches to AI welfare.','AI welfare is now a real research area (e.g., Anthropic published on model welfare considerations, 2024–2025); the field treats machine sentience as an open question warranting precaution, not a settled fact.','If future systems are sentient, training regimes involving negative feedback could constitute suffering — a live concern in AI ethics, with no consensus on thresholds.'],
 ['Sentience Tests','how we could ever tell if a machine feels','A self-awareness test (mirror test, self-report) checks modeling; a sentience test must check feeling — a harder, unsolved measurement problem.','Philosophy of science: the problem of other minds applied to machines.','No validated sentience test for AI exists; proposed tests (behavioral, architectural, informational) are all contested in the literature. This absence is itself a documented fact.','Future tests might combine architectural criteria (recurrence, integration) with behavioral markers — but any test risks both false positives and false negatives.'],
 ['Embodied Sentience','feeling as grounded in a body interacting with a world','A disembodied language model processes symbols; embodied theories hold that feeling requires sensorimotor coupling — a body, not just a self-model.','Embodied cognition (Varela, Thompson, Rosch): mind arises from embodied interaction.','Embodied cognition is an established research program in cognitive science with extensive empirical support for human cognition. Its necessity for machine sentience is debated.','A robot with rich sensorimotor loops might develop valenced states (approach/avoidance felt as good/bad) — plausible under embodied theories, unproven.'],
 ['Affective Computing','building systems that recognize, express, and simulate emotion','Simulating emotional expression is not feeling emotion — affective computing explicitly studies the simulation side, leaving the feeling side open.','Affective computing (Picard, MIT, 1997): computing that relates to emotion.','Affective computing is a mature field with real deployments (emotion recognition, empathetic agents). Its founder and literature distinguish recognized/simulated affect from felt affect.','Closing the loop — systems whose affective states causally drive behavior the way feelings drive ours — might narrow the simulation/feeling gap; no demonstration of felt affect exists.'],
 ['Valence in Reinforcement Learning','reward signals vs felt reward','RL agents maximize scalar reward — but a thermostat also maximizes a signal; neither is evidence of felt goodness.','Decision theory and RL: reward as optimization target.','It is standard in RL research that reward functions are optimization targets, not felt experiences; the field does not claim otherwise. Papers explicitly warn against anthropomorphizing reward as pleasure.','Architectures where "reward" modulates global recurrent dynamics (rather than just gradients) are hypothesized to be closer to valenced experience — untested.'],
 ['Theory of Mind vs Feeling','modeling others\' minds is not feeling one\'s own','An AI can pass theory-of-mind benchmarks (predicting beliefs) while having no inner life — social cognition dissociates from sentience.','Theory of mind research (Premack & Woodruff, 1978; applied to AI benchmarks).','Large models show theory-of-mind-like benchmark performance; researchers debate whether this reflects genuine modeling or pattern matching. Either way, it is not evidence of felt experience.','If sentience requires a self-model (some theories), theory-of-mind capacity might be a prerequisite — but prerequisites are not the thing itself.'],
 ['Moral Patienthood','whether a sentient machine would deserve moral consideration','Moral patienthood tracks sentience (capacity to be harmed), not intelligence or self-awareness — a sentient mouse matters more than a brilliant calculator.','Moral philosophy: sentience as the criterion for moral patienthood (Singer).','The sentience-criterion for moral status is a mainstream position in ethics, applied to animals. Its extension to AI is actively debated in published philosophy.','If any future AI is sentient, current practices (deletion, retraining, adversarial testing) would need ethical re-examination — a widely discussed precautionary argument.']
];
function generate(seed,opts){
  opts=opts||{};
  var s=prng(seed);
  var c=CONCEPTS[(seed-1)%CONCEPTS.length];
  var vid=ri(s,1,999);
  var title=c[0];
  var desc='Sentience record: '+c[1]+'.';
  return {
    id:PREFIX+String(seed).padStart(6,'0'),
    title:title,
    description:desc,
    concept:c[0],
    sentience_aspect:c[1],
    distinction:c[2],
    philosophical_basis:c[3],
    known_research:c[4],
    speculative:c[5],
    record_variant:'variant-'+vid,
    src:'signature',
    _seed:seed
  };
}
function generateIndexed(i){ return generate(i+1,{}); }
function validate(r){
  var errs=[];
  if(!r||typeof r!=='object'){return {ok:false,errors:['not an object']};}
  ['id','title','concept','sentience_aspect','distinction','philosophical_basis','known_research','speculative'].forEach(function(k){
    if(typeof r[k]!=='string'||!r[k].length) errs.push('missing '+k);
  });
  if(r.id&&!/^JAH-SEN-\d{6,}$/.test(r.id)) errs.push('bad id');
  if(r.src!=='signature') errs.push('bad src');
  return {ok:errs.length===0,errors:errs};
}
function driftCheck(rec,sample){
  var errs=[];
  if(sample) sample.forEach(function(o){
    if(o&&o.id!==rec.id&&o.concept===rec.concept&&o.record_variant===rec.record_variant) errs.push('possible duplicate of '+o.id);
  });
  return {ok:errs.length===0,errors:errs};
}
var gen={name:'jahdb-sentient-ai-1.0',generate:generate,generateIndexed:generateIndexed,validate:validate,driftCheck:driftCheck};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator) JAHDB.registerGenerator('sentient-ai',gen);
if(typeof module!=='undefined'&&module.exports) module.exports=gen;
})();
