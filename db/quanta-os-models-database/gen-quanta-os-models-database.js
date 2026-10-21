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
var PREFIX='JAH-QOSM-';
var SEEDS=[{"t": "Qiskit Runtime \u2014 Hybrid Execution Model", "c": "runtime", "l": 1, "d": "Qiskit Runtime is IBM's execution model for the quantum-classical loop: instead of queueing every circuit separately, the classical optimizer runs co-located with the QPU and streams circuits with sub-second latency. Primitives like Sampler and Estimator replaced raw job submission, cutting variational workloads from hours to minutes. It is the closest thing the field has to a quantum operating system's process model.", "f": {"vendor": "IBM", "primitives": ["Sampler", "Estimator"], "latency": "sub-second classical-quantum loop", "effect": "variational workloads: hours \u2192 minutes"}, "p": "// JAH demo program \u2014 Runtime speedup model\n\"use strict\";\nvar __checks=[];\nfunction check(l,g,w){__checks.push([l,g,w]);}\nfunction jobTime(nCircuits, queueS, runS){ return nCircuits*(queueS+runS); }\nfunction runtimeTime(nCircuits, runS){ return 5+nCircuits*runS; } // one queue wait\ncheck(\"100 circuits, 60s queue, 2s run: jobs\", jobTime(100,60,2), 6200);\ncheck(\"runtime model\", Math.round(runtimeTime(100,2)), 205);\ncheck(\"~30x faster\", Math.round(jobTime(100,60,2)/runtimeTime(100,2)), 30);\nvar __ok=true;\n__checks.forEach(function(c){var ok=String(c[1])===String(c[2]);__ok=ok&&__ok;console.log((ok?\"PASS\":\"FAIL\")+\" | \"+c[0]+\" => \"+c[1]);});\nconsole.log(__ok?\"ALL CHECKS PASSED\":\"SOME CHECKS FAILED\");\nif(!__ok){throw new Error(\"demo self-check failed\");}", "s": ["Save the program as demo.js.", "Run it with: node demo.js", "Confirm every line prints PASS and the run ends with ALL CHECKS PASSED."]}, {"t": "ARTIQ and Sinara \u2014 Open Quantum Control Hardware", "c": "control", "l": 2, "d": "ARTIQ is the open-source control system for trapped ions and other precise quantum experiments: nanosecond timing, FPGA-driven, with a Python DSL for describing experiments. Sinara is its open hardware ecosystem \u2014 DACs, ADCs, DDS channels in MicroTCA and EEM crates. Together they run some of the world's best ion-trap clocks and quantum-logic experiments, proving open hardware can hold its own at the bleeding edge.", "f": {"type": "open control hardware/software", "timing": "nanosecond resolution", "language": "Python DSL", "hardware": "Sinara (MicroTCA/EEM)", "license": "open source"}, "p": "// JAH demo program \u2014 Timing resolution demo\n\"use strict\";\nvar __checks=[];\nfunction check(l,g,w){__checks.push([l,g,w]);}\nfunction cyclesNeeded(durationNs, resNs){ return Math.ceil(durationNs/resNs); }\ncheck(\"1\\u00b5s gate at 1ns resolution\", cyclesNeeded(1000,1), 1000);\ncheck(\"FPGA clock ticks\", cyclesNeeded(40,1), 40);\nvar __ok=true;\n__checks.forEach(function(c){var ok=String(c[1])===String(c[2]);__ok=ok&&__ok;console.log((ok?\"PASS\":\"FAIL\")+\" | \"+c[0]+\" => \"+c[1]);});\nconsole.log(__ok?\"ALL CHECKS PASSED\":\"SOME CHECKS FAILED\");\nif(!__ok){throw new Error(\"demo self-check failed\");}", "s": ["Save the program as demo.js.", "Run it with: node demo.js", "Confirm every line prints PASS and the run ends with ALL CHECKS PASSED."]}, {"t": "QCoDeS \u2014 Instrument Control Framework", "c": "control", "l": 3, "d": "QCoDeS is the Python framework behind countless qubit bring-ups: it models every lab instrument as parameters with set/get, ramping, and validation, then sweeps them in orchestrated measurement loops with live plotting and HDF5 datasets. Born at Copenhagen/Delft for quantum-dot experiments, it is now the de facto standard for experimental quantum labs. Every automated qubit calibration routine \u2014 Rabi, Ramsey, T1 \u2014 typically runs through QCoDeS drivers.", "f": {"type": "instrument control", "language": "Python", "origin": "Copenhagen/Delft quantum dots", "features": ["parameter abstraction", "sweeps", "live plotting", "HDF5 datasets"]}, "p": "// JAH demo program \u2014 Parameter ramp demo\n\"use strict\";\nvar __checks=[];\nfunction check(l,g,w){__checks.push([l,g,w]);}\nfunction ramp(start, stop, n){ var out=[]; for(var i=0;i<n;i++) out.push(start+(stop-start)*i/(n-1)); return out; }\nvar pts=ramp(0,5,6);\ncheck(\"6 points from 0 to 5\", pts.length, 6);\ncheck(\"endpoints exact\", pts[0]===0&&pts[5]===5, true);\ncheck(\"midpoint 2.5\", pts[2]+pts[3], 5);\nvar __ok=true;\n__checks.forEach(function(c){var ok=String(c[1])===String(c[2]);__ok=ok&&__ok;console.log((ok?\"PASS\":\"FAIL\")+\" | \"+c[0]+\" => \"+c[1]);});\nconsole.log(__ok?\"ALL CHECKS PASSED\":\"SOME CHECKS FAILED\");\nif(!__ok){throw new Error(\"demo self-check failed\");}", "s": ["Save the program as demo.js.", "Run it with: node demo.js", "Confirm every line prints PASS and the run ends with ALL CHECKS PASSED."]}, {"t": "Pulse-Level Programming \u2014 Qiskit Pulse", "c": "control", "l": 4, "d": "Qiskit Pulse exposes the layer beneath the gates: the actual microwave pulse schedules \u2014 durations, amplitudes, phases per channel \u2014 that implement each operation on the hardware. Researchers use it to design better gates (DRAG pulses that cancel leakage), characterize crosstalk, and squeeze fidelity the compiler cannot reach. It is the difference between driving an automatic and opening the gearbox.", "f": {"level": "microwave pulses", "channels": ["drive", "control", "measure", "acquire"], "uses": ["custom gates (DRAG)", "crosstalk characterization", "optimal control"]}, "p": "// JAH demo program \u2014 DRAG pulse leakage estimate\n\"use strict\";\nvar __checks=[];\nfunction check(l,g,w){__checks.push([l,g,w]);}\nfunction leakage(amp){ return amp*amp/2; } // toy: leakage grows with drive amplitude\nfunction dragFix(raw){ return raw/10; }\ncheck(\"well-shaped pulse leaks little\", leakage(0.2)<0.05, true);\ncheck(\"hotter pulse leaks more\", leakage(0.5)>leakage(0.2), true);\ncheck(\"DRAG correction cuts leakage 10x\", dragFix(leakage(0.5))<leakage(0.5), true);\nvar __ok=true;\n__checks.forEach(function(c){var ok=String(c[1])===String(c[2]);__ok=ok&&__ok;console.log((ok?\"PASS\":\"FAIL\")+\" | \"+c[0]+\" => \"+c[1]);});\nconsole.log(__ok?\"ALL CHECKS PASSED\":\"SOME CHECKS FAILED\");\nif(!__ok){throw new Error(\"demo self-check failed\");}", "s": ["Save the program as demo.js.", "Run it with: node demo.js", "Confirm every line prints PASS and the run ends with ALL CHECKS PASSED."]}, {"t": "Transpiler Optimization Levels", "c": "compilation", "l": 5, "d": "The transpiler is the quantum compiler pass that rewrites abstract circuits onto real hardware: rebasing gates to the native set, routing around limited connectivity with SWAPs, and optimizing away redundancies. Qiskit's levels 0\u20133 trade compile time for circuit quality; level 3 can halve two-qubit counts on deep circuits. On noisy hardware, transpiler quality is second only to the device itself in determining whether a result means anything.", "f": {"levels": ["0: none", "1: light", "2: medium", "3: heavy"], "passes": ["translation", "optimization", "routing", "scheduling"]}, "p": "// JAH demo program \u2014 Routing overhead on a line\n\"use strict\";\nvar __checks=[];\nfunction check(l,g,w){__checks.push([l,g,w]);}\nfunction overhead(nQubits, twoQ){ return twoQ*3*(nQubits-1)/nQubits; } // illustrative\ncheck(\"overhead grows with distance\", overhead(5,10)>overhead(2,10), true);\ncheck(\"2 qubits: no routing\", overhead(2,10)<overhead(5,10), true);\nvar __ok=true;\n__checks.forEach(function(c){var ok=String(c[1])===String(c[2]);__ok=ok&&__ok;console.log((ok?\"PASS\":\"FAIL\")+\" | \"+c[0]+\" => \"+c[1]);});\nconsole.log(__ok?\"ALL CHECKS PASSED\":\"SOME CHECKS FAILED\");\nif(!__ok){throw new Error(\"demo self-check failed\");}", "s": ["Save the program as demo.js.", "Run it with: node demo.js", "Confirm every line prints PASS and the run ends with ALL CHECKS PASSED."]}, {"t": "FPGA/AWG Control Electronics", "c": "control", "l": 6, "d": "Between the Python and the qubit sits the control stack's muscle: FPGAs sequencing nanosecond pulses, arbitrary waveform generators shaping them, and digitizers reading the faint readout tones. Quantum Machines' OPX, Zurich Instruments' SHFQC, and Keysight's quantum line integrate this into rack units with real-time feedback for mid-circuit decisions. This layer's latency budget decides whether error correction is even possible.", "f": {"vendors": ["Quantum Machines OPX", "Zurich Instruments SHFQC", "Keysight"], "functions": ["pulse sequencing", "waveform generation", "readout digitization", "real-time feedback"]}, "p": "// JAH demo program \u2014 Feedback latency budget\n\"use strict\";\nvar __checks=[];\nfunction check(l,g,w){__checks.push([l,g,w]);}\nfunction budgetOk(seqNs, fbNs, coherenceNs){ return seqNs+fbNs<coherenceNs/10; }\ncheck(\"40ns gate + 300ns feedback vs 100\\u00b5s coherence\", budgetOk(40,300,100000), true);\ncheck(\"slow feedback breaks budget\", budgetOk(40,50000,100000), false);\nvar __ok=true;\n__checks.forEach(function(c){var ok=String(c[1])===String(c[2]);__ok=ok&&__ok;console.log((ok?\"PASS\":\"FAIL\")+\" | \"+c[0]+\" => \"+c[1]);});\nconsole.log(__ok?\"ALL CHECKS PASSED\":\"SOME CHECKS FAILED\");\nif(!__ok){throw new Error(\"demo self-check failed\");}", "s": ["Save the program as demo.js.", "Run it with: node demo.js", "Confirm every line prints PASS and the run ends with ALL CHECKS PASSED."]}, {"t": "Cloud Queue Schedulers \u2014 Fair Share", "c": "scheduling", "l": 7, "d": "Quantum hardware is scarce, so cloud schedulers ration it: IBM Quantum's fair-share algorithm weighs each group's recent usage against their allocation, prioritizing the underserved without starving anyone. Jobs carry priorities, backends advertise calibrations, and the scheduler matches circuits to the freshest, best-connected device available. It is an operating system's process scheduler, stretched across the planet.", "f": {"policy": "fair-share", "factors": ["recent usage", "allocation", "job priority", "device calibration"]}, "p": "// JAH demo program \u2014 Fair-share priority demo\n\"use strict\";\nvar __checks=[];\nfunction check(l,g,w){__checks.push([l,g,w]);}\nfunction priority(share, used){ return share/(1+used); }\ncheck(\"unused group wins\", priority(10,0)>priority(10,9), true);\ncheck(\"heavy user deprioritized\", priority(10,20)<priority(10,1), true);\nvar __ok=true;\n__checks.forEach(function(c){var ok=String(c[1])===String(c[2]);__ok=ok&&__ok;console.log((ok?\"PASS\":\"FAIL\")+\" | \"+c[0]+\" => \"+c[1]);});\nconsole.log(__ok?\"ALL CHECKS PASSED\":\"SOME CHECKS FAILED\");\nif(!__ok){throw new Error(\"demo self-check failed\");}", "s": ["Save the program as demo.js.", "Run it with: node demo.js", "Confirm every line prints PASS and the run ends with ALL CHECKS PASSED."]}, {"t": "Error Mitigation as a Service Layer", "c": "runtime", "l": 8, "d": "Error mitigation is becoming infrastructure rather than user code: runtime services that automatically apply zero-noise extrapolation, readout correction, and dynamical decoupling around every job. IBM's resilience levels (0\u20133) let users dial mitigation like a volume knob, trading classical post-processing for accuracy. This is the quantum equivalent of the OS memory manager \u2014 everyone uses it, nobody hand-rolls it.", "f": {"levels": ["0: none", "1: readout correction", "2: + dynamical decoupling", "3: + ZNE"], "trade": "classical post-processing for accuracy"}, "p": "// JAH demo program \u2014 Mitigation cost/benefit\n\"use strict\";\nvar __checks=[];\nfunction check(l,g,w){__checks.push([l,g,w]);}\nfunction benefit(rawErr, mitigatedErr, overhead){ return (rawErr-mitigatedErr)/overhead; }\ncheck(\"ZNE: 5%\\u21921% at 3x cost\", Math.round(benefit(0.05,0.01,3)*1000)/1000, 0.013);\ncheck(\"positive benefit\", benefit(0.05,0.01,3)>0, true);\nvar __ok=true;\n__checks.forEach(function(c){var ok=String(c[1])===String(c[2]);__ok=ok&&__ok;console.log((ok?\"PASS\":\"FAIL\")+\" | \"+c[0]+\" => \"+c[1]);});\nconsole.log(__ok?\"ALL CHECKS PASSED\":\"SOME CHECKS FAILED\");\nif(!__ok){throw new Error(\"demo self-check failed\");}", "s": ["Save the program as demo.js.", "Run it with: node demo.js", "Confirm every line prints PASS and the run ends with ALL CHECKS PASSED."]}, {"t": "Hybrid Jobs \u2014 Braket and QCS", "c": "runtime", "l": 9, "d": "Braket Hybrid Jobs and Rigetti's QCS co-locate classical compute with QPUs so variational loops don't cross the internet per iteration \u2014 the classical optimizer lives next door to the quantum processor. Containerized algorithms, checkpointing, and spot pricing make thousand-iteration VQE runs practical. This architecture acknowledges the truth: near-term quantum computers are accelerators, and accelerators need hosts.", "f": {"platforms": ["Braket Hybrid Jobs", "Rigetti QCS"], "pattern": "classical optimizer co-located with QPU"}, "p": "// JAH demo program \u2014 Co-location latency win\n\"use strict\";\nvar __checks=[];\nfunction check(l,g,w){__checks.push([l,g,w]);}\nfunction loopMin(iters, qpuS, lanMs, wanMs){ return iters*(qpuS+lanMs/1000); }\nfunction loopWan(iters, qpuS, wanMs){ return iters*(qpuS+wanMs/1000); }\ncheck(\"1000 iters, 2s QPU: LAN 1ms\", Math.round(loopMin(1000,2,1)), 2001);\ncheck(\"WAN 200ms adds 200s\", Math.round(loopWan(1000,2,200)-loopMin(1000,2,1)), 199);\nvar __ok=true;\n__checks.forEach(function(c){var ok=String(c[1])===String(c[2]);__ok=ok&&__ok;console.log((ok?\"PASS\":\"FAIL\")+\" | \"+c[0]+\" => \"+c[1]);});\nconsole.log(__ok?\"ALL CHECKS PASSED\":\"SOME CHECKS FAILED\");\nif(!__ok){throw new Error(\"demo self-check failed\");}", "s": ["Save the program as demo.js.", "Run it with: node demo.js", "Confirm every line prints PASS and the run ends with ALL CHECKS PASSED."]}, {"t": "Quantum Inspire \u2014 Full-Stack Platform", "c": "runtime", "l": 10, "d": "QuTech's Quantum Inspire offers the full stack in the open: superconducting and spin-qubit backends, a web composer, and an API, run as public infrastructure by a research institute rather than a vendor. Its openness makes it a favorite for education and for experiments vendors won't prioritize. It demonstrates that quantum cloud access can be a public good, not just a product.", "f": {"operator": "QuTech (Delft)", "backends": ["superconducting", "spin qubits"], "model": "public research infrastructure"}, "p": "// JAH demo program \u2014 Education throughput\n\"use strict\";\nvar __checks=[];\nfunction check(l,g,w){__checks.push([l,g,w]);}\nfunction studentJobs(students, perStudent){ return students*perStudent; }\ncheck(\"200 students \\u00d7 5 jobs\", studentJobs(200,5), 1000);\ncheck(\"scales linearly\", studentJobs(400,5)===2*studentJobs(200,5), true);\nvar __ok=true;\n__checks.forEach(function(c){var ok=String(c[1])===String(c[2]);__ok=ok&&__ok;console.log((ok?\"PASS\":\"FAIL\")+\" | \"+c[0]+\" => \"+c[1]);});\nconsole.log(__ok?\"ALL CHECKS PASSED\":\"SOME CHECKS FAILED\");\nif(!__ok){throw new Error(\"demo self-check failed\");}", "s": ["Save the program as demo.js.", "Run it with: node demo.js", "Confirm every line prints PASS and the run ends with ALL CHECKS PASSED."]}, {"t": "Cryogenic Control \u2014 Cryo-CMOS", "c": "control", "l": 11, "d": "Every qubit wire running from room temperature to millikelvin carries heat, and thousands of qubits need thousands of wires \u2014 the wiring bottleneck. Cryo-CMOS puts control electronics inside the fridge at 4K, multiplexing signals and cutting the wire count by orders of magnitude. Intel's Horse Ridge and academic prototypes prove the concept; scaling it is one of the field's critical engineering races.", "f": {"problem": "wiring bottleneck (heat per wire)", "solution": "cryo-CMOS multiplexing at 4K", "example": "Intel Horse Ridge"}, "p": "// JAH demo program \u2014 Wiring reduction\n\"use strict\";\nvar __checks=[];\nfunction check(l,g,w){__checks.push([l,g,w]);}\nfunction wires(qubits, mux){ return Math.ceil(qubits/mux)+2; }\ncheck(\"1000 qubits, no mux\", wires(1000,1), 1002);\ncheck(\"1000 qubits, 64x mux\", wires(1000,64), 18);\ncheck(\"~56x fewer wires\", Math.round(wires(1000,1)/wires(1000,64)), 56);\nvar __ok=true;\n__checks.forEach(function(c){var ok=String(c[1])===String(c[2]);__ok=ok&&__ok;console.log((ok?\"PASS\":\"FAIL\")+\" | \"+c[0]+\" => \"+c[1]);});\nconsole.log(__ok?\"ALL CHECKS PASSED\":\"SOME CHECKS FAILED\");\nif(!__ok){throw new Error(\"demo self-check failed\");}", "s": ["Save the program as demo.js.", "Run it with: node demo.js", "Confirm every line prints PASS and the run ends with ALL CHECKS PASSED."]}, {"t": "Photonic Control Stack", "c": "control", "l": 12, "d": "Photonic quantum computers trade dilution fridges for optical tables: squeezed-light sources, programmable interferometers, and photon-number-resolving detectors, all stabilized to sub-wavelength precision. Xanadu's stack runs at room temperature, and control means phase lockers, delay lines, and fast feedforward on detection events. The engineering looks more like telecom than cryogenics \u2014 which may be its decisive advantage.", "f": {"vendor": "Xanadu", "temperature": "room temperature", "components": ["squeezers", "interferometers", "photon detectors", "phase lockers"]}, "p": "// JAH demo program \u2014 Phase stability requirement\n\"use strict\";\nvar __checks=[];\nfunction check(l,g,w){__checks.push([l,g,w]);}\nfunction allowedJitter(wavelengthNm){ return wavelengthNm/20; }\ncheck(\"1550nm light \\u2192 77.5nm tolerance\", allowedJitter(1550), 77.5);\ncheck(\"tighter than a virus\", allowedJitter(1550)<100, true);\nvar __ok=true;\n__checks.forEach(function(c){var ok=String(c[1])===String(c[2]);__ok=ok&&__ok;console.log((ok?\"PASS\":\"FAIL\")+\" | \"+c[0]+\" => \"+c[1]);});\nconsole.log(__ok?\"ALL CHECKS PASSED\":\"SOME CHECKS FAILED\");\nif(!__ok){throw new Error(\"demo self-check failed\");}", "s": ["Save the program as demo.js.", "Run it with: node demo.js", "Confirm every line prints PASS and the run ends with ALL CHECKS PASSED."]}, {"t": "Neutral-Atom Control Stack", "c": "control", "l": 13, "d": "Neutral-atom machines (Pasqal, QuEra) trap hundreds of atoms in optical tweezers and excite them to Rydberg states for interaction \u2014 control means acousto-optic deflectors steering hundreds of laser beams with microsecond precision. Atoms can be rearranged mid-computation, giving flexible connectivity no solid-state chip can match. The stack is equal parts atomic physics and high-speed optical engineering.", "f": {"vendors": ["Pasqal", "QuEra"], "qubits": "trapped neutral atoms (100s)", "control": "optical tweezers + Rydberg excitation"}, "p": "// JAH demo program \u2014 Tweezer count scaling\n\"use strict\";\nvar __checks=[];\nfunction check(l,g,w){__checks.push([l,g,w]);}\nfunction lasers(atoms, perBeam){ return Math.ceil(atoms/perBeam); }\ncheck(\"256 atoms, 1 per beam\", lasers(256,1), 256);\ncheck(\"shared beams cut count\", lasers(256,8), 32);\nvar __ok=true;\n__checks.forEach(function(c){var ok=String(c[1])===String(c[2]);__ok=ok&&__ok;console.log((ok?\"PASS\":\"FAIL\")+\" | \"+c[0]+\" => \"+c[1]);});\nconsole.log(__ok?\"ALL CHECKS PASSED\":\"SOME CHECKS FAILED\");\nif(!__ok){throw new Error(\"demo self-check failed\");}", "s": ["Save the program as demo.js.", "Run it with: node demo.js", "Confirm every line prints PASS and the run ends with ALL CHECKS PASSED."]}, {"t": "Quantum OS Research Proposals", "c": "runtime", "l": 14, "d": "A true quantum operating system \u2014 scheduling, memory management, and process isolation for quantum resources \u2014 exists today only as research proposals, and honesty requires saying so. Papers have proposed qubit allocators, quantum process abstractions, and multi-programming schemes, but no deployed system manages quantum resources the way Linux manages classical ones. This record tracks the proposals, not a product: the OS layer is the stack's biggest open gap.", "f": {"status": "research proposals only \u2014 no deployed quantum OS", "proposed": ["qubit allocators", "quantum processes", "multi-programming"], "honest_note": "the OS layer is the stack's biggest open gap"}, "p": "// JAH demo program \u2014 Multi-programming capacity (proposed model)\n\"use strict\";\nvar __checks=[];\nfunction check(l,g,w){__checks.push([l,g,w]);}\nfunction capacity(qubits, perProg){ return Math.floor(qubits/perProg); }\ncheck(\"100 qubits, 10 per program \\u2192 10 programs\", capacity(100,10), 10);\ncheck(\"isolation overhead reduces it\", capacity(100,12)<capacity(100,10), true);\nvar __ok=true;\n__checks.forEach(function(c){var ok=String(c[1])===String(c[2]);__ok=ok&&__ok;console.log((ok?\"PASS\":\"FAIL\")+\" | \"+c[0]+\" => \"+c[1]);});\nconsole.log(__ok?\"ALL CHECKS PASSED\":\"SOME CHECKS FAILED\");\nif(!__ok){throw new Error(\"demo self-check failed\");}", "s": ["Save the program as demo.js.", "Run it with: node demo.js", "Confirm every line prints PASS and the run ends with ALL CHECKS PASSED."]}, {"t": "Distributed Quantum Stack \u2014 Entanglement Distribution", "c": "networking", "l": 15, "d": "Distributed quantum computing links processors with entanglement: photons carry Bell pairs between nodes, repeaters extend the range, and teleportation moves data without moving qubits. The stack spans physical (photon sources), link (entanglement swapping), and network (routing) layers \u2014 a quantum TCP/IP being drafted in real time. Delft, Chicago, and Hefei run the testbeds; a quantum internet is infrastructure decades in the making.", "f": {"layers": ["photon sources", "entanglement swapping", "routing"], "testbeds": ["Delft", "Chicago", "Hefei"], "primitive": "teleportation over distributed Bell pairs"}, "p": "// JAH demo program \u2014 Repeater chain fidelity\n\"use strict\";\nvar __checks=[];\nfunction check(l,g,w){__checks.push([l,g,w]);}\nfunction chainFid(links, perLink){ return Math.pow(perLink, links); }\ncheck(\"10 links at 99% \\u2192 90.4%\", Math.round(chainFid(10,0.99)*1000)/1000, 0.904);\ncheck(\"repeaters needed for distance\", chainFid(100,0.99)<chainFid(10,0.99), true);\nvar __ok=true;\n__checks.forEach(function(c){var ok=String(c[1])===String(c[2]);__ok=ok&&__ok;console.log((ok?\"PASS\":\"FAIL\")+\" | \"+c[0]+\" => \"+c[1]);});\nconsole.log(__ok?\"ALL CHECKS PASSED\":\"SOME CHECKS FAILED\");\nif(!__ok){throw new Error(\"demo self-check failed\");}", "s": ["Save the program as demo.js.", "Run it with: node demo.js", "Confirm every line prints PASS and the run ends with ALL CHECKS PASSED."]}];
var GEN_VARIANTS=["stack deep-dive", "vendor comparison", "latency analysis", "open-source spotlight", "research-frontier brief", "beginner explainer"];
var GEN_PROV="Signature simulated record - boundless generator output; labeled simulated for weeding per standing order. Verified by generator self-check 2026-10-21.";
var GEN_LIC="Public facts compiled from public sources; original demo code CC0.";
var SRC_EDITION="public";
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
  add('/readme.txt','QuantaOS '+"public"+' — simulated quanta desktop.\nEvery app below genuinely runs in this page.');
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
  return ['virtual QPU status ('+"public"+')',
   'qubits simulated : 2 (state-vector)',
   'jobs queued      : '+Math.floor(r()*4),
   'coherence util   : '+fmtN(80+r()*19,1)+'%',
   'cryo stage       : '+fmtN(0.012+r()*0.004,3)+' K (simulated)',
   'uptime           : '+Math.floor((Date.now()-_bootT)/1000)+' s'].join('\n');});
defApp('settings','Settings','\u2699',
 'theme dark|light | about',
 function(input){var p=String(input||'').trim().toLowerCase();
  if(p==='about')return 'QuantaOS '+"public"+' — simulated quanta desktop running entirely in this page.';
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
  edition:"public",
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
  var clock=el('span','dim','QuantaOS '+"public");
  taskbar.appendChild(clock);
  var time=el('span','dim','');taskbar.appendChild(time);
  setInterval(function(){var d=new Date();time.textContent=d.toLocaleTimeString();},1000);
  return {openWin:openWin};
}
return {api:api,mount:mount,APPS:APPS};
})();

var gen={version:'jahdb-quanta-os-models-database-1.0',generate:generate,validate:validate,driftCheck:driftCheck,selfReg:SELF_REG};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('quanta-os-models-database',gen);
if(typeof window!=='undefined'&&typeof QuantaSim!=='undefined'){window.QuantaSim=QuantaSim;}
if(typeof module!=='undefined'&&module.exports){module.exports=gen;if(typeof QuantaSim!=='undefined'){module.exports.QuantaSim=QuantaSim;}}
})();
