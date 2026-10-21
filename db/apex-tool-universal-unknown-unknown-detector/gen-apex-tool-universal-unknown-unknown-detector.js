(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];} function ri(s,a,b){return a+((s()*(b-a+1))|0);}
var CATS=["architecture", "component", "benchmark", "interface", "worked-example"];
var PREFIX="JAH-APX11-";
var VERSION="jahdb-apex-tool-universal-unknown-unknown-detector-1.0";
/* rows: [group, focus, title, description, architecture] */
var B=[["architecture", "Concept and purpose", "What the Unknown-Unknown Detector is", "The detector systematically looks for what is missing: archive regions with no coverage, questions no tool can answer, capability combinations nobody provides. It turns 'we don't know what we don't know' from a slogan into a work queue, prioritized by the evidence that the gap matters.", "Coverage model of the known; gap finder comparing expectation to coverage; importance scorer; prioritized gap queue with review workflow."], ["architecture", "Core data model", "Coverage and gap data model", "Coverage is modeled as a grid over subjects, capabilities, languages, and time: each cell records what exists and how well. A gap is a cell that expectation says should be filled but is not — with the expectation's reasoning attached, so gaps are argued, not asserted.", "Multi-dimensional coverage grid; expectation rules with reasoning; gap records linking expectation to empty cells; review states."], ["component", "Key algorithm I", "Expectation-based gap finding algorithm", "Gaps are found by comparing coverage against expectations derived from population, economic weight, scientific activity, and analogies to covered areas. If a language with two million speakers has zero agricultural records while similar languages have hundreds, that asymmetry is a detected gap with quantified evidence.", "Expectation models per dimension; asymmetry detector; evidence quantifier; false-positive filter using known structural reasons for emptiness."], ["component", "Key algorithm II", "Novelty and anomaly detection algorithm", "Beyond expectations, the detector watches for anomalies: capability combinations that exist nowhere, questions that stump every archive, search trails that dead-end. One-class models trained on 'what exists' flag the shapes of 'what doesn't' for human review.", "Feature encoding of capabilities and questions; one-class models; dead-end trail analyzer; human review queue."], ["interface", "Interface specification", "Gap query interface specification", "Callers ask 'what are we missing in X' and get ranked gaps with evidence: the empty cells, why they should be filled, and what filling them would unlock. The interface also serves 'prove this gap is real' deep-dives with the full search trail that established the absence.", "Gap query service; evidence assembler; absence-proof trail exporter; ranking by importance."], ["component", "Ingestion and adapters", "Ingestion: building the coverage model", "Coverage data comes from catalogs, archive descriptors, query logs, and capability registries. Ingestion normalizes each into the coverage grid with provenance, and records each source's blind spots — a catalog that never lists community archives creates a systematic blind spot the detector must know about.", "Per-source coverage importers; blind-spot annotator; grid merger with provenance; freshness tracking."], ["component", "Indexing and retrieval", "Gap indexing and retrieval", "Detected gaps are indexed by domain, language, capability, and importance so planners can pull 'top gaps in agriculture' or 'all language gaps above threshold'. The index supports the detector's own re-check scheduling — gaps are re-probed on schedule because absence is a claim that expires.", "Gap index with faceted search; re-check scheduler; expiry on absence claims; change feed for gap status."], ["component", "Reasoning and decision component", "Reasoning: is this gap real and does it matter", "Not every empty cell is a real gap — some things should not exist, and some absences do not matter. The reasoner checks structural explanations (legal, physical, logical), estimates impact from the expectation evidence, and only promotes gaps that survive both filters to the priority queue.", "Structural-explanation checker; impact estimator; two-gate promotion; promoted-gap dossier assembler."], ["interface", "Output and presentation", "Gap dossier presentation output", "Each promoted gap gets a dossier: what is missing, the evidence it should exist, the search that proved it absent, the estimated impact of filling it, and suggested next steps. The dossier is written for the person who might fill the gap — a builder, a researcher, a funder — with everything needed to act.", "Dossier assembler; evidence linker; impact visualizer; action recommender."], ["benchmark", "Benchmark harness and measured baseline", "Detection benchmark harness", "The detector is tested on planted gaps in fixture catalogs: known missing categories it must find, known structural empties it must not flag, and importance rankings compared to expert judgment. Baselines are manual audit samples and random inspection; the detector must find more real gaps per review hour.", "Fixture catalogs with planted gaps; detection runner; precision/recall and ranking scorers; baseline gate."], ["worked-example", "End-to-end worked example", "Worked example: the missing maintenance manuals", "Scanning equipment coverage, the detector finds that three widely deployed pump models have zero maintenance manuals in any catalog, while comparable models average six each. Expectation evidence: deployment numbers from procurement records. The dossier goes to the manufacturers' documentation teams with the deployment figures attached.", "Equipment coverage scan; expectation from deployment data; absence verification; dossier routing."], ["component", "Failure modes and reliability", "Failure modes: false gaps and gap blindness", "The detector's own failures are tracked: false gaps from bad expectations, and blind spots from incomplete coverage data. Every promoted gap carries its expectation's provenance so bad expectations can be corrected, and coverage blind spots are published so users know where the detector cannot see.", "Expectation provenance tracking; false-gap feedback loop; blind-spot publisher; detector self-audit."], ["architecture", "Scaling architecture", "Scaling: continuous planetary gap watch", "Gap detection runs continuously across all catalogs: incremental coverage updates feed the detector, which re-scores gaps and emits a changing watch list. The watch is partitioned by domain with a global rollup, so both specialists and generalists get a useful view.", "Incremental coverage feed; continuous detector; partitioned watch lists; global rollup."], ["interface", "Security, permissions, and audit", "Security: gaps as sensitive information", "Some gaps are sensitive — revealing exactly what intelligence is missing helps adversaries. Gap dossiers carry sensitivity markings, sensitive gaps are summarized rather than detailed, and access is controlled. The detector never publishes a gap whose disclosure harms the people it aims to help.", "Sensitivity classifier for gaps; summarized rendering for sensitive gaps; access-controlled detail; disclosure review."], ["worked-example", "Compounded integration and acceptance suite", "Compounded integration and acceptance suite", "Acceptance plants gaps in fixture catalogs and requires the detector to find the real ones, dismiss the structural empties, rank by expert-judged importance, and produce actionable dossiers — with blind spots declared. The detector ships only when its watch list is both accurate and honest about its limits.", "Planted-gap fixtures; full detection run; accuracy, ranking, and honesty scorers; release gate."]];
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
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("apex-tool-universal-unknown-unknown-detector",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();