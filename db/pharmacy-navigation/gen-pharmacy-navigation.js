(function(){'use strict';
/* JAH The Pharmacy Navigation Database generator — jahdb-pharmacy-navigation-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-PN-";
var FIELDS=["foundations","compounded","advanced"];
var TOPICS={
 "foundations": [
  "Pharmacy Navigation: Plain-Language Basics — foundations",
  "Pharmacy Navigation: Normal vs Concern Thresholds — foundations",
  "Pharmacy Navigation: Preparing for Appointments — foundations",
  "Pharmacy Navigation: Understanding Test Results — foundations",
  "Pharmacy Navigation: Medication Management — foundations",
  "Pharmacy Navigation: Daily Habits That Matter Most — foundations",
  "Pharmacy Navigation: Nutrition Fundamentals — foundations",
  "Pharmacy Navigation: Movement and Exercise Basics — foundations",
  "Pharmacy Navigation: Sleep Foundations — foundations",
  "Pharmacy Navigation: Stress and Its Signals — foundations",
  "Pharmacy Navigation: Finding Reliable Information — foundations",
  "Pharmacy Navigation: Talking to Family About Health — foundations"
 ],
 "compounded": [
  "Pharmacy Navigation: Navigating Insurance and Costs — compounded",
  "Pharmacy Navigation: Second Opinions Done Right — compounded",
  "Pharmacy Navigation: Caregiver Essentials — compounded",
  "Pharmacy Navigation: Tracking Symptoms Usefully — compounded",
  "Pharmacy Navigation: Prevention Checklists by Age — compounded",
  "Pharmacy Navigation: Emergency Recognition — compounded",
  "Pharmacy Navigation: Mental Health Foundations — compounded",
  "Pharmacy Navigation: Building Your Care Team — compounded",
  "Pharmacy Navigation: Health Literacy for Kids — compounded",
  "Pharmacy Navigation: Workplace Health Intersections — compounded",
  "Pharmacy Navigation: Advanced: Reading Research — compounded",
  "Pharmacy Navigation: Advanced: Managing Chronic Conditions — compounded"
 ],
 "advanced": [
  "Pharmacy Navigation: Advanced: Care Transitions — advanced",
  "Pharmacy Navigation: Advanced: Advocating in the System — advanced",
  "Pharmacy Navigation: Advanced: End-of-Life Planning — advanced",
  "Pharmacy Navigation: Advanced: Health Data and Privacy — advanced",
  "Pharmacy Navigation: Advanced: Integrative Approaches — advanced",
  "Pharmacy Navigation: Advanced: Community Health Action — advanced",
  "Pharmacy Navigation: Advanced: Preparing for Aging — advanced",
  "Pharmacy Navigation: Advanced: Teaching Health Topics — advanced",
  "Pharmacy Navigation: Advanced: Emergency Preparedness — advanced",
  "Pharmacy Navigation: Advanced: The Quantified Self, Wisely — advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# The Pharmacy Navigation Database — structural study\n"
   + "# Field: "+field+"\n"
   + "record = {'title': \""+safe+"\", 'field': \""+field+"\"}\n"
   + "def summarize(r):\n"
   + "    return r['title'] + ' [' + r['field'] + ']'\n"
   + "print(summarize(record))\n"
   + "print('Sample record — structural sample, not an archive entry.')\n";
}
function generate(seed,opts,rnd){
  opts=opts||{}; rnd=rnd||prng(seed);
  var field=opts.field&&FIELDS.indexOf(opts.field)>=0?opts.field:pick(FIELDS,rnd);
  var pool=TOPICS[field]||["General Study"];
  var topic=pick(pool,rnd);
  var id=PREFIX+String(seed).padStart(6,'0');
  return {
    id:id,
    name:topic+' — practical guidance record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A practical guidance record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'public-harvest-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"python",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-pharmacy-navigation-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('pharmacy-navigation',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
