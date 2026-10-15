(function(){'use strict';
/* Signature 15 Minute Cities Database generator — jahdb-15-minute-cities-generator-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed always makes the same record.
   src:"signature" = Signature-authored original (clearly labeled) */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX='JAH-15MIN-';
var TOPICS=[["The Concept", "Daily needs within 15 minutes; Carlos Moreno's urban vision."], ["Paris's Implementation", "Mayor Hidalgo adopted it; the bike lanes multiplied."], ["The Four Pillars", "Proximity, diversity, density, ubiquity; the framework."], ["Chronourbanism", "Planning by time, not distance; the paradigm shift."], ["Melbourne's 20-Minute Neighbourhoods", "The Australian parallel; the policy spread."], ["Portland's Complete Neighborhoods", "The American version; the zoning fights."], ["The Conspiracy Backlash", "Lockdown fears hijacked the concept; the misinformation."], ["Oxford's Traffic Filters", "Protests erupted; the implementation stumbled."], ["What It Isn't", "Not confinement, not bans; the clarifications."], ["The Equity Question", "Do poor areas get 15-minute service?; the justice test."], ["Gentrification Risks", "Improvements raise rents; the paradox."], ["The Suburban Challenge", "Sprawl resists proximity; the retrofit problem."], ["Rural Exclusion", "The concept is urban; the countryside differs."], ["Health Benefits", "Walking cities are healthier; the data is strong."], ["Climate Benefits", "Fewer car trips; the emissions math."], ["Local Economies", "Neighborhood shops thrive; the economic case."], ["The Role of Density", "Gentle density enables; the missing middle."], ["Mixed-Use Zoning", "Ending single-use separation; the reform wave."], ["School Proximity", "Kids walk to school; the generational win."], ["Elderly-Friendly Design", "Aging in walkable places; the demographic fit."], ["Digital Services Layer", "Apps coordinate local life; the tech enablement."], ["Measuring the 15 Minutes", "Isochrone mapping; the analytics."], ["Critics: Freedom of Movement", "Car advocates object; the culture clash."], ["The Global South Angle", "Informal cities are already 15-minute; the lesson reverses."], ["Implementation Playbook", "Tactical urbanism to policy; the steps."], ["The 2040 City", "Polycentric regions; the vision."], ["Beyond 15 Minutes", "The one-minute city; the radical edge."], ["The Deeper Goal", "Time affluence; the philosophy."]];
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
    type:'15 minute cities exploration', content:content, content_completeness:'stub',
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
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator){JAHDB.registerGenerator('15-minute-cities',{generate:generate,validate:validate,driftCheck:driftCheck});}
if(typeof module!=='undefined'&&module.exports){module.exports={generate:generate,validate:validate,driftCheck:driftCheck};}
})();