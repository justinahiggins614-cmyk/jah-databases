(function(){'use strict';
/* JAH Grid-Scale Battery Storage Database generator — jahdb-grid-scale-battery-storage-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic synthesis record generation: pick a field, set a seed, get a complete record.
   Same seed + same field = same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-GSBS-";
var FIELDS=["lithium-ion", "flow batteries", "inverters (PCS)", "thermal management", "controls", "revenue stacking"];
var TOPICS=[
    {t: "Why Grids Need Storage", b: "Renewable variability, evening ramps, and contingency reserves: storage time-shifts energy and firms capacity."},
    {t: "Lithium-Ion Chemistries", b: "LFP (safe, long-lived) vs NMC (dense): grid storage has converged on LFP for its cycle life and thermal stability."},
    {t: "Flow Batteries", b: "Vanadium and zinc-bromine decouple power from energy: tanks scale duration independently \u2014 the long-duration candidate."},
    {t: "Alternative Long-Duration", b: "Compressed air, pumped hydro, iron-air, thermal: the 8\u2013100-hour technologies beyond lithium's 4-hour sweet spot."},
    {t: "Power Conversion Systems", b: "Bidirectional inverters (PCS) interface DC batteries to AC grids: efficiency, overload, and grid-forming capability."},
    {t: "Battery Management", b: "Cell balancing, SOC/SOH estimation, and contactor control: the BMS keeps thousands of cells acting as one."},
    {t: "Thermal Management", b: "Liquid cooling loops hold cells in their happy band: temperature uniformity is lifetime uniformity."},
    {t: "Fire Safety", b: "UL 9540/9540A testing, gas detection, deflagration venting, and spacing: the safety engineering buyers audit first."},
    {t: "Energy Management Systems", b: "Dispatch algorithms chase price signals and grid needs: software is the revenue engine."},
    {t: "Revenue Streams", b: "Energy arbitrage, frequency regulation, spinning reserve, capacity payments, transmission deferral: stacking the value."},
    {t: "Degradation Modeling", b: "Cycle-counting, calendar fade, and augmentation planning: predicting the battery's 15-year earning curve."},
    {t: "Project Development", b: "Site, interconnection, offtake contracts, and financing: storage projects as infrastructure assets."}
];
var PRINCIPLES=[
    {n: "Degradation is the business model", e: "", s: "Cycle life, calendar aging, and augmentation schedules decide whether the project earns its return."},
    {n: "Safety is non-negotiable", e: "", s: "Thermal-runaway propagation testing (UL 9540A) gates every installation: one fire poisons the market."},
    {n: "Revenue stacks or it doesn't pencil", e: "", s: "Arbitrage alone rarely pays: frequency regulation, capacity, and ancillary services combine into bankability."}
];
var USES=["Sizing storage for solar firming", "Selecting battery chemistries", "Modeling project revenue", "Designing fire-safe installations"];
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
    id:id, t:tp.t, g:field, name:"Grid-Scale Battery Storage"+': '+tp.t, title:tp.t,
    description:desc, edition: seed%2 ? 'signature' : 'public',
    ladder_rank:rank, field:field,
    principle:{name:pr.n, equation:pr.e, statement:pr.s},
    key_points:[tp.b, pr.n+': '+pr.s, 'Application: '+use, 'Ladder rank '+rank+'/6'],
    src:'generator-sample', sample:true,
    disclaimer:'Generated sample record - not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:'python',language:'python',program:'# JAH Grid Storage Synthesis demo\n# Record '+id+' — '+tp.t.replace(/\n/g,' ')+'\nprint("record jahdb-grid-scale-battery-storage-1.0")\nprint("OK: '+id+' generated synthesis record")\n',note:'Generator sample demo.'},
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
var gen={version:"jahdb-grid-scale-battery-storage-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("grid-scale-battery-storage",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
