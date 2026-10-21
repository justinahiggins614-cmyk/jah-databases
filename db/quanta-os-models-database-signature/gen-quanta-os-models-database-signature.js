(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];} function ri(s,a,b){return a+((s()*(b-a+1))|0);}
/* Self-regulation — his standing order: hard stop at 1 trillion records,
   throttled output, simulated labeling, correctness verification,
   completion detection. */
var SELF_REG={HARD_STOP:1000000000000,MAX_BATCH:50,WINDOW_MS:60000,LABEL:'simulated'};
var _callTimes=[];
function selfRegCheck(seed){
  if(typeof seed==='number'&&seed>SELF_REG.HARD_STOP){throw new Error('generator hard stop: 1,000,000,000,000 record limit reached — generation complete');}
  var now=Date.now();_callTimes=_callTimes.filter(function(t){return now-t<SELF_REG.WINDOW_MS;});
  if(_callTimes.length>=SELF_REG.MAX_BATCH){throw new Error('generator throttled: max '+SELF_REG.MAX_BATCH+' generations per minute');}
  _callTimes.push(now);
}
var CATS=["runtime", "control", "compilation", "scheduling", "networking"];
var PREFIX='JAH-QOSMS-';
var SEEDS=[{"t": "Signature Quanta OS: The Conductor", "c": "runtime", "l": 1, "d": "Manon's Conductor concept: a quanta OS whose scheduler treats quantum and classical tasks as one orchestra \u2014 the classical optimizer and the QPU never wait on each other because the Conductor pipelines them like an assembly line. Its signature abstraction is the 'movement': a hybrid program section with declared quantum/classical phases the scheduler can interleave across jobs. Labeled Signature concept.", "f": {"origin": "Signature original by Justin Addam Higgins", "type": "Signature concept", "abstraction": "the 'movement' \u2014 declared hybrid program phases"}, "p": "// JAH demo program \u2014 Pipeline utilization\n\"use strict\";\nvar __checks=[];\nfunction check(l,g,w){__checks.push([l,g,w]);}\nfunction util(qpuBusy, cpuBusy, total){ return (qpuBusy+cpuBusy)/(2*total); }\ncheck(\"both busy \\u2192 100%\", util(10,10,10), 1);\ncheck(\"QPU idle \\u2192 50%\", util(0,10,10), 0.5);\nvar __ok=true;\n__checks.forEach(function(c){var ok=String(c[1])===String(c[2]);__ok=ok&&__ok;console.log((ok?\"PASS\":\"FAIL\")+\" | \"+c[0]+\" => \"+c[1]);});\nconsole.log(__ok?\"ALL CHECKS PASSED\":\"SOME CHECKS FAILED\");\nif(!__ok){throw new Error(\"demo self-check failed\");}", "s": ["Save the program as demo.js.", "Run it with: node demo.js", "Confirm every line prints PASS and the run ends with ALL CHECKS PASSED."]}, {"t": "Signature Quanta OS: Qubit Tenancy", "c": "scheduling", "l": 2, "d": "Manon's Qubit Tenancy concept: the OS leases qubits to programs the way landlords lease apartments \u2014 with contracts (qubit count, duration, fidelity SLA), eviction policies for hogs, and a public ledger of who holds what. A program that exceeds its fidelity budget gets migrated or paused, not silently corrupted. It applies operating-system fairness to a resource more precious than RAM. Signature concept.", "f": {"origin": "Signature original by Justin Addam Higgins", "type": "Signature concept", "lease": "qubits + duration + fidelity SLA"}, "p": "// JAH demo program \u2014 Tenancy enforcement\n\"use strict\";\nvar __checks=[];\nfunction check(l,g,w){__checks.push([l,g,w]);}\nfunction tenancy(overBudget, hogging){ if(hogging) return 'evict \u2014 hog policy';\n  if(overBudget) return 'migrate to better qubits'; return 'lease honored'; }\ncheck(\"hogging\", tenancy(false,true), \"evict \\u2014 hog policy\");\ncheck(\"over budget\", tenancy(true,false), \"migrate to better qubits\");\ncheck(\"healthy\", tenancy(false,false), \"lease honored\");\nvar __ok=true;\n__checks.forEach(function(c){var ok=String(c[1])===String(c[2]);__ok=ok&&__ok;console.log((ok?\"PASS\":\"FAIL\")+\" | \"+c[0]+\" => \"+c[1]);});\nconsole.log(__ok?\"ALL CHECKS PASSED\":\"SOME CHECKS FAILED\");\nif(!__ok){throw new Error(\"demo self-check failed\");}", "s": ["Save the program as demo.js.", "Run it with: node demo.js", "Confirm every line prints PASS and the run ends with ALL CHECKS PASSED."]}, {"t": "Signature Quanta OS: The Noise Ledger", "c": "runtime", "l": 3, "d": "Manon's Noise Ledger concept: every qubit in the system carries a live ledger of its error history \u2014 gate errors, readout errors, drift \u2014 updated by every job and readable by every scheduler. The scheduler places sensitive operations on the quietest qubits automatically, and the ledger's history makes device comparisons honest. It turns calibration from a snapshot into a reputation. Signature concept.", "f": {"origin": "Signature original by Justin Addam Higgins", "type": "Signature concept"}, "p": "// JAH demo program \u2014 Qubit reputation score\n\"use strict\";\nvar __checks=[];\nfunction check(l,g,w){__checks.push([l,g,w]);}\nfunction reputation(errors){ var avg=errors.reduce(function(s,e){return s+e;},0)/errors.length; return Math.round((1-avg)*1000)/1000; }\ncheck(\"clean qubit \\u2248 1\", reputation([0.001,0.002,0.001]), 0.999);\ncheck(\"noisy qubit lower\", reputation([0.05,0.06])<reputation([0.001,0.002]), true);\nvar __ok=true;\n__checks.forEach(function(c){var ok=String(c[1])===String(c[2]);__ok=ok&&__ok;console.log((ok?\"PASS\":\"FAIL\")+\" | \"+c[0]+\" => \"+c[1]);});\nconsole.log(__ok?\"ALL CHECKS PASSED\":\"SOME CHECKS FAILED\");\nif(!__ok){throw new Error(\"demo self-check failed\");}", "s": ["Save the program as demo.js.", "Run it with: node demo.js", "Confirm every line prints PASS and the run ends with ALL CHECKS PASSED."]}, {"t": "Signature Quanta OS: Checkpoint Everything", "c": "runtime", "l": 4, "d": "Manon's Checkpoint Everything concept: the OS snapshots hybrid jobs at every classical-quantum boundary, so a failed QPU run resumes from the last checkpoint instead of restarting the thousand-iteration loop. Checkpoints are content-addressed and portable \u2014 move the job to a different backend and resume. It treats QPU time as too precious to ever waste twice. Signature concept.", "f": {"origin": "Signature original by Justin Addam Higgins", "type": "Signature concept", "rule": "QPU time is too precious to waste twice"}, "p": "// JAH demo program \u2014 Checkpoint savings\n\"use strict\";\nvar __checks=[];\nfunction check(l,g,w){__checks.push([l,g,w]);}\nfunction saved(iters, failAt, costPer){ return (iters-failAt)*costPer; }\ncheck(\"fail at 900/1000, $0.10/iter \\u2192 $10 saved\", saved(1000,900,0.1), 10);\ncheck(\"early fail saves more\", saved(1000,100,0.1)>saved(1000,900,0.1), true);\nvar __ok=true;\n__checks.forEach(function(c){var ok=String(c[1])===String(c[2]);__ok=ok&&__ok;console.log((ok?\"PASS\":\"FAIL\")+\" | \"+c[0]+\" => \"+c[1]);});\nconsole.log(__ok?\"ALL CHECKS PASSED\":\"SOME CHECKS FAILED\");\nif(!__ok){throw new Error(\"demo self-check failed\");}", "s": ["Save the program as demo.js.", "Run it with: node demo.js", "Confirm every line prints PASS and the run ends with ALL CHECKS PASSED."]}, {"t": "Signature Quanta OS: The Honest Queue", "c": "scheduling", "l": 5, "d": "Manon's Honest Queue concept: the job scheduler shows every user their true position, the jobs ahead, and why \u2014 no 'pending' black box. It publishes the scheduling policy as executable code anyone can audit, and estimated start times come with confidence intervals. The concept argues that scarce shared hardware survives on legitimacy, and legitimacy requires transparency. Signature concept.", "f": {"origin": "Signature original by Justin Addam Higgins", "type": "Signature concept", "rule": "publish the policy as auditable code"}, "p": "// JAH demo program \u2014 Wait estimate with confidence\n\"use strict\";\nvar __checks=[];\nfunction check(l,g,w){__checks.push([l,g,w]);}\nfunction eta(ahead, avgMin){ return {low:ahead*avgMin*0.8, high:ahead*avgMin*1.5}; }\nvar e=eta(4,5);\ncheck(\"low bound 16 min\", e.low, 16);\ncheck(\"high bound 30 min\", e.high, 30);\nvar __ok=true;\n__checks.forEach(function(c){var ok=String(c[1])===String(c[2]);__ok=ok&&__ok;console.log((ok?\"PASS\":\"FAIL\")+\" | \"+c[0]+\" => \"+c[1]);});\nconsole.log(__ok?\"ALL CHECKS PASSED\":\"SOME CHECKS FAILED\");\nif(!__ok){throw new Error(\"demo self-check failed\");}", "s": ["Save the program as demo.js.", "Run it with: node demo.js", "Confirm every line prints PASS and the run ends with ALL CHECKS PASSED."]}, {"t": "Signature Quanta OS: Pulse Sandbox", "c": "control", "l": 6, "d": "Manon's Pulse Sandbox concept: a safe playground inside the OS where users design custom pulses and test them on a simulator twin of the exact QPU before touching hardware \u2014 with a 'blast radius' limiter that rejects pulses that could damage or badly miscalibrate the device. Graduation from sandbox to hardware requires passing the twin's fidelity bar. It makes pulse-level research safe for non-experts. Signature concept.", "f": {"origin": "Signature original by Justin Addam Higgins", "type": "Signature concept", "safety": "blast-radius limiter; twin fidelity bar for graduation"}, "p": "// JAH demo program \u2014 Sandbox graduation\n\"use strict\";\nvar __checks=[];\nfunction check(l,g,w){__checks.push([l,g,w]);}\nfunction graduate(twinFid, bar, safe){ if(!safe) return 'rejected \u2014 blast radius';\n  if(twinFid<bar) return 'keep tuning in sandbox'; return 'graduated to hardware'; }\ncheck(\"passes bar, safe\", graduate(0.99,0.98,true), \"graduated to hardware\");\ncheck(\"unsafe pulse\", graduate(0.99,0.98,false), \"rejected \\u2014 blast radius\");\ncheck(\"below bar\", graduate(0.90,0.98,true), \"keep tuning in sandbox\");\nvar __ok=true;\n__checks.forEach(function(c){var ok=String(c[1])===String(c[2]);__ok=ok&&__ok;console.log((ok?\"PASS\":\"FAIL\")+\" | \"+c[0]+\" => \"+c[1]);});\nconsole.log(__ok?\"ALL CHECKS PASSED\":\"SOME CHECKS FAILED\");\nif(!__ok){throw new Error(\"demo self-check failed\");}", "s": ["Save the program as demo.js.", "Run it with: node demo.js", "Confirm every line prints PASS and the run ends with ALL CHECKS PASSED."]}, {"t": "Signature Quanta OS: The Fidelity Accountant", "c": "compilation", "l": 7, "d": "Manon's Fidelity Accountant concept: a compiler pass that attaches a predicted fidelity receipt to every compiled circuit \u2014 per-gate, per-qubit, per-readout contributions itemized \u2014 before anything runs. If the receipt predicts below the user's threshold, the compiler suggests concrete fixes: fewer SWAPs, different mapping, shallower ansatz. It makes fidelity a compile-time conversation. Signature concept.", "f": {"origin": "Signature original by Justin Addam Higgins", "type": "Signature concept"}, "p": "// JAH demo program \u2014 Receipt total\n\"use strict\";\nvar __checks=[];\nfunction check(l,g,w){__checks.push([l,g,w]);}\nfunction receipt(items){ return items.reduce(function(s,i){return s*i;},1); }\ncheck(\"three 99% gates \\u2192 97%\", Math.round(receipt([0.99,0.99,0.99])*100), 97);\ncheck(\"readout dominates at scale\", receipt([0.99,0.99,0.9])<receipt([0.99,0.99,0.99]), true);\nvar __ok=true;\n__checks.forEach(function(c){var ok=String(c[1])===String(c[2]);__ok=ok&&__ok;console.log((ok?\"PASS\":\"FAIL\")+\" | \"+c[0]+\" => \"+c[1]);});\nconsole.log(__ok?\"ALL CHECKS PASSED\":\"SOME CHECKS FAILED\");\nif(!__ok){throw new Error(\"demo self-check failed\");}", "s": ["Save the program as demo.js.", "Run it with: node demo.js", "Confirm every line prints PASS and the run ends with ALL CHECKS PASSED."]}, {"t": "Signature Quanta OS: Sleep Mode for Qubits", "c": "control", "l": 8, "d": "Manon's Sleep Mode concept: idle qubits are dynamically decoupled into protected states instead of sitting exposed to noise \u2014 the OS 'parks' qubits a job isn't using yet, cutting their effective error rate while they wait. Wake-up is a calibrated pulse sequence, and the scheduler accounts for wake latency. It treats qubit coherence as a budget the OS actively manages. Signature concept.", "f": {"origin": "Signature original by Justin Addam Higgins", "type": "Signature concept"}, "p": "// JAH demo program \u2014 Parking benefit\n\"use strict\";\nvar __checks=[];\nfunction check(l,g,w){__checks.push([l,g,w]);}\nfunction effectiveErr(rawErr, parked){ return parked?rawErr/5:rawErr; }\ncheck(\"parked qubit 5x quieter\", effectiveErr(0.01,true), 0.002);\ncheck(\"unparked unchanged\", effectiveErr(0.01,false), 0.01);\nvar __ok=true;\n__checks.forEach(function(c){var ok=String(c[1])===String(c[2]);__ok=ok&&__ok;console.log((ok?\"PASS\":\"FAIL\")+\" | \"+c[0]+\" => \"+c[1]);});\nconsole.log(__ok?\"ALL CHECKS PASSED\":\"SOME CHECKS FAILED\");\nif(!__ok){throw new Error(\"demo self-check failed\");}", "s": ["Save the program as demo.js.", "Run it with: node demo.js", "Confirm every line prints PASS and the run ends with ALL CHECKS PASSED."]}, {"t": "Signature Quanta OS: The Rosetta Driver", "c": "control", "l": 9, "d": "Manon's Rosetta Driver concept: a hardware-abstraction layer that lets one program run on superconducting, ion-trap, photonic, and neutral-atom backends \u2014 translating gates, connectivity, and even error models per target. 'Write once, run anywhere' for quantum, with a performance report per backend so the user sees what portability costs. Signature concept.", "f": {"origin": "Signature original by Justin Addam Higgins", "type": "Signature concept"}, "p": "// JAH demo program \u2014 Portability cost report\n\"use strict\";\nvar __checks=[];\nfunction check(l,g,w){__checks.push([l,g,w]);}\nfunction costReport(native, ported){ return {overhead:ported-native, ratio:Math.round(ported/native*100)/100}; }\nvar r=costReport(100,140);\ncheck(\"40 extra gates\", r.overhead, 40);\ncheck(\"1.4x ratio\", r.ratio, 1.4);\nvar __ok=true;\n__checks.forEach(function(c){var ok=String(c[1])===String(c[2]);__ok=ok&&__ok;console.log((ok?\"PASS\":\"FAIL\")+\" | \"+c[0]+\" => \"+c[1]);});\nconsole.log(__ok?\"ALL CHECKS PASSED\":\"SOME CHECKS FAILED\");\nif(!__ok){throw new Error(\"demo self-check failed\");}", "s": ["Save the program as demo.js.", "Run it with: node demo.js", "Confirm every line prints PASS and the run ends with ALL CHECKS PASSED."]}, {"t": "Signature Quanta OS: Entanglement Post Office", "c": "networking", "l": 10, "d": "Manon's Entanglement Post Office concept: the OS manages distributed Bell pairs like mail \u2014 generated, addressed to node pairs, tracked with sequence numbers, and delivered with fidelity stamps. Programs request entanglement the way they request memory; the post office handles generation, purification, and routing. It makes the quantum network programmable. Signature concept.", "f": {"origin": "Signature original by Justin Addam Higgins", "type": "Signature concept"}, "p": "// JAH demo program \u2014 Post office throughput\n\"use strict\";\nvar __checks=[];\nfunction check(l,g,w){__checks.push([l,g,w]);}\nfunction pairsPerSec(rate, fid, minFid){ return fid>=minFid?rate:0; }\ncheck(\"good pairs flow\", pairsPerSec(100,0.95,0.9), 100);\ncheck(\"bad pairs rejected\", pairsPerSec(100,0.8,0.9), 0);\nvar __ok=true;\n__checks.forEach(function(c){var ok=String(c[1])===String(c[2]);__ok=ok&&__ok;console.log((ok?\"PASS\":\"FAIL\")+\" | \"+c[0]+\" => \"+c[1]);});\nconsole.log(__ok?\"ALL CHECKS PASSED\":\"SOME CHECKS FAILED\");\nif(!__ok){throw new Error(\"demo self-check failed\");}", "s": ["Save the program as demo.js.", "Run it with: node demo.js", "Confirm every line prints PASS and the run ends with ALL CHECKS PASSED."]}, {"t": "Signature Quanta OS: The Calibration Market", "c": "scheduling", "l": 11, "d": "Manon's Calibration Market concept: QPU time is priced dynamically \u2014 fresh-calibration slots cost more, stale slots cost less, and users bid with priority points instead of money. The market clears every scheduling round, and the price history is public. It rations scarce premium hardware without a committee, using the oldest fair mechanism there is. Signature concept.", "f": {"origin": "Signature original by Justin Addam Higgins", "type": "Signature concept"}, "p": "// JAH demo program \u2014 Market clearing (toy)\n\"use strict\";\nvar __checks=[];\nfunction check(l,g,w){__checks.push([l,g,w]);}\nfunction clear(bids, slots){ bids.sort(function(a,b){return b-a;}); return bids.slice(0,slots); }\nvar win=clear([5,9,3,12,7],2);\ncheck(\"top 2 bids win\", win.join(','), \"12,9\");\ncheck(\"losers wait\", win.length, 2);\nvar __ok=true;\n__checks.forEach(function(c){var ok=String(c[1])===String(c[2]);__ok=ok&&__ok;console.log((ok?\"PASS\":\"FAIL\")+\" | \"+c[0]+\" => \"+c[1]);});\nconsole.log(__ok?\"ALL CHECKS PASSED\":\"SOME CHECKS FAILED\");\nif(!__ok){throw new Error(\"demo self-check failed\");}", "s": ["Save the program as demo.js.", "Run it with: node demo.js", "Confirm every line prints PASS and the run ends with ALL CHECKS PASSED."]}, {"t": "Signature Quanta OS: Crash-Only Qubits", "c": "runtime", "l": 12, "d": "Manon's Crash-Only concept, borrowed from classic systems design: quanta programs are written so any qubit can be re-initialized at any time without corrupting the computation \u2014 no graceful teardown, just crash and rebuild from checkpoints. The OS kills and restarts flaky qubits mid-job instead of nursing them. It trades elegance for the reality that qubits are the flakiest components ever put in a computer. Signature concept.", "f": {"origin": "Signature original by Justin Addam Higgins", "type": "Signature concept", "rule": "any qubit re-initializable at any time"}, "p": "// JAH demo program \u2014 Restart vs nurse\n\"use strict\";\nvar __checks=[];\nfunction check(l,g,w){__checks.push([l,g,w]);}\nfunction downtime(restarts, restartMs, nurseMs){ return restarts*restartMs<nurseMs; }\ncheck(\"3 quick restarts beat nursing\", downtime(3,50,500), true);\ncheck(\"slow restarts lose\", downtime(3,500,500), false);\nvar __ok=true;\n__checks.forEach(function(c){var ok=String(c[1])===String(c[2]);__ok=ok&&__ok;console.log((ok?\"PASS\":\"FAIL\")+\" | \"+c[0]+\" => \"+c[1]);});\nconsole.log(__ok?\"ALL CHECKS PASSED\":\"SOME CHECKS FAILED\");\nif(!__ok){throw new Error(\"demo self-check failed\");}", "s": ["Save the program as demo.js.", "Run it with: node demo.js", "Confirm every line prints PASS and the run ends with ALL CHECKS PASSED."]}, {"t": "Signature Quanta OS: The Audit Trail", "c": "runtime", "l": 13, "d": "Manon's Audit Trail concept: every quantum job records an immutable trail \u2014 circuit hash, calibration snapshot, transpiler version, seed, results \u2014 so any result can be reproduced or challenged years later. 'A quantum result without a trail is a rumor.' The trail is the foundation of the field's credibility as results get harder to verify classically. Signature concept.", "f": {"origin": "Signature original by Justin Addam Higgins", "type": "Signature concept", "rule": "a result without a trail is a rumor"}, "p": "// JAH demo program \u2014 Trail completeness\n\"use strict\";\nvar __checks=[];\nfunction check(l,g,w){__checks.push([l,g,w]);}\nfunction complete(trail){ var need=['circuit','calibration','transpiler','seed','results'];\n  return need.filter(function(k){return trail[k];}).length; }\ncheck(\"full trail = 5\", complete({circuit:1,calibration:1,transpiler:1,seed:1,results:1}), 5);\ncheck(\"missing seed = 4\", complete({circuit:1,calibration:1,transpiler:1,results:1}), 4);\nvar __ok=true;\n__checks.forEach(function(c){var ok=String(c[1])===String(c[2]);__ok=ok&&__ok;console.log((ok?\"PASS\":\"FAIL\")+\" | \"+c[0]+\" => \"+c[1]);});\nconsole.log(__ok?\"ALL CHECKS PASSED\":\"SOME CHECKS FAILED\");\nif(!__ok){throw new Error(\"demo self-check failed\");}", "s": ["Save the program as demo.js.", "Run it with: node demo.js", "Confirm every line prints PASS and the run ends with ALL CHECKS PASSED."]}, {"t": "Signature Quanta OS: The Quiet Hours", "c": "scheduling", "l": 14, "d": "Manon's Quiet Hours concept: the scheduler reserves nightly windows for long, delicate jobs \u2014 deep circuits, precision metrology \u2014 when the lab is thermally stable and nobody is opening fridge doors. Daytime gets the short interactive jobs. The concept treats environmental stability as a schedulable resource, which, the proposal notes, it physically is. Signature concept.", "f": {"origin": "Signature original by Justin Addam Higgins", "type": "Signature concept"}, "p": "// JAH demo program \u2014 Job placement\n\"use strict\";\nvar __checks=[];\nfunction check(l,g,w){__checks.push([l,g,w]);}\nfunction place(depth, delicate){ if(depth>50||delicate) return 'quiet hours (02:00\u201306:00)';\n  return 'daytime interactive queue'; }\ncheck(\"deep circuit \\u2192 night\", place(100,false), \"quiet hours (02:00\\u201306:00)\");\ncheck(\"delicate \\u2192 night\", place(10,true), \"quiet hours (02:00\\u201306:00)\");\ncheck(\"shallow test \\u2192 day\", place(5,false), \"daytime interactive queue\");\nvar __ok=true;\n__checks.forEach(function(c){var ok=String(c[1])===String(c[2]);__ok=ok&&__ok;console.log((ok?\"PASS\":\"FAIL\")+\" | \"+c[0]+\" => \"+c[1]);});\nconsole.log(__ok?\"ALL CHECKS PASSED\":\"SOME CHECKS FAILED\");\nif(!__ok){throw new Error(\"demo self-check failed\");}", "s": ["Save the program as demo.js.", "Run it with: node demo.js", "Confirm every line prints PASS and the run ends with ALL CHECKS PASSED."]}, {"t": "Signature Quanta OS: The Onboarding Simulator", "c": "runtime", "l": 15, "d": "Manon's Onboarding Simulator concept: before a new user touches real QPU time, they qualify in a simulator twin that behaves like the device \u2014 same gate set, same noise model, same queue. The twin scores their circuits' efficiency and only graduates users whose jobs would not waste the hardware. It protects the scarce resource while training the next generation. This database's simulator is its prototype. Signature concept.", "f": {"origin": "Signature original by Justin Addam Higgins", "type": "Signature concept"}, "p": "// JAH demo program \u2014 Graduation score\n\"use strict\";\nvar __checks=[];\nfunction check(l,g,w){__checks.push([l,g,w]);}\nfunction gradScore(efficiency, waste){ return Math.round(efficiency*100-waste*10); }\ncheck(\"90% efficient, 1 waste \\u2192 80\", gradScore(0.9,1), 80);\ncheck(\"graduation bar at 70\", gradScore(0.9,1)>=70, true);\nvar __ok=true;\n__checks.forEach(function(c){var ok=String(c[1])===String(c[2]);__ok=ok&&__ok;console.log((ok?\"PASS\":\"FAIL\")+\" | \"+c[0]+\" => \"+c[1]);});\nconsole.log(__ok?\"ALL CHECKS PASSED\":\"SOME CHECKS FAILED\");\nif(!__ok){throw new Error(\"demo self-check failed\");}", "s": ["Save the program as demo.js.", "Run it with: node demo.js", "Confirm every line prints PASS and the run ends with ALL CHECKS PASSED."]}];
var GEN_VARIANTS=["Signature concept sketch", "Signature prototype notes", "Signature v2 idea", "Signature field test", "Signature crossover", "Signature minimal version"];
var GEN_PROV="Signature simulated record - boundless generator output; labeled simulated for weeding per standing order. Verified by generator self-check 2026-10-21.";
var GEN_LIC="Signature original by Justin Addam Higgins.";
var SRC_EDITION="signature";
function generate(seed,opts,rnd){
  selfRegCheck(seed);
  opts=opts||{};rnd=rnd||prng(seed);
  var cat=opts.category||pick(CATS,rnd);
  var pool=SEEDS.filter(function(s){return s.c===cat;});
  var sd=pick(pool.length?pool:SEEDS,rnd);
  var variant=pick(GEN_VARIANTS,rnd);
  var id=PREFIX+String(seed).padStart(6,'0');
  var ladder=sd.l+ri(rnd,-2,2);if(ladder<1)ladder=1;if(ladder>15)ladder=15;
  var rec={
    id:id,
    title:sd.t+' \u2014 '+variant,
    ladder_rank:ladder,
    category:cat,
    description:'Simulated '+(SRC_EDITION==='signature'?'Signature-style':'public-style')+' variant ('+variant+') of the archive record \u201c'+sd.t+'\u201d. '+sd.d,
    fields:sd.f,
    demo:{language:'javascript',program:sd.p,run_steps:sd.s,expected_output:'ALL CHECKS PASSED'},
    march:'March to a million in progress \u2014 generated record (seed '+seed+'), marching toward the 1,000,000-record target.',
    provenance:GEN_PROV,
    licensing:GEN_LIC,
    source_edition:SRC_EDITION,
    last_verified:'2026-10-21',
    simulated:true
  };
  rec._seed=seed;
  var v=validate(rec);
  if(!v.ok){throw new Error('generator self-check failed: '+v.errors.join(', '));}
  return rec;
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  var idre=new RegExp('^'+PREFIX.replace(/[.*+?^${}()|[\]\\]/g,'\\$&')+'\\d{6}$');
  if(!idre.test(r.id||''))e.push('id');
  if(typeof r.title!=='string'||!r.title.length)e.push('title');
  if(CATS.indexOf(r.category)<0)e.push('category');
  if(!(r.ladder_rank>=1&&r.ladder_rank<=15))e.push('ladder_rank');
  if(typeof r.description!=='string'||r.description.length<40)e.push('description');
  if(r.simulated!==true)e.push('simulated-label');
  if(!r.demo||typeof r.demo.program!=='string'||r.demo.program.length<40)e.push('demo');
  if(r.last_verified!=='2026-10-21')e.push('last_verified');

  return {ok:!e.length,errors:e};
}
function driftCheck(rec,sample){
  sample=sample||[];
  var t=String(rec.title||'').toLowerCase();
  for(var i=0;i<sample.length;i++){
    if(String(sample[i].title||'').toLowerCase()===t){return {ok:false,errors:['duplicate of archive title: '+sample[i].title]};}
  }
  return {ok:true,errors:[]};
}

