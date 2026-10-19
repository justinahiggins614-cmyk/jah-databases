(function(){'use strict';
/* JAH Fundamentals of Particle Physics Database generator — jahdb-fundamental-particle-physics-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic fundamental record generation: pick a field, set a seed, get a complete record.
   Same seed + same field = same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-PP-";
var FIELDS=["the Standard Model", "quarks", "leptons", "gauge bosons", "the Higgs", "beyond the Standard Model"];
var TOPICS=[
    {t: "The Particle Zoo, Organized", b: "Quarks and leptons (matter), gauge bosons (forces), the Higgs: the Standard Model's complete cast of characters."},
    {t: "Quarks", b: "Six flavors in three generations; never seen alone (confinement) \u2014 protons and neutrons are uud and udd triplets."},
    {t: "Leptons", b: "Electrons, muons, taus plus their neutrinos: pointlike, generation-structured, and the neutrino's shape-shifting mystery."},
    {t: "The Four Forces", b: "Strong (gluons), electromagnetic (photons), weak (W/Z), gravity (outside the model): strengths spanning 40 orders of magnitude."},
    {t: "Gauge Theory Idea", b: "Demanding local symmetry forces the existence of force carriers \u2014 the deep principle generating three of four forces."},
    {t: "The Higgs Mechanism", b: "The Higgs field's nonzero vacuum value gives particles mass; its boson (2012) completed the Standard Model."},
    {t: "Antimatter", b: "Every particle has an opposite: Dirac's equation demanded it, Anderson found the positron \u2014 annihilation converts mass fully to energy."},
    {t: "Symmetries and Conservation", b: "Charge, baryon number, lepton number conserved (mostly); CP violation's tiny crack explains why matter survived the Big Bang."},
    {t: "How Colliders Work", b: "Accelerate, collide, detect: LHC's 13.6 TeV collisions recreate Big Bang energies in microscopic fireballs."},
    {t: "Detectors", b: "Tracking (momentum), calorimetry (energy), muon chambers: layered instruments reconstructing collisions from debris."},
    {t: "Neutrino Physics", b: "Ghost particles changing flavor in flight: oscillations proved they have mass \u2014 physics beyond the Standard Model, confirmed."},
    {t: "Open Questions", b: "Dark matter, matter-antimatter asymmetry, hierarchy problem, quantum gravity: the Standard Model is complete and clearly incomplete."}
];
var PRINCIPLES=[
    {n: "E\u00b2 = (pc)\u00b2 + (mc\u00b2)\u00b2", e: "relativistic energy", s: "The energy-momentum relation every particle obeys \u2014 mass is rest energy."},
    {n: "Heisenberg (energy-time)", e: "\u0394E\u00b7\u0394t \u2265 \u210f/2", s: "Short-lived virtual particles borrow energy \u2014 the quantum foam behind forces."},
    {n: "Running couplings", e: "\u03b1_s falls with energy", s: "The strong force weakens at high energy (asymptotic freedom) \u2014 the 2004 Nobel insight."}
];
var USES=["Designing particle detectors", "Interpreting collider data", "Modeling early-universe physics", "Developing medical particle beams"];
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
    id:id, t:tp.t, g:field, name:"Particle Physics"+': '+tp.t, title:tp.t,
    description:desc, edition: seed%2 ? 'signature' : 'public',
    ladder_rank:rank, field:field,
    principle:{name:pr.n, equation:pr.e, statement:pr.s},
    key_points:[tp.b, pr.n+': '+pr.s, 'Application: '+use, 'Ladder rank '+rank+'/6'],
    src:'generator-sample', sample:true,
    disclaimer:'Generated sample record - not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:'python',language:'python',program:'# JAH Fundamentals of Particle Physics demo\n# Record '+id+' — '+tp.t.replace(/\n/g,' ')+'\nprint("record jahdb-fundamental-particle-physics-1.0")\nprint("OK: '+id+' generated fundamental record")\n',note:'Generator sample demo.'},
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
var gen={version:"jahdb-fundamental-particle-physics-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("fundamental-particle-physics",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
