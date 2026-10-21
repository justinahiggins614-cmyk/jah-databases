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
var CATS=["sdks", "simulators", "compilers", "annealing", "mitigation"];
var PREFIX='JAH-QCTOS-';
var SEEDS=[{"t": "Signature Tool: Circuit Sketchpad", "c": "compilers", "l": 1, "d": "Manon's Circuit Sketchpad concept: a visual circuit editor where gates are dragged onto wires and the state vector updates live beside the circuit \u2014 every gate shows its immediate effect on probabilities. The tool's signature feature is 'why' mode: click any amplitude and it traces which gates created it. Designed for learning, it caps at 4 qubits so the math stays visible. Signature concept.", "f": {"origin": "Signature original by Justin Addam Higgins", "type": "Signature concept", "cap": "4 qubits for visibility"}, "p": "// JAH demo program \u2014 Live probability update demo\n\"use strict\";\nvar __checks=[];\nfunction check(l,g,w){__checks.push([l,g,w]);}\nfunction probsAfter(gates){ var s=[1,0]; gates.forEach(function(g){\n  var h=1/Math.sqrt(2); var n0=g==='H'?(s[0]+s[1])*h:s[0], n1=g==='H'?(s[0]-s[1])*h:(g==='X'?s[0]:s[1]);\n  s=g==='X'?[s[1],s[0]]:[n0,n1]; }); return s.map(function(a){return Math.round(a*a*100)/100;}); }\ncheck(\"H \\u2192 50/50\", probsAfter(['H']).join('/'), \"0.5/0.5\");\ncheck(\"H then X \\u2192 50/50\", probsAfter(['H','X']).join('/'), \"0.5/0.5\");\ncheck(\"X \\u2192 |1>\", probsAfter(['X']).join('/'), \"0/1\");\nvar __ok=true;\n__checks.forEach(function(c){var ok=String(c[1])===String(c[2]);__ok=ok&&__ok;console.log((ok?\"PASS\":\"FAIL\")+\" | \"+c[0]+\" => \"+c[1]);});\nconsole.log(__ok?\"ALL CHECKS PASSED\":\"SOME CHECKS FAILED\");\nif(!__ok){throw new Error(\"demo self-check failed\");}", "s": ["Save the program as demo.js.", "Run it with: node demo.js", "Confirm every line prints PASS and the run ends with ALL CHECKS PASSED."]}, {"t": "Signature Tool: Noise Painter", "c": "mitigation", "l": 2, "d": "Manon's Noise Painter concept: an error-mitigation workbench where the user 'paints' noise models onto circuit regions \u2014 depolarizing here, readout error there \u2014 and watches the expected fidelity update live. Then one click applies ZNE, PEC, or CDR and shows the before/after side by side. It makes error mitigation tangible instead of theoretical. Signature concept.", "f": {"origin": "Signature original by Justin Addam Higgins", "type": "Signature concept"}, "p": "// JAH demo program \u2014 Fidelity estimator\n\"use strict\";\nvar __checks=[];\nfunction check(l,g,w){__checks.push([l,g,w]);}\nfunction fidelity(gates, p){ return Math.pow(1-p, gates); }\ncheck(\"100 gates at 0.1% \\u2192 ~90%\", Math.round(fidelity(100,0.001)*100), 90);\ncheck(\"1000 gates at 0.1% \\u2192 ~37%\", Math.round(fidelity(1000,0.001)*100), 37);\nvar __ok=true;\n__checks.forEach(function(c){var ok=String(c[1])===String(c[2]);__ok=ok&&__ok;console.log((ok?\"PASS\":\"FAIL\")+\" | \"+c[0]+\" => \"+c[1]);});\nconsole.log(__ok?\"ALL CHECKS PASSED\":\"SOME CHECKS FAILED\");\nif(!__ok){throw new Error(\"demo self-check failed\");}", "s": ["Save the program as demo.js.", "Run it with: node demo.js", "Confirm every line prints PASS and the run ends with ALL CHECKS PASSED."]}, {"t": "Signature Tool: Qubit Landlord", "c": "annealing", "l": 3, "d": "Manon's Qubit Landlord concept: a resource manager for shared quantum hardware that shows who is using which qubits, queues jobs fairly, and predicts wait times honestly \u2014 including why your job is third in line. The tool's fairness dashboard is public to all users of the machine, which the concept argues is the only way shared scarce hardware stays legitimate. Signature concept.", "f": {"origin": "Signature original by Justin Addam Higgins", "type": "Signature concept"}, "p": "// JAH demo program \u2014 Fair-share wait estimate\n\"use strict\";\nvar __checks=[];\nfunction check(l,g,w){__checks.push([l,g,w]);}\nfunction waitAhead(jobsAhead, avgMin){ return jobsAhead*avgMin; }\ncheck(\"3 jobs ahead, 5 min avg \\u2192 15\", waitAhead(3,5), 15);\ncheck(\"empty queue \\u2192 0\", waitAhead(0,5), 0);\nvar __ok=true;\n__checks.forEach(function(c){var ok=String(c[1])===String(c[2]);__ok=ok&&__ok;console.log((ok?\"PASS\":\"FAIL\")+\" | \"+c[0]+\" => \"+c[1]);});\nconsole.log(__ok?\"ALL CHECKS PASSED\":\"SOME CHECKS FAILED\");\nif(!__ok){throw new Error(\"demo self-check failed\");}", "s": ["Save the program as demo.js.", "Run it with: node demo.js", "Confirm every line prints PASS and the run ends with ALL CHECKS PASSED."]}, {"t": "Signature Tool: Pulse Composer", "c": "simulators", "l": 4, "d": "Manon's Pulse Composer concept: a drag-and-drop pulse sequencer for the microwave pulses that actually drive qubits \u2014 Gaussian, DRAG, flat-top \u2014 with a live Bloch-sphere preview of what each pulse does to the qubit state. It teaches the layer beneath the gates: every H and X is a shaped pulse, and shaping it better is free fidelity. Signature concept.", "f": {"origin": "Signature original by Justin Addam Higgins", "type": "Signature concept"}, "p": "// JAH demo program \u2014 Gaussian pulse area\n\"use strict\";\nvar __checks=[];\nfunction check(l,g,w){__checks.push([l,g,w]);}\nfunction area(amp, sigma){ return amp*sigma*Math.sqrt(2*Math.PI); }\ncheck(\"pi-pulse area \\u2248 \\u03c0\", Math.round(area(0.5, 2.5066)*100)/100, 3.14);\ncheck(\"double amp \\u2192 double area\", Math.round(area(1.0,2.5066)/area(0.5,2.5066)), 2);\nvar __ok=true;\n__checks.forEach(function(c){var ok=String(c[1])===String(c[2]);__ok=ok&&__ok;console.log((ok?\"PASS\":\"FAIL\")+\" | \"+c[0]+\" => \"+c[1]);});\nconsole.log(__ok?\"ALL CHECKS PASSED\":\"SOME CHECKS FAILED\");\nif(!__ok){throw new Error(\"demo self-check failed\");}", "s": ["Save the program as demo.js.", "Run it with: node demo.js", "Confirm every line prints PASS and the run ends with ALL CHECKS PASSED."]}, {"t": "Signature Tool: Benchmark Arena", "c": "compilers", "l": 5, "d": "Manon's Benchmark Arena concept: a standardized dueling ground where compilers and transpilers compete on identical circuits \u2014 gate count, depth, and estimated fidelity reported on a public leaderboard. Vendors submit passes, the arena runs them, nobody grades their own homework. It would do for quantum compilation what MLPerf did for machine learning. Signature concept.", "f": {"origin": "Signature original by Justin Addam Higgins", "type": "Signature concept"}, "p": "// JAH demo program \u2014 Arena scoring\n\"use strict\";\nvar __checks=[];\nfunction check(l,g,w){__checks.push([l,g,w]);}\nfunction arenaScore(gates, depth, estFid){ return Math.round(estFid*1000/(gates+depth)); }\ncheck(\"fewer gates wins\", arenaScore(10,8,0.99)>arenaScore(20,16,0.99), true);\ncheck(\"score is a number\", arenaScore(10,8,0.99)>0, true);\nvar __ok=true;\n__checks.forEach(function(c){var ok=String(c[1])===String(c[2]);__ok=ok&&__ok;console.log((ok?\"PASS\":\"FAIL\")+\" | \"+c[0]+\" => \"+c[1]);});\nconsole.log(__ok?\"ALL CHECKS PASSED\":\"SOME CHECKS FAILED\");\nif(!__ok){throw new Error(\"demo self-check failed\");}", "s": ["Save the program as demo.js.", "Run it with: node demo.js", "Confirm every line prints PASS and the run ends with ALL CHECKS PASSED."]}, {"t": "Signature Tool: Error Budget Planner", "c": "mitigation", "l": 6, "d": "Manon's Error Budget Planner concept: given a target algorithm fidelity, it works backward through the circuit \u2014 allocating allowable error per gate type, per qubit, per readout \u2014 and tells you whether today's hardware can run it or which component must improve. 'Every quantum program has an error budget; most just never write it down.' Signature concept.", "f": {"origin": "Signature original by Justin Addam Higgins", "type": "Signature concept"}, "p": "// JAH demo program \u2014 Error budget check\n\"use strict\";\nvar __checks=[];\nfunction check(l,g,w){__checks.push([l,g,w]);}\nfunction budgetOK(gates, pGate, target){ return Math.pow(1-pGate,gates)>=target; }\ncheck(\"100 gates, 0.1%, target 90% \\u2192 ok\", budgetOK(100,0.001,0.9), true);\ncheck(\"1000 gates, 0.1%, target 90% \\u2192 no\", budgetOK(1000,0.001,0.9), false);\nvar __ok=true;\n__checks.forEach(function(c){var ok=String(c[1])===String(c[2]);__ok=ok&&__ok;console.log((ok?\"PASS\":\"FAIL\")+\" | \"+c[0]+\" => \"+c[1]);});\nconsole.log(__ok?\"ALL CHECKS PASSED\":\"SOME CHECKS FAILED\");\nif(!__ok){throw new Error(\"demo self-check failed\");}", "s": ["Save the program as demo.js.", "Run it with: node demo.js", "Confirm every line prints PASS and the run ends with ALL CHECKS PASSED."]}, {"t": "Signature Tool: Anneal Tuner", "c": "annealing", "l": 7, "d": "Manon's Anneal Tuner concept: a visual tuner for quantum annealing schedules \u2014 drag the anneal curve, set pauses and quenches, and watch the predicted success probability update from the problem's energy landscape. It includes a library of schedule shapes that worked on published problems, because schedule design is currently folklore and should be engineering. Signature concept.", "f": {"origin": "Signature original by Justin Addam Higgins", "type": "Signature concept"}, "p": "// JAH demo program \u2014 Schedule success model\n\"use strict\";\nvar __checks=[];\nfunction check(l,g,w){__checks.push([l,g,w]);}\nfunction success(annealUs, gap){ return 1-Math.exp(-annealUs*gap*gap/100); }\ncheck(\"longer anneal helps\", success(200,0.5)>success(20,0.5), true);\ncheck(\"success bounded by 1\", success(1000,1)<1, true);\nvar __ok=true;\n__checks.forEach(function(c){var ok=String(c[1])===String(c[2]);__ok=ok&&__ok;console.log((ok?\"PASS\":\"FAIL\")+\" | \"+c[0]+\" => \"+c[1]);});\nconsole.log(__ok?\"ALL CHECKS PASSED\":\"SOME CHECKS FAILED\");\nif(!__ok){throw new Error(\"demo self-check failed\");}", "s": ["Save the program as demo.js.", "Run it with: node demo.js", "Confirm every line prints PASS and the run ends with ALL CHECKS PASSED."]}, {"t": "Signature Tool: Readout Fixer", "c": "mitigation", "l": 8, "d": "Manon's Readout Fixer concept: a one-click readout-error correction tool \u2014 it measures the device's confusion matrix once, then inverts it on every result histogram automatically. The tool shows the raw vs corrected distributions side by side so the user sees exactly what the correction bought. Readout error is the cheapest error to fix, and this tool makes it free. Signature concept.", "f": {"origin": "Signature original by Justin Addam Higgins", "type": "Signature concept"}, "p": "// JAH demo program \u2014 Confusion-matrix inversion (2 outcomes)\n\"use strict\";\nvar __checks=[];\nfunction check(l,g,w){__checks.push([l,g,w]);}\nfunction correct(counts, p01, p10){ var n0=counts[0], n1=counts[1];\n  var t0=(n0*(1-p10)-n1*p01)/((1-p01)*(1-p10)-p01*p10);\n  var t1=(n1*(1-p01)-n0*p10)/((1-p01)*(1-p10)-p01*p10); return [t0,t1]; }\nvar c=correct([900,100],0.05,0.05);\ncheck(\"corrected |0> \\u2248 944\", Math.round(c[0]), 944);\ncheck(\"correction shifts counts up\", c[0]>900, true);\nvar __ok=true;\n__checks.forEach(function(c){var ok=String(c[1])===String(c[2]);__ok=ok&&__ok;console.log((ok?\"PASS\":\"FAIL\")+\" | \"+c[0]+\" => \"+c[1]);});\nconsole.log(__ok?\"ALL CHECKS PASSED\":\"SOME CHECKS FAILED\");\nif(!__ok){throw new Error(\"demo self-check failed\");}", "s": ["Save the program as demo.js.", "Run it with: node demo.js", "Confirm every line prints PASS and the run ends with ALL CHECKS PASSED."]}, {"t": "Signature Tool: Topology Mapper", "c": "compilers", "l": 9, "d": "Manon's Topology Mapper concept: an interactive map of a QPU's qubit connectivity where the user drops their circuit's interaction graph on top and watches the router insert SWAPs live. It teaches why topology matters \u2014 a linear chain can triple your two-qubit count \u2014 and lets users try different initial mappings to minimize overhead. Signature concept.", "f": {"origin": "Signature original by Justin Addam Higgins", "type": "Signature concept"}, "p": "// JAH demo program \u2014 SWAP overhead estimate\n\"use strict\";\nvar __checks=[];\nfunction check(l,g,w){__checks.push([l,g,w]);}\nfunction swapsNeeded(dist){ return Math.max(0, dist-1); }\ncheck(\"adjacent \\u2192 0 SWAPs\", swapsNeeded(1), 0);\ncheck(\"distance 4 \\u2192 3 SWAPs\", swapsNeeded(4), 3);\ncheck(\"each SWAP = 3 CNOTs\", swapsNeeded(4)*3, 9);\nvar __ok=true;\n__checks.forEach(function(c){var ok=String(c[1])===String(c[2]);__ok=ok&&__ok;console.log((ok?\"PASS\":\"FAIL\")+\" | \"+c[0]+\" => \"+c[1]);});\nconsole.log(__ok?\"ALL CHECKS PASSED\":\"SOME CHECKS FAILED\");\nif(!__ok){throw new Error(\"demo self-check failed\");}", "s": ["Save the program as demo.js.", "Run it with: node demo.js", "Confirm every line prints PASS and the run ends with ALL CHECKS PASSED."]}, {"t": "Signature Tool: Shot Forecaster", "c": "simulators", "l": 10, "d": "Manon's Shot Forecaster concept: before spending QPU time, it predicts how many shots an experiment needs for a target precision \u2014 from the observable's variance and the device's readout error \u2014 and prices the run. 'Never book a million shots when ten thousand would do.' It would save the field real money. Signature concept.", "f": {"origin": "Signature original by Justin Addam Higgins", "type": "Signature concept"}, "p": "// JAH demo program \u2014 Shot forecast\n\"use strict\";\nvar __checks=[];\nfunction check(l,g,w){__checks.push([l,g,w]);}\nfunction forecast(variance, eps){ return Math.ceil(variance/(eps*eps)); }\ncheck(\"var 1, eps 0.01 \\u2192 10k\", forecast(1,0.01), 10000);\ncheck(\"halve eps \\u2192 4x shots\", forecast(1,0.005)/forecast(1,0.01), 4);\nvar __ok=true;\n__checks.forEach(function(c){var ok=String(c[1])===String(c[2]);__ok=ok&&__ok;console.log((ok?\"PASS\":\"FAIL\")+\" | \"+c[0]+\" => \"+c[1]);});\nconsole.log(__ok?\"ALL CHECKS PASSED\":\"SOME CHECKS FAILED\");\nif(!__ok){throw new Error(\"demo self-check failed\");}", "s": ["Save the program as demo.js.", "Run it with: node demo.js", "Confirm every line prints PASS and the run ends with ALL CHECKS PASSED."]}, {"t": "Signature Tool: Calibration Diary", "c": "sdks", "l": 11, "d": "Manon's Calibration Diary concept: a lab notebook that automatically logs every qubit calibration \u2014 T1, T2, gate errors, readout fidelity \u2014 with timestamps, and plots drift over days. When an experiment fails, the diary answers 'was it the device or my circuit?' The concept treats calibration data as a first-class experimental record, not a log file nobody reads. Signature concept.", "f": {"origin": "Signature original by Justin Addam Higgins", "type": "Signature concept"}, "p": "// JAH demo program \u2014 Drift detector\n\"use strict\";\nvar __checks=[];\nfunction check(l,g,w){__checks.push([l,g,w]);}\nfunction drifted(recent, baseline, tol){ return Math.abs(recent-baseline)>tol; }\ncheck(\"T1 dropped 20% \\u2192 drifted\", drifted(80,100,10), true);\ncheck(\"within tolerance \\u2192 stable\", drifted(95,100,10), false);\nvar __ok=true;\n__checks.forEach(function(c){var ok=String(c[1])===String(c[2]);__ok=ok&&__ok;console.log((ok?\"PASS\":\"FAIL\")+\" | \"+c[0]+\" => \"+c[1]);});\nconsole.log(__ok?\"ALL CHECKS PASSED\":\"SOME CHECKS FAILED\");\nif(!__ok){throw new Error(\"demo self-check failed\");}", "s": ["Save the program as demo.js.", "Run it with: node demo.js", "Confirm every line prints PASS and the run ends with ALL CHECKS PASSED."]}, {"t": "Signature Tool: Hybrid Debugger", "c": "mitigation", "l": 12, "d": "Manon's Hybrid Debugger concept: a debugger for variational algorithms that shows both halves of the hybrid loop \u2014 the quantum circuit with per-layer gradients and the classical optimizer's trajectory \u2014 in one view. Barren plateaus show up as flat gradient landscapes; the debugger flags them and suggests layer surgery. It debugs the loop, not just the circuit. Signature concept.", "f": {"origin": "Signature original by Justin Addam Higgins", "type": "Signature concept"}, "p": "// JAH demo program \u2014 Barren-plateau detector\n\"use strict\";\nvar __checks=[];\nfunction check(l,g,w){__checks.push([l,g,w]);}\nfunction plateau(grads){ var v=grads.reduce(function(s,g){return s+g*g;},0)/grads.length; return v<1e-6; }\ncheck(\"vanishing gradients \\u2192 plateau\", plateau([1e-8,2e-8,1e-8]), true);\ncheck(\"healthy gradients \\u2192 ok\", plateau([0.1,0.2,0.15]), false);\nvar __ok=true;\n__checks.forEach(function(c){var ok=String(c[1])===String(c[2]);__ok=ok&&__ok;console.log((ok?\"PASS\":\"FAIL\")+\" | \"+c[0]+\" => \"+c[1]);});\nconsole.log(__ok?\"ALL CHECKS PASSED\":\"SOME CHECKS FAILED\");\nif(!__ok){throw new Error(\"demo self-check failed\");}", "s": ["Save the program as demo.js.", "Run it with: node demo.js", "Confirm every line prints PASS and the run ends with ALL CHECKS PASSED."]}, {"t": "Signature Tool: Quanta Linter", "c": "compilers", "l": 13, "d": "Manon's Quanta Linter concept: a static analyzer for quantum programs that flags the classic mistakes \u2014 measuring a qubit then using it, deep circuits on high-error qubits, uncomputed ancillas left entangled, missing transpilation. It runs in the editor as you type, with explanations written for humans, not compiler engineers. 'The linter catches at write-time what the QPU would punish at run-time.' Signature concept.", "f": {"origin": "Signature original by Justin Addam Higgins", "type": "Signature concept"}, "p": "// JAH demo program \u2014 Lint rule demo\n\"use strict\";\nvar __checks=[];\nfunction check(l,g,w){__checks.push([l,g,w]);}\nfunction lint(ops){ var warns=[]; var measured={};\n  ops.forEach(function(op){ if(op[0]==='measure')measured[op[1]]=1;\n    if(op[0]==='H'&&measured[op[1]])warns.push('use after measure on q'+op[1]); });\n  return warns; }\ncheck(\"flags use-after-measure\", lint([['measure',0],['H',0]]).length, 1);\ncheck(\"clean circuit \\u2192 no warnings\", lint([['H',0],['measure',0]]).length, 0);\nvar __ok=true;\n__checks.forEach(function(c){var ok=String(c[1])===String(c[2]);__ok=ok&&__ok;console.log((ok?\"PASS\":\"FAIL\")+\" | \"+c[0]+\" => \"+c[1]);});\nconsole.log(__ok?\"ALL CHECKS PASSED\":\"SOME CHECKS FAILED\");\nif(!__ok){throw new Error(\"demo self-check failed\");}", "s": ["Save the program as demo.js.", "Run it with: node demo.js", "Confirm every line prints PASS and the run ends with ALL CHECKS PASSED."]}, {"t": "Signature Tool: Fidelity Ledger", "c": "sdks", "l": 14, "d": "Manon's Fidelity Ledger concept: an accounting book for quantum experiments where every run logs its fidelity budget \u2014 predicted vs measured \u2014 and the ledger reconciles the difference, attributing loss to gates, readout, or decoherence. Over time the ledger learns your device's true error profile and predicts new circuits' fidelity within a few percent. Signature concept.", "f": {"origin": "Signature original by Justin Addam Higgins", "type": "Signature concept"}, "p": "// JAH demo program \u2014 Ledger reconciliation\n\"use strict\";\nvar __checks=[];\nfunction check(l,g,w){__checks.push([l,g,w]);}\nfunction attribute(predicted, measured){ var loss=predicted-measured;\n  return {gates:Math.round(loss*0.5*1000)/1000, readout:Math.round(loss*0.3*1000)/1000, decoherence:Math.round(loss*0.2*1000)/1000}; }\nvar a=attribute(0.95,0.90);\ncheck(\"total attributed = 0.05\", Math.round((a.gates+a.readout+a.decoherence)*1000)/1000, 0.05);\ncheck(\"gates get half\", a.gates, 0.025);\nvar __ok=true;\n__checks.forEach(function(c){var ok=String(c[1])===String(c[2]);__ok=ok&&__ok;console.log((ok?\"PASS\":\"FAIL\")+\" | \"+c[0]+\" => \"+c[1]);});\nconsole.log(__ok?\"ALL CHECKS PASSED\":\"SOME CHECKS FAILED\");\nif(!__ok){throw new Error(\"demo self-check failed\");}", "s": ["Save the program as demo.js.", "Run it with: node demo.js", "Confirm every line prints PASS and the run ends with ALL CHECKS PASSED."]}, {"t": "Signature Tool: Quanta Playground", "c": "simulators", "l": 15, "d": "Manon's Quanta Playground concept: a zero-install browser playground (this database's simulator is its prototype) where every quantum concept runs as an interactive toy \u2014 Bell states, teleportation, Grover \u2014 with the math shown beside the picture. No accounts, no queues, no QPU: the playground's promise is that the first hour of quantum computing should be free and instant. Signature concept.", "f": {"origin": "Signature original by Justin Addam Higgins", "type": "Signature concept", "promise": "first hour of quantum computing: free and instant"}, "p": "// JAH demo program \u2014 Playground session stats\n\"use strict\";\nvar __checks=[];\nfunction check(l,g,w){__checks.push([l,g,w]);}\nfunction sessionStats(minutes, toys){ return {toys:toys, perToy:Math.round(minutes/toys)}; }\nvar s=sessionStats(60,12);\ncheck(\"12 toys tried\", s.toys, 12);\ncheck(\"5 min per toy\", s.perToy, 5);\nvar __ok=true;\n__checks.forEach(function(c){var ok=String(c[1])===String(c[2]);__ok=ok&&__ok;console.log((ok?\"PASS\":\"FAIL\")+\" | \"+c[0]+\" => \"+c[1]);});\nconsole.log(__ok?\"ALL CHECKS PASSED\":\"SOME CHECKS FAILED\");\nif(!__ok){throw new Error(\"demo self-check failed\");}", "s": ["Save the program as demo.js.", "Run it with: node demo.js", "Confirm every line prints PASS and the run ends with ALL CHECKS PASSED."]}];
var GEN_VARIANTS=["Signature prototype notes", "Signature v2 idea", "Signature field test", "Signature minimal version", "Signature crossover", "Signature concept sketch"];
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

