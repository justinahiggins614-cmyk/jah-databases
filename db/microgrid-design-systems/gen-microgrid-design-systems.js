(function(){'use strict';
/* JAH Microgrid Design Systems Database generator — jahdb-microgrid-design-systems-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic synthesis record generation: pick a field, set a seed, get a complete record.
   Same seed + same field = same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-MDS-";
var FIELDS=["architectures", "generation mix", "islanding", "protection", "controls", "economics"];
var TOPICS=[
    {t: "What Counts as a Microgrid", b: "Bounded electrical systems with generation, load, and the ability to island: DOE's definition and the common architectures."},
    {t: "Use Cases", b: "Campus resilience, remote villages, military bases, community solar+storage: different missions, different designs."},
    {t: "Generation Mix", b: "Solar, gas gensets, CHP, wind, small hydro: sizing each to the load-duration curve and fuel logistics."},
    {t: "Sizing Storage", b: "Power (kW) for transients and peaks, energy (kWh) for ride-through duration: the two-axis sizing problem."},
    {t: "Islanding Switches and Controls", b: "Static switches, synchronizing breakers, and the 2-second transfer: the hardware of separation."},
    {t: "Hierarchical Control", b: "Primary (droop), secondary (restoration), tertiary (economic dispatch): the three control layers keeping islanded grids stable."},
    {t: "Protection Challenges", b: "Inverter fault currents are small and weird: protection must detect faults with 1.2-pu current, not 6-pu."},
    {t: "Black Start", b: "Cranking the microgrid from dead with grid-forming inverters or gensets: the ultimate resilience test."},
    {t: "Cybersecurity", b: "Networked controllers are attack surfaces: segmentation, authentication, and NERC CIP-inspired practice for microgrids."},
    {t: "Utility Interconnection", b: "IEEE 1547-2018 microgrid provisions: the technical and procedural path to legal operation."},
    {t: "Business Models", b: "Utility-owned, third-party, community: who pays, who benefits, and how regulations treat each."},
    {t: "Economics", b: "Demand-charge shaving, outage value, and incentives vs capex: the spreadsheet behind every go/no-go."}
];
var PRINCIPLES=[
    {n: "Islanding is the defining feature", e: "", s: "Seamless separation and resynchronization with the main grid is what makes a microgrid, not just local generation."},
    {n: "Protection must work both ways", e: "", s: "Fault currents differ grid-tied vs islanded: relays need settings groups or adaptive schemes for both modes."},
    {n: "Resilience has a price tag", e: "", s: "Hours of islanding capability vs cost: the value-of-lost-load math sizes the system honestly."}
];
var USES=["Designing campus microgrids", "Sizing islanding storage", "Planning protection schemes", "Modeling resilience economics"];
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
    id:id, t:tp.t, g:field, name:"Microgrid Design Systems"+': '+tp.t, title:tp.t,
    description:desc, edition: seed%2 ? 'signature' : 'public',
    ladder_rank:rank, field:field,
    principle:{name:pr.n, equation:pr.e, statement:pr.s},
    key_points:[tp.b, pr.n+': '+pr.s, 'Application: '+use, 'Ladder rank '+rank+'/6'],
    src:'generator-sample', sample:true,
    disclaimer:'Generated sample record - not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:'python',language:'python',program:'# JAH Microgrid Synthesis demo\n# Record '+id+' — '+tp.t.replace(/\n/g,' ')+'\nprint("record jahdb-microgrid-design-systems-1.0")\nprint("OK: '+id+' generated synthesis record")\n',note:'Generator sample demo.'},
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
var gen={version:"jahdb-microgrid-design-systems-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("microgrid-design-systems",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
