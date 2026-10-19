(function(){'use strict';
/* JAH Fundamentals of Ergonomics Database generator — jahdb-fundamental-ergonomics-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic fundamental record generation: pick a field, set a seed, get a complete record.
   Same seed + same field = same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-ERG-";
var FIELDS=["anthropometry", "biomechanics", "workstation design", "cognitive ergonomics", "environmental factors", "safety and error"];
var TOPICS=[
    {t: "What Ergonomics Is", b: "Ergonomics fits the task, tools, and environment to human bodies and minds \u2014 designing for the 5th-to-95th percentile, never the average alone."},
    {t: "Anthropometry: Measuring People", b: "Body dimensions vary by sex, age, and population; design adjustability (chairs, desks) beats designing for one fixed size."},
    {t: "Biomechanics of Lifting", b: "The spine is a lever: loads held far from the body multiply spinal force, which is why lifting close and with legs matters."},
    {t: "Repetitive Strain and MSDs", b: "Repetition, force, and awkward posture combine into musculoskeletal disorders; job rotation and tool redesign are the engineering fixes."},
    {t: "Workstation Layout", b: "Reach envelopes, sight lines, and the normal work area dictate where controls and materials belong \u2014 frequency of use sets placement priority."},
    {t: "Seated vs Standing Work", b: "Prolonged sitting loads spinal discs; prolonged standing swells legs \u2014 sit-stand rotation with anti-fatigue mats is the evidence-backed middle path."},
    {t: "Cognitive Ergonomics", b: "Mental workload, attention, and memory limits shape interfaces: chunk information, confirm destructive actions, and never rely on unaided recall."},
    {t: "Displays and Controls", b: "Compatibility rules: up/right means increase, red means stop, and control-display mapping must match the operator's mental model."},
    {t: "Lighting, Noise, and Climate", b: "500 lux for office tasks, 65 dB conversation limits, 20\u201324\u00b0C comfort bands \u2014 environmental factors are ergonomic factors."},
    {t: "Human Error and Safety", b: "Errors are systematic, not moral failings: design affordances, constraints, and forcing functions that make the right action easy and the wrong one hard."},
    {t: "Shift Work and Fatigue", b: "Night shifts fight circadian biology; forward-rotating schedules, light management, and protected sleep windows cut fatigue-related errors."},
    {t: "Usability Testing", b: "Watch real users perform real tasks, measure errors and time, iterate: the empirical loop that turns ergonomic theory into working products."}
];
var PRINCIPLES=[
    {n: "NIOSH lifting equation", e: "RWL = LC \u00b7 HM \u00b7 VM \u00b7 DM \u00b7 AM \u00b7 FM \u00b7 CM", s: "Recommended weight limit falls as lifts get farther, lower, more twisted, or more frequent."},
    {n: "Fitts's law", e: "MT = a + b \u00b7 log2(2D/W)", s: "Pointing time grows with distance and shrinks with target size \u2014 the law behind button sizing."},
    {n: "Comfort zone principle", e: "work between knuckle and shoulder height", s: "Keeping work inside the body's power zone minimizes strain and fatigue."}
];
var USES=["Designing adjustable office workstations", "Reducing warehouse lifting injuries", "Building usable software interfaces", "Planning safe shift schedules"];
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
    id:id, t:tp.t, g:field, name:"Ergonomics"+': '+tp.t, title:tp.t,
    description:desc, edition: seed%2 ? 'signature' : 'public',
    ladder_rank:rank, field:field,
    principle:{name:pr.n, equation:pr.e, statement:pr.s},
    key_points:[tp.b, pr.n+': '+pr.s, 'Application: '+use, 'Ladder rank '+rank+'/6'],
    src:'generator-sample', sample:true,
    disclaimer:'Generated sample record - not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:'python',language:'python',program:'# JAH Fundamentals of Ergonomics demo\n# Record '+id+' — '+tp.t.replace(/\n/g,' ')+'\nprint("record jahdb-fundamental-ergonomics-1.0")\nprint("OK: '+id+' generated fundamental record")\n',note:'Generator sample demo.'},
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
var gen={version:"jahdb-fundamental-ergonomics-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("fundamental-ergonomics",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
