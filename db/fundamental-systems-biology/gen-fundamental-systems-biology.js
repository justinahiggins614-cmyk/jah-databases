(function(){'use strict';
/* JAH Fundamentals of Systems Biology Database generator — jahdb-fundamental-systems-biology-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic fundamental record generation: pick a field, set a seed, get a complete record.
   Same seed + same field = same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-SB2-";
var FIELDS=["networks and pathways", "feedback and motifs", "omics data", "kinetic modeling", "flux analysis", "multiscale models"];
var TOPICS=[
    {t: "From Parts Lists to Systems", b: "Genomes list components; systems biology maps how they interact as networks \u2014 function emerges from wiring, not just parts."},
    {t: "Network Motifs", b: "Feed-forward loops, feedback loops, and autoregulation recur in gene networks because each motif computes a useful dynamical function."},
    {t: "Feedback: Stability and Switching", b: "Negative feedback stabilizes and speeds responses; positive feedback creates switches and memory \u2014 topology determines behavior."},
    {t: "Omics: Measuring Everything", b: "Genomics, transcriptomics, proteomics, and metabolomics snapshot whole molecular layers; integration across layers reveals regulation."},
    {t: "Kinetic Models (ODEs)", b: "Ordinary differential equations turn reaction diagrams into time courses \u2014 the workhorse for signaling and metabolic dynamics."},
    {t: "Parameter Estimation", b: "Rate constants come from experiments with noise; fitting, identifiability, and sensitivity analysis separate solid models from fantasy."},
    {t: "Flux Balance Analysis", b: "Assuming steady state, linear programming finds feasible metabolic flux distributions \u2014 predicting microbial growth without kinetic parameters."},
    {t: "Stochastic Gene Expression", b: "Low molecule counts make gene expression noisy; the chemical master equation and Gillespie simulation capture the randomness."},
    {t: "Robustness and Evolvability", b: "Biological networks tolerate mutations and noise yet remain evolvable \u2014 design principles engineers now copy."},
    {t: "Signaling Pathways", b: "MAPK cascades and similar modules transmit, amplify, and adapt signals; ultrasensitivity and adaptation are engineered into the wiring."},
    {t: "From Cell to Tissue Models", b: "Agent-based and continuum models scale single-cell rules to tissues, tumors, and developing embryos."},
    {t: "Model Validation Cycle", b: "Predict, perturb, measure, revise: models earn trust only by surviving experiments designed to break them."}
];
var PRINCIPLES=[
    {n: "Mass-action kinetics", e: "rate = k\u00b7[A]\u00b7[B]", s: "Reaction speed scales with reactant concentrations \u2014 the basis of every pathway model."},
    {n: "Michaelis-Menten", e: "v = Vmax\u00b7[S]/(Km + [S])", s: "Enzyme rate saturates with substrate; Km marks the half-maximum point."},
    {n: "Flux balance", e: "S\u00b7v = 0 (steady state)", s: "At steady state, metabolite production equals consumption across the network."}
];
var USES=["Modeling drug-target pathways", "Predicting microbial fermentation yields", "Analyzing cancer signaling networks", "Designing robust synthetic circuits"];
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
    id:id, t:tp.t, g:field, name:"Systems Biology"+': '+tp.t, title:tp.t,
    description:desc, edition: seed%2 ? 'signature' : 'public',
    ladder_rank:rank, field:field,
    principle:{name:pr.n, equation:pr.e, statement:pr.s},
    key_points:[tp.b, pr.n+': '+pr.s, 'Application: '+use, 'Ladder rank '+rank+'/6'],
    src:'generator-sample', sample:true,
    disclaimer:'Generated sample record - not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:'python',language:'python',program:'# JAH Fundamentals of Systems Biology demo\n# Record '+id+' — '+tp.t.replace(/\n/g,' ')+'\nprint("record jahdb-fundamental-systems-biology-1.0")\nprint("OK: '+id+' generated fundamental record")\n',note:'Generator sample demo.'},
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
var gen={version:"jahdb-fundamental-systems-biology-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("fundamental-systems-biology",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
