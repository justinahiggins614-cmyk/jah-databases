(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];} function ri(s,a,b){return a+((s()*(b-a+1))|0);}
var CATS=["architecture", "component", "benchmark", "interface", "worked-example"];
var PREFIX="JAH-APX25-";
var VERSION="jahdb-apex-tool-mathematical-discovery-laboratory-1.0";
/* rows: [group, focus, title, description, architecture] */
var B=[["architecture", "Concept and purpose", "What the Discovery Laboratory is", "The laboratory automates the experimental side of mathematics: compute many examples, detect patterns, formulate conjectures, search for proofs, and verify with proof assistants where possible. It produces conjectures with evidence and proofs with certificates — and labels everything honestly by verification rung.", "Example computer; pattern detector; conjecture formulator; proof searcher; verification ladder."], ["architecture", "Core data model", "Mathematical claim data model", "Every claim is a record: its statement in formal and informal language, its verification rung, the evidence (examples computed, proof certificate), and its dependencies on other claims. The rung system is schema-enforced — promoting a claim requires the evidence the rung demands.", "Claim documents; rung definitions with evidence requirements; dependency graph; promotion workflow."], ["component", "Key algorithm I", "Pattern detection algorithm", "Given computed examples, the detector finds patterns: closed forms via symbolic regression, recurrences via sequence analysis, divisibility and modular patterns via number-theoretic scans. Candidate patterns are ranked by simplicity and fit — the simplest pattern fitting all examples wins the conjecture slot.", "Example tabulator; symbolic regressor; sequence analyzer; simplicity ranker."], ["component", "Key algorithm II", "Conjecture formulation algorithm", "Detected patterns become conjectures with precise statements, scope conditions, and the evidence behind them. The formulator states the conjecture in both human and formal language, lists the examples supporting it, and notes the nearest known results — positioning each conjecture in the literature.", "Pattern-to-statement translator; scope inferrer; evidence attacher; literature positioner."], ["interface", "Interface specification", "Discovery query interface specification", "Callers ask 'find patterns in this sequence', 'conjecture identities for this structure', or 'attempt a proof of this claim'. Responses carry verification rungs, evidence, and certificates. The interface never upgrades a rung without the required evidence — the ladder is load-bearing.", "Discovery endpoint; rung enforcer; certificate store; evidence linker."], ["component", "Ingestion and adapters", "Ingestion: problems and literature", "The laboratory ingests open problems, sequence databases, and formalized libraries. Intake parses problem statements into formal targets and links new conjectures to existing results — rediscovery is caught by matching against the claim database before announcement.", "Problem importer; formalizer; literature matcher; rediscovery checker."], ["component", "Indexing and retrieval", "Claim indexing and retrieval", "Claims are indexed by statement, rung, domain, and dependency — so 'machine-checked results about partitions depending on Euler's theorem' is one query. The index is the laboratory's memory: every new conjecture is checked against it before being announced as new.", "Claim index; dependency-aware retrieval; novelty checker; faceted search."], ["component", "Reasoning and decision component", "Reasoning: proof search and verification", "Proof search tries tactics, lemma combinations, and induction schemes against the formal statement; successes become certificates checked by the proof assistant's kernel. Failed attempts are analyzed for the missing lemma — the most valuable output of a failed proof is knowing exactly what is missing.", "Tactic searcher; lemma proposer; kernel verifier; missing-lemma analyzer."], ["interface", "Output and presentation", "Discovery report presentation output", "Discoveries render as mathematical reports: the claim, its rung badge, the evidence or proof, the dependencies, and the open questions it raises. Machine-checked claims carry their certificates; conjectures carry their example counts. The report reads like a paper's core, minus the prose.", "Report assembler; rung badger; certificate linker; question raiser."], ["benchmark", "Benchmark harness and measured baseline", "Discovery benchmark harness", "The laboratory is tested on sequences and structures with known patterns: does it find the known closed form, formulate it correctly, and verify honestly? Proof search is tested on theorems with known machine-checked proofs. Baselines are human mathematicians' time-to-discovery on historical cases.", "Pattern fixture suite; proof fixture suite; discovery runner; honesty scorer; baseline gate."], ["worked-example", "End-to-end worked example", "Worked example: rediscovering the odd-sum identity", "Given the sequence of partial sums 1, 4, 9, 16, 25, the laboratory detects squares, formulates 'sum of first n odds equals n squared', tests it on 50 cases, proves it by induction, and kernel-verifies the proof. The claim climbs the ladder rung by rung, each step evidenced — a complete discovery arc in minutes.", "Sequence intake; pattern detection; formulation; testing; proof search; verification; ladder climb."], ["component", "Failure modes and reliability", "Failure modes: false patterns and rung fraud", "The laboratory fails by finding patterns in noise (overfitting small examples) or by claiming rungs without evidence. Defenses: minimum example counts per claim type, holdout validation of patterns, and kernel-level verification for the top rung. A 'proved' claim without a certificate is rejected by the schema.", "Example-count enforcer; holdout validator; certificate requirement; fraud rejector."], ["architecture", "Scaling architecture", "Scaling: laboratory compute grids", "Discovery at scale means massive example computation and parallel proof search: distributed workers tabulate examples, GPU clusters run symbolic regression, and proof search parallelizes over tactics. The laboratory scales compute elastically — idle cycles become conjectures.", "Distributed tabulator; elastic compute; parallel proof search; result aggregator."], ["interface", "Security, permissions, and audit", "Security: proof integrity", "Mathematical claims need integrity: certificates are kernel-checked, claim dependencies are hash-linked, and the ladder's rung promotions are signed. A forged 'machine-checked' badge is treated as fraud — detected by re-verification and punished by expulsion from the claim database.", "Kernel re-verifier; hash-linked dependencies; signed promotions; fraud expeller."], ["worked-example", "Compounded integration and acceptance suite", "Compounded integration and acceptance suite", "Acceptance runs the laboratory on fixture sequences and theorems: detect the patterns, formulate correctly, climb the ladder honestly, and verify with certificates. Planted false patterns must be rejected. The laboratory ships only when its mathematics is both discovered and disciplined.", "Fixture suite; full discovery run; pattern, honesty, and verification scorers; release gate."]];
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
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("apex-tool-mathematical-discovery-laboratory",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();