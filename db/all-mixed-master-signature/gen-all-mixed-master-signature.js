(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var SLUG="all-mixed-master-signature";
var CATS=["signature"];
var PREFIX="JAH-ALLMIX-S-";
var KIND="master program";
/* rows: [category, title, description-head] — seeded from the archive */
var B=[
 ["signature","Signature Toolkit","PROGRAM: Signature Toolkit (['maker-mark stamper', 'spec-id generator', 'lineage chain', 'hash id coder']). Th"],
 ["signature","Archive Manager","PROGRAM: Archive Manager (['record validator', 'lineage chain', 'seed generator']). Manages archive records: v"],
 ["signature","Wordplay Studio","PROGRAM: Wordplay Studio (['pig latin', 'word scrambler', 'morse code', 'banner maker', 'acronym maker']). The"],
 ["signature","Number Systems Lab","PROGRAM: Number Systems Lab (['roman numerals', 'number to words', 'fizzbuzz', 'coin flip']). Numbers every wa"],
 ["signature","Game Arcade","PROGRAM: Game Arcade (['hangman', 'rps game', 'coin flip', 'countdown']). Signature game arcade: hangman, RPS,"],
 ["signature","Crypto Lite","PROGRAM: Crypto Lite (['morse code', 'hash id coder', 'maker-mark stamper']). Lightweight crypto: hashes, mark"],
 ["signature","Classroom Suite","PROGRAM: Classroom Suite (['grade calculator', 'fizzbuzz', 'countdown', 'rps game']). Teacher's kit: grades, w"],
 ["signature","Registry System","PROGRAM: Registry System (['spec-id generator', 'lineage chain', 'record validator', 'maker-mark stamper']). F"],
 ["signature","Random Lab","PROGRAM: Random Lab (['seed generator', 'coin flip', 'word scrambler']). Deterministic randomness lab: seeded "],
 ["signature","Text Tools","PROGRAM: Text Tools (['banner maker', 'acronym maker', 'pig latin', 'morse code']). Text transformer bench: ba"],
 ["signature","Provenance Suite","PROGRAM: Provenance Suite (['maker-mark stamper', 'hash id coder', 'lineage chain', 'record validator']). Prov"],
 ["signature","Math Fun Pack","PROGRAM: Math Fun Pack (['roman numerals', 'fizzbuzz', 'number to words', 'grade calculator']). Math you can p"]
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
