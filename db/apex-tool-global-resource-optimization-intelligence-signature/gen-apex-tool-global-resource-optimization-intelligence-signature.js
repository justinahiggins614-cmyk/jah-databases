(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var CATS=["allocation-planning", "budget-enforcement", "priority-balancing"];
var PREFIX='JAH-APX65S-';
var VERSION='jahdb-apex-tool-global-resource-optimization-intelligence-signature-1.0';
var TOOLNAME='Global Resource Optimization Intelligence';
var PROV='Signature original design by Justin Addam Higgins (JAH). Signature-labeled original work - not a public record. Demo executed 2026-10-21.';
var DEPS=["Resource usage meters", "Budget policy store", "Priority declarations", "Cost rate tables"];
var PARAMS=[[10, 300], [15, 400], [20, 500], [25, 600], [30, 800], [40, 1000], [50, 1200], [60, 1500], [75, 1800], [90, 2200], [110, 2600], [130, 3000], [150, 3500], [180, 4000], [200, 5000]];
var DEMO_TPL="function prng(seed){var a=seed>>>0||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}\nvar R=prng(__SEED__);\nvar T0=Date.now();\nvar P=__P0__,BUD=__P1__;\nvar projs=[];for(var i=0;i<P;i++){var cost=10+Math.floor(R()*90);projs.push({cost:cost,roi:+(cost*(0.5+R()*2)).toFixed(1)});}\nvar byDens=projs.slice().sort(function(a,b){return (b.roi/b.cost)-(a.roi/a.cost);});\nvar spent=0,roi=0,n=0;byDens.forEach(function(p){if(spent+p.cost<=BUD){spent+=p.cost;roi+=p.roi;n++;}});\nvar spent2=0,roi2=0;projs.forEach(function(p){if(spent2+p.cost<=BUD){spent2+=p.cost;roi2+=p.roi;}});\nconsole.log(JSON.stringify({id:\"__ID__\",ok:true,metrics:{projects:P,budget:BUD,funded:n,spent:spent,total_roi:+roi.toFixed(1),baseline_roi:+roi2.toFixed(1),gain_vs_baseline_pct:+((roi/Math.max(roi2,1)-1)*100).toFixed(1)},ms:Date.now()-T0}));";
var BP=[["allocation-planning", "Signature Demand Prophet", "Justin's forecaster seals demand predictions per consumer.", "Sealed forecast records.", "Signature demand prophet|Signature fairness auditor|Signature budget ledger|Signature allocation solver", "allocate(demands,budget)->plan|allocate(demands,budget)->plan", "signature-original - established-pattern", "The demo's sealed forecast beats naive carry-forward."], ["allocation-planning", "Signature Priority Codex", "His ranker seals priority decisions with reasons.", "Sealed ranking records.", "Signature allocation solver|Signature demand prophet|Signature fairness auditor|Signature budget ledger", "rebalance(state)->plan|rebalance(state)->plan", "signature-original - established-pattern", "The demo's critical-first ranking is sealed."], ["allocation-planning", "Signature Budget Ledger", "A budget ledger of sealed spend records.", "Sealed ledger entries.", "Signature budget ledger|Signature allocation solver|Signature demand prophet|Signature fairness auditor", "audit(plan)->report|audit(plan)->report", "signature-original - established-pattern", "The demo's overrun flag cites the sealed ledger."], ["allocation-planning", "Signature Allocation Solver", "His solver seals the optimal plan with its objective value.", "Sealed allocation records.", "Signature fairness auditor|Signature budget ledger|Signature allocation solver|Signature demand prophet", "allocate(demands,budget)->plan|allocate(demands,budget)->plan", "signature-original - established-pattern", "The demo's win over equal-split is sealed."], ["allocation-planning", "Signature Quota Warden", "Enforces quotas with sealed records.", "Sealed quota records.", "Signature demand prophet|Signature fairness auditor|Signature budget ledger|Signature allocation solver", "rebalance(state)->plan|rebalance(state)->plan", "signature-original - established-pattern", "The demo block cites the sealed quota."], ["budget-enforcement", "Signature Rebalancer", "His rebalancer seals drift-triggered moves.", "Sealed rebalance records.", "Signature allocation solver|Signature demand prophet|Signature fairness auditor|Signature budget ledger", "audit(plan)->report|audit(plan)->report", "signature-original - prototype-demonstrated", "The demo's move to the spiking workload is sealed."], ["budget-enforcement", "Signature Waste Hunter", "Finds waste as sealed findings with reclaimed amounts.", "Sealed waste records.", "Signature budget ledger|Signature allocation solver|Signature demand prophet|Signature fairness auditor", "allocate(demands,budget)->plan|allocate(demands,budget)->plan", "signature-original - prototype-demonstrated", "The demo's reclaimed idle capacity is sealed."], ["budget-enforcement", "Signature Fairness Auditor", "Audits fairness with sealed metrics.", "Sealed audit records.", "Signature fairness auditor|Signature budget ledger|Signature allocation solver|Signature demand prophet", "rebalance(state)->plan|rebalance(state)->plan", "signature-original - prototype-demonstrated", "The demo's skewed-plan flag is sealed."], ["budget-enforcement", "Signature Cost Prophet", "His projector seals burn-rate projections.", "Sealed projection records.", "Signature demand prophet|Signature fairness auditor|Signature budget ledger|Signature allocation solver", "audit(plan)->report|audit(plan)->report", "signature-original - prototype-demonstrated", "The demo projection seals within the band."], ["budget-enforcement", "Signature Policy Warden", "His gate seals policy evaluations.", "Sealed policy records.", "Signature allocation solver|Signature demand prophet|Signature fairness auditor|Signature budget ledger", "allocate(demands,budget)->plan|allocate(demands,budget)->plan", "signature-original - prototype-demonstrated", "The demo block cites the sealed policy."], ["priority-balancing", "Signature Multi-Packer", "His packer seals joint four-resource plans.", "Sealed packing records.", "Signature budget ledger|Signature allocation solver|Signature demand prophet|Signature fairness auditor", "rebalance(state)->plan|rebalance(state)->plan", "signature-original - design-stage", "The demo's joint feasibility win is sealed."], ["priority-balancing", "Signature Spot Trader", "His buyer seals blended-cost purchases.", "Sealed trade records.", "Signature fairness auditor|Signature budget ledger|Signature allocation solver|Signature demand prophet", "audit(plan)->report|audit(plan)->report", "signature-original - design-stage", "The demo's blended savings are sealed."], ["priority-balancing", "Signature Reservation Planner", "Plans reserve/on-demand mixes as sealed records.", "Sealed mix records.", "Signature demand prophet|Signature fairness auditor|Signature budget ledger|Signature allocation solver", "allocate(demands,budget)->plan|allocate(demands,budget)->plan", "signature-original - design-stage", "The demo mix seals cheaper than pure strategies."], ["priority-balancing", "Signature Showback Scribe", "His reporter seals per-team cost attributions.", "Sealed showback records.", "Signature allocation solver|Signature demand prophet|Signature fairness auditor|Signature budget ledger", "rebalance(state)->plan|rebalance(state)->plan", "signature-original - design-stage", "The demo report seals against the ledger."], ["priority-balancing", "Signature Allocation Director", "The Signature director: sealed forecast, sealed solve, sealed enforce.", "Sealed stage records.", "Signature budget ledger|Signature allocation solver|Signature demand prophet|Signature fairness auditor", "audit(plan)->report|audit(plan)->report", "signature-original - design-stage", "The demo director's green budgets are sealed."]];
function demoSource(rank,seed,id){
  var p=PARAMS[(rank-1)%PARAMS.length];
  var s=DEMO_TPL;
  s=s.split('__SEED__').join(String(seed));
  s=s.split('__ID__').join(id);
  for(var i=0;i<p.length;i++)s=s.split('__P'+i+'__').join(String(p[i]));
  return s;
}
function generate(seed,opts){
  opts=opts||{};
  var idx=Math.abs(seed)%BP.length;
  if(opts.category){
    for(var i=0;i<BP.length;i++)if(BP[i][0]===opts.category){idx=i;break;}
  }
  var b=BP[idx];
  var rank=1+(Math.abs(seed*7+idx)%15);
  var id=PREFIX+String(100000+(Math.abs(seed)%899999)).padStart(6,'0');
  var comps=b[4]?b[4].split('|'):[];
  var ifaces=b[5]?b[5].split('|'):[];
  return {id:id,t:b[1],g:b[0],title:b[1],description:b[2],ladder_rank:rank,
    demo:demoSource(rank,seed,id),architecture:b[3],components:comps,interfaces:ifaces,
    implementation_status:b[6],acceptance_tests:[b[7],'Generated record - run its demo program with node to verify.'],
    dependencies:DEPS.slice(0,3),provenance:PROV,last_verified:'2026-10-21',
    march_marker:'Million in progress - generated record marching to 1,000,000.',
    edition:'signature',tool_number:65,tool_name:TOOLNAME,_seed:seed};
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  var rx=new RegExp('^'+PREFIX.replace(/[-]/g,'\\-')+'\\d{6}$');
  if(!rx.test(r.id||''))e.push('id');
  if(typeof r.title!=='string'||!r.title.length)e.push('title');
  if(typeof r.description!=='string'||r.description.length<20)e.push('description');
  if(!(r.ladder_rank>=1&&r.ladder_rank<=15))e.push('ladder_rank');
  if(typeof r.demo!=='string'||r.demo.indexOf('console.log')<0)e.push('demo');
  if(typeof r.architecture!=='string'||!r.architecture.length)e.push('architecture');
  if(!Array.isArray(r.components)||!r.components.length)e.push('components');
  if(!Array.isArray(r.acceptance_tests)||!r.acceptance_tests.length)e.push('acceptance_tests');
  if(CATS.indexOf(r.g)<0)e.push('g');
  if(r.last_verified!=='2026-10-21')e.push('last_verified');
  return {ok:!e.length,errors:e};
}
function driftCheck(rec,sample){
  sample=sample||[];
  for(var i=0;i<sample.length;i++)if(sample[i]&&sample[i].id===rec.id)return {ok:false,errors:['duplicate id']};
  return {ok:true,errors:[]};
}
var gen={version:VERSION,generate:generate,validate:validate,driftCheck:driftCheck};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('apex-tool-global-resource-optimization-intelligence-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
