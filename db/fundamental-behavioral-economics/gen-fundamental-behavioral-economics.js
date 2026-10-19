(function(){'use strict';
/* JAH Fundamentals of Behavioral Economics Database generator — jahdb-fundamental-behavioral-economics-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic fundamental record generation: pick a field, set a seed, get a complete record.
   Same seed + same field = same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-BE-";
var FIELDS=["heuristics and biases", "prospect theory", "time and self-control", "social preferences", "choice architecture", "behavioral policy"];
var TOPICS=[
    {t: "Homo Economicus vs Humans", b: "Classical economics assumes perfect rationality; behavioral economics documents the systematic, predictable ways real people deviate."},
    {t: "Heuristics: Fast Thinking", b: "Availability, representativeness, and anchoring are mental shortcuts \u2014 efficient, but reliably biased in predictable directions."},
    {t: "Loss Aversion", b: "Losses loom about twice as large as gains: it explains the endowment effect, status-quo bias, and why selling losers hurts."},
    {t: "Prospect Theory", b: "Kahneman and Tversky's value function \u2014 reference-dependent, loss-averse, diminishing sensitivity \u2014 predicts risky choice far better than utility theory."},
    {t: "Framing Effects", b: "'90% survival' vs '10% mortality' describe the same surgery but change choices: presentation constructs preference."},
    {t: "Present Bias and Procrastination", b: "We overweight now versus later, then regret it: commitment devices (automatic savings, deadlines) are the engineered fix."},
    {t: "Mental Accounting", b: "People bucket money (rent jar, fun jar) and treat identical dollars differently \u2014 irrational, but design can work with it."},
    {t: "Defaults: The Power of Pre-Set", b: "Auto-enrollment in retirement plans lifts participation from ~50% to ~90%: the default is the most powerful choice architect."},
    {t: "Social Norms and Nudges", b: "'Your neighbors use less energy' letters cut consumption; nudges steer without banning \u2014 libertarian paternalism in action."},
    {t: "Fairness and Ultimatum Games", b: "People reject unfair splits even at personal cost: reciprocity and punishment instincts shape markets and negotiations."},
    {t: "Overconfidence", b: "Most drivers rate themselves above average; overconfidence inflates trading, entrepreneurship failure, and planning fallacies."},
    {t: "Behavioral Policy Design", b: "From organ-donor defaults to simplified tax forms, governments now design with biases in mind \u2014 tested by randomized trials."}
];
var PRINCIPLES=[
    {n: "Prospect theory value", e: "v(x): concave gains, convex losses, steeper losses", s: "Losses hurt ~2\u00d7 more than equal gains please \u2014 loss aversion quantified."},
    {n: "Present bias", e: "\u03b2\u00b7\u03b4^t discounting", s: "Hyperbolic-like discounting makes 'later' collapse against 'now' \u2014 the math of procrastination."},
    {n: "Expected utility violation", e: "Allais paradox choices", s: "Real choices systematically break expected-utility axioms, motivating the whole field."}
];
var USES=["Designing retirement savings plans", "Reducing energy consumption", "Improving tax compliance", "Building better choice interfaces"];
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
    id:id, t:tp.t, g:field, name:"Behavioral Economics"+': '+tp.t, title:tp.t,
    description:desc, edition: seed%2 ? 'signature' : 'public',
    ladder_rank:rank, field:field,
    principle:{name:pr.n, equation:pr.e, statement:pr.s},
    key_points:[tp.b, pr.n+': '+pr.s, 'Application: '+use, 'Ladder rank '+rank+'/6'],
    src:'generator-sample', sample:true,
    disclaimer:'Generated sample record - not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:'python',language:'python',program:'# JAH Fundamentals of Behavioral Economics demo\n# Record '+id+' — '+tp.t.replace(/\n/g,' ')+'\nprint("record jahdb-fundamental-behavioral-economics-1.0")\nprint("OK: '+id+' generated fundamental record")\n',note:'Generator sample demo.'},
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
var gen={version:"jahdb-fundamental-behavioral-economics-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("fundamental-behavioral-economics",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
