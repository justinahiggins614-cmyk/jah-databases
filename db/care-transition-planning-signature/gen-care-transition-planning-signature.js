(function(){'use strict';
/* JAH The Care Transition Planning Signature Database generator — jahdb-care-transition-planning-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-CTPS-";
var FIELDS=["foundations","compounded","advanced"];
var TOPICS={
 "foundations": [
  "Care Transition Planning (Signature): Plain-Language Basics — foundations",
  "Care Transition Planning (Signature): Normal vs Concern Thresholds — foundations",
  "Care Transition Planning (Signature): Preparing for Appointments — foundations",
  "Care Transition Planning (Signature): Understanding Test Results — foundations",
  "Care Transition Planning (Signature): Medication Management — foundations",
  "Care Transition Planning (Signature): Daily Habits That Matter Most — foundations",
  "Care Transition Planning (Signature): Nutrition Fundamentals — foundations",
  "Care Transition Planning (Signature): Movement and Exercise Basics — foundations",
  "Care Transition Planning (Signature): Sleep Foundations — foundations",
  "Care Transition Planning (Signature): Stress and Its Signals — foundations",
  "Care Transition Planning (Signature): Finding Reliable Information — foundations",
  "Care Transition Planning (Signature): Talking to Family About Health — foundations"
 ],
 "compounded": [
  "Care Transition Planning (Signature): Navigating Insurance and Costs — compounded",
  "Care Transition Planning (Signature): Second Opinions Done Right — compounded",
  "Care Transition Planning (Signature): Caregiver Essentials — compounded",
  "Care Transition Planning (Signature): Tracking Symptoms Usefully — compounded",
  "Care Transition Planning (Signature): Prevention Checklists by Age — compounded",
  "Care Transition Planning (Signature): Emergency Recognition — compounded",
  "Care Transition Planning (Signature): Mental Health Foundations — compounded",
  "Care Transition Planning (Signature): Building Your Care Team — compounded",
  "Care Transition Planning (Signature): Health Literacy for Kids — compounded",
  "Care Transition Planning (Signature): Workplace Health Intersections — compounded",
  "Care Transition Planning (Signature): Advanced: Reading Research — compounded",
  "Care Transition Planning (Signature): Advanced: Managing Chronic Conditions — compounded"
 ],
 "advanced": [
  "Care Transition Planning (Signature): Advanced: Care Transitions — advanced",
  "Care Transition Planning (Signature): Advanced: Advocating in the System — advanced",
  "Care Transition Planning (Signature): Advanced: End-of-Life Planning — advanced",
  "Care Transition Planning (Signature): Advanced: Health Data and Privacy — advanced",
  "Care Transition Planning (Signature): Advanced: Integrative Approaches — advanced",
  "Care Transition Planning (Signature): Advanced: Community Health Action — advanced",
  "Care Transition Planning (Signature): Advanced: Preparing for Aging — advanced",
  "Care Transition Planning (Signature): Advanced: Teaching Health Topics — advanced",
  "Care Transition Planning (Signature): Advanced: Emergency Preparedness — advanced",
  "Care Transition Planning (Signature): Advanced: The Quantified Self, Wisely — advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# The Care Transition Planning Signature Database — structural study\n"
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
var gen={version:'jahdb-care-transition-planning-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('care-transition-planning-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
