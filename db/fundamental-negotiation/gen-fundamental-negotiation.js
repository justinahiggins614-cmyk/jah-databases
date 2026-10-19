(function(){'use strict';
/* JAH Fundamentals of Negotiation Database generator — jahdb-fundamental-negotiation-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic fundamental record generation: pick a field, set a seed, get a complete record.
   Same seed + same field = same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-NEG-";
var FIELDS=["preparation", "interests vs positions", "BATNA", "value creation", "tactics", "multi-party deals"];
var TOPICS=[
    {t: "Positions vs Interests", b: "Positions are demands ('$50k'); interests are needs behind them (security, recognition) \u2014 interests unlock trades positions block."},
    {t: "BATNA: Your Walk-Away Power", b: "The best alternative to agreement determines leverage: strengthen your BATNA before the table and you negotiate from power."},
    {t: "The ZOPA", b: "The zone of possible agreement lies between reservation points; no overlap means no deal without changing the alternatives."},
    {t: "Creating Value First", b: "Logrolling \u2014 trading what you value less for what you value more \u2014 expands the pie before anyone divides it."},
    {t: "Claiming Value Fairly", b: "Anchoring, bracketing, and principled concessions divide the pie; objective criteria (market data, precedent) depersonalize the split."},
    {t: "Information Is Leverage", b: "Who knows whose deadline and alternatives holds power: ask questions, test assumptions, and reveal selectively."},
    {t: "Hardball Tactics and Defenses", b: "Good-cop/bad-cop, nibbling, and exploding offers all have counters: name the tactic, pause, and return to interests."},
    {t: "Emotion at the Table", b: "Anger extracts concessions but poisons implementation; preparation rituals and caucuses keep feelings from deciding."},
    {t: "Cross-Cultural Negotiation", b: "Direct vs indirect styles, relationship vs contract emphasis, and time horizons differ \u2014 adapt without abandoning interests."},
    {t: "Multi-Party Negotiations", b: "Coalitions, voting rules, and sequencing dominate: build the winning coalition before the final session, not during it."},
    {t: "Agents and Principals", b: "Negotiating through lawyers or brokers adds agency risk: align incentives and authority limits explicitly."},
    {t: "Implementation and Compliance", b: "The best-signed deal fails without monitoring, milestones, and relationship repair clauses \u2014 negotiate the after, not just the now."}
];
var PRINCIPLES=[
    {n: "ZOPA", e: "zone between reservation points", s: "Agreement is possible exactly where the buyer's max exceeds the seller's min."},
    {n: "BATNA rule", e: "never accept worse than your BATNA", s: "Your best alternative sets the walk-away line \u2014 improve it and every deal improves."},
    {n: "Pareto frontier", e: "no joint gains left unclaimed", s: "Efficient deals sit on the frontier where neither side can gain without the other losing."}
];
var USES=["Negotiating salaries and contracts", "Settling business disputes", "Buying companies and assets", "Resolving workplace conflicts"];
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
    id:id, t:tp.t, g:field, name:"Negotiation"+': '+tp.t, title:tp.t,
    description:desc, edition: seed%2 ? 'signature' : 'public',
    ladder_rank:rank, field:field,
    principle:{name:pr.n, equation:pr.e, statement:pr.s},
    key_points:[tp.b, pr.n+': '+pr.s, 'Application: '+use, 'Ladder rank '+rank+'/6'],
    src:'generator-sample', sample:true,
    disclaimer:'Generated sample record - not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:'python',language:'python',program:'# JAH Fundamentals of Negotiation demo\n# Record '+id+' — '+tp.t.replace(/\n/g,' ')+'\nprint("record jahdb-fundamental-negotiation-1.0")\nprint("OK: '+id+' generated fundamental record")\n',note:'Generator sample demo.'},
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
var gen={version:"jahdb-fundamental-negotiation-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("fundamental-negotiation",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
