(function(){'use strict';
/* JAH The Combinatorics Database generator — jahdb-combinatorics-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-COMB-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "What Combinatorics Is - Foundations",
  "The Addition and Multiplication Principles - Foundations",
  "The Pigeonhole Principle - Foundations",
  "Permutations: Counting Ordered Arrangements - Foundations",
  "Combinations: Choosing Without Order - Foundations",
  "Pascal's Triangle and the Binomial Theorem - Foundations",
  "Permutations with Repetition and Multinomial Coefficients - Foundations",
  "Combinations with Repetition: Stars and Bars - Foundations"
 ],
 "Compounded": [
  "Binomial Identities: Algebraic and Combinatorial Proofs - Compounded",
  "The Inclusion-Exclusion Principle - Compounded",
  "Derangements: Permutations with No Fixed Points - Compounded",
  "The Bijection Principle and Combinatorial Proofs - Compounded",
  "Double Counting: One Answer, Two Ways - Compounded",
  "Integer Partitions: Breaking Numbers Apart - Compounded",
  "Set Partitions and Stirling Numbers of the Second Kind - Compounded",
  "Permutation Cycles and Stirling Numbers of the First Kind - Compounded",
  "Lattice Paths and the Reflection Principle - Compounded",
  "Recurrence Relations: Sequences Defined by Their Past - Compounded",
  "Solving Linear Recurrences: The Characteristic Equation - Compounded",
  "Ordinary Generating Functions - Compounded",
  "Exponential Generating Functions - Compounded",
  "The Twelvefold Way: Balls into Boxes - Compounded",
  "Catalan Numbers: The Ubiquitous Sequence - Compounded"
 ],
 "Advanced": [
  "Bell Numbers and the Partitions of a Set - Advanced",
  "Partitions of Integers: Euler's Theorems - Advanced",
  "Graph Theory as Counting: Walks and the Handshaking Lemma - Advanced",
  "Trees and Cayley's Formula - Advanced",
  "Eulerian Trails and Hamiltonian Cycles - Advanced",
  "Ramsey Theory: Order Forced from Chaos - Advanced",
  "Block Designs and the Fano Plane - Advanced",
  "Latin Squares and Orthogonal Arrays - Advanced",
  "Combinatorial Games: Winning Strategies - Advanced",
  "Extremal Combinatorics: Turan's Theorem - Advanced",
  "The Probabilistic Method: Proving by Random Choice - Advanced",
  "Polya Enumeration: Counting Up to Symmetry - Advanced",
  "Algebraic Combinatorics: Symmetric Functions - Advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Combinatorics Study — "+safe+"\n"
   + "# Field: "+field+"\n"
   + "record = {'title': \""+safe+"\", 'field': \""+field+"\"}\n"
   + "def summarize(r):\n"
   + "    return r['title'] + ' [' + r['field'] + ']'\n"
   + "print(summarize(record))\n"
   + "print('Sample record — structural sample, not an archive entry.')\n";
}
function generate(seed,opts,rnd){
  opts=opts||{}; rnd=rnd||prng(seed);
  var field=opts.field&&FIELDS.indexOf(opts.field)>=0?opts.field:pick(FIELDS,rnd);
  var pool=TOPICS[field]||["General Study"];
  var topic=pick(pool,rnd);
  var id=PREFIX+String(seed).padStart(6,'0');
  return {
    id:id,
    name:topic+' — combinatorics record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A combinatorics record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"combinatorics-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
    _seed:seed
  };
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  if(!new RegExp('^'+PREFIX.replace(/-/g,'\\-')+'\\d{6}$').test(r.id||''))e.push('id');
  if(FIELDS.indexOf(r.field)<0)e.push('field');
  if(!r.src)e.push('src');
  if(!r.demo||!r.demo.program)e.push('demo');
  return {ok:!e.length,errors:e};
}
function driftCheck(record,sample){
  var dups=(sample||[]).filter(function(r){return r&&r.title===record.title&&r.field===record.field;});
  return dups.length?{ok:false,errors:['duplicate topic+field in archive sample']}:{ok:true,errors:[]};
}
var gen={version:'jahdb-combinatorics-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('combinatorics',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
