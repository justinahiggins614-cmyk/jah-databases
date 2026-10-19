(function(){'use strict';
/* JAH Climate Data Systems Database generator — jahdb-climate-data-systems-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic synthesis record generation: pick a field, set a seed, get a complete record.
   Same seed + same field = same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-CDS-";
var FIELDS=["observations", "reanalysis", "data formats", "quality control", "services", "applications"];
var TOPICS=[
    {t: "The Observing System", b: "Satellites, Argo floats, buoys, stations, aircraft: the global sensor network watching the planet."},
    {t: "Satellite Missions", b: "Landsat, Sentinel, MODIS, GRACE: the flagship records and what each measures."},
    {t: "In-Situ Networks", b: "Weather stations, ocean moorings, tide gauges: ground truth calibrating the view from space."},
    {t: "Reanalysis", b: "Blending models with observations (ERA5, MERRA): the best-estimate history of the atmosphere."},
    {t: "Data Formats", b: "NetCDF, HDF5, Zarr, cloud-optimized GeoTIFF: the containers and conventions (CF) of climate data."},
    {t: "Quality Control", b: "Range checks, buddy checks, homogenization: the unglamorous pipeline behind trustworthy trends."},
    {t: "Cloud Platforms", b: "Earth Engine, Pangeo, AWS Open Data: petabyte analysis without downloading petabytes."},
    {t: "Climate Services", b: "Downscaled projections, indices, and APIs: delivering science to farmers, engineers, and planners."},
    {t: "Attribution Datasets", b: "The curated records behind 'climate change made this worse' statements."},
    {t: "Data Rescue", b: "Digitizing paper records and recovering old tapes: extending the instrumental record backward."},
    {t: "Uncertainty Communication", b: "Ensembles, error bars, and plain language: honest numbers for high-stakes decisions."},
    {t: "Governance", b: "WMO, GCOS, and data policies: the international agreements keeping observations flowing."}
];
var PRINCIPLES=[
    {n: "Provenance is everything", e: "", s: "A number without its instrument, calibration, and processing history is not data \u2014 it's a rumor."},
    {n: "Homogeneity enables trends", e: "", s: "Merging decades of changing instruments demands homogenization: climate signals hide in the joins."},
    {n: "Open data multiplies value", e: "", s: "Every download by a new user is free science: FAIR principles maximize the public investment."}
];
var USES=["Building climate data pipelines", "Homogenizing station records", "Serving downscaled projections", "Running analysis platforms"];
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
    id:id, t:tp.t, g:field, name:"Climate Data Systems"+': '+tp.t, title:tp.t,
    description:desc, edition: seed%2 ? 'signature' : 'public',
    ladder_rank:rank, field:field,
    principle:{name:pr.n, equation:pr.e, statement:pr.s},
    key_points:[tp.b, pr.n+': '+pr.s, 'Application: '+use, 'Ladder rank '+rank+'/6'],
    src:'generator-sample', sample:true,
    disclaimer:'Generated sample record - not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:'python',language:'python',program:'# JAH Climate Data Synthesis demo\n# Record '+id+' — '+tp.t.replace(/\n/g,' ')+'\nprint("record jahdb-climate-data-systems-1.0")\nprint("OK: '+id+' generated synthesis record")\n',note:'Generator sample demo.'},
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
var gen={version:"jahdb-climate-data-systems-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("climate-data-systems",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
