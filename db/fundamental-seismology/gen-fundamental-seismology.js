(function(){'use strict';
/* JAH Fundamentals of Seismology Database generator — jahdb-fundamental-seismology-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic fundamental record generation: pick a field, set a seed, get a complete record.
   Same seed + same field = same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-SEI-";
var FIELDS=["seismic waves", "faults", "magnitude", "location", "hazard", "engineering seismology"];
var TOPICS=[
    {t: "What Causes Earthquakes", b: "Faults stick, strain accumulates from plate motion, then sudden slip releases it as seismic waves \u2014 elastic rebound theory."},
    {t: "P, S, and Surface Waves", b: "P waves compress, S waves shear, Love and Rayleigh waves roll the surface: arrival order and motion reveal the source."},
    {t: "Fault Types", b: "Normal (extension), reverse (compression), and strike-slip (lateral) faults match the tectonic stress squeezing or stretching the crust."},
    {t: "Locating Earthquakes", b: "P-minus-S times at three+ stations triangulate the hypocenter; depth separates crustal from subduction quakes."},
    {t: "Magnitude Scales", b: "Richter (local) saturated, so moment magnitude (Mw) now measures true energy: each unit is ~32\u00d7 the energy."},
    {t: "Intensity: What People Feel", b: "Modified Mercalli intensity maps shaking effects (I\u2013XII) \u2014 magnitude is one number, intensity is the felt map."},
    {t: "The Seismic Moment", b: "Rigidity \u00d7 rupture area \u00d7 slip: the physical size of the quake, from which Mw is computed."},
    {t: "Aftershocks and Omori's Law", b: "Aftershock rate decays roughly as 1/time \u2014 the statistical clock ticking after every mainshock."},
    {t: "Seismic Hazard Maps", b: "Combining fault slip rates, Gutenberg-Richter statistics, and ground-motion models yields the shaking probabilities engineers design to."},
    {t: "Site Effects", b: "Soft soils amplify shaking (Mexico City 1985): local geology can matter more than distance or magnitude."},
    {t: "Tsunami Generation", b: "Seafloor vertical displacement from megathrust quakes displaces the ocean \u2014 wave speed \u221a(g\u00b7depth) gives warning time."},
    {t: "Earthquake Early Warning", b: "P waves outrun destructive S waves by seconds: sensor networks (ShakeAlert) buy precious seconds for automated shutdowns."}
];
var PRINCIPLES=[
    {n: "P vs S waves", e: "Vp \u2248 1.7 \u00d7 Vs", s: "Compressional waves outrun shear waves \u2014 the time gap locates the quake."},
    {n: "Moment magnitude", e: "Mw = \u2154\u00b7log10(M0) \u2212 10.7", s: "Seismic moment (rigidity \u00d7 area \u00d7 slip) gives the true energy scale."},
    {n: "Gutenberg-Richter", e: "log N = a \u2212 b\u00b7M (b \u2248 1)", s: "Each magnitude unit has ~10\u00d7 fewer quakes \u2014 the statistical law of seismicity."}
];
var USES=["Designing earthquake-resistant buildings", "Mapping seismic hazard zones", "Operating early-warning systems", "Assessing tsunami risk"];
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
    id:id, t:tp.t, g:field, name:"Seismology"+': '+tp.t, title:tp.t,
    description:desc, edition: seed%2 ? 'signature' : 'public',
    ladder_rank:rank, field:field,
    principle:{name:pr.n, equation:pr.e, statement:pr.s},
    key_points:[tp.b, pr.n+': '+pr.s, 'Application: '+use, 'Ladder rank '+rank+'/6'],
    src:'generator-sample', sample:true,
    disclaimer:'Generated sample record - not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:'python',language:'python',program:'# JAH Fundamentals of Seismology demo\n# Record '+id+' — '+tp.t.replace(/\n/g,' ')+'\nprint("record jahdb-fundamental-seismology-1.0")\nprint("OK: '+id+' generated fundamental record")\n',note:'Generator sample demo.'},
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
var gen={version:"jahdb-fundamental-seismology-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("fundamental-seismology",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
