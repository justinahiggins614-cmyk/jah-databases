(function(){'use strict';
/* JAH The Preventive Care Schedules Signature Database generator — jahdb-preventive-care-schedules-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-PCSS-";
var FIELDS=["foundations","compounded","advanced"];
var TOPICS={
 "foundations": [
  "Preventive Care Schedules (Signature): Plain-Language Basics — foundations",
  "Preventive Care Schedules (Signature): Normal vs Concern Thresholds — foundations",
  "Preventive Care Schedules (Signature): Preparing for Appointments — foundations",
  "Preventive Care Schedules (Signature): Understanding Test Results — foundations",
  "Preventive Care Schedules (Signature): Medication Management — foundations",
  "Preventive Care Schedules (Signature): Daily Habits That Matter Most — foundations",
  "Preventive Care Schedules (Signature): Nutrition Fundamentals — foundations",
  "Preventive Care Schedules (Signature): Movement and Exercise Basics — foundations",
  "Preventive Care Schedules (Signature): Sleep Foundations — foundations",
  "Preventive Care Schedules (Signature): Stress and Its Signals — foundations",
  "Preventive Care Schedules (Signature): Finding Reliable Information — foundations",
  "Preventive Care Schedules (Signature): Talking to Family About Health — foundations"
 ],
 "compounded": [
  "Preventive Care Schedules (Signature): Navigating Insurance and Costs — compounded",
  "Preventive Care Schedules (Signature): Second Opinions Done Right — compounded",
  "Preventive Care Schedules (Signature): Caregiver Essentials — compounded",
  "Preventive Care Schedules (Signature): Tracking Symptoms Usefully — compounded",
  "Preventive Care Schedules (Signature): Prevention Checklists by Age — compounded",
  "Preventive Care Schedules (Signature): Emergency Recognition — compounded",
  "Preventive Care Schedules (Signature): Mental Health Foundations — compounded",
  "Preventive Care Schedules (Signature): Building Your Care Team — compounded",
  "Preventive Care Schedules (Signature): Health Literacy for Kids — compounded",
  "Preventive Care Schedules (Signature): Workplace Health Intersections — compounded",
  "Preventive Care Schedules (Signature): Advanced: Reading Research — compounded",
  "Preventive Care Schedules (Signature): Advanced: Managing Chronic Conditions — compounded"
 ],
 "advanced": [
  "Preventive Care Schedules (Signature): Advanced: Care Transitions — advanced",
  "Preventive Care Schedules (Signature): Advanced: Advocating in the System — advanced",
  "Preventive Care Schedules (Signature): Advanced: End-of-Life Planning — advanced",
  "Preventive Care Schedules (Signature): Advanced: Health Data and Privacy — advanced",
  "Preventive Care Schedules (Signature): Advanced: Integrative Approaches — advanced",
  "Preventive Care Schedules (Signature): Advanced: Community Health Action — advanced",
  "Preventive Care Schedules (Signature): Advanced: Preparing for Aging — advanced",
  "Preventive Care Schedules (Signature): Advanced: Teaching Health Topics — advanced",
  "Preventive Care Schedules (Signature): Advanced: Emergency Preparedness — advanced",
  "Preventive Care Schedules (Signature): Advanced: The Quantified Self, Wisely — advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# The Preventive Care Schedules Signature Database — structural study\n"
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
    name:topic+' — signature-original record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A signature-original record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
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
var gen={version:'jahdb-preventive-care-schedules-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('preventive-care-schedules-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
