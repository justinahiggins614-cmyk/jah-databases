(function(){'use strict';
/* JAH The Database Cost Accounting Database generator — jahdb-database-cost-accounting-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-DCA-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "Cost Accounting Overview - Foundations",
  "Storage Cost Model - Foundations",
  "Compute Cost Model - Foundations",
  "Bandwidth and Egress Cost Model - Foundations",
  "Indexing Cost Model - Foundations",
  "Generation Cost Model - Foundations",
  "Retrieval Cost Model - Foundations",
  "Fixed vs Variable Costs - Foundations",
  "Cost Allocation Principles - Foundations",
  "Per-Record Cost Unit - Foundations"
 ],
 "Compounded": [
  "Per-Database Cost Ledger - Compounded",
  "Shared-Cost Allocation Models - Compounded",
  "Storage Tiering Costs - Compounded",
  "Index Rebuild Costs - Compounded",
  "Generation Batch Costing - Compounded",
  "Retrieval SLA Cost Tradeoffs - Compounded",
  "Cache Cost-Benefit Analysis - Compounded",
  "Compression Savings Record - Compounded",
  "Backup and Disaster Recovery Costs - Compounded",
  "Inter-Shard Transfer Costs - Compounded",
  "Cost Anomaly Detection - Compounded"
 ],
 "Advanced": [
  "Total Cost of Ownership at Scale - Advanced",
  "Forecasting-Driven Budgeting - Advanced",
  "Chargeback and Showback Models - Advanced",
  "Cost of Data Quality - Advanced",
  "Cost of Governance Overhead - Advanced",
  "Marginal Cost per Million Records - Advanced",
  "Public vs Signature Pipeline Cost Comparison - Advanced",
  "Energy and Carbon Cost Accounting - Advanced",
  "Cost Audit Record - Advanced",
  "Budget Variance Record - Advanced",
  "Cost Optimization Playbook - Advanced",
  "Cost Dashboard Exemplar - Advanced",
  "Cost Self-Audit and Mastery Record - Advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Cost Study — "+safe+"\n"
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
    name:topic+' — cost accounting record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A cost accounting record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"cost-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-database-cost-accounting-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('database-cost-accounting',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
