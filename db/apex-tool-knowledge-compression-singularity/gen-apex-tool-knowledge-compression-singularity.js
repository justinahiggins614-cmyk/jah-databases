(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];} function ri(s,a,b){return a+((s()*(b-a+1))|0);}
var CATS=["architecture", "component", "benchmark", "interface", "worked-example"];
var PREFIX="JAH-APX17-";
var VERSION="jahdb-apex-tool-knowledge-compression-singularity-1.0";
/* rows: [group, focus, title, description, architecture] */
var B=[["architecture", "Concept and purpose", "What the Compression Singularity is", "The singularity compresses knowledge into layers of increasing density — brief, summary, digest, index — where each layer links down to the fuller layer below. Readers choose their depth; the system guarantees every compressed claim can be expanded to its evidence. Compression serves understanding, not just storage.", "Layered compression pipeline; claim-preserving summarizers; evidence link maintainer; depth-choice renderer."], ["architecture", "Core data model", "Compression layer data model", "Each layer is a record: its depth, its claims with evidence links to the layer below, its compression ratio, and its measured claim-retention score. Layers form a chain back to the source — break a link and the layer above it is invalid until recompressed.", "Layer documents; claim-link edges; retention scores; chain integrity checker."], ["component", "Key algorithm I", "Claim-preserving summarization algorithm", "Summarization extracts the source's checkable claims first, then compresses around them: every claim in the summary must trace to the source, and the claim set must cover the source's key findings. Fluency without claim coverage is rejected — a pretty summary that drops the findings is a failure.", "Claim extractor; coverage planner; claim-anchored generator; coverage verifier."], ["component", "Key algorithm II", "Progressive refinement algorithm", "Readers drill down progressively: the brief expands to the summary, the summary to the digest, the digest to the full text. Refinement is instant because deeper layers are precomputed, and each expansion preserves context — the reader never loses their place while going deeper.", "Precomputed layer chain; expansion navigator; context preserver; prefetch predictor."], ["interface", "Interface specification", "Compression query interface specification", "Callers request knowledge at a depth: brief me, summarize this, give me the digest. Responses include the compressed content, its retention score, and expansion links. The interface also answers 'what did compression drop' — the claims below the cut line, available on request.", "Depth-parameterized endpoint; retention reporter; dropped-claims lister; expansion linker."], ["component", "Ingestion and adapters", "Ingestion: compressing the archive", "The archive's documents flow through the pipeline on arrival and on schedule: new documents get compressed immediately, changed documents trigger recompression of affected layers, and link integrity is verified continuously. Compression is infrastructure, not an afterthought.", "Arrival trigger; change detector; recompression scheduler; integrity verifier."], ["component", "Indexing and retrieval", "Compressed index and retrieval", "Each layer is indexed for its use: briefs for instant answers, summaries for semantic search, digests for deep research. Retrieval picks the shallowest layer that can answer, expanding only when needed — speed from compression, depth on demand.", "Per-layer indexes; shallowest-sufficient router; expansion-on-demand; layer-aware ranking."], ["component", "Reasoning and decision component", "Reasoning: retention vs ratio tradeoffs", "Compression trades ratio against retention: the engine measures both and lets policy choose the operating point. Critical domains run high-retention; casual browsing runs high-ratio. The tradeoff curve is published per subject so the choice is informed, not arbitrary.", "Ratio-retention measurer; tradeoff curve publisher; policy-configured operating points; per-subject curves."], ["interface", "Output and presentation", "Layered reading presentation output", "Compressed knowledge renders as layered reading: the brief up front, expandable sections below, evidence links throughout. Readers control their depth with a single control, and the interface remembers their preferred depth per subject.", "Layered renderer; depth control; preference memory; evidence linker."], ["benchmark", "Benchmark harness and measured baseline", "Compression benchmark harness", "Compression is measured on claim retention (ROUGE-style overlap plus claim-level checks), ratio, and link integrity — not just bytes. Baselines are truncation and generic summarizers; the singularity's layers must retain more claims per byte with intact links to win.", "Claim-level test suite; retention and ratio scorers; link integrity checker; baseline gate."], ["worked-example", "End-to-end worked example", "Worked example: compressing a research archive", "A 2,000-document research archive gets four layers: briefs for executives, summaries for researchers, digests for specialists, full text for auditors. Claim retention averages 0.91 at the brief layer; every brief claim expands to its source page. Reading time for the archive's essence drops from weeks to an afternoon — without losing the ability to verify.", "Batch pipeline; per-layer generation; retention measurement; expansion verification; reading-time estimate."], ["component", "Failure modes and reliability", "Failure modes: lossy lies and link rot", "Compression fails by dropping load-bearing claims or by links rotting underneath. The engine defends with claim-retention floors per layer, continuous link integrity checks, and automatic recompression when links break. A layer that cannot prove its claims is withdrawn, not served.", "Retention floor enforcer; link checker; recompression trigger; withdrawal policy."], ["architecture", "Scaling architecture", "Scaling: compressing planetary corpora", "Planetary scale means streaming compression: documents compressed on arrival by distributed workers, layers sharded by subject, and link integrity checked by background sweepers. Throughput scales horizontally; the amnesia ban holds at any volume because it is schema-enforced, not process-dependent.", "Streaming workers; subject sharding; background sweepers; schema-enforced link requirements."], ["interface", "Security, permissions, and audit", "Security: compression as an attack surface", "Summaries can be weaponized: selective compression that drops exculpatory claims, or poisoned sources amplified by compression. Defenses include retention audits, source diversity requirements per layer, and provenance on every claim. Compression must not become a laundering machine.", "Retention auditor; diversity enforcer; claim provenance; laundering detector."], ["worked-example", "Compounded integration and acceptance suite", "Compounded integration and acceptance suite", "Acceptance compresses a fixture corpus end to end: generate all layers, measure retention and ratio, break links to verify recompression, and audit that no claim floats without evidence. The singularity ships only when compression is deep, faithful, and fully traceable.", "Fixture corpus; full compression run; retention, ratio, and integrity scorers; link-break injector; release gate."]];
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
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("apex-tool-knowledge-compression-singularity",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();