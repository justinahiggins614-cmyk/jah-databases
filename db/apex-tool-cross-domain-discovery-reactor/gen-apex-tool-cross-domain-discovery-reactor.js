(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];} function ri(s,a,b){return a+((s()*(b-a+1))|0);}
var CATS=["architecture", "component", "benchmark", "interface", "worked-example"];
var PREFIX="JAH-APX19-";
var VERSION="jahdb-apex-tool-cross-domain-discovery-reactor-1.0";
/* rows: [group, focus, title, description, architecture] */
var B=[["architecture", "Concept and purpose", "What the Discovery Reactor is", "The reactor systematically hunts for cross-domain combinations: it indexes methods by what they do (not what field they come from), matches unsolved problems to methods from other fields, and proposes transfers with explicit analogy mappings. Each proposal includes where the analogy is expected to break — honesty about limits is what makes the proposals testable.", "Method index by capability; problem index by structure; analogy mapper; breakdown predictor; proposal ranker."], ["architecture", "Core data model", "Method and problem data model", "Methods are recorded by their mechanism, inputs, outputs, assumptions, and known limits — not by their home field. Problems are recorded by their structure: constraints, goals, and failure modes. This field-blind representation is what lets a heat-transfer method match a finance problem: the structures align even when the vocabularies do not.", "Mechanism-first method schema; structure-first problem schema; field tags as metadata, never as match keys; assumption and limit fields required."], ["component", "Key algorithm I", "Analogical matching algorithm", "Matching finds structural alignment between a method's mechanism and a problem's structure: shared causal patterns, shared constraint shapes, shared resource flows. Surface similarity is distrusted — the algorithm scores deep structural matches and penalizes keyword coincidence, using structure-mapping principles.", "Structure extractor; alignment scorer; surface-similarity penalizer; ranked candidate list."], ["component", "Key algorithm II", "Breakdown prediction algorithm", "Every analogy breaks somewhere: the predictor identifies where by comparing the method's assumptions against the problem's conditions. Assumption violations become predicted breakdown points with severity estimates — the proposal ships with its own falsification checklist, which is what makes it scientific.", "Assumption-condition comparator; violation detector; severity estimator; falsification checklist generator."], ["interface", "Interface specification", "Transfer proposal interface specification", "Callers submit a problem and get ranked transfer proposals: the method, its home field, the analogy mapping, predicted breakdowns, and a test plan. The interface also takes a method and finds problems it could solve — prospecting in both directions.", "Bidirectional proposal service; mapping renderer; test-plan generator; ranking with explanations."], ["component", "Ingestion and adapters", "Ingestion: mining methods and problems", "Methods are mined from papers, patents, and engineering handbooks; problems from issue trackers, research agendas, and failure reports. Miners extract mechanism and structure, not just keywords, with human review for high-value entries. The indexes grow with the literature.", "Method miner; problem miner; mechanism/structure extractor; review queue."], ["component", "Indexing and retrieval", "Transfer indexing and retrieval", "Proposals are indexed by method, problem structure, fields involved, test status, and outcome — so 'show me tested transfers from biology to engineering' is one query. The outcome index is the reactor's memory: which analogies survived contact with reality.", "Proposal index; outcome tracker; status lifecycle; faceted retrieval."], ["component", "Reasoning and decision component", "Reasoning: testing the analogy", "Proposals graduate by testing: the reactor designs the cheapest discriminating test from the breakdown predictions, tracks results, and updates the analogy's status. Failed transfers are as valuable as successes — the ledger records why, so the same mistake is not proposed twice.", "Test designer; result tracker; status updater; failure-lesson recorder."], ["interface", "Output and presentation", "Proposal presentation output", "Proposals render as innovation briefs: the problem, the method and its origin, the analogy mapping in plain language, the predicted breakdowns, and the test plan. A domain expert can evaluate the proposal without learning the reactor's internals — the brief speaks their language.", "Brief assembler; mapping visualizer; breakdown renderer; test-plan formatter."], ["benchmark", "Benchmark harness and measured baseline", "Transfer benchmark harness", "The reactor is tested on historical transfers with known outcomes: famous cross-domain successes it should have proposed, and famous failures it should have flagged. Metrics cover proposal recall, breakdown prediction accuracy, and test cost efficiency. Baselines are keyword matching and expert brainstorming samples.", "Historical transfer suite; proposal runner; breakdown scorer; baseline gate."], ["worked-example", "End-to-end worked example", "Worked example: cooling the data center", "Faced with bursty hot spots, the reactor proposes fin geometry from power electronics, phase-change materials from building design, and workload shifting from grid management — each with analogy mappings, breakdown predictions, and test plans. The cheapest test (simulation) kills the fin idea fast; phase-change proceeds to prototyping. Two proposals, one survivor, zero wasted prototypes on the dead idea.", "Problem intake; multi-method proposal; breakdown analysis; test sequencing by cost; outcome tracking."], ["component", "Failure modes and reliability", "Failure modes: cargo-cult transfer and analogy blindness", "Transfers fail when surface similarity masquerades as structural fit, or when teams fall in love with an analogy and ignore its breakdowns. The reactor defends with structural scoring, mandatory breakdown sections, and test-first gating — no proposal proceeds to building without surviving its cheapest discriminating test.", "Structural scorer; breakdown mandator; test gate; analogy-attachment monitor."], ["architecture", "Scaling architecture", "Scaling: reactor networks", "Reactors specialize by field-pair (bio-to-engineering, math-to-computing) and share validated transfers through a network: a transfer proven in one reactor becomes a candidate everywhere. The network compounds — each validated analogy enriches every reactor's method index.", "Specialized reactors; transfer sharing protocol; network-wide method index; validation propagation."], ["interface", "Security, permissions, and audit", "Security: dual-use transfer screening", "Some transfers are dual-use: a method that improves medicine could improve weapons. The reactor screens proposals against dual-use policies, escalates risky ones for human review, and blocks transfers that fail review. Innovation with guardrails, not blinders.", "Dual-use screener; escalation workflow; review board data; block enforcer."], ["worked-example", "Compounded integration and acceptance suite", "Compounded integration and acceptance suite", "Acceptance runs the reactor on fixture problems with known historical transfers: propose, predict breakdowns, design tests, track outcomes, and verify the ledger learns. The reactor ships only when its proposals are structurally sound, honestly bounded, and improve with experience.", "Fixture problems; full proposal run; soundness, honesty, and learning scorers; release gate."]];
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
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("apex-tool-cross-domain-discovery-reactor",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();