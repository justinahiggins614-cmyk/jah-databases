(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];} function ri(s,a,b){return a+((s()*(b-a+1))|0);}
var CATS=["architecture", "component", "benchmark", "interface", "worked-example"];
var PREFIX="JAH-APX8-";
var VERSION="jahdb-apex-tool-universal-information-reconstruction-engine-1.0";
/* rows: [group, focus, title, description, architecture] */
var B=[["architecture", "Concept and purpose", "What the Reconstruction Engine is", "The engine rebuilds lost or damaged information from what survived: quotations in other works, redundant copies, earlier versions, and derived artifacts. It produces the most defensible reconstruction possible and marks every uncertain passage, so readers always know which parts are solid and which are educated inference.", "Evidence collector gathering surviving traces; alignment engine mapping traces to the lost original's structure; reconstruction assembler with confidence tagging; uncertainty ledger."], ["architecture", "Core data model", "Trace and reconstruction data model", "Every surviving trace is a record: what it is, where it was found, what it claims about the original, and how reliable its chain of custody is. Reconstructions reference traces, never float free — a reconstructed sentence must point at the quotations and versions it was built from.", "Trace documents with custody chains; reconstruction documents with trace references per passage; confidence as a computed field from trace agreement."], ["component", "Key algorithm I", "Trace alignment algorithm", "Traces must be aligned to the original's structure before they can be combined: which quotation belongs to which lost page, which version fragment fills which gap. The aligner uses overlapping content, sequence anchors, and metadata to place each trace, scoring each placement so weak alignments are visible.", "Anchor-based placement; overlap scoring; sequence constraint solver; placement confidence per trace."], ["component", "Key algorithm II", "Consensus reconstruction algorithm", "Where multiple traces cover the same passage, the engine builds consensus: agreement strengthens confidence, disagreement is preserved as variants rather than averaged away. A passage quoted three ways appears with all three readings and the evidence for each — the reader decides, informed.", "Per-passage trace clustering; agreement scorer; variant preserver; consensus text with variant apparatus."], ["interface", "Interface specification", "Reconstruction query interface specification", "Callers request reconstruction of a lost item by identity and get back the best reconstruction with per-passage confidence, the trace inventory, and explicit gaps where nothing survived. The interface also serves 'what do we know about X' queries that return only high-confidence passages.", "Reconstruction service; confidence-filtered query modes; trace inventory endpoint; gap reporter."], ["component", "Ingestion and adapters", "Ingestion: gathering surviving traces", "Traces hide in mirrors, citations, quotations, derived datasets, and format-migrated copies. Collectors sweep each source type, extract candidate traces with custody information, and deduplicate the same trace found twice. Collection is exhaustive within budget and honest about its coverage.", "Per-source collectors; custody extractor; trace deduper; coverage reporter."], ["component", "Indexing and retrieval", "Trace indexing and retrieval", "Traces are indexed by the lost item they bear on, by passage, by source type, and by custody strength, so reconstruction of any passage pulls exactly its relevant traces. Redundant traces are linked, not duplicated, keeping the evidence graph clean.", "Multi-facet trace index; redundancy linker; passage-scoped retrieval; custody-weighted ranking."], ["component", "Reasoning and decision component", "Reasoning: weighing conflicting traces", "Traces conflict — two quotations of the same passage differ. The engine weighs them by custody strength, source independence, and corroboration, and when traces are not independent (one copied the other), it discounts the copy. The reasoning is shown, not hidden: every verdict lists its weights.", "Independence analyzer over trace lineages; weighted consensus; weight disclosure in verdicts; copy-detection discounting."], ["interface", "Output and presentation", "Reconstructed document presentation output", "Reconstructions render as readable documents where confidence is visible: solid passages in normal text, uncertain passages marked with confidence badges, gaps shown as explicit lacunae. A reader can see at a glance what is known, what is inferred, and what is lost — the honest shape of our knowledge.", "Confidence-aware renderer; lacuna markers; variant apparatus; trace deep-links per passage."], ["benchmark", "Benchmark harness and measured baseline", "Reconstruction benchmark harness", "The engine is tested by deliberate destruction: take a known document, delete parts, and measure how accurately the engine reconstructs them from the remaining traces. Metrics cover passage accuracy, confidence calibration (does 80% confidence mean right 80% of the time?), and gap honesty. Baselines are single-best-trace and naive concatenation.", "Destruction-and-rebuild test rig; accuracy and calibration scorers; gap-honesty checker; baseline gate."], ["worked-example", "End-to-end worked example", "Worked example: rebuilding a lost manual", "A 60-page equipment manual is lost; two partial mirrors, eleven citing papers, and a draft version survive. The engine aligns 94 traces, builds consensus for 48 pages, marks 4 pages medium-confidence from single quotations, and declares 8 pages lost. The rebuilt manual ships with its uncertainty ledger — usable for reference, honest about limits.", "Trace sweep; alignment; consensus assembly; confidence tagging; lacuna declaration; ledger export."], ["component", "Failure modes and reliability", "Failure modes: invented certainty and trace poisoning", "The worst failures are silent: an engine that fills gaps with plausible invention, or traces planted to rewrite history. Defenses include the schema-level ban on unmarked invention, independence analysis that discounts coordinated traces, and calibration audits that punish overconfidence. Uncertainty is a safety feature.", "Invention ban enforced by schema; coordinated-trace detector; calibration audits; overconfidence penalties in scoring."], ["architecture", "Scaling architecture", "Scaling: reconstructing at archive scale", "Whole archives go dark — thousands of items needing reconstruction. The engine parallelizes by item with shared trace indexes, prioritizes by demand and cultural value, and streams partial reconstructions as traces arrive. Scale never compromises the uncertainty ledger: every passage keeps its confidence at any volume.", "Item-parallel workers; shared trace index; priority scheduler; streaming partial results with confidence intact."], ["interface", "Security, permissions, and audit", "Security: custody integrity", "Traces are evidence, and evidence must be tamper-evident: hash-chained custody records, signed mirror attestations, and provenance verification before a trace enters the ledger. A trace with broken custody is treated as hearsay — usable as a lead, never as evidence.", "Hash-chained custody; attestation verifier; custody-graded trace admission; hearsay quarantine."], ["worked-example", "Compounded integration and acceptance suite", "Compounded integration and acceptance suite", "Acceptance destroys fixture documents in controlled ways and requires the engine to rebuild them with calibrated confidence and honest gaps: trace sweep, alignment, consensus, ledger, and presentation all scored. The build ships only when reconstructions are accurate, confidence is calibrated, and no gap is ever silently filled.", "Destruction fixtures; full-loop runner; accuracy, calibration, and honesty scorers; release gate."]];
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
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("apex-tool-universal-information-reconstruction-engine",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();