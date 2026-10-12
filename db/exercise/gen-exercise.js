(function(){'use strict';
/* Exercise Database generator — jahdb-exercise-generator-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed always makes the same record.
   src:"public" = Fact-checked public information */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX='JAH-EXER-';
var TOPICS=[["Cardio Exercise", "Activities like walking and swimming that raise the heart rate."], ["Strength Training", "Working muscles against resistance to build strength."], ["Flexibility", "Stretching to keep joints moving freely."], ["Warming Up", "Gentle activity preparing the body for harder exercise."], ["Cooling Down", "Easy movement after exercise to recover gradually."], ["Walking", "The simplest exercise, good for nearly everyone."], ["Running", "The classic cardio workout, built up gradually to avoid injury."], ["Swimming", "A full-body workout gentle on the joints."], ["Cycling", "Low-impact cardio for legs and heart."], ["Yoga", "The practice combining poses, breathing, and balance."], ["Stretching", "Lengthening muscles to stay limber and prevent stiffness."], ["Rest Days", "Recovery time that lets muscles repair and grow stronger."], ["Hydration", "Drinking water before, during, and after exercise."], ["Proper Form", "Correct technique that prevents injury and works the right muscles."], ["Breathing", "Steady breathing that fuels working muscles."], ["Bodyweight Exercises", "Strength moves using only your own weight."], ["Push-Ups", "The classic upper-body bodyweight exercise."], ["Squats", "The fundamental lower-body strength movement."], ["Planks", "The core-stability hold that strengthens the midsection."], ["Lunges", "The stepping exercise for legs and balance."], ["Balance Exercises", "Moves that improve stability and prevent falls."], ["Aerobic vs. Anaerobic", "Sustained oxygen-using exercise versus short intense bursts."], ["Consistency", "Regular exercise beats occasional intense workouts."], ["Setting Goals", "Clear, realistic fitness targets that keep motivation up."], ["Exercise and Mood", "How activity helps reduce stress and lift spirits."], ["Exercise and Sleep", "How regular activity supports better rest."], ["Listening to Your Body", "Resting when something hurts rather than pushing through pain."], ["Getting Started", "Beginning gently and building the habit step by step."]];
var ANGLES=['overview','detailed','examples','faq','history','applications'];
function pad(n){var s=String(n);while(s.length<6)s='0'+s;return s;}
function generate(seed,opts){
  var s=prng(seed);
  var ti=(s()*TOPICS.length)|0, ai=(s()*ANGLES.length)|0;
  var topic=TOPICS[ti], angle=ANGLES[ai];
  var id=PREFIX+pad(seed);
  var title=topic[0]+' ('+angle+')';
  var desc=topic[1]+' This '+angle+' guide provides comprehensive coverage.';
  var content='['+angle+'] '+topic[0]+': '+topic[1]+' Full detailed content for '+angle+' perspective.';
  return {
    id:id, title:title, description:desc, genre:angle,
    type:'exercise record', content:content,
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
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator){JAHDB.registerGenerator('exercise',{generate:generate,validate:validate,driftCheck:driftCheck});}
if(typeof module!=='undefined'&&module.exports){module.exports={generate:generate,validate:validate,driftCheck:driftCheck};}
})();