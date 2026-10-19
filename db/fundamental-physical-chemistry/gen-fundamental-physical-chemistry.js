(function(){'use strict';
/* JAH Fundamentals of Physical Chemistry Database generator — jahdb-fundamental-physical-chemistry-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic fundamental record generation: pick a field, set a seed, get a complete record.
   Same seed + same field = same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-PC-";
var FIELDS=["chemical thermodynamics", "kinetics", "quantum chemistry", "statistical mechanics", "electrochemistry", "spectroscopy"];
var TOPICS=[
    {t: "Chemical Thermodynamics", b: "Enthalpy, entropy, and Gibbs energy predict whether reactions go and how far \u2014 \u0394G\u00b0 = \u2212RT ln K ties energy to equilibrium."},
    {t: "Equilibrium Constants", b: "K expresses the balance point of a reaction; Le Chatelier's principle is just the system restoring K after disturbance."},
    {t: "Reaction Kinetics", b: "Rate laws come from experiment, mechanisms from rate laws: the slow step's molecularity is written in the exponents."},
    {t: "Activation Energy", b: "The Arrhenius barrier explains why rates double-ish per 10\u00b0C and why catalysts (lowering Ea) are so powerful."},
    {t: "Catalysis", b: "Catalysts provide lower-energy pathways without being consumed: enzymes do it with exquisite specificity at room temperature."},
    {t: "Quantum Chemistry Basics", b: "Schr\u00f6dinger's equation gives orbitals their shapes and energies; bonding is just electrons minimizing total energy."},
    {t: "Molecular Orbital Theory", b: "Atomic orbitals combine into bonding and antibonding MOs; bond order (bonding \u2212 antibonding)/2 predicts strength and magnetism."},
    {t: "Statistical Mechanics Bridge", b: "The Boltzmann distribution over molecular states yields all macroscopic thermodynamics \u2014 the deepest 'why' in chemistry."},
    {t: "Electrochemistry", b: "Redox half-reactions plus the Nernst equation describe batteries, corrosion, and electroplating quantitatively."},
    {t: "Transport Phenomena", b: "Diffusion (Fick's laws), viscosity, and conductivity move matter, momentum, and charge \u2014 kinetics of the bulk."},
    {t: "Photochemistry", b: "Absorbed photons are reagents: excited states react by different rules, enabling photosynthesis and photolithography."},
    {t: "Surface Chemistry", b: "Adsorption isotherms (Langmuir) describe molecules on surfaces \u2014 the basis of heterogeneous catalysis and chromatography."}
];
var PRINCIPLES=[
    {n: "Gibbs free energy", e: "\u0394G = \u0394H \u2212 T\u0394S", s: "Spontaneity and equilibrium both follow from minimizing Gibbs energy at constant T and P."},
    {n: "Arrhenius equation", e: "k = A\u00b7e^(\u2212Ea/RT)", s: "Reaction rates grow exponentially as temperature climbs past the activation barrier."},
    {n: "Nernst equation", e: "E = E\u00b0 \u2212 (RT/nF)\u00b7ln Q", s: "Electrode potential shifts with concentration \u2014 the quantitative law of batteries."}
];
var USES=["Predicting reaction feasibility", "Designing catalysts", "Engineering battery cells", "Modeling atmospheric chemistry"];
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
    id:id, t:tp.t, g:field, name:"Physical Chemistry"+': '+tp.t, title:tp.t,
    description:desc, edition: seed%2 ? 'signature' : 'public',
    ladder_rank:rank, field:field,
    principle:{name:pr.n, equation:pr.e, statement:pr.s},
    key_points:[tp.b, pr.n+': '+pr.s, 'Application: '+use, 'Ladder rank '+rank+'/6'],
    src:'generator-sample', sample:true,
    disclaimer:'Generated sample record - not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:'python',language:'python',program:'# JAH Fundamentals of Physical Chemistry demo\n# Record '+id+' — '+tp.t.replace(/\n/g,' ')+'\nprint("record jahdb-fundamental-physical-chemistry-1.0")\nprint("OK: '+id+' generated fundamental record")\n',note:'Generator sample demo.'},
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
var gen={version:"jahdb-fundamental-physical-chemistry-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("fundamental-physical-chemistry",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
