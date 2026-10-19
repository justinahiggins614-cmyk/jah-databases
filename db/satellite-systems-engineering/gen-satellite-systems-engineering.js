(function(){'use strict';
/* JAH Satellite Systems Engineering Database generator — jahdb-satellite-systems-engineering-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic synthesis record generation: pick a field, set a seed, get a complete record.
   Same seed + same field = same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-SSE2-";
var FIELDS=["bus subsystems", "power", "communications", "ADCS", "payloads", "constellations"];
var TOPICS=[
    {t: "Satellite Anatomy", b: "Bus (power, comms, ADCS, thermal, structure) plus payload: the standard decomposition of every spacecraft."},
    {t: "Power Systems", b: "Solar arrays, batteries (Li-ion), power distribution: sizing for eclipse and end-of-life degradation."},
    {t: "Communications", b: "TT&C links, link budgets, frequency bands: the RF engineering connecting orbit to ground."},
    {t: "Attitude Control (ADCS)", b: "Reaction wheels, magnetorquers, star trackers: pointing payloads precisely while orbiting at 7.8 km/s."},
    {t: "Thermal Control", b: "MLI blankets, radiators, heaters: surviving \u00b1150\u00b0C swings with passive-first design."},
    {t: "Propulsion", b: "Chemical, electric (Hall, ion), cold gas: station-keeping, deorbit, and the delta-v budget."},
    {t: "Payloads", b: "Imagers, transponders, science instruments: the mission hardware the bus exists to serve."},
    {t: "CubeSats", b: "The 10-cm revolution: standardized small sats democratizing orbit \u2014 capabilities and limits."},
    {t: "Constellations", b: "Starlink-class networks: orbital shells, coverage math, and collision-avoidance at scale."},
    {t: "Launch", b: "Rideshare vs dedicated, deployment, commissioning: getting to orbit and waking up healthy."},
    {t: "Ground Segment", b: "Ground stations, operations centers, and automation: the terrestrial half of the system."},
    {t: "Space Debris", b: "Tracking, avoidance maneuvers, and deorbit rules: the sustainability crisis of low Earth orbit."}
];
var PRINCIPLES=[
    {n: "Power is the currency", e: "", s: "Every subsystem spends watts from the same solar-battery budget: power allocation is system design."},
    {n: "Radiation is the environment", e: "", s: "Single-event effects and total dose shape every part choice: rad-hard or rad-tolerant by design."},
    {n: "Test like you fly", e: "", s: "Thermal vacuum, vibration, EMC: the test campaign is where missions are saved, on the ground."}
];
var USES=["Sizing satellite power systems", "Designing CubeSat missions", "Planning constellations", "Budgeting communications links"];
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
    id:id, t:tp.t, g:field, name:"Satellite Systems Engineering"+': '+tp.t, title:tp.t,
    description:desc, edition: seed%2 ? 'signature' : 'public',
    ladder_rank:rank, field:field,
    principle:{name:pr.n, equation:pr.e, statement:pr.s},
    key_points:[tp.b, pr.n+': '+pr.s, 'Application: '+use, 'Ladder rank '+rank+'/6'],
    src:'generator-sample', sample:true,
    disclaimer:'Generated sample record - not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:'python',language:'python',program:'# JAH Satellite Systems Synthesis demo\n# Record '+id+' — '+tp.t.replace(/\n/g,' ')+'\nprint("record jahdb-satellite-systems-engineering-1.0")\nprint("OK: '+id+' generated synthesis record")\n',note:'Generator sample demo.'},
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
var gen={version:"jahdb-satellite-systems-engineering-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("satellite-systems-engineering",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
