(function(){'use strict';
/* JAH Fundamentals of Tribology Database generator — jahdb-fundamental-tribology-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic fundamental record generation: pick a field, set a seed, get a complete record.
   Same seed + same field = same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-TRI-";
var FIELDS=["contact mechanics", "friction", "wear mechanisms", "lubrication regimes", "lubricants", "bearings and seals"];
var TOPICS=[
    {t: "What Tribology Covers", b: "Friction, wear, and lubrication together: every moving contact in every machine is a tribological system."},
    {t: "Real vs Apparent Contact Area", b: "Surfaces touch only at asperity tips \u2014 real contact area is orders of magnitude smaller, which is why friction follows load, not area."},
    {t: "Hertzian Contact Stress", b: "Elastic contact theory predicts the pressure distribution under balls and rollers \u2014 the basis of bearing life calculation."},
    {t: "Static vs Kinetic Friction", b: "Breakaway (static) friction exceeds sliding (kinetic): the difference causes stick-slip squeal, chatter, and violin bows."},
    {t: "Adhesive Wear", b: "Asperities cold-weld and tear: adhesive wear transfers material between surfaces and dominates unlubricated metal contact."},
    {t: "Abrasive Wear", b: "Hard particles or asperities plow grooves \u2014 two-body (rough surface) or three-body (loose grit); hardness ratios predict severity."},
    {t: "Fatigue and Fretting", b: "Rolling contacts fail by subsurface fatigue (bearing spalling); tiny oscillating motions cause fretting at bolted joints and splines."},
    {t: "Boundary Lubrication", b: "At monolayer thickness, chemistry rules: friction modifiers and anti-wear additives (ZDDP) form protective tribofilms."},
    {t: "Hydrodynamic Lubrication", b: "A converging wedge drags fluid into a pressure film that fully separates surfaces \u2014 journal bearings ride on this principle."},
    {t: "Elastohydrodynamic (EHL) Films", b: "In gears and rolling bearings, extreme pressure elastically flattens contacts while viscosity spikes \u2014 films thinner than a wavelength still protect."},
    {t: "Lubricant Properties", b: "Viscosity index, pour point, oxidation stability, and additive packages (detergents, dispersants, EP agents) define oil performance."},
    {t: "Seals and Contamination Control", b: "Lip seals, labyrinths, and filtration keep lubricant in and abrasives out \u2014 contamination is the leading cause of premature bearing death."}
];
var PRINCIPLES=[
    {n: "Amontons-Coulomb friction", e: "F = \u03bc * N", s: "Friction force is proportional to normal load and independent of apparent contact area."},
    {n: "Archard wear law", e: "V = K * W * s / H", s: "Wear volume scales with load and sliding distance, inversely with hardness."},
    {n: "Stribeck curve", e: "friction vs \u03b7N/P", s: "Friction bottoms in mixed lubrication and rises in both boundary and hydrodynamic extremes."}
];
var USES=["Selecting engine and gearbox oils", "Sizing rolling-element bearings", "Diagnosing machinery wear debris", "Designing low-friction seals"];
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
    id:id, t:tp.t, g:field, name:"Tribology"+': '+tp.t, title:tp.t,
    description:desc, edition: seed%2 ? 'signature' : 'public',
    ladder_rank:rank, field:field,
    principle:{name:pr.n, equation:pr.e, statement:pr.s},
    key_points:[tp.b, pr.n+': '+pr.s, 'Application: '+use, 'Ladder rank '+rank+'/6'],
    src:'generator-sample', sample:true,
    disclaimer:'Generated sample record - not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:'python',language:'python',program:'# JAH Fundamentals of Tribology demo\n# Record '+id+' — '+tp.t.replace(/\n/g,' ')+'\nprint("record jahdb-fundamental-tribology-1.0")\nprint("OK: '+id+' generated fundamental record")\n',note:'Generator sample demo.'},
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
var gen={version:"jahdb-fundamental-tribology-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("fundamental-tribology",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
