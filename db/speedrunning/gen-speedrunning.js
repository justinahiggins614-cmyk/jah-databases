(function(){'use strict';
/* Signature Speedrunning Database generator — jahdb-speedrunning-generator-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed always makes the same record.
   src:"signature" = Signature-authored original (clearly labeled) */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX='JAH-SPEED-';
var TOPICS=[["What Is Speedrunning?", "The fastest; the categories."], ["Super Mario Bros.", "The 4:54; the perfect."], ["The Tool-Assisted", "The TAS; the theory."], ["Games Done Quick", "The charity; the millions."], ["The Any% Category", "The fastest; the glitches."], ["100% Runs", "The completion; the endurance."], ["The Glitch Hunting", "The wrong warp; the science."], ["Sequence Breaking", "The intended; the skip."], ["The RNG Manipulation", "The luck; the control."], ["The Frame Perfect", "The 1/60; the skill."], ["The Grind", "The attempts; the mentality."], ["The World Records", "The history; the rivalries."], ["Summoning Salt", "The documentaries; the stories."], ["The Community", "The Discord; the support."], ["Race Events", "The head-to-head; the hype."], ["The Verification", "The mods; the proof."], ["Cheating Scandals", "The splicing; the bans."], ["The Dream Incident", "The Minecraft; the statistics."], ["TASBot", "The robot; the GDQ."], ["The Blindfolded", "The memory; the feat."], ["The Marathon", "The 24-hour; the charity."], ["Speedrun.com", "The leaderboards; the database."], ["The Categories Debate", "The rules; the splits."], ["The New Game Hype", "The release; the routing."], ["The Accessibility", "The entry; the guides."], ["The Psychology", "The obsession; the flow."], ["The Future", "The AI routing; the prediction."], ["Getting Started", "The game choice; the advice."]];
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
    type:'speedrunning exploration', content:content, content_completeness:'stub',
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
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator){JAHDB.registerGenerator('speedrunning',{generate:generate,validate:validate,driftCheck:driftCheck});}
if(typeof module!=='undefined'&&module.exports){module.exports={generate:generate,validate:validate,driftCheck:driftCheck};}
})();