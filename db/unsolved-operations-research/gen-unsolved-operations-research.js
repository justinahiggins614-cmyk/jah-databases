(function(){'use strict';
/* JAH The Unsolved Operations Research Database generator — jahdb-unsolved-operations-research-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-USOR-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "The Traveling Salesman Exact Solution Problem - Optimization",
  "The Vehicle Routing Exact Problem - Optimization",
  "The Bin Packing Online Problem - Optimization",
  "The Job Shop Scheduling Problem - Optimization",
  "The Cutting Stock Problem - Optimization",
  "The Facility Location Approximation Gap - Optimization",
  "The Inventory Policy Under Nonstationary Demand Problem - Stochastic Models",
  "The Secretary Problem and Optimal Stopping - Decision Analysis",
  "The Multi-Armed Bandit Lower Bound Problem - Stochastic Models",
  "The Online Bipartite Matching Problem - Optimization",
  "The Newsvendor Problem Extensions - Stochastic Models"
 ],
 "Compounded": [
  "The Branch and Bound Node Selection Problem - Optimization",
  "The Cutting Plane Closure Problem - Optimization",
  "The Column Generation Convergence Problem - Optimization",
  "The Mixed Integer Nonlinear Programming Problem - Optimization",
  "The Stochastic Programming Scenario Problem - Stochastic Models",
  "The Robust Optimization Conservatism Problem - Stochastic Models",
  "The Multi-Objective Pareto Frontier Problem - Decision Analysis",
  "The Dynamic Pricing With Strategic Customers Problem - Decision Analysis",
  "The Revenue Management Network Problem - Decision Analysis",
  "The Supply Chain Bullwhip Quantification Problem - Stochastic Models",
  "The Resource Constrained Project Scheduling Problem - Optimization",
  "The Crew Scheduling Set Partitioning Problem - Optimization"
 ],
 "Advanced": [
  "The Semidefinite Programming Rank Problem - Optimization",
  "The Simulation Optimization Convergence Problem - Stochastic Models",
  "The Ranking and Selection Problem - Stochastic Models",
  "The Markov Decision Process Sample Complexity Problem - Stochastic Models",
  "The Queueing Network Product Form Limit Problem - Stochastic Models",
  "The Maintenance Optimization With Imperfect Information Problem - Stochastic Models",
  "The Reliability Allocation Problem - Optimization",
  "The Truthful Mechanism Design Problem - Decision Analysis",
  "The Nash Equilibrium Computation Problem - Decision Analysis",
  "The Discrete Event Simulation Warmup Problem - Stochastic Models",
  "The Unified Optimization Under Uncertainty Problem - Decision Analysis"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Unsolved Operations Research Study — "+safe+"\n"
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
    demo:{kind:"unsolved-operations-research-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-unsolved-operations-research-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('unsolved-operations-research',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
