(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var SLUG="full-working-programs";
var CATS=["algorithms","data","math","networking","productivity","security","text processing","utilities"];
var PREFIX="JAH-FWPROG-";
var KIND="working program";
/* rows: [category, title, description-head] — seeded from the archive */
var B=[
 ["algorithms","Sorting Visualizer","PROGRAM: Sorting Visualizer (sorting visualizer). Bubble sort that prints the array after every swap, so you c"],
 ["networking","HTTP Server","PROGRAM: HTTP Server (http server). A tiny HTTP server (stdlib http.server) that starts in a background thread"],
 ["text processing","Markdown Parser","PROGRAM: Markdown Parser (markdown parser). A small markdown-to-HTML converter handling headers, bold, italic,"],
 ["algorithms","Prime Sieve","PROGRAM: Prime Sieve (prime sieve). The Sieve of Eratosthenes: finds all primes up to N in near-linear time, w"],
 ["data","JSON Formatter","PROGRAM: JSON Formatter (json formatter). Validates JSON and pretty-prints it with sorted keys; reports errors"],
 ["security","Password Generator","PROGRAM: Password Generator (password generator). Generates cryptographically strong passwords with the secret"],
 ["security","Caesar Cipher","PROGRAM: Caesar Cipher (caesar cipher). Encrypts and decrypts text with a Caesar shift, preserving case and le"],
 ["algorithms","Fibonacci","PROGRAM: Fibonacci (fibonacci). Fibonacci three ways: naive recursion, memoized, and iterative — with a speed "],
 ["data","CSV to JSON Converter","PROGRAM: CSV to JSON Converter (csv to json). Converts CSV text to JSON, handling headers, quoted fields, and "],
 ["math","Calculator","PROGRAM: Calculator (calculator). A safe expression evaluator built on the ast module — no eval(), full operat"],
 ["data","Base64 Tool","PROGRAM: Base64 Tool (base64 tool). Encodes and decodes base64, including URL-safe mode and data-URL building."],
 ["text processing","Word Frequency Counter","PROGRAM: Word Frequency Counter (word frequency). Counts word frequencies with stopword filtering and reports "]
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
