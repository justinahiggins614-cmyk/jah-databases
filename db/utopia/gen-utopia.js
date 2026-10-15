(function(){'use strict';
/* Signature Utopia Database generator — jahdb-utopia-generator-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed always makes the same record.
   src:"signature" = Signature-authored original (clearly labeled) */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX='JAH-UTOPIA-';
var TOPICS=[["Utopia: The Book", "1516's More; the coinage."], ["The Eutopia", "The good place; the pun."], ["The Arcadia", "The pastoral; the ideal."], ["The New Atlantis", "The Bacon; the science."], ["Looking Backward", "The Bellamy; the 2000."], ["The Ecotopia", "The Callenbach; the green."], ["The Dispossessed", "The ambiguous; the anarchist."], ["The Culture", "The Banks; the post-scarcity."], ["Star Trek's Federation", "The Roddenberry; the optimism."], ["The Solarpunk", "The sustainable; the movement."], ["The Intentional Communities", "The communes; the experiments."], ["The Kibbutz", "The collective; the Israel."], ["The Co-Housing", "The Danish; the model."], ["The Transition Towns", "The Rob Hopkins; the resilience."], ["The Critique", "The boring; the static."], ["The Dystopian Flip", "The perfect prison; the twist."], ["The Design", "The planning; the architecture."], ["The Economics", "The abundance; the models."], ["The Governance", "The decisions; the democracy."], ["The Technology", "The enabler; the appropriate."], ["The Psychology", "The meaning; the purpose."], ["The Education", "The learning; the Summerhill."], ["The Work", "The play; the post-work."], ["The Art", "The flourishing; the culture."], ["The 2025 Experiments", "The projects; the state."], ["Imagining Better", "The craft; the necessity."], ["The Future", "The hope; the prediction."], ["Why Utopia Matters", "The direction; the North Star."]];
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
    type:'utopia exploration', content:content, content_completeness:'stub',
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
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator){JAHDB.registerGenerator('utopia',{generate:generate,validate:validate,driftCheck:driftCheck});}
if(typeof module!=='undefined'&&module.exports){module.exports={generate:generate,validate:validate,driftCheck:driftCheck};}
})();