(function(){'use strict';
/* JAH Submarine Systems Engineering Database generator — jahdb-submarine-systems-engineering-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic synthesis record generation: pick a field, set a seed, get a complete record.
   Same seed + same field = same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-SSE-";
var FIELDS=["pressure hulls", "propulsion", "life support", "sonar and sensors", "safety", "operations"];
var TOPICS=[
    {t: "Pressure Hull Design", b: "HY-80/100 steels and titanium: ring-stiffened cylinders analyzed for buckling collapse with safety factors that reflect the stakes."},
    {t: "Depth Ratings", b: "Test depth, crush depth, never-exceed: the margins between operational and catastrophic."},
    {t: "Diesel-Electric Propulsion", b: "Snorting diesels charging batteries for silent running: the classic cycle and its indiscretion-rate limits."},
    {t: "Air-Independent Propulsion", b: "Fuel cells, Stirling engines, MESMA: weeks submerged without snorkeling \u2014 the conventional submarine's revolution."},
    {t: "Nuclear Propulsion", b: "Pressurized-water reactors giving unlimited submerged endurance: Nautilus's legacy and modern plant design."},
    {t: "Life Support", b: "Oxygen generation, CO\u2082 scrubbing, atmosphere monitoring: keeping 100+ people alive in a sealed tube for months."},
    {t: "Trim and Ballast", b: "Main ballast tanks, trim pumps, hover systems: the delicate buoyancy ballet of neutral depth-keeping."},
    {t: "Sonar Systems", b: "Passive listening vs active pinging: the acoustic duel, array design, and the thermocline's tricks."},
    {t: "Periscopes and Masts", b: "Optronics replacing hull-penetrating periscopes: photons up, vulnerability down."},
    {t: "Escape and Rescue", b: "Escape trunks, DSRVs, and rescue chambers: planning for the worst day with international cooperation."},
    {t: "Manned Submersibles", b: "Alvin, Trieste, Titan lessons: scientific and tourist deep diving under extreme pressure with tiny margins."},
    {t: "Unmanned Underwater Vehicles", b: "AUVs and ROVs for survey, inspection, and research: the growing robotic fleet."}
];
var PRINCIPLES=[
    {n: "The ocean is always trying to crush you", e: "", s: "Every depth adds a bar: pressure-hull design with collapse margins and rigorous NDT is survival engineering."},
    {n: "Silence is survival", e: "", s: "Machinery rafting, slow-turning propellers, anechoic tiles: acoustic stealth shapes every system choice."},
    {n: "Redundancy is life support", e: "", s: "Air, power, and surfacing capability in depth: no single failure may strand the boat."}
];
var USES=["Designing pressure hulls", "Planning AIP installations", "Engineering life-support systems", "Assessing submarine safety"];
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
    id:id, t:tp.t, g:field, name:"Submarine Systems Engineering"+': '+tp.t, title:tp.t,
    description:desc, edition: seed%2 ? 'signature' : 'public',
    ladder_rank:rank, field:field,
    principle:{name:pr.n, equation:pr.e, statement:pr.s},
    key_points:[tp.b, pr.n+': '+pr.s, 'Application: '+use, 'Ladder rank '+rank+'/6'],
    src:'generator-sample', sample:true,
    disclaimer:'Generated sample record - not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:'python',language:'python',program:'# JAH Submarine Systems Synthesis demo\n# Record '+id+' — '+tp.t.replace(/\n/g,' ')+'\nprint("record jahdb-submarine-systems-engineering-1.0")\nprint("OK: '+id+' generated synthesis record")\n',note:'Generator sample demo.'},
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
var gen={version:"jahdb-submarine-systems-engineering-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("submarine-systems-engineering",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
