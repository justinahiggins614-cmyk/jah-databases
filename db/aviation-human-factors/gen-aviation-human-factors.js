(function(){'use strict';
/* JAH Aviation Human Factors Database generator — jahdb-aviation-human-factors-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic synthesis record generation: pick a field, set a seed, get a complete record.
   Same seed + same field = same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-AHF-";
var FIELDS=["CRM", "cockpit design", "fatigue", "error", "automation", "investigation"];
var TOPICS=[
    {t: "Crew Resource Management", b: "Communication, leadership, and decision-making in the cockpit: the training born from 1970s disasters."},
    {t: "The SHELL Model", b: "Software, hardware, environment, liveware: the framework mapping human-system interactions."},
    {t: "Cockpit Design", b: "Displays, controls, and alerting (EICAS/ECAM): the human-machine interface evolving from steam gauges to glass."},
    {t: "Automation Philosophy", b: "Boeing (pilot authority) vs Airbus (envelope protection): two answers to how much the machine should override."},
    {t: "Mode Awareness", b: "Knowing what the automation is doing: the confusion behind several accidents, fixed by better feedback."},
    {t: "Fatigue", b: "Circadian disruption, duty limits (Part 117), and controlled rest: managing the biology of long-haul crews."},
    {t: "Situation Awareness", b: "Perception, comprehension, projection (Endsley): the cognitive skill training and design must support."},
    {t: "Checklists", b: "Normal, abnormal, emergency: the discipline that caught what memory misses \u2014 from B-17 to surgery."},
    {t: "Threat and Error Management", b: "Anticipating, trapping, and mitigating threats and errors: the operational philosophy of modern airlines."},
    {t: "Accident Investigation", b: "NTSB process, human-factors analysis (HFACS): learning systems, not blaming individuals."},
    {t: "Cabin Safety", b: "Evacuation, ditching, and passenger behavior: the 90-second rule and the human factors of the cabin."},
    {t: "Maintenance Human Factors", b: "Dirty dozen (complacency, pressure, fatigue): the error traps in hangars, addressed by MRM programs."}
];
var PRINCIPLES=[
    {n: "Humans err; systems must tolerate it", e: "", s: "Design assumes mistakes: cross-checks, warnings, and recoverable states, not perfect pilots."},
    {n: "Workload must fit the human", e: "", s: "Too high overwhelms, too low bores into inattention: automation levels tuned to keep pilots in the loop."},
    {n: "Culture enables safety", e: "", s: "Just culture reporting (ASRS) surfaces the near-misses that investigations need: blame kills data."}
];
var USES=["Designing cockpit procedures", "Training CRM", "Investigating incidents", "Managing crew fatigue"];
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
    id:id, t:tp.t, g:field, name:"Aviation Human Factors"+': '+tp.t, title:tp.t,
    description:desc, edition: seed%2 ? 'signature' : 'public',
    ladder_rank:rank, field:field,
    principle:{name:pr.n, equation:pr.e, statement:pr.s},
    key_points:[tp.b, pr.n+': '+pr.s, 'Application: '+use, 'Ladder rank '+rank+'/6'],
    src:'generator-sample', sample:true,
    disclaimer:'Generated sample record - not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:'python',language:'python',program:'# JAH Aviation Human Factors Synthesis demo\n# Record '+id+' — '+tp.t.replace(/\n/g,' ')+'\nprint("record jahdb-aviation-human-factors-1.0")\nprint("OK: '+id+' generated synthesis record")\n',note:'Generator sample demo.'},
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
var gen={version:"jahdb-aviation-human-factors-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("aviation-human-factors",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
