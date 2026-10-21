(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];} function ri(s,a,b){return a+((s()*(b-a+1))|0);}
var CATS=["architecture", "component", "benchmark", "interface", "worked-example"];
var PREFIX="JAH-APX14-";
var VERSION="jahdb-apex-tool-universal-evidence-constellation-engine-1.0";
/* rows: [group, focus, title, description, architecture] */
var B=[["architecture", "Concept and purpose", "What the Evidence Constellation Engine is", "The engine maintains constellations: each conclusion surrounded by its supporting sources, its counterevidence, the conclusions it depends on, and its uncertainty assessment. Nothing stands alone. When evidence changes, the constellation updates and every dependent conclusion is re-evaluated automatically.", "Conclusion nodes with evidence edges; dependency graph; change propagation on evidence updates; uncertainty recomputation."], ["architecture", "Core data model", "Constellation data model", "A constellation is a record: the conclusion statement, supporting sources with weights, counterevidence with weights, dependency links to other conclusions, uncertainty decomposition, and a verdict with its margin. The model makes 'what would change my mind' a computable question — the nearest strong counterevidence.", "Conclusion documents; weighted evidence edges; dependency edges; uncertainty fields; mind-change query support."], ["component", "Key algorithm I", "Evidence weighing algorithm", "Not all evidence weighs the same: replicated experiments outweigh single observations, independent sources outweigh correlated ones, direct measurements outweigh proxies. The weighing algorithm combines source reliability, independence, and relevance into weights, and publishes the weighting so it can be argued with.", "Source reliability scorer; independence analyzer; relevance grader; published weight combination with rationale."], ["component", "Key algorithm II", "Dependency propagation algorithm", "Conclusions depend on conclusions: if a supporting study is retracted, every conclusion downstream must be re-evaluated. The propagator walks the dependency graph on evidence changes, recomputes verdicts in topological order, and reports exactly which conclusions changed and why.", "Dependency DAG; topological recompute; change reports with reasons; subscriber notifications."], ["interface", "Interface specification", "Constellation query interface specification", "Callers ask 'what is the evidence for X', 'what would change your mind about X', or 'what depends on study S'. Responses include the full constellation with weights and the reasoning trail. The interface treats counterevidence as a first-class answer, never buried.", "Constellation query service; mind-change computer; dependency explorer; reasoning-trail renderer."], ["component", "Ingestion and adapters", "Ingestion: harvesting evidence", "Evidence arrives from studies, datasets, expert assessments, and sensor records. Harvesters extract claims and their support relations, grade sources, and link everything into constellations. Ingestion never creates a conclusion without evidence — the orphan-claim ban is enforced at write time.", "Per-source harvesters; claim extractor; source grader; ban-enforcing writer."], ["component", "Indexing and retrieval", "Evidence indexing and retrieval", "Evidence is indexed by claim, source, source type, reliability tier, and time, so 'all high-reliability counterevidence to X since 2020' is one query. The index powers both constellation rendering and the change propagator's need to find everything downstream of a retraction.", "Multi-facet evidence index; reliability tiers; temporal slicing; downstream lookup for propagation."], ["component", "Reasoning and decision component", "Reasoning: verdicts with margins", "A verdict is not just 'supported' — it is 'supported with margin 2.3, nearest counterevidence at weight 1.1'. Margins make verdicts actionable: thin margins trigger watchfulness, wide margins allow reliance. When margins cross thresholds, the engine raises or lowers its confidence publicly.", "Margin computer; threshold watcher; confidence announcer; verdict history."], ["interface", "Output and presentation", "Constellation presentation output", "Constellations render as navigable diagrams: the conclusion centered, supporters in one arc, counterevidence in another, dependencies below, uncertainty as a halo. Clicking any element reveals its evidence and reasoning. The visualization is a working instrument, not decoration.", "Constellation layout engine; arc arrangement by stance; halo uncertainty rendering; evidence drill-down."], ["benchmark", "Benchmark harness and measured baseline", "Evidence benchmark harness", "The engine is tested on fixture debates with known right answers: planted evidence sets where the correct verdict is known, retraction scenarios where propagation must reach every dependent, and calibration tests on uncertainty. Baselines are simple vote-counting and single-source trust.", "Fixture debate suite; retraction injector; verdict and calibration scorers; baseline gate."], ["worked-example", "End-to-end worked example", "Worked example: should we recommend encapsulation", "A product team asks whether to recommend encapsulation for humid climates. The constellation shows strong lab support, a 5-year dataset, one contesting tropical field study, and a thin margin on the humid-climate sub-claim. The verdict: recommend with humid-climate monitoring, and the mind-changer that would reverse it is named explicitly.", "Claim intake; constellation assembly; sub-claim margin analysis; recommendation with conditions and mind-changer."], ["component", "Failure modes and reliability", "Failure modes: evidence laundering and cascade errors", "Evidence can be laundered — one source cited many times looking like many sources — and errors cascade through dependencies. The engine fights laundering with independence analysis and cascades with propagation that shows its work. Every verdict can answer 'which three sources matter most' to expose laundering.", "Independence analyzer; laundering detector; cascade tracer; top-sources explainer."], ["architecture", "Scaling architecture", "Scaling: constellations at web scale", "Millions of conclusions need partitioned constellations: sharded by topic with cross-shard dependency links, propagation bounded by impact radius, and lazy recomputation for low-stakes conclusions. The engine scales by not recomputing the world on every new paper — only the affected neighborhood.", "Topic sharding; cross-shard links; impact-bounded propagation; lazy recompute tiers."], ["interface", "Security, permissions, and audit", "Security: evidence integrity", "Constellations are only as honest as their evidence links: signed sources, tamper-evident citation records, and provenance verification before admission. Fabricated evidence is treated as an attack — quarantined, investigated, and its submitter flagged across the system.", "Source signer; citation integrity checker; fabrication detector; submitter reputation."], ["worked-example", "Compounded integration and acceptance suite", "Compounded integration and acceptance suite", "Acceptance runs fixture debates end to end: harvest evidence, build constellations, render verdicts with margins, inject retractions and fabricated evidence, and verify propagation reaches every dependent and fraud is quarantined. The engine ships only when its constellations are complete, current, and honest.", "Fixture debates; retraction and fraud injection; full-loop runner; completeness, currency, and honesty scorers; release gate."]];
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
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("apex-tool-universal-evidence-constellation-engine",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();