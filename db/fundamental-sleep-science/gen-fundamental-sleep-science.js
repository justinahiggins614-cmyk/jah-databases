(function(){'use strict';
/* JAH Fundamentals of Sleep Science Database generator — jahdb-fundamental-sleep-science-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic fundamental record generation: pick a field, set a seed, get a complete record.
   Same seed + same field = same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-SS-";
var FIELDS=["sleep stages", "circadian rhythms", "sleep regulation", "dreams", "sleep disorders", "sleep optimization"];
var TOPICS=[
    {t: "Why Sleep Exists", b: "Memory consolidation, metabolic clearance (glymphatic system), immune tuning, and growth hormone release all require the sleeping brain."},
    {t: "The Stages of Sleep", b: "N1 drowsing, N2 light sleep with spindles, N3 deep slow-wave sleep, and REM dreaming \u2014 each with distinct brain waves and jobs."},
    {t: "Deep Sleep: Body Repair", b: "Slow-wave sleep releases growth hormone, consolidates declarative memory, and clears metabolic waste \u2014 the physically restorative stage."},
    {t: "REM Sleep: Brain Work", b: "Dreaming sleep processes emotion and procedural memory while paralyzing muscles \u2014 vivid dreams with an active, offline brain."},
    {t: "The Circadian Clock", b: "The suprachiasmatic nucleus runs a ~24.2-hour cycle, entrained by morning light; it times sleep, hormones, and alertness peaks."},
    {t: "Melatonin and Light", b: "Darkness triggers melatonin release; blue-rich light suppresses it \u2014 the lever behind screen-time sleep advice."},
    {t: "Sleep Pressure and Adenosine", b: "Every waking hour accumulates adenosine; caffeine works by blocking its receptors, borrowing alertness against future sleep."},
    {t: "How Much Sleep", b: "Adults need 7\u20139 hours; teenagers need more; chronic restriction below 6 hours impairs cognition like intoxication \u2014 with no full adaptation."},
    {t: "Naps: Strategic Rest", b: "10\u201320-minute naps boost alertness without grogginess; 90-minute naps complete a full cycle \u2014 timing decides the benefit."},
    {t: "Insomnia", b: "Hyperarousal, not just bad habits, drives insomnia; CBT-I (stimulus control, sleep restriction) outperforms pills long-term."},
    {t: "Sleep Apnea", b: "Repeated airway collapse fragments sleep and strains the heart; CPAP pneumatically splints the airway open \u2014 the gold-standard fix."},
    {t: "Shift Work and Jet Lag", b: "Fighting the circadian clock costs health and safety; timed light, melatonin, and anchor sleep are the evidence-based countermeasures."}
];
var PRINCIPLES=[
    {n: "Two-process model", e: "sleepiness = circadian + homeostatic", s: "Sleep pressure builds with wakefulness (adenosine) and gates with the circadian clock."},
    {n: "90-minute cycles", e: "NREM \u2192 REM repeats ~90 min", s: "Sleep cycles through light, deep, and REM stages roughly every hour and a half."},
    {n: "Adenosine accumulation", e: "pressure \u221d hours awake", s: "The homeostatic sleep drive tracks a molecule caffeine blocks \u2014 the chemistry of tiredness."}
];
var USES=["Treating insomnia without drugs", "Fitting CPAP for apnea patients", "Scheduling shift work safely", "Optimizing athletic recovery sleep"];
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
    id:id, t:tp.t, g:field, name:"Sleep Science"+': '+tp.t, title:tp.t,
    description:desc, edition: seed%2 ? 'signature' : 'public',
    ladder_rank:rank, field:field,
    principle:{name:pr.n, equation:pr.e, statement:pr.s},
    key_points:[tp.b, pr.n+': '+pr.s, 'Application: '+use, 'Ladder rank '+rank+'/6'],
    src:'generator-sample', sample:true,
    disclaimer:'Generated sample record - not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:'python',language:'python',program:'# JAH Fundamentals of Sleep Science demo\n# Record '+id+' — '+tp.t.replace(/\n/g,' ')+'\nprint("record jahdb-fundamental-sleep-science-1.0")\nprint("OK: '+id+' generated fundamental record")\n',note:'Generator sample demo.'},
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
var gen={version:"jahdb-fundamental-sleep-science-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("fundamental-sleep-science",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
