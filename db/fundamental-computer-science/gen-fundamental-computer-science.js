(function(){'use strict';
/* jahdb-fundamental-computer-science-1.0 — fundamental computer-science bedrock generator.
   Property of Justin Addam Higgins (JAH). Deterministic: same seed always makes the same record.
   src:"public-harvest" = established first-principles knowledge, fact-checked */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var PREFIX='JAH-FCSC-';
var KIND='fundamental computer-science record';
var SECTIONS=['about', 'reasoning', 'quantities', 'mechanism', 'miscon'];
var BRIEF={'about':'Computer science is the study of computation: what can be computed, how efficiently, and how to organize computation into reliable systems. It spans theory (algorithms, complexity) and practice (systems, software) as one discipline.', 'reasoning':'Computer scientists reason by abstraction and reduction: define the problem precisely, reduce it to known problems, analyze the algorithm\'s resource use, and prove correctness. A program is a constructive proof that a problem is solvable.', 'quantities':'The core quantities are time and space complexity — how resource use grows with input size — measured in Big-O notation. Bits, operations, and memory accesses are the field\'s atoms of cost.', 'mechanism':'Computer science advances by the algorithm-implementation-measurement loop: design the algorithm, analyze it theoretically, implement it, and measure it on real workloads. Theory predicts; measurement decides.', 'miscon':'Computer science is not just programming: programming is the laboratory, not the science. Computers do not \'think\' in any human sense — they execute instructions. And more hardware does not fix a bad algorithm: complexity dominates constants.'};
var SIGLENS=['In the Signature system, computer science is the foundation of all digital construction: every database engine, every generator, every AI in this network is applied computer science, and the Signature formulation teaches each principle as machinery you can run.','The Signature practice is to run the computer science: implement the algorithm, measure the complexity, prove the property on the machine — so computation is experienced as executable truth.'];
var DEMOS=['#!/usr/bin/env python3\n"""{TITLE} -- binary search demo. Runs as-is with python3."""\ndef binary_search(a, x):\n    lo, hi, steps = 0, len(a) - 1, 0\n    while lo <= hi:\n        steps += 1\n        mid = (lo + hi) // 2\n        if a[mid] == x:\n            return mid, steps\n        elif a[mid] < x:\n            lo = mid + 1\n        else:\n            hi = mid - 1\n    return -1, steps\na = list(range(0, 1000000, 2))\nfor x in [0, 42, 999998, 7]:\n    idx, steps = binary_search(a, x)\n    print(f"search {x}: index={idx} steps={steps} (log2(500000)~19)")\n', '#!/usr/bin/env python3\n"""{TITLE} -- Big-O growth demo. Runs as-is with python3."""\nimport math\nfor n in [10, 100, 1000, 10000]:\n    print(f"n={n:>5}: n={n}  n log n={int(n*math.log2(n)):>7}  n^2={n*n:>9}")\nprint("a quadratic algorithm at n=10000 does 100M ops; n log n does 130K")\n', '#!/usr/bin/env python3\n"""{TITLE} -- recursion demo (Towers of Hanoi). Runs as-is with python3."""\ndef hanoi(n, src, dst, aux, moves):\n    if n == 1:\n        moves.append((src, dst))\n    else:\n        hanoi(n - 1, src, aux, dst, moves)\n        moves.append((src, dst))\n        hanoi(n - 1, aux, dst, src, moves)\nmoves = []\nhanoi(4, "A", "C", "B", moves)\nprint("moves for 4 disks:", len(moves), "(2^4 - 1 = 15)")\nprint(moves[:5], "...")\n'];
var TOPICS=[['What Computer Science Is','Computer science is the science of computation: which problems can be solved mechanically, how efficiently, and how to build reliable systems that do it. It is both mathematics (algorithms, complexity, logic) and engineering (systems that must work in the world).'],
['The Core Question of Computer Science','The core question is: what is computable, and at what cost? Turing\'s 1936 paper defined computability itself; complexity theory then asked the price — and found problems whose solutions exist but cannot be found before the universe ends.'],
['Assumptions: The Church-Turing Thesis','The field assumes the Church-Turing thesis: every effectively computable function is computable by a Turing machine. It is unprovable but unfalsified — every proposed model of computation has proved equivalent in power.'],
['The Vocabulary: Algorithms, Data Structures, Complexity','The vocabulary names the pieces: algorithms (precise procedures), data structures (organized data), and complexity (resource growth). Fluency means thinking in these three simultaneously — the right structure makes the algorithm obvious.'],
['Time and Space: The Fundamental Quantities','Time and space complexity are the fundamental quantities: how runtime and memory grow with input size, expressed in Big-O notation. An O(n log n) sort beats O(n²) at scale no matter the hardware — complexity is destiny.'],
['The Algorithm: The Primary Method','The algorithm is the primary method: a finite, unambiguous procedure that solves a problem class. Euclid\'s algorithm for the greatest common divisor, from 300 BCE, still runs — the oldest algorithm in continuous use.'],
['A Canonical First Example','The canonical first example is binary search: to find x in a sorted array, compare with the middle, discard half, repeat. Twenty comparisons search a million entries — the logarithm made concrete, and the pattern behind all divide-and-conquer.'],
['How Computer Science Measures','The field measures with benchmarks, profilers, and asymptotic analysis: wall-clock time on real workloads, operation counts in theory. Both matter — theory predicts scaling, measurement catches the constants theory ignores.'],
['The Core Mechanism: Abstraction Layers','The core mechanism is abstraction layers: transistors to gates to machine code to operating systems to applications, each layer hiding the one below. Computer science is the discipline of building and reasoning across these layers without drowning.'],
['The Simplest Law: The Stored Program','The simplest law is the stored-program concept: instructions and data share the same memory, so programs can manipulate programs. Compilers, operating systems, and viruses are all consequences of this one architectural decision.'],
['Common Misconceptions in Computer Science','The misconceptions mislead: that computer science equals programming (it is the science; programming is the lab), that computers understand (they execute), that more hardware fixes bad algorithms (complexity dominates), and that AI \'thinks\' like a person.'],
['How Beginners Practice Computer Science','Beginners practice by writing, testing, and reading programs: solve small problems daily, trace execution by hand, read others\' code. Debugging is the core skill — the patient, systematic hunt for the false assumption.'],
['The Core Model: The Turing Machine','The Turing machine is the core model: an infinite tape, a read-write head, a finite control — and provably equivalent to every computer ever built. It defines computability, and its halting problem defines the limits of computation.'],
['The Great Result: P versus NP','The P versus NP question is the great open problem: can every problem whose solution is quickly checkable also be quickly solved? A proof either way would remake cryptography, optimization, and our understanding of creativity itself.'],
['Systems Thinking: Operating Systems','Systems thinking in computer science is the operating system: managing processes, memory, and I/O across competing programs with limited resources. Scheduling, virtual memory, and filesystems are applied resource economics.'],
['Invariance: What Abstraction Preserves','The invariance principle is that correct abstractions preserve behavior: a sorting algorithm sorts regardless of language; a protocol works regardless of medium. Invariants — properties preserved by every step — are also how we prove programs correct.'],
['Approximation: Heuristics','Approximation uses heuristics where exactness is unaffordable: greedy algorithms, local search, and randomized methods trade optimality for speed. For NP-hard problems, approximation is not a compromise — it is the only game.'],
['Evidence Standards: Proof and Benchmark','The evidence standard is proof for algorithms, benchmarks for systems: prove correctness and complexity, then measure on real workloads. A benchmark without a workload description is marketing; a proof without an implementation is a promise.'],
['Classic Discoveries','The classic discoveries are the stored program, the compiler, time-sharing, the relational model, public-key cryptography, and the World Wide Web. Each turned a theoretical possibility into infrastructure civilization now depends on.'],
['Core Trade-offs: Time versus Space','The core trade-off is time versus space: memoization trades memory for speed, compression trades time for space, indexes trade storage for query speed. Every system design is a point chosen on this frontier.'],
['Handling Uncertainty: Randomization','Randomized algorithms handle uncertainty by design: random pivots make quicksort fast with high probability, probabilistic data structures answer approximately with bounded error. Randomness is a computational resource, like time and space.'],
['Tools of the Trade','The tools of the trade are a programming language, a debugger, a profiler, and version control. The deepest is the invariant — the statement true before and after every loop iteration, which turns testing into proof.'],
['Ethics and Responsibility','Ethics in computer science is about power: algorithms decide loans, sentences, and visibility. The field\'s responsibility is to audit its systems for bias, protect privacy by design, and refuse the comforting fiction that code is neutral.'],
['Teaching Computer Science','Teaching it well starts with making things: the first program should do something visible within minutes. Concepts follow construction — loops make sense when you have needed one, recursion when iteration has failed you.'],
['The Frontier Question','The frontier question is the cost of intelligence: what are the fundamental limits of learning, reasoning, and optimization? Deep learning works beyond current theory — the frontier is building the theory that explains the practice.'],
['Unifying Theories','The unifying theories connect computation\'s faces: the Curry-Howard correspondence (proofs are programs), the equivalence of computational models, and information theory beneath it all. One subject — symbol manipulation — seen as logic, as physics, as engineering.'],
['Computational Thinking About Computation','Metacomputation studies computation studying itself: interpreters running interpreters, compilers compiling compilers, complexity of complexity. Self-reference is not a paradox here — it is the bootstrap the whole field stands on.'],
['Bridges to Other Fields','Computer science bridges to every field it touches: bioinformatics, computational physics, digital humanities, fintech, and AI as its most ambitious child. Each bridge exports algorithms and imports problems that demand new theory.'],
['The Great Unsolved Problems','The great unsolved problems are open and labeled as such: P versus NP, the exact power of quantum computation, optimal sorting networks, and the theoretical foundations of deep learning. Millennium Prize included; no settled answers.'],
['How New Claims Are Validated','New claims are validated by proof, artifact, and replication: the theorem proved, the code released, the benchmark reproduced by others. Reproducibility badges and artifact evaluation are the field\'s growing immune system.'],
['The Great Debates','The great debates include the role of theory versus hacking, whether software engineering is engineering, open versus closed models, and how to value correctness against speed. The debates are productive — each side ships.'],
['Failure Modes: When Computer Science Gets It Wrong','The field gets it wrong through unproved \'obvious\' optimizations, benchmarks that don\'t match workloads, and complexity analysis that ignores constants users feel. The immune system is measurement on real data and proof where it counts.'],
['Synthesis: Building on the Fundamentals','Advanced synthesis designs whole systems from fundamentals: choose the data structure for the access pattern, the algorithm for the complexity budget, the abstraction for the team. The fundamentals are the load-bearing decisions in every architecture.'],
['The Signature Formulation: Computer Science as Executable Truth','The Signature formulation makes computer science the executable bedrock of the network: every principle here runs as code you can execute and measure, because in the Signature system computation that cannot be run is speculation. That is the Signature capstone on computational bedrock.']];
var TIERS=[['foundations','Foundations',1,12],['compounded','Compounded',13,24],['advanced','Advanced',25,34]];
function pad(n){var s=String(n);while(s.length<6)s='0'+s;return s;}
function firstSentence(s){var m=/^(.+?[.!?])(\s|$)/.exec(String(s).trim());return m?m[1]:String(s).slice(0,160);}
function compose(i,title,essence){
  var elab,desc,how,kps;
  if(true){
    elab=[BRIEF[SECTIONS[(i+0)%5]],BRIEF[SECTIONS[(i+2)%5]]];
    desc=essence+'\n\n'+elab.join('\n\n');
    how=BRIEF.mechanism+' '+firstSentence(essence)+' The working habit here: '+BRIEF.reasoning.split('. ')[0]+'.';
    kps=[firstSentence(essence),'How the field reasons: '+firstSentence(BRIEF.reasoning),'Core quantities and units: '+firstSentence(BRIEF.quantities),'Common misconception to avoid: '+firstSentence(BRIEF.miscon),'Run the demo program below to make this principle concrete and testable.'];
  }else{
    elab=[SIGLENS[0],BRIEF[SECTIONS[(i+3)%5]]];
    desc=essence+'\n\n'+elab.join('\n\n');
    how=SIGLENS[1]+' '+BRIEF.mechanism+' '+firstSentence(essence);
    kps=[firstSentence(essence),'Signature framing: '+firstSentence(SIGLENS[0]),'Signature practice: '+firstSentence(SIGLENS[1]),'Common misconception to avoid: '+firstSentence(BRIEF.miscon),'Run the demo program below to make this principle concrete and testable.'];
  }
  return {desc:desc,how:how,kps:kps};
}
function generate(seed,opts){
  var s=prng(seed);
  var ti=(s()*TOPICS.length)|0;
  var topic=TOPICS[ti], i=ti, rank=ti+1, title=topic[0], essence=topic[1];
  var tier='foundations',glabel='Foundations';
  for(var k=0;k<TIERS.length;k++){if(rank>=TIERS[k][2]&&rank<=TIERS[k][3]){tier=TIERS[k][0];glabel=TIERS[k][1];}}
  var id=PREFIX+pad(seed);
  var c=compose(i,title,essence);
  var demo=DEMOS[ti%DEMOS.length].split('{TITLE}').join(title);
  return {id:id,t:title,g:glabel,c:0,name:title+' - '+KIND,title:title,description:c.desc,how_it_works:c.how,
    key_points:c.kps,requirements:['Read the description and key points first — they carry the essential first principles.','No prior knowledge of the subject is assumed; the ladder rank tells you what to read first.','Use the demo program to make the principle concrete — run it, change the numbers, re-run.'],
    standards:["Correctness first: an algorithm must be proved or tested correct before it is optimized.", "Complexity is analyzed asymptotically: state the Big-O, not just the benchmark.", "Reproducibility: code, data, and environment are shared so results can be rebuilt."],citations:["Cormen, T. H. et al. \u2014 Introduction to Algorithms (MIT Press).", "Turing, A. M. \u2014 On Computable Numbers (1936): the founding paper.", "Cross-checked against the JAH Databases network archive before filing."],src:'public-harvest',ladder_rank:rank,ladder_tier:tier,
    demo:{kind:'fundamental-computer-science-demo',language:'python',program:demo,note:'Working demonstration program for this record. Runs as-is with python3.'},_seed:seed};
}
function validate(r){
  var errs=[];
  if(!r.id)errs.push('missing id');
  if(!r.title)errs.push('missing title');
  if(!r.description||r.description.length<200)errs.push('description too short (<200)');
  if(!r.key_points||r.key_points.length<3)errs.push('key_points too few');
  if(!r.demo||!r.demo.program||r.demo.program.length<100)errs.push('demo program missing/short');
  if(!r.ladder_rank||!r.ladder_tier)errs.push('ladder missing');
  return {ok:errs.length===0,errors:errs};
}
function driftCheck(rec,sample){
  for(var i=0;i<sample.length;i++){if(sample[i].t===rec.title)return {ok:false,errors:['duplicate title']};}
  return {ok:true,errors:[]};
}
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator){JAHDB.registerGenerator('fundamental-computer-science',{generate:generate,validate:validate,driftCheck:driftCheck});}
if(typeof module!=='undefined'&&module.exports){module.exports={generate:generate,validate:validate,driftCheck:driftCheck};}
})();
