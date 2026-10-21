(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var SLUG="full-working-programs-signature";
var CATS=["signature"];
var PREFIX="JAH-FWPROG-S-";
var KIND="working program";
/* rows: [category, title, description-head] — seeded from the archive */
var B=[
 ["signature","Maker-Mark Stamper","PROGRAM: Maker-Mark Stamper (maker-mark stamper). Stamps any text with a deterministic SHA-256-based Signature"],
 ["signature","Spec ID Generator","PROGRAM: Spec ID Generator (spec-id generator). Generates and validates JAH-SPEC-###### deterministic IDs from"],
 ["signature","Lineage Chain Builder","PROGRAM: Lineage Chain Builder (lineage chain). Builds parent/child lineage chains between records and walks t"],
 ["signature","Hash ID Coder","PROGRAM: Hash ID Coder (hash id coder). Encodes any string into a short deterministic ID using SHA-256, with c"],
 ["signature","Boundless Seed Generator","PROGRAM: Boundless Seed Generator (seed generator). A deterministic seeded PRNG (mulberry32-style) — same seed"],
 ["signature","Record Validator","PROGRAM: Record Validator (record validator). Validates database records against a schema: required fields, ID"],
 ["signature","Text Banner Maker","PROGRAM: Text Banner Maker (banner maker). Renders big ASCII-art banners from text with a 5x5 block font. This"],
 ["signature","Word Scrambler","PROGRAM: Word Scrambler (word scrambler). Scrambles word interiors (typoglycemia) while keeping first/last let"],
 ["signature","Number to Words","PROGRAM: Number to Words (number to words). Converts integers to English words (0 to 999,999). This record IS "],
 ["signature","Morse Code Translator","PROGRAM: Morse Code Translator (morse code). Encodes text to International Morse code and decodes it back. Thi"],
 ["signature","Roman Numerals","PROGRAM: Roman Numerals (roman numerals). Converts between integers and Roman numerals (1-3999), both directio"],
 ["signature","Pig Latin Translator","PROGRAM: Pig Latin Translator (pig latin). Translates English to Pig Latin and back for simple words. This rec"]
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
