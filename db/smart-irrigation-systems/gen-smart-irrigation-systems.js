(function(){'use strict';
/* JAH Smart Irrigation Systems Database generator — jahdb-smart-irrigation-systems-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic synthesis record generation: pick a field, set a seed, get a complete record.
   Same seed + same field = same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-SIS-";
var FIELDS=["soil moisture sensing", "ET scheduling", "drip systems", "center pivots", "pumps and valves", "automation"];
var TOPICS=[
    {t: "How Much Water Crops Need", b: "Crop evapotranspiration (ETc = ETo \u00d7 Kc): reference ET times the crop coefficient, by growth stage."},
    {t: "Soil as a Reservoir", b: "Field capacity minus wilting point is the usable tank; management-allowed depletion sets the refill trigger."},
    {t: "Soil Moisture Sensors", b: "Capacitance, TDR, tensiometers: each reads a different moisture language \u2014 calibration to your soil is mandatory."},
    {t: "Scheduling Methods", b: "Water-balance bookkeeping, sensor thresholds, and plant-based sensing (canopy temperature): three ways to decide 'now'."},
    {t: "Drip Irrigation", b: "Emitters deliver water to the root zone at 90%+ efficiency: filtration, flushing, and chemigation management."},
    {t: "Center Pivots", b: "The workhorse of broadacre irrigation: spans, sprinklers, and variable-rate (VRI) zones following soil maps."},
    {t: "Pumps and Hydraulics", b: "Matching pump curves to system demand: pressure, flow, and energy cost per acre-inch."},
    {t: "Valves and Control", b: "Solenoids, pressure regulation, and flow control: the electromechanical layer automation commands."},
    {t: "Automation Architecture", b: "Controllers, telemetry (LoRa/cellular), and software: from timer boxes to cloud-scheduled precision systems."},
    {t: "Fertigation", b: "Feeding nutrients through the water: injection ratios, compatibility, and backflow prevention (safety first)."},
    {t: "Deficit Irrigation", b: "Strategic under-watering at tolerant growth stages saves water with minimal yield loss \u2014 stress as a tool."},
    {t: "Economics of Water", b: "Pumping energy, water cost, and yield response: the $/acre-inch math behind every upgrade decision."}
];
var PRINCIPLES=[
    {n: "Irrigate the root zone, not the calendar", e: "", s: "Soil-moisture depletion and crop ET set timing and depth: schedules follow physics, not days of the week."},
    {n: "Uniformity is efficiency", e: "", s: "A system applying unevenly wastes water wherever it over-applies: distribution uniformity above 85% is the target."},
    {n: "Measure, don't guess", e: "", s: "Sensors and flow meters close the loop: automated systems still need ground-truth verification."}
];
var USES=["Scheduling almond irrigation", "Designing drip systems", "Automating pivot control", "Troubleshooting uniformity problems"];
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
    id:id, t:tp.t, g:field, name:"Smart Irrigation Systems"+': '+tp.t, title:tp.t,
    description:desc, edition: seed%2 ? 'signature' : 'public',
    ladder_rank:rank, field:field,
    principle:{name:pr.n, equation:pr.e, statement:pr.s},
    key_points:[tp.b, pr.n+': '+pr.s, 'Application: '+use, 'Ladder rank '+rank+'/6'],
    src:'generator-sample', sample:true,
    disclaimer:'Generated sample record - not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:'python',language:'python',program:'# JAH Smart Irrigation Synthesis demo\n# Record '+id+' — '+tp.t.replace(/\n/g,' ')+'\nprint("record jahdb-smart-irrigation-systems-1.0")\nprint("OK: '+id+' generated synthesis record")\n',note:'Generator sample demo.'},
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
var gen={version:"jahdb-smart-irrigation-systems-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("smart-irrigation-systems",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
