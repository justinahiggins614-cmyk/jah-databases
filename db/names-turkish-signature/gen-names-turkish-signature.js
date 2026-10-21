(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var CATS=["signature-study", "framework"];
var PREFIX="JAH-NMTS4-";
/* rows: [category, display name, meaning, origin, ladder_rank] */
var B=[
 ["signature-study","Signature study: Mehmet","Signature study of the public Turkish masculine name Mehmet. Sound: 2 syllables, firm consonant close. Structure: A traditional name of this language.. Recorded","signature-study",2],
 ["signature-study","Signature study: Ayşe","Signature study of the public Turkish feminine name Ayşe. Sound: 2 syllables, open vowels. Structure: A traditional name of this language.. Recorded meaning: Th","signature-study",2],
 ["signature-study","Signature study: Mustafa","Signature study of the public Turkish masculine name Mustafa. Sound: 3 syllables, open vowels. Structure: A traditional name of this language.. Recorded meaning","signature-study",2],
 ["signature-study","Signature study: Fatma","Signature study of the public Turkish feminine name Fatma. Sound: 2 syllables, open vowels. Structure: A traditional name of this language.. Recorded meaning: T","signature-study",2],
 ["framework","The Signature Name-Forge Method","Signature original framework for Turkish names. Forging a new Signature name runs in four passes: sound (two to four syllables that read aloud cleanly), meaning","The Signature Name-Forge Method",3],
 ["framework","Signature Sound-First Naming","Signature original framework for Turkish names. Many strong names are built sound-first: pick a rhythm (STRESS-unstress, or three even beats), fill it with open","Signature Sound-First Naming",3],
 ["framework","Signature Meaning-First Construction","Signature original framework for Turkish names. Meaning-first names start from one plain word — light, stone, river, oath — and grow syllables around it until t","Signature Meaning-First Construction",3],
 ["framework","Signature Brand-Name Creation System","Signature original framework for Turkish names. A Signature brand name must do three jobs: say what it is (or hint it), survive a trademark-style collision chec","Signature Brand-Name Creation System",3],
 ["framework","Signature Product-Naming Framework","Signature original framework for Turkish names. Products in a Signature line share a skeleton: family word + model word + edition mark. The family word never ch","Signature Product-Naming Framework",3],
 ["framework","Signature Place-Naming Framework","Signature original framework for Turkish names. Signature place names are built from landform + story: what the ground does (ford, hill, mouth) plus what happen","Signature Place-Naming Framework",3],
 ["framework","Signature Personal-Naming Framework","Signature original framework for Turkish names. A Signature personal name pairs one given name with one family-style name; the given name is chosen for meaning,","Signature Personal-Naming Framework",3],
 ["framework","Signature Lineage Tagging","Signature original framework for Turkish names. Every Signature name carries a lineage tag naming the earlier Signature name or public name it descends from. A ","Signature Lineage Tagging",3],
 ["framework","Signature Cross-Language Name Porting","Signature original framework for Turkish names. Porting a name into another language keeps the meaning first and the sound second: translate the gloss, then res","Signature Cross-Language Name Porting",3],
 ["framework","Signature Name Validation Checklist","Signature original framework for Turkish names. Before a Signature name ships it must pass the checklist: sayable on first read, one clear meaning, no accidenta","Signature Name Validation Checklist",3],
 ["framework","Signature Naming Taboos","Signature original framework for Turkish names. Signature names avoid four traps: copying a living person's full name, borrowing sacred names as decoration, hid","Signature Naming Taboos",3]
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
  var esc="JAH-NMTS4-".replace(/[.*+?^${}()|[\]\\]/g,'\\$&');
  if(!new RegExp('^'+esc+'\\d{6}$').test(r.id||''))e.push('id');
  if(typeof r.name!=='string'||!r.name.length)e.push('name');
  if(typeof r.meaning!=='string'||!r.meaning.length)e.push('meaning');
  if(typeof r.title!=='string'||!r.title.length)e.push('title');
  if(CATS.indexOf(r.category)<0)e.push('category');
  if(!(r.ladder_rank>=1&&r.ladder_rank<=3))e.push('ladder_rank');
  return {ok:!e.length,errors:e};
}
var gen={version:"jahdb-names-turkish-signature-1.0",generate:generate,validate:validate};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("names-turkish-signature",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
