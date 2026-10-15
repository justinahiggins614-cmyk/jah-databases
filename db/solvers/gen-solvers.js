(function(){'use strict';
/* JAH The Solvers Database generator — jahdb-solvers-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-SLV-";
var FIELDS=["solver"];
var TOPICS={
 "solver": [
  "SAT Solvers \u2014 solver",
  "SMT Solvers \u2014 solver",
  "MaxSAT Solvers \u2014 solver",
  "QBF Solvers \u2014 solver",
  "Constraint Programmers \u2014 solver",
  "Theorem Provers \u2014 solver",
  "Automated Provers \u2014 solver",
  "Proof Checkers \u2014 solver",
  "Model Checkers \u2014 solver",
  "Symbolic Executors \u2014 solver",
  "Computer Algebra Systems \u2014 solver",
  "Linear Programmers \u2014 solver",
  "Mixed-Integer Programmers \u2014 solver",
  "Quadratic Programmers \u2014 solver",
  "Semidefinite Programmers \u2014 solver",
  "Convex Optimizers \u2014 solver",
  "Nonlinear Optimizers \u2014 solver",
  "Global Optimizers \u2014 solver",
  "Combinatorial Optimizers \u2014 solver",
  "Graph Solvers \u2014 solver",
  "Max-Flow Solvers \u2014 solver",
  "Matching Solvers \u2014 solver",
  "Shortest-Path Solvers \u2014 solver",
  "Traveling Salesperson Solvers \u2014 solver",
  "Scheduling Solvers \u2014 solver",
  "Timetabling Solvers \u2014 solver",
  "Bin-Packing Solvers \u2014 solver",
  "Knapsack Solvers \u2014 solver",
  "Prime Sieves \u2014 solver",
  "Primality Testers \u2014 solver",
  "Factorization Engines \u2014 solver",
  "Discrete-Log Solvers \u2014 solver",
  "Lattice Reducers \u2014 solver",
  "Gr\u00f6bner Engines \u2014 solver",
  "Resultant Solvers \u2014 solver",
  "Homotopy Solvers \u2014 solver",
  "Interval Solvers \u2014 solver",
  "Differential Equation Solvers \u2014 solver",
  "Eigenvalue Solvers \u2014 solver",
  "Linear System Solvers \u2014 solver",
  "Sparse Solvers \u2014 solver",
  "FFT Engines \u2014 solver",
  "Number-Theoretic Transforms \u2014 solver",
  "Wavelet Engines \u2014 solver",
  "Optimization Libraries \u2014 solver",
  "Automatic Differentiators \u2014 solver",
  "Root Finders \u2014 solver",
  "Integrators \u2014 solver",
  "Interpolation Engines \u2014 solver",
  "Regression Solvers \u2014 solver",
  "Classification Solvers \u2014 solver",
  "Clustering Solvers \u2014 solver",
  "Dimensionality Reducers \u2014 solver",
  "Density Estimators \u2014 solver",
  "Sampling Engines \u2014 solver",
  "Bayesian Inference Engines \u2014 solver",
  "Probabilistic Programmers \u2014 solver"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Solvers — "+safe+"\n"
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
    name:topic+' — solver record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A solver record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
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
var gen={version:'jahdb-solvers-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('solvers',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
