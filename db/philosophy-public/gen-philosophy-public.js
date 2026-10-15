(function(){'use strict';
/* Public Philosophy Database generator — jahdb-philosophy-public-generator-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed always makes the same record.
   src:"public" = Fact-checked public information */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX='JAH-PHIL-PUB-';
var TOPICS=[["Ethics", "Theories of right and wrong: virtue, duty, and consequences."], ["Metaphysics", "The nature of reality, being, and causation."], ["Epistemology", "Knowledge, belief, justification, and skepticism."], ["Logic", "Valid reasoning: deduction, induction, and fallacies."], ["Philosophy of Mind", "Consciousness, the self, and the mind-body problem."], ["Political Philosophy", "Justice, liberty, authority, and the social contract."], ["Aesthetics", "Beauty, art, and aesthetic judgment."], ["Existentialism", "Freedom, absurdity, and creating meaning."], ["Stoicism", "Ancient wisdom on control, virtue, and resilience."], ["Utilitarianism", "Greatest happiness for the greatest number."], ["Deontology", "Duty-based ethics and Kant's categorical imperative."], ["Virtue Ethics", "Character, habits, and Aristotle's golden mean."], ["Socrates", "The examined life and the Socratic method."], ["Plato", "Forms, the Republic, and the allegory of the cave."], ["Aristotle", "Logic, ethics, and the first systematic philosophy."], ["Descartes", "Doubt, the cogito, and modern philosophy's start."], ["Hume", "Empiricism, causation, and the problem of induction."], ["Kant", "Synthesizing reason and experience; moral philosophy."], ["Nietzsche", "Will to power, master morality, and the death of God."], ["Eastern Philosophy", "Confucianism, Buddhism, Taoism, and Hindu thought."], ["Philosophy of Science", "What makes science work: falsification and paradigms."], ["Philosophy of Language", "Meaning, reference, and how words hook to the world."], ["Free Will", "Determinism, compatibilism, and moral responsibility."], ["The Good Life", "What makes a life go well: competing visions."], ["Thought Experiments", "Trolley problems, brains in vats, and philosophical method."]];
var ANGLES=['overview','detailed','examples','faq','history','applications'];
function pad(n){var s=String(n);while(s.length<6)s='0'+s;return s;}
function generate(seed,opts){
  var s=prng(seed);
  var ti=(s()*TOPICS.length)|0, ai=(s()*ANGLES.length)|0;
  var topic=TOPICS[ti], angle=ANGLES[ai];
  var id=PREFIX+pad(seed);
  var title=topic[0]+' ('+angle+')';
  var desc=topic[1];
  var content=topic[0]+' \u2014 '+topic[1];
  return {
    id:id, title:title, description:desc, genre:angle,
    type:'philosophy knowledge record', content:content, content_completeness:'stub',
    stub_note:'Topic stub: the topic title and its one-line brief are real; the full guide article is not yet written. This record does not present shell text as a complete guide.',
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
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator){JAHDB.registerGenerator('philosophy-public',{generate:generate,validate:validate,driftCheck:driftCheck});}
if(typeof module!=='undefined'&&module.exports){module.exports={generate:generate,validate:validate,driftCheck:driftCheck};}
})();