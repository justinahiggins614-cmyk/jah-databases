(function(){'use strict';
/* Signature Paintball Database generator — jahdb-paintball-generator-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed always makes the same record.
   src:"signature" = Signature-authored original (clearly labeled) */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX='JAH-PAINTB-';
var TOPICS=[["The Origin: Forestry", "The Nel-Spot; the marking."], ["The First Game", "1981's capture the flag; the 12 players."], ["How Markers Work", "The CO2; the HPA."], ["The Gear", "The mask; the essential."], ["The Fields", "The woodsball; the speedball."], ["The Tactics", "The snap shooting; the bunkering."], ["The Tournaments", "The NXL; the pro."], ["The Woodsball", "The scenario; the milsim."], ["MagFed", "The realism; the subculture."], ["The Safety Record", "The stats; the masks."], ["The Pain Question", "The welts; the honesty."], ["The Cost", "The paint; the budget."], ["The Maintenance", "The cleaning; the O-rings."], ["The Scenario Games", "The D-Day; the Oklahoma."], ["The Big Games", "The thousands; the events."], ["The Referees", "The calls; the honor."], ["The Cheating", "The wiping; the penalties."], ["The Exercise", "The workout; the fun."], ["The Teamwork", "The comms; the bonding."], ["The Military Training", "The simulation; the use."], ["The Environmental", "The fill; the biodegradable."], ["The Industry", "The manufacturers; the market."], ["The 2025 Scene", "The state; the trends."], ["The Future", "The .50 cal; the prediction."], ["Getting Started", "The rental; the advice."], ["The Community", "The regulars; the culture."], ["The Variants", "The airsoft; the comparison."], ["Why We Play", "The adrenaline; the friends."]];
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
    type:'paintball exploration', content:content, content_completeness:'stub',
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
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator){JAHDB.registerGenerator('paintball',{generate:generate,validate:validate,driftCheck:driftCheck});}
if(typeof module!=='undefined'&&module.exports){module.exports={generate:generate,validate:validate,driftCheck:driftCheck};}
})();