(function(){'use strict';
/* JAH Fundamentals of Operations Research Database generator — jahdb-fundamental-operations-research-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic fundamental record generation: pick a field, set a seed, get a complete record.
   Same seed + same field = same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-OR-";
var FIELDS=["linear programming", "integer programming", "queuing theory", "network optimization", "inventory theory", "simulation"];
var TOPICS=[
    {t: "What Operations Research Does", b: "OR turns decisions into mathematics: define variables, write the objective, list constraints, and compute the provably best choice."},
    {t: "Linear Programming", b: "Optimizing a linear objective over linear constraints; the optimum always sits at a corner of the feasible region \u2014 the simplex method walks corners."},
    {t: "Duality and Shadow Prices", b: "Every LP has a dual whose variables price the constraints: shadow prices tell exactly what one more unit of a resource is worth."},
    {t: "Integer Programming", b: "Requiring whole-number answers (trucks, people, yes/no choices) makes problems vastly harder \u2014 branch-and-bound searches systematically."},
    {t: "Queuing Theory", b: "Arrival and service rates determine waits: Little's law (L = \u03bbW) and the M/M/1 formulas predict lines at call centers, ports, and ERs."},
    {t: "Why Queues Explode", b: "As utilization nears 100%, waiting time blows up nonlinearly \u2014 running a system at 95% busy guarantees long queues from tiny variations."},
    {t: "Network Flows", b: "Shortest paths, max flows, and min-cost flows route trucks, data, and power; the max-flow min-cut theorem exposes every network's bottleneck."},
    {t: "Inventory and EOQ", b: "The economic order quantity balances ordering cost against holding cost: order \u221a(2DS/H) at a time for minimum total cost."},
    {t: "Project Scheduling (CPM/PERT)", b: "Critical-path analysis finds which tasks truly gate a project; slack elsewhere is free, delay on the critical path delays everything."},
    {t: "Markov Decision Processes", b: "Sequential decisions under uncertainty become MDPs: states, actions, rewards, and Bellman's equation for optimal policies."},
    {t: "Simulation and Monte Carlo", b: "When formulas fail, simulate: run thousands of randomized trials to estimate outcomes of complex stochastic systems."},
    {t: "Heuristics for Hard Problems", b: "For NP-hard routing and scheduling, greedy, local search, and genetic heuristics find excellent (not provably optimal) answers fast."}
];
var PRINCIPLES=[
    {n: "LP duality", e: "primal optimum = dual optimum", s: "Every linear program has a mirror whose optimum equals it \u2014 and reveals shadow prices."},
    {n: "Little's law", e: "L = \u03bb * W", s: "Average queue length equals arrival rate times average wait \u2014 true for any stable queue."},
    {n: "Max-flow min-cut", e: "max flow = min cut capacity", s: "The most you can push through a network equals the cheapest bottleneck separating source from sink."}
];
var USES=["Routing delivery fleets", "Staffing call centers and hospitals", "Scheduling airline crews", "Managing warehouse inventory"];
function generate(seed,opts,rnd){
  opts=opts||{};rnd=rnd||prng(seed);
  var field=opts.field&&FIELDS.indexOf(opts.field)>=0?opts.field:pick(FIELDS,rnd);
  var ti=(rnd()*TOPICS.length)|0, pi=(rnd()*PRINCIPLES.length)|0, ui=(rnd()*USES.length)|0;
  var tp=TOPICS[ti], pr=PRINCIPLES[pi], use=USES[ui];
  var rank=((ti/2)|0)+1;
  var id=PREFIX+String(seed).padStart(6,'0');
  var eq=pr.e?(' Governing relation: '+pr.e+'.'):'';
  var desc=tp.b+' First principle: '+pr.n+' — '+pr.s+'.'+eq+' In practice: '+use+' Rank '+rank+' of 6 on the teaching ladder.';
  return {
    id:id, t:tp.t, g:field, name:"Operations Research"+': '+tp.t, title:tp.t,
    description:desc, edition: seed%2 ? 'signature' : 'public',
    ladder_rank:rank, field:field,
    principle:{name:pr.n, equation:pr.e, statement:pr.s},
    key_points:[tp.b, pr.n+': '+pr.s, 'Application: '+use, 'Ladder rank '+rank+'/6'],
    src:'generator-sample', sample:true,
    disclaimer:'Generated sample record - not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:'python',language:'python',program:'# JAH Fundamentals of Operations Research demo\n# Record '+id+' — '+tp.t.replace(/\n/g,' ')+'\nprint("record jahdb-fundamental-operations-research-1.0")\nprint("OK: '+id+' generated fundamental record")\n',note:'Generator sample demo.'},
    _seed:seed
  };
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  if(!new RegExp('^'+PREFIX.replace(/-/g,'\\-')+'\\d{6}$').test(r.id||''))e.push('id');
  if(FIELDS.indexOf(r.g)<0&&FIELDS.indexOf(r.field)<0)e.push('field');
  if(!r.src)e.push('src');
  if(!r.demo||!r.demo.program)e.push('demo');
  return {ok:!e.length,errors:e};
}
function driftCheck(record,sample){
  var dups=(sample||[]).filter(function(r){return r&&r.title===record.title&&(r.g===record.g||r.field===record.field);});
  return dups.length?{ok:false,errors:['duplicate topic+field in archive sample']}:{ok:true,errors:[]};
}
var gen={version:"jahdb-fundamental-operations-research-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("fundamental-operations-research",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
