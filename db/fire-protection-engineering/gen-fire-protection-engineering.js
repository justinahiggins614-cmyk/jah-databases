(function(){'use strict';
/* JAH Fire Protection Engineering Database generator — jahdb-fire-protection-engineering-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic synthesis record generation: pick a field, set a seed, get a complete record.
   Same seed + same field = same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-FPE-";
var FIELDS=["fire dynamics", "suppression", "detection", "smoke control", "egress", "codes"];
var TOPICS=[
    {t: "Fire Chemistry", b: "Pyrolysis, flaming vs smoldering, the fire tetrahedron: the chemistry every suppression agent interrupts."},
    {t: "Fire Growth", b: "Incipient, growth, flashover, fully developed, decay: the time-temperature curve structures burn through."},
    {t: "Heat Release Rate", b: "The single number characterizing fire size (kW to MW): what sprinklers, vents, and structures are designed against."},
    {t: "Sprinkler Systems", b: "Wet, dry, preaction, deluge: K-factors, design densities, and hydraulic calculations per NFPA 13."},
    {t: "Standpipes and Hydrants", b: "Firefighter water supply inside buildings: the manual backup when automatic systems need help."},
    {t: "Special Suppression", b: "Clean agents, CO\u2082, foam, water mist: protecting data centers, kitchens, and hazards water can't."},
    {t: "Detection and Alarm", b: "Smoke (ionization/photoelectric), heat, flame detectors plus notification: NFPA 72's engineered early warning."},
    {t: "Smoke Control", b: "Pressurized stairs, exhaust fans, atrium design: keeping escape routes tenable when fires fill spaces with smoke."},
    {t: "Egress Design", b: "Occupant load, exit width, travel distance, remoteness: the arithmetic of getting everyone out in time."},
    {t: "Passive Protection", b: "Fire-rated assemblies, firestopping penetrations, structural fireproofing: the protection that works without power."},
    {t: "Performance-Based Design", b: "Fire modeling (FDS) proving safety beyond prescriptive codes: engineering for the specific building."},
    {t: "Inspection and Maintenance", b: "NFPA 25 testing of sprinklers, alarms, extinguishers: protection that isn't maintained isn't protection."}
];
var PRINCIPLES=[
    {n: "Fire needs fuel, oxygen, heat", e: "", s: "Remove any leg of the triangle (or break the chain reaction): every suppression method attacks one leg."},
    {n: "Detection buys egress time", e: "", s: "Earlier warning is more survivable than bigger hoses: detection and alarm are the first line."},
    {n: "Compartmentation contains", e: "", s: "Fire-rated walls, floors, and dampers keep fires small: passive protection never needs water pressure."}
];
var USES=["Designing sprinkler systems", "Planning smoke control", "Calculating egress capacity", "Inspecting fire protection"];
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
    id:id, t:tp.t, g:field, name:"Fire Protection Engineering"+': '+tp.t, title:tp.t,
    description:desc, edition: seed%2 ? 'signature' : 'public',
    ladder_rank:rank, field:field,
    principle:{name:pr.n, equation:pr.e, statement:pr.s},
    key_points:[tp.b, pr.n+': '+pr.s, 'Application: '+use, 'Ladder rank '+rank+'/6'],
    src:'generator-sample', sample:true,
    disclaimer:'Generated sample record - not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:'python',language:'python',program:'# JAH Fire Protection Synthesis demo\n# Record '+id+' — '+tp.t.replace(/\n/g,' ')+'\nprint("record jahdb-fire-protection-engineering-1.0")\nprint("OK: '+id+' generated synthesis record")\n',note:'Generator sample demo.'},
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
var gen={version:"jahdb-fire-protection-engineering-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("fire-protection-engineering",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
