(function(){'use strict';
/* Sleep Database generator — jahdb-sleep-generator-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed always makes the same record.
   src:"public" = Fact-checked public information */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX='JAH-SLEEP-';
var TOPICS=[["Why We Sleep", "How sleep restores the brain and body."], ["Sleep Cycles", "The repeating stages from light sleep to deep sleep and REM."], ["REM Sleep", "The dreaming stage of vivid brain activity."], ["Deep Sleep", "The restorative stage of slow brain waves."], ["Circadian Rhythm", "The body's internal twenty-four-hour clock."], ["Melatonin", "The hormone signaling that it is time to sleep."], ["Sleep Hygiene", "The habits promoting good sleep."], ["Naps", "Short daytime rests and how to take them well."], ["Dreams", "The stories the sleeping mind tells."], ["Snoring", "Noisy breathing in sleep and when to ask a doctor."], ["Sleep Apnea", "Breathing interruptions in sleep; a doctor can help."], ["Caffeine and Sleep", "How coffee and tea late in the day disrupt rest."], ["Screens Before Bed", "Why bright screens make falling asleep harder."], ["Consistent Schedules", "Going to bed at regular times."], ["The Bedroom Environment", "Dark, cool, and quiet rooms for better sleep."], ["Exercise and Sleep", "How daytime activity improves nighttime rest."], ["Stress and Sleep", "Calming a worried mind before bed."], ["Teen Sleep", "Why adolescents need more sleep."], ["Baby Sleep", "How infant sleep patterns work."], ["Shift Work", "Sleeping well on irregular schedules."], ["Jet Lag", "Resetting the body clock after travel."], ["Insomnia", "Trouble falling or staying asleep, and what helps."], ["Sleepwalking", "Wandering during sleep, common in children."], ["Nightmares", "Bad dreams and how to handle them."], ["Sleep Talking", "Chattering during sleep, usually harmless."], ["Oversleeping", "Why too much sleep can leave you groggy."], ["Sleep Debt", "Catching up after nights of too little rest."], ["When to See a Doctor", "Persistent sleep problems deserve professional help."]];
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
    type:'sleep record', content:content, content_completeness:'stub',
    stub_note:'Topic stub: the topic title and its one-line brief are real; the full guide article is not yet written. This record does not present shell text as a complete guide.',
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
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator){JAHDB.registerGenerator('sleep',{generate:generate,validate:validate,driftCheck:driftCheck});}
if(typeof module!=='undefined'&&module.exports){module.exports={generate:generate,validate:validate,driftCheck:driftCheck};}
})();