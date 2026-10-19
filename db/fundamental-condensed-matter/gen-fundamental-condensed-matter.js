(function(){'use strict';
/* JAH Fundamentals of Condensed Matter Database generator — jahdb-fundamental-condensed-matter-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic fundamental record generation: pick a field, set a seed, get a complete record.
   Same seed + same field = same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-CM3-";
var FIELDS=["crystal structure", "band theory", "phonons", "magnetism", "superconductivity", "soft matter"];
var TOPICS=[
    {t: "Why Solids Hold Together", b: "Ionic, covalent, metallic, van der Waals bonding in competition: bond type predicts nearly every solid property."},
    {t: "Crystal Lattices", b: "Bravais lattices plus bases describe all crystals; Miller indices name the planes X-rays see."},
    {t: "Reciprocal Space", b: "Diffraction patterns live in reciprocal space: the Fourier transform of the lattice is what experiments actually measure."},
    {t: "Band Theory", b: "Periodic potentials split electron energies into allowed bands and forbidden gaps \u2014 the quantum origin of conductors vs insulators."},
    {t: "Semiconductors", b: "Doping moves the Fermi level: p-n junctions, the basis of all electronics, are applied band theory."},
    {t: "Phonons: Quantized Sound", b: "Lattice vibrations carry heat and scatter electrons; Debye and Einstein models predict heat capacities."},
    {t: "Magnetism", b: "Exchange interaction aligns spins: ferromagnets, antiferromagnets, and the Curie temperature where order melts."},
    {t: "Superconductivity", b: "Cooper pairs condense into a quantum fluid with zero resistance and perfect diamagnetism \u2014 BCS theory's triumph."},
    {t: "Superfluidity", b: "Helium-4 flows without viscosity below 2.17 K: macroscopic quantum mechanics you can pour."},
    {t: "Topological Phases", b: "Quantum Hall states and topological insulators conduct on edges but not bulk \u2014 protected by mathematics, not perfection."},
    {t: "Soft Matter", b: "Polymers, colloids, liquid crystals: entropy-dominated materials where fluctuations, not bonds, rule."},
    {t: "Experimental Probes", b: "X-ray/neutron diffraction, ARPES, STM, transport: how we interrogate quantum materials."}
];
var PRINCIPLES=[
    {n: "Bloch's theorem", e: "\u03c8_k(r) = e^{ik\u00b7r}\u00b7u_k(r)", s: "Electrons in crystals are plane waves modulated by the lattice periodicity."},
    {n: "BCS gap", e: "\u0394 \u2248 1.76\u00b7k_B\u00b7T_c", s: "Superconducting energy gap scales with critical temperature \u2014 the signature of Cooper pairing."},
    {n: "Curie-Weiss law", e: "\u03c7 = C/(T \u2212 \u03b8)", s: "Magnetic susceptibility diverges near ordering temperature \u2014 the fingerprint of cooperative magnetism."}
];
var USES=["Engineering semiconductor devices", "Developing superconducting magnets", "Designing magnetic storage", "Creating novel quantum materials"];
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
    id:id, t:tp.t, g:field, name:"Condensed Matter"+': '+tp.t, title:tp.t,
    description:desc, edition: seed%2 ? 'signature' : 'public',
    ladder_rank:rank, field:field,
    principle:{name:pr.n, equation:pr.e, statement:pr.s},
    key_points:[tp.b, pr.n+': '+pr.s, 'Application: '+use, 'Ladder rank '+rank+'/6'],
    src:'generator-sample', sample:true,
    disclaimer:'Generated sample record - not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:'python',language:'python',program:'# JAH Fundamentals of Condensed Matter demo\n# Record '+id+' — '+tp.t.replace(/\n/g,' ')+'\nprint("record jahdb-fundamental-condensed-matter-1.0")\nprint("OK: '+id+' generated fundamental record")\n',note:'Generator sample demo.'},
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
var gen={version:"jahdb-fundamental-condensed-matter-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("fundamental-condensed-matter",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
