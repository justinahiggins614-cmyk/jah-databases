(function(){'use strict';
/* Signature Dystopia Database generator — jahdb-dystopia-generator-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed always makes the same record.
   src:"signature" = Signature-authored original (clearly labeled) */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX='JAH-DYST-';
var TOPICS=[["1984", "The Orwell; the surveillance."], ["Brave New World", "The Huxley; the pleasure."], ["Fahrenheit 451", "The Bradbury; the books."], ["The Handmaid's Tale", "The Atwood; the theocracy."], ["The Hunger Games", "The Collins; the spectacle."], ["The Road", "The McCarthy; the ash."], ["A Clockwork Orange", "The Burgess; the ultraviolence."], ["We", "The Zamyatin; the original."], ["The Dispossessed", "The Le Guin; the ambiguous."], ["Parable of the Sower", "The Butler; the prescient."], ["The Children of Men", "The James; the infertility."], ["The Stand", "The King; the plague."], ["The Dystopian YA Boom", "The 2010s; the wave."], ["The Surveillance State", "The trope; the reality."], ["The Corporate Dystopia", "The company; the rule."], ["The Climate Dystopia", "The collapse; the warning."], ["The Technological", "The AI; the control."], ["The Theocratic", "The faith; the oppression."], ["The Post-Nuclear", "The wasteland; the Fallout."], ["The Pandemic", "The Station Eleven; the art."], ["The Function", "The warning; the mirror."], ["The Hope", "The resistance; the ember."], ["The Satire", "The exaggeration; the critique."], ["The Film Adaptations", "The screen; the hits."], ["The 2025 Relevance", "The echoes; the unease."], ["Writing Dystopia", "The craft; the responsibility."], ["The Future", "The trends; the prediction."], ["Why We Read", "The caution; the catharsis."]];
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
    type:'dystopia exploration', content:content, content_completeness:'stub',
    stub_note:'Topic stub: the topic title and its one-line brief are real; the full guide article is not yet written. This record does not present shell text as a complete guide.',
    demo:null, src:'signature', _seed:seed
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
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator){JAHDB.registerGenerator('dystopia',{generate:generate,validate:validate,driftCheck:driftCheck});}
if(typeof module!=='undefined'&&module.exports){module.exports={generate:generate,validate:validate,driftCheck:driftCheck};}
})();