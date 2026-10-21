(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var CATS=["signature-study", "framework"];
var PREFIX="JAH-NMIS3-";
/* rows: [category, display name, meaning, origin, ladder_rank] */
var B=[
 ["signature-study","Signature study: Chiamaka","Signature study of the public Igbo feminine name Chiamaka. Sound: 3 syllables, open vowels. Structure: Chi (God) + amaka (beautiful).. Recorded meaning: God is ","signature-study",2],
 ["signature-study","Signature study: Obinna","Signature study of the public Igbo masculine name Obinna. Sound: 3 syllables, open vowels. Structure: Obi (heart) + nna (father).. Recorded meaning: Father's he","signature-study",2],
 ["signature-study","Signature study: Adaeze","Signature study of the public Igbo feminine name Adaeze. Sound: 3 syllables, open vowels. Structure: Ada (daughter) + eze (king).. Recorded meaning: King's daug","signature-study",2],
 ["signature-study","Signature study: Ngozi","Signature study of the public Igbo unisex name Ngozi. Sound: 2 syllables, open vowels. Structure: Unisex.. Recorded meaning: Blessing. Naming power: the name is","signature-study",2],
 ["framework","The Signature Name-Forge Method","Signature original framework for Igbo names. Forging a new Signature name runs in four passes: sound (two to four syllables that read aloud cleanly), meaning (o","The Signature Name-Forge Method",3],
 ["framework","Signature Sound-First Naming","Signature original framework for Igbo names. Many strong names are built sound-first: pick a rhythm (STRESS-unstress, or three even beats), fill it with open vo","Signature Sound-First Naming",3],
 ["framework","Signature Meaning-First Construction","Signature original framework for Igbo names. Meaning-first names start from one plain word — light, stone, river, oath — and grow syllables around it until the ","Signature Meaning-First Construction",3],
 ["framework","Signature Brand-Name Creation System","Signature original framework for Igbo names. A Signature brand name must do three jobs: say what it is (or hint it), survive a trademark-style collision check, ","Signature Brand-Name Creation System",3],
 ["framework","Signature Product-Naming Framework","Signature original framework for Igbo names. Products in a Signature line share a skeleton: family word + model word + edition mark. The family word never chang","Signature Product-Naming Framework",3],
 ["framework","Signature Place-Naming Framework","Signature original framework for Igbo names. Signature place names are built from landform + story: what the ground does (ford, hill, mouth) plus what happened ","Signature Place-Naming Framework",3],
 ["framework","Signature Personal-Naming Framework","Signature original framework for Igbo names. A Signature personal name pairs one given name with one family-style name; the given name is chosen for meaning, th","Signature Personal-Naming Framework",3],
 ["framework","Signature Lineage Tagging","Signature original framework for Igbo names. Every Signature name carries a lineage tag naming the earlier Signature name or public name it descends from. A nam","Signature Lineage Tagging",3],
 ["framework","Signature Cross-Language Name Porting","Signature original framework for Igbo names. Porting a name into another language keeps the meaning first and the sound second: translate the gloss, then reshap","Signature Cross-Language Name Porting",3],
 ["framework","Signature Name Validation Checklist","Signature original framework for Igbo names. Before a Signature name ships it must pass the checklist: sayable on first read, one clear meaning, no accidental t","Signature Name Validation Checklist",3],
 ["framework","Signature Naming Taboos","Signature original framework for Igbo names. Signature names avoid four traps: copying a living person's full name, borrowing sacred names as decoration, hiding","Signature Naming Taboos",3]
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
  var esc="JAH-NMIS3-".replace(/[.*+?^${}()|[\]\\]/g,'\\$&');
  if(!new RegExp('^'+esc+'\\d{6}$').test(r.id||''))e.push('id');
  if(typeof r.name!=='string'||!r.name.length)e.push('name');
  if(typeof r.meaning!=='string'||!r.meaning.length)e.push('meaning');
  if(typeof r.title!=='string'||!r.title.length)e.push('title');
  if(CATS.indexOf(r.category)<0)e.push('category');
  if(!(r.ladder_rank>=1&&r.ladder_rank<=3))e.push('ladder_rank');
  return {ok:!e.length,errors:e};
}
var gen={version:"jahdb-names-igbo-signature-1.0",generate:generate,validate:validate};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("names-igbo-signature",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
