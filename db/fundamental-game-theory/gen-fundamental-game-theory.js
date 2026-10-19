(function(){'use strict';
/* JAH Fundamentals of Game Theory Database generator — jahdb-fundamental-game-theory-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic fundamental record generation: pick a field, set a seed, get a complete record.
   Same seed + same field = same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-GT-";
var FIELDS=["games and strategies", "Nash equilibrium", "cooperation", "auctions", "voting and social choice", "mechanism design"];
var TOPICS=[
    {t: "What Is a Game", b: "A game is players, strategies, and payoffs: the mathematics applies equally to chess, price wars, evolution, and traffic."},
    {t: "Zero-Sum Games", b: "In strictly opposed games one player's gain is the other's loss; minimax strategies guarantee the best worst-case outcome."},
    {t: "The Prisoner's Dilemma", b: "Individual rationality drives both players to defect even though cooperation pays more \u2014 the canonical model of failed cooperation."},
    {t: "Nash Equilibrium", b: "A Nash equilibrium is a mutual best-response: no one gains by changing alone. It predicts stable outcomes but not necessarily good ones."},
    {t: "Repeated Games and Trust", b: "Repeating the prisoner's dilemma enables cooperation: tit-for-tat thrives because defection today invites retaliation tomorrow."},
    {t: "Mixed Strategies", b: "Randomizing between options (like a goalkeeper guessing dive direction) makes opponents unable to exploit predictable patterns."},
    {t: "Auctions as Games", b: "English, Dutch, sealed-bid, and Vickrey auctions are games whose rules determine revenue; the second-price auction makes truthful bidding optimal."},
    {t: "The Winner's Curse", b: "Winning a common-value auction often means overpaying \u2014 the winner is whoever most overestimated the value, a systematic trap."},
    {t: "Voting and Social Choice", b: "Arrow's impossibility theorem proves no voting system satisfies all fairness criteria simultaneously; every method has a flaw."},
    {t: "Bargaining and Fair Division", b: "Nash bargaining and cut-and-choose protocols show how rational parties split surplus and cake without envy."},
    {t: "Signaling and Information", b: "Costly signals (degrees, warranties, peacock tails) credibly convey hidden information precisely because faking them is expensive."},
    {t: "Mechanism Design", b: "Instead of analyzing games, design them: set rules so self-interested play produces the outcome you want \u2014 markets, matching, and kidney exchanges."}
];
var PRINCIPLES=[
    {n: "Nash equilibrium", e: "no player can gain by deviating alone", s: "A strategy profile is stable exactly when unilateral deviation never pays."},
    {n: "Minimax (zero-sum)", e: "value = max_min = min_max", s: "In strictly opposed games, optimal play guarantees the same value to both sides."},
    {n: "Expected utility", e: "U = \u03a3 p_i \u00b7 u_i", s: "Rational choice maximizes probability-weighted utility."}
];
var USES=["Designing spectrum and ad auctions", "Setting competitive pricing strategy", "Building stable matching markets", "Analyzing arms races and treaties"];
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
    id:id, t:tp.t, g:field, name:"Game Theory"+': '+tp.t, title:tp.t,
    description:desc, edition: seed%2 ? 'signature' : 'public',
    ladder_rank:rank, field:field,
    principle:{name:pr.n, equation:pr.e, statement:pr.s},
    key_points:[tp.b, pr.n+': '+pr.s, 'Application: '+use, 'Ladder rank '+rank+'/6'],
    src:'generator-sample', sample:true,
    disclaimer:'Generated sample record - not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:'python',language:'python',program:'# JAH Fundamentals of Game Theory demo\n# Record '+id+' — '+tp.t.replace(/\n/g,' ')+'\nprint("record jahdb-fundamental-game-theory-1.0")\nprint("OK: '+id+' generated fundamental record")\n',note:'Generator sample demo.'},
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
var gen={version:"jahdb-fundamental-game-theory-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("fundamental-game-theory",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
