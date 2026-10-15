(function(){'use strict';
/* Time Zones Database generator — jahdb-time-zones-generator-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed always makes the same record.
   src:"public" = Fact-checked public information */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX='JAH-TZ-';
var TOPICS=[["UTC", "Coordinated Universal Time, the world's time standard."], ["Greenwich Mean Time", "The historic basis of world time zones."], ["The Prime Meridian", "The zero line from which zones are counted."], ["The International Date Line", "Where the calendar date changes."], ["Eastern Time", "The zone of New York and the United States East Coast."], ["Pacific Time", "The zone of Los Angeles and the United States West Coast."], ["Central European Time", "The zone covering much of Western Europe."], ["India Standard Time", "The half-hour zone of India."], ["Japan Standard Time", "The zone of Japan, nine hours ahead of UTC."], ["Australian Eastern Time", "The zone of Sydney and Melbourne."], ["Daylight Saving Time", "The seasonal clock shift for longer evenings."], ["Jet Lag", "The body-clock disruption of crossing zones."], ["Converting Time Zones", "Adding and subtracting hours to find the time elsewhere."], ["World Clocks", "Displays showing many zones at once."], ["The 24-Hour Clock", "Military and international time format."], ["Local Solar Time", "Time by the Sun before standard zones."], ["Half-Hour Zones", "Zones offset by thirty minutes, like India's."], ["The Date Line Crossing", "Gaining or losing a day when crossing."], ["Scheduling Across Zones", "Finding meeting times for global teams."], ["Flight Times", "Why arrival times differ from departure times."], ["Time Zone Maps", "Visual guides to the world's zones."], ["China's Single Zone", "One official time across the whole country."], ["Russia's Many Zones", "The numerous zones spanning the country."], ["Arizona and Daylight Saving", "The state that mostly skips the clock change."], ["The History of Time Zones", "How railways created standard time."], ["Atomic Clocks", "The ultra-precise keepers of world time."], ["Leap Seconds", "Occasional adjustments keeping clocks aligned with Earth."], ["Living on Zone Borders", "Towns where the time changes across the street."]];
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
    type:'time zones record', content:content, content_completeness:'stub',
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
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator){JAHDB.registerGenerator('time-zones',{generate:generate,validate:validate,driftCheck:driftCheck});}
if(typeof module!=='undefined'&&module.exports){module.exports={generate:generate,validate:validate,driftCheck:driftCheck};}
})();