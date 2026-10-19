(function(){'use strict';
/* JAH Fundamentals of Powder Metallurgy Database generator — jahdb-fundamental-powder-metallurgy-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic fundamental record generation: pick a field, set a seed, get a complete record.
   Same seed + same field = same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-PM-";
var FIELDS=["powder production", "powder characterization", "compaction", "sintering", "secondary operations", "design for PM"];
var TOPICS=[
    {t: "Why Make Parts from Powder", b: "Near-net-shape production with almost no waste, alloys impossible to cast, and controlled porosity \u2014 gears, filters, and magnets."},
    {t: "Atomization: Making Powder", b: "Gas or water jets shatter molten metal into droplets; gas gives spherical powder (additive-ready), water gives irregular (press-ready)."},
    {t: "Other Powder Routes", b: "Oxide reduction, electrolysis, and carbonyl decomposition each produce signature particle shapes, purities, and costs."},
    {t: "Powder Characterization", b: "Apparent density, flow rate (Hall), particle size distribution, and compressibility predict how powder will press and sinter."},
    {t: "Mixing and Lubrication", b: "Admixed graphite, nickel, and wax lubricants homogenize composition and ease ejection \u2014 segregation during handling is the enemy."},
    {t: "Compaction Pressing", b: "Rigid dies press powder to 'green' compacts at 400\u2013800 MPa; density gradients from die-wall friction are the core defect source."},
    {t: "Metal Injection Molding", b: "MIM mixes fine powder with binder, injection-molds complex shapes like plastic, then debinds and sinters to near-full density."},
    {t: "Sintering Atmospheres", b: "Endothermic gas, hydrogen, or vacuum atmospheres prevent oxidation during firing \u2014 atmosphere choice is chemistry, not plumbing."},
    {t: "Liquid-Phase Sintering", b: "A small melt fraction (as in tungsten heavy alloys and cemented carbides) accelerates densification dramatically via capillary forces."},
    {t: "Sizing, Infiltration, Heat Treat", b: "Coining hits final tolerances, copper infiltration seals porosity, and sinter-hardening or quench-and-temper builds strength."},
    {t: "Porosity as a Feature", b: "Controlled pores make self-lubricating bearings (oil-impregnated bronze) and filters \u2014 PM's unique selling point."},
    {t: "Design Rules for PM", b: "Uniform wall thickness, generous radii, no undercuts, and draft angles: design with pressing and ejection in mind from the start."}
];
var PRINCIPLES=[
    {n: "Green density vs pressure", e: "density rises steeply, then asymptotically", s: "Compaction pressure densifies powder rapidly at first, then fights work hardening."},
    {n: "Sintering necks", e: "x/r \u221d t^n", s: "Neck growth between particles follows time-power laws set by the diffusion mechanism."},
    {n: "Compressibility", e: "final density = f(pressure, powder)", s: "Harder, irregular powders need more pressure for the same green density."}
];
var USES=["Producing automotive transmission gears", "Making porous bronze bearings", "Manufacturing cemented-carbide tools", "Forming complex MIM medical parts"];
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
    id:id, t:tp.t, g:field, name:"Powder Metallurgy"+': '+tp.t, title:tp.t,
    description:desc, edition: seed%2 ? 'signature' : 'public',
    ladder_rank:rank, field:field,
    principle:{name:pr.n, equation:pr.e, statement:pr.s},
    key_points:[tp.b, pr.n+': '+pr.s, 'Application: '+use, 'Ladder rank '+rank+'/6'],
    src:'generator-sample', sample:true,
    disclaimer:'Generated sample record - not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:'python',language:'python',program:'# JAH Fundamentals of Powder Metallurgy demo\n# Record '+id+' — '+tp.t.replace(/\n/g,' ')+'\nprint("record jahdb-fundamental-powder-metallurgy-1.0")\nprint("OK: '+id+' generated fundamental record")\n',note:'Generator sample demo.'},
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
var gen={version:"jahdb-fundamental-powder-metallurgy-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("fundamental-powder-metallurgy",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
