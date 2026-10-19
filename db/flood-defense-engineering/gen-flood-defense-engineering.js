(function(){'use strict';
/* JAH Flood Defense Engineering Database generator — jahdb-flood-defense-engineering-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic synthesis record generation: pick a field, set a seed, get a complete record.
   Same seed + same field = same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-FDE-";
var FIELDS=["levees", "dams", "storm surge barriers", "flood mapping", "pumping", "residual risk"];
var TOPICS=[
    {t: "Flood Types", b: "Riverine, coastal surge, pluvial, flash: different physics, different defenses, different warnings."},
    {t: "Levee Design", b: "Embankment geometry, seepage cutoffs, slope protection: USACE EM 1110-2-1913's geotechnical discipline."},
    {t: "Levee Failure Modes", b: "Overtopping, piping, slope instability: New Orleans 2005's lessons written into modern practice."},
    {t: "Dams for Flood Control", b: "Reservoir routing: storing the peak and releasing it slowly \u2014 rule curves balancing flood space vs water supply."},
    {t: "Spillways", b: "Service, auxiliary, and emergency spillways pass the probable maximum flood: Oroville 2017's warning about spillway integrity."},
    {t: "Storm Surge Barriers", b: "Thames, Maeslant, Venice MOSE: movable barriers closing against the sea \u2014 the Netherlands' mastery."},
    {t: "Flood Mapping", b: "HEC-RAS modeling, FEMA floodplains, future-conditions hydrology: the maps that set insurance and building codes."},
    {t: "Urban Drainage", b: "Storm sewers, detention basins, green infrastructure: managing the paved watershed's flashy runoff."},
    {t: "Pumping Stations", b: "Low-lying areas pump out: capacity, redundancy, and backup power when the grid fails during the storm."},
    {t: "Nature-Based Defenses", b: "Wetlands, dunes, and floodplain reconnection: working with water's physics instead of against it."},
    {t: "Residual Risk", b: "Levees reduce risk, never eliminate it: evacuation planning, floodproofing, and insurance for the beyond-design flood."},
    {t: "Climate Adaptation", b: "Heavier rainfall and higher seas move the goalposts: adaptive pathways planning for uncertain futures."}
];
var PRINCIPLES=[
    {n: "Design for the overtopping", e: "", s: "Every defense can be exceeded: armored crests, controlled spillways, and evacuation plans assume failure happens."},
    {n: "Geotechnics decides levees", e: "", s: "Seepage, slope stability, and underseepage piping \u2014 not concrete \u2014 are levee engineering's core."},
    {n: "Conveyance beats containment alone", e: "", s: "Channel capacity, detention, and floodplain storage work with barriers: systems, not walls."}
];
var USES=["Designing levee systems", "Mapping floodplains", "Planning surge barriers", "Managing residual flood risk"];
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
    id:id, t:tp.t, g:field, name:"Flood Defense Engineering"+': '+tp.t, title:tp.t,
    description:desc, edition: seed%2 ? 'signature' : 'public',
    ladder_rank:rank, field:field,
    principle:{name:pr.n, equation:pr.e, statement:pr.s},
    key_points:[tp.b, pr.n+': '+pr.s, 'Application: '+use, 'Ladder rank '+rank+'/6'],
    src:'generator-sample', sample:true,
    disclaimer:'Generated sample record - not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:'python',language:'python',program:'# JAH Flood Defense Synthesis demo\n# Record '+id+' — '+tp.t.replace(/\n/g,' ')+'\nprint("record jahdb-flood-defense-engineering-1.0")\nprint("OK: '+id+' generated synthesis record")\n',note:'Generator sample demo.'},
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
var gen={version:"jahdb-flood-defense-engineering-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("flood-defense-engineering",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
