(function(){'use strict';
/* JAH Flying Taxi Systems Database generator — jahdb-flying-taxi-systems-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic synthesis record generation: pick a field, set a seed, get a complete record.
   Same seed + same field = same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-FTS-";
var FIELDS=["eVTOL configurations", "batteries", "vertiports", "air traffic", "certification", "operations"];
var TOPICS=[
    {t: "eVTOL Configurations", b: "Multirotor, lift-plus-cruise, tilt-rotor, tilt-wing: the architectural trades between hover efficiency and cruise speed."},
    {t: "Distributed Electric Propulsion", b: "Many small motors: redundancy, blown-wing lift, and acoustic benefits \u2014 the enabling technology."},
    {t: "Batteries for Flight", b: "Energy density, power density, cycle life, charge rate: aviation demands all four simultaneously \u2014 the hardest battery job."},
    {t: "Noise", b: "Blade-vortex interaction and tip speed: designing for 65 dBA at 100 m \u2014 the community acceptance threshold."},
    {t: "Autonomy Path", b: "Piloted first, remotely supervised, then autonomous: the staged route through certification and trust."},
    {t: "Vertiports", b: "Takeoff pads, charging, passenger processing, and airspace access: the ground infrastructure network."},
    {t: "Air Traffic Integration", b: "UTM/U-space corridors, detect-and-avoid, and ATC interfaces: fitting thousands of new aircraft into the sky."},
    {t: "Certification", b: "FAA Part 23/27/29 adaptations, EASA SC-VTOL: the regulatory frameworks being written in real time."},
    {t: "Weather Limits", b: "Icing, winds, and visibility: urban microclimates constrain dispatch reliability."},
    {t: "Business Models", b: "Air taxi, airport shuttle, cargo, medevac: the use cases with economics that close first."},
    {t: "Safety Analysis", b: "System safety assessments, redundancy, and ballistic parachutes: proving eVTOL safety to regulators and riders."},
    {t: "Community Integration", b: "Routes over rivers and highways, equitable access, emergency services: earning the city's welcome."}
];
var PRINCIPLES=[
    {n: "Safety must beat driving, not just flying", e: "", s: "Public acceptance demands airline-like safety at car-like convenience: the certification bar is existential."},
    {n: "Noise decides where you can fly", e: "", s: "Community acceptance lives or dies on acoustic footprint: low-tip-speed distributed propellers are the answer."},
    {n: "Economics need utilization", e: "", s: "Expensive aircraft must fly constantly: turnaround time, charging, and demand density make or break the model."}
];
var USES=["Designing eVTOL configurations", "Planning vertiport networks", "Navigating certification", "Modeling air-taxi economics"];
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
    id:id, t:tp.t, g:field, name:"Flying Taxi Systems"+': '+tp.t, title:tp.t,
    description:desc, edition: seed%2 ? 'signature' : 'public',
    ladder_rank:rank, field:field,
    principle:{name:pr.n, equation:pr.e, statement:pr.s},
    key_points:[tp.b, pr.n+': '+pr.s, 'Application: '+use, 'Ladder rank '+rank+'/6'],
    src:'generator-sample', sample:true,
    disclaimer:'Generated sample record - not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:'python',language:'python',program:'# JAH Flying Taxi Synthesis demo\n# Record '+id+' — '+tp.t.replace(/\n/g,' ')+'\nprint("record jahdb-flying-taxi-systems-1.0")\nprint("OK: '+id+' generated synthesis record")\n',note:'Generator sample demo.'},
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
var gen={version:"jahdb-flying-taxi-systems-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("flying-taxi-systems",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
