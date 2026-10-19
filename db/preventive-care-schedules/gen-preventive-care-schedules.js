(function(){'use strict';
/* JAH The Preventive Care Schedules Database generator — jahdb-preventive-care-schedules-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-PCS-";
var FIELDS=["foundations","compounded","advanced"];
var TOPICS={
 "foundations": [
  "Preventive Care Schedules: Plain-Language Basics — foundations",
  "Preventive Care Schedules: Normal vs Concern Thresholds — foundations",
  "Preventive Care Schedules: Preparing for Appointments — foundations",
  "Preventive Care Schedules: Understanding Test Results — foundations",
  "Preventive Care Schedules: Medication Management — foundations",
  "Preventive Care Schedules: Daily Habits That Matter Most — foundations",
  "Preventive Care Schedules: Nutrition Fundamentals — foundations",
  "Preventive Care Schedules: Movement and Exercise Basics — foundations",
  "Preventive Care Schedules: Sleep Foundations — foundations",
  "Preventive Care Schedules: Stress and Its Signals — foundations",
  "Preventive Care Schedules: Finding Reliable Information — foundations",
  "Preventive Care Schedules: Talking to Family About Health — foundations"
 ],
 "compounded": [
  "Preventive Care Schedules: Navigating Insurance and Costs — compounded",
  "Preventive Care Schedules: Second Opinions Done Right — compounded",
  "Preventive Care Schedules: Caregiver Essentials — compounded",
  "Preventive Care Schedules: Tracking Symptoms Usefully — compounded",
  "Preventive Care Schedules: Prevention Checklists by Age — compounded",
  "Preventive Care Schedules: Emergency Recognition — compounded",
  "Preventive Care Schedules: Mental Health Foundations — compounded",
  "Preventive Care Schedules: Building Your Care Team — compounded",
  "Preventive Care Schedules: Health Literacy for Kids — compounded",
  "Preventive Care Schedules: Workplace Health Intersections — compounded",
  "Preventive Care Schedules: Advanced: Reading Research — compounded",
  "Preventive Care Schedules: Advanced: Managing Chronic Conditions — compounded"
 ],
 "advanced": [
  "Preventive Care Schedules: Advanced: Care Transitions — advanced",
  "Preventive Care Schedules: Advanced: Advocating in the System — advanced",
  "Preventive Care Schedules: Advanced: End-of-Life Planning — advanced",
  "Preventive Care Schedules: Advanced: Health Data and Privacy — advanced",
  "Preventive Care Schedules: Advanced: Integrative Approaches — advanced",
  "Preventive Care Schedules: Advanced: Community Health Action — advanced",
  "Preventive Care Schedules: Advanced: Preparing for Aging — advanced",
  "Preventive Care Schedules: Advanced: Teaching Health Topics — advanced",
  "Preventive Care Schedules: Advanced: Emergency Preparedness — advanced",
  "Preventive Care Schedules: Advanced: The Quantified Self, Wisely — advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# The Preventive Care Schedules Database — structural study\n"
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
var gen={version:'jahdb-preventive-care-schedules-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('preventive-care-schedules',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
