(function(){'use strict';
/* JAH Fundamentals of Decision Theory Database generator — jahdb-fundamental-decision-theory-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic fundamental record generation: pick a field, set a seed, get a complete record.
   Same seed + same field = same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-DT-";
var FIELDS=["rational choice", "expected utility", "Bayesian reasoning", "risk attitudes", "multi-criteria decisions", "decisions under deep uncertainty"];
var TOPICS=[
    {t: "Decisions as Lotteries", b: "Formalize options as probability distributions over outcomes: once written down, choices become comparable mathematics."},
    {t: "Expected Value First", b: "Multiply outcomes by probabilities and sum: the baseline that beats gut feel for repeated, symmetric risks."},
    {t: "Expected Utility and Risk Attitude", b: "Diminishing marginal utility makes rational agents risk-averse over wealth \u2014 insurance and diversification follow."},
    {t: "Bayes' Rule: Updating Beliefs", b: "New evidence multiplies prior odds by the likelihood ratio: the uniquely coherent way to learn from data."},
    {t: "Base-Rate Neglect", b: "Even experts forget priors: a 99%-accurate test for a 1-in-10,000 condition still yields mostly false positives."},
    {t: "Value of Information", b: "Information is worth what it changes: compute expected gain from a test before paying for it \u2014 sometimes ignorance is optimal."},
    {t: "Decision Trees", b: "Chance nodes, decision nodes, payoffs: trees make sequential choices (test, then treat) computable by backward induction."},
    {t: "Sensitivity Analysis", b: "Vary the uncertain inputs and watch the decision flip: robust choices survive wide input ranges."},
    {t: "Multi-Criteria Decisions", b: "Weight and score competing objectives (cost, safety, speed) explicitly \u2014 hidden weights still decide, so write them down."},
    {t: "Decisions Under Deep Uncertainty", b: "No probabilities? Use maximin, minimax regret, or robust satisficing \u2014 choose what fails gracefully across futures."},
    {t: "Group Decisions and Voting", b: "Aggregating judgments invites paradoxes (Condorcet cycles); structured methods (Delphi, prediction markets) tame them."},
    {t: "Calibrating Judgment", b: "Track predictions against outcomes, score with Brier rules, and shrink overconfidence \u2014 calibration is a trainable skill."}
];
var PRINCIPLES=[
    {n: "Expected value", e: "EV = \u03a3 p_i \u00b7 x_i", s: "Probability-weighted outcomes: the baseline rule for risky choice."},
    {n: "Bayes' rule", e: "P(H|E) = P(E|H)\u00b7P(H)/P(E)", s: "Beliefs update by multiplying prior odds with the likelihood ratio of new evidence."},
    {n: "Maximin", e: "choose max over options of min payoff", s: "When probabilities are unknown, maximize the worst case \u2014 Wald's cautious rule."}
];
var USES=["Evaluating medical test-and-treat options", "Pricing insurance and warranties", "Siting facilities under uncertainty", "Calibrating expert forecasts"];
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
    id:id, t:tp.t, g:field, name:"Decision Theory"+': '+tp.t, title:tp.t,
    description:desc, edition: seed%2 ? 'signature' : 'public',
    ladder_rank:rank, field:field,
    principle:{name:pr.n, equation:pr.e, statement:pr.s},
    key_points:[tp.b, pr.n+': '+pr.s, 'Application: '+use, 'Ladder rank '+rank+'/6'],
    src:'generator-sample', sample:true,
    disclaimer:'Generated sample record - not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:'python',language:'python',program:'# JAH Fundamentals of Decision Theory demo\n# Record '+id+' — '+tp.t.replace(/\n/g,' ')+'\nprint("record jahdb-fundamental-decision-theory-1.0")\nprint("OK: '+id+' generated fundamental record")\n',note:'Generator sample demo.'},
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
var gen={version:"jahdb-fundamental-decision-theory-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("fundamental-decision-theory",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
