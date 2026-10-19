(function(){'use strict';
/* JAH Fundamentals of Hydrology Database generator — jahdb-fundamental-hydrology-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic fundamental record generation: pick a field, set a seed, get a complete record.
   Same seed + same field = same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-HYD-";
var FIELDS=["the water cycle", "precipitation", "runoff", "groundwater", "floods", "water resources"];
var TOPICS=[
    {t: "The Hydrologic Cycle", b: "Evaporation, condensation, precipitation, runoff, infiltration: water circulates endlessly, driven by solar energy and gravity."},
    {t: "Precipitation Measurement", b: "Rain gauges, radar, and satellites each sample rainfall differently; areal averaging (Thiessen, isohyetal) turns points into basins."},
    {t: "Interception and Infiltration", b: "Canopies catch rain, soils drink it: Horton's curve shows infiltration capacity falling as soil wets \u2014 the gate to runoff."},
    {t: "Runoff Generation", b: "Saturation-excess and infiltration-excess mechanisms decide when rain becomes streamflow \u2014 the core prediction of flood hydrology."},
    {t: "The Unit Hydrograph", b: "A watershed's fingerprint: the runoff response to one unit of excess rain, scaled and superposed to predict any storm's flood."},
    {t: "Groundwater and Aquifers", b: "Porous rock stores vast water; Darcy's law governs its slow flow \u2014 wells, springs, and baseflow all obey it."},
    {t: "Wells and Drawdown", b: "Pumping creates a cone of depression; Theis and Thiem equations predict drawdown and safe yield from aquifer tests."},
    {t: "Flood Frequency Analysis", b: "Annual maxima fit extreme-value distributions (Log-Pearson III): the '100-year flood' is a 1%-per-year probability, not a schedule."},
    {t: "Routing Floods Downstream", b: "Muskingum and dynamic-wave routing translate upstream hydrographs into downstream arrival times and attenuated peaks."},
    {t: "Evapotranspiration", b: "Penman-Monteith combines radiation, wind, and humidity to estimate the atmosphere's thirst \u2014 the largest term in most water budgets."},
    {t: "Urban Hydrology", b: "Pavement kills infiltration: cities make flashier floods and dirtier runoff, fought with detention, green infrastructure, and permeable design."},
    {t: "Water Resources Planning", b: "Reservoir yield, safe groundwater yield, and environmental flows balance human demand against the water cycle's limits."}
];
var PRINCIPLES=[
    {n: "Water balance", e: "P = ET + Q + \u0394S", s: "Precipitation partitions into evapotranspiration, runoff, and storage change \u2014 the master budget."},
    {n: "Darcy's law", e: "Q = \u2212K\u00b7A\u00b7dh/dl", s: "Groundwater flow is proportional to hydraulic conductivity and the head gradient."},
    {n: "Manning's equation", e: "V = (1/n)\u00b7R^(2/3)\u00b7S^(1/2)", s: "Open-channel velocity follows roughness, hydraulic radius, and slope."}
];
var USES=["Designing flood-control structures", "Siting and testing water wells", "Planning reservoir operations", "Managing urban stormwater"];
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
    id:id, t:tp.t, g:field, name:"Hydrology"+': '+tp.t, title:tp.t,
    description:desc, edition: seed%2 ? 'signature' : 'public',
    ladder_rank:rank, field:field,
    principle:{name:pr.n, equation:pr.e, statement:pr.s},
    key_points:[tp.b, pr.n+': '+pr.s, 'Application: '+use, 'Ladder rank '+rank+'/6'],
    src:'generator-sample', sample:true,
    disclaimer:'Generated sample record - not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:'python',language:'python',program:'# JAH Fundamentals of Hydrology demo\n# Record '+id+' — '+tp.t.replace(/\n/g,' ')+'\nprint("record jahdb-fundamental-hydrology-1.0")\nprint("OK: '+id+' generated fundamental record")\n',note:'Generator sample demo.'},
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
var gen={version:"jahdb-fundamental-hydrology-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("fundamental-hydrology",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
