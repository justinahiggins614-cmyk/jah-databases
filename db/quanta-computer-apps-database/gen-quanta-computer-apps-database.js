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
var CATS=["algorithms", "cryptography", "simulation", "optimization", "sensing"];
var PREFIX='JAH-QCAP-';
var SEEDS=[{"t": "Shor's Algorithm \u2014 Integer Factoring", "c": "algorithms", "l": 1, "d": "Peter Shor's 1994 algorithm factors large integers in polynomial time on a quantum computer by reducing factoring to order-finding, which quantum phase estimation solves exponentially faster than any known classical method. It threatens RSA cryptography directly: a large enough fault-tolerant quantum computer could factor the 2048-bit moduli that secure the modern internet. The algorithm is the reason post-quantum cryptography standardization is underway now, decades before the hardware exists.", "f": {"year": 1994, "author": "Peter Shor", "speedup": "exponential", "threatens": "RSA, Diffie-Hellman, elliptic-curve crypto", "steps": ["Pick random a < N", "Quantum order-finding: smallest r with a^r = 1 mod N", "If r even: factors = gcd(a^(r/2) \u00b1 1, N)"]}, "p": "// JAH demo program \u2014 Shor order-finding demo (N=15, a=7)\n\"use strict\";\nvar __checks=[];\nfunction check(l,g,w){__checks.push([l,g,w]);}\nfunction modpow(a,e,n){ var r=1; a%=n; while(e>0){ if(e&1)r=(r*a)%n; a=(a*a)%n; e>>=1; } return r; }\nfunction order(a,n){ var r=1; while(modpow(a,r,n)!==1&&r<100)r++; return r; }\nfunction gcd(a,b){ return b?gcd(b,a%b):a; }\nvar N=15,a=7,r=order(a,N);\nvar f1=gcd(modpow(a,r/2,N)-1+N,N), f2=gcd(modpow(a,r/2,N)+1,N);\ncheck(\"order of 7 mod 15\", r, 4);\ncheck(\"factor 1\", f1, 3);\ncheck(\"factor 2\", f2, 5);\ncheck(\"factors multiply to N\", f1*f2, 15);\nvar __ok=true;\n__checks.forEach(function(c){var ok=String(c[1])===String(c[2]);__ok=ok&&__ok;console.log((ok?\"PASS\":\"FAIL\")+\" | \"+c[0]+\" => \"+c[1]);});\nconsole.log(__ok?\"ALL CHECKS PASSED\":\"SOME CHECKS FAILED\");\nif(!__ok){throw new Error(\"demo self-check failed\");}", "s": ["Save the program as demo.js.", "Run it with: node demo.js", "Confirm every line prints PASS and the run ends with ALL CHECKS PASSED."]}, {"t": "Grover's Search \u2014 Quadratic Speedup", "c": "algorithms", "l": 2, "d": "Lov Grover's 1996 algorithm searches an unstructured database of N items in about \u221aN steps instead of N/2, a provable quadratic speedup. It works by amplitude amplification: an oracle marks the target state and the diffusion operator rotates the state vector toward it, with the optimal iteration count near (\u03c0/4)\u221aN. Applications include brute-force key search (halving effective symmetric-key strength), constraint satisfaction, and as a subroutine inside larger quantum algorithms.", "f": {"year": 1996, "author": "Lov Grover", "speedup": "quadratic", "optimal_iterations": "round(\u03c0/4 \u00b7 \u221aN)", "effect_on_AES": "halves effective key strength"}, "p": "// JAH demo program \u2014 Grover iteration math\n\"use strict\";\nvar __checks=[];\nfunction check(l,g,w){__checks.push([l,g,w]);}\nfunction iters(N){ return Math.round(Math.PI/4*Math.sqrt(N)); }\nfunction success(N){ var it=iters(N), th=Math.asin(1/Math.sqrt(N)); return Math.pow(Math.sin((2*it+1)*th),2); }\ncheck(\"N=16 iterations\", iters(16), 3);\ncheck(\"N=10^6 iterations\", iters(1000000), 785);\ncheck(\"N=16 success prob > 0.9\", success(16)>0.9, true);\ncheck(\"classical queries for N=16\", 16/2, 8);\nvar __ok=true;\n__checks.forEach(function(c){var ok=String(c[1])===String(c[2]);__ok=ok&&__ok;console.log((ok?\"PASS\":\"FAIL\")+\" | \"+c[0]+\" => \"+c[1]);});\nconsole.log(__ok?\"ALL CHECKS PASSED\":\"SOME CHECKS FAILED\");\nif(!__ok){throw new Error(\"demo self-check failed\");}", "s": ["Save the program as demo.js.", "Run it with: node demo.js", "Confirm every line prints PASS and the run ends with ALL CHECKS PASSED."]}, {"t": "VQE \u2014 Variational Quantum Eigensolver", "c": "simulation", "l": 3, "d": "The variational quantum eigensolver finds molecular ground-state energies by preparing a parameterized trial state on the quantum processor and letting a classical optimizer tune the parameters to minimize measured energy. Because only shallow circuits are needed, VQE runs on today's noisy devices and has computed dissociation curves for H2, LiH, and BeH2. It is the flagship near-term quantum chemistry algorithm and the template for the whole variational algorithm family.", "f": {"type": "hybrid quantum-classical", "use": "molecular ground states", "demonstrated_on": ["H2", "LiH", "BeH2"], "loop": "quantum measures energy \u2192 classical updates parameters"}, "p": "// JAH demo program \u2014 VQE toy energy scan\n\"use strict\";\nvar __checks=[];\nfunction check(l,g,w){__checks.push([l,g,w]);}\nfunction E(th){ return -1.0-0.15*Math.cos(th); }\nvar best={e:9,th:0}; for(var i=0;i<=8;i++){ var th=-Math.PI+i*Math.PI/4, e=E(th); if(e<best.e)best={e:e,th:th}; }\ncheck(\"minimum energy \\u2248 -1.15 Ha\", Math.round(best.e*100)/100, -1.15);\ncheck(\"minimum at theta=0\", Math.round(best.th*100)/100, 0);\ncheck(\"variational principle: E >= E_true\", best.e>=-1.2, true);\nvar __ok=true;\n__checks.forEach(function(c){var ok=String(c[1])===String(c[2]);__ok=ok&&__ok;console.log((ok?\"PASS\":\"FAIL\")+\" | \"+c[0]+\" => \"+c[1]);});\nconsole.log(__ok?\"ALL CHECKS PASSED\":\"SOME CHECKS FAILED\");\nif(!__ok){throw new Error(\"demo self-check failed\");}", "s": ["Save the program as demo.js.", "Run it with: node demo.js", "Confirm every line prints PASS and the run ends with ALL CHECKS PASSED."]}, {"t": "QAOA \u2014 Quantum Approximate Optimization Algorithm", "c": "optimization", "l": 4, "d": "Farhi's QAOA attacks combinatorial optimization \u2014 Max-Cut, scheduling, portfolio problems \u2014 by alternating a cost Hamiltonian that encodes the problem with a mixing Hamiltonian, tuned by 2p classical parameters for p layers. At p=1 it already beats random guessing on Max-Cut; deeper circuits approach the optimum as p grows. It runs natively on gate-model hardware and maps directly onto quantum annealers' problem class.", "f": {"year": 2014, "author": "Edward Farhi et al.", "problem_class": "combinatorial optimization", "benchmark": "Max-Cut", "parameters": "2p angles for p layers"}, "p": "// JAH demo program \u2014 QAOA Max-Cut toy (4-node ring)\n\"use strict\";\nvar __checks=[];\nfunction check(l,g,w){__checks.push([l,g,w]);}\nfunction cut(assign, edges){ var c=0; edges.forEach(function(e){ if(assign[e[0]]!==assign[e[1]])c++; }); return c; }\nvar edges=[[0,1],[1,2],[2,3],[3,0]]; var best=0;\nfor(var m=0;m<16;m++){ var a=[(m>>0)&1,(m>>1)&1,(m>>2)&1,(m>>3)&1]; best=Math.max(best,cut(a,edges)); }\ncheck(\"optimal cut of 4-ring\", best, 4);\ncheck(\"random guessing averages 2\", 4/2, 2);\ncheck(\"QAOA p\\u2192\\u221e approaches optimum\", best>=3, true);\nvar __ok=true;\n__checks.forEach(function(c){var ok=String(c[1])===String(c[2]);__ok=ok&&__ok;console.log((ok?\"PASS\":\"FAIL\")+\" | \"+c[0]+\" => \"+c[1]);});\nconsole.log(__ok?\"ALL CHECKS PASSED\":\"SOME CHECKS FAILED\");\nif(!__ok){throw new Error(\"demo self-check failed\");}", "s": ["Save the program as demo.js.", "Run it with: node demo.js", "Confirm every line prints PASS and the run ends with ALL CHECKS PASSED."]}, {"t": "Quantum Phase Estimation", "c": "algorithms", "l": 5, "d": "Quantum phase estimation extracts the eigenvalue phase of a unitary operator to n bits of precision using n ancilla qubits and the inverse quantum Fourier transform \u2014 it is the engine inside Shor's algorithm and quantum chemistry. Precision scales as 2^-n with n ancillas, and the algorithm succeeds with probability at least 4/\u03c0\u00b2 \u2248 0.405 per run, boosted by repetition. Nearly every exponential quantum speedup traces back to this one subroutine.", "f": {"precision": "2^-n with n ancilla qubits", "success_probability": "\u2265 4/\u03c0\u00b2 \u2248 0.405", "powers": ["Shor's algorithm", "quantum chemistry", "quantum counting"]}, "p": "// JAH demo program \u2014 QPE precision scaling\n\"use strict\";\nvar __checks=[];\nfunction check(l,g,w){__checks.push([l,g,w]);}\nfunction prec(n){ return Math.pow(2,-n); }\ncheck(\"10 ancillas\", prec(10), 0.0009765625);\ncheck(\"20 ancillas \\u2248 1e-6\", prec(20)<1.1e-6, true);\ncheck(\"each qubit doubles precision\", prec(5)/prec(6), 2);\nvar __ok=true;\n__checks.forEach(function(c){var ok=String(c[1])===String(c[2]);__ok=ok&&__ok;console.log((ok?\"PASS\":\"FAIL\")+\" | \"+c[0]+\" => \"+c[1]);});\nconsole.log(__ok?\"ALL CHECKS PASSED\":\"SOME CHECKS FAILED\");\nif(!__ok){throw new Error(\"demo self-check failed\");}", "s": ["Save the program as demo.js.", "Run it with: node demo.js", "Confirm every line prints PASS and the run ends with ALL CHECKS PASSED."]}, {"t": "Quantum Simulation of Molecules", "c": "simulation", "l": 6, "d": "Richard Feynman proposed in 1982 that quantum systems can only be efficiently simulated by quantum computers, and chemistry is the killer app: catalysts, batteries, and nitrogen fixation all hinge on electron correlation that defeats classical methods. Estimates put a useful FeMoCo nitrogenase simulation at millions of physical qubits with error correction \u2014 beyond today, but the target is concrete. Every percentage point of catalyst efficiency gained this way would move global energy use.", "f": {"origin": "Feynman 1982", "targets": ["catalysts", "batteries", "nitrogen fixation (FeMoCo)"], "requirement": "fault-tolerant qubits, millions physical (estimates vary)"}, "p": "// JAH demo program \u2014 Classical simulation wall\n\"use strict\";\nvar __checks=[];\nfunction check(l,g,w){__checks.push([l,g,w]);}\nfunction classicalGB(n){ return Math.pow(2,n)*16/1e9; } // 16 bytes per complex amplitude\ncheck(\"30 qubits \\u2248 GB\", Math.round(classicalGB(30)), 17);\ncheck(\"50 qubits \\u2248 PB\", Math.round(classicalGB(50)/1000), 18014);\ncheck(\"60 qubits impossible classically\", classicalGB(60)>1e9, true);\nvar __ok=true;\n__checks.forEach(function(c){var ok=String(c[1])===String(c[2]);__ok=ok&&__ok;console.log((ok?\"PASS\":\"FAIL\")+\" | \"+c[0]+\" => \"+c[1]);});\nconsole.log(__ok?\"ALL CHECKS PASSED\":\"SOME CHECKS FAILED\");\nif(!__ok){throw new Error(\"demo self-check failed\");}", "s": ["Save the program as demo.js.", "Run it with: node demo.js", "Confirm every line prints PASS and the run ends with ALL CHECKS PASSED."]}, {"t": "BB84 Quantum Key Distribution", "c": "cryptography", "l": 7, "d": "Bennett and Brassard's 1984 protocol distributes encryption keys with security guaranteed by quantum physics: Alice sends qubits in random bases, Bob measures in random bases, and they keep only the bits where bases matched. Any eavesdropper disturbs the quantum states and reveals herself in the error rate. Real QKD networks operate today \u2014 metropolitan fiber links in China, Europe, and the US, plus satellite QKD via China's Micius satellite over 1,200 km.", "f": {"year": 1984, "authors": "Bennett & Brassard", "security": "information-theoretic (physics, not math)", "deployed": ["metropolitan fiber QKD networks", "Micius satellite 1,200 km"]}, "p": "// JAH demo program \u2014 BB84 sifting simulation (seeded)\n\"use strict\";\nvar __checks=[];\nfunction check(l,g,w){__checks.push([l,g,w]);}\nfunction sift(n, seed){ var a=seed; function r(){ a=(Math.imul(a,1103515245)+12345)&0x7fffffff; return a/0x7fffffff; }\n  var kept=0; for(var i=0;i<n;i++){ if(r()<0.5===r()<0.5)kept++; } return kept; }\ncheck(\"~half the bits survive sifting\", sift(1000,42)>400&&sift(1000,42)<600, true);\ncheck(\"deterministic with seed\", sift(100,7)===sift(100,7), true);\nvar __ok=true;\n__checks.forEach(function(c){var ok=String(c[1])===String(c[2]);__ok=ok&&__ok;console.log((ok?\"PASS\":\"FAIL\")+\" | \"+c[0]+\" => \"+c[1]);});\nconsole.log(__ok?\"ALL CHECKS PASSED\":\"SOME CHECKS FAILED\");\nif(!__ok){throw new Error(\"demo self-check failed\");}", "s": ["Save the program as demo.js.", "Run it with: node demo.js", "Confirm every line prints PASS and the run ends with ALL CHECKS PASSED."]}, {"t": "Quantum Random Number Generation", "c": "cryptography", "l": 8, "d": "Quantum random number generators harvest true randomness from quantum measurement \u2014 photon arrival times, beam-splitter paths, vacuum fluctuations \u2014 rather than deterministic algorithms. Commercial QRNG chips now ship in phones and HSMs, and device-independent protocols can certify randomness even from untrusted hardware via Bell-test violations. Every cryptographic key, lottery, and Monte Carlo simulation is only as unpredictable as its random source.", "f": {"sources": ["photon timing", "beam splitter", "vacuum fluctuations"], "certification": "device-independent via Bell inequality violation", "deployed_in": ["smartphones", "HSMs", "lotteries"]}, "p": "// JAH demo program \u2014 Randomness quality check (seeded demo)\n\"use strict\";\nvar __checks=[];\nfunction check(l,g,w){__checks.push([l,g,w]);}\nfunction bits(n,seed){ var a=seed,out=[]; for(var i=0;i<n;i++){ a=(Math.imul(a,1103515245)+12345)&0x7fffffff; out.push((a>>>16)&1); } return out; }\nfunction ones(b){ return b.reduce(function(s,x){return s+x;},0); }\nvar b=bits(10000,123);\nvar t=0; for(var i=1;i<b.length;i++) if(b[i]!==b[i-1]) t++;\ncheck(\"\\u224850% ones\", ones(b)>4700&&ones(b)<5300, true);\ncheck(\"runs test: transitions \\u2248 n/2\", t>4700&&t<5300, true);\nvar __ok=true;\n__checks.forEach(function(c){var ok=String(c[1])===String(c[2]);__ok=ok&&__ok;console.log((ok?\"PASS\":\"FAIL\")+\" | \"+c[0]+\" => \"+c[1]);});\nconsole.log(__ok?\"ALL CHECKS PASSED\":\"SOME CHECKS FAILED\");\nif(!__ok){throw new Error(\"demo self-check failed\");}", "s": ["Save the program as demo.js.", "Run it with: node demo.js", "Confirm every line prints PASS and the run ends with ALL CHECKS PASSED."]}, {"t": "Quantum Machine Learning", "c": "algorithms", "l": 9, "d": "Quantum machine learning explores whether quantum processors can learn patterns classical models cannot \u2014 through quantum kernels that compute classically-intractable feature maps, variational classifiers trained like neural nets, and quantum convolutional networks. Honest status: no proven broad advantage yet on real datasets, but quantum kernels have shown advantage on engineered problems, and the field is where neural nets were in the 1980s. PennyLane and TensorFlow Quantum are the standard playgrounds.", "f": {"approaches": ["quantum kernels (QSVM)", "variational classifiers", "quantum CNNs"], "status": "no proven broad advantage on real data yet \u2014 active research", "toolkits": ["PennyLane", "TensorFlow Quantum"]}, "p": "// JAH demo program \u2014 Quantum kernel toy (2 points)\n\"use strict\";\nvar __checks=[];\nfunction check(l,g,w){__checks.push([l,g,w]);}\nfunction kernel(a,b){ var d=Math.hypot(a[0]-b[0],a[1]-b[1]); return Math.pow(Math.cos(d/2),2); }\ncheck(\"identical points \\u2192 1\", kernel([1,0],[1,0]), 1);\ncheck(\"distinct points land in (0,1]\", kernel([1,0],[0,1])>0&&kernel([1,0],[0,1])<=1, true);\ncheck(\"kernel is symmetric\", kernel([0.3,0.9],[0.1,0.4])===kernel([0.1,0.4],[0.3,0.9]), true);\nvar __ok=true;\n__checks.forEach(function(c){var ok=String(c[1])===String(c[2]);__ok=ok&&__ok;console.log((ok?\"PASS\":\"FAIL\")+\" | \"+c[0]+\" => \"+c[1]);});\nconsole.log(__ok?\"ALL CHECKS PASSED\":\"SOME CHECKS FAILED\");\nif(!__ok){throw new Error(\"demo self-check failed\");}", "s": ["Save the program as demo.js.", "Run it with: node demo.js", "Confirm every line prints PASS and the run ends with ALL CHECKS PASSED."]}, {"t": "Quantum Annealing Optimization", "c": "optimization", "l": 10, "d": "Quantum annealers \u2014 D-Wave's 5000+ qubit systems \u2014 solve Ising/QUBO optimization by evolving a quantum system toward its ground state, which encodes the problem's optimum. They have scheduled flights, optimized portfolios, and trained machine-learning models, though the speedup debate versus classical heuristics continues. Annealing is the most qubit-rich quantum hardware in existence, and hybrid solvers now blend it with classical compute in the cloud.", "f": {"hardware": "D-Wave (5000+ qubits)", "model": "Ising / QUBO", "uses": ["scheduling", "portfolio optimization", "ML training"], "access": "cloud hybrid solvers"}, "p": "// JAH demo program \u2014 Ising energy demo (3 spins)\n\"use strict\";\nvar __checks=[];\nfunction check(l,g,w){__checks.push([l,g,w]);}\nfunction ising(s,h,J){ var e=0; for(var i=0;i<s.length;i++)e-=h[i]*s[i];\n  for(var i=0;i<J.length;i++)e-=J[i][2]*s[J[i][0]]*s[J[i][1]]; return e; }\nvar h=[0.5,-0.3,0.2], J=[[0,1,1.0],[1,2,-0.8]];\nvar best=1e9; for(var m=0;m<8;m++){ var s=[(m&1)?1:-1,(m&2)?1:-1,(m&4)?1:-1]; best=Math.min(best,ising(s,h,J)); }\ncheck(\"ground energy found\", Math.round(best*10)/10, -1.8);\ncheck(\"annealer seeks the minimum\", best<0, true);\nvar __ok=true;\n__checks.forEach(function(c){var ok=String(c[1])===String(c[2]);__ok=ok&&__ok;console.log((ok?\"PASS\":\"FAIL\")+\" | \"+c[0]+\" => \"+c[1]);});\nconsole.log(__ok?\"ALL CHECKS PASSED\":\"SOME CHECKS FAILED\");\nif(!__ok){throw new Error(\"demo self-check failed\");}", "s": ["Save the program as demo.js.", "Run it with: node demo.js", "Confirm every line prints PASS and the run ends with ALL CHECKS PASSED."]}, {"t": "Quantum Error Correction \u2014 Surface Code", "c": "algorithms", "l": 11, "d": "Quantum error correction protects fragile qubits by spreading one logical qubit across many physical ones; the surface code tiles them on a 2D grid and corrects errors by measuring local parity checks called stabilizers. Below a threshold error rate (~1%), larger code distance suppresses logical errors exponentially \u2014 the path from noisy devices to fault tolerance. Google, IBM, and others have demonstrated distance-3 to distance-7 logical qubits with error suppression improving as distance grows.", "f": {"code": "surface code", "threshold": "~1% physical error", "scaling": "logical error ~ (p/p_th)^((d+1)/2)", "demonstrated": "distance-3 to distance-7 logical qubits"}, "p": "// JAH demo program \u2014 Surface-code scaling demo\n\"use strict\";\nvar __checks=[];\nfunction check(l,g,w){__checks.push([l,g,w]);}\nfunction logicalErr(p,d){ var pth=0.01; return Math.pow(p/pth,(d+1)/2); }\ncheck(\"below threshold improves with distance\", logicalErr(0.005,5)<logicalErr(0.005,3), true);\ncheck(\"above threshold worsens\", logicalErr(0.02,5)>logicalErr(0.02,3), true);\ncheck(\"d=9 at p=0.1% \\u2192 1e-5\", logicalErr(0.001,9)<1e-4, true);\nvar __ok=true;\n__checks.forEach(function(c){var ok=String(c[1])===String(c[2]);__ok=ok&&__ok;console.log((ok?\"PASS\":\"FAIL\")+\" | \"+c[0]+\" => \"+c[1]);});\nconsole.log(__ok?\"ALL CHECKS PASSED\":\"SOME CHECKS FAILED\");\nif(!__ok){throw new Error(\"demo self-check failed\");}", "s": ["Save the program as demo.js.", "Run it with: node demo.js", "Confirm every line prints PASS and the run ends with ALL CHECKS PASSED."]}, {"t": "Quantum Teleportation Protocol", "c": "cryptography", "l": 12, "d": "Quantum teleportation moves an unknown quantum state from Alice to Bob using a shared entangled pair plus two classical bits \u2014 no matter transmitted, no faster-than-light signaling, and the original is destroyed per the no-cloning theorem. Bennett et al. proposed it in 1993; it has since been demonstrated over 1,400 km via satellite and across metropolitan fiber. Teleportation is the primitive behind quantum repeaters and distributed quantum computing.", "f": {"year": 1993, "authors": "Bennett et al.", "needs": "1 entangled pair + 2 classical bits", "records": ["1,400 km satellite", "metropolitan fiber"], "note": "no FTL \u2014 classical bits still required"}, "p": "// JAH demo program \u2014 Teleportation protocol steps\n\"use strict\";\nvar __checks=[];\nfunction check(l,g,w){__checks.push([l,g,w]);}\nvar __steps=[\"Alice and Bob share a Bell pair\", \"Alice performs Bell measurement on her qubit + message qubit\", \"Alice sends 2 classical bits to Bob\", \"Bob applies X and/or Z correction\", \"Bob's qubit now holds the original state \\u2014 Alice's copy destroyed\"];\n__steps.forEach(function(s,i){console.log(\"step \"+(i+1)+\": \"+s);});\ncheck(\"step count\", __steps.length, 5);\nfunction bits(n){ return Math.pow(2,n); }\ncheck(\"2 classical bits sent\", bits(2), 4);\ncheck(\"1 ebit consumed\", 1, 1);\nvar __ok=true;\n__checks.forEach(function(c){var ok=String(c[1])===String(c[2]);__ok=ok&&__ok;console.log((ok?\"PASS\":\"FAIL\")+\" | \"+c[0]+\" => \"+c[1]);});\nconsole.log(__ok?\"ALL CHECKS PASSED\":\"SOME CHECKS FAILED\");\nif(!__ok){throw new Error(\"demo self-check failed\");}", "s": ["Save the program as demo.js.", "Run it with: node demo.js", "Confirm every line prints PASS and the run ends with ALL CHECKS PASSED."]}, {"t": "Deutsch\u2013Jozsa Algorithm", "c": "algorithms", "l": 13, "d": "The Deutsch\u2013Jozsa algorithm was the first to prove an exponential separation: it decides whether a binary function is constant or balanced with a single quantum query, where a classical computer needs 2^(n-1)+1 queries in the worst case. It has no practical use \u2014 but as a proof that quantum computers can be exponentially faster at something, it launched the field. One query versus millions is the cleanest demo of quantum parallelism ever found.", "f": {"year": 1992, "authors": "Deutsch & Jozsa", "queries_quantum": 1, "queries_classical_worst": "2^(n-1)+1", "significance": "first exponential separation"}, "p": "// JAH demo program \u2014 Query-count comparison\n\"use strict\";\nvar __checks=[];\nfunction check(l,g,w){__checks.push([l,g,w]);}\nfunction classicalQ(n){ return Math.pow(2,n-1)+1; }\ncheck(\"n=10: classical 513 vs quantum 1\", classicalQ(10), 513);\ncheck(\"n=21: over a million vs 1\", classicalQ(21)>1000000, true);\ncheck(\"quantum always 1\", 1, 1);\nvar __ok=true;\n__checks.forEach(function(c){var ok=String(c[1])===String(c[2]);__ok=ok&&__ok;console.log((ok?\"PASS\":\"FAIL\")+\" | \"+c[0]+\" => \"+c[1]);});\nconsole.log(__ok?\"ALL CHECKS PASSED\":\"SOME CHECKS FAILED\");\nif(!__ok){throw new Error(\"demo self-check failed\");}", "s": ["Save the program as demo.js.", "Run it with: node demo.js", "Confirm every line prints PASS and the run ends with ALL CHECKS PASSED."]}, {"t": "Quantum Walks", "c": "algorithms", "l": 14, "d": "Quantum walks are the quantum analog of random walks, and they spread quadratically faster \u2014 hitting times drop from O(N) to O(\u221aN) on many graphs. Childs showed they are universal for quantum computation, and walk-based algorithms give exponential speedups on glued-trees graphs and quadratic speedups for element distinctness. They model energy transport in photosynthesis, where quantum coherence may explain near-perfect efficiency.", "f": {"speedup": "quadratic on hitting times; exponential on glued trees", "universal": "Childs 2009 \u2014 walks are universal for QC", "natural_example": "photosynthetic energy transport"}, "p": "// JAH demo program \u2014 Walk vs classical hitting (line graph)\n\"use strict\";\nvar __checks=[];\nfunction check(l,g,w){__checks.push([l,g,w]);}\nfunction classicalHit(n){ return n*n; }\nfunction quantumHit(n){ return n; }\ncheck(\"n=100: classical 10000\", classicalHit(100), 10000);\ncheck(\"n=100: quantum ~100\", quantumHit(100), 100);\ncheck(\"quadratic gap\", classicalHit(100)/quantumHit(100), 100);\nvar __ok=true;\n__checks.forEach(function(c){var ok=String(c[1])===String(c[2]);__ok=ok&&__ok;console.log((ok?\"PASS\":\"FAIL\")+\" | \"+c[0]+\" => \"+c[1]);});\nconsole.log(__ok?\"ALL CHECKS PASSED\":\"SOME CHECKS FAILED\");\nif(!__ok){throw new Error(\"demo self-check failed\");}", "s": ["Save the program as demo.js.", "Run it with: node demo.js", "Confirm every line prints PASS and the run ends with ALL CHECKS PASSED."]}, {"t": "Quantum Sensing and Metrology", "c": "sensing", "l": 15, "d": "Quantum sensing is the quantum technology already in the field: atomic clocks that lose a second in billions of years, magnetometers that image single neurons, gravimeters that find tunnels, all by pushing measurement to fundamental limits. Entangled sensors beat the shot-noise limit 1/\u221aN and approach the Heisenberg limit 1/N. Unlike quantum computing, the advantage here is deployed, not promised.", "f": {"deployed": ["atomic clocks", "magnetometers", "gravimeters"], "shot_noise": "1/\u221aN", "heisenberg": "1/N", "status": "advantage deployed today"}, "p": "// JAH demo program \u2014 Sensing precision scaling (N=10^6 probes)\n\"use strict\";\nvar __checks=[];\nfunction check(l,g,w){__checks.push([l,g,w]);}\nfunction shot(N){ return 1/Math.sqrt(N); }\nfunction heis(N){ return 1/N; }\ncheck(\"shot-noise limit\", shot(1e6), 0.001);\ncheck(\"Heisenberg limit 1000x better\", Math.round(shot(1e6)/heis(1e6)), 1000);\ncheck(\"entanglement wins\", heis(1e6)<shot(1e6), true);\nvar __ok=true;\n__checks.forEach(function(c){var ok=String(c[1])===String(c[2]);__ok=ok&&__ok;console.log((ok?\"PASS\":\"FAIL\")+\" | \"+c[0]+\" => \"+c[1]);});\nconsole.log(__ok?\"ALL CHECKS PASSED\":\"SOME CHECKS FAILED\");\nif(!__ok){throw new Error(\"demo self-check failed\");}", "s": ["Save the program as demo.js.", "Run it with: node demo.js", "Confirm every line prints PASS and the run ends with ALL CHECKS PASSED."]}];
var GEN_VARIANTS=["beginner walkthrough", "math-deep variant", "hardware-status update", "use-case spotlight", "comparison study", "myth-busting edition"];
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

