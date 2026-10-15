(function(){'use strict';
/* Signature Chess Database generator — jahdb-chess-generator-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed always makes the same record.
   src:"signature" = Signature-authored original (clearly labeled) */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX='JAH-CHESS-';
var TOPICS=[["The History", "India to Persia; the 1500 years."], ["The Rules", "The moves; the basics."], ["The Openings", "The Ruy Lopez; the theory."], ["The Sicilian Defense", "The counter; the sharp."], ["The Queen's Gambit", "The show; the boom."], ["Tactics: Forks", "The double; the patterns."], ["Tactics: Pins", "The absolute; the skewers."], ["The Endgame", "The king; the technique."], ["The Masters", "Fischer to Carlsen; the legends."], ["The 1972 Match", "Fischer-Spassky; the Cold War."], ["Kasparov vs. Deep Blue", "1997's loss; the milestone."], ["AlphaZero", "The self-taught; the revolution."], ["The Online Boom", "Chess.com; the pandemic."], ["The PogChamps", "The streamers; the crossover."], ["Blitz and Bullet", "The speed; the Hikaru."], ["The Cheating Scandals", "The Niemann; the detection."], ["The World Championship", "The cycle; the format."], ["The Candidates", "The tournament; the grind."], ["Women in Chess", "The Polgar; the gap."], ["Chess in Schools", "The benefits; the programs."], ["The Variants", "Fischer Random; the 960."], ["The Puzzles", "The compositions; the art."], ["The Clocks", "The flag; the increment."], ["The Notation", "The algebraic; the scoresheets."], ["The Psychology", "The tilt; the preparation."], ["The Future", "The freestyle; the prediction."], ["Learning Chess", "The steps; the advice."], ["Why Chess Endures", "The depth; the beauty."]];
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
    type:'chess exploration', content:content, content_completeness:'stub',
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
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator){JAHDB.registerGenerator('chess',{generate:generate,validate:validate,driftCheck:driftCheck});}
if(typeof module!=='undefined'&&module.exports){module.exports={generate:generate,validate:validate,driftCheck:driftCheck};}
})();