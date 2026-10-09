(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function ri(r,a,b){return a+((r()*(b-a+1))|0);}
function pad6(n){return String(n).padStart(6,'0');}

var CATS=['beginner','intermediate','expert'];

var BANK=[
 {archetype:'Weekend Gardener',expertise:'beginner',
  goals:['Grow tomatoes on a small balcony','Keep houseplants alive through winter','Learn composting basics'],
  style:'Encouraging, plain language, step-by-step instructions, no jargon.',
  queries:['Why are my tomato leaves turning yellow?','How often should I water a pothos?','What is the easiest compost setup for an apartment?']},
 {archetype:'First-Time Home Buyer',expertise:'beginner',
  goals:['Understand mortgage terminology','Save for a down payment','Avoid common buying mistakes'],
  style:'Patient explainer, defines every term, uses concrete dollar examples.',
  queries:['What is the difference between APR and interest rate?','How much should I save for closing costs?','What is PMI and how do I avoid it?']},
 {archetype:'Casual Fitness Starter',expertise:'beginner',
  goals:['Build a sustainable 3-day workout routine','Learn proper form for basic lifts','Eat enough protein on a budget'],
  style:'Motivating but honest, short routines, safety-first cues.',
  queries:['What is a good beginner full-body workout?','How do I squat without hurting my knees?','How much protein do I need per day?']},
 {archetype:'New Parent',expertise:'beginner',
  goals:['Establish a baby sleep routine','Understand feeding schedules','Find trustworthy pediatric guidance'],
  style:'Warm, reassuring, evidence-based, never alarmist.',
  queries:['How many naps does a 6-month-old need?','Is it normal for a newborn to sleep 5 hours straight?','When should I call the pediatrician about a fever?']},
 {archetype:'Junior Python Developer',expertise:'intermediate',
  goals:['Write cleaner, more testable code','Understand async programming','Prepare for a mid-level interview'],
  style:'Code-first answers with runnable examples and brief explanations.',
  queries:['When should I use async/await in Python?','How do I structure a medium-size Flask project?','What are Python decorators really doing?']},
 {archetype:'Small Business Owner',expertise:'intermediate',
  goals:['Track cash flow monthly','Price products for sustainable margins','Hire the first employee'],
  style:'Practical, numbers-driven, short action lists.',
  queries:['How do I build a simple cash-flow spreadsheet?','What margin should I target on handmade goods?','What paperwork do I need to hire someone?']},
 {archetype:'Amateur Photographer',expertise:'intermediate',
  goals:['Master manual exposure','Build a coherent portfolio','Learn off-camera flash'],
  style:'Visual and technical, with settings examples for real scenes.',
  queries:['What settings for sharp indoor sports photos?','How do I balance flash with ambient light?','How many photos should a portfolio have?']},
 {archetype:'Data Analyst',expertise:'intermediate',
  goals:['Automate weekly reporting','Learn window functions in SQL','Tell clearer stories with dashboards'],
  style:'Precise, shows queries and formulas, warns about pitfalls.',
  queries:['How do window functions differ from GROUP BY?','How do I automate a weekly Excel report?','What makes a dashboard actually readable?']},
 {archetype:'Language Learner (Spanish)',expertise:'intermediate',
  goals:['Hold a 10-minute conversation','Master the subjunctive','Understand fast native speech'],
  style:'Bilingual examples, gentle corrections, cultural notes.',
  queries:['When do I use the subjunctive in Spanish?','How can I understand fast native speakers?','What is the difference between por and para?']},
 {archetype:'Indie Game Developer',expertise:'intermediate',
  goals:['Ship a first playable prototype','Learn 2D physics basics','Market a game with no budget'],
  style:'Builder mindset, concrete tools and workflows, honest about scope.',
  queries:['How do I scope a game I can finish in 3 months?','What is a simple 2D collision approach?','How do indies market games for free?']},
 {archetype:'DevOps Engineer',expertise:'expert',
  goals:['Cut deployment time under 10 minutes','Design multi-region failover','Reduce cloud spend 20 percent'],
  style:'Terse, assumes fundamentals, cites real tooling and metrics.',
  queries:['How do I debug a slow Kubernetes rollout?','What is the cheapest multi-region failover pattern?','How do I right-size overprovisioned nodes?']},
 {archetype:'Machine Learning Researcher',expertise:'expert',
  goals:['Reproduce a recent paper faithfully','Design an ablation study','Write a clear methods section'],
  style:'Rigorous, notation-heavy, points to primary sources.',
  queries:['How do I run a proper ablation study?','What details belong in a reproducibility checklist?','How should I report confidence intervals?']},
 {archetype:'Tax Accountant',expertise:'expert',
  goals:['Stay current on code changes','Optimize a client\'s entity structure','Survive busy season efficiently'],
  style:'Citation-driven, precise, flags jurisdictional differences.',
  queries:['How did the latest code change affect pass-through deductions?','LLC vs S-corp for a freelancer in 2026?','What triggers an audit most often?']},
 {archetype:'Emergency Room Physician',expertise:'expert',
  goals:['Triage faster under pressure','Keep up with protocol updates','Communicate clearly with families'],
  style:'Clinical, protocol-oriented, prioritizes patient safety.',
  queries:['What is the current sepsis bundle protocol?','How do I break bad news efficiently and kindly?','Which stroke scale is fastest at triage?']},
 {archetype:'Patent Attorney',expertise:'expert',
  goals:['Draft bulletproof independent claims','Navigate office actions strategically','Advise on international filing'],
  style:'Formal, claim-focused, distinguishes jurisdictions.',
  queries:['How broad can an independent claim be without prior art risk?','What is the best response to a 103 rejection?','When should I file a PCT application?']},
 {archetype:'Structural Engineer',expertise:'expert',
  goals:['Verify load paths on a retrofit','Specify seismic detailing','Review a peer\'s calculations'],
  style:'Numbers first, code references, safety margins explicit.',
  queries:['How do I check a beam for lateral-torsional buckling?','What seismic detailing does this frame need?','How do I validate a finite-element model?']},
 {archetype:'Retired History Buff',expertise:'intermediate',
  goals:['Trace family genealogy','Understand the causes of WWI','Plan a history-themed trip'],
  style:'Story-driven, dates and sources included, recommends books.',
  queries:['Where do I start tracing my family tree?','What really caused World War I?','What are the best Roman sites to visit in Italy?']},
 {archetype:'High School Science Teacher',expertise:'intermediate',
  goals:['Design engaging lab activities','Explain abstract concepts simply','Manage a mixed-ability classroom'],
  style:'Classroom-ready, demos and analogies, standards-aware.',
  queries:['What is a safe, impressive chemistry demo?','How do I explain entropy to 15-year-olds?','How do I differentiate a physics lesson?']}
];

function generate(seed,opts,rnd){
  rnd=rnd||prng(seed);
  var pool=BANK;
  if(opts&&opts.category&&CATS.indexOf(opts.category)>=0){
    var f=BANK.filter(function(p){return p.expertise===opts.category;});
    if(f.length)pool=f;
  }
  var p=pool[ri(rnd,0,pool.length-1)];
  var id='JAH-PERSONA-'+pad6(seed);
  return {id:id,persona_id:id,archetype:p.archetype,goals:p.goals.slice(),
    expertise:p.expertise,preferred_style:p.style,example_queries:p.queries.slice(),title:p.archetype};
}

function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  if(!/^JAH-PERSONA-\d{6}$/.test(r.id))e.push('id');
  if(r.persona_id!==r.id)e.push('persona_id');
  if(typeof r.archetype!=='string'||!r.archetype.length||r.archetype.length>600)e.push('archetype');
  if(!Array.isArray(r.goals)||r.goals.length<2||r.goals.length>4)e.push('goals');
  if(CATS.indexOf(r.expertise)<0)e.push('expertise');
  if(typeof r.preferred_style!=='string'||!r.preferred_style.length||r.preferred_style.length>600)e.push('preferred_style');
  if(!Array.isArray(r.example_queries)||r.example_queries.length<2||r.example_queries.length>3)e.push('example_queries');
  if(r.title!==r.archetype)e.push('title');
  return {ok:!e.length,errors:e};
}

var gen={version:'jahdb-persona-profiles-1.0',generate:generate,validate:validate};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('persona-profiles',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
