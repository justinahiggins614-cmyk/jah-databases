(function(){'use strict';
/* JAH Soil Sensor Networks Database generator — jahdb-soil-sensor-networks-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic synthesis record generation: pick a field, set a seed, get a complete record.
   Same seed + same field = same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-SSN-";
var FIELDS=["soil probes", "wireless networks", "LoRa and telemetry", "data platforms", "calibration", "decision integration"];
var TOPICS=[
    {t: "What to Sense", b: "Moisture (irrigation), temperature (planting, disease), EC/salinity, and emerging nitrate sensing: the soil's vital signs."},
    {t: "Moisture Probe Physics", b: "Capacitance/FDR and TDR read the soil's dielectric: water's \u03b5\u224880 against soil's ~4 makes moisture measurable."},
    {t: "Placement Strategy", b: "Depth (root zone), location (representative zones from EC maps), replication: where probes go matters more than which probes."},
    {t: "Wireless Options", b: "LoRaWAN (kilometers, years of battery), cellular, and Wi-Fi mesh: range, power, and cost traded per farm layout."},
    {t: "Power Budgets", b: "Solar plus lithium: sizing panels and batteries for cloudy weeks and winter \u2014 energy arithmetic for unattended nodes."},
    {t: "Gateways and Backhaul", b: "Field gateways aggregate node traffic to the cloud: placement, antenna height, and redundancy."},
    {t: "Data Platforms", b: "Dashboards, alerts, and APIs: turning time series into irrigation calls and agronomist reports."},
    {t: "Calibration Protocols", b: "Gravimetric sampling, lab analysis, and seasonal re-checks: the unglamorous work behind trustworthy numbers."},
    {t: "Maintenance Reality", b: "Flooded enclosures, chewed cables, dead batteries: a maintenance plan is part of the system design."},
    {t: "From Data to Irrigation", b: "Thresholds, trends, and integration with ET models: the decision rules that make sensors pay."},
    {t: "Nutrient Sensing Frontier", b: "Ion-selective and spectral probes for nitrate and pH: promising, still maturing \u2014 know the limits."},
    {t: "Economics", b: "Nodes per acre, subscription costs, and water/labor saved: the ROI math for sensing investments."}
];
var PRINCIPLES=[
    {n: "One probe is an anecdote", e: "", s: "Soil varies across every field: sensor density and placement strategy decide whether data represents the zone."},
    {n: "Calibrate to your soil", e: "", s: "Factory calibrations assume average soils: site-specific calibration against gravimetric samples is the difference between numbers and truth."},
    {n: "Networks must survive the field", e: "", s: "Mud, tractors, lightning, and seasons: enclosures, power budgets, and mounting decide whether the network lives past year one."}
];
var USES=["Planning sensor placement", "Choosing wireless telemetry", "Calibrating moisture probes", "Integrating data into irrigation calls"];
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
    id:id, t:tp.t, g:field, name:"Soil Sensor Networks"+': '+tp.t, title:tp.t,
    description:desc, edition: seed%2 ? 'signature' : 'public',
    ladder_rank:rank, field:field,
    principle:{name:pr.n, equation:pr.e, statement:pr.s},
    key_points:[tp.b, pr.n+': '+pr.s, 'Application: '+use, 'Ladder rank '+rank+'/6'],
    src:'generator-sample', sample:true,
    disclaimer:'Generated sample record - not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:'python',language:'python',program:'# JAH Soil Sensor Synthesis demo\n# Record '+id+' — '+tp.t.replace(/\n/g,' ')+'\nprint("record jahdb-soil-sensor-networks-1.0")\nprint("OK: '+id+' generated synthesis record")\n',note:'Generator sample demo.'},
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
var gen={version:"jahdb-soil-sensor-networks-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("soil-sensor-networks",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
