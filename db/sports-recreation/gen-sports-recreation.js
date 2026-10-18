(function(){'use strict';
/* JAH The Sports and Recreation Database generator — jahdb-sports-recreation-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-SPRC-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "What the Sports Industry Is — Overview - Foundations",
  "Exercise Physiology Basics - Foundations",
  "Biomechanics of Movement - Foundations",
  "Training Fundamentals - Foundations",
  "Sports Nutrition Basics - Foundations",
  "Rules of Team Sports - Foundations",
  "Rules of Individual Sports - Foundations",
  "Officiating and Referees - Foundations",
  "Coaching Fundamentals - Foundations",
  "Youth Sports - Foundations",
  "Sports Equipment Basics - Foundations",
  "Sports Math I — Scoring, Averages, and Percentages - Foundations",
 ],
 "Compounded": [
  "Periodization — Training Cycles - Compounded",
  "Strength and Conditioning - Compounded",
  "Sports Medicine Basics - Compounded",
  "Performance Statistics - Compounded",
  "Equipment Engineering - Compounded",
  "Venue Design - Compounded",
  "Field and Turf Management - Compounded",
  "Event Operations - Compounded",
  "Ticketing and Fan Services - Compounded",
  "Sports Broadcasting Basics - Compounded",
  "Recreation Infrastructure — Parks and Trails - Compounded",
 ],
 "Advanced": [
  "Advanced Sports Analytics - Advanced",
  "Anti-Doping Programs - Advanced",
  "Sports Business and Finance - Advanced",
  "Sponsorship and Marketing - Advanced",
  "Adaptive and Paralympic Sports - Advanced",
  "Sports Psychology - Advanced",
  "Facility Maintenance Operations - Advanced",
  "Mega-Event Planning - Advanced",
  "Sports Law Basics - Advanced",
  "The Future of Sport Technology - Advanced",
  "Sports Mastery Review — Running the Whole Industry - Advanced",
 ],
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "#!/usr/bin/env python3\n"
   + "# "+safe+" -- structural sample demo. Property of Justin Addam Higgins (JAH).\n"
   + "# Win-percentage structural sample calculator (sports industry)\n"
   + "w, l = 58.0, 24.0\n"
   + "pct = w/(w+l)\n"
   + "print('sample wins:', w, 'losses:', l)\n"
   + "print('sample win pct:', round(pct,3))\n"
   + "assert 0 <= pct <= 1\n"
   + "print('OK: structural sample demo ran')\n";
}
function generate(seed,opts,rnd){
  opts=opts||{}; rnd=rnd||prng(seed);
  var field=opts.field&&FIELDS.indexOf(opts.field)>=0?opts.field:pick(FIELDS,rnd);
  var pool=TOPICS[field]||["General Study"];
  var topic=pick(pool,rnd);
  var id=PREFIX+String(seed).padStart(6,'0');
  return {
    id:id,
    name:topic+' — sports industry record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A sports industry record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"sports-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
    _seed:seed
  };
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  if(!new RegExp('^'+PREFIX.replace(/-/g,'\\-')+'\\d{6}$').test(r.id||''))e.push('id');
  if(FIELDS.indexOf(r.field)<0)e.push('field');
  if(!r.src)e.push('src');
  if(!r.demo||!r.demo.program)e.push('demo');
  return {ok:!e.length,errors:e};
}
function driftCheck(record,sample){
  var dups=(sample||[]).filter(function(r){return r&&r.title===record.title&&r.field===record.field;});
  return dups.length?{ok:false,errors:['duplicate topic+field in archive sample']}:{ok:true,errors:[]};
}
var gen={version:'jahdb-sports-recreation-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('sports-recreation',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
