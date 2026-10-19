(function(){'use strict';
/* JAH The Tolerance Stack-Up Analysis Database generator — jahdb-tolerance-stack-up-analysis-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-TSUA-";
var FIELDS=["foundations","compounded","advanced"];
var TOPICS={
 "foundations": [
  "Tolerance Stack-Up Analysis: First Principles Refresher — foundations",
  "Tolerance Stack-Up Analysis: Reading Drawings and Specs — foundations",
  "Tolerance Stack-Up Analysis: Materials: Choosing Right — foundations",
  "Tolerance Stack-Up Analysis: The Calculation Habit — foundations",
  "Tolerance Stack-Up Analysis: Safety Factors Explained — foundations",
  "Tolerance Stack-Up Analysis: Failure Modes First — foundations",
  "Tolerance Stack-Up Analysis: Tolerances That Work — foundations",
  "Tolerance Stack-Up Analysis: Prototyping Fast — foundations",
  "Tolerance Stack-Up Analysis: Testing Like It Matters — foundations",
  "Tolerance Stack-Up Analysis: Reading Standards — foundations",
  "Tolerance Stack-Up Analysis: Manufacturing Awareness — foundations",
  "Tolerance Stack-Up Analysis: Cost Engineering — foundations"
 ],
 "compounded": [
  "Tolerance Stack-Up Analysis: Reliability Basics — compounded",
  "Tolerance Stack-Up Analysis: Maintainability Design — compounded",
  "Tolerance Stack-Up Analysis: Human Factors — compounded",
  "Tolerance Stack-Up Analysis: Environmental Responsibility — compounded",
  "Tolerance Stack-Up Analysis: Working With Suppliers — compounded",
  "Tolerance Stack-Up Analysis: Quality Systems — compounded",
  "Tolerance Stack-Up Analysis: Root Cause Analysis — compounded",
  "Tolerance Stack-Up Analysis: Change Control — compounded",
  "Tolerance Stack-Up Analysis: Documentation That Builds — compounded",
  "Tolerance Stack-Up Analysis: Project Planning — compounded",
  "Tolerance Stack-Up Analysis: Advanced: Advanced Analysis — compounded",
  "Tolerance Stack-Up Analysis: Advanced: Systems Engineering — compounded"
 ],
 "advanced": [
  "Tolerance Stack-Up Analysis: Advanced: Risk Management — advanced",
  "Tolerance Stack-Up Analysis: Advanced: Lifecycle Assessment — advanced",
  "Tolerance Stack-Up Analysis: Advanced: Design for Excellence — advanced",
  "Tolerance Stack-Up Analysis: Advanced: Reliability Engineering Deep — advanced",
  "Tolerance Stack-Up Analysis: Advanced: Leading Engineering Teams — advanced",
  "Tolerance Stack-Up Analysis: Advanced: Innovation Methods — advanced",
  "Tolerance Stack-Up Analysis: Advanced: Forensic Engineering — advanced",
  "Tolerance Stack-Up Analysis: Advanced: Standards Development — advanced",
  "Tolerance Stack-Up Analysis: Advanced: The 30-Year View — advanced",
  "Tolerance Stack-Up Analysis: Advanced: Teaching Engineering — advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# The Tolerance Stack-Up Analysis Database — structural study\n"
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
var gen={version:'jahdb-tolerance-stack-up-analysis-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('tolerance-stack-up-analysis',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