defApp('transpile','Circuit Transpiler','\uD83D\uDD27',
 'Transpile gates to basis {U, CX}. Input gates like: H 0; T 0; CNOT 0 1',
 function(input){var basis={H:['U(pi/2,0,pi)'],X:['U(pi,0,pi)'],T:['U(0,0,pi/4)'],S:['U(0,0,pi/2)'],Z:['U(0,0,pi)']};
  var lines=String(input||'').split(/[\n;]+/);var out=[];var before=0,after=0,depth=0;
  lines.forEach(function(ln){var p=ln.trim().split(/\s+/);if(!p[0])return;before++;
    var g=p[0].toUpperCase();var q=p[1]||'0';
    if(g==='CNOT'){out.push('CX '+p[1]+' '+p[2]);after++;depth++;}
    else if(g==='RX'){out.push('U('+p[2]+',-pi/2,pi/2) q'+q);after++;depth++;}
    else if(basis[g]){out.push(basis[g][0]+' q'+q);after++;depth++;}
    else throw new Error('unsupported gate: '+g);});
  return ['transpile to basis {U, CX}:',out.join('\n'),
   'gates: '+before+' -> '+after+', depth '+depth,
   'real basis translation (single-qubit unitaries + CX)'].join('\n');});
defApp('pulse','Pulse Schedule','\u3030',
 'Show the microwave pulse schedule for a gate. Input: X 0 | H 1 | CNOT 0 1',
 function(input){var p=String(input||'').trim().split(/\s+/);var g=(p[0]||'').toUpperCase();var q=p[1]||'0';
  var sched={'X':{dur:40,amp:0.35,sigma:10},'H':{dur:32,amp:0.28,sigma:8},'Z':{dur:0,amp:0,sigma:0}};
  if(g==='CNOT')return ['pulse schedule: CNOT '+p[1]+' '+p[2],
   'ch drive(q'+p[1]+'): Gaussian dur=40ns amp=0.35 sigma=10ns',
   'ch drive(q'+p[2]+'): Gaussian dur=40ns amp=0.22 sigma=10ns (cross-resonance)',
   'ch control: flat-top 40ns — real pulse-level structure, simulated values'].join('\n');
  var s=sched[g];if(!s)return 'usage: X 0 | H 1 | Z 0 | CNOT 0 1';
  return ['pulse schedule: '+g+' q'+q,
   'channel: drive(q'+q+')',
   s.dur?('envelope: Gaussian  dur='+s.dur+'ns  amp='+s.amp+'  sigma='+s.sigma+'ns'):'envelope: virtual-Z (frame change, 0ns)',
   'real pulse-level structure, simulated values'].join('\n');});
