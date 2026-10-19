(function(){'use strict';
/* JAH Fundamentals of Rhetoric Database generator — jahdb-fundamental-rhetoric-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic fundamental record generation: pick a field, set a seed, get a complete record.
   Same seed + same field = same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-RHE-";
var FIELDS=["the rhetorical triangle", "invention", "arrangement", "style", "memory and delivery", "argumentation"];
var TOPICS=[
    {t: "What Rhetoric Is", b: "Rhetoric is the art of discovering the available means of persuasion in any situation \u2014 Aristotle's definition, still the best."},
    {t: "Ethos: Character Persuades", b: "Audiences believe speakers they judge competent, honest, and benevolent: credibility is built before the argument starts."},
    {t: "Pathos: Emotion Moves", b: "Stories, vivid detail, and shared values move audiences to act \u2014 emotion is the engine, logic the steering."},
    {t: "Logos: Reason Convinces", b: "Evidence, statistics, and valid inference earn the mind's assent; without logos, persuasion is manipulation."},
    {t: "Invention: Finding Arguments", b: "Topoi (topics) are argument search patterns \u2014 definition, comparison, cause, testimony \u2014 the brainstorming system of rhetoric."},
    {t: "Arrangement: Structure", b: "Exordium, narration, proof, refutation, peroration: classical speeches follow an architecture refined over two millennia."},
    {t: "Style: Saying It Well", b: "Clarity, vividness, and rhythm: tropes (metaphor) and schemes (parallelism) make language memorable and moving."},
    {t: "Figures That Stick", b: "Anaphora, antithesis, and the rule of three pattern sound for memory \u2014 the devices behind history's quoted lines."},
    {t: "Refutation", b: "Steel-manning the opponent's best case before dismantling it is both honest and devastating \u2014 the strongest defensive move."},
    {t: "Kairos: Timing", b: "The right argument at the wrong moment fails: reading the audience's readiness is a rhetorical skill, not luck."},
    {t: "Delivery: Voice and Body", b: "Pace, pause, gesture, and eye contact carry meaning beyond words \u2014 delivery can double or halve a speech's force."},
    {t: "Rhetoric vs Sophistry", b: "Persuasion serves truth when arguments are checkable and audiences free; manipulation hides premises and blocks exit."}
];
var PRINCIPLES=[
    {n: "Rhetorical triangle", e: "ethos \u00d7 pathos \u00d7 logos", s: "Persuasion needs credibility, emotion, and logic together \u2014 weakness in one sinks the other two."},
    {n: "Syllogism", e: "major + minor premise \u2192 conclusion", s: "Deductive argument structure: if premises hold, the conclusion is inescapable."},
    {n: "Enthymeme", e: "argument with an unstated premise", s: "Everyday persuasion omits the obvious premise \u2014 and opponents attack exactly there."}
];
var USES=["Writing persuasive speeches", "Structuring legal arguments", "Crafting marketing messages", "Teaching critical thinking"];
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
    id:id, t:tp.t, g:field, name:"Rhetoric"+': '+tp.t, title:tp.t,
    description:desc, edition: seed%2 ? 'signature' : 'public',
    ladder_rank:rank, field:field,
    principle:{name:pr.n, equation:pr.e, statement:pr.s},
    key_points:[tp.b, pr.n+': '+pr.s, 'Application: '+use, 'Ladder rank '+rank+'/6'],
    src:'generator-sample', sample:true,
    disclaimer:'Generated sample record - not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:'python',language:'python',program:'# JAH Fundamentals of Rhetoric demo\n# Record '+id+' — '+tp.t.replace(/\n/g,' ')+'\nprint("record jahdb-fundamental-rhetoric-1.0")\nprint("OK: '+id+' generated fundamental record")\n',note:'Generator sample demo.'},
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
var gen={version:"jahdb-fundamental-rhetoric-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("fundamental-rhetoric",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
