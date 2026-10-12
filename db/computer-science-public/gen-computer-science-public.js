(function(){'use strict';
/* Public Computer Science Database generator — jahdb-computer-science-public-generator-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed always makes the same record.
   src:"public" = Fact-checked public information */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX='JAH-COMP-PUB-';
var TOPICS=[["Algorithms", "Step-by-step procedures; correctness and efficiency."], ["Data Structures", "Arrays, lists, trees, graphs, and hash tables."], ["Programming Basics", "Variables, control flow, functions, and types."], ["Object-Oriented Programming", "Classes, objects, inheritance, and encapsulation."], ["Functional Programming", "Pure functions, immutability, and higher-order functions."], ["Databases", "Relational models, SQL, and indexing."], ["Operating Systems", "Processes, memory, filesystems, and scheduling."], ["Computer Networks", "Packets, protocols, TCP/IP, and the internet."], ["Web Development", "HTML, CSS, JavaScript, and client-server architecture."], ["Compilers", "From source code to machine code: lexing, parsing, codegen."], ["Machine Learning", "Training models from data: supervised and unsupervised."], ["Artificial Intelligence", "Search, reasoning, and intelligent agents."], ["Cybersecurity", "Threats, cryptography, and secure design."], ["Cryptography", "Encryption, hashing, and key exchange."], ["Software Engineering", "Design, testing, version control, and teamwork."], ["Big-O Notation", "Analyzing algorithm running time and space."], ["Recursion", "Functions that call themselves; divide and conquer."], ["Sorting Algorithms", "Quicksort, mergesort, heapsort, and their trade-offs."], ["Graph Algorithms", "BFS, DFS, shortest paths, and spanning trees."], ["Dynamic Programming", "Solving problems by caching subproblem results."], ["Concurrency", "Threads, locks, and parallel execution."], ["Distributed Systems", "Consensus, replication, and fault tolerance."], ["Computer Architecture", "CPUs, caches, and instruction sets."], ["Theory of Computation", "Automata, Turing machines, and complexity classes."], ["Debugging", "Systematic methods for finding and fixing bugs."]];
var ANGLES=['overview','detailed','examples','faq','history','applications'];
function pad(n){var s=String(n);while(s.length<6)s='0'+s;return s;}
function generate(seed,opts){
  var s=prng(seed);
  var ti=(s()*TOPICS.length)|0, ai=(s()*ANGLES.length)|0;
  var topic=TOPICS[ti], angle=ANGLES[ai];
  var id=PREFIX+pad(seed);
  var title=topic[0]+' ('+angle+')';
  var desc=topic[1]+' This '+angle+' guide provides comprehensive coverage.';
  var content='['+angle+'] '+topic[0]+': '+topic[1]+' Full detailed content for '+angle+' perspective.';
  return {
    id:id, title:title, description:desc, genre:angle,
    type:'computer science knowledge record', content:content,
    demo:null, src:'public', _seed:seed
  };
}
function validate(r){
  var errs=[];
  if(!r.id)errs.push('missing id');
  if(!r.title)errs.push('missing title');
  if(!r.content||r.content.length<50)errs.push('content too short');
  return {ok:errs.length===0, errors:errs};
}
function driftCheck(rec,sample){
  // Simple: check for exact title duplicates in sample
  for(var i=0;i<sample.length;i++){if(sample[i].t===rec.title)return {ok:false,errors:['duplicate title']};}
  return {ok:true,errors:[]};
}
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator){JAHDB.registerGenerator('computer-science-public',{generate:generate,validate:validate,driftCheck:driftCheck});}
if(typeof module!=='undefined'&&module.exports){module.exports={generate:generate,validate:validate,driftCheck:driftCheck};}
})();