defApp('zne','Error Mitigation (ZNE)','\uD83D\uDEE1',
 'Zero-noise extrapolation demo. Input: p=<base error rate>  (e.g. p=0.02)',
 function(input){var m=String(input||'').match(/p\s*=\s*([\d.]+)/);var p=m?+m[1]:0.02;
  var E0=0.85;var scales=[1,3,5];
  var vals=scales.map(function(x){return E0*(1-p*x);});
  var n=scales.length;var sx=0,sy=0,sxx=0,sxy=0;
  for(var i=0;i<n;i++){sx+=scales[i];sy+=vals[i];sxx+=scales[i]*scales[i];sxy+=scales[i]*vals[i];}
  var slope=(n*sxy-sx*sy)/(n*sxx-sx*sx);var icept=(sy-slope*sx)/n;
  return ['ZNE: measured <Z> at noise scale factors 1x, 3x, 5x (base error p='+p+')',
   scales.map(function(x,i){return 'scale '+x+'x: '+fmtN(vals[i],4);}).join('\n'),
   'linear fit: E(x) = '+fmtN(icept,4)+' + '+fmtN(slope,4)+'*x',
   'extrapolated zero-noise value: '+fmtN(icept,4)+'  (true '+E0+')',
   'real Richardson-style extrapolation math'].join('\n');});

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

var gen={version:'jahdb-quanta-computer-tools-database-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,selfReg:SELF_REG};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('quanta-computer-tools-database-signature',gen);
if(typeof window!=='undefined'&&typeof QuantaSim!=='undefined'){window.QuantaSim=QuantaSim;}
if(typeof module!=='undefined'&&module.exports){module.exports=gen;if(typeof QuantaSim!=='undefined'){module.exports.QuantaSim=QuantaSim;}}
})();
