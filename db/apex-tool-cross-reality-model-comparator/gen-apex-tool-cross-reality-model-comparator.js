(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];} function ri(s,a,b){return a+((s()*(b-a+1))|0);}
var CATS=["architecture", "component", "benchmark", "interface", "worked-example"];
var PREFIX="JAH-APX13-";
var VERSION="jahdb-apex-tool-cross-reality-model-comparator-1.0";
/* rows: [group, focus, title, description, architecture] */
var B=[["architecture", "Concept and purpose", "What the Model Comparator is", "The comparator stages fair contests between models: same tasks, same metrics, same conditions, with each model's assumptions documented and its reality grade labeled. It reports which model won, by how much, under which assumptions — and explicitly what the result does not prove about the physical world.", "Model registry with assumption documents; contest runner with fixed tasks and metrics; reality-grade labeling; assumption-aware result reporting."], ["architecture", "Core data model", "Model and reality-grade data model", "Every model is a record: its equations or code, its assumptions, its training data, its reality grade (measured, simulated, hypothesized), and its known failure conditions. Reality grades are enforced by the schema — a simulated result cannot be stored as a measurement, full stop.", "Model documents with grade field; schema-level grade enforcement; assumption versioning; failure-condition registry."], ["component", "Key algorithm I", "Fair contest design algorithm", "A fair contest gives every model the same tasks, the same inputs, the same metrics, and no peeking at the answers. The designer checks for leakage (did a model train on the test data?), balances task difficulty, and pre-registers the scoring so nobody moves the goalposts after seeing results.", "Task suite assembler; leakage checker; difficulty balancer; pre-registered scoring plan; contest executor."], ["component", "Key algorithm II", "Assumption sensitivity algorithm", "Models win under assumptions; the comparator varies the assumptions to see which victories survive. A model that only wins when its favorite assumption holds is fragile — the sensitivity analysis shows exactly where each model's advantage comes from and where it collapses.", "Assumption parameterizer; sweep executor; victory-margin tracker per assumption setting; fragility reporter."], ["interface", "Interface specification", "Comparison query interface specification", "Callers ask 'compare these models on this task' and get a structured verdict: rankings with margins, assumption sensitivities, reality grades, and the explicit non-claim about physical reality. The interface also answers 'under what assumptions does model X win' — the question that actually matters.", "Comparison service; verdict assembler; assumption-conditional query support; non-claim disclaimers attached."], ["component", "Ingestion and adapters", "Ingestion: registering models honestly", "Models enter the registry with full disclosure: code or equations, training data, assumptions, known failures, and claimed reality grade. Registration validates the disclosure — a model claiming 'measured' must point at measurements — and grades are audited, not self-assigned on trust.", "Disclosure validator; grade auditor; training-data checker; failure-condition extractor."], ["component", "Indexing and retrieval", "Contest result indexing and retrieval", "Contest results are indexed by model, task, assumption setting, and date, so 'how has model X done on forecasting tasks under cloudy assumptions' is one query. Historical contests reveal model improvement — or degradation — over versions, with every result linked to its contest conditions.", "Result index with faceted search; version-over-version tracker; condition-linked retrieval."], ["component", "Reasoning and decision component", "Reasoning: what a contest result means", "Winning a contest means winning under its conditions — the reasoner translates results into careful claims: model A beats model B on these tasks under these assumptions at this reality grade. It blocks the leap from 'won the simulation contest' to 'is true about the world' with explicit, unavoidable disclaimers.", "Claim translator; leap-blocker rules; disclaimer generator; claim strength grader."], ["interface", "Output and presentation", "Contest report presentation output", "Contest reports read like sports coverage with scientific discipline: the matchup, the conditions, the scores, the turning points (which assumptions decided it), and the standings over time. Reality grades are badges on every number, and the 'what this does not prove' section is mandatory, not optional.", "Report assembler; grade badger; turning-point analyzer; mandatory non-claim section."], ["benchmark", "Benchmark harness and measured baseline", "Comparison benchmark harness", "The comparator itself is tested: given models with known relative quality on fixture tasks, does it rank them correctly, detect leakage, and refuse to overclaim? The harness plants cheaters (models trained on test data) and checks the leakage detector catches them.", "Fixture model zoo with known quality; cheater planters; ranking and leakage scorers; overclaim checker; baseline gate."], ["worked-example", "End-to-end worked example", "Worked example: three solar forecast models", "Three solar forecasting models contest on a year of weather tasks: a physics model, a machine-learning model, and a hybrid. The ML model wins overall but collapses on rare storm patterns; the physics model wins those. The verdict recommends the hybrid for deployment with storm-mode fallback — a decision no single-number ranking could produce.", "Contest setup; per-task scoring; assumption-conditioned analysis; deployment recommender."], ["component", "Failure modes and reliability", "Failure modes: leakage and grade fraud", "Contests fail when models peek at answers or when simulated results masquerade as measured. The comparator defends with leakage detection (train/test overlap analysis), grade auditing, and a fraud ledger for violations. A caught cheater is disqualified publicly within the system — deterrence is part of the design.", "Overlap analyzer; grade auditor; fraud ledger; disqualification workflow."], ["architecture", "Scaling architecture", "Scaling: continuous model arena", "The arena runs continuously: new model versions enter, contests rerun on schedules, leaderboards update with assumption-conditioned rankings. Scale comes from parallel contest shards and cached task suites; every leaderboard entry links to its contest conditions.", "Continuous contest scheduler; parallel shards; version-aware leaderboards; condition-linked entries."], ["interface", "Security, permissions, and audit", "Security: contest integrity", "Contests are targets: model thieves, result manipulators, and grade fraudsters. Models run in sandboxes, results are hash-committed before reveal, and the audit trail lets anyone verify a contest after the fact. Integrity is engineered, not assumed.", "Sandboxed execution; commit-reveal results; verifiable audit trail; anomaly detection on submissions."], ["worked-example", "Compounded integration and acceptance suite", "Compounded integration and acceptance suite", "Acceptance stages full contests in a fixture arena with planted cheaters and grade fraud: the comparator must rank correctly, catch the cheaters, audit the grades, and refuse to overclaim. The arena is certified only when its verdicts are both accurate and disciplined about reality.", "Fixture arena; planted violations; full contest run; accuracy, integrity, and discipline scorers; release gate."]];
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
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("apex-tool-cross-reality-model-comparator",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();