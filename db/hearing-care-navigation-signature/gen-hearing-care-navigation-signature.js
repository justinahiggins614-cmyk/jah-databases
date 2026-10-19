(function(){'use strict';
/* JAH The Hearing Care Navigation Signature Database generator — jahdb-hearing-care-navigation-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-HCNS-";
var FIELDS=["foundations","compounded","advanced"];
var TOPICS={
 "foundations": [
  "Hearing Care Navigation (Signature): Plain-Language Basics — foundations",
  "Hearing Care Navigation (Signature): Normal vs Concern Thresholds — foundations",
  "Hearing Care Navigation (Signature): Preparing for Appointments — foundations",
  "Hearing Care Navigation (Signature): Understanding Test Results — foundations",
  "Hearing Care Navigation (Signature): Medication Management — foundations",
  "Hearing Care Navigation (Signature): Daily Habits That Matter Most — foundations",
  "Hearing Care Navigation (Signature): Nutrition Fundamentals — foundations",
  "Hearing Care Navigation (Signature): Movement and Exercise Basics — foundations",
  "Hearing Care Navigation (Signature): Sleep Foundations — foundations",
  "Hearing Care Navigation (Signature): Stress and Its Signals — foundations",
  "Hearing Care Navigation (Signature): Finding Reliable Information — foundations",
  "Hearing Care Navigation (Signature): Talking to Family About Health — foundations"
 ],
 "compounded": [
  "Hearing Care Navigation (Signature): Navigating Insurance and Costs — compounded",
  "Hearing Care Navigation (Signature): Second Opinions Done Right — compounded",
  "Hearing Care Navigation (Signature): Caregiver Essentials — compounded",
  "Hearing Care Navigation (Signature): Tracking Symptoms Usefully — compounded",
  "Hearing Care Navigation (Signature): Prevention Checklists by Age — compounded",
  "Hearing Care Navigation (Signature): Emergency Recognition — compounded",
  "Hearing Care Navigation (Signature): Mental Health Foundations — compounded",
  "Hearing Care Navigation (Signature): Building Your Care Team — compounded",
  "Hearing Care Navigation (Signature): Health Literacy for Kids — compounded",
  "Hearing Care Navigation (Signature): Workplace Health Intersections — compounded",
  "Hearing Care Navigation (Signature): Advanced: Reading Research — compounded",
  "Hearing Care Navigation (Signature): Advanced: Managing Chronic Conditions — compounded"
 ],
 "advanced": [
  "Hearing Care Navigation (Signature): Advanced: Care Transitions — advanced",
  "Hearing Care Navigation (Signature): Advanced: Advocating in the System — advanced",
  "Hearing Care Navigation (Signature): Advanced: End-of-Life Planning — advanced",
  "Hearing Care Navigation (Signature): Advanced: Health Data and Privacy — advanced",
  "Hearing Care Navigation (Signature): Advanced: Integrative Approaches — advanced",
  "Hearing Care Navigation (Signature): Advanced: Community Health Action — advanced",
  "Hearing Care Navigation (Signature): Advanced: Preparing for Aging — advanced",
  "Hearing Care Navigation (Signature): Advanced: Teaching Health Topics — advanced",
  "Hearing Care Navigation (Signature): Advanced: Emergency Preparedness — advanced",
  "Hearing Care Navigation (Signature): Advanced: The Quantified Self, Wisely — advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# The Hearing Care Navigation Signature Database — structural study\n"
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
var gen={version:'jahdb-hearing-care-navigation-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('hearing-care-navigation-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
