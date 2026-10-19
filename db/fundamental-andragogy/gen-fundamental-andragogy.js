(function(){'use strict';
/* JAH Fundamentals of Andragogy Database generator — jahdb-fundamental-andragogy-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic fundamental record generation: pick a field, set a seed, get a complete record.
   Same seed + same field = same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-AND-";
var FIELDS=["adult learning principles", "self-direction", "experience as resource", "motivation", "training design", "workplace learning"];
var TOPICS=[
    {t: "Andragogy vs Pedagogy", b: "Knowles' insight: adults bring self-concept, experience, readiness tied to roles, and problem-centered orientation \u2014 teach accordingly."},
    {t: "Self-Directed Learning", b: "Adults learn best when they set goals, choose resources, and pace themselves; the trainer becomes a facilitator and coach."},
    {t: "Experience as Curriculum", b: "Decades of work experience are the richest textbook: case discussions, peer teaching, and reflection harvest it."},
    {t: "Readiness to Learn", b: "Adults engage when facing real transitions \u2014 promotions, new systems, new regulations: timing training to need multiplies impact."},
    {t: "Problem-Centered Design", b: "Organize around problems ('close the month faster'), not subjects ('accounting chapter 4') \u2014 adults learn to solve, not to know."},
    {t: "Intrinsic Motivation", b: "Autonomy, mastery, and purpose drive adult learners more than grades or certificates \u2014 design for the inner game."},
    {t: "The 70-20-10 Framework", b: "Stretch assignments (70), mentoring (20), and formal courses (10) together build capability; courses alone never do."},
    {t: "Microlearning", b: "Short, focused, just-in-time modules fit workdays and memory: five sharp minutes beat fifty foggy ones."},
    {t: "Feedback and Coaching", b: "Adults accept critique tied to their goals from credible peers; coaching conversations outperform lecture corrections."},
    {t: "Transfer of Training", b: "Learning dies without application: action plans, manager support, and follow-up determine whether training changes behavior."},
    {t: "Assessing Adult Learning", b: "Portfolios, demonstrations, and on-the-job metrics beat multiple-choice for proving real capability."},
    {t: "Learning Organizations", b: "After-action reviews, knowledge sharing, and psychological safety turn companies into places where adults keep learning."}
];
var PRINCIPLES=[
    {n: "Self-direction principle", e: "adults need control of learning", s: "Treating adults like children in training triggers resistance; autonomy unlocks engagement."},
    {n: "Relevance filter", e: "learning \u221d perceived job relevance", s: "Adults invest effort in proportion to how clearly learning solves their real problems."},
    {n: "70-20-10 model", e: "experience/social/formal", s: "Roughly 70% of workplace capability comes from doing, 20% from others, 10% from courses."}
];
var USES=["Designing corporate training programs", "Onboarding new employees", "Building apprenticeship systems", "Coaching professional development"];
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
    id:id, t:tp.t, g:field, name:"Andragogy"+': '+tp.t, title:tp.t,
    description:desc, edition: seed%2 ? 'signature' : 'public',
    ladder_rank:rank, field:field,
    principle:{name:pr.n, equation:pr.e, statement:pr.s},
    key_points:[tp.b, pr.n+': '+pr.s, 'Application: '+use, 'Ladder rank '+rank+'/6'],
    src:'generator-sample', sample:true,
    disclaimer:'Generated sample record - not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:'python',language:'python',program:'# JAH Fundamentals of Andragogy demo\n# Record '+id+' — '+tp.t.replace(/\n/g,' ')+'\nprint("record jahdb-fundamental-andragogy-1.0")\nprint("OK: '+id+' generated fundamental record")\n',note:'Generator sample demo.'},
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
var gen={version:"jahdb-fundamental-andragogy-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("fundamental-andragogy",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
