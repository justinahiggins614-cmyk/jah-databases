(function(){'use strict';
/* JAH The Medical Terminology Explainer Database generator — jahdb-medical-terminology-explainer-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-MTE-";
var FIELDS=["foundations","compounded","advanced"];
var TOPICS={
 "foundations": [
  "Medical Terminology Explainer: Plain-Language Basics — foundations",
  "Medical Terminology Explainer: Normal vs Concern Thresholds — foundations",
  "Medical Terminology Explainer: Preparing for Appointments — foundations",
  "Medical Terminology Explainer: Understanding Test Results — foundations",
  "Medical Terminology Explainer: Medication Management — foundations",
  "Medical Terminology Explainer: Daily Habits That Matter Most — foundations",
  "Medical Terminology Explainer: Nutrition Fundamentals — foundations",
  "Medical Terminology Explainer: Movement and Exercise Basics — foundations",
  "Medical Terminology Explainer: Sleep Foundations — foundations",
  "Medical Terminology Explainer: Stress and Its Signals — foundations",
  "Medical Terminology Explainer: Finding Reliable Information — foundations",
  "Medical Terminology Explainer: Talking to Family About Health — foundations"
 ],
 "compounded": [
  "Medical Terminology Explainer: Navigating Insurance and Costs — compounded",
  "Medical Terminology Explainer: Second Opinions Done Right — compounded",
  "Medical Terminology Explainer: Caregiver Essentials — compounded",
  "Medical Terminology Explainer: Tracking Symptoms Usefully — compounded",
  "Medical Terminology Explainer: Prevention Checklists by Age — compounded",
  "Medical Terminology Explainer: Emergency Recognition — compounded",
  "Medical Terminology Explainer: Mental Health Foundations — compounded",
  "Medical Terminology Explainer: Building Your Care Team — compounded",
  "Medical Terminology Explainer: Health Literacy for Kids — compounded",
  "Medical Terminology Explainer: Workplace Health Intersections — compounded",
  "Medical Terminology Explainer: Advanced: Reading Research — compounded",
  "Medical Terminology Explainer: Advanced: Managing Chronic Conditions — compounded"
 ],
 "advanced": [
  "Medical Terminology Explainer: Advanced: Care Transitions — advanced",
  "Medical Terminology Explainer: Advanced: Advocating in the System — advanced",
  "Medical Terminology Explainer: Advanced: End-of-Life Planning — advanced",
  "Medical Terminology Explainer: Advanced: Health Data and Privacy — advanced",
  "Medical Terminology Explainer: Advanced: Integrative Approaches — advanced",
  "Medical Terminology Explainer: Advanced: Community Health Action — advanced",
  "Medical Terminology Explainer: Advanced: Preparing for Aging — advanced",
  "Medical Terminology Explainer: Advanced: Teaching Health Topics — advanced",
  "Medical Terminology Explainer: Advanced: Emergency Preparedness — advanced",
  "Medical Terminology Explainer: Advanced: The Quantified Self, Wisely — advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# The Medical Terminology Explainer Database — structural study\n"
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
var gen={version:'jahdb-medical-terminology-explainer-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('medical-terminology-explainer',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