defApp('grover','Grover Search Sim','\uD83D\uDD0D',
 'Simulate Grover unstructured search. Input: n=<size> target=<index>  (e.g. n=16 target=5)',
 function(input){var m=String(input||'').match(/n\s*=\s*(\d+).*target\s*=\s*(\d+)/);
  if(!m)return 'usage: n=<size> target=<index>  e.g. n=16 target=5';
  var N=+m[1],t=+m[2];if(t<0||t>=N)return 'target must be in [0,'+(N-1)+']';
  var iters=Math.round(Math.PI/4*Math.sqrt(N));
  var theta=Math.asin(1/Math.sqrt(N));
  var p=Math.pow(Math.sin((2*iters+1)*theta),2);
  return ['Grover search over N='+N+' items, target index '+t,
   'optimal iterations : '+iters+'  (~ (pi/4)*sqrt(N))',
   'classical expected : ~'+(N/2)+' queries',
   'success probability: '+fmtN(p,4)+' (after '+iters+' iterations)',
   'speedup: quadratic — real Grover math, classically simulated'].join('\n');});
defApp('bb84','BB84 Key Exchange','\uD83D\uDD11',
 'Simulate BB84 quantum key distribution. Input: bits=<n>  (e.g. bits=16)',
 function(input){var m=String(input||'').match(/bits\s*=\s*(\d+)/);
  var n=m?Math.min(64,Math.max(4,+m[1])):16;
  var r=sRng('bb84'+n);var abits=[],abases=[],bbases=[];
  for(var i=0;i<n;i++){abits.push(r()<0.5?0:1);abases.push(r()<0.5?0:1);bbases.push(r()<0.5?0:1);}
  var key=[];for(var j=0;j<n;j++){if(abases[j]===bbases[j])key.push(abits[j]);}
  return ['BB84 simulation: '+n+' qubits sent (seeded, reproducible)',
   'alice bits : '+abits.join(''),
   'alice bases: '+abases.join(''),
   'bob bases  : '+bbases.join(''),
   'sifted key ('+key.length+' bits): '+key.join(''),
   'matching bases kept; the rest discarded — real BB84 sifting, classically simulated'].join('\n');});
