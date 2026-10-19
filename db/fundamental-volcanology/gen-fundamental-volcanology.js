(function(){'use strict';
/* JAH Fundamentals of Volcanology Database generator — jahdb-fundamental-volcanology-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic fundamental record generation: pick a field, set a seed, get a complete record.
   Same seed + same field = same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-VOL-";
var FIELDS=["magma", "eruption styles", "volcanic products", "hazards", "monitoring", "risk mitigation"];
var TOPICS=[
    {t: "What Drives Volcanoes", b: "Plate tectonics melts rock at subduction zones, rifts, and hotspots; buoyant magma rises because it is less dense than its surroundings."},
    {t: "Magma Chemistry", b: "Basalt (mafic) flows, andesite builds cones, rhyolite (felsic) explodes \u2014 silica content sets viscosity and thus destiny."},
    {t: "Gas: The Hidden Driver", b: "Dissolved volatiles (H\u2082O, CO\u2082, SO\u2082) exsolve as magma rises; expanding bubbles provide the explosive energy."},
    {t: "Effusive Eruptions", b: "Low-viscosity basalt erupts as lava flows, fountains, and shield volcanoes \u2014 spectacular but usually outrunnable."},
    {t: "Explosive Eruptions", b: "High-viscosity magma fragments into ash and pumice: Plinian columns reach the stratosphere and collapse into pyroclastic flows."},
    {t: "Pyroclastic Flows", b: "Gas-particle avalanches at hundreds of km/h and hundreds of \u00b0C are volcanoes' deadliest product \u2014 unsurvivable in their path."},
    {t: "Lahars: Volcanic Mudflows", b: "Meltwater plus loose ash makes concrete-like slurries that bury valleys tens of kilometers from the volcano."},
    {t: "Volcanic Gases and Climate", b: "SO\u2082 becomes sulfate aerosols that cool the planet: Pinatubo (1991) dropped global temperatures ~0.5\u00b0C for two years."},
    {t: "Monitoring: Seismic", b: "Volcano-tectonic earthquakes track magma movement; harmonic tremor signals sustained fluid motion \u2014 seismology is the primary watch."},
    {t: "Monitoring: Deformation and Gas", b: "GPS/inclinometers catch inflation, and CO\u2082/SO\u2082 ratios sniff rising magma \u2014 combined networks forecast eruptions."},
    {t: "Volcano Alert Levels", b: "Color codes and alert levels translate monitoring into decisions: access closures and evacuations follow protocols, not panic."},
    {t: "Living with Volcanoes", b: "Hazard maps, exclusion zones, and land-use planning let societies farm volcanic soils while respecting eruption return periods."}
];
var PRINCIPLES=[
    {n: "Viscosity control", e: "explosivity \u221d silica content", s: "Rhyolite's polymerized silica traps gas \u2192 explosions; fluid basalt degasses \u2192 lava flows."},
    {n: "VEI scale", e: "VEI = f(erupted volume)", s: "Each Volcanic Explosivity Index step is ~10\u00d7 the erupted volume of the last."},
    {n: "Fragmentation", e: "bubbles > ~70% \u2192 fragmentation", s: "When gas bubbles crowd past critical volume fraction, magma shatters into ash."}
];
var USES=["Forecasting volcanic eruptions", "Mapping lahar hazard zones", "Planning evacuations", "Assessing aviation ash risk"];
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
    id:id, t:tp.t, g:field, name:"Volcanology"+': '+tp.t, title:tp.t,
    description:desc, edition: seed%2 ? 'signature' : 'public',
    ladder_rank:rank, field:field,
    principle:{name:pr.n, equation:pr.e, statement:pr.s},
    key_points:[tp.b, pr.n+': '+pr.s, 'Application: '+use, 'Ladder rank '+rank+'/6'],
    src:'generator-sample', sample:true,
    disclaimer:'Generated sample record - not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:'python',language:'python',program:'# JAH Fundamentals of Volcanology demo\n# Record '+id+' — '+tp.t.replace(/\n/g,' ')+'\nprint("record jahdb-fundamental-volcanology-1.0")\nprint("OK: '+id+' generated fundamental record")\n',note:'Generator sample demo.'},
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
var gen={version:"jahdb-fundamental-volcanology-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("fundamental-volcanology",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