var QuantaSim=(function(){
'use strict';
/* ================= utilities ================= */
function sHash(s){var h=2166136261;for(var i=0;i<s.length;i++){h^=s.charCodeAt(i);h=Math.imul(h,16777619);}return h>>>0;}
function sRng(seed){var a=sHash(String(seed))||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function fmtN(x,d){if(!isFinite(x))return String(x);var p=Math.pow(10,d==null?4:d);return String(Math.round(x*p)/p);}
/* safe expression evaluator: numbers, + - * / ^ % ( ) sqrt sin cos tan log */
function evalExpr(src){
  var toks=String(src).match(/(\d+\.?\d*|\.\d+|[A-Za-z_]\w*|[+\-*/^%(),])/g)||[];
  var pos=0;
  function peek(){return toks[pos];} function next(){return toks[pos++];}
  function parseE(){var v=parseT();while(peek()==='+'||peek()==='-'){var o=next();var r=parseT();v=o==='+'?v+r:v-r;}return v;}
  function parseT(){var v=parseP();while(peek()==='*'||peek()==='/'||peek()==='%'){var o=next();var r=parseP();v=o==='*'?v*r:(o==='/'?v/r:v%r);}return v;}
  function parseP(){var v=parseU();if(peek()==='^'){next();var r=parseP();v=Math.pow(v,r);}return v;}
  function parseU(){var t=peek();if(t==='-'){next();return -parseU();}if(t==='+'){next();return parseU();}
    if(t==='('){next();var v=parseE();if(next()!==')')throw new Error('missing )');return v;}
    if(/^[A-Za-z_]/.test(t||'')){next();var f=t.toLowerCase();
      if(peek()==='('){next();var a=parseE();if(next()!==')')throw new Error('missing )');
        var F={sqrt:Math.sqrt,sin:Math.sin,cos:Math.cos,tan:Math.tan,log:Math.log,exp:Math.exp,abs:Math.abs};
        if(!F[f])throw new Error('unknown function '+f);return F[f](a);}
      var C={pi:Math.PI,e:Math.E};if(C[f]!=null)return C[f];throw new Error('unknown name '+f);}
    if(/^\d/.test(t||'')){next();return parseFloat(t);}
    throw new Error('unexpected '+(t==null?'end':t));}
  var v=parseE();if(pos<toks.length)throw new Error('trailing input');
  return v;
}
/* complex numbers for the state-vector lab */
function C(re,im){return {re:re,im:im||0};}
function cadd(a,b){return C(a.re+b.re,a.im+b.im);}
function cmul(a,b){return C(a.re*b.re-a.im*b.im,a.re*b.im+a.im*b.re);}
function cprob(a){return a.re*a.re+a.im*a.im;}
/* 2-qubit state vector simulator: state[4] over |00>,|01>,|10>,|11> (q0 = leftmost bit) */
function newState(){return [C(1),C(0),C(0),C(0)];}
function apply1(st,q,mat){ /* mat: [[a,b],[c,d]] on qubit q */
  var n=[C(0),C(0),C(0),C(0)];
  for(var i=0;i<4;i++){var bit=(i>>(1-q))&1;
    for(var nb=0;nb<2;nb++){var j=(i&(~(1<<(1-q))))|(nb<<(1-q));
      n[j]=cadd(n[j],cmul(mat[bit][nb],st[i]));}}
  for(var k=0;k<4;k++)st[k]=n[k];return st;}
function applyCNOT(st,c,t){
  var n=[C(0),C(0),C(0),C(0)];
  for(var i=0;i<4;i++){var cb=(i>>(1-c))&1;var j=cb?i^(1<<(1-t)):i;n[j]=cadd(n[j],st[i]);}
  for(var k=0;k<4;k++)st[k]=n[k];return st;}
var SQ1=Math.SQRT1_2;
var GATES={
  H:[[C(SQ1),C(SQ1)],[C(SQ1),C(-SQ1)]],
  X:[[C(0),C(1)],[C(1),C(0)]],
  Z:[[C(1),C(0)],[C(0),C(-1)]],
  S:[[C(1),C(0)],[C(0),C(0,1)]],
  T:[[C(1),C(0)],[C(0),C(SQ1,SQ1)]]
};
function runCircuit(src){
  var st=newState();var steps=[];
  var lines=String(src).split(/[\n;]+/);
  lines.forEach(function(ln){
    var p=ln.trim().split(/\s+/);if(!p[0])return;
    var g=p[0].toUpperCase();
    if(g==='CNOT'&&p.length>=3){applyCNOT(st,+p[1],+p[2]);steps.push('CNOT '+p[1]+' '+p[2]);}
    else if(g==='RX'&&p.length>=3){var th=parseFloat(p[2]);var q=+p[1];
      apply1(st,q,[[C(Math.cos(th/2)),C(0,-Math.sin(th/2))],[C(0,-Math.sin(th/2)),C(Math.cos(th/2))]]);steps.push('RX('+th+') q'+q);}
    else if(GATES[g]&&p.length>=2){apply1(st,+p[1],GATES[g]);steps.push(g+' q'+p[1]);}
    else throw new Error('bad gate line: '+ln);
  });
  var labels=['00','01','10','11'];
  var out=['2-qubit state after '+steps.length+' gate(s): '+steps.join(', ')];
  var tot=0;
  for(var i=0;i<4;i++){var pr=cprob(st[i]);tot+=pr;
    out.push('|'+labels[i]+'>  P='+fmtN(pr)+'  amp='+fmtN(st[i].re)+((st[i].im>=0?'+':'')+fmtN(st[i].im)+'i'));}
  out.push('total probability = '+fmtN(tot)+' (must be 1)');
  return out.join('\n');
}
/* ================= virtual FS ================= */
function makeFS(){
  var F={'/':{d:1}};
  function add(p,content){F[p]={d:0,content:String(content)};}
  add('/readme.txt','QuantaOS '+"signature"+' — simulated quanta desktop.\nEvery app below genuinely runs in this page.');
  add('/notes.txt','- Grover gives quadratic speedup for unstructured search.\n- BB84 key exchange is information-theoretically secure.');
  add('/circuits/bell.txt','H 0\nCNOT 0 1');
  add('/circuits/ghz2.txt','H 0\nCNOT 0 1');
  return {
    ls:function(p){p=p||'/';var out=[];Object.keys(F).forEach(function(k){
      if(k!==p&&k.indexOf(p)===0){var rest=k.slice(p.length).replace(/^\//,'');
        var seg=rest.split('/')[0];if(seg&&out.indexOf(seg)<0)out.push(seg+(F[k].d?'/':''));}});
      return out.length?out.join('  '):'(empty)';},
    cat:function(p){if(!F[p]||F[p].d)throw new Error('no such file: '+p);return F[p].content;},
    write:function(p,c){add(p,c);return 'wrote '+c.length+' chars to '+p;}
  };
}
/* ================= app registry ================= */
var APPS={};
function defApp(id,name,icon,help,run){APPS[id]={id:id,name:name,icon:icon,help:help,run:run};}
defApp('terminal','Quanta Terminal','\u2328',
 'help | apps | echo <t> | calc <expr> | run <app> <args> | qubits | whoami | clear',
 function(input,ctx){
  var p=String(input||'').trim().split(/\s+/);var c=(p[0]||'').toLowerCase();
  if(c===''||c==='help')return 'commands: help, apps, echo <text>, calc <expr>, run <app> <args>, qubits, whoami, clear';
  if(c==='apps')return api.apps().map(function(a){return a.id+' — '+a.name;}).join('\n');
  if(c==='echo')return p.slice(1).join(' ');
  if(c==='calc'){try{return String(fmtN(evalExpr(p.slice(1).join(' '))));}catch(e){return 'calc error: '+e.message;}}
  if(c==='run'){var id=p[1];if(!APPS[id])return 'no such app: '+id;try{return APPS[id].run(p.slice(2).join(' '),ctx);}catch(e){return id+' error: '+e.message;}}
  if(c==='qubits')return 'virtual QPU: 2 simulated qubits, state-vector backend (classical simulation)';
  if(c==='whoami')return 'quanta-operator@quanta-desktop';
  if(c==='clear')return '';
  return 'unknown command: '+c+' (try help)';
 });
defApp('calc','Quanta Calculator','\u03BB',
 'Evaluate math: 2+2*2, sqrt(16), sin(pi/2), 2^10',
 function(input){ if(!String(input).trim())return 'type an expression, e.g. 2+2*2';
  try{return String(input).trim()+' = '+fmtN(evalExpr(input));}catch(e){return 'error: '+e.message;} });
defApp('circuit','Quantum Circuit Lab','\u269B',
 'One gate per line: H q | X q | Z q | S q | T q | RX q theta | CNOT c t   (2 qubits, q = 0 or 1). Real state-vector math.',
 function(input){ if(!String(input).trim())return 'enter gates, e.g.:\nH 0\nCNOT 0 1';
  try{return runCircuit(input);}catch(e){return 'circuit error: '+e.message;} });
defApp('explorer','File Explorer','\uD83D\uDDC0',
 'ls [path] | open <path>',
 function(input,ctx){var p=String(input||'').trim().split(/\s+/);
  if(p[0]==='open'&&p[1]){try{return ctx.fs.cat(p[1]);}catch(e){return e.message;}}
  return ctx.fs.ls(p[0]==='ls'?(p[1]||'/'):(p[0]||'/'));});
defApp('editor','Text Editor','\u270E',
 'open <path> | write <path> <text>',
 function(input,ctx){var s=String(input||'').trim();
  if(s.indexOf('write ')===0){var rest=s.slice(6);var sp=rest.indexOf(' ');
    if(sp<0)return 'usage: write <path> <text>';
    return ctx.fs.write(rest.slice(0,sp),rest.slice(sp+1));}
  if(s.indexOf('open ')===0){try{return ctx.fs.cat(s.slice(5).trim());}catch(e){return e.message;}}
  return 'usage: open <path> | write <path> <text>';});
var _bootT=Date.now();
defApp('monitor','System Monitor','\uD83D\uDCCA',
 'Live virtual-QPU stats (no input needed)',
 function(input,ctx){var r=sRng('mon'+Math.floor(Date.now()/4000));
  return ['virtual QPU status ('+"signature"+')',
   'qubits simulated : 2 (state-vector)',
   'jobs queued      : '+Math.floor(r()*4),
   'coherence util   : '+fmtN(80+r()*19,1)+'%',
   'cryo stage       : '+fmtN(0.012+r()*0.004,3)+' K (simulated)',
   'uptime           : '+Math.floor((Date.now()-_bootT)/1000)+' s'].join('\n');});
defApp('settings','Settings','\u2699',
 'theme dark|light | about',
 function(input){var p=String(input||'').trim().toLowerCase();
  if(p==='about')return 'QuantaOS '+"signature"+' — simulated quanta desktop running entirely in this page.';
  if(p==='theme dark'||p==='theme light')return 'theme set: '+p.split(' ')[1]+' (applies to new windows)';
  return 'usage: theme dark|light | about';});

defApp('sched','Job Scheduler','\uD83D\uDDC2',
 'Simulate the fair-share quantum job queue. Input: jobs=<n>  (e.g. jobs=6)',
 function(input){var m=String(input||'').match(/jobs\s*=\s*(\d+)/);var n=m?Math.min(12,Math.max(1,+m[1])):6;
  var r=sRng('sched'+n);var jobs=[];
  for(var i=0;i<n;i++)jobs.push({id:'job-'+(1000+i),shots:1000+Math.floor(r()*7000),prio:1+Math.floor(r()*3),user:'user'+(1+Math.floor(r()*3))});
  jobs.sort(function(a,b){return a.prio-b.prio||a.shots-b.shots;});
  var t=0;var out=['fair-share queue: '+n+' jobs (sorted by priority, then shots)'];
  jobs.forEach(function(j){var wait=t;var dur=Math.round(j.shots/4000*10)/10;t+=dur;
    out.push(j.id+' ['+j.user+' prio='+j.prio+' shots='+j.shots+'] wait='+wait.toFixed(1)+'s run='+dur+'s');});
  out.push('makespan: '+t.toFixed(1)+'s — real queueing simulation');return out.join('\n');});
defApp('procs','Process Manager','\u2699',
 'List quanta processes. Input: list | kill <pid>',
 function(input,ctx){ctx._procs=ctx._procs||[
    {pid:101,cmd:'qpu-driver',q:'2qb'},
    {pid:204,cmd:'transpiler',q:'-'},
    {pid:317,cmd:'zne-service',q:'-'},
    {pid:422,cmd:'user-circuit',q:'2qb'}];
  var p=String(input||'').trim().split(/\s+/);
  if(p[0]==='kill'&&p[1]){var i=ctx._procs.findIndex(function(x){return x.pid===+p[1];});
    if(i<0)return 'no such pid: '+p[1];var k=ctx._procs.splice(i,1)[0];return 'killed '+k.pid+' ('+k.cmd+')';}
  return 'PID   CMD           QUBITS\n'+ctx._procs.map(function(x){return String(x.pid).padEnd(6)+x.cmd.padEnd(14)+x.q;}).join('\n');});
defApp('ctrlstack','Control Stack','\uD83D\uDCE1',
 'Show the quanta control stack layers. Input: layers | ping',
 function(input){var p=String(input||'').trim().toLowerCase();
  var layers=[['L5 application','Qiskit/Cirq program','—'],
   ['L4 runtime','hybrid job manager','~50 ms'],
   ['L3 compiler','transpiler → basis {U,CX}','~5 ms'],
   ['L2 firmware','FPGA sequencer / AWG','~1 us'],
   ['L1 cryo-electronics','cryo-CMOS mux','~100 ns'],
   ['L0 QPU','2 simulated qubits','gate ~40 ns (simulated)']];
  if(p==='ping'){var r=sRng('ping'+Date.now()%97);
    return 'round trip application → QPU → application: '+fmtN(52+r()*8,1)+' ms (simulated)';}
  return 'quanta control stack (top to bottom):\n'+layers.map(function(l){return l[0].padEnd(20)+l[1].padEnd(28)+'latency '+l[2];}).join('\n');});

/* ================= API ================= */
var _fs=makeFS();
var api={
  edition:"signature",
  apps:function(){return Object.keys(APPS).map(function(k){return {id:k,name:APPS[k].name,icon:APPS[k].icon};});},
  help:function(id){return APPS[id]?APPS[id].help:'no such app';},
  run:function(id,input){if(!APPS[id])throw new Error('no such app: '+id);
    return APPS[id].run(input==null?'':input,{fs:_fs,api:api});}
};
/* ================= DOM ================= */
function el(tag,cls,html){var d=document.createElement(tag);if(cls)d.className=cls;if(html!=null)d.innerHTML=html;return d;}
function mount(host){
  host.innerHTML='';
  var desk=el('div','qsim-desktop');host.appendChild(desk);
  var icons=el('div','qsim-icons');desk.appendChild(icons);
  var taskbar=el('div','qsim-taskbar');desk.appendChild(taskbar);
  var zTop=10;
  function openWin(appId){
    var app=APPS[appId];if(!app)return;
    var w=el('div','qsim-win');w.style.zIndex=++zTop;
    w.style.left=(20+ (zTop*37)%220)+'px';w.style.top=(16+(zTop*29)%120)+'px';w.style.width='380px';
    var tb=el('div','tbar','<span>'+app.icon+' '+app.name+'</span><button style="padding:2px 8px">\u2715</button>');
    var body=el('div','tbody');
    var pre=el('pre','',app.help);body.appendChild(pre);
    var row=el('div','row');var inp=document.createElement('input');
    inp.style.flex='1';inp.placeholder='type input, Enter to run';row.appendChild(inp);
    var go=el('button','go','Run');row.appendChild(go);body.appendChild(row);
    w.appendChild(tb);w.appendChild(body);desk.appendChild(w);
    var fs=makeFS();
    function runIt(){var v=inp.value;inp.value='';
      var out=el('div');out.innerHTML='<div class="dim">&gt; '+String(v).replace(/[<>&]/g,function(c){return {'<':'&lt;','>':'&gt;','&':'&amp;'}[c];})+'</div>';
      body.insertBefore(out,row);
      try{var r=app.run(v,{fs:fs,api:api});var o=el('pre','',String(r).replace(/[<>&]/g,function(c){return {'<':'&lt;','>':'&gt;','&':'&amp;'}[c];}));body.insertBefore(o,row);}
      catch(e){var er=el('div','bad','error: '+e.message);body.insertBefore(er,row);}
      body.scrollTop=body.scrollHeight;}
    go.addEventListener('click',runIt);
    inp.addEventListener('keydown',function(e){if(e.key==='Enter')runIt();});
    tb.querySelector('button').addEventListener('click',function(){w.remove();});
    tb.addEventListener('mousedown',function(e){if(e.target.tagName==='BUTTON')return;
      var sx=e.clientX-w.offsetLeft,sy=e.clientY-w.offsetTop;
      function mv(ev){w.style.left=(ev.clientX-sx)+'px';w.style.top=Math.max(0,ev.clientY-sy)+'px';}
      function up(){document.removeEventListener('mousemove',mv);document.removeEventListener('mouseup',up);}
      document.addEventListener('mousemove',mv);document.addEventListener('mouseup',up);});
    w.addEventListener('mousedown',function(){w.style.zIndex=++zTop;});
    if(appId==='monitor'){var iv=setInterval(function(){if(!w.isConnected){clearInterval(iv);return;}
      try{pre.textContent=app.run('',{fs:fs,api:api});}catch(e){}},4000);}
  }
  api.apps().forEach(function(a){
    var ic=el('div','qsim-icon','<span class="g">'+a.icon+'</span>'+a.name);
    ic.addEventListener('click',function(){openWin(a.id);});
    icons.appendChild(ic);});
  var clock=el('span','dim','QuantaOS '+"signature");
  taskbar.appendChild(clock);
  var time=el('span','dim','');taskbar.appendChild(time);
  setInterval(function(){var d=new Date();time.textContent=d.toLocaleTimeString();},1000);
  return {openWin:openWin};
}
return {api:api,mount:mount,APPS:APPS};
})();

var gen={version:'jahdb-quanta-os-models-database-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,selfReg:SELF_REG};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('quanta-os-models-database-signature',gen);
if(typeof window!=='undefined'&&typeof QuantaSim!=='undefined'){window.QuantaSim=QuantaSim;}
if(typeof module!=='undefined'&&module.exports){module.exports=gen;if(typeof QuantaSim!=='undefined'){module.exports.QuantaSim=QuantaSim;}}
})();
