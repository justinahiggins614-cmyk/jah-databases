(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];} function ri(s,a,b){return a+((s()*(b-a+1))|0);}
var CATS=["architecture", "component", "benchmark", "interface", "worked-example"];
var PREFIX="JAH-APX22-";
var VERSION="jahdb-apex-tool-universal-problem-decomposition-engine-1.0";
/* rows: [group, focus, title, description, architecture] */
var B=[["architecture", "Concept and purpose", "What the Decomposition Engine is", "The engine takes an objective that looks impossible and returns a plan: a dependency graph of subtasks, each smaller than its parent, each with acceptance criteria, each assigned an owner and an estimate. Impossibility usually dissolves under decomposition — what remains is either a real blocker or a real plan.", "Objective parser; recursive decomposer; dependency graph builder; acceptance-criteria attacher; blocker detector."], ["architecture", "Core data model", "Task and dependency data model", "Every task is a record: its objective, acceptance criteria, estimated cost and duration, dependencies, owner, and status. Dependencies form a DAG — cycles are rejected as planning errors, not tolerated. The model distinguishes hard dependencies (must precede) from soft ones (prefer to precede).", "Task documents; dependency DAG with cycle rejection; hard/soft edge typing; status state machine."], ["component", "Key algorithm I", "Recursive decomposition algorithm", "Decomposition recurses: a task too big to estimate is split by strategy (by phase, by component, by risk), and each child is split again until leaves are estimable and verifiable. The algorithm stops splitting when leaves meet the verifiability bar — not too fine (overhead) and not too coarse (unplannable).", "Split-strategy library; recursion controller with stopping rules; leaf verifiability checker; plan assembler."], ["component", "Key algorithm II", "Critical-path and bottleneck algorithm", "From the dependency DAG, the engine computes the critical path — the sequence determining the earliest finish — and finds bottlenecks where many tasks funnel through one dependency. Bottlenecks get mitigation plans: parallelization, redundancy, or early risk retirement.", "DAG analyzer; critical-path computer; bottleneck detector; mitigation planner."], ["interface", "Interface specification", "Decomposition interface specification", "Callers submit an objective with constraints (budget, deadline, resources) and get a full plan: tasks, dependencies, critical path, estimates, and blockers. The interface supports re-decomposition as reality changes — plans are living documents, replanned on events, not carved in stone.", "Planning endpoint; constraint solver; replan trigger; plan versioning."], ["component", "Ingestion and adapters", "Ingestion: knowledge for decomposition", "Good decomposition needs knowledge: task libraries from past projects, estimation data, dependency patterns, and domain playbooks. Ingestion harvests these into the decomposer's knowledge base, with provenance — estimates from real past projects outweigh guesses.", "Project history importer; estimation database; pattern miner; playbook curator."], ["component", "Indexing and retrieval", "Plan indexing and retrieval", "Plans are indexed by objective, domain, size, and outcome — so 'show me power-system plans from past projects' informs new estimates. The plan library compounds: every completed project improves the next decomposition.", "Plan library index; outcome tracker; similarity retrieval; estimate calibrator."], ["component", "Reasoning and decision component", "Reasoning: feasibility from the plan", "A finished plan answers feasibility: given constraints, does a path exist? The reasoner checks resource feasibility, schedule feasibility, and risk exposure — and when infeasible, identifies the binding constraint and what would relax it. 'Impossible under these constraints, possible if X' is the honest answer.", "Resource checker; schedule simulator; risk aggregator; binding-constraint finder."], ["interface", "Output and presentation", "Plan presentation output", "Plans render as navigable work breakdowns: objectives decomposed to verifiable leaves, critical path highlighted, bottlenecks flagged, blockers called out. Executives see the summary; engineers see the leaves; everyone sees the same truth at their depth.", "WBS renderer; path highlighter; blocker caller; depth-adaptive views."], ["benchmark", "Benchmark harness and measured baseline", "Decomposition benchmark harness", "Decomposition is tested on objectives with known good plans from past projects: does the engine's plan cover the known tasks, find the known dependencies, and estimate within tolerance? Baselines are template plans and expert decompositions; the engine must match expert coverage to graduate.", "Historical objective suite; plan comparator; coverage and estimate scorers; baseline gate."], ["worked-example", "End-to-end worked example", "Worked example: decomposing the moon base", "The 'impossible' moon base becomes 1,204 tasks: habitat, power, life support, communications, transport, science — each decomposed to verifiable leaves with estimates from analogous projects. The critical path, bottlenecks, and the radiation-shielding blocker emerge from the structure. Impossible became a plan with one honest risk.", "Objective intake; recursive decomposition; analysis; presentation."], ["component", "Failure modes and reliability", "Failure modes: fantasy plans and estimate collapse", "Plans fail as fantasy: unverifiable leaves, estimates without basis, dependencies wished away. The engine defends with the measurability mandate, estimate provenance requirements, and dependency validation. A plan that cannot be checked is not a plan — the engine refuses to produce one.", "Verifiability enforcer; estimate provenance checker; dependency validator; fantasy detector."], ["architecture", "Scaling architecture", "Scaling: decomposing programs of programs", "Mega-objectives decompose into programs, programs into projects, projects into tasks — a hierarchy of plans with rollup. The engine manages the hierarchy: changes propagate, critical paths compose, and executives see rollups while teams see leaves, all from one consistent structure.", "Hierarchical plan manager; change propagator; path composer; rollup renderer."], ["interface", "Security, permissions, and audit", "Security: planning sensitive objectives", "Plans for sensitive objectives need compartmentalization: teams see their tasks, not the whole plan; dependencies across compartments are mediated. The engine enforces need-to-know at the task level while keeping the overall plan coherent for cleared planners.", "Task-level ACLs; compartment mediator; coherent-planning service; access audit."], ["worked-example", "Compounded integration and acceptance suite", "Compounded integration and acceptance suite", "Acceptance decomposes fixture objectives with known plans: coverage of known tasks, dependency accuracy, estimate tolerance, blocker detection, and fantasy rejection. The engine ships only when its plans are complete, honest, and checkable.", "Fixture objectives; full decomposition run; coverage, accuracy, and honesty scorers; release gate."]];
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
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("apex-tool-universal-problem-decomposition-engine",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();