(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var SLUG="math-proof-database-signature";
var CATS=["index","proof"];
var PREFIX="JAH-MPROOF-S-";
var KIND="math proof";
/* rows: [category, title, description-head] — seeded from the archive */
var B=[
 ["proof","Quadratic Formula via Completing the Square (Geometric View)","PROOF: Quadratic formula. Statement: For a != 0, ax^2 + bx + c = 0 has solutions x = (-b +- sqrt(b^2-4ac))/(2a"],
 ["proof","Geometric Series via Telescoping Difference","PROOF: Geometric series sum. Statement: For r != 1: 1 + r + ... + r^(n-1) = (1-r^n)/(1-r). Signature-composed "],
 ["proof","Triangular Numbers by Double Counting","PROOF: Arithmetic series. Statement: 1 + 2 + ... + n = n(n+1)/2. Signature-composed exposition: a counting pro"],
 ["proof","Pythagoras via Similar Triangles","PROOF: Pythagorean theorem. Statement: For right triangle legs a, b, hypotenuse c: a^2 + b^2 = c^2. Signature-"],
 ["proof","Power Rule via the Binomial Lens","PROOF: Power rule. Statement: For positive integer n: d/dx[x^n] = n*x^(n-1). Signature-composed exposition: zo"],
 ["proof","Irrationality of sqrt(2) by Infinite Descent","PROOF: sqrt(2) is irrational. Statement: No integers p, q give (p/q)^2 = 2. Signature-composed exposition: Fer"],
 ["proof","Euclid's Proof, Optimized","PROOF: Infinite primes. Statement: Infinitely many primes exist. Signature-composed exposition with the remain"],
 ["proof","Sum of Squares via Stacked Cubes","PROOF: Sum of squares. Statement: 1^2 + ... + n^2 = n(n+1)(2n+1)/6. Signature-composed exposition: the inducti"],
 ["proof","Binomial Theorem by Induction","PROOF: Binomial theorem. Statement: (x+y)^n = sum C(n,k) x^(n-k) y^k. Signature-composed exposition: induction"],
 ["proof","Euler's Identity from Series","PROOF: Euler's identity. Statement: e^(i*pi) + 1 = 0. Signature-composed exposition: the series split shown te"],
 ["proof","AM-GM by Rearrangement","PROOF: AM >= GM. Statement: For a, b >= 0: (a+b)/2 >= sqrt(ab). Signature-composed exposition: center-and-devi"],
 ["proof","Why e^x Is Its Own Derivative, Intuitively","PROOF: d/dx e^x = e^x. Statement: d/dx[e^x] = e^x. Signature-composed exposition: intuition first, the same ri"]
];
function generate(seed,opts,rnd){
  opts=opts||{};rnd=rnd||prng(seed);
  var cat=opts.category||pick(CATS,rnd);
  var pool=B.filter(function(b){return b[0]===cat;});
  var b=pick(pool.length?pool:B,rnd);
  var id=PREFIX+String(seed).padStart(6,'0');
  return {id:id,title:b[1],description:b[2],category:cat,
    ladder_rank:1+((rnd()*3)|0),
    demo:'#!/usr/bin/env python3\nprint('+JSON.stringify('demo for '+b[1])+')\n',
    provenance:'Boundless generator jahdb-'+SLUG+'-1.0; seed '+seed+'.',
    last_verified:'2026-10-21',
    src:"signature-generated-completion",
    _seed:seed};
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  var rx=new RegExp('^'+PREFIX.replace(/[.*+?^${}()|[\]\\]/g,'\\$&')+'\\d{6}$');
  if(!rx.test(r.id||''))e.push('id');
  if(typeof r.title!=='string'||!r.title.length)e.push('title');
  if(typeof r.description!=='string'||!r.description.length)e.push('description');
  if(CATS.indexOf(r.category)<0)e.push('category');
  if(!(r.ladder_rank>=1&&r.ladder_rank<=3))e.push('ladder_rank');
  if(typeof r.demo!=='string'||!r.demo.length)e.push('demo');
  if(r.last_verified!=='2026-10-21')e.push('last_verified');
  return {ok:!e.length,errors:e};
}
function driftCheck(rec,sample){
  var e=[];
  for(var i=0;i<sample.length;i++){
    if(sample[i]&&sample[i].title===rec.title&&sample[i].id!==rec.id){e.push('near-duplicate title');break;}
  }
  return {ok:!e.length,errors:e};
}
var gen={version:'jahdb-'+SLUG+'-1.0',generate:generate,validate:validate,driftCheck:driftCheck};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
