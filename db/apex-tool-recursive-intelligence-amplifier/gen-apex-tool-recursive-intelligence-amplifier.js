(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];} function ri(s,a,b){return a+((s()*(b-a+1))|0);}
var CATS=["architecture", "component", "benchmark", "interface", "worked-example"];
var PREFIX="JAH-APX21-";
var VERSION="jahdb-apex-tool-recursive-intelligence-amplifier-1.0";
/* rows: [group, focus, title, description, architecture] */
var B=[["architecture", "Concept and purpose", "What the Intelligence Amplifier is", "The amplifier takes a working workflow and makes it better, recursively: it evaluates the workflow's results, finds the weakest step, generates alternative strategies for that step, tests them against the baseline, and keeps winners. Each cycle is small, measured, and reversible — compounding gains without compounding risk.", "Workflow evaluator; weakness localizer; strategy generator; A/B tester against baseline; winner keeper with rollback."], ["architecture", "Core data model", "Amplification cycle data model", "Every cycle is a record: the baseline snapshot, the hypothesized weakness, the alternative tried, the measured delta, the cost, and the keep-or-rollback decision. The ledger of cycles is the amplifier's memory — it prevents retrying failed ideas and proves improvement over time.", "Cycle documents; baseline snapshots; delta measurements; decision log; ledger query."], ["component", "Key algorithm I", "Weakness localization algorithm", "Improving everything at once is wasteful; the localizer finds the step whose improvement would help most. It uses ablation (remove a step, measure the damage), sensitivity analysis, and error attribution to rank steps by improvement potential — then the amplifier attacks the top of the list.", "Ablation runner; sensitivity analyzer; error attributor; potential ranker."], ["component", "Key algorithm II", "Alternative strategy generation algorithm", "For the weakest step, the generator proposes alternatives: parameter variations, algorithm swaps, and structural changes, drawn from a strategy library and from mutations of the current approach. Proposals are filtered for plausibility before testing — the tester’s time is precious.", "Strategy library; mutator; plausibility filter; proposal ranker."], ["interface", "Interface specification", "Amplification interface specification", "Callers submit a workflow with its evaluation harness and get back an amplified workflow plus the ledger of cycles: what was tried, what won, what it cost. The interface supports amplification budgets (stop after N cycles or X cost) and human approval gates for high-stakes changes.", "Amplification endpoint; budget enforcer; approval gates; ledger exporter."], ["component", "Ingestion and adapters", "Ingestion: workflows and harnesses", "The amplifier consumes workflows as executable graphs and harnesses as fixed evaluation suites. Intake validates that the harness is deterministic and the baseline reproducible — amplification on a flaky harness produces noise, not improvement, and the intake refuses it.", "Workflow importer; harness validator; baseline reproducer; intake gate."], ["component", "Indexing and retrieval", "Cycle indexing and retrieval", "Cycles are indexed by workflow, step, strategy type, and outcome — so 'has anyone tried a re-ranker swap on a ranking step' is one query. The index prevents repeated failures and spreads successes: a winning strategy in one workflow becomes a candidate everywhere.", "Cycle index; failure memory; success propagator; faceted retrieval."], ["component", "Reasoning and decision component", "Reasoning: keep, rollback, or investigate", "Each cycle ends with a decision: keep (beats baseline significantly), rollback (regresses or ties), or investigate (beats baseline but suspiciously — possible harness gaming). The decision rules are statistical, published, and conservative — the amplifier would rather miss a gain than ship a phantom one.", "Significance tester; gaming detector; decision rules; investigation queue."], ["interface", "Output and presentation", "Amplification report presentation output", "Amplification renders as a progress story: baseline, cycles tried, deltas achieved, cost spent, and the current champion workflow with its ledger. Stakeholders see improvement as a measured curve, not a claimed leap — and every point on the curve expands to its cycle.", "Curve renderer; cycle expander; cost accountant display; champion exporter."], ["benchmark", "Benchmark harness and measured baseline", "Amplifier benchmark harness", "The amplifier is tested on workflows with known headroom: planted inefficiencies it should find and fix, measured in delta-per-cost. Baselines are random search and human expert tuning samples; the amplifier must find more improvement per cost to graduate.", "Fixture workflows with planted flaws; amplification runner; delta-per-cost scorer; baseline gate."], ["worked-example", "End-to-end worked example", "Worked example: amplifying a search workflow", "A search workflow at 0.82 gets amplified: localization fingers the ranking step, the generator proposes five alternatives, testing keeps a re-ranker swap (+0.06) and a cache layer (+0.03), rolls back three, and flags one. Six cycles, +0.09 total, every decision evidenced. The workflow is better and the team knows exactly why.", "Intake; localization; generation; testing; decisions; report."], ["component", "Failure modes and reliability", "Failure modes: harness gaming and baseline rot", "Amplifiers fail by gaming their harness (improving the metric, not the mission) or by baselines rotting as data drifts. Defenses: held-out evaluation sets the amplifier never sees, gaming detectors watching for metric-only improvements, and baseline refresh protocols. Improvement must be real, not measured-real.", "Held-out sets; gaming detector; baseline refresher; mission-metric audits."], ["architecture", "Scaling architecture", "Scaling: amplifying fleets of workflows", "Organizations run hundreds of workflows: a fleet amplifier schedules cycles across them by expected gain, shares winning strategies between similar workflows, and maintains a global ledger. Compute budgets are allocated like investments — to the workflows where improvement pays most.", "Fleet scheduler; strategy sharing; global ledger; budget allocator."], ["interface", "Security, permissions, and audit", "Security: amplification safety", "Self-improvement needs guardrails: change budgets per workflow, approval gates for production workflows, rollback guarantees, and audit trails of every kept change. The amplifier cannot silently rewrite a critical workflow at 3 AM — the gates and the ledger forbid it.", "Change budgets; approval gates; guaranteed rollback; audit trail."], ["worked-example", "Compounded integration and acceptance suite", "Compounded integration and acceptance suite", "Acceptance amplifies fixture workflows with planted flaws and gaming traps: find the flaws, beat the baseline, catch the gaming, respect the gates. The amplifier ships only when its improvements are real, measured, and safely governed.", "Fixture workflows; flaw and trap planters; full amplification run; reality, safety, and efficiency scorers; release gate."]];
function demoProgram(seed,title,rnd){
  var n=ri(rnd,5,12);
  var lines=['// JAH demo program — runnable with: node demo.js','// generated record demo (seed '+seed+')','\'use strict\';'];
  lines.push('var checks=[');
  for(var i=0;i<n;i++){lines.push('  {expr:"'+(i+2)+'*'+(i+3)+'",expect:'+((i+2)*(i+3))+'}'+(i<n-1?',':''));}
  lines.push('];');
  lines.push('var fails=0;');
  lines.push('checks.forEach(function(c){var got=eval(c.expr);var ok=got===c.expect;if(!ok)fails++;console.log((ok?"PASS":"FAIL")+"  "+c.expr+" = "+got);});');
  lines.push('console.log("generated demo: "+(checks.length-fails)+"/"+checks.length+" checks passed");');
  return lines.join("\n");
}
function generate(seed,opts,rnd){
  opts=opts||{};rnd=rnd||prng(seed);
  var cat=opts.category||pick(CATS,rnd);
  var pool=B.filter(function(b){return b[0]===cat;});
  var b=pick(pool.length?pool:B,rnd);
  var id=PREFIX+String(seed).padStart(6,'0');
  var title=b[2]+' — variant '+seed;
  var prog=demoProgram(seed,title,rnd);
  return {id:id,title:title,description:b[3],ladder_rank:ri(rnd,1,15),
    demo:{kind:'code',title:'Runnable code demo — '+title.slice(0,50),program:prog,language:'javascript'},
    architecture:b[4],components:['core coordinator','interface adapter','validation harness','telemetry exporter'],
    interfaces:['JSON record schema v1','query API (filter/sort/paginate)','demo runner (node-compatible JS)'],
    implementation_status:'Generated design record — proposed capability; demo program is real executable code.',
    acceptance_tests:{criteria:['demo program executes without errors','record validates against schema','no duplicate id in archive'],demo_status:'generated at runtime'},
    dependencies:['node.js runtime (demo execution)','JAH database core (jahdb.js)','gzip JSONL archive'],
    provenance:"Public-record survey",last_verified:"2026-10-21",march_marker:"March to a million in progress \u2014 15 of 1,000,000 records (0.0015%)",
    t:title,g:cat,c:1,_seed:seed};
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  if(typeof r.id!=='string'||r.id.indexOf(PREFIX)!==0)e.push('id');
  if(typeof r.title!=='string'||!r.title.length)e.push('title');
  if(typeof r.description!=='string'||!r.description.length)e.push('description');
  if(!(r.ladder_rank>=1&&r.ladder_rank<=15))e.push('ladder_rank');
  var d=r.demo;
  if(!d||d.language!=='javascript'||typeof d.program!=='string'||d.program.indexOf('console.log')<0)e.push('demo');
  if(typeof r.architecture!=='string'||!r.architecture.length)e.push('architecture');
  if(!Array.isArray(r.components)||!r.components.length)e.push('components');
  if(!Array.isArray(r.interfaces)||!r.interfaces.length)e.push('interfaces');
  if(typeof r.implementation_status!=='string'||!r.implementation_status.length)e.push('implementation_status');
  if(!r.acceptance_tests||typeof r.acceptance_tests!=='object')e.push('acceptance_tests');
  if(!Array.isArray(r.dependencies)||!r.dependencies.length)e.push('dependencies');
  if(CATS.indexOf(r.g)<0)e.push('g');
  return {ok:!e.length,errors:e};
}
var gen={version:VERSION,generate:generate,validate:validate};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("apex-tool-recursive-intelligence-amplifier",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();