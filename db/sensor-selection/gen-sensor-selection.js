(function(){'use strict';
/* JAH The Sensor Selection Database generator — jahdb-sensor-selection-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-SS-";
var FIELDS=["foundations","compounded","advanced"];
var TOPICS={
 "foundations": [
  "Sensor Selection: First Principles Refresher — foundations",
  "Sensor Selection: Reading Drawings and Specs — foundations",
  "Sensor Selection: Materials: Choosing Right — foundations",
  "Sensor Selection: The Calculation Habit — foundations",
  "Sensor Selection: Safety Factors Explained — foundations",
  "Sensor Selection: Failure Modes First — foundations",
  "Sensor Selection: Tolerances That Work — foundations",
  "Sensor Selection: Prototyping Fast — foundations",
  "Sensor Selection: Testing Like It Matters — foundations",
  "Sensor Selection: Reading Standards — foundations",
  "Sensor Selection: Manufacturing Awareness — foundations",
  "Sensor Selection: Cost Engineering — foundations"
 ],
 "compounded": [
  "Sensor Selection: Reliability Basics — compounded",
  "Sensor Selection: Maintainability Design — compounded",
  "Sensor Selection: Human Factors — compounded",
  "Sensor Selection: Environmental Responsibility — compounded",
  "Sensor Selection: Working With Suppliers — compounded",
  "Sensor Selection: Quality Systems — compounded",
  "Sensor Selection: Root Cause Analysis — compounded",
  "Sensor Selection: Change Control — compounded",
  "Sensor Selection: Documentation That Builds — compounded",
  "Sensor Selection: Project Planning — compounded",
  "Sensor Selection: Advanced: Advanced Analysis — compounded",
  "Sensor Selection: Advanced: Systems Engineering — compounded"
 ],
 "advanced": [
  "Sensor Selection: Advanced: Risk Management — advanced",
  "Sensor Selection: Advanced: Lifecycle Assessment — advanced",
  "Sensor Selection: Advanced: Design for Excellence — advanced",
  "Sensor Selection: Advanced: Reliability Engineering Deep — advanced",
  "Sensor Selection: Advanced: Leading Engineering Teams — advanced",
  "Sensor Selection: Advanced: Innovation Methods — advanced",
  "Sensor Selection: Advanced: Forensic Engineering — advanced",
  "Sensor Selection: Advanced: Standards Development — advanced",
  "Sensor Selection: Advanced: The 30-Year View — advanced",
  "Sensor Selection: Advanced: Teaching Engineering — advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# The Sensor Selection Database — structural study\n"
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
var gen={version:'jahdb-sensor-selection-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('sensor-selection',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
