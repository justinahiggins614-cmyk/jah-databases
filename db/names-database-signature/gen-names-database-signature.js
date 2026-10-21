(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var CATS=["framework"];
var PREFIX="JAH-NAMES-S-";
/* rows: [category, display name, meaning, origin, ladder_rank] */
var B=[
 ["framework","The Signature Naming Philosophy","Signature original. A name is a small machine with three moving parts: sound that survives being shouted across a room, meaning that survives being explained in","The Signature Naming Philosophy",1],
 ["framework","The Signature Name-Forge","Signature original. The Name-Forge is the working method behind every Signature name: gather seed words, shape syllables, test the sound aloud, fix one meaning,","The Signature Name-Forge",1],
 ["framework","Signature Personal Names","Signature original. A Signature personal name is built for one bearer: a given name chosen for its meaning plus a lineage name that records descent. Both glosse","Signature Personal Names",2],
 ["framework","Signature Family-Style Names","Signature original. Signature family-style names work like surnames but are earned or chosen rather than inherited: they may record a craft, a place, or a found","Signature Family-Style Names",2],
 ["framework","Signature Brand Names","Signature original. Signature brand names are forged, not found: clarity first, sayability second, collision check third. Every brand name in the Signature line","Signature Brand Names",2],
 ["framework","Signature Product-Line Naming","Signature original. A Signature product line names its children on a skeleton: family word, model word, edition number. The family word is permanent, the model ","Signature Product-Line Naming",2],
 ["framework","Signature Place Names","Signature original. Signature place names are built landform-first: the ground's shape plus the story of the place, in that order. Invented places are labeled i","Signature Place Names",2],
 ["framework","Signature Project Codenames","Signature original. Signature codenames are short, pronounceable, and meaningless on purpose — they identify a project without describing it, so a leaked codena","Signature Project Codenames",3],
 ["framework","Signature Names for the Million-File March","Signature original. As the databases march toward a million records, Signature naming keeps the archive navigable: one naming skeleton per database family, edit","Signature Names for the Million-File March",3],
 ["framework","Signature Name Porting Across Languages","Signature original. When a Signature name crosses into another language, the meaning is ported first and the sound reshaped second, with source and port recorde","Signature Name Porting Across Languages",3],
 ["framework","Signature Lineage and Edition Marks","Signature original. Every Signature name carries two tags: lineage (what it descends from) and edition (public or Signature). The tags are part of the record, n","Signature Lineage and Edition Marks",3],
 ["framework","Signature Naming Taboos","Signature original. The forge refuses: copying a living person's full name, dressing a joke as a formal name, borrowing sacred names as decoration, and filing a","Signature Naming Taboos",3],
 ["framework","Signature Sound Patterns","Signature original. Signature names favor two-beat and three-beat rhythms with open vowels and clean consonant edges. The pattern is tested by reading the name ","Signature Sound Patterns",3],
 ["framework","Signature Meaning Ledger","Signature original. Every Signature name's meaning is entered in the ledger in plain words, one line per name. The ledger is the check against drift: if the mea","Signature Meaning Ledger",3],
 ["framework","The Signature Master Name Index","Signature original. The master index is the map of all Signature names: every name, its meaning, its lineage, its edition mark, in one searchable list. New name","The Signature Master Name Index",3]
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
  var esc="JAH-NAMES-S-".replace(/[.*+?^${}()|[\]\\]/g,'\\$&');
  if(!new RegExp('^'+esc+'\\d{6}$').test(r.id||''))e.push('id');
  if(typeof r.name!=='string'||!r.name.length)e.push('name');
  if(typeof r.meaning!=='string'||!r.meaning.length)e.push('meaning');
  if(typeof r.title!=='string'||!r.title.length)e.push('title');
  if(CATS.indexOf(r.category)<0)e.push('category');
  if(!(r.ladder_rank>=1&&r.ladder_rank<=3))e.push('ladder_rank');
  return {ok:!e.length,errors:e};
}
var gen={version:"jahdb-names-database-signature-1.0",generate:generate,validate:validate};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("names-database-signature",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
