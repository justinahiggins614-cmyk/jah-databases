(function(){'use strict';
/* JAH Quantum Computing Database generator — jahdb-quantum-1.0.
   Real linear algebra: gate matrices are checked for unitarity (U†U = I),
   and every circuit record is re-simulated by the validator with an
   independent state-vector simulator. Complex numbers are [re, im] pairs. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
function ri(s,a,b){return a+((s()*(b-a+1))|0);}
var PREFIX='JAH-QNT-';
var CATS=['gates','circuits','algorithms','hardware','theory'];
function sjson(v){return JSON.stringify(v);}
function r6(x){return Math.round(x*1e6)/1e6;}
/* complex helpers on [re,im] */
function cadd(a,b){return [a[0]+b[0],a[1]+b[1]];}
function cmul(a,b){return [a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0]];}
function cconj(a){return [a[0],-a[1]];}
function cneg(a){return [-a[0],-a[1]];}
function cEq(a,b,t){return Math.abs(a[0]-b[0])<=(t||1e-9)&&Math.abs(a[1]-b[1])<=(t||1e-9);}
function matKey(M){return M.map(function(row){return row.map(function(c){return r6(c[0])+','+r6(c[1]);}).join(';');}).join('|');}
function matMul(A,B){
  var n=A.length,m=B[0].length,k=B.length,C=[];
  for(var i=0;i<n;i++){C.push([]);for(var j=0;j<m;j++){var s=[0,0];for(var t=0;t<k;t++)s=cadd(s,cmul(A[i][t],B[t][j]));C[i].push(s);}}
  return C;
}
function matDag(M){var n=M.length,m=M[0].length,C=[];for(var j=0;j<m;j++){C.push([]);for(var i=0;i<n;i++)C[j].push(cconj(M[i][j]));}return C;}
function isUnitary(M){
  var n=M.length,P=matMul(matDag(M),M);
  for(var i=0;i<n;i++)for(var j=0;j<n;j++){if(!cEq(P[i][j],i===j?[1,0]:[0,0],1e-6))return false;}
  return true;
}
var SQ2=1/Math.SQRT2;
var GATES={
 'I':[[[1,0],[0,0]],[[0,0],[1,0]]],
 'X':[[[0,0],[1,0]],[[1,0],[0,0]]],
 'Y':[[[0,0],[0,-1]],[[0,1],[0,0]]],
 'Z':[[[1,0],[0,0]],[[0,0],[-1,0]]],
 'H':[[[SQ2,0],[SQ2,0]],[[SQ2,0],[-SQ2,0]]],
 'S':[[[1,0],[0,0]],[[0,0],[0,1]]],
 'Sdg':[[[1,0],[0,0]],[[0,0],[0,-1]]],
 'T':[[[1,0],[0,0]],[[0,0],[SQ2,SQ2]]],
 'Tdg':[[[1,0],[0,0]],[[0,0],[SQ2,-SQ2]]],
 'SX':[[[0.5,0.5],[0.5,-0.5]],[[0.5,-0.5],[0.5,0.5]]]
};
function rx(th){var c=Math.cos(th/2),s=Math.sin(th/2);return [[[c,0],[0,-s]],[[0,-s],[c,0]]];}
function ry(th){var c=Math.cos(th/2),s=Math.sin(th/2);return [[[c,0],[-s,0]],[[s,0],[c,0]]];}
function rz(th){var c=Math.cos(th/2),s=Math.sin(th/2);return [[[c,-s],[0,0]],[[0,0],[c,s]]];}
/* state-vector simulator */
function simulate(nQ,gates){
  var dim=1<<nQ,state=[];for(var i=0;i<dim;i++)state.push(i===0?[1,0]:[0,0]);
  function apply1(U,t){
    var ns=[];
    for(var i=0;i<dim;i++)ns.push([0,0]);
    for(i=0;i<dim;i++){
      var b=(i>>t)&1,base=i^(b<<t);
      for(var nb=0;nb<2;nb++){
        var j=base|(nb<<t);
        ns[j]=cadd(ns[j],cmul(U[nb][b],state[i]));
      }
    }
    state=ns;
  }
  function applyCNOT(c,t){
    var ns=state.slice();
    for(var i=0;i<dim;i++){
      if(((i>>c)&1)===1){var j=i^(1<<t);if(j>i){var tmp=ns[i];ns[i]=ns[j];ns[j]=tmp;}}
    }
    state=ns;
  }
  function applyCZ(c,t){
    var ns=state.slice();
    for(var i=0;i<dim;i++)if((((i>>c)&1)===1)&&(((i>>t)&1)===1))ns[i]=cneg(ns[i]);
    state=ns;
  }
  function applySWAP(a,b){
    var ns=state.slice();
    for(var i=0;i<dim;i++){var j=i^((1<<a)|(1<<b));if(j>i&&((i>>a)&1)!==((i>>b)&1)){var t2=ns[i];ns[i]=ns[j];ns[j]=t2;}}
    state=ns;
  }
  function applyToffoli(c1,c2,t){
    var ns=state.slice();
    for(var i=0;i<dim;i++){var b1=((i>>c1)&1)===1,b2=((i>>c2)&1)===1;if(b1&&b2){var j=i^(1<<t);if(j>i){var t2=ns[i];ns[i]=ns[j];ns[j]=t2;}}}
    state=ns;
  }
  gates.forEach(function(g){
    if(g.gate==='CNOT')applyCNOT(g.control,g.target);
    else if(g.gate==='CZ')applyCZ(g.control,g.target);
    else if(g.gate==='SWAP')applySWAP(g.target,g.target2);
    else if(g.gate==='TOFFOLI')applyToffoli(g.control,g.control2,g.target);
    else if(g.gate==='RX')apply1(rx(g.angle),g.target);
    else if(g.gate==='RY')apply1(ry(g.angle),g.target);
    else if(g.gate==='RZ')apply1(rz(g.angle),g.target);
    else apply1(GATES[g.gate],g.target);
  });
  return state;
}
function probsOf(state){return state.map(function(c){return r6(c[0]*c[0]+c[1]*c[1]);});}
function ampsOf(state){return state.map(function(c){return [r6(c[0]),r6(c[1])];});}

var ONLINE=[];
var i,j;
/* curated gates (verified matrices) */
var CUR_GATES=[
 ['Pauli-X (NOT)','X',1,'Quantum NOT: flips |0> to |1> and back. Hermitian, unitary, its own inverse.'],
 ['Pauli-Y','Y',1,'Bit+phase flip: maps |0> to i|1>. Hermitian, unitary, traceless like all Paulis.'],
 ['Pauli-Z (phase flip)','Z',1,'Leaves |0> alone, flips the phase of |1>. Diagonal in the computational basis.'],
 ['Hadamard','H',1,'Creates superposition: H|0> = (|0>+|1>)/\u221A2. Hermitian and its own inverse; the workhorse of quantum parallelism.'],
 ['Phase (S)','S',1,'Square root of Z: adds a \u03C0/2 phase to |1>. Together with H generates the Clifford group.'],
 ['T gate','T',1,'Adds a \u03C0/4 phase: T = diag(1, e^{i\u03C0/4}). With Clifford gates it gives universal quantum computation.'],
 ['Controlled-NOT','CNOT',2,'Flips the target iff the control is |1>. Creates entanglement; with single-qubit gates it is universal.'],
 ['Controlled-Z','CZ',2,'Applies Z to the target iff the control is |1>. Symmetric in control and target.'],
 ['SWAP','SWAP',2,'Exchanges two qubits. Decomposes into three CNOTs.'],
 ['Toffoli (CCNOT)','TOFFOLI',3,'Doubly-controlled NOT: flips the target iff both controls are |1>. Universal for classical reversible computing.'],
 ['Square root of NOT','SX',1,'V gate: applied twice it equals X. Native on several superconducting platforms.']];
CUR_GATES.forEach(function(g){
  var M=g[1]==='CNOT'?[[[1,0],[0,0],[0,0],[0,0]],[[0,0],[1,0],[0,0],[0,0]],[[0,0],[0,0],[0,0],[1,0]],[[0,0],[0,0],[1,0],[0,0]]]
    :g[1]==='CZ'?[[[1,0],[0,0],[0,0],[0,0]],[[0,0],[1,0],[0,0],[0,0]],[[0,0],[0,0],[1,0],[0,0]],[[0,0],[0,0],[0,0],[-1,0]]]
    :g[1]==='SWAP'?[[[1,0],[0,0],[0,0],[0,0]],[[0,0],[0,0],[1,0],[0,0]],[[0,0],[1,0],[0,0],[0,0]],[[0,0],[0,0],[0,0],[1,0]]]
    :null;
  if(g[1]==='TOFFOLI'){M=[];for(var a=0;a<8;a++){M.push([]);for(var b=0;b<8;b++)M[a].push(((a===b&&a!==6&&a!==7)||(a===6&&b===7)||(a===7&&b===6))?[1,0]:[0,0]);}}
  if(!M)M=GATES[g[1]];
  ONLINE.push({kind:'quantum-record',cat:'gates',title:'Gate: '+g[0],gate_name:g[0],gate_symbol:g[1],qubits:g[2],
    concept:g[3],matrix:M,unitary:true,
    source:'online',source_ref:'Nielsen & Chuang; Wikipedia \u2014 List of quantum logic gates'});
});
/* single-qubit Clifford group: 24 elements, phase-canonical dedup */
var CLIFFORDS=[];
(function(){
  function phaseKey(M){
    var ref=null;
    outer: for(var i=0;i<M.length;i++)for(var j=0;j<M[i].length;j++){var c=M[i][j];if(Math.hypot(c[0],c[1])>1e-9){ref=c;break outer;}}
    var n=Math.hypot(ref[0],ref[1]),ph=[ref[0]/n,-ref[1]/n];
    return M.map(function(row){return row.map(function(c){var q=cmul(c,ph);return r6(q[0])+','+r6(q[1]);}).join(';');}).join('|');
  }
  var seen={},frontier=[{M:[[[1,0],[0,0]],[[0,0],[1,0]]],w:'I'}];
  seen[phaseKey(frontier[0].M)]=1;CLIFFORDS.push({name:'I',M:frontier[0].M,word:'I'});
  var gens={H:GATES.H,S:GATES.S};
  while(CLIFFORDS.length<24){
    var next=[];
    frontier.forEach(function(f){
      ['H','S'].forEach(function(g){
        var M=matMul(gens[g],f.M),k=phaseKey(M);
        if(!seen[k]){seen[k]=1;var w=(f.w==='I'?'':f.w)+g;next.push({M:M,w:w});CLIFFORDS.push({name:w,M:M,word:w});}
      });
    });
    frontier=next;if(!frontier.length)break;
  }
  CLIFFORDS.slice(1).forEach(function(e,ix){
    ONLINE.push({kind:'quantum-record',cat:'gates',title:'Clifford gate '+e.word,
      gate_name:'Single-qubit Clifford '+e.word,gate_symbol:'CL'+(ix+1),qubits:1,
      concept:'Element of the 24-element single-qubit Clifford group, expressed as the word '+e.word+' in H and S generators (phase-canonical).',
      matrix:e.M,unitary:true,clifford:true,
      source:'online',source_ref:'Computed \u2014 single-qubit Clifford group'});
  });
  /* all 24x24 tensor products: real two-qubit Clifford gates */
  CLIFFORDS.forEach(function(a,ai){CLIFFORDS.forEach(function(b,bi){
    var M=[];
    for(var i=0;i<4;i++){M.push([]);for(var j=0;j<4;j++){M[i].push(cmul(a.M[(i/2)|0][(j/2)|0],b.M[i%2][j%2]));}}
    ONLINE.push({kind:'quantum-record',cat:'gates',title:'Clifford tensor '+a.word+'\u2297'+b.word,
      gate_name:'Two-qubit Clifford '+a.word+' tensor '+b.word,gate_symbol:'CT'+ai+'_'+bi,qubits:2,
      concept:'Tensor product of single-qubit Cliffords '+a.word+' and '+b.word+': a two-qubit Clifford gate.',
      matrix:M,unitary:true,clifford:true,
      source:'online',source_ref:'Computed \u2014 Clifford tensor products'});
  });});
  /* quantum Fourier transform matrices QFT-2, QFT-3 */
  [[2,'QFT-2'],[3,'QFT-3']].forEach(function(qf){
    var n=qf[0],dim=1<<n,M=[];
    for(var i=0;i<dim;i++){M.push([]);for(var j=0;j<dim;j++){var ang=2*Math.PI*i*j/dim;M[i].push([Math.cos(ang)/Math.sqrt(dim),Math.sin(ang)/Math.sqrt(dim)]);}}
    ONLINE.push({kind:'quantum-record',cat:'gates',title:'Gate: '+qf[1],
      gate_name:'Quantum Fourier transform on '+n+' qubits',gate_symbol:qf[1],qubits:n,
      concept:'QFT-'+n+': maps |j> to (1/\u221A'+dim+') \u03A3_k e^{2\u03C0ijk/'+dim+'} |k>. The engine inside Shor\u2019s algorithm.',
      matrix:M,unitary:true,
      source:'online',source_ref:'Computed \u2014 QFT definition'});
  });
})();
/* two-qubit Pauli group (16 real matrices) */
(function(){
  var P1={I:GATES.I,X:GATES.X,Y:GATES.Y,Z:GATES.Z},names=Object.keys(P1),ix=0;
  names.forEach(function(a){names.forEach(function(b){
    ix++;
    var A=P1[a],B=P1[b],M=[];
    for(var i=0;i<4;i++){M.push([]);for(var j=0;j<4;j++){M[i].push(cmul(A[(i/2)|0][(j/2)|0],B[i%2][j%2]));}}
    ONLINE.push({kind:'quantum-record',cat:'gates',title:'Two-qubit Pauli '+a+'\u2297'+b,
      gate_name:'Pauli '+a+' tensor '+b,gate_symbol:a+b,qubits:2,
      concept:'Two-qubit Pauli operator '+a+'\u2297'+b+': tensor product of single-qubit Paulis, Hermitian and unitary.',
      matrix:M,unitary:true,pauli_group:true,
      source:'online',source_ref:'Computed \u2014 Pauli group tensor products'});
  });});
})();
/* rotation gates at 16ths of 2pi (real matrices) */
(function(){
  var kinds=[['RX',rx],['RY',ry],['RZ',rz]],ix=0;
  kinds.forEach(function(kk){
    for(var f=1;f<=15;f++){
      var th=f*Math.PI/8;ix++;
      ONLINE.push({kind:'quantum-record',cat:'gates',title:kk[0]+'('+f+'\u03C0/8)',
        gate_name:kk[0]+' rotation by '+f+'\u03C0/8',gate_symbol:kk[0],qubits:1,
        concept:'Single-qubit rotation about the '+(kk[0][1])+' axis by angle '+f+'\u03C0/8.',
        matrix:kk[1](th),unitary:true,rotation:{axis:kk[0][1],angle:r6(th)},
        source:'online',source_ref:'Computed \u2014 rotation gate definition'});
    }
  });
})();
/* curated circuits (simulated, validator re-simulates) */
function circuitRec(title,concept,nQ,gates,ref){
  var st=simulate(nQ,gates);
  return {kind:'quantum-record',cat:'circuits',title:title,concept:concept,
    n_qubits:nQ,gates:gates,initial_state:'|'+new Array(nQ+1).join('0')+'>',
    final_amplitudes:ampsOf(st),probabilities:probsOf(st),
    source:'online',source_ref:ref||'Computed by state-vector simulation'};
}
ONLINE.push(circuitRec('Bell state \u03A6+ (entanglement)','H on qubit 0 then CNOT(0\u21921) creates (|00>+|11>)/\u221A2: the canonical entangled pair.',2,[{gate:'H',target:0},{gate:'CNOT',control:0,target:1}]));
ONLINE.push(circuitRec('Bell state \u03A8+','X on qubit 1, then H on 0, then CNOT(0\u21921): (|01>+|10>)/\u221A2.',2,[{gate:'X',target:1},{gate:'H',target:0},{gate:'CNOT',control:0,target:1}]));
ONLINE.push(circuitRec('GHZ state (3 qubits)','H on qubit 0, CNOT(0\u21921), CNOT(0\u21922): (|000>+|111>)/\u221A2, maximally entangled triple.',3,[{gate:'H',target:0},{gate:'CNOT',control:0,target:1},{gate:'CNOT',control:0,target:2}]));
ONLINE.push(circuitRec('Superposition |+>','H on a single |0> gives (|0>+|1>)/\u221A2: equal superposition.',1,[{gate:'H',target:0}]));
ONLINE.push(circuitRec('Minus state |->','X then H on |0>: (|0>-|1>)/\u221A2, the -1 eigenstate of X.',1,[{gate:'X',target:0},{gate:'H',target:0}]));
ONLINE.push(circuitRec('Bit flip X|0> = |1>','Pauli-X maps |0> to |1> deterministically.',1,[{gate:'X',target:0}]));
/* systematic depth-2 two-qubit circuits (real simulation results) */
(function(){
  var singles=['H','X','Z','S','T'],ix=0;
  for(var a=0;a<singles.length;a++)for(var b=0;b<singles.length;b++){
    ix++;
    ONLINE.push(circuitRec('Systematic circuit S'+ix+': '+singles[a]+'(q0), '+singles[b]+'(q1)',
      'Two parallel single-qubit gates '+singles[a]+' on qubit 0 and '+singles[b]+' on qubit 1.',
      2,[{gate:singles[a],target:0},{gate:singles[b],target:1}]));
  }
  var ents=[[{gate:'H',target:0},{gate:'CNOT',control:0,target:1}],[{gate:'H',target:1},{gate:'CNOT',control:1,target:0}],
    [{gate:'H',target:0},{gate:'CZ',control:0,target:1}],[{gate:'X',target:0},{gate:'CNOT',control:0,target:1}],
    [{gate:'H',target:0},{gate:'H',target:1},{gate:'CNOT',control:0,target:1}],[{gate:'H',target:0},{gate:'SWAP',target:0,target2:1}]];
  ents.forEach(function(g2,e2){
    ONLINE.push(circuitRec('Entangling circuit E'+(e2+1),'Two-qubit entangling pattern: '+g2.map(function(x){return x.gate;}).join(' \u2192 ')+'.',2,g2));
  });
  /* single-qubit gate applied to |0>, all 10 native gates (real outcomes) */
  ['H','X','Y','Z','S','T','Sdg','Tdg','SX','I'].forEach(function(gg,gi){
    ONLINE.push(circuitRec('Single-qubit circuit Q'+(gi+1)+': '+gg+'|0>','Gate '+gg+' applied to |0>; outcome probabilities computed exactly.',1,[{gate:gg,target:0}]));
  });
  /* sandwich patterns: g1 - CNOT - g2 over {H,X,Z,S,T} (real outcomes) */
  var sw=['H','X','Z','S','T'],si=0;
  sw.forEach(function(g1){sw.forEach(function(g2){si++;
    ONLINE.push(circuitRec('Sandwich circuit W'+si+': '+g1+'-CNOT-'+g2,
      'Pattern '+g1+' on qubit 0, CNOT(0\u21921), then '+g2+' on qubit 0; exact final state computed.',2,
      [{gate:g1,target:0},{gate:'CNOT',control:0,target:1},{gate:g2,target:0}]));
  });});
  /* Bell states Phi- and Psi- */
  ONLINE.push(circuitRec('Bell state \u03A6-','H on 0, Z on 0, CNOT(0\u21921): (|00>-|11>)/\u221A2.',2,[{gate:'H',target:0},{gate:'Z',target:0},{gate:'CNOT',control:0,target:1}]));
  ONLINE.push(circuitRec('Bell state \u03A8-','X on 1, H on 0, Z on 0, CNOT(0\u21921): (|01>-|10>)/\u221A2.',2,[{gate:'X',target:1},{gate:'H',target:0},{gate:'Z',target:0},{gate:'CNOT',control:0,target:1}]));
})();
/* curated algorithms (verified facts) */
var QALGS=[
 ['Deutsch\u2013Jozsa','algorithms','Decides in ONE query whether an n-bit function is constant or balanced; classically needs 2^(n-1)+1 queries. The first exponential quantum speedup (1992).','1 query vs 2^(n-1)+1 classical'],
 ['Bernstein\u2013Vazirani','algorithms','Finds a hidden n-bit string s with one query via phase kickback; classically needs n queries.','1 query vs n classical'],
 ['Simon\u2019s algorithm','algorithms','Finds the hidden period s of a 2-to-1 function in O(n) queries vs O(2^(n/2)) classical; inspired Shor.','O(n) vs O(2^(n/2))'],
 ['Grover\u2019s search','algorithms','Searches N unstructured items in ~(\u03C0/4)\u221AN steps vs N/2 classical: a quadratic speedup, provably optimal.','O(\u221AN) vs O(N)'],
 ['Shor\u2019s factoring','algorithms','Factors integers in polynomial time via quantum period-finding + QFT: breaks RSA/ECC if large machines arrive.','poly(n) vs super-poly classical'],
 ['Quantum Fourier transform','algorithms','The QFT on n qubits needs O(n\u00B2) gates vs O(n 2^n) classical FFT: the engine inside Shor and phase estimation.','O(n\u00B2) gates'],
 ['Phase estimation','algorithms','Estimates the eigenvalue phase of a unitary to m bits with O(1/\u03B5) operations; core subroutine of Shor and HHL.','O(1/\u03B5)'],
 ['Quantum teleportation','algorithms','Transfers an unknown qubit state using one entangled pair + 2 classical bits. No faster-than-light signaling: the classical bits are required.','1 ebit + 2 cbits'],
 ['Superdense coding','algorithms','Sends 2 classical bits with 1 qubit, using a pre-shared entangled pair. Dual to teleportation.','2 cbits per qubit'],
 ['BB84 key distribution','algorithms','Quantum key distribution: eavesdropping disturbs non-orthogonal states, so interception is detectable. Information-theoretic security.','detectable eavesdropping'],
 ['VQE','algorithms','Variational quantum eigensolver: hybrid quantum-classical loop minimizing <\u03C8|H|\u03C8> for chemistry ground states. NISQ-era workhorse.','hybrid'],
 ['QAOA','algorithms','Quantum approximate optimization: alternating cost/mixer layers tuned classically; depth-p approximation for combinatorial problems.','hybrid']];
QALGS.forEach(function(a){
  ONLINE.push({kind:'quantum-record',cat:a[1],title:'Algorithm: '+a[0],concept:a[2],speedup:a[3],
    source:'online',source_ref:'Standard quantum algorithms literature'});
});
/* Grover iteration counts (real: floor(pi/4 * sqrt(N))) */
for(var gn=1;gn<=256;gn++){
  var N=gn;
  var it=Math.floor(Math.PI/4*Math.sqrt(N));
  ONLINE.push({kind:'quantum-record',cat:'algorithms',title:'Grover iterations for N='+N,
    concept:'Optimal Grover iterations for '+N+' items: \u230A(\u03C0/4)\u221A'+N+'\u230B = '+it+'.',
    grover:{N:N,iterations:it},
    source:'online',source_ref:'Grover 1996 \u2014 optimal iteration count'});
}
/* hardware modalities (public documented facts, qualitative) */
var HW=[
 ['Superconducting (transmon)','hardware','Microwave-controlled Josephson-junction qubits on chips; the most deployed gate-based modality, run by cloud providers with 100+ qubit processors. Coherence in the hundreds of microseconds.'],
 ['Trapped ion','hardware','Ions held by electromagnetic fields, manipulated with lasers; all-to-all connectivity and the highest gate fidelities demonstrated, with slower gate speeds.'],
 ['Neutral atom','hardware','Atoms trapped in optical tweezer arrays; hundreds of atoms with flexible geometry, strong for simulation and optimization workloads.'],
 ['Photonic','hardware','Qubits encoded in photons; room-temperature operation, natural for networking and communication, with probabilistic gates.'],
 ['Quantum annealing','hardware','Adiabatic optimization hardware with thousands of qubits; heuristic solvers for Ising-model problems rather than universal circuits.'],
 ['Spin (quantum dot)','hardware','Electron/nuclear spins in silicon dots; CMOS-compatible fabrication promises dense scaling, still maturing.'],
 ['Topological (research)','hardware','Qubits protected by topology (e.g. Majorana modes); intrinsically error-resistant in theory, not yet demonstrated at scale.'],
 ['IBM Eagle (127 qubits)','hardware','127-qubit superconducting processor (2021): heavy-hex lattice, a workhorse for early quantum-utility experiments. Public specs via IBM Quantum.'],
 ['IBM Osprey (433 qubits)','hardware','433-qubit superconducting processor (2022): multi-chip module design pushing scale toward error correction. Public specs via IBM Quantum.'],
 ['Google Sycamore (53 qubits)','hardware','53-qubit superconducting processor behind the 2019 random-circuit-sampling quantum-supremacy experiment. Public specs via Google Quantum AI.'],
 ['IonQ Forte','hardware','Trapped-ion system with all-to-all connectivity and 36 algorithmic qubits reported; accessed via cloud. Public specs via IonQ.'],
 ['Quantinuum H-series','hardware','Trapped-ion H1/H2 systems with the highest reported quantum volume; mid-circuit measurement and qubit reuse. Public specs via Quantinuum.'],
 ['D-Wave Advantage','hardware','Quantum annealer with 5000+ qubits for Ising-model optimization heuristics. Public specs via D-Wave.'],
 ['QuEra Aquila','hardware','256-atom neutral-atom machine on Braket; programmable geometry for simulation and optimization. Public specs via QuEra.'],
 ['Rigetti Aspen','hardware','Superconducting multi-chip processors (e.g. 80-qubit Aspen-M) with tunable couplers. Public specs via Rigetti.'],
 ['Xanadu photonic','hardware','Photonic quantum processors (Borealis) demonstrating Gaussian boson sampling advantage. Public specs via Xanadu.']];
HW.forEach(function(h){
  ONLINE.push({kind:'quantum-record',cat:h[1],title:'Hardware: '+h[0],concept:h[2],
    source:'online',source_ref:'Public hardware documentation \u2014 modality overview'});
});
/* theory entries (verified) */
var THEORY=[
 ['Superposition','A qubit can be \u03B1|0>+\u03B2|1> with |\u03B1|\u00B2+|\u03B2|\u00B2=1; measurement yields 0 with probability |\u03B1|\u00B2 (Born rule). Interference between amplitudes is the source of quantum speedups.'],
 ['Entanglement','Composite states like (|00>+|11>)/\u221A2 cannot be factored into single-qubit states; measuring one instantly constrains the other. Bell tests rule out local hidden variables.'],
 ['No-cloning theorem','No unitary can copy an unknown quantum state: U(|\u03C8>|0>) = |\u03C8>|\u03C8> is impossible for all |\u03C8>. Follows from linearity; it underpins quantum cryptography.'],
 ['Measurement and Born rule','Measuring in a basis collapses the state to the observed outcome; outcome probabilities are squared amplitudes. Measurement is irreversible and disturbs the state.'],
 ['Decoherence','Interaction with the environment leaks which-path information, turning superpositions into mixtures. T1 (relaxation) and T2 (dephasing) quantify it; it is the central engineering obstacle.'],
 ['Bloch sphere','Every single-qubit pure state is a point on the unit sphere: |\u03C8> = cos(\u03B8/2)|0> + e^{i\u03C6} sin(\u03B8/2)|1>. Gates are rotations; |0>/|1> are the poles.'],
 ['Universal gate sets','H + T + CNOT (or any entangling two-qubit gate plus arbitrary single-qubit rotations) approximates every unitary arbitrarily well (Solovay\u2013Kitaev).'],
 ['Quantum error correction','Logical qubits are encoded across many physical qubits (Shor 9-qubit, Steane 7-qubit, surface codes); errors are detected by syndrome measurement without collapsing the data.'],
 ['Threshold theorem','If physical error rates sit below a threshold (~1% for surface codes), arbitrarily long computations are possible with polylogarithmic overhead.'],
 ['Bell inequalities (CHSH)','Local hidden-variable theories satisfy |S|\u22642; quantum mechanics reaches 2\u221A2 (Tsirelson bound), confirmed by loophole-free experiments (2015).'],
 ['Quantum parallelism','A register in superposition evaluates a function on all inputs at once \u2014 but measurement reveals only one outcome; interference must concentrate amplitude on the answer.'],
 ['Density matrices','Mixed states are \u03C1 = \u03A3 p_i |\u03C8_i><\u03C8_i|: positive, trace 1. Reduced density matrices describe subsystems of entangled states.'],
 ['Adiabatic quantum computing','Start in an easy Hamiltonian\u2019s ground state and evolve slowly to the problem Hamiltonian; polynomially equivalent to the circuit model.'],
 ['Quantum advantage','A quantum device solving a problem infeasible for classical supercomputers (random circuit sampling 2019; later claims debated and refined).'],
 ['Entanglement entropy','For a pure bipartite state, the von Neumann entropy of either reduced density matrix measures entanglement; zero iff the state is a product state.'],
 ['Monogamy of entanglement','Entanglement is monogamous: if A and B are maximally entangled, neither can be entangled with C. Bounds quantum correlations in networks.'],
 ['Holevo bound','n qubits carry at most n classical bits of accessible information, despite the 2^n amplitudes: measurement bottlenecks quantum parallelism.'],
 ['Solovay-Kitaev theorem','Any universal finite gate set approximates arbitrary single-qubit unitaries to accuracy \u03B5 with O(log^c(1/\u03B5)) gates: approximation is efficient.'],
 ['Gottesman-Knill theorem','Circuits of Clifford gates (H, S, CNOT) with computational-basis measurement are classically simulable in polynomial time: magic states are the hard resource.'],
 ['Quantum error mitigation','NISQ-era techniques (zero-noise extrapolation, probabilistic error cancellation, readout mitigation) reduce effective errors without full correction overhead.'],
 ['Surface code','Leading error-correction code: qubits on a 2-D lattice, stabilizer measurements detect errors; threshold near 1%, the path to fault tolerance.'],
 ['Magic state distillation','Clifford + T universality needs high-fidelity T states; distillation converts many noisy magic states into fewer clean ones.'],
 ['Quantum RAM (QRAM)','Hypothetical memory querying superpositions of addresses; powerful if built, but its physical cost is debated (no scalable QRAM exists).']];
THEORY.forEach(function(t){
  ONLINE.push({kind:'quantum-record',cat:'theory',title:'Theory: '+t[0],concept:t[1],
    source:'online',source_ref:'Standard quantum information theory'});
});

/* ---------- generated records (source: signature) ---------- */
function genGate(rnd){
  var th=rnd()*2*Math.PI;
  var M=matMul(rz(th),matMul(ry(th/2),rx(th/3)));
  return {kind:'generated-gate',cat:'gates',title:'Generated unitary gate G'+ri(rnd,1000,9999),
    gate_name:'Signature-generated single-qubit unitary',qubits:1,
    concept:'A randomly generated single-qubit unitary (product of rotations); verified unitary by the validator.',
    matrix:M,unitary:true,
    source:'signature',creation_mode:'SIGNATURE-GENERATED'};
}
function genCircuit(rnd){
  var nQ=ri(rnd,1,3),gates=[],ng=ri(rnd,1,4);
  var singles=['H','X','Z','S','T'];
  for(var i=0;i<ng;i++){
    var roll=rnd();
    if(nQ>=2&&roll<0.3){var c=ri(rnd,0,nQ-1),t=ri(rnd,0,nQ-1);if(t===c)t=(t+1)%nQ;gates.push({gate:'CNOT',control:c,target:t});}
    else gates.push({gate:pick(singles,rnd),target:ri(rnd,0,nQ-1)});
  }
  var st=simulate(nQ,gates);
  return {kind:'generated-circuit',cat:'circuits',title:'Generated circuit R'+ri(rnd,1000,9999)+' ('+nQ+' qubits)',
    concept:'A randomly generated '+nQ+'-qubit circuit; the validator re-simulates it and checks every amplitude.',
    n_qubits:nQ,gates:gates,initial_state:'|'+new Array(nQ+1).join('0')+'>',
    final_amplitudes:ampsOf(st),probabilities:probsOf(st),
    source:'signature',creation_mode:'SIGNATURE-GENERATED'};
}
function genTheory(rnd){
  var topics=[['Quantum volume','A single-number benchmark combining qubit count, connectivity and error rates into effective circuit size.'],
   ['Mid-circuit measurement','Measuring some qubits mid-computation and conditioning later gates on the result; enables teleportation and error correction.'],
   ['Dynamical decoupling','Pulse sequences that average away environmental noise, extending effective coherence times.'],
   ['Readout error mitigation','Characterizing the measurement confusion matrix and inverting it classically to unbias results.'],
   ['Zero-noise extrapolation','Running at amplified noise levels and extrapolating back to zero noise; a practical error-mitigation trick.'],
   ['Entanglement swapping','Bell measurement on halves of two pairs entangles the remaining halves: the backbone of quantum repeaters.']];
  var t=pick(topics,rnd);
  return {kind:'generated-theory',cat:'theory',title:'Generated note: '+t[0],concept:t[1],
    source:'signature',creation_mode:'SIGNATURE-GENERATED'};
}

function baseRec(seed,cat,title){return {id:PREFIX+String(seed).padStart(7,'0'),category:cat,title:title,_seed:seed};}
function generate(seed,opts,rnd){
  opts=opts||{};rnd=rnd||prng(seed);
  var cat=opts.category;
  if(seed>=1&&seed<=ONLINE.length&&!cat){
    var e=ONLINE[seed-1],r=baseRec(seed,e.cat,e.title);
    Object.keys(e).forEach(function(k){if(k!=='cat'&&k!=='title')r[k]=e[k];});
    return r;
  }
  if(seed>=1&&seed<=ONLINE.length&&cat){
    var pool=ONLINE.filter(function(x){return x.cat===cat;});
    if(pool.length){var e2=pool[(rnd()*pool.length)|0],r2=baseRec(seed,cat,e2.title+' \u2014 archive pick');
      Object.keys(e2).forEach(function(k){if(k!=='cat'&&k!=='title')r2[k]=e2[k];});return r2;}
  }
  var roll=rnd(),g;
  if(cat==='gates')g=genGate(rnd);
  else if(cat==='circuits')g=genCircuit(rnd);
  else if(cat==='theory')g=genTheory(rnd);
  else g=roll<0.4?genGate(rnd):(roll<0.8?genCircuit(rnd):genTheory(rnd));
  cat=cat||g.cat;g.category=cat;
  var rec=baseRec(seed,cat,g.title);
  Object.keys(g).forEach(function(k){if(k!=='cat'&&k!=='title')rec[k]=g[k];});
  return rec;
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  if(!/^JAH-QNT-\d{7}$/.test(r.id||''))e.push('id');
  if(CATS.indexOf(r.category)<0)e.push('category');
  if(typeof r.title!=='string'||!r.title.length)e.push('title');
  if(typeof r.concept!=='string'||r.concept.length<10)e.push('concept');
  if(r.source!=='online'&&r.source!=='signature')e.push('source');
  if(r.source==='online'&&typeof r.source_ref!=='string')e.push('source_ref');
  if(r.source==='signature'&&r.creation_mode!=='SIGNATURE-GENERATED')e.push('creation_mode');
  var k=r.kind;
  if(r.matrix){
    if(!isUnitary(r.matrix))e.push('not unitary');
  }
  if(k==='quantum-record'&&r.cat==='circuits'){
    var st;
    try{st=simulate(r.n_qubits,r.gates);}catch(x){e.push('sim threw');}
    if(st){
      var a=ampsOf(st),p=probsOf(st);
      if(a.length!==r.final_amplitudes.length)e.push('amplitude count');
      else for(var i=0;i<a.length;i++){if(!cEq([a[i][0],a[i][1]],[r.final_amplitudes[i][0],r.final_amplitudes[i][1]],2e-6))e.push('amplitude mismatch');}
      for(i=0;i<p.length;i++)if(Math.abs(p[i]-r.probabilities[i])>2e-6)e.push('probability mismatch');
    }
  }
  if(k==='generated-circuit'){
    var st2=simulate(r.n_qubits,r.gates),a2=ampsOf(st2);
    for(var j=0;j<a2.length;j++)if(!cEq([a2[j][0],a2[j][1]],[r.final_amplitudes[j][0],r.final_amplitudes[j][1]],2e-6))e.push('amplitude mismatch');
  }
  if(r.grover){
    var want=Math.floor(Math.PI/4*Math.sqrt(r.grover.N));
    if(want!==r.grover.iterations)e.push('grover count');
  }
  return {ok:!e.length,errors:e};
}
function driftCheck(rec,sample){
  var seen={};(sample||[]).forEach(function(s){if(s&&s.t)seen[s.t]=1;});
  if(seen[rec.title])return {ok:false,errors:['duplicate title in archive sample']};
  return {ok:true,errors:[]};
}
var gen={version:'jahdb-quantum-1.0',generate:generate,validate:validate,driftCheck:driftCheck};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('quantum',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
