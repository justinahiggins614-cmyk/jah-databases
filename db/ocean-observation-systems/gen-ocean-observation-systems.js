(function(){'use strict';
/* JAH Ocean Observation Systems Database generator — jahdb-ocean-observation-systems-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic synthesis record generation: pick a field, set a seed, get a complete record.
   Same seed + same field = same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-OOS-";
var FIELDS=["Argo floats", "gliders", "moorings", "satellites", "sensors", "data systems"];
var TOPICS=[
    {t: "Why Observe the Ocean", b: "Weather forecasts, hurricane intensity, fisheries, climate: the societal products of ocean data."},
    {t: "Argo Floats", b: "4,000 autonomous profilers diving to 2,000 m: temperature and salinity profiles revolutionizing oceanography."},
    {t: "Deep Argo", b: "Extending to 6,000 m: measuring the abyssal warming satellites can't see."},
    {t: "Gliders", b: "Buoyancy-driven autonomous vehicles: months-long transects on minimal energy."},
    {t: "Moorings", b: "Fixed-point time series (TAO/TRITON, OOI): the Eulerian anchors of ocean observation."},
    {t: "Satellite Oceanography", b: "Altimetry (sea level), SST, ocean color, scatterometry (winds): the synoptic view from orbit."},
    {t: "Biogeochemical Sensors", b: "Oxygen, nitrate, pH, chlorophyll on floats: the ocean's metabolism, measured autonomously."},
    {t: "Acoustic Tomography", b: "Sound speed mapping temperature: listening to ocean heat content across basins."},
    {t: "Data Systems", b: "Real-time GTS feeds, delayed-mode QC, and open archives: the pipeline from sensor to scientist."},
    {t: "Hurricane Reconnaissance", b: "Aircraft, dropsondes, and floats feeding intensity forecasts: observations saving coastal lives."},
    {t: "Fisheries Acoustics", b: "Echosounders assessing stocks: the surveys behind sustainable quotas."},
    {t: "The Future: Smart Ocean", b: "Cabled observatories, animal-borne sensors, AI QC: the next decade's network."}
];
var PRINCIPLES=[
    {n: "Calibration is the measurement", e: "", s: "Drifting sensors lie: pre/post-deployment calibrations and delayed-mode QC make data trustworthy."},
    {n: "The ocean destroys instruments", e: "", s: "Pressure, corrosion, biofouling: survival engineering precedes science."},
    {n: "Sustained beats heroic", e: "", s: "Decades-long time series (HOT, BATS) reveal what expeditions cannot: commitment outranks cleverness."}
];
var USES=["Deploying Argo floats", "Planning glider missions", "Calibrating ocean sensors", "Assessing hurricane data"];
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
    id:id, t:tp.t, g:field, name:"Ocean Observation Systems"+': '+tp.t, title:tp.t,
    description:desc, edition: seed%2 ? 'signature' : 'public',
    ladder_rank:rank, field:field,
    principle:{name:pr.n, equation:pr.e, statement:pr.s},
    key_points:[tp.b, pr.n+': '+pr.s, 'Application: '+use, 'Ladder rank '+rank+'/6'],
    src:'generator-sample', sample:true,
    disclaimer:'Generated sample record - not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:'python',language:'python',program:'# JAH Ocean Observation Synthesis demo\n# Record '+id+' — '+tp.t.replace(/\n/g,' ')+'\nprint("record jahdb-ocean-observation-systems-1.0")\nprint("OK: '+id+' generated synthesis record")\n',note:'Generator sample demo.'},
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
var gen={version:"jahdb-ocean-observation-systems-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("ocean-observation-systems",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
