(function(){'use strict';
/* JAH Fundamentals of Statistical Mechanics Database generator — jahdb-fundamental-statistical-mechanics-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic fundamental record generation: pick a field, set a seed, get a complete record.
   Same seed + same field = same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-SM-";
var FIELDS=["probability", "ensembles", "Boltzmann distribution", "partition functions", "quantum statistics", "phase transitions"];
var TOPICS=[
    {t: "Why Statistics for Physics", b: "10\u00b2\u00b3 particles can't be tracked; probability distributions over microstates predict exactly what thermometers measure."},
    {t: "Microstates and Macrostates", b: "A macrostate (T, P, V) hides astronomically many microstates; counting them is the whole game."},
    {t: "The Fundamental Postulate", b: "Isolated systems visit all accessible microstates equally \u2014 from this one assumption, everything follows."},
    {t: "Boltzmann Distribution", b: "In contact with a heat bath, probability \u221d e^(\u2212E/kT): the exponential that rules chemistry, semiconductors, and stars."},
    {t: "Partition Functions", b: "Z sums the Boltzmann weights; every thermodynamic quantity is a derivative of ln Z \u2014 the computational engine."},
    {t: "Entropy as Counting", b: "S = k ln W makes the second law obvious: systems evolve toward the most numerous microstates."},
    {t: "Ideal Gas from Scratch", b: "Deriving PV = nRT and heat capacities from molecular partition functions \u2014 thermodynamics' laws as theorems."},
    {t: "Quantum Statistics", b: "Bosons (Bose-Einstein) bunch, fermions (Fermi-Dirac) exclude: low-temperature quantum gases obey different counting."},
    {t: "Fermi-Dirac and Metals", b: "Electrons fill states to the Fermi energy: electrical conduction, heat capacity, and white dwarfs follow."},
    {t: "Bose-Einstein Condensation", b: "Bosons collapsing into one quantum state at nanokelvin temperatures \u2014 a new state of matter made in 1995."},
    {t: "Phase Transitions", b: "Singularities in free energy mark boiling, magnetizing, superconducting: universality classes group wildly different systems."},
    {t: "Fluctuations and Response", b: "Fluctuation-dissipation theorems tie microscopic jitter to macroscopic response \u2014 noise as a measurement tool."}
];
var PRINCIPLES=[
    {n: "Boltzmann distribution", e: "P_i \u221d e^(\u2212E_i/kT)", s: "State probability falls exponentially with energy over temperature \u2014 the master law."},
    {n: "Entropy (statistical)", e: "S = k\u00b7ln W", s: "Entropy counts microstates: the bridge between atoms and thermodynamics."},
    {n: "Partition function", e: "Z = \u03a3 e^(\u2212E_i/kT)", s: "One sum generates all thermodynamics: energy, entropy, pressure from derivatives of ln Z."}
];
var USES=["Predicting material heat capacities", "Modeling semiconductor carrier statistics", "Understanding critical phenomena", "Designing cryogenic systems"];
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
    id:id, t:tp.t, g:field, name:"Statistical Mechanics"+': '+tp.t, title:tp.t,
    description:desc, edition: seed%2 ? 'signature' : 'public',
    ladder_rank:rank, field:field,
    principle:{name:pr.n, equation:pr.e, statement:pr.s},
    key_points:[tp.b, pr.n+': '+pr.s, 'Application: '+use, 'Ladder rank '+rank+'/6'],
    src:'generator-sample', sample:true,
    disclaimer:'Generated sample record - not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:'python',language:'python',program:'# JAH Fundamentals of Statistical Mechanics demo\n# Record '+id+' — '+tp.t.replace(/\n/g,' ')+'\nprint("record jahdb-fundamental-statistical-mechanics-1.0")\nprint("OK: '+id+' generated fundamental record")\n',note:'Generator sample demo.'},
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
var gen={version:"jahdb-fundamental-statistical-mechanics-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("fundamental-statistical-mechanics",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
