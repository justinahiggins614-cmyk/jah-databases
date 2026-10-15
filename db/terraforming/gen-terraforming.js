(function(){'use strict';
/* Signature Terraforming Database generator — jahdb-terraforming-generator-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed always makes the same record.
   src:"signature" = Signature-authored original (clearly labeled) */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX='JAH-TERRA-';
var TOPICS=[["What Terraforming Means", "Reshaping a planet for human life; the concept is grand and fraught."], ["Terraforming Mars: The Basics", "Thicken the air, warm the planet; the steps are outlined."], ["The Magnetic Field Problem", "Mars lost its shield; without it, the solar wind strips air."], ["Artificial Magnetospheres", "A satellite magnet could shield Mars; the proposal is serious."], ["Super Greenhouse Gases", "Potent warming gases could heat Mars; the chemistry is speculative."], ["Importing Volatiles", "Steering comets to Mars; the energy and ethics are staggering."], ["The Timescale: Millennia", "Even optimists say centuries; the patience required is civilizational."], ["Paraterraforming: Domes Instead", "Enclosed regions, not whole planets; the practical alternative."], ["Terraforming Venus", "The harder target; sunshades and chemistry are proposed."], ["Venus's Runaway Greenhouse", "Understanding Venus warns Earth; the cautionary planet."], ["Terraforming the Moon", "Too little gravity to hold air; the physics says no."], ["Ethics: Planetary Protection", "Native Martian life would be priceless; contamination is irreversible."], ["Who Decides?", "No governance exists; the decision would be humanity's biggest."], ["Ecopoiesis: Seeding Life", "Engineered microbes first; the biology is the long pole."], ["The Economics", "Costs exceed any budget; the motivation must be non-economic."], ["Terraforming in Fiction", "Kim Stanley Robinson's Mars trilogy; fiction did the systems thinking."], ["The Overview Effect Scaled", "Watching a world come alive; the spiritual dimension."], ["Unintended Consequences", "Planetary engineering risks; the humility lesson."], ["Alternative: Adaptation", "Engineer humans, not planets; the bioethics are thorny."], ["The Drake Angle", "Terraforming signatures could be technosignatures; SETI watches."], ["Mars Sample Return First", "We must check for life before reshaping; the sequencing matters."], ["The 1000-Year Plan", "Thinking on civilizational timescales; the philosophy is the point."], ["Terraforming and Religion", "Faiths weigh in on remaking worlds; the dialogue is young."], ["Legal Frameworks", "The Outer Space Treaty is silent; new law is needed."], ["Public Opinion", "Polls show fascination plus unease; the ambivalence is healthy."], ["The Anti-Terraforming Case", "Preserve worlds pristine; the conservation ethic."], ["A Middle Path", "Domes now, planets later; the pragmatic sequence."], ["The Ultimate Question", "Should we?; the answer defines us."]];
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
    type:'terraforming exploration', content:content, content_completeness:'stub',
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
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator){JAHDB.registerGenerator('terraforming',{generate:generate,validate:validate,driftCheck:driftCheck});}
if(typeof module!=='undefined'&&module.exports){module.exports={generate:generate,validate:validate,driftCheck:driftCheck};}
})();