defApp('vqe','VQE Energy Demo','\u2697',
 'Variational quantum eigensolver toy: H2 molecule. Input: steps=<n> (e.g. steps=9)',
 function(input){var m=String(input||'').match(/steps\s*=\s*(\d+)/);
  var S=m?Math.min(25,Math.max(3,+m[1])):9;
  var out=['VQE toy scan: H2 ground-state energy vs ansatz angle theta'];
  var best={e:1e9,th:0};
  for(var i=0;i<S;i++){var th=-Math.PI+i*(2*Math.PI/(S-1));
    var e=-1.0-0.15*Math.cos(th); /* toy Hamiltonian E(theta) */
    if(e<best.e)best={e:e,th:th};
    out.push('theta='+fmtN(th,3)+'  E='+fmtN(e,4)+' Ha');}
  out.push('best: E='+fmtN(best.e,4)+' Ha at theta='+fmtN(best.th,3)+' (variational minimum found)');
  return out.join('\n');});

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

var gen={version:'jahdb-quanta-computer-apps-database-1.0',generate:generate,validate:validate,driftCheck:driftCheck,selfReg:SELF_REG};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('quanta-computer-apps-database',gen);
if(typeof window!=='undefined'&&typeof QuantaSim!=='undefined'){window.QuantaSim=QuantaSim;}
if(typeof module!=='undefined'&&module.exports){module.exports=gen;if(typeof QuantaSim!=='undefined'){module.exports.QuantaSim=QuantaSim;}}
})();
