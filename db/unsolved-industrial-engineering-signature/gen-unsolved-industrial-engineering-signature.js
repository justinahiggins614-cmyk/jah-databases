(function(){'use strict';
/* JAH The Unsolved Industrial Engineering Signature Database generator — jahdb-unsolved-industrial-engineering-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-USIES-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "The Assembly Line Balancing Problem (Signature Edition) - Manufacturing Systems",
  "The Facility Layout Problem (Signature Edition) - Manufacturing Systems",
  "The Bottleneck Identification Problem (Signature Edition) - Manufacturing Systems",
  "The Work Measurement in Knowledge Work Problem (Signature Edition) - Human Factors",
  "The Learning Curve Universality Problem (Signature Edition) - Human Factors",
  "The Overall Equipment Effectiveness Decomposition Problem (Signature Edition) - Manufacturing Systems",
  "The Single Minute Die Exchange Limit Problem (Signature Edition) - Manufacturing Systems",
  "The Statistical Process Control for Autocorrelated Data Problem (Signature Edition) - Quality Engineering",
  "The Small Batch Quality Control Problem (Signature Edition) - Quality Engineering",
  "The Tolerance Allocation Problem (Signature Edition) - Quality Engineering",
  "The Shift Work Circadian Optimization Problem (Signature Edition) - Human Factors"
 ],
 "Compounded": [
  "The Cellular Manufacturing Design Problem (Signature Edition) - Manufacturing Systems",
  "The Flexible Manufacturing Scheduling Problem (Signature Edition) - Manufacturing Systems",
  "The Predictive Maintenance Remaining Life Problem (Signature Edition) - Manufacturing Systems",
  "The Digital Twin Fidelity Problem (Signature Edition) - Manufacturing Systems",
  "The Lean Against Resilience Tradeoff Problem (Signature Edition) - Manufacturing Systems",
  "The Warehouse Slotting Problem (Signature Edition) - Manufacturing Systems",
  "The Order Picking Routing Problem (Signature Edition) - Manufacturing Systems",
  "The Production Planning Hierarchy Integration Problem (Signature Edition) - Manufacturing Systems",
  "The Capacitated Lot Sizing Problem (Signature Edition) - Manufacturing Systems",
  "The Human Robot Collaboration Safety Problem (Signature Edition) - Human Factors",
  "The Exoskeleton Effectiveness Problem (Signature Edition) - Human Factors",
  "The Safety Culture Measurement Problem (Signature Edition) - Human Factors"
 ],
 "Advanced": [
  "The Cognitive Workload Quantification Problem (Signature Edition) - Human Factors",
  "The Ergonomic Injury Prediction Problem (Signature Edition) - Human Factors",
  "The Design of Experiments for Complex Systems Problem (Signature Edition) - Quality Engineering",
  "The Response Surface Global Optimization Problem (Signature Edition) - Quality Engineering",
  "The Supply Chain Network Design Under Disruption Problem (Signature Edition) - Manufacturing Systems",
  "The Theory of Constraints Throughput Limit Problem (Signature Edition) - Manufacturing Systems",
  "The Jidoka Automation Limit Problem (Signature Edition) - Manufacturing Systems",
  "The Resilience Engineering Quantification Problem (Signature Edition) - Human Factors",
  "The Material Handling System Selection Problem (Signature Edition) - Manufacturing Systems",
  "The Sequencing With Setup Times Problem (Signature Edition) - Manufacturing Systems",
  "The Unified Human Machine System Design Problem (Signature Edition) - Human Factors"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Unsolved Industrial Engineering Study — "+safe+"\n"
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
    name:topic+' — unsolved problem record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A unsolved problem record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"unsolved-industrial-engineering-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-unsolved-industrial-engineering-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('unsolved-industrial-engineering-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
