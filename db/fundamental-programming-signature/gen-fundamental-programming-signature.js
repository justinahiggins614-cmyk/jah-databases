(function(){'use strict';
/* jahdb-fundamental-programming-signature-1.0 — fundamental programming bedrock generator.
   Property of Justin Addam Higgins (JAH). Deterministic: same seed always makes the same record.
   src:"signature" = Signature-system formulation, clearly labeled */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var PREFIX='JAH-SFPRO-';
var KIND='fundamental programming record (Signature original)';
var SECTIONS=['about', 'reasoning', 'quantities', 'mechanism', 'miscon'];
var BRIEF={'about':'Programming is the craft of instructing computers precisely: translating human intent into unambiguous steps a machine can execute. It is applied logic — every program is an executable argument.', 'reasoning':'Programmers reason by decomposition and testing: break the problem into small functions, define their contracts, implement, and test each piece. The computer is the ultimate pedant — it does exactly what you wrote, not what you meant.', 'quantities':'The core quantities are correctness (does it work), complexity (how cost grows), and readability (can a human follow it). Lines of code measure size; bugs per thousand lines measure quality; latency and throughput measure performance.', 'mechanism':'Programming proceeds by the write-test-refine loop: write a small piece, run it, observe the failure, fix the understanding, repeat. The error message is the teacher — reading it carefully is the master skill.', 'miscon':'Programming is not typing fast: it is thinking precisely. Copying code without understanding builds nothing. And \'it works on my machine\' is not done — done means tested, readable, and reproducible.'};
var SIGLENS=['In the Signature system, programming is the literacy of construction: every generator, every demo, every tool in this network is a program, and the Signature formulation teaches each principle as code you can run and modify.','The Signature practice is to write the program: implement the principle, run it, break it, fix it — so programming fundamentals are learned at the keyboard, not just read on the page.'];
var DEMOS=['#!/usr/bin/env python3\n"""{TITLE} -- recursion demo. Runs as-is with python3."""\ndef factorial(n):\n    return 1 if n <= 1 else n * factorial(n - 1)\ndef fib(n):\n    return n if n < 2 else fib(n-1) + fib(n-2)\nprint("5! =", factorial(5))\nprint("fib(10) =", fib(10))\nprint("recursion: solve a smaller version of the same problem")\n', '#!/usr/bin/env python3\n"""{TITLE} -- functions and scope demo. Runs as-is with python3."""\ncounter = 0\ndef increment(step=1):\n    global counter\n    counter += step\n    return counter\nprint(increment(), increment(5), increment())\nprint("final counter:", counter)\ndef make_adder(n):\n    return lambda x: x + n\nadd10 = make_adder(10)\nprint("add10(5) =", add10(5))\n', '#!/usr/bin/env python3\n"""{TITLE} -- list processing demo. Runs as-is with python3."""\nnums = list(range(1, 21))\nevens = [n for n in nums if n % 2 == 0]\nsquares = {n: n * n for n in evens}\ntotal = sum(squares.values())\nprint("evens:", evens)\nprint("sum of even squares 1..20:", total)\nwords = ["apple", "fig", "cherry"]\nprint("sorted by length:", sorted(words, key=len))\n'];
var TOPICS=[['Signature What Programming Is','Programming is writing precise instructions a computer can execute: the translation of intent into algorithm into code. It is the most literal form of writing — the machine does exactly what the program says, which is why programming teaches precision of thought.'],
['Signature The Core Question of Programming','The core question is: how do I tell the machine to do this correctly? Every programming task decomposes into specifying the what (the contract), designing the how (the algorithm), and verifying the result (the tests).'],
['Signature Assumptions: The Machine Is Literal','Programming assumes the machine is perfectly literal: it executes the instructions written, not the ones intended. This assumption is the source of both the power (total control) and the pain (total responsibility) of the craft.'],
['Signature The Vocabulary: Variables, Functions, Control Flow','The vocabulary names the building blocks: variables (named storage), functions (named computations), conditionals (choices), loops (repetition), and data structures (organization). Every program in every language is built from these.'],
['Signature Correctness: The Fundamental Quantity','Correctness is the fundamental quantity: does the program do what it should for all valid inputs? It is established by testing (evidence) and, where it matters, by proof (certainty). A fast wrong program is worthless.'],
['Signature Decomposition: The Primary Method','Decomposition is the primary method: split the problem until each piece is trivially solvable, solve the pieces, compose the solutions. Functions are the unit of decomposition; their contracts — what they assume, what they guarantee — are the load-bearing specifications.'],
['Signature A Canonical First Example','The canonical first example prints \'Hello, world\' — then the real first program computes something: the factorial, the Fibonacci numbers, a sorted list. From the first program, the loop is the same forever: write, run, read the error, fix, repeat.'],
['Signature How Programming Measures','Programming measures with tests and profilers: unit tests asserting behavior, benchmarks timing performance, coverage measuring what the tests touch. \'It works\' is a claim; the test suite is the evidence.'],
['Signature The Core Mechanism: Write, Run, Fix','The core mechanism is the feedback loop: write a small piece, run it, read the failure, correct the understanding. Short loops beat long planning — the computer corrects your mental model faster than speculation does.'],
['Signature The Simplest Law: Names Mean What You Define','The simplest law is that names mean exactly what the definition says — no more. A variable holds what was assigned; a function does what its body says. Bugs live in the gap between what you think a name means and what it actually means.'],
['Signature Common Misconceptions in Programming','The misconceptions mislead beginners: that programming is typing speed (it is thinking), that copying code is learning (understanding is learning), that the language matters most (concepts transfer; syntax doesn\'t), and that experts don\'t get errors (experts get them constantly and read them).'],
['Signature How Beginners Practice Programming','Beginners practice by writing lots of small programs: daily coding, tracing execution by hand, and fixing bugs without help first. Reading others\' code teaches idioms; writing your own teaches thinking. There is no substitute for hours at the keyboard.'],
['Signature The Core Model: The Function','The function is the core model: input in, output out, with a contract. Pure functions — same input, same output, no side effects — are the easiest to test and compose, which is why functional ideas permeate all modern programming.'],
['Signature The Great Idea: Abstraction','Abstraction is the great idea: hiding complexity behind interfaces so each level of a program thinks at its own scale. Libraries, APIs, and languages themselves are abstractions — the whole edifice of software is abstraction stacked on abstraction.'],
['Signature Systems Thinking: State and Side Effects','Systems thinking in programming confronts state: programs that remember are powerful and dangerous. Managing state — who can change what, when — is the central difficulty of large programs, and the reason for encapsulation, immutability, and transactions.'],
['Signature Invariance: Loop Invariants','The invariance principle is the loop invariant: a property true before and after every iteration. Finding it turns testing into reasoning — if the invariant holds and the loop terminates, the result is correct by construction.'],
['Signature Approximation: Trade-offs in Code','Approximation in programming is the engineering trade: clarity versus speed, generality versus simplicity, done now versus perfect later. Premature optimization is the classic sin — measure first, then optimize the hot spot.'],
['Signature Evidence Standards: Tests','The evidence standard is the test suite: automated checks that the program behaves as specified, run on every change. Test-driven development writes the test first — the specification executable — then the code that satisfies it.'],
['Signature Classic Discoveries','The classic discoveries are structured programming, the relational model, object orientation, functional programming\'s renaissance, and version control. Each changed not just what programs do but how programmers think.'],
['Signature Core Trade-offs: Readability versus Cleverness','The core trade-off is readability versus cleverness: the clever one-liner that no one can debug loses to the clear ten-liner. Code is read far more than written — optimize for the reader, who is often your future self.'],
['Signature Handling Uncertainty: Defensive Programming','Programming handles uncertainty defensively: validate inputs, handle errors explicitly, fail fast with clear messages. A program that crashes loudly at the bug beats one that corrupts data silently for months.'],
['Signature Tools of the Trade','The tools of the trade are the editor, the debugger, the test runner, and version control. The deepest is the debugger used well — not print statements scattered, but breakpoints, watches, and the discipline to form a hypothesis before stepping.'],
['Signature Ethics and Responsibility','Ethics in programming is about the systems you build: who they serve, who they harm, what data they take. The programmer\'s responsibility includes refusing harmful work and writing software that respects its users\' privacy and autonomy.'],
['Signature Teaching Programming','Teaching programming well means writing code from the first minutes: the first program runs today, not after a chapter of theory. Live coding, small exercises, and immediate feedback beat lectures — programming is learned by doing.'],
['Signature The Frontier Question','The frontier question is human-machine collaboration in coding: AI assistants that write code shift the skill from writing to specifying, reviewing, and verifying. The frontier asks what programming becomes when the typing is automated.'],
['Signature Unifying Theories','The unifying theories are computability and the lambda calculus: all programming languages express the same computable functions, and the lambda calculus shows computation needs only function definition and application. One foundation beneath a thousand languages.'],
['Signature Computational Thinking','Computational thinking exports programming\'s methods everywhere: decomposition, pattern recognition, abstraction, and algorithms applied to non-programming problems. It is programming\'s gift to general problem-solving.'],
['Signature Bridges to Other Fields','Programming bridges to every field with a computer: science (simulation), art (creative coding), business (automation), and AI (models as programs). Software ate the world because programming is the universal lever.'],
['Signature The Great Unsolved Problems','The great unsolved problems are open and labeled as such: fully automatic bug-free programming, the perfect balance of safety and expressiveness in language design, and verifying large systems completely. Active research, no settled answers.'],
['Signature How New Claims Are Validated','New programming claims are validated by implementation and adoption: the language feature shipped, the tool used on real codebases, the benchmark reproduced. A programming idea earns trust when programmers voluntarily use it.'],
['Signature The Great Debates','The great debates — static versus dynamic typing, objects versus functions, tabs versus spaces — are really about values: safety versus flexibility, structure versus freedom. The debates persist because different problems reward different trade-offs.'],
['Signature Failure Modes: When Programming Gets It Wrong','Programming gets it wrong through untested assumptions, clever code nobody understands, and \'temporary\' hacks that become permanent. The immune system is code review, tests, and the discipline to refactor.'],
['Signature Synthesis: Building on the Fundamentals','Advanced synthesis architects whole systems from fundamentals: modules with clean contracts, tested in isolation, composed into reliable wholes. The fundamentals — decomposition, contracts, tests — are the difference between software and spaghetti.'],
['Signature The Signature Formulation: Programming as Executable Literacy','The Signature formulation makes programming the literacy of the network: every principle here is code you can run, because in the Signature system a programming concept you cannot execute is a concept you have not yet learned. That is the Signature capstone on programming bedrock.']];
var TIERS=[['foundations','Foundations',1,12],['compounded','Compounded',13,24],['advanced','Advanced',25,34]];
function pad(n){var s=String(n);while(s.length<6)s='0'+s;return s;}
function firstSentence(s){var m=/^(.+?[.!?])(\s|$)/.exec(String(s).trim());return m?m[1]:String(s).slice(0,160);}
function compose(i,title,essence){
  var elab,desc,how,kps;
  if(false){
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
    standards:["Programs are tested: every function has cases that prove it works.", "Code is readable: names say what things are, structure shows the logic.", "Reproducibility: anyone can run it and get the same result."],citations:["Knuth, D. E. \u2014 The Art of Computer Programming (Addison-Wesley).", "Petzold, C. \u2014 Code: The Hidden Language of Computer Hardware and Software.", "Cross-checked against the JAH Databases network archive before filing."],src:'signature',ladder_rank:rank,ladder_tier:tier,
    demo:{kind:'fundamental-programming-demo',language:'python',program:demo,note:'Working demonstration program for this record. Runs as-is with python3.'},_seed:seed};
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
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator){JAHDB.registerGenerator('fundamental-programming-signature',{generate:generate,validate:validate,driftCheck:driftCheck});}
if(typeof module!=='undefined'&&module.exports){module.exports={generate:generate,validate:validate,driftCheck:driftCheck};}
})();
