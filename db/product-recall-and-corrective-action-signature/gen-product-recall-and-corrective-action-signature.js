(function(){'use strict';
/* JAH The Product Recall and Corrective Action Signature Database generator — jahdb-product-recall-and-corrective-action-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-PRACAS-";
var FIELDS=["foundations","compounded","advanced"];
var TOPICS={
 "foundations": [
  "Product Recall and Corrective Action (Signature): First Principles Refresher — foundations",
  "Product Recall and Corrective Action (Signature): Reading Drawings and Specs — foundations",
  "Product Recall and Corrective Action (Signature): Materials: Choosing Right — foundations",
  "Product Recall and Corrective Action (Signature): The Calculation Habit — foundations",
  "Product Recall and Corrective Action (Signature): Safety Factors Explained — foundations",
  "Product Recall and Corrective Action (Signature): Failure Modes First — foundations",
  "Product Recall and Corrective Action (Signature): Tolerances That Work — foundations",
  "Product Recall and Corrective Action (Signature): Prototyping Fast — foundations",
  "Product Recall and Corrective Action (Signature): Testing Like It Matters — foundations",
  "Product Recall and Corrective Action (Signature): Reading Standards — foundations",
  "Product Recall and Corrective Action (Signature): Manufacturing Awareness — foundations",
  "Product Recall and Corrective Action (Signature): Cost Engineering — foundations"
 ],
 "compounded": [
  "Product Recall and Corrective Action (Signature): Reliability Basics — compounded",
  "Product Recall and Corrective Action (Signature): Maintainability Design — compounded",
  "Product Recall and Corrective Action (Signature): Human Factors — compounded",
  "Product Recall and Corrective Action (Signature): Environmental Responsibility — compounded",
  "Product Recall and Corrective Action (Signature): Working With Suppliers — compounded",
  "Product Recall and Corrective Action (Signature): Quality Systems — compounded",
  "Product Recall and Corrective Action (Signature): Root Cause Analysis — compounded",
  "Product Recall and Corrective Action (Signature): Change Control — compounded",
  "Product Recall and Corrective Action (Signature): Documentation That Builds — compounded",
  "Product Recall and Corrective Action (Signature): Project Planning — compounded",
  "Product Recall and Corrective Action (Signature): Advanced: Advanced Analysis — compounded",
  "Product Recall and Corrective Action (Signature): Advanced: Systems Engineering — compounded"
 ],
 "advanced": [
  "Product Recall and Corrective Action (Signature): Advanced: Risk Management — advanced",
  "Product Recall and Corrective Action (Signature): Advanced: Lifecycle Assessment — advanced",
  "Product Recall and Corrective Action (Signature): Advanced: Design for Excellence — advanced",
  "Product Recall and Corrective Action (Signature): Advanced: Reliability Engineering Deep — advanced",
  "Product Recall and Corrective Action (Signature): Advanced: Leading Engineering Teams — advanced",
  "Product Recall and Corrective Action (Signature): Advanced: Innovation Methods — advanced",
  "Product Recall and Corrective Action (Signature): Advanced: Forensic Engineering — advanced",
  "Product Recall and Corrective Action (Signature): Advanced: Standards Development — advanced",
  "Product Recall and Corrective Action (Signature): Advanced: The 30-Year View — advanced",
  "Product Recall and Corrective Action (Signature): Advanced: Teaching Engineering — advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# The Product Recall and Corrective Action Signature Database — structural study\n"
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
var gen={version:'jahdb-product-recall-and-corrective-action-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('product-recall-and-corrective-action-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
