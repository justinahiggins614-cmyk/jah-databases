(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];} function ri(s,a,b){return a+((s()*(b-a+1))|0);}
var CATS=["chaos-principles", "fault-types", "blast-radius", "game-days", "resilience-patterns"];
var PREFIX="JAH-SFI-";
var FIELDS=["technique", "target", "method", "safeguard", "benefit", "complexity"];
var SRC="public-harvest";
var POOL=[["Chaos Engineering Principles", "Hypothesize steady state, inject real-world faults, compare: the scientific method applied to resilience. The principles make chaos engineering, not chaos. Discipline tames the chaos.", "chaos-principles", 1, "Principles", "System", "Hypothesis + inject", "Blast radius", "Disciplined chaos", "Low"], ["Kill Random Instances", "Terminating random instances proves the system survives host loss; the classic Chaos Monkey. Survivors serve. Randomness is the teacher.", "fault-types", 1, "Instance kill", "Compute", "Random termination", "Min survivors", "Host-loss proof", "Low"], ["Network Partition Injection", "Splitting the network proves partitions are handled: split-brain must not corrupt. Partitions are the hard fault. Handling gets proven.", "fault-types", 3, "Partition", "Network", "Split brain", "Quorum rules", "Partition proof", "High"], ["Latency Injection", "Adding latency proves timeouts and retries work; slow dependencies must not cascade. Latency is the sneaky fault. Timeouts get tested.", "fault-types", 2, "Latency fault", "Dependencies", "Delay inject", "Timeout budget", "Tested timeouts", "Medium"], ["Blast Radius Control", "Experiments start tiny (one instance) and grow only with confidence; automatic halt on bad metrics. Radius is the safety. Small first.", "blast-radius", 1, "Radius control", "Experiment", "Grow with confidence", "Auto-halt", "Safe chaos", "Low"], ["Game Day Exercises", "Teams practice failures together on a schedule: the game day builds muscle memory. Practice makes resilient. Rehearsal beats panic.", "game-days", 2, "Game day", "Team + system", "Scheduled practice", "Business hours", "Muscle memory", "Medium"], ["Dependency Failure Injection", "Killing dependencies proves graceful degradation: the system must limp, not fall. Dependencies fail; grace is designed. Limping beats falling.", "fault-types", 2, "Dep kill", "Dependencies", "Remove dep", "Fallbacks", "Designed grace", "Medium"], ["Resource Exhaustion (CPU/Memory)", "Filling CPU or memory proves limits and OOM handling work; the system must degrade, not die. Exhaustion is the slow fault. Limits get proven.", "fault-types", 2, "Exhaustion", "Resources", "Fill up", "Limits + alerts", "Proven limits", "Medium"], ["Clock Skew Injection", "Skewing clocks proves time assumptions hold; distributed systems must tolerate drift. Time lies sometimes. Tolerance gets tested.", "fault-types", 3, "Skew", "Clocks", "Offset inject", "Bounded skew", "Tested tolerance", "High"], ["DNS Failure Injection", "Breaking DNS proves the system doesn't hard-depend on names; caches and IPs cover. DNS is the forgotten dependency. Forgetting gets tested.", "fault-types", 2, "DNS break", "Name resolution", "Blackhole DNS", "Caches", "Forgotten covered", "Medium"], ["Steady-State Hypothesis", "Every experiment defines steady state first (metrics in normal bounds); the hypothesis is about preserving it. Definition precedes injection. Science needs its control.", "chaos-principles", 1, "Hypothesis", "Experiment", "Define steady", "Clear abort", "Scientific", "Low"], ["Automated Halt Conditions", "Experiments halt automatically when guardrail metrics breach; humans don't need to watch. Automation is the safety net. Halts get instant.", "blast-radius", 1, "Auto-halt", "Experiment", "Guardrails", "Instant halt", "Safety net", "Low"], ["Failure Injection in CI", "Small faults run in CI on every build: the pipeline proves resilience continuously. Resilience gets tested like features. Every build proves.", "game-days", 2, "CI chaos", "Builds", "Pipeline faults", "Ephemeral env", "Continuous proof", "Medium"], ["Multi-Region Failover Drill", "Failing a whole region proves traffic moves; DNS and load balancers do the dance. Regions are expendable. Drills prove it.", "game-days", 3, "Region drill", "Traffic", "Region kill", "Other regions", "Expendable regions", "High"], ["Retry Storm Prevention", "Injecting failures tests that retries back off instead of storming; the storm is worse than the outage. Backoff gets proven. Storms get prevented.", "resilience-patterns", 2, "Storm test", "Retries", "Fail + watch", "Backoff + jitter", "Prevented storms", "Medium"], ["Circuit Breaker Validation", "Breakers must open on failure and half-open to test recovery; injection validates the state machine. Breakers get exercised. States get proven.", "resilience-patterns", 2, "Breaker test", "Breakers", "Fail + recover", "Half-open", "Exercised", "Medium"], ["Bulkhead Verification", "Bulkheads isolate failures to compartments; sinking one must not sink the ship. Compartments get flooded on purpose. Ships stay afloat.", "resilience-patterns", 2, "Flood test", "Bulkheads", "Compartment fail", "Isolation", "Afloat ships", "Medium"], ["Data Corruption Injection", "Corrupting data proves checksums and validation catch it; silent corruption is the nightmare. Nightmares get tested. Checksums get proven.", "fault-types", 3, "Corruption", "Data path", "Bit flips", "Checksums", "Tested nightmares", "High"], ["Leader Election Chaos", "Killing leaders proves elections converge fast without split-brain; leadership is the critical fault. Elections get stress-tested. Leaders get replaced.", "fault-types", 3, "Leader kill", "Consensus", "Kill leader", "Quorum", "Stress-tested", "High"], ["Chaos Dashboard", "All experiments are visible on one dashboard: what's running, blast radius, results. Visibility is the accountability. Chaos gets watched.", "chaos-principles", 1, "Dashboard", "Program", "Central view", "Visibility", "Watched chaos", "Low"]];
function generate(seed,opts,rnd){
  opts=opts||{};rnd=rnd||prng(seed);
  var cat=opts.category||pick(CATS,rnd);
  var sub=POOL.filter(function(p){return p[2]===cat;});
  var row=pick(sub.length?sub:POOL,rnd);
  var id=PREFIX+String(seed).padStart(6,'0');
  var rec={id:id,t:row[0],g:row[2],c:0,title:row[0],description:row[1],category:row[2],ladder_rank:row[3]};
  for(var i=0;i<FIELDS.length;i++){ rec[FIELDS[i]]=row[4+i]; }
  var param=ri(rnd,2,40);
  rec.demo={language:'python',code:'import random\nrandom.seed(7)\nnodes = [\"a\", \"b\", \"c\", \"d\", \"e\"]\nvictim = random.choice(nodes)\nprint(\"injecting: kill\", victim)\nalive = [n for n in nodes if n != victim]\nprint(\"system serves from:\", alive, \"(quorum kept)\")\nfor _ in range(__PARAM__):\n    pass\nprint(\"param:\", __PARAM__)\n',run:'python3'};
  rec.demo.code=rec.demo.code.replace(/__PARAM__/g,String(param));
  rec.provenance='JAH Databases lane N1 build';
  rec.last_verified='2026-10-21';
  rec.src=SRC;
  rec._seed=seed;
  return rec;
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  if(!new RegExp('^'+PREFIX.replace(/[-\/\\^$*+?.()|[\]{}]/g,'\\$&')+'\\d{6}$').test(r.id||''))e.push('id');
  if(typeof r.title!=='string'||!r.title.length)e.push('title');
  if(typeof r.description!=='string'||r.description.length<40)e.push('description');
  if(CATS.indexOf(r.category)<0)e.push('category');
  if([1,2,3].indexOf(r.ladder_rank)<0)e.push('ladder_rank');
  FIELDS.forEach(function(f){ if(typeof r[f]!=='string'||!r[f].length)e.push('field:'+f); });
  if(!r.demo||r.demo.language!=='python'||typeof r.demo.code!=='string'||!r.demo.code.length)e.push('demo');
  if(r.src!==SRC)e.push('src');
  return {ok:!e.length,errors:e};
}
var gen={version:"jahdb-system-failure-injection-1.0",generate:generate,validate:validate};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("system-failure-injection",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
