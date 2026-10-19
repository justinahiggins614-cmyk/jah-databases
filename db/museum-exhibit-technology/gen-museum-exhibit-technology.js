(function(){'use strict';
/* JAH Museum Exhibit Technology Database generator — jahdb-museum-exhibit-technology-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic synthesis record generation: pick a field, set a seed, get a complete record.
   Same seed + same field = same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-MET2-";
var FIELDS=["interactives", "lighting", "AV systems", "sensors", "conservation", "maintenance"];
var TOPICS=[
    {t: "Exhibit Design Process", b: "Storyline, schematic, design development: the phases turning curatorial ideas into built experiences."},
    {t: "Interactive Displays", b: "Touchscreens, mechanical interactives, and tangible interfaces: dwell time as the success metric."},
    {t: "Museum Lighting", b: "50 lux for sensitive works, CRI 95+, UV-free LEDs: the conservation lighting discipline."},
    {t: "Projection and AV", b: "Edge-blended projection, directional audio: immersive media without touching artifacts."},
    {t: "Sensors and Triggers", b: "Proximity, capacitive, computer vision: exhibits that respond to visitors."},
    {t: "Show Control", b: "Centralized scheduling, monitoring, and content management: the backstage automation."},
    {t: "Conservation Constraints", b: "Light budgets (lux-hours), microclimates, vibration limits: the numbers technology must respect."},
    {t: "Accessibility", b: "Audio description, captions, tactile models, wheelchair sightlines: the inclusive exhibit standard."},
    {t: "Evaluation", b: "Timing, tracking, and surveys: measuring whether exhibits actually teach."},
    {t: "Maintenance", b: "Lamp schedules, software updates, spare parts: the operations plan behind the magic."},
    {t: "Temporary Exhibitions", b: "Touring shows' crates, couriers, and install choreography: the logistics of borrowed treasures."},
    {t: "Digital Extensions", b: "Apps, AR, and online collections: the museum beyond its walls."}
];
var PRINCIPLES=[
    {n: "Collections safety is absolute", e: "", s: "Light, heat, vibration, and off-gassing budgets constrain every technology near artifacts."},
    {n: "Reliability is the exhibit", e: "", s: "A dark interactive teaches nothing: commercial-grade hardware and remote monitoring keep exhibits alive."},
    {n: "Content drives technology", e: "", s: "The story chooses the medium: tech serving narrative, never tech for its own sake."}
];
var USES=["Designing interactive exhibits", "Specifying conservation lighting", "Planning AV systems", "Evaluating visitor engagement"];
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
    id:id, t:tp.t, g:field, name:"Museum Exhibit Technology"+': '+tp.t, title:tp.t,
    description:desc, edition: seed%2 ? 'signature' : 'public',
    ladder_rank:rank, field:field,
    principle:{name:pr.n, equation:pr.e, statement:pr.s},
    key_points:[tp.b, pr.n+': '+pr.s, 'Application: '+use, 'Ladder rank '+rank+'/6'],
    src:'generator-sample', sample:true,
    disclaimer:'Generated sample record - not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:'python',language:'python',program:'# JAH Museum Exhibit Synthesis demo\n# Record '+id+' — '+tp.t.replace(/\n/g,' ')+'\nprint("record jahdb-museum-exhibit-technology-1.0")\nprint("OK: '+id+' generated synthesis record")\n',note:'Generator sample demo.'},
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
var gen={version:"jahdb-museum-exhibit-technology-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("museum-exhibit-technology",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
