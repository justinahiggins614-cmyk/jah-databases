(function(){'use strict';
/* Signature Party Games Database generator — jahdb-party-games-generator-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed always makes the same record.
   src:"signature" = Signature-authored original (clearly labeled) */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX='JAH-PARTY-';
var TOPICS=[["Charades", "The classic; the acting."], ["Pictionary", "The drawing; the guesses."], ["Codenames", "The word; the spymaster."], ["Wavelength", "The telepathy; the dial."], ["Werewolf/Mafia", "The deception; the accusations."], ["The Jackbox Party Packs", "The phones; the streaming."], ["Among Us", "The sus; the phenomenon."], ["Keep Talking and Nobody Explodes", "The manual; the panic."], ["Overcooked", "The kitchen; the chaos."], ["Mario Party", "The stars; the friendships ended."], ["The Drinking Games", "The responsibly; the classics."], ["Two Truths and a Lie", "The icebreaker; the reveals."], ["The Categories Game", "Scattergories; the lists."], ["Telestrations", "The telephone pictionary; the laughter."], ["Just One", "The co-op; the clues."], ["The Chameleon", "The hidden; the bluff."], ["Spyfall", "The questions; the spy."], ["Dixit", "The dreamy; the art."], ["The Hosting Art", "The energy; the pacing."], ["The Group Size", "The scaling; the splitting."], ["Icebreakers", "The awkward; the best."], ["The Cleanup", "The pieces; the ritual."], ["Digital Party Games", "The apps; the remote."], ["The Classics", "The canon; the why."], ["Designing Party Games", "The accessibility; the advice."], ["The 2025 Hits", "The new; the buzz."], ["The Psychology", "The laughter; the bonding."], ["The Perfect Party", "The mix; the guide."]];
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
    type:'party games exploration', content:content, content_completeness:'stub',
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
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator){JAHDB.registerGenerator('party-games',{generate:generate,validate:validate,driftCheck:driftCheck});}
if(typeof module!=='undefined'&&module.exports){module.exports={generate:generate,validate:validate,driftCheck:driftCheck};}
})();