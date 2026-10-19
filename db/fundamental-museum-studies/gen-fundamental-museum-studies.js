(function(){'use strict';
/* JAH Fundamentals of Museum Studies Database generator — jahdb-fundamental-museum-studies-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic fundamental record generation: pick a field, set a seed, get a complete record.
   Same seed + same field = same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-MS-";
var FIELDS=["collections", "conservation", "curation", "exhibition design", "education", "museum management"];
var TOPICS=[
    {t: "What Museums Are For", b: "Museums collect, preserve, research, and interpret material culture \u2014 public trust institutions holding heritage in perpetuity."},
    {t: "Collecting and Accessioning", b: "Acquisition policies, provenance research, and accession records decide what enters the permanent collection \u2014 and document it forever."},
    {t: "Provenance and Ethics", b: "Ownership history must be clean: looted, stolen, or unethically excavated objects don't belong in museums \u2014 repatriation follows."},
    {t: "Preventive Conservation", b: "50% RH \u00b15, 18\u201320\u00b0C, under 50 lux for sensitive works: environmental control prevents the damage restoration can't undo."},
    {t: "Conservation Treatments", b: "Cleaning, stabilization, and repair follow minimal-intervention ethics: every treatment must be reversible and documented."},
    {t: "Registration and Documentation", b: "Catalog numbers, condition reports, and location tracking make thousands of objects findable, accountable, and researchable."},
    {t: "Curatorial Research", b: "Curators authenticate, contextualize, and publish: scholarship turns stored objects into knowledge."},
    {t: "Exhibition Design", b: "Narrative arcs, sight lines, lighting, and pacing turn galleries into arguments visitors walk through."},
    {t: "Labels and Interpretation", b: "50-word labels beat 500: layered interpretation (title, theme, detail) serves skimmers and scholars alike."},
    {t: "Museum Education", b: "Tours, programs, and interactives translate collections into learning for every age \u2014 education is the public half of the mission."},
    {t: "Visitor Studies", b: "Tracking, timing, and surveys reveal what visitors actually do \u2014 then design serves behavior, not assumptions."},
    {t: "Museum Management", b: "Governance, fundraising, security, and facilities keep the mission alive: nonprofits with collections to protect forever."}
];
var PRINCIPLES=[
    {n: "Preventive conservation", e: "control environment, not objects", s: "Stable temperature, humidity, and light prevent damage cheaper than any restoration."},
    {n: "Significance assessment", e: "value = f(rarity, context, condition)", s: "What to keep, and why, follows from documented significance \u2014 not sentiment."},
    {n: "Interpretive hierarchy", e: "theme \u2192 storyline \u2192 labels", s: "Exhibitions communicate one big idea through layered, progressively detailed interpretation."}
];
var USES=["Planning museum exhibitions", "Writing collection policies", "Designing conservation environments", "Building visitor programs"];
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
    id:id, t:tp.t, g:field, name:"Museum Studies"+': '+tp.t, title:tp.t,
    description:desc, edition: seed%2 ? 'signature' : 'public',
    ladder_rank:rank, field:field,
    principle:{name:pr.n, equation:pr.e, statement:pr.s},
    key_points:[tp.b, pr.n+': '+pr.s, 'Application: '+use, 'Ladder rank '+rank+'/6'],
    src:'generator-sample', sample:true,
    disclaimer:'Generated sample record - not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:'python',language:'python',program:'# JAH Fundamentals of Museum Studies demo\n# Record '+id+' — '+tp.t.replace(/\n/g,' ')+'\nprint("record jahdb-fundamental-museum-studies-1.0")\nprint("OK: '+id+' generated fundamental record")\n',note:'Generator sample demo.'},
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
var gen={version:"jahdb-fundamental-museum-studies-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("fundamental-museum-studies",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
