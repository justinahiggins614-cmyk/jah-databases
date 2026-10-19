(function(){'use strict';
/* JAH Fundamentals of MEMS Database generator — jahdb-fundamental-mems-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic fundamental record generation: pick a field, set a seed, get a complete record.
   Same seed + same field = same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-MEM-";
var FIELDS=["micromachining", "sensors", "actuators", "microfluidics", "packaging", "reliability"];
var TOPICS=[
    {t: "What MEMS Are", b: "Micro-electro-mechanical systems: micron-scale moving structures built with chip-fabrication tools \u2014 accelerometers, gyros, microphones, print heads."},
    {t: "Why the Microscale Is Different", b: "Gravity becomes negligible while surface tension, electrostatics, and viscosity dominate \u2014 intuition from the macro world misleads."},
    {t: "Bulk Micromachining", b: "Etching into silicon wafers with anisotropic KOH/IPA etches carves V-grooves, membranes, and nozzles along crystal planes."},
    {t: "Surface Micromachining", b: "Depositing and selectively removing sacrificial layers builds free-standing beams, gears, and comb drives above the substrate."},
    {t: "Accelerometers", b: "A micro proof-mass on springs: acceleration displaces it, capacitive fingers read the shift \u2014 the sensor in every phone and airbag."},
    {t: "Gyroscopes", b: "Vibrating masses feel Coriolis forces when rotated; drive and sense modes turn rotation into an electrical signal for navigation."},
    {t: "Electrostatic Actuation", b: "Comb drives and parallel plates pull with voltage-squared force \u2014 strong at microns, which is why MEMS mirrors and switches use it."},
    {t: "Piezoelectric MEMS", b: "Piezo films both sense and actuate: inkjet nozzles, ultrasound transducers, and energy harvesters in one material class."},
    {t: "Microfluidics: Lab on a Chip", b: "Laminar flow at microns mixes only by diffusion \u2014 enabling precise droplet, sorting, and diagnostic devices from tiny samples."},
    {t: "Packaging Is Half the Product", b: "MEMS need cavities, getters, and stress isolation: wafer-level packaging protects moving parts while letting the measurand in."},
    {t: "Stiction and Reliability", b: "Capillary and van der Waals forces can glue micro-parts permanently (stiction); coatings, dimples, and hermeticity fight it."},
    {t: "From Prototype to Volume", b: "DRIE, foundry PDKs, and design-for-test turn one-off devices into million-unit products \u2014 manufacturing discipline decides winners."}
];
var PRINCIPLES=[
    {n: "Scaling of forces", e: "surface/volume \u221d 1/L", s: "At microscale, surface forces (electrostatic, capillary) beat body forces (gravity, inertia)."},
    {n: "Cantilever stiffness", e: "k = 3EI/L\u00b3", s: "Micromechanical spring constants follow beam theory down to microns."},
    {n: "Capacitive sensing", e: "\u0394C/C = \u0394x/d", s: "Tiny displacements become measurable signals through capacitance change."}
];
var USES=["Specifying phone inertial sensors", "Designing microfluidic diagnostics", "Building optical MEMS switches", "Qualifying automotive MEMS reliability"];
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
    id:id, t:tp.t, g:field, name:"MEMS"+': '+tp.t, title:tp.t,
    description:desc, edition: seed%2 ? 'signature' : 'public',
    ladder_rank:rank, field:field,
    principle:{name:pr.n, equation:pr.e, statement:pr.s},
    key_points:[tp.b, pr.n+': '+pr.s, 'Application: '+use, 'Ladder rank '+rank+'/6'],
    src:'generator-sample', sample:true,
    disclaimer:'Generated sample record - not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:'python',language:'python',program:'# JAH Fundamentals of MEMS demo\n# Record '+id+' — '+tp.t.replace(/\n/g,' ')+'\nprint("record jahdb-fundamental-mems-1.0")\nprint("OK: '+id+' generated fundamental record")\n',note:'Generator sample demo.'},
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
var gen={version:"jahdb-fundamental-mems-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("fundamental-mems",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
