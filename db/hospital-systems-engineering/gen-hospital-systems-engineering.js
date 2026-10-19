(function(){'use strict';
/* JAH Hospital Systems Engineering Database generator — jahdb-hospital-systems-engineering-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic synthesis record generation: pick a field, set a seed, get a complete record.
   Same seed + same field = same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-HSE-";
var FIELDS=["master planning", "infection control", "HVAC and airflow", "medical gases", "critical power", "patient flow"];
var TOPICS=[
    {t: "Hospital Master Planning", b: "Bed towers, diagnostic cores, and growth spines: planning for expansion you'll need and flexibility you can't predict."},
    {t: "Department Adjacencies", b: "ED next to imaging next to surgery: travel distances for trauma, stroke, and sepsis patients are clinical outcomes."},
    {t: "Isolation Rooms", b: "Negative pressure for airborne (TB), positive for protective (transplant): 12 air changes per hour and pressure monitors."},
    {t: "Operating Room Design", b: "Laminar airflow, 20+ air changes, temperature/humidity control, and boom-mounted utilities: the OR as a machine."},
    {t: "Medical Gas Systems", b: "Oxygen, medical air, vacuum, nitrous: manifolded, piped, alarmed per NFPA 99 \u2014 the hospital's hidden utilities."},
    {t: "Critical Power", b: "Essential electrical systems (life-safety, critical, equipment branches) with generator backup in 10 seconds per code."},
    {t: "Water Safety", b: "Legionella control in complex plumbing: temperature maintenance, flushing protocols, and water management plans."},
    {t: "Wayfinding", b: "Stressed visitors navigate by landmarks, color, and sightlines: signage systems designed for the worst day of someone's life."},
    {t: "Patient Flow Engineering", b: "Bed management, ED throughput, and discharge lounges: queuing theory applied to hallways and waiting rooms."},
    {t: "Resilience", b: "Hospitals must function through disasters: flood elevation, seismic design, fuel storage, and 96-hour self-sufficiency."},
    {t: "Sustainability", b: "Energy-intensive 24/7 operations meet efficiency: heat recovery, LED retrofits, and waste segregation cut costs and footprint."},
    {t: "Commissioning", b: "Testing every system under load before opening: the verification step that catches what drawings missed."}
];
var PRINCIPLES=[
    {n: "Infection control is architecture", e: "", s: "Hand-wash placement, isolation room pressure, and material cleanability are designed before the first wall is drawn."},
    {n: "Hospitals never lose power", e: "", s: "Redundant feeds, generators in 10 seconds, and isolated-power ORs: electrical design assumes the grid fails."},
    {n: "Flow is the product", e: "", s: "Patient, staff, supply, and waste flows that cross contaminate or delay care are design failures, whatever the finishes look like."}
];
var USES=["Planning hospital expansions", "Designing isolation rooms", "Sizing emergency power", "Improving patient throughput"];
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
    id:id, t:tp.t, g:field, name:"Hospital Systems Engineering"+': '+tp.t, title:tp.t,
    description:desc, edition: seed%2 ? 'signature' : 'public',
    ladder_rank:rank, field:field,
    principle:{name:pr.n, equation:pr.e, statement:pr.s},
    key_points:[tp.b, pr.n+': '+pr.s, 'Application: '+use, 'Ladder rank '+rank+'/6'],
    src:'generator-sample', sample:true,
    disclaimer:'Generated sample record - not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:'python',language:'python',program:'# JAH Hospital Systems Synthesis demo\n# Record '+id+' — '+tp.t.replace(/\n/g,' ')+'\nprint("record jahdb-hospital-systems-engineering-1.0")\nprint("OK: '+id+' generated synthesis record")\n',note:'Generator sample demo.'},
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
var gen={version:"jahdb-hospital-systems-engineering-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("hospital-systems-engineering",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
