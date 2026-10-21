(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var SLUG="program-mixes-signature";
var CATS=["signature"];
var PREFIX="JAH-PMIX-S-";
var KIND="program mix";
/* rows: [category, title, description-head] — seeded from the archive */
var B=[
 ["signature","Stamped ID Registry","PROGRAM: Stamped ID Registry (['maker-mark stamper', 'spec-id generator']). Mints spec IDs and immediately sta"],
 ["signature","Hashed Lineage","PROGRAM: Hashed Lineage (['lineage chain', 'hash id coder']). Lineage chains where every node carries a conten"],
 ["signature","Seeded Random Suite","PROGRAM: Seeded Random Suite (['seed generator', 'coin flip']). Deterministic randomness lab: the boundless PR"],
 ["signature","Code Talker","PROGRAM: Code Talker (['morse code', 'pig latin']). Double-encoded secret messages: Pig Latin first, then Mors"],
 ["signature","Number Systems Lab","PROGRAM: Number Systems Lab (['roman numerals', 'number to words']). Displays numbers three ways: digits, Roma"],
 ["signature","Logo Maker","PROGRAM: Logo Maker (['banner maker', 'acronym maker']). Builds a text logo: acronym rendered as an ASCII bann"],
 ["signature","Word Game Arcade","PROGRAM: Word Game Arcade (['hangman', 'word scrambler']). Word-game arcade: unscramble challenge plus scripte"],
 ["signature","Game Suite","PROGRAM: Game Suite (['rps game', 'coin flip']). Two-game suite: rock-paper-scissors tournament plus coin-flip"],
 ["signature","School Math Kit","PROGRAM: School Math Kit (['grade calculator', 'tip calculator']). Everyday math kit: course grades and fair b"],
 ["signature","Launch Sequence","PROGRAM: Launch Sequence (['countdown', 'fizzbuzz']). Countdown that calls out FizzBuzz milestones on the way "],
 ["signature","Archive Tools","PROGRAM: Archive Tools (['record validator', 'lineage chain']). Validates records, then links the valid ones i"],
 ["signature","Provenance Stamper","PROGRAM: Provenance Stamper (['maker-mark stamper', 'hash id coder']). Stamps content with both a maker mark a"]
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
