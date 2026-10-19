(function(){'use strict';
/* JAH Fundamentals of Pedagogy Database generator — jahdb-fundamental-pedagogy-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic fundamental record generation: pick a field, set a seed, get a complete record.
   Same seed + same field = same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-PED-";
var FIELDS=["learning science", "memory", "motivation", "lesson design", "assessment", "classroom management"];
var TOPICS=[
    {t: "How Memory Works", b: "Encoding, storage, retrieval: learning is durable change in long-term memory, and every technique serves those three stages."},
    {t: "Working Memory Limits", b: "Working memory holds about four chunks: novices drown in unchunked detail, so segment and scaffold."},
    {t: "The Testing Effect", b: "Retrieval practice \u2014 low-stakes quizzes \u2014 is the most powerful study technique known, beating re-reading by wide margins."},
    {t: "Spacing and Interleaving", b: "Distributed practice and mixed problem sets build durable, flexible knowledge; blocked cramming builds illusions."},
    {t: "Elaboration and Dual Coding", b: "Explaining ideas in your own words and pairing words with visuals create multiple retrieval routes."},
    {t: "Motivation: Autonomy, Mastery, Purpose", b: "Self-determination theory: people persist when they feel choice, growing competence, and meaningful purpose."},
    {t: "Growth Mindset, Carefully", b: "Believing ability can grow helps when paired with strategies and feedback \u2014 praise effort's process, not empty slogans."},
    {t: "Formative Assessment", b: "Frequent low-stakes checks reveal misconceptions while there's still time to fix them \u2014 assessment for learning, not just of it."},
    {t: "Feedback That Works", b: "Specific, timely, actionable, and focused on the task (not the person): feedback closes the gap between current and goal performance."},
    {t: "Lesson Architecture", b: "Hook, direct instruction in small steps, guided practice, independent practice, review \u2014 the skeleton of an effective lesson."},
    {t: "Differentiation", b: "Same goals, multiple paths: tiered tasks and flexible grouping meet varied readiness without tracking students permanently."},
    {t: "Classroom Management", b: "Routines, clear expectations, and high engagement prevent most misbehavior \u2014 management is mostly design, not discipline."}
];
var PRINCIPLES=[
    {n: "Testing effect", e: "retrieval > restudy", s: "Actively recalling material strengthens memory far more than re-reading it."},
    {n: "Spacing effect", e: "distributed > massed practice", s: "Spreading study over time beats cramming for durable learning."},
    {n: "Cognitive load", e: "working memory \u2248 4 chunks", s: "Instruction must respect the narrow bottleneck of working memory."}
];
var USES=["Designing school lessons", "Building corporate training", "Writing effective textbooks", "Tutoring struggling students"];
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
    id:id, t:tp.t, g:field, name:"Pedagogy"+': '+tp.t, title:tp.t,
    description:desc, edition: seed%2 ? 'signature' : 'public',
    ladder_rank:rank, field:field,
    principle:{name:pr.n, equation:pr.e, statement:pr.s},
    key_points:[tp.b, pr.n+': '+pr.s, 'Application: '+use, 'Ladder rank '+rank+'/6'],
    src:'generator-sample', sample:true,
    disclaimer:'Generated sample record - not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:'python',language:'python',program:'# JAH Fundamentals of Pedagogy demo\n# Record '+id+' — '+tp.t.replace(/\n/g,' ')+'\nprint("record jahdb-fundamental-pedagogy-1.0")\nprint("OK: '+id+' generated fundamental record")\n',note:'Generator sample demo.'},
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
var gen={version:"jahdb-fundamental-pedagogy-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("fundamental-pedagogy",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
