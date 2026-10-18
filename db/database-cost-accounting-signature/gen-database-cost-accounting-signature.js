(function(){'use strict';
/* JAH The Database Cost Accounting Signature Database generator — jahdb-database-cost-accounting-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-DCAS-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "Cost Accounting Overview (Signature Edition) - Foundations",
  "Storage Cost Model (Signature Edition) - Foundations",
  "Compute Cost Model (Signature Edition) - Foundations",
  "Bandwidth and Egress Cost Model (Signature Edition) - Foundations",
  "Indexing Cost Model (Signature Edition) - Foundations",
  "Generation Cost Model (Signature Edition) - Foundations",
  "Retrieval Cost Model (Signature Edition) - Foundations",
  "Fixed vs Variable Costs (Signature Edition) - Foundations",
  "Cost Allocation Principles (Signature Edition) - Foundations",
  "Per-Record Cost Unit (Signature Edition) - Foundations"
 ],
 "Compounded": [
  "Per-Database Cost Ledger (Signature Edition) - Compounded",
  "Shared-Cost Allocation Models (Signature Edition) - Compounded",
  "Storage Tiering Costs (Signature Edition) - Compounded",
  "Index Rebuild Costs (Signature Edition) - Compounded",
  "Generation Batch Costing (Signature Edition) - Compounded",
  "Retrieval SLA Cost Tradeoffs (Signature Edition) - Compounded",
  "Cache Cost-Benefit Analysis (Signature Edition) - Compounded",
  "Compression Savings Record (Signature Edition) - Compounded",
  "Backup and Disaster Recovery Costs (Signature Edition) - Compounded",
  "Inter-Shard Transfer Costs (Signature Edition) - Compounded",
  "Cost Anomaly Detection (Signature Edition) - Compounded"
 ],
 "Advanced": [
  "Total Cost of Ownership at Scale (Signature Edition) - Advanced",
  "Forecasting-Driven Budgeting (Signature Edition) - Advanced",
  "Chargeback and Showback Models (Signature Edition) - Advanced",
  "Cost of Data Quality (Signature Edition) - Advanced",
  "Cost of Governance Overhead (Signature Edition) - Advanced",
  "Marginal Cost per Million Records (Signature Edition) - Advanced",
  "Public vs Signature Pipeline Cost Comparison (Signature Edition) - Advanced",
  "Energy and Carbon Cost Accounting (Signature Edition) - Advanced",
  "Cost Audit Record (Signature Edition) - Advanced",
  "Budget Variance Record (Signature Edition) - Advanced",
  "Cost Optimization Playbook (Signature Edition) - Advanced",
  "Cost Dashboard Exemplar (Signature Edition) - Advanced",
  "Cost Self-Audit and Mastery Record (Signature Edition) - Advanced"
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
var gen={version:'jahdb-database-cost-accounting-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('database-cost-accounting-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
