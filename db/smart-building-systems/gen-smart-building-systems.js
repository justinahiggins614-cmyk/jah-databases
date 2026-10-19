(function(){'use strict';
/* JAH Smart Building Systems Database generator — jahdb-smart-building-systems-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic synthesis record generation: pick a field, set a seed, get a complete record.
   Same seed + same field = same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-SBS-";
var FIELDS=["BMS", "HVAC controls", "lighting", "sensors", "integration", "cybersecurity"];
var TOPICS=[
    {t: "What Makes a Building Smart", b: "Sensing, control, and optimization serving comfort, efficiency, and maintenance: outcomes, not gadgets."},
    {t: "Building Management Systems", b: "Supervisory controllers, field devices, and graphics: the architecture of modern BMS."},
    {t: "HVAC Controls", b: "VAV boxes, economizers, demand-controlled ventilation: the sequences saving 20\u201330% of building energy."},
    {t: "Lighting Controls", b: "Daylight harvesting, occupancy sensing, tunable white: lighting as a responsive system."},
    {t: "Sensors", b: "Temperature, CO\u2082, occupancy, light level: the instrument layer feeding every decision."},
    {t: "BACnet and Protocols", b: "Objects, services, and interoperability: the lingua franca gluing multi-vendor systems."},
    {t: "Energy Analytics", b: "Fault detection and diagnostics (FDD): algorithms finding the stuck dampers and fighting valves humans miss."},
    {t: "Access and Security", b: "Card readers, cameras, and intrusion on the same network: physical security's IT convergence."},
    {t: "Cybersecurity", b: "Segmented networks, patched controllers, and incident plans: buildings as cyber-physical targets."},
    {t: "Occupant Experience", b: "Apps for booking, comfort voting, and wayfinding: the human interface of the smart building."},
    {t: "Grid Interaction", b: "Demand response and thermal storage: buildings as flexible grid resources earning revenue."},
    {t: "Commissioning and Retro-Cx", b: "Testing sequences under real loads, then re-testing every few years: performance doesn't persist by itself."}
];
var PRINCIPLES=[
    {n: "Integration is the value", e: "", s: "Isolated smart devices are gadgets: BACnet/IP integration into one BMS is the building system."},
    {n: "Commissioning decides performance", e: "", s: "Uncommissioned controls waste the hardware investment: functional testing in real operation is mandatory."},
    {n: "Open protocols prevent lock-in", e: "", s: "BACnet, Modbus, KNX: specifying open standards keeps owners free from single-vendor capture."}
];
var USES=["Specifying BMS systems", "Commissioning HVAC controls", "Integrating building networks", "Securing building OT"];
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
    id:id, t:tp.t, g:field, name:"Smart Building Systems"+': '+tp.t, title:tp.t,
    description:desc, edition: seed%2 ? 'signature' : 'public',
    ladder_rank:rank, field:field,
    principle:{name:pr.n, equation:pr.e, statement:pr.s},
    key_points:[tp.b, pr.n+': '+pr.s, 'Application: '+use, 'Ladder rank '+rank+'/6'],
    src:'generator-sample', sample:true,
    disclaimer:'Generated sample record - not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:'python',language:'python',program:'# JAH Smart Building Synthesis demo\n# Record '+id+' — '+tp.t.replace(/\n/g,' ')+'\nprint("record jahdb-smart-building-systems-1.0")\nprint("OK: '+id+' generated synthesis record")\n',note:'Generator sample demo.'},
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
var gen={version:"jahdb-smart-building-systems-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("smart-building-systems",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
