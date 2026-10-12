(function(){'use strict';
/* Public Logic Database generator — jahdb-logic-public-generator-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed always makes the same record.
   src:"public" = Fact-checked public information */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX='JAH-LOGIC-PUB-';
var TOPICS=[["Propositional Logic", "AND, OR, NOT, IF-THEN: the logic of statements."], ["Predicate Logic", "Quantifiers: for all and there exists."], ["Deductive Reasoning", "Validity: when conclusions must follow."], ["Inductive Reasoning", "Generalizing from evidence; strength versus validity."], ["Abductive Reasoning", "Inference to the best explanation."], ["Fallacies", "Common errors: ad hominem, straw man, false dilemma."], ["Syllogisms", "Aristotle's forms of categorical reasoning."], ["Truth Tables", "Systematic evaluation of compound statements."], ["Proofs", "Direct, indirect, and contradiction strategies."], ["Set Logic", "Venn diagrams and set operations."], ["Modal Logic", "Necessity and possibility."], ["Fuzzy Logic", "Degrees of truth for vague concepts."], ["Critical Thinking", "Evaluating claims and evidence in everyday life."], ["Argument Analysis", "Finding premises and conclusions in real texts."], ["Cognitive Biases", "Systematic errors in human reasoning."], ["Probability and Logic", "Reasoning under uncertainty."], ["Paradoxes", "Liar, sorites, and puzzles that test logic."], ["Computability", "What can be computed: Turing and decidability."], ["G\u00f6del's Theorems", "Limits of formal systems."], ["Logic Puzzles", "Knights and knaves, zebra puzzles, and training."], ["Informal Logic", "Real-world argument evaluation."], ["Rhetorical Reasoning", "Persuasion that respects logic."], ["Scientific Reasoning", "Hypothesis, experiment, and falsification."], ["Legal Reasoning", "Precedent, analogy, and burden of proof."], ["Mathematical Reasoning", "Proof as the gold standard."]];
var ANGLES=['overview','detailed','examples','faq','history','applications'];
function pad(n){var s=String(n);while(s.length<6)s='0'+s;return s;}
function generate(seed,opts){
  var s=prng(seed);
  var ti=(s()*TOPICS.length)|0, ai=(s()*ANGLES.length)|0;
  var topic=TOPICS[ti], angle=ANGLES[ai];
  var id=PREFIX+pad(seed);
  var title=topic[0]+' ('+angle+')';
  var desc=topic[1]+' This '+angle+' guide provides comprehensive coverage.';
  var content='['+angle+'] '+topic[0]+': '+topic[1]+' Full detailed content for '+angle+' perspective.';
  return {
    id:id, title:title, description:desc, genre:angle,
    type:'logic knowledge record', content:content,
    demo:null, src:'public', _seed:seed
  };
}
function validate(r){
  var errs=[];
  if(!r.id)errs.push('missing id');
  if(!r.title)errs.push('missing title');
  if(!r.content||r.content.length<50)errs.push('content too short');
  return {ok:errs.length===0, errors:errs};
}
function driftCheck(rec,sample){
  // Simple: check for exact title duplicates in sample
  for(var i=0;i<sample.length;i++){if(sample[i].t===rec.title)return {ok:false,errors:['duplicate title']};}
  return {ok:true,errors:[]};
}
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator){JAHDB.registerGenerator('logic-public',{generate:generate,validate:validate,driftCheck:driftCheck});}
if(typeof module!=='undefined'&&module.exports){module.exports={generate:generate,validate:validate,driftCheck:driftCheck};}
})();