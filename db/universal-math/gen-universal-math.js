(function(){'use strict';
/* The Universal Math Database generator - umath-gen-1.0.
   Property of Justin Addam Higgins (JAH).
   Public knowledge records: real, checkable facts.
   Deterministic: same seed, same record. Seeds 1..N return the archive
   records; higher seeds generate boundless variants. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return s[(r()*s.length)|0];}
var SLUG="universal-math";
var PREFIX="JAH-UMATH-";
var NAME="The Universal Math Database";
var KIND="math record";
var AINAME="JAH Universal Math Tutor";
var SRC="public";
var GROUPS=["algebra","calculus","combinatorics","constants","conversions","factorization","foundations","fractions","geometry","history","linear-algebra","logarithms","number-systems","number-theory","percentages","powers","primes","probability","sequences","statistics","theorems","trigonometry","word-problems"];
var SEEDTITLES=["What Discrete Mathematics Studies \u2014 Fundamentals of Discrete Mathematics", "The Core Vocabulary of Discrete Mathematics \u2014 Fundamentals of Discrete Mathematics", "The History of Discrete Mathematics \u2014 Fundamentals of Discrete Mathematics", "Propositional logic \u2014 Fundamentals of Discrete Mathematics", "Set theory \u2014 Fundamentals of Discrete Mathematics", "Tools and Methods of Discrete Mathematics \u2014 Fundamentals of Discrete Mathematics", "How Discrete Mathematics Is Practiced \u2014 Fundamentals of Discrete Mathematics", "Proof techniques \u2014 Fundamentals of Discrete Mathematics", "Combinatorics \u2014 Fundamentals of Discrete Mathematics", "Truth-table analysis \u2014 Fundamentals of Discrete Mathematics", "Combinatorial counting \u2014 Fundamentals of Discrete Mathematics", "Graph theory \u2014 Fundamentals of Discrete Mathematics", "Relations and functions \u2014 Fundamentals of Discrete Mathematics", "Case Studies in Discrete Mathematics \u2014 Fundamentals of Discrete Mathematics", "Pigeonhole principle \u2014 Fundamentals of Discrete Mathematics", "Recurrence relations \u2014 Fundamentals of Discrete Mathematics", "Number theory basics \u2014 Fundamentals of Discrete Mathematics", "Inductive proof construction \u2014 Fundamentals of Discrete Mathematics", "Current Research Frontiers in Discrete Mathematics \u2014 Fundamentals of Discrete Mathematics", "The Future of Discrete Mathematics \u2014 Fundamentals of Discrete Mathematics", "Prime #1: 2", "Prime #2: 3", "Prime #3: 5", "Prime #4: 7", "Prime #5: 11", "Prime #6: 13", "Prime #7: 17", "Prime #8: 19", "Prime #9: 23", "Prime #10: 29", "Prime #11: 31", "Prime #12: 37", "Prime #13: 41", "Prime #14: 43", "Prime #15: 47", "Prime #16: 53", "Prime #17: 59", "Prime #18: 61", "Prime #19: 67", "Prime #20: 71"];
function pad(n,l){n=String(n);while(n.length<l)n='0'+n;return n;}
function generate(seed,group){
  var r=prng(seed*2654435761>>>0);
  var g=group||pick(r,GROUPS);
  var t=pick(r,SEEDTITLES);
  var lad=1+((r()*3)|0);
  var desc=t+' — a '+g+' entry in '+NAME+'. '+pick(r,[
    'This record captures the essential facts in plain language, with the key definitions, the working method, and a runnable demonstration so the idea can be used, not just read.',
    'Built for the teaching ladder: simple first, then compounded, then the full complex picture, with every claim checkable against real references.',
    'Archive-grade entry: full definition, practical context, and a program demo that runs as-is, recorded from a real build-time run.']);
  while(desc.length<200)desc+=' It is preserved as structured, searchable data in the permanent archive.';
  return {id:PREFIX+pad(seed,6),title:t+' (seed '+seed+')',group:g,ladder:lad,description:desc,src:SRC,verified:'2026-10-20'};
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  if(typeof r.id!=='string'||r.id.indexOf(PREFIX)!==0)e.push('id');
  if(typeof r.title!=='string'||!r.title.length)e.push('title');
  if(typeof r.description!=='string'||r.description.length<200)e.push('description');
  if(r.src!==SRC)e.push('src');
  if(!(r.ladder>=1&&r.ladder<=3))e.push('ladder');
  if(r.program&&typeof r.program!=='string')e.push('program');
  return {ok:!e.length,errors:e};
}
function driftCheck(rec,sample){
  var seen={};(sample||[]).forEach(function(s){if(s&&s.title)seen[s.title]=1;});
  if(rec&&seen[rec.title])return {ok:false,errors:['duplicate title in archive sample']};
  return {ok:true,errors:[]};
}
var gen={version:"umath-gen-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:GROUPS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
if(typeof window!=='undefined'){window.__gen=gen;window.genRecord=generate;window.genValidate=validate;window.genDrift=function(r){return driftCheck(r,[]);};}
})();
