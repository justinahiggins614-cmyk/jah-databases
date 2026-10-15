(function(){'use strict';
/* Calendars Database generator — jahdb-calendars-generator-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed always makes the same record.
   src:"public" = Fact-checked public information */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX='JAH-CAL-';
var TOPICS=[["The Gregorian Calendar", "The internationally used civil calendar, a refinement of the Julian calendar."], ["The Julian Calendar", "The Roman calendar introduced by Julius Caesar, basis of the Gregorian reform."], ["Lunar Calendars", "Calendars based on the phases of the Moon, such as the Islamic calendar."], ["Solar Calendars", "Calendars based on the Earth's orbit around the Sun."], ["Leap Year", "The extra day added roughly every four years to keep the calendar aligned with the seasons."], ["The Months", "The twelve divisions of the year, most named for Roman gods, emperors, or numbers."], ["The Week", "The seven-day cycle, with day names rooted in ancient gods and planets."], ["Fiscal Year", "The twelve-month accounting period used by governments and businesses."], ["School Year", "The annual term of classes, typically running from late summer to spring."], ["Holiday Calendars", "Annual listings of public holidays and observances."], ["Timekeeping History", "From sundials and water clocks to atomic clocks, the story of measuring time."], ["The Sundial", "The ancient device telling time by the shadow of the Sun."], ["The Hourglass", "The sand timer used for centuries to measure short intervals."], ["Chinese Zodiac", "The twelve-year animal cycle used in traditional Chinese timekeeping."], ["The Mayan Calendar", "The intricate calendar systems of the ancient Maya civilization."], ["The Hebrew Calendar", "The lunisolar calendar used for Jewish religious observance."], ["The Islamic Calendar", "The lunar calendar used to date religious events in Islam."], ["Daylight Saving Time", "The seasonal clock shift practiced in many countries to extend evening daylight."], ["The 24-Hour Clock", "The timekeeping format counting hours from midnight to midnight."], ["Time Zones", "The regions sharing a standard time, based on longitude."], ["The International Date Line", "The line where the calendar date changes when crossed."], ["Eras and Epochs", "Systems of counting years from a starting point, such as the common era."], ["Perpetual Calendars", "Calendars and devices that give the weekday for any date."], ["Advent Calendars", "December calendars counting down the days to Christmas."], ["Wall Calendars", "The familiar printed yearly calendar with monthly grids."], ["Desk Calendars", "Compact daily or weekly calendars for offices."], ["Astronomical Calendars", "Calendars based on observed celestial events."], ["Calendar Reform", "Historical efforts to fix calendar drift, including the Gregorian reform."]];
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
    type:'calendars record', content:content, content_completeness:'stub',
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
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator){JAHDB.registerGenerator('calendars',{generate:generate,validate:validate,driftCheck:driftCheck});}
if(typeof module!=='undefined'&&module.exports){module.exports={generate:generate,validate:validate,driftCheck:driftCheck};}
})();