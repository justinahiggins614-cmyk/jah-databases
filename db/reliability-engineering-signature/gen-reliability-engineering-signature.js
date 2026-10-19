(function(){'use strict';
/* JAH The Reliability Engineering Signature Database generator — jahdb-reliability-engineering-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-RES-";
var FIELDS=["foundations","compounded","advanced"];
var TOPICS={
 "foundations": [
  "Reliability Engineering (Signature): First Principles Refresher — foundations",
  "Reliability Engineering (Signature): Reading Drawings and Specs — foundations",
  "Reliability Engineering (Signature): Materials: Choosing Right — foundations",
  "Reliability Engineering (Signature): The Calculation Habit — foundations",
  "Reliability Engineering (Signature): Safety Factors Explained — foundations",
  "Reliability Engineering (Signature): Failure Modes First — foundations",
  "Reliability Engineering (Signature): Tolerances That Work — foundations",
  "Reliability Engineering (Signature): Prototyping Fast — foundations",
  "Reliability Engineering (Signature): Testing Like It Matters — foundations",
  "Reliability Engineering (Signature): Reading Standards — foundations",
  "Reliability Engineering (Signature): Manufacturing Awareness — foundations",
  "Reliability Engineering (Signature): Cost Engineering — foundations"
 ],
 "compounded": [
  "Reliability Engineering (Signature): Reliability Basics — compounded",
  "Reliability Engineering (Signature): Maintainability Design — compounded",
  "Reliability Engineering (Signature): Human Factors — compounded",
  "Reliability Engineering (Signature): Environmental Responsibility — compounded",
  "Reliability Engineering (Signature): Working With Suppliers — compounded",
  "Reliability Engineering (Signature): Quality Systems — compounded",
  "Reliability Engineering (Signature): Root Cause Analysis — compounded",
  "Reliability Engineering (Signature): Change Control — compounded",
  "Reliability Engineering (Signature): Documentation That Builds — compounded",
  "Reliability Engineering (Signature): Project Planning — compounded",
  "Reliability Engineering (Signature): Advanced: Advanced Analysis — compounded",
  "Reliability Engineering (Signature): Advanced: Systems Engineering — compounded"
 ],
 "advanced": [
  "Reliability Engineering (Signature): Advanced: Risk Management — advanced",
  "Reliability Engineering (Signature): Advanced: Lifecycle Assessment — advanced",
  "Reliability Engineering (Signature): Advanced: Design for Excellence — advanced",
  "Reliability Engineering (Signature): Advanced: Reliability Engineering Deep — advanced",
  "Reliability Engineering (Signature): Advanced: Leading Engineering Teams — advanced",
  "Reliability Engineering (Signature): Advanced: Innovation Methods — advanced",
  "Reliability Engineering (Signature): Advanced: Forensic Engineering — advanced",
  "Reliability Engineering (Signature): Advanced: Standards Development — advanced",
  "Reliability Engineering (Signature): Advanced: The 30-Year View — advanced",
  "Reliability Engineering (Signature): Advanced: Teaching Engineering — advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# The Reliability Engineering Signature Database — structural study\n"
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
var gen={version:'jahdb-reliability-engineering-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('reliability-engineering-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
