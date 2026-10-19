(function(){'use strict';
/* JAH Fundamentals of Nuclear Physics Database generator — jahdb-fundamental-nuclear-physics-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic fundamental record generation: pick a field, set a seed, get a complete record.
   Same seed + same field = same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-NP-";
var FIELDS=["nuclear structure", "binding energy", "radioactivity", "fission", "fusion", "applications"];
var TOPICS=[
    {t: "The Nucleus", b: "Protons and neutrons bound by the strong force into femtometer-scale cores holding 99.9% of atomic mass."},
    {t: "Binding Energy Curve", b: "Binding per nucleon peaks at iron-56: fusing lighter or splitting heavier nuclei releases energy \u2014 the whole map of nuclear power."},
    {t: "Nuclear Models", b: "Liquid-drop (collective) and shell model (quantized orbits, magic numbers) each capture part of nuclear structure."},
    {t: "Radioactive Decay Modes", b: "Alpha (helium nuclei), beta (weak-force transmutation), gamma (electromagnetic de-excitation): three exits for unstable nuclei."},
    {t: "Half-Lives", b: "From microseconds to billions of years: the decay constant \u03bb is each isotope's unchangeable fingerprint."},
    {t: "Decay Chains", b: "Uranium-238 cascades through 14 steps to lead-206: secular equilibrium makes daughters track parents' activity."},
    {t: "Fission", b: "Neutron-induced splitting of U-235 releases ~200 MeV plus more neutrons: chain reactions, criticality, and reactors follow."},
    {t: "Fusion in Stars", b: "Proton-proton chains and CNO cycles fuse hydrogen to helium: E = mc\u00b2 written across the sky, element by element."},
    {t: "Nucleosynthesis", b: "Big Bang (H, He), stars (C through Fe), supernovae (beyond Fe): every heavy atom in your body was forged in stellar death."},
    {t: "Radiation and Matter", b: "Alpha stopped by paper, beta by aluminum, gamma by lead: interaction physics dictates shielding and detection."},
    {t: "Nuclear Reactors", b: "Moderation, control rods, and coolant loops tame the chain reaction: PWRs, BWRs, and next-generation designs."},
    {t: "Uses of Isotopes", b: "Medical imaging (Tc-99m), cancer therapy, radiocarbon dating, smoke detectors: the peaceful nucleus at work."}
];
var PRINCIPLES=[
    {n: "Mass-energy binding", e: "E_b = \u0394m\u00b7c\u00b2", s: "The missing mass of a nucleus is its binding energy \u2014 the ledger of nuclear power."},
    {n: "Decay law", e: "N = N\u2080\u00b7e^(\u2212\u03bbt)", s: "Radioactive decay is exponential with a fixed half-life \u2014 statistics of huge numbers."},
    {n: "Q-value", e: "Q = (m_initial \u2212 m_final)\u00b7c\u00b2", s: "Positive Q means energy released: the accountant's rule for every nuclear reaction."}
];
var USES=["Designing reactor cores", "Dating archaeological samples", "Producing medical isotopes", "Shielding radiation facilities"];
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
    id:id, t:tp.t, g:field, name:"Nuclear Physics"+': '+tp.t, title:tp.t,
    description:desc, edition: seed%2 ? 'signature' : 'public',
    ladder_rank:rank, field:field,
    principle:{name:pr.n, equation:pr.e, statement:pr.s},
    key_points:[tp.b, pr.n+': '+pr.s, 'Application: '+use, 'Ladder rank '+rank+'/6'],
    src:'generator-sample', sample:true,
    disclaimer:'Generated sample record - not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:'python',language:'python',program:'# JAH Fundamentals of Nuclear Physics demo\n# Record '+id+' — '+tp.t.replace(/\n/g,' ')+'\nprint("record jahdb-fundamental-nuclear-physics-1.0")\nprint("OK: '+id+' generated fundamental record")\n',note:'Generator sample demo.'},
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
var gen={version:"jahdb-fundamental-nuclear-physics-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("fundamental-nuclear-physics",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
