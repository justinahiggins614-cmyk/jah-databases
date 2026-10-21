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
var PREFIX='JAH-QCTO-';
var SEEDS=[{"t": "Qiskit \u2014 IBM's Open-Source Quantum SDK", "c": "sdks", "l": 1, "d": "Qiskit is the most widely used quantum SDK: a Python framework for building circuits, transpiling them to hardware, and running on IBM's 100+ qubit superconducting processors or high-performance simulators. Its stack spans Terra (circuits), Aer (simulators), and Runtime (hybrid execution), with Qiskit Patterns codifying reusable workflows. Open-source under Apache 2.0, it is the default entry point for learning quantum programming.", "f": {"vendor": "IBM", "language": "Python", "license": "Apache 2.0", "hardware": "IBM superconducting QPUs", "stack": ["Terra \u2014 circuits", "Aer \u2014 simulators", "Runtime \u2014 hybrid execution"]}, "p": "// JAH demo program \u2014 Bell-state simulator (mini Qiskit-style)\n\"use strict\";\nvar __checks=[];\nfunction check(l,g,w){__checks.push([l,g,w]);}\nfunction bell(){ var s=[1,0,0,0];\n// H on q0\n  var h=[[Math.SQRT1_2,Math.SQRT1_2],[Math.SQRT1_2,-Math.SQRT1_2]];\n  var n=[0,0,0,0]; for(var i=0;i<4;i++){ var b=(i>>1)&1; for(var nb=0;nb<2;nb++){ var j=(i&1)|(nb<<1); n[j]+=h[b][nb]*s[i]; } }\n  s=n; n=[0,0,0,0]; for(var k=0;k<4;k++){ var c=(k>>1)&1; var j2=c?(k^1):k; n[j2]+=s[k]; }\n  return n.map(function(a){return Math.round(a*a*100)/100;}); }\nvar probs=bell();\ncheck(\"P(|00>)=0.5\", probs[0], 0.5);\ncheck(\"P(|11>)=0.5\", probs[3], 0.5);\ncheck(\"P(|01>)=P(|10>)=0\", probs[1]+probs[2], 0);\ncheck(\"probabilities sum to 1\", probs.reduce(function(a,b){return a+b;},0), 1);\nvar __ok=true;\n__checks.forEach(function(c){var ok=String(c[1])===String(c[2]);__ok=ok&&__ok;console.log((ok?\"PASS\":\"FAIL\")+\" | \"+c[0]+\" => \"+c[1]);});\nconsole.log(__ok?\"ALL CHECKS PASSED\":\"SOME CHECKS FAILED\");\nif(!__ok){throw new Error(\"demo self-check failed\");}", "s": ["Save the program as demo.js.", "Run it with: node demo.js", "Confirm every line prints PASS and the run ends with ALL CHECKS PASSED."]}, {"t": "Cirq \u2014 Google's Quantum SDK", "c": "sdks", "l": 2, "d": "Cirq is Google's Python SDK for noisy intermediate-scale quantum computing, built around the realities of real hardware: qubits on a grid, limited connectivity, and native gate sets. It powered the 2019 quantum-supremacy experiment on Sycamore and pairs with qsim for high-performance simulation. Its moment-based circuit model maps naturally onto superconducting qubit layouts.", "f": {"vendor": "Google", "language": "Python", "license": "Apache 2.0", "notable": "2019 Sycamore supremacy experiment", "simulator": "qsim"}, "p": "// JAH demo program \u2014 Grid-connectivity check\n\"use strict\";\nvar __checks=[];\nfunction check(l,g,w){__checks.push([l,g,w]);}\nfunction neighbors(q, rows, cols){ var r=Math.floor(q/cols), c=q%cols, n=[];\n  if(r>0)n.push(q-cols); if(r<rows-1)n.push(q+cols); if(c>0)n.push(q-1); if(c<cols-1)n.push(q+1); return n; }\ncheck(\"qubit 0 on 3x3 has 2 neighbors\", neighbors(0,3,3).length, 2);\ncheck(\"center qubit has 4\", neighbors(4,3,3).length, 4);\ncheck(\"corner qubits listed\", neighbors(0,3,3).join(','), \"3,1\");\nvar __ok=true;\n__checks.forEach(function(c){var ok=String(c[1])===String(c[2]);__ok=ok&&__ok;console.log((ok?\"PASS\":\"FAIL\")+\" | \"+c[0]+\" => \"+c[1]);});\nconsole.log(__ok?\"ALL CHECKS PASSED\":\"SOME CHECKS FAILED\");\nif(!__ok){throw new Error(\"demo self-check failed\");}", "s": ["Save the program as demo.js.", "Run it with: node demo.js", "Confirm every line prints PASS and the run ends with ALL CHECKS PASSED."]}, {"t": "PennyLane \u2014 Quantum Machine Learning SDK", "c": "sdks", "l": 3, "d": "PennyLane by Xanadu is the SDK for quantum machine learning: it treats quantum circuits as differentiable programs and plugs them into PyTorch, TensorFlow, and JAX for gradient-based training. Its device abstraction runs the same code on simulators and on Xanadu's photonic hardware, Rigetti, or IBM backends. If QML finds its killer app, it will likely be prototyped in PennyLane first.", "f": {"vendor": "Xanadu", "language": "Python", "paradigm": "differentiable quantum programming", "integrates": ["PyTorch", "TensorFlow", "JAX"]}, "p": "// JAH demo program \u2014 Parameter-shift gradient (PennyLane's core trick)\n\"use strict\";\nvar __checks=[];\nfunction check(l,g,w){__checks.push([l,g,w]);}\nfunction f(th){ return Math.cos(th); } // Pauli-Z expectation under Rx(th)\nfunction grad(th){ return (f(th+Math.PI/2)-f(th-Math.PI/2))/2; } // parameter-shift rule\ncheck(\"gradient of cos at \\u03c0/4 \\u2248 -0.707\", Math.round(grad(Math.PI/4)*1000)/1000, -0.707);\ncheck(\"gradient at \\u03b8=0 \\u2248 0\", Math.abs(grad(0))<0.01, true);\nvar __ok=true;\n__checks.forEach(function(c){var ok=String(c[1])===String(c[2]);__ok=ok&&__ok;console.log((ok?\"PASS\":\"FAIL\")+\" | \"+c[0]+\" => \"+c[1]);});\nconsole.log(__ok?\"ALL CHECKS PASSED\":\"SOME CHECKS FAILED\");\nif(!__ok){throw new Error(\"demo self-check failed\");}", "s": ["Save the program as demo.js.", "Run it with: node demo.js", "Confirm every line prints PASS and the run ends with ALL CHECKS PASSED."]}, {"t": "Q# and Azure Quantum", "c": "sdks", "l": 4, "d": "Q# is Microsoft's quantum programming language \u2014 a standalone language with quantum-native types like Qubit and Result, plus libraries for chemistry, arithmetic, and error correction. Azure Quantum brokers access to IonQ, Quantinuum, Rigetti, and Pasqal hardware behind one API, and the newer Azure Quantum Elements targets scientific discovery workflows. Q#'s type system catches quantum bugs \u2014 like using a released qubit \u2014 at compile time.", "f": {"vendor": "Microsoft", "language": "Q#", "platform": "Azure Quantum", "hardware_partners": ["IonQ", "Quantinuum", "Rigetti", "Pasqal"]}, "p": "// JAH demo program \u2014 Qubit-release safety (type-system idea)\n\"use strict\";\nvar __checks=[];\nfunction check(l,g,w){__checks.push([l,g,w]);}\nfunction useQubit(q, released){ if(released.indexOf(q)>=0) return 'COMPILE ERROR: use of released qubit'; return 'ok'; }\ncheck(\"fresh qubit ok\", useQubit(0,[]), \"ok\");\ncheck(\"released qubit caught\", useQubit(1,[1]), \"COMPILE ERROR: use of released qubit\");\nvar __ok=true;\n__checks.forEach(function(c){var ok=String(c[1])===String(c[2]);__ok=ok&&__ok;console.log((ok?\"PASS\":\"FAIL\")+\" | \"+c[0]+\" => \"+c[1]);});\nconsole.log(__ok?\"ALL CHECKS PASSED\":\"SOME CHECKS FAILED\");\nif(!__ok){throw new Error(\"demo self-check failed\");}", "s": ["Save the program as demo.js.", "Run it with: node demo.js", "Confirm every line prints PASS and the run ends with ALL CHECKS PASSED."]}, {"t": "Amazon Braket SDK", "c": "sdks", "l": 5, "d": "Amazon Braket is AWS's quantum service: one SDK addressing IonQ, IQM, QuEra, and Rigetti QPUs plus managed simulators like SV1 (state vector) and TN1 (tensor network). Braket Hybrid Jobs runs variational algorithms with classical compute co-located near the QPU to cut latency. For teams already on AWS, it is the path of least resistance to real hardware.", "f": {"vendor": "AWS", "language": "Python", "hardware": ["IonQ", "IQM", "QuEra", "Rigetti"], "simulators": ["SV1 state vector", "TN1 tensor network", "local simulator"]}, "p": "// JAH demo program \u2014 Shot-budget planner\n\"use strict\";\nvar __checks=[];\nfunction check(l,g,w){__checks.push([l,g,w]);}\nfunction shotsNeeded(eps){ return Math.ceil(1/(eps*eps)); }\ncheck(\"1% precision \\u2192 10k shots\", shotsNeeded(0.01), 10000);\ncheck(\"0.1% \\u2192 1M shots\", shotsNeeded(0.001), 1000000);\nvar __ok=true;\n__checks.forEach(function(c){var ok=String(c[1])===String(c[2]);__ok=ok&&__ok;console.log((ok?\"PASS\":\"FAIL\")+\" | \"+c[0]+\" => \"+c[1]);});\nconsole.log(__ok?\"ALL CHECKS PASSED\":\"SOME CHECKS FAILED\");\nif(!__ok){throw new Error(\"demo self-check failed\");}", "s": ["Save the program as demo.js.", "Run it with: node demo.js", "Confirm every line prints PASS and the run ends with ALL CHECKS PASSED."]}, {"t": "Strawberry Fields \u2014 Photonic Quantum SDK", "c": "sdks", "l": 6, "d": "Strawberry Fields is Xanadu's SDK for photonic continuous-variable quantum computing, where information lives in qumodes \u2014 the amplitude and phase of light \u2014 instead of two-level qubits. Gaussian gates, squeezing, and photon counting replace the usual gate set, and programs run on Xanadu's photonic chips or the built-in simulators. It is the main on-ramp to the photonic path to quantum computing.", "f": {"vendor": "Xanadu", "model": "continuous-variable (qumodes)", "language": "Python", "operations": ["squeezing", "displacement", "beamsplitter", "photon counting"]}, "p": "// JAH demo program \u2014 Squeezing noise reduction\n\"use strict\";\nvar __checks=[];\nfunction check(l,g,w){__checks.push([l,g,w]);}\nfunction noise(r){ return Math.exp(-2*r); }\ncheck(\"no squeezing \\u2192 1\", noise(0), 1);\ncheck(\"r=1 \\u2192 ~0.135\", Math.round(noise(1)*1000)/1000, 0.135);\ncheck(\"more squeezing, less noise\", noise(2)<noise(1), true);\nvar __ok=true;\n__checks.forEach(function(c){var ok=String(c[1])===String(c[2]);__ok=ok&&__ok;console.log((ok?\"PASS\":\"FAIL\")+\" | \"+c[0]+\" => \"+c[1]);});\nconsole.log(__ok?\"ALL CHECKS PASSED\":\"SOME CHECKS FAILED\");\nif(!__ok){throw new Error(\"demo self-check failed\");}", "s": ["Save the program as demo.js.", "Run it with: node demo.js", "Confirm every line prints PASS and the run ends with ALL CHECKS PASSED."]}, {"t": "QuTiP \u2014 Quantum Toolbox in Python", "c": "simulators", "l": 7, "d": "QuTiP is the open-source workhorse for simulating open quantum systems: Lindblad master equations, Monte Carlo trajectories, and time-dependent Hamiltonians, all in NumPy/SciPy-friendly Python. Before anyone books QPU time, the dynamics get validated in QuTiP. It is cited in thousands of papers and remains the standard for quantum optics and control simulation.", "f": {"type": "open quantum systems simulator", "language": "Python", "solvers": ["Lindblad master equation", "Monte Carlo", "Floquet"]}, "p": "// JAH demo program \u2014 Two-level decay (Lindblad-style)\n\"use strict\";\nvar __checks=[];\nfunction check(l,g,w){__checks.push([l,g,w]);}\nfunction decay(t, gamma){ return Math.exp(-gamma*t); }\ncheck(\"t=0 \\u2192 excited\", decay(0,1), 1);\ncheck(\"t=1, \\u03b3=1 \\u2192 1/e\", Math.round(decay(1,1)*1000)/1000, 0.368);\ncheck(\"decay is monotonic\", decay(2,1)<decay(1,1), true);\nvar __ok=true;\n__checks.forEach(function(c){var ok=String(c[1])===String(c[2]);__ok=ok&&__ok;console.log((ok?\"PASS\":\"FAIL\")+\" | \"+c[0]+\" => \"+c[1]);});\nconsole.log(__ok?\"ALL CHECKS PASSED\":\"SOME CHECKS FAILED\");\nif(!__ok){throw new Error(\"demo self-check failed\");}", "s": ["Save the program as demo.js.", "Run it with: node demo.js", "Confirm every line prints PASS and the run ends with ALL CHECKS PASSED."]}, {"t": "t|ket> \u2014 Quantinuum's Quantum Compiler", "c": "compilers", "l": 8, "d": "t|ket> is Quantinuum's retargetable quantum compiler: it optimizes circuits \u2014 gate cancellation, commutation-based reduction, routing onto device topology \u2014 and retargets them across backends. Benchmarks consistently show it producing among the lowest two-qubit gate counts in the industry, which directly translates to less noise on real hardware. It is available as a Python package and as a compilation service.", "f": {"vendor": "Quantinuum", "type": "retargetable compiler", "language": "Python", "passes": ["gate cancellation", "commutation reduction", "routing", "rebasing"]}, "p": "// JAH demo program \u2014 Gate-cancellation pass demo\n\"use strict\";\nvar __checks=[];\nfunction check(l,g,w){__checks.push([l,g,w]);}\nfunction cancel(gates){ var out=[]; gates.forEach(function(g){\n  var top=out[out.length-1];\n  if(top&&top[0]===g[0]&&top[1]===g[1]&&(g[0]==='X'||g[0]==='H')) out.pop(); else out.push(g); }); return out; }\ncheck(\"X X cancels\", cancel([['X',0],['X',0]]).length, 0);\ncheck(\"H X H survives\", cancel([['H',0],['X',0],['H',0]]).length, 3);\ncheck(\"CNOT never cancels here\", cancel([['CX',0],['CX',0]]).length, 2);\nvar __ok=true;\n__checks.forEach(function(c){var ok=String(c[1])===String(c[2]);__ok=ok&&__ok;console.log((ok?\"PASS\":\"FAIL\")+\" | \"+c[0]+\" => \"+c[1]);});\nconsole.log(__ok?\"ALL CHECKS PASSED\":\"SOME CHECKS FAILED\");\nif(!__ok){throw new Error(\"demo self-check failed\");}", "s": ["Save the program as demo.js.", "Run it with: node demo.js", "Confirm every line prints PASS and the run ends with ALL CHECKS PASSED."]}, {"t": "D-Wave Ocean SDK", "c": "annealing", "l": 9, "d": "Ocean is D-Wave's Python SDK for quantum annealing: formulate problems as binary quadratic models, embed them onto the QPU's Pegasus graph, and sample. It includes hybrid solvers that split work between classical CPUs/GPUs and the annealer, handling problems far larger than the QPU alone. Tens of thousands of developers have run optimization through it.", "f": {"vendor": "D-Wave", "model": "annealing (Ising/QUBO)", "topology": "Pegasus graph", "tools": ["embedding", "hybrid solvers", "problem inspector"]}, "p": "// JAH demo program \u2014 QUBO energy demo\n\"use strict\";\nvar __checks=[];\nfunction check(l,g,w){__checks.push([l,g,w]);}\nfunction qubo(x,Q){ var e=0; for(var i=0;i<x.length;i++)for(var j=0;j<x.length;j++)e+=Q[i][j]*x[i]*x[j]; return e; }\nvar Q=[[2,-3],[-3,0]]; var best={e:1e9,x:null};\nfor(var m=0;m<4;m++){ var x=[(m>>0)&1,(m>>1)&1]; var e=qubo(x,Q); if(e<best.e)best={e:e,x:x}; }\ncheck(\"optimal energy\", best.e, -4);\ncheck(\"optimal x=[1,1]\", best.x.join(''), \"11\");\nvar __ok=true;\n__checks.forEach(function(c){var ok=String(c[1])===String(c[2]);__ok=ok&&__ok;console.log((ok?\"PASS\":\"FAIL\")+\" | \"+c[0]+\" => \"+c[1]);});\nconsole.log(__ok?\"ALL CHECKS PASSED\":\"SOME CHECKS FAILED\");\nif(!__ok){throw new Error(\"demo self-check failed\");}", "s": ["Save the program as demo.js.", "Run it with: node demo.js", "Confirm every line prints PASS and the run ends with ALL CHECKS PASSED."]}, {"t": "PyQuil \u2014 Rigetti's SDK", "c": "sdks", "l": 10, "d": "PyQuil is Rigetti's Python SDK built on Quil, the quantum instruction language that exposes classical-quantum feedback \u2014 mid-circuit measurement and feedforward \u2014 as first-class operations. Rigetti's Quantum Cloud Services pairs it with their superconducting QPUs, and quilc compiles to native gates. Quil's explicit memory model made hybrid algorithms portable before the term was fashionable.", "f": {"vendor": "Rigetti", "language": "Python/Quil", "feature": "classical-quantum feedback in Quil", "compiler": "quilc"}, "p": "// JAH demo program \u2014 Mid-circuit feedback idea\n\"use strict\";\nvar __checks=[];\nfunction check(l,g,w){__checks.push([l,g,w]);}\nfunction feedforward(meas){ return meas===1?'X 1  // correct':'// no correction'; }\ncheck(\"measure 1 \\u2192 correct\", feedforward(1), \"X 1  // correct\");\ncheck(\"measure 0 \\u2192 skip\", feedforward(0), \"// no correction\");\nvar __ok=true;\n__checks.forEach(function(c){var ok=String(c[1])===String(c[2]);__ok=ok&&__ok;console.log((ok?\"PASS\":\"FAIL\")+\" | \"+c[0]+\" => \"+c[1]);});\nconsole.log(__ok?\"ALL CHECKS PASSED\":\"SOME CHECKS FAILED\");\nif(!__ok){throw new Error(\"demo self-check failed\");}", "s": ["Save the program as demo.js.", "Run it with: node demo.js", "Confirm every line prints PASS and the run ends with ALL CHECKS PASSED."]}, {"t": "Mitiq \u2014 Quantum Error Mitigation Toolkit", "c": "mitigation", "l": 11, "d": "Mitiq is the open-source toolkit for error mitigation \u2014 the software techniques (zero-noise extrapolation, probabilistic error cancellation, Clifford data regression) that squeeze useful results from noisy qubits without full error correction. It plugs into Cirq, Qiskit, PennyLane, and Braket, applying mitigation as circuit transformations. On current hardware, mitigation is often the difference between noise and signal.", "f": {"type": "error mitigation", "techniques": ["ZNE", "PEC", "CDR"], "integrates": ["Cirq", "Qiskit", "PennyLane", "Braket"]}, "p": "// JAH demo program \u2014 ZNE linear extrapolation\n\"use strict\";\nvar __checks=[];\nfunction check(l,g,w){__checks.push([l,g,w]);}\nfunction zne(vals){ var x=[1,3,5], n=3, sx=9, sy=vals[0]+vals[1]+vals[2], sxx=35, sxy=x[0]*vals[0]+x[1]*vals[1]+x[2]*vals[2];\n  var slope=(n*sxy-sx*sy)/(n*sxx-sx*sx); return (sy-slope*sx)/n; }\ncheck(\"extrapolates toward true 1.0\", Math.abs(zne([0.98,0.94,0.90])-1.0)<0.02, true);\ncheck(\"beats the noisiest point\", zne([0.98,0.94,0.90])>0.90, true);\nvar __ok=true;\n__checks.forEach(function(c){var ok=String(c[1])===String(c[2]);__ok=ok&&__ok;console.log((ok?\"PASS\":\"FAIL\")+\" | \"+c[0]+\" => \"+c[1]);});\nconsole.log(__ok?\"ALL CHECKS PASSED\":\"SOME CHECKS FAILED\");\nif(!__ok){throw new Error(\"demo self-check failed\");}", "s": ["Save the program as demo.js.", "Run it with: node demo.js", "Confirm every line prints PASS and the run ends with ALL CHECKS PASSED."]}, {"t": "Qibo \u2014 Full-Stack Quantum SDK", "c": "sdks", "l": 12, "d": "Qibo is an open-source full-stack framework covering simulation, hardware control, and calibration \u2014 with GPU-accelerated simulators and a lab-instrument layer for real qubit bring-up. Its qibolab module speaks to actual control electronics, making it one of the few frameworks spanning from pulse calibration to algorithms. Developed with an eye toward self-hosted quantum labs.", "f": {"type": "full-stack (sim + hardware)", "language": "Python", "modules": ["simulation", "qibolab instruments", "calibration"]}, "p": "// JAH demo program \u2014 GPU-style batch simulation timing model\n\"use strict\";\nvar __checks=[];\nfunction check(l,g,w){__checks.push([l,g,w]);}\nfunction timeMs(qubits, backend){ var base=Math.pow(2,qubits)*0.001; return backend==='gpu'?base/20:base; }\ncheck(\"20 qubits CPU \\u2248 1000ms\", Math.round(timeMs(20,'cpu')), 1049);\ncheck(\"GPU ~20x faster\", Math.round(timeMs(20,'cpu')/timeMs(20,'gpu')), 20);\nvar __ok=true;\n__checks.forEach(function(c){var ok=String(c[1])===String(c[2]);__ok=ok&&__ok;console.log((ok?\"PASS\":\"FAIL\")+\" | \"+c[0]+\" => \"+c[1]);});\nconsole.log(__ok?\"ALL CHECKS PASSED\":\"SOME CHECKS FAILED\");\nif(!__ok){throw new Error(\"demo self-check failed\");}", "s": ["Save the program as demo.js.", "Run it with: node demo.js", "Confirm every line prints PASS and the run ends with ALL CHECKS PASSED."]}, {"t": "ProjectQ \u2014 ETH Zurich Quantum SDK", "c": "sdks", "l": 13, "d": "ProjectQ from ETH Zurich compiles high-level quantum programs down to hardware backends through an extensible compiler engine, and its simulators handle 20+ qubits efficiently. It emphasizes clean abstractions \u2014 engines, mappers, backends \u2014 that compiler researchers extend, and it interoperates with IBM hardware. A favorite in academic quantum-compilation courses.", "f": {"origin": "ETH Zurich", "language": "Python", "paradigm": "extensible compiler engines"}, "p": "// JAH demo program \u2014 Compiler-engine pipeline demo\n\"use strict\";\nvar __checks=[];\nfunction check(l,g,w){__checks.push([l,g,w]);}\nfunction compileProg(gates){ return gates.map(function(g){ return g[0]==='H'?'U2(0,pi) q'+g[1]:g[0]+' q'+g[1]; }); }\ncheck(\"H rebased to U2\", compileProg([['H',0]])[0], \"U2(0,pi) q0\");\ncheck(\"X passes through\", compileProg([['X',1]])[0], \"X q1\");\nvar __ok=true;\n__checks.forEach(function(c){var ok=String(c[1])===String(c[2]);__ok=ok&&__ok;console.log((ok?\"PASS\":\"FAIL\")+\" | \"+c[0]+\" => \"+c[1]);});\nconsole.log(__ok?\"ALL CHECKS PASSED\":\"SOME CHECKS FAILED\");\nif(!__ok){throw new Error(\"demo self-check failed\");}", "s": ["Save the program as demo.js.", "Run it with: node demo.js", "Confirm every line prints PASS and the run ends with ALL CHECKS PASSED."]}, {"t": "Yao.jl \u2014 Quantum Computing in Julia", "c": "sdks", "l": 14, "d": "Yao.jl brings quantum simulation to Julia, exploiting the language's speed and autodiff for differentiable quantum programming and batched circuit simulation. Its block-based circuit representation composes like LEGO, and benchmarks show it among the fastest state-vector simulators per qubit. For researchers living in Julia, it removes the two-language problem from quantum work.", "f": {"language": "Julia", "paradigm": "differentiable, block-based circuits"}, "p": "// JAH demo program \u2014 Block composition demo\n\"use strict\";\nvar __checks=[];\nfunction check(l,g,w){__checks.push([l,g,w]);}\nfunction chain(blocks){ return blocks.join(' \u2192 '); }\ncheck(\"blocks compose\", chain(['H(1)','CNOT(1,2)','measure']), \"H(1) \\u2192 CNOT(1,2) \\u2192 measure\");\nvar __ok=true;\n__checks.forEach(function(c){var ok=String(c[1])===String(c[2]);__ok=ok&&__ok;console.log((ok?\"PASS\":\"FAIL\")+\" | \"+c[0]+\" => \"+c[1]);});\nconsole.log(__ok?\"ALL CHECKS PASSED\":\"SOME CHECKS FAILED\");\nif(!__ok){throw new Error(\"demo self-check failed\");}", "s": ["Save the program as demo.js.", "Run it with: node demo.js", "Confirm every line prints PASS and the run ends with ALL CHECKS PASSED."]}, {"t": "qsim \u2014 Google's High-Performance Simulator", "c": "simulators", "l": 15, "d": "qsim is Google's C++ state-vector simulator with a Cirq front end, built for the supremacy era: it simulates 30+ qubit circuits using gate fusion, SIMD, and multi-threading. It validated the Sycamore supremacy circuits classically where possible and remains the reference for 'how far can classical simulation go.' When a paper claims a quantum advantage, qsim-class tools set the bar it must beat.", "f": {"vendor": "Google", "type": "state-vector simulator", "language": "C++ with Cirq frontend", "techniques": ["gate fusion", "SIMD", "multithreading"]}, "p": "// JAH demo program \u2014 Simulation cost model\n\"use strict\";\nvar __checks=[];\nfunction check(l,g,w){__checks.push([l,g,w]);}\nfunction flops(qubits, gates){ return gates*Math.pow(2,qubits)*8; }\ncheck(\"30 qubits, 1000 gates \\u2248 8.6e12 flops\", flops(30,1000)>8e12, true);\ncheck(\"each qubit doubles cost\", flops(21,100)/flops(20,100), 2);\nvar __ok=true;\n__checks.forEach(function(c){var ok=String(c[1])===String(c[2]);__ok=ok&&__ok;console.log((ok?\"PASS\":\"FAIL\")+\" | \"+c[0]+\" => \"+c[1]);});\nconsole.log(__ok?\"ALL CHECKS PASSED\":\"SOME CHECKS FAILED\");\nif(!__ok){throw new Error(\"demo self-check failed\");}", "s": ["Save the program as demo.js.", "Run it with: node demo.js", "Confirm every line prints PASS and the run ends with ALL CHECKS PASSED."]}];
var GEN_VARIANTS=["quickstart recipe", "backend comparison", "performance notes", "migration guide", "best-practices sheet", "troubleshooting card"];
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

var gen={version:'jahdb-quanta-computer-tools-database-1.0',generate:generate,validate:validate,driftCheck:driftCheck,selfReg:SELF_REG};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('quanta-computer-tools-database',gen);
if(typeof window!=='undefined'&&typeof QuantaSim!=='undefined'){window.QuantaSim=QuantaSim;}
if(typeof module!=='undefined'&&module.exports){module.exports=gen;if(typeof QuantaSim!=='undefined'){module.exports.QuantaSim=QuantaSim;}}
})();
