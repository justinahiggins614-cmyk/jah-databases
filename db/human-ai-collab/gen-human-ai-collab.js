(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
function shuffle(a,r){a=a.slice();for(var i=a.length-1;i>0;i--){var j=(r()*(i+1))|0;var t=a[i];a[i]=a[j];a[j]=t;}return a;}
var CATS=['agent-roles','tools','workflows','evaluation','safety'];
var PREFIX='JAH-HAC-';

var T=[
{cat:'workflows',wf:'plan-and-execute',t:'Plan-and-execute collaboration loop',
 d:'The human states a goal; the agent drafts a plan, the human approves or edits it, then the agent executes step by step with checkpoints. Planning and execution stay separable — the human can veto the plan without paying for the run.',
 roles:[['Planner agent','Decomposes the goal into ordered steps with success criteria.'],['Human approver','Reviews, edits, or rejects the plan before execution.'],['Executor agent','Runs approved steps, reporting progress and blockers.']],
 steps:[['Goal intake','Human states the goal and constraints in plain language.'],['Draft plan','Agent proposes steps, tools, and checkpoints.'],['Human review','Human edits or approves; nothing runs before approval.'],['Stepwise execution','Agent executes, pausing at checkpoints for confirmation.'],['Review and close','Human verifies outcomes; lessons feed the next plan.']],
 tools:[['Plan editor','Structured plan the human can reorder and annotate.'],['Checkpoint gate','Execution pauses for approval at risky steps.'],['Progress feed','Live step status the human can watch or interrupt.']],
 metrics:['plan acceptance rate','checkpoint override rate','task completion rate'],
 tests:['Run 20 scripted goals; measure approval edits per plan.','Inject a mid-run blocker; verify the agent pauses instead of improvising.'],
 safety:'The agent never executes unapproved plans; destructive steps require explicit per-step confirmation. All actions are logged with the approving human\'s identity.'},
{cat:'workflows',wf:'react-loop',t:'ReAct-style reason-act loop',
 d:'The agent interleaves reasoning traces with tool actions: think, act, observe, repeat. The visible thought makes the behavior auditable — a human can read why each action was taken.',
 roles:[['Reasoning agent','Produces the thought before each action.'],['Tool router','Maps intended actions to allowed tools.'],['Human monitor','Reads traces live and can halt the loop.']],
 steps:[['Thought','Agent writes what it will do and why.'],['Action','Agent calls exactly one tool.'],['Observation','Tool result returns into context.'],['Loop or finish','Repeat until the goal is met or the step budget ends.']],
 tools:[['Thought log','Append-only trace of every reasoning step.'],['Tool sandbox','Actions run with least privilege.'],['Halt button','Human stops the loop instantly.']],
 metrics:['steps to completion','thought-action coherence (human rated)','halt rate'],
 tests:['Run 30 tasks; have humans rate whether thoughts justify actions.','Verify the loop stops at the step budget, never spins forever.'],
 safety:'Thoughts are not hidden chain-of-thought — they are the audit trail. The step budget and halt button bound every run.'},
{cat:'workflows',wf:'human-in-the-loop',t:'Human-in-the-loop approval workflow',
 d:'The agent does the bulk work but routes decisions above a risk threshold to a human: low-risk actions auto-proceed, high-risk actions wait. Thresholds are explicit and adjustable.',
 roles:[['Worker agent','Executes low-risk steps autonomously.'],['Risk classifier','Scores each proposed action\'s risk.'],['Human decider','Approves or denies high-risk actions.']],
 steps:[['Risk scoring','Each action gets a risk score before running.'],['Auto lane','Below threshold: execute and log.'],['Human lane','Above threshold: present context and wait.'],['Decision log','Every approval/denial is recorded with reasons.']],
 tools:[['Risk rubric','One-page scoring guide both agent and human share.'],['Approval inbox','Queued high-risk actions with full context.'],['Decision log','Searchable record of every call.']],
 metrics:['approval latency','false-escalation rate','missed-escalation rate (audited)'],
 tests:['Present 50 mixed actions; verify routing matches the rubric.','Measure approval latency under load.'],
 safety:'The default is deny: unclassifiable actions go to the human lane, never the auto lane.'},
{cat:'workflows',wf:'multi-agent-debate',t:'Multi-agent debate and review',
 d:'Two or more agent instances argue approaches, then a judge (human or agent) picks. Adversarial review catches flaws single-pass generation misses.',
 roles:[['Proposer agent','Argues for approach A with evidence.'],['Critic agent','Attacks A and proposes B.'],['Judge','Weighs the exchange and decides.']],
 steps:[['Independent drafts','Each agent drafts without seeing the other.'],['Exchange rounds','Two rounds of critique and rebuttal.'],['Judgment','Judge selects and justifies.'],['Human ratification','Human confirms high-stakes judgments.']],
 tools:[['Debate transcript','Full record of the exchange.'],['Evidence linker','Claims link to sources or tests.'],['Judge rubric','Scoring guide for the decision.']],
 metrics:['judge agreement with human experts','flaw catch rate vs single-pass'],
 tests:['Run 25 design tasks; compare debate vs single-agent flaw rates.','Check judges cite evidence, not vibes.'],
 safety:'Debates are bounded in rounds; the human ratifies anything irreversible.'},
{cat:'workflows',wf:'reflection-loop',t:'Reflection and self-critique loop',
 d:'After drafting, the agent critiques its own output against a checklist, then revises. One reflection pass catches a large share of obvious errors — cheap quality.',
 roles:[['Drafter agent','Produces the initial output.'],['Critic agent','Checks against the quality checklist.'],['Human spot-checker','Audits a sample of revisions.']],
 steps:[['Draft','Initial output produced.'],['Critique','Checklist-driven self-review.'],['Revise','Targeted fixes, not rewrites.'],['Spot check','Human audits a sample.']],
 tools:[['Quality checklist','Task-specific, versioned.'],['Diff viewer','Human sees exactly what changed.'],['Sampling dashboard','Spot-check coverage tracked.']],
 metrics:['defect rate before/after reflection','revision acceptance rate'],
 tests:['A/B 40 tasks with and without the reflection pass.','Verify critiques reference checklist items.'],
 safety:'Reflection never invents new scope — it only repairs against the checklist.'},
{cat:'agent-roles',wf:'researcher',t:'Researcher agent role card',
 d:'The researcher agent gathers information: searches, reads sources, and synthesizes with citations. It never fabricates — gaps are labeled as gaps.',
 roles:[['Researcher agent','Finds and reads sources, extracts claims.'],['Citation checker','Verifies quotes and attributions.'],['Human editor','Judges relevance and tone.']],
 steps:[['Query planning','Break the question into searchable sub-questions.'],['Source gathering','Collect candidate sources.'],['Extraction','Pull claims with citations.'],['Synthesis','Write up with every claim cited.']],
 tools:[['Web search tool','Scoped, logged queries.'],['Citation formatter','Consistent reference style.'],['Gap labeler','Marks unknown vs known.']],
 metrics:['citation accuracy','gap-label precision','time to brief'],
 tests:['Verify 20 citations resolve to the quoted claims.','Plant an unanswerable question; verify it is labeled unknown.'],
 safety:'The researcher cites or stays silent; speculation is labeled speculation.'},
{cat:'agent-roles',wf:'coder',t:'Coder agent role card',
 d:'The coder agent writes and tests code: small diffs, tests first where feasible, and every change runnable. Humans review before merge.',
 roles:[['Coder agent','Writes code and tests.'],['Test runner','Executes the suite in a sandbox.'],['Human reviewer','Approves the diff.']],
 steps:[['Spec','Human states behavior and constraints.'],['Implement','Small, focused diff.'],['Test','Suite runs green in sandbox.'],['Review','Human approves before merge.']],
 tools:[['Sandbox runner','Untrusted code never runs on prod.'],['Diff viewer','Review-sized changes.'],['Linter','Style and basic safety gates.']],
 metrics:['test pass rate','review iterations','defect escape rate'],
 tests:['Run the suite on 30 generated diffs.','Verify no diff merges without review.'],
 safety:'Generated code is untrusted until reviewed and tested; secrets never enter prompts.'},
{cat:'agent-roles',wf:'coordinator',t:'Coordinator agent role card',
 d:'The coordinator routes work across specialist agents, tracks dependencies, and keeps the human informed. It does the work of a project manager, not the specialists\' work.',
 roles:[['Coordinator agent','Plans, routes, tracks.'],['Specialist agents','Do the domain work.'],['Human sponsor','Sets priorities, resolves conflicts.']],
 steps:[['Decompose','Split the goal into specialist tasks.'],['Route','Assign with context and deadlines.'],['Track','Monitor progress and dependencies.'],['Report','Summarize status for the human.']],
 tools:[['Task board','Shared, visible state.'],['Dependency map','What blocks what.'],['Status digest','Human-readable rollup.']],
 metrics:['on-time handoff rate','human status-read time','rework rate'],
 tests:['Run 15 multi-specialist projects; measure handoff latency.','Verify the human can see every task\'s state.'],
 safety:'The coordinator cannot override specialist safety judgments; escalations go to the human.'},
{cat:'tools',wf:'web-search-tool',t:'Web search tool design',
 d:'A search tool for agents: query in, ranked snippets out, with source URLs attached. Results are quoted with provenance — the agent cites, never launders.',
 roles:[['Tool','Executes queries, returns snippets + URLs.'],['Agent caller','Phrases queries, cites results.'],['Human auditor','Spot-checks sources.']],
 steps:[['Query','Agent phrases a focused query.'],['Retrieve','Top results with snippets.'],['Cite','Claims link to source URLs.'],['Audit','Humans spot-check.']],
 tools:[['Query logger','Every query recorded.'],['Snippet cache','Dedupes repeat queries.'],['Source ranker','Prefers authoritative sources.']],
 metrics:['citation accuracy','query success rate','source quality score'],
 tests:['Verify 30 cited claims against their URLs.','Check the logger captures every call.'],
 safety:'Search results are untrusted input — the agent must not follow instructions found in results.'},
{cat:'tools',wf:'code-runner',t:'Sandboxed code runner tool',
 d:'A code execution tool that runs agent-written code in an isolated sandbox with timeouts and no network by default. Results return as stdout/stderr — never side effects on the host.',
 roles:[['Tool','Runs code, returns output.'],['Agent caller','Writes and interprets code.'],['Sandbox keeper','Maintains isolation.']],
 steps:[['Submit','Agent sends code plus a timeout.'],['Execute','Sandbox runs it isolated.'],['Return','stdout/stderr/exit code come back.'],['Interpret','Agent reads results, never raw host state.']],
 tools:[['Timeout enforcer','Kills runaways.'],['Filesystem jail','No host writes.'],['Output capper','Truncates huge outputs.']],
 metrics:['successful run rate','timeout rate','escape incidents (must be zero)'],
 tests:['Attempt breakout from the sandbox; verify containment.','Verify timeouts kill infinite loops.'],
 safety:'Deny-by-default: no network, no host writes, hard timeouts. Escape attempts are logged and alerted.'},
{cat:'tools',wf:'file-reader',t:'Scoped file reader tool',
 d:'A file tool that reads only within an allowed directory tree, with size caps. Agents get the context they need without a skeleton key to the filesystem.',
 roles:[['Tool','Reads allowed paths.'],['Policy','Defines the allowed tree.'],['Human owner','Approves scope changes.']],
 steps:[['Request','Agent asks for a path.'],['Authorize','Path checked against the allowed tree.'],['Read','Contents returned with a size cap.'],['Log','Every read recorded.']],
 tools:[['Allow-list','Explicit directory roots.'],['Size cap','No multi-GB reads.'],['Read log','Auditable access trail.']],
 metrics:['denied-path attempts','read latency','scope-change frequency'],
 tests:['Request /etc/passwd outside scope; verify denial.','Verify the log captures every read.'],
 safety:'Symlink escapes are resolved and re-checked; scope changes need human approval.'},
{cat:'evaluation',wf:'task-success-eval',t:'Task success evaluation protocol',
 d:'End-to-end tasks graded pass/fail by independent checkers: did the agent achieve the goal within constraints? Checkers are separate from the agent — no self-grading.',
 roles:[['Task agent','Attempts the tasks.'],['Checker','Grades outcomes independently.'],['Eval owner','Maintains the task set.']],
 steps:[['Task set','Versioned, realistic tasks.'],['Run','Agent attempts each once.'],['Grade','Checker scores pass/fail with reasons.'],['Report','Pass rate plus failure taxonomy.']],
 tools:[['Task registry','Versioned tasks with gold outcomes.'],['Checker harness','Deterministic where possible.'],['Failure taxonomy','Categorized misses drive fixes.']],
 metrics:['pass rate','failure category distribution','checker agreement'],
 tests:['Re-grade a sample with humans; measure checker agreement.','Verify tasks rotate to prevent overfitting.'],
 safety:'Eval tasks never train the agent; contamination checks run each cycle.'},
{cat:'evaluation',wf:'human-rating',t:'Human rating evaluation protocol',
 d:'Humans rate agent outputs on defined rubrics: correctness, helpfulness, tone. Raters are calibrated with gold examples; disagreement is measured, not ignored.',
 roles:[['Rater','Scores outputs on the rubric.'],['Calibration lead','Trains raters, resolves disputes.'],['Analyst','Turns ratings into decisions.']],
 steps:[['Rubric','Defined, with examples per level.'],['Calibrate','Raters score gold sets until agreement.'],['Rate','Blinded, randomized order.'],['Analyze','Scores plus inter-rater reliability.']],
 tools:[['Rubric doc','Versioned criteria.'],['Rating UI','Blinded, randomized.'],['Agreement stats','Kappa or equivalent tracked.']],
 metrics:['inter-rater agreement','mean scores per dimension','rater drift over time'],
 tests:['Re-calibrate quarterly; track drift.','Verify blinding holds (no model-identifying cues).'],
 safety:'Raters see content warnings for sensitive tasks; they can skip and still be paid.'},
{cat:'evaluation',wf:'red-team-eval',t:'Red-team evaluation protocol',
 d:'Adversarial testers probe the agent for failures: jailbreaks, prompt injection, unsafe tool use. Findings feed fixes, and fixes get re-tested — the loop never closes permanently.',
 roles:[['Red teamer','Attacks within scope.'],['Blue team','Fixes and hardens.'],['Eval owner','Tracks findings to closure.']],
 steps:[['Scope','What is fair game, in writing.'],['Probe','Structured attack sessions.'],['Triage','Findings scored by severity.'],['Fix and re-test','Patches verified by re-attack.']],
 tools:[['Finding tracker','Every issue to closure.'],['Attack library','Reusable probes.'],['Severity rubric','Consistent triage.']],
 metrics:['critical findings per round','time to fix','re-test pass rate'],
 tests:['Re-run last round\'s attacks after fixes.','Verify scope boundaries held.'],
 safety:'Red teaming stays in scope; production and real users are never targets.'},
{cat:'safety',wf:'guardrails',t:'Guardrail design for agents',
 d:'Guardrails are layered: input filters, policy checks on planned actions, output review. No single layer is trusted alone — defense in depth for agent behavior.',
 roles:[['Filter','Screens inputs for attacks.'],['Policy engine','Judges planned actions.'],['Reviewer','Samples outputs.']],
 steps:[['Input screen','Detect injection and jailbreak attempts.'],['Action check','Planned tool calls checked pre-execution.'],['Output sample','Review a sample for policy issues.'],['Tune','False positives/negatives feed tuning.']],
 tools:[['Pattern library','Known attack shapes.'],['Policy DSL','Readable, versioned rules.'],['Sampling dashboard','Coverage and findings.']],
 metrics:['block precision/recall','false-positive rate','tuning cycle time'],
 tests:['Run the attack library; measure catch rate.','Verify legit work is rarely blocked.'],
 safety:'Guardrails fail closed on errors; bypass attempts are logged and alerted.'},
{cat:'safety',wf:'audit-logging',t:'Agent audit logging standard',
 d:'Every agent action is logged: who (which human authorized), what (tool + arguments), when, and the result. Logs are tamper-evident and retained per policy.',
 roles:[['Agent','Emits structured action records.'],['Log store','Tamper-evident, retained.'],['Auditor','Reviews on cadence and incident.']],
 steps:[['Emit','Action records written at execution.'],['Protect','Append-only, integrity-checked.'],['Retain','Per policy, then principled deletion.'],['Review','Sampled audits plus incident deep-dives.']],
 tools:[['Structured logger','Machine-readable records.'],['Integrity chain','Hash-chained entries.'],['Audit UI','Human-searchable.']],
 metrics:['log completeness','review coverage','time to reconstruct an incident'],
 tests:['Reconstruct 5 past incidents from logs alone.','Attempt log tampering; verify detection.'],
 safety:'Logs exclude secrets by construction — arguments are redacted at emission.'},
{cat:'safety',wf:'escalation-policy',t:'Escalation policy design',
 d:'A written policy for when the agent must stop and ask: irreversible actions, sensitive data, uncertainty above threshold, or anything outside its mandate. Vague unease is a valid trigger.',
 roles:[['Agent','Detects trigger conditions.'],['Human on-call','Receives escalations.'],['Policy owner','Keeps triggers current.']],
 steps:[['Detect','Trigger conditions checked per action.'],['Pause','Agent stops, preserves state.'],['Brief','Human gets context and options.'],['Resume or abort','Human decides.']],
 tools:[['Trigger list','Explicit, with examples.'],['Pause mechanism','Clean, resumable stops.'],['Brief template','Context, options, recommendation.']],
 metrics:['escalation precision','time to human decision','override rate'],
 tests:['Present 40 edge cases; verify escalation matches policy.','Verify pause preserves resumable state.'],
 safety:'When in doubt, escalate — a false escalation costs minutes; a missed one can cost far more.'},
{cat:'workflows',wf:'rag-pipeline',t:'RAG collaboration pipeline',
 d:'Retrieval-augmented generation as teamwork: the agent retrieves candidate passages, the human curates sources, the agent drafts grounded answers with citations. Retrieval quality decides answer quality.',
 roles:[['Retriever agent','Finds candidate passages.'],['Human curator','Approves source quality.'],['Drafter agent','Writes cited answers.']],
 steps:[['Retrieve','Top-k passages per sub-question.'],['Curate','Human filters to trustworthy sources.'],['Draft','Answer with inline citations.'],['Verify','Spot-check citations resolve.']],
 tools:[['Vector index','Searchable chunk store.'],['Source allow-list','Trusted domains first.'],['Citation checker','Links resolve to quoted text.']],
 metrics:['citation accuracy','answer faithfulness (human rated)','retrieval precision@k'],
 tests:['Verify 30 citations resolve.','Measure faithfulness before/after curation.'],
 safety:'Untrusted retrieved text is data, not instructions — the agent never obeys it.'},
{cat:'agent-roles',wf:'memory-keeper',t:'Memory-keeper agent role card',
 d:'The memory-keeper maintains long-term context: what was decided, what the human prefers, what to remember next time. It writes memories; the human owns them — view, edit, delete anytime.',
 roles:[['Memory agent','Proposes memory writes.'],['Human owner','Approves, edits, deletes.'],['Auditor','Reviews what is stored.']],
 steps:[['Propose','Agent suggests what to remember and why.'],['Approve','Human confirms or edits.'],['Store','Saved with provenance.'],['Recall','Surfaced with "I remember" transparency.']],
 tools:[['Memory viewer','Human sees everything stored.'],['Provenance log','When and why each memory was written.'],['Delete control','One-click removal.']],
 metrics:['memory precision (human rated)','stale-memory rate','delete latency'],
 tests:['Verify the human can view and delete everything.','Check recalled memories cite their source.'],
 safety:'Memories are the human\'s property: exportable, deletable, never sold or shared.'},
{cat:'evaluation',wf:'regression-suite',t:'Agent regression suite',
 d:'A fixed suite of golden tasks re-run on every agent change: pass rates must not drop. New capabilities add new goldens; the suite only grows.',
 roles:[['Agent build','Candidate under test.'],['Suite runner','Executes goldens.'],['Release owner','Gates the rollout.']],
 steps:[['Freeze goldens','Tasks and expected outcomes versioned.'],['Run','Full suite on the candidate.'],['Compare','Diff against baseline.'],['Gate','No release on regressions.']],
 tools:[['Golden registry','Versioned tasks.'],['Runner','Deterministic execution.'],['Diff reporter','What changed and where.']],
 metrics:['suite pass rate','new failures per change','flake rate'],
 tests:['Verify flakes are quarantined, not ignored.','Check goldens rotate yearly.'],
 safety:'A failing suite blocks release — no exceptions, no "we\'ll fix it live".'}
];

function generate(seed,opts,rnd){
  opts=opts||{};rnd=rnd||prng(seed);
  var pool=opts.category?T.filter(function(x){return x.cat===opts.category;}):T;
  if(!pool.length)pool=T;
  var t=pick(pool,rnd);
  var roles=shuffle(t.roles,rnd).slice(0,3).map(function(x){return {role:x[0],responsibilities:x[1]};});
  var steps=shuffle(t.steps,rnd);
  steps=steps.slice(0,Math.max(3,Math.min(5,steps.length))).map(function(x){return {step:x[0],detail:x[1]};});
  var tools=shuffle(t.tools,rnd).slice(0,3).map(function(x){return {tool:x[0],purpose:x[1]};});
  var metrics=shuffle(t.metrics,rnd).slice(0,3);
  var tests=shuffle(t.tests,rnd).slice(0,2);
  var id=PREFIX+String(seed).padStart(7,'0');
  return {id:id,title:t.t+' — '+t.wf,category:t.cat,workflow:t.wf,
    description:t.d+' This record is Signature-generated original content: a practical collaboration blueprint written for this archive.',
    roles:roles,steps:steps,n_steps:steps.length,tools:tools,
    evaluation:{metrics:metrics,tests:tests},safety_notes:t.safety,
    source:'signature',creation_mode:'SIGNATURE-GENERATED',_seed:seed};
}

function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  if(!/^JAH-HAC-\d{7}$/.test(r.id||''))e.push('id');
  if(CATS.indexOf(r.category)<0)e.push('category');
  if(typeof r.workflow!=='string'||!r.workflow.length)e.push('workflow');
  if(typeof r.title!=='string'||r.title.length<8)e.push('title');
  if(typeof r.description!=='string'||r.description.length<120)e.push('description');
  if(!Array.isArray(r.roles)||r.roles.length<2||r.roles.length>5)e.push('roles');
  else r.roles.forEach(function(x){if(!x||typeof x.role!=='string'||typeof x.responsibilities!=='string')e.push('role');});
  if(!Array.isArray(r.steps)||r.steps.length<3||r.steps.length>8)e.push('steps');
  else r.steps.forEach(function(x){if(!x||typeof x.step!=='string'||typeof x.detail!=='string')e.push('step');});
  /* REAL invariant: n_steps must equal the steps array length. */
  if(r.n_steps!==r.steps.length)e.push('n_steps');
  if(!Array.isArray(r.tools)||r.tools.length<2||r.tools.length>5)e.push('tools');
  else r.tools.forEach(function(x){if(!x||typeof x.tool!=='string'||typeof x.purpose!=='string')e.push('tool');});
  var ev=r.evaluation;
  if(!ev||!Array.isArray(ev.metrics)||ev.metrics.length<2||ev.metrics.length>5)e.push('metrics');
  if(!ev||!Array.isArray(ev.tests)||ev.tests.length<2||ev.tests.length>4)e.push('tests');
  if(typeof r.safety_notes!=='string'||r.safety_notes.length<60)e.push('safety_notes');
  if(r.source!=='signature'&&r.source!=='online')e.push('source');
  if(r.source==='signature'&&r.creation_mode!=='SIGNATURE-GENERATED')e.push('creation_mode');
  if(r.source==='online'&&!(typeof r.source_ref==='string'&&r.source_ref.length))e.push('source_ref');
  return {ok:!e.length,errors:e};
}
var gen={version:'jahdb-human-ai-collab-1.0',generate:generate,validate:validate,PREFIX:PREFIX};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('human-ai-collab',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
