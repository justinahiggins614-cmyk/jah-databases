(function(){'use strict';
/* JAH The Combinatorics Signature Database generator — jahdb-combinatorics-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-COMBS-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "What Combinatorics Is (Signature Edition) - Foundations",
  "The Addition and Multiplication Principles (Signature Edition) - Foundations",
  "The Pigeonhole Principle (Signature Edition) - Foundations",
  "Permutations: Counting Ordered Arrangements (Signature Edition) - Foundations",
  "Combinations: Choosing Without Order (Signature Edition) - Foundations",
  "Pascal's Triangle and the Binomial Theorem (Signature Edition) - Foundations",
  "Permutations with Repetition and Multinomial Coefficients (Signature Edition) - Foundations",
  "Combinations with Repetition: Stars and Bars (Signature Edition) - Foundations"
 ],
 "Compounded": [
  "Binomial Identities: Algebraic and Combinatorial Proofs (Signature Edition) - Compounded",
  "The Inclusion-Exclusion Principle (Signature Edition) - Compounded",
  "Derangements: Permutations with No Fixed Points (Signature Edition) - Compounded",
  "The Bijection Principle and Combinatorial Proofs (Signature Edition) - Compounded",
  "Double Counting: One Answer, Two Ways (Signature Edition) - Compounded",
  "Integer Partitions: Breaking Numbers Apart (Signature Edition) - Compounded",
  "Set Partitions and Stirling Numbers of the Second Kind (Signature Edition) - Compounded",
  "Permutation Cycles and Stirling Numbers of the First Kind (Signature Edition) - Compounded",
  "Lattice Paths and the Reflection Principle (Signature Edition) - Compounded",
  "Recurrence Relations: Sequences Defined by Their Past (Signature Edition) - Compounded",
  "Solving Linear Recurrences: The Characteristic Equation (Signature Edition) - Compounded",
  "Ordinary Generating Functions (Signature Edition) - Compounded",
  "Exponential Generating Functions (Signature Edition) - Compounded",
  "The Twelvefold Way: Balls into Boxes (Signature Edition) - Compounded",
  "Catalan Numbers: The Ubiquitous Sequence (Signature Edition) - Compounded"
 ],
 "Advanced": [
  "Bell Numbers and the Partitions of a Set (Signature Edition) - Advanced",
  "Partitions of Integers: Euler's Theorems (Signature Edition) - Advanced",
  "Graph Theory as Counting: Walks and the Handshaking Lemma (Signature Edition) - Advanced",
  "Trees and Cayley's Formula (Signature Edition) - Advanced",
  "Eulerian Trails and Hamiltonian Cycles (Signature Edition) - Advanced",
  "Ramsey Theory: Order Forced from Chaos (Signature Edition) - Advanced",
  "Block Designs and the Fano Plane (Signature Edition) - Advanced",
  "Latin Squares and Orthogonal Arrays (Signature Edition) - Advanced",
  "Combinatorial Games: Winning Strategies (Signature Edition) - Advanced",
  "Extremal Combinatorics: Turan's Theorem (Signature Edition) - Advanced",
  "The Probabilistic Method: Proving by Random Choice (Signature Edition) - Advanced",
  "Polya Enumeration: Counting Up to Symmetry (Signature Edition) - Advanced",
  "Algebraic Combinatorics: Symmetric Functions (Signature Edition) - Advanced"
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
var gen={version:'jahdb-combinatorics-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('combinatorics-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
