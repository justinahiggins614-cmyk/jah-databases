(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var CATS=["signature-study", "framework"];
var PREFIX="JAH-NMDS2-";
/* rows: [category, display name, meaning, origin, ladder_rank] */
var B=[
 ["signature-study","Signature study: Jan","Signature study of the public Dutch masculine name Jan. Sound: 1 syllables, firm consonant close. Structure: The Dutch form of John.. Recorded meaning: God is g","signature-study",2],
 ["signature-study","Signature study: Maria","Signature study of the public Dutch feminine name Maria. Sound: 2 syllables, open vowels. Structure: A traditional name of this language.. Recorded meaning: Bel","signature-study",2],
 ["signature-study","Signature study: Pieter","Signature study of the public Dutch masculine name Pieter. Sound: 2 syllables, firm consonant close. Structure: The Dutch form of Peter.. Recorded meaning: Ston","signature-study",2],
 ["signature-study","Signature study: Anna","Signature study of the public Dutch feminine name Anna. Sound: 2 syllables, open vowels. Structure: A traditional name of this language.. Recorded meaning: Grac","signature-study",2],
 ["framework","The Signature Name-Forge Method","Signature original framework for Dutch names. Forging a new Signature name runs in four passes: sound (two to four syllables that read aloud cleanly), meaning (","The Signature Name-Forge Method",3],
 ["framework","Signature Sound-First Naming","Signature original framework for Dutch names. Many strong names are built sound-first: pick a rhythm (STRESS-unstress, or three even beats), fill it with open v","Signature Sound-First Naming",3],
 ["framework","Signature Meaning-First Construction","Signature original framework for Dutch names. Meaning-first names start from one plain word — light, stone, river, oath — and grow syllables around it until the","Signature Meaning-First Construction",3],
 ["framework","Signature Brand-Name Creation System","Signature original framework for Dutch names. A Signature brand name must do three jobs: say what it is (or hint it), survive a trademark-style collision check,","Signature Brand-Name Creation System",3],
 ["framework","Signature Product-Naming Framework","Signature original framework for Dutch names. Products in a Signature line share a skeleton: family word + model word + edition mark. The family word never chan","Signature Product-Naming Framework",3],
 ["framework","Signature Place-Naming Framework","Signature original framework for Dutch names. Signature place names are built from landform + story: what the ground does (ford, hill, mouth) plus what happened","Signature Place-Naming Framework",3],
 ["framework","Signature Personal-Naming Framework","Signature original framework for Dutch names. A Signature personal name pairs one given name with one family-style name; the given name is chosen for meaning, t","Signature Personal-Naming Framework",3],
 ["framework","Signature Lineage Tagging","Signature original framework for Dutch names. Every Signature name carries a lineage tag naming the earlier Signature name or public name it descends from. A na","Signature Lineage Tagging",3],
 ["framework","Signature Cross-Language Name Porting","Signature original framework for Dutch names. Porting a name into another language keeps the meaning first and the sound second: translate the gloss, then resha","Signature Cross-Language Name Porting",3],
 ["framework","Signature Name Validation Checklist","Signature original framework for Dutch names. Before a Signature name ships it must pass the checklist: sayable on first read, one clear meaning, no accidental ","Signature Name Validation Checklist",3],
 ["framework","Signature Naming Taboos","Signature original framework for Dutch names. Signature names avoid four traps: copying a living person's full name, borrowing sacred names as decoration, hidin","Signature Naming Taboos",3]
];
function generate(seed,opts,rnd){
  opts=opts||{};rnd=rnd||prng(seed);
  var cat=opts.category||pick(CATS,rnd);
  var pool=B.filter(function(b){return b[0]===cat;});
  var b=pick(pool.length?pool:B,rnd);
  var id=PREFIX+String(seed).padStart(6,'0');
  return {id:id,name:b[1],title:(b[1]+' \u2014 '+b[2]).slice(0,80),meaning:b[2],origin:b[3],category:cat,ladder_rank:b[4],_seed:seed};
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  var esc="JAH-NMDS2-".replace(/[.*+?^${}()|[\]\\]/g,'\\$&');
  if(!new RegExp('^'+esc+'\\d{6}$').test(r.id||''))e.push('id');
  if(typeof r.name!=='string'||!r.name.length)e.push('name');
  if(typeof r.meaning!=='string'||!r.meaning.length)e.push('meaning');
  if(typeof r.title!=='string'||!r.title.length)e.push('title');
  if(CATS.indexOf(r.category)<0)e.push('category');
  if(!(r.ladder_rank>=1&&r.ladder_rank<=3))e.push('ladder_rank');
  return {ok:!e.length,errors:e};
}
var gen={version:"jahdb-names-dutch-signature-1.0",generate:generate,validate:validate};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("names-dutch-signature",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
