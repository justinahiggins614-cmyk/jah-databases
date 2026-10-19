(function(){'use strict';
/* JAH The Care Transition Planning Database generator — jahdb-care-transition-planning-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-CTP-";
var FIELDS=["foundations","compounded","advanced"];
var TOPICS={
 "foundations": [
  "Care Transition Planning: Plain-Language Basics — foundations",
  "Care Transition Planning: Normal vs Concern Thresholds — foundations",
  "Care Transition Planning: Preparing for Appointments — foundations",
  "Care Transition Planning: Understanding Test Results — foundations",
  "Care Transition Planning: Medication Management — foundations",
  "Care Transition Planning: Daily Habits That Matter Most — foundations",
  "Care Transition Planning: Nutrition Fundamentals — foundations",
  "Care Transition Planning: Movement and Exercise Basics — foundations",
  "Care Transition Planning: Sleep Foundations — foundations",
  "Care Transition Planning: Stress and Its Signals — foundations",
  "Care Transition Planning: Finding Reliable Information — foundations",
  "Care Transition Planning: Talking to Family About Health — foundations"
 ],
 "compounded": [
  "Care Transition Planning: Navigating Insurance and Costs — compounded",
  "Care Transition Planning: Second Opinions Done Right — compounded",
  "Care Transition Planning: Caregiver Essentials — compounded",
  "Care Transition Planning: Tracking Symptoms Usefully — compounded",
  "Care Transition Planning: Prevention Checklists by Age — compounded",
  "Care Transition Planning: Emergency Recognition — compounded",
  "Care Transition Planning: Mental Health Foundations — compounded",
  "Care Transition Planning: Building Your Care Team — compounded",
  "Care Transition Planning: Health Literacy for Kids — compounded",
  "Care Transition Planning: Workplace Health Intersections — compounded",
  "Care Transition Planning: Advanced: Reading Research — compounded",
  "Care Transition Planning: Advanced: Managing Chronic Conditions — compounded"
 ],
 "advanced": [
  "Care Transition Planning: Advanced: Care Transitions — advanced",
  "Care Transition Planning: Advanced: Advocating in the System — advanced",
  "Care Transition Planning: Advanced: End-of-Life Planning — advanced",
  "Care Transition Planning: Advanced: Health Data and Privacy — advanced",
  "Care Transition Planning: Advanced: Integrative Approaches — advanced",
  "Care Transition Planning: Advanced: Community Health Action — advanced",
  "Care Transition Planning: Advanced: Preparing for Aging — advanced",
  "Care Transition Planning: Advanced: Teaching Health Topics — advanced",
  "Care Transition Planning: Advanced: Emergency Preparedness — advanced",
  "Care Transition Planning: Advanced: The Quantified Self, Wisely — advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# The Care Transition Planning Database — structural study\n"
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
var gen={version:'jahdb-care-transition-planning-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('care-transition-planning',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
