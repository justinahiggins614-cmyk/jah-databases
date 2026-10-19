(function(){'use strict';
/* JAH The Reliability Engineering Database generator — jahdb-reliability-engineering-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-RE-";
var FIELDS=["foundations","compounded","advanced"];
var TOPICS={
 "foundations": [
  "Reliability Engineering: First Principles Refresher — foundations",
  "Reliability Engineering: Reading Drawings and Specs — foundations",
  "Reliability Engineering: Materials: Choosing Right — foundations",
  "Reliability Engineering: The Calculation Habit — foundations",
  "Reliability Engineering: Safety Factors Explained — foundations",
  "Reliability Engineering: Failure Modes First — foundations",
  "Reliability Engineering: Tolerances That Work — foundations",
  "Reliability Engineering: Prototyping Fast — foundations",
  "Reliability Engineering: Testing Like It Matters — foundations",
  "Reliability Engineering: Reading Standards — foundations",
  "Reliability Engineering: Manufacturing Awareness — foundations",
  "Reliability Engineering: Cost Engineering — foundations"
 ],
 "compounded": [
  "Reliability Engineering: Reliability Basics — compounded",
  "Reliability Engineering: Maintainability Design — compounded",
  "Reliability Engineering: Human Factors — compounded",
  "Reliability Engineering: Environmental Responsibility — compounded",
  "Reliability Engineering: Working With Suppliers — compounded",
  "Reliability Engineering: Quality Systems — compounded",
  "Reliability Engineering: Root Cause Analysis — compounded",
  "Reliability Engineering: Change Control — compounded",
  "Reliability Engineering: Documentation That Builds — compounded",
  "Reliability Engineering: Project Planning — compounded",
  "Reliability Engineering: Advanced: Advanced Analysis — compounded",
  "Reliability Engineering: Advanced: Systems Engineering — compounded"
 ],
 "advanced": [
  "Reliability Engineering: Advanced: Risk Management — advanced",
  "Reliability Engineering: Advanced: Lifecycle Assessment — advanced",
  "Reliability Engineering: Advanced: Design for Excellence — advanced",
  "Reliability Engineering: Advanced: Reliability Engineering Deep — advanced",
  "Reliability Engineering: Advanced: Leading Engineering Teams — advanced",
  "Reliability Engineering: Advanced: Innovation Methods — advanced",
  "Reliability Engineering: Advanced: Forensic Engineering — advanced",
  "Reliability Engineering: Advanced: Standards Development — advanced",
  "Reliability Engineering: Advanced: The 30-Year View — advanced",
  "Reliability Engineering: Advanced: Teaching Engineering — advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# The Reliability Engineering Database — structural study\n"
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
var gen={version:'jahdb-reliability-engineering-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('reliability-engineering',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
