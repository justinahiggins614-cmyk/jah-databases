(function(){'use strict';
/* JAH Fundamentals of Metamaterials Database generator — jahdb-fundamental-metamaterials-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic fundamental record generation: pick a field, set a seed, get a complete record.
   Same seed + same field = same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-MET-";
var FIELDS=["effective media", "negative index", "cloaking", "acoustic metamaterials", "programmable matter", "fabrication"];
var TOPICS=[
    {t: "Properties from Structure, Not Chemistry", b: "Metamaterials get their behavior from engineered sub-wavelength architecture \u2014 the same metal becomes a new material by shaping."},
    {t: "Effective Medium Theory", b: "When unit cells are much smaller than the wavelength, waves respond to averaged permittivity and permeability, not the fine detail."},
    {t: "Split-Ring Resonators", b: "Tiny broken loops act as magnetic atoms, giving a magnetic response at frequencies where nature provides none."},
    {t: "Negative Refractive Index", b: "With \u03b5 and \u03bc both negative, phase velocity opposes energy flow: reversed Doppler, reversed Cherenkov, flat-lens focusing."},
    {t: "The Perfect Lens Idea", b: "A negative-index slab amplifies evanescent waves, promising imaging beyond the diffraction limit \u2014 loss is the practical limit."},
    {t: "Cloaking by Transformation Optics", b: "Compressing space mathematically and realizing the map in materials bends waves smoothly around a hidden region."},
    {t: "Acoustic and Elastic Metamaterials", b: "The same ideas work for sound and vibration: negative-density and negative-modulus structures block or steer mechanical waves."},
    {t: "Seismic and Vibration Shields", b: "Buried resonator arrays can divert earthquake surface waves around buildings \u2014 civil-scale metamaterials in field trials."},
    {t: "Programmable and Tunable Media", b: "Varactors, MEMS, and phase-change inclusions make unit cells switchable: one hardware, many wave behaviors on command."},
    {t: "Topological Wave Physics", b: "Topologically protected edge states guide waves around defects without backscattering \u2014 robustness by mathematics."},
    {t: "Fabrication Across Scales", b: "Printed circuit boards for microwaves, nanolithography for optics, 3-D printing for acoustics \u2014 each band has its factory."},
    {t: "Limits: Loss, Bandwidth, Scale", b: "Resonant metamaterials are narrowband and lossy; the field's progress is measured in widening bands and taming absorption."}
];
var PRINCIPLES=[
    {n: "Effective medium", e: "\u03bb >> unit cell", s: "When structures are far smaller than the wavelength, waves see averaged properties."},
    {n: "Negative index condition", e: "\u03b5 < 0 and \u03bc < 0 simultaneously", s: "Doubly-negative media refract light backward, reversing Snell's law."},
    {n: "Transformation optics", e: "\u03b5\u2032, \u03bc\u2032 from coordinate maps", s: "Warping coordinates designs the material that warps waves \u2014 the math of cloaking."}
];
var USES=["Designing flat lenses and beam steerers", "Building vibration-isolation structures", "Prototyping RF cloaking shells", "Engineering acoustic barriers"];
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
    id:id, t:tp.t, g:field, name:"Metamaterials"+': '+tp.t, title:tp.t,
    description:desc, edition: seed%2 ? 'signature' : 'public',
    ladder_rank:rank, field:field,
    principle:{name:pr.n, equation:pr.e, statement:pr.s},
    key_points:[tp.b, pr.n+': '+pr.s, 'Application: '+use, 'Ladder rank '+rank+'/6'],
    src:'generator-sample', sample:true,
    disclaimer:'Generated sample record - not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:'python',language:'python',program:'# JAH Fundamentals of Metamaterials demo\n# Record '+id+' — '+tp.t.replace(/\n/g,' ')+'\nprint("record jahdb-fundamental-metamaterials-1.0")\nprint("OK: '+id+' generated fundamental record")\n',note:'Generator sample demo.'},
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
var gen={version:"jahdb-fundamental-metamaterials-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("fundamental-metamaterials",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
