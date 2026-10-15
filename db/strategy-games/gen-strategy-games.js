(function(){'use strict';
/* Signature Strategy Games Database generator — jahdb-strategy-games-generator-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed always makes the same record.
   src:"signature" = Signature-authored original (clearly labeled) */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX='JAH-STRAT-';
var TOPICS=[["Chess", "The king; the depth."], ["Go", "The ancient; the complexity."], ["StarCraft", "The RTS; the Korea."], ["Age of Empires", "The history; the wololo."], ["Civilization", "The 4X; the one more turn."], ["Total War", "The battles; the campaign."], ["XCOM", "The tactics; the 99%."], ["Fire Emblem", "The permadeath; the relationships."], ["Into the Breach", "The perfect info; the design."], ["Slay the Spire", "The roguelike deck; the genre."], ["The 4X Genre", "Explore to exterminate; the best."], ["Grand Strategy", "Paradox; the maps."], ["The RTS Decline", "The MOBA drain; the revival attempts."], ["Auto Battlers", "Teamfight Tactics; the genre."], ["Tower Defense", "The maze; the mobile."], ["The Fog of War", "The information; the design."], ["APM and Skill", "The mechanics; the ceiling."], ["The Meta Game", "The balance; the patches."], ["Competitive Scenes", "The pros; the prize."], ["The AI Opponents", "The cheating; the design."], ["Board Game Strategy", "The tabletop; the depth."], ["The Psychology", "The planning; the tilt."], ["Learning Resources", "The guides; the improvement."], ["The Classics", "The canon; the influence."], ["The 2025 Releases", "The new; the buzz."], ["Designing Strategy", "The balance; the advice."], ["The Future", "The AI; the prediction."], ["Why We Strategize", "The mind; the satisfaction."]];
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
    type:'strategy games exploration', content:content, content_completeness:'stub',
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
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator){JAHDB.registerGenerator('strategy-games',{generate:generate,validate:validate,driftCheck:driftCheck});}
if(typeof module!=='undefined'&&module.exports){module.exports={generate:generate,validate:validate,driftCheck:driftCheck};}
})();