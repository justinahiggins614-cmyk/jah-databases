(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var SLUG="math-proof-database";
var CATS=["index","proof"];
var PREFIX="JAH-MPROOF-";
var KIND="math proof";
/* rows: [category, title, description-head] — seeded from the archive */
var B=[
 ["proof","Proof of the Quadratic Formula","PROOF: Quadratic formula. Statement: For real numbers a, b, c with a != 0, the solutions of ax^2 + bx + c = 0 "],
 ["proof","Sum of a Geometric Series","PROOF: Geometric series sum. Statement: For r != 1, 1 + r + r^2 + ... + r^(n-1) = (1 - r^n)/(1 - r). The subtr"],
 ["proof","Sum of the First n Natural Numbers","PROOF: Arithmetic series. Statement: 1 + 2 + ... + n = n(n+1)/2. Gauss's pairing argument, allegedly discovere"],
 ["proof","Pythagorean Theorem (Algebraic Proof)","PROOF: Pythagorean theorem. Statement: In a right triangle with legs a, b and hypotenuse c: a^2 + b^2 = c^2. O"],
 ["proof","Power Rule for Derivatives","PROOF: Power rule. Statement: For positive integer n, d/dx[x^n] = n*x^(n-1). The binomial expansion does the h"],
 ["proof","Irrationality of sqrt(2)","PROOF: sqrt(2) is irrational. Statement: There are no integers p, q (q != 0) with (p/q)^2 = 2. A proof by cont"],
 ["proof","Infinitude of Primes (Euclid)","PROOF: Infinite primes. Statement: There are infinitely many prime numbers. Euclid's proof is constructive: it"],
 ["proof","Sum of Squares Formula","PROOF: Sum of squares. Statement: 1^2 + 2^2 + ... + n^2 = n(n+1)(2n+1)/6. Induction handles it cleanly; the al"],
 ["proof","Binomial Theorem","PROOF: Binomial theorem. Statement: (x+y)^n = sum_{k=0}^{n} C(n,k) x^(n-k) y^k for nonnegative integer n. The "],
 ["proof","Euler's Identity","PROOF: Euler's identity. Statement: e^(i*pi) + 1 = 0. The series proof of Euler's formula is the deep part; th"],
 ["proof","AM-GM Inequality (Two Variables)","PROOF: AM >= GM. Statement: For a, b >= 0: (a+b)/2 >= sqrt(ab). Equality holds exactly when a = b — visible ri"],
 ["proof","Derivative of e^x","PROOF: d/dx e^x = e^x. Statement: The function e^x is its own derivative. This is really the DEFINITION of e d"]
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
    src:"public-harvest",
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
