(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var SLUG="program-mixes";
var CATS=["algorithms","data","games","math","networking","productivity","security","text processing","web"];
var PREFIX="JAH-PMIX-";
var KIND="program mix";
/* rows: [category, title, description-head] — seeded from the archive */
var B=[
 ["web","Markdown Web Server","PROGRAM: Markdown Web Server (['http server', 'markdown parser']). Serves rendered markdown over HTTP: the mar"],
 ["security","Encrypted Password Vault","PROGRAM: Encrypted Password Vault (['caesar cipher', 'password generator']). Generates strong passwords and st"],
 ["algorithms","Sort Then Search","PROGRAM: Sort Then Search (['sorting visualizer', 'binary search']). Sorts data with bubble sort, then binary-"],
 ["data","Data Format Converter","PROGRAM: Data Format Converter (['json formatter', 'csv to json']). Converts CSV to JSON and pretty-prints the"],
 ["math","Prime Fibonacci Finder","PROGRAM: Prime Fibonacci Finder (['fibonacci', 'prime sieve']). Finds Fibonacci numbers that are also prime, u"],
 ["text processing","Text Analyzer","PROGRAM: Text Analyzer (['word frequency', 'palindrome checker']). Analyzes text: word frequencies plus which "],
 ["web","Data URL Builder","PROGRAM: Data URL Builder (['base64 tool', 'url parser']). Builds data: URLs from content and parses them back"],
 ["math","Engineering Calculator","PROGRAM: Engineering Calculator (['calculator', 'unit converter']). Safe expression evaluation applied to unit"],
 ["games","Random Maze Sampler","PROGRAM: Random Maze Sampler (['maze generator', 'dice statistics']). Uses dice rolls to pick maze seeds, then"],
 ["productivity","Pretty Todo Store","PROGRAM: Pretty Todo Store (['todo list', 'json formatter']). To-do list persisted as pretty-printed JSON — hu"],
 ["algorithms","Sort Benchmark","PROGRAM: Sort Benchmark (['stopwatch', 'sorting visualizer']). Benchmarks bubble sort vs Python's built-in sor"],
 ["text processing","JSON Doc Generator","PROGRAM: JSON Doc Generator (['markdown parser', 'json formatter']). Turns a JSON record into a markdown docum"]
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
