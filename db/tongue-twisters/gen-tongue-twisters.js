(function(){'use strict';
/* Signature Tongue Twisters Database generator — jahdb-tongue-twisters-generator-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed always makes the same record.
   src:"signature" = Signature-authored original (clearly labeled) */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX='JAH-TONGUE-';
var TOPICS=[["Classic Twisters", "The all-time greats everyone mumbles."], ["Silly Sally Set", "She-sells-style shell games."], ["Peter Piper Pack", "Pepper-picking practice lines."], ["Woodchuck Wonders", "How-much-wood classics."], ["Beginner Twisters", "Easy warm-ups for little tongues."], ["Animal Twisters", "Beasts that tie tongues in knots."], ["Food Twisters", "Snack-flavored speech workouts."], ["Speed Twisters", "Say-it-fast championship lines."], ["Long Twisters", "Marathon mouthfuls for pros."], ["Alliteration Adventures", "Letter-focused tongue trainers."], ["Consonant Clusters", "Th-, sh-, and ch- challenges."], ["Vowel Voyages", "Vowel-heavy tricky lines."], ["Name Game Twisters", "Personal-name puzzlers."], ["Silly Sentences", "Goofy phrases that trip you up."], ["Farm Twisters", "Barnyard babble builders."], ["Ocean Twisters", "Seaside speech tangles."], ["Weather Twisters", "Stormy saying stumbles."], ["Holiday Twisters", "Festive flub-makers."], ["Sports Twisters", "Athletic articulation drills."], ["Travel Twisters", "Globe-trotting tongue trips."], ["Monster Twisters", "Spooky-silly sayings."], ["Robot Twisters", "Mechanical mouth exercises."], ["Pirate Twisters", "Arrr-ticulation adventures."], ["Wizard Twisters", "Magical mouthfuls."], ["Party Twisters", "Crowd-pleasing tongue games."]];
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
    type:'tongue twisters creation', content:content, content_completeness:'stub',
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
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator){JAHDB.registerGenerator('tongue-twisters',{generate:generate,validate:validate,driftCheck:driftCheck});}
if(typeof module!=='undefined'&&module.exports){module.exports={generate:generate,validate:validate,driftCheck:driftCheck};}
})();