(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var CATS=["first-name", "surname", "place-name", "naming-convention"];
var PREFIX="JAH-NMN-";
/* rows: [category, display name, meaning, origin, ladder_rank] */
var B=[
 ["first-name","Ram","Ram is a masculine given name in Nepali. Meaning: The hero of the Ramayana..","The hero of the Ramayana.",1],
 ["first-name","Sita","Sita is a feminine given name in Nepali. Meaning: The heroine of the Ramayana..","The heroine of the Ramayana.",1],
 ["first-name","Hari","Hari is a masculine given name in Nepali. Meaning: A name of Vishnu..","A name of Vishnu.",1],
 ["first-name","Gita","Gita is a feminine given name in Nepali. Meaning: Song. The Bhagavad Gita's name.","The Bhagavad Gita's name.",1],
 ["first-name","Prakash","Prakash is a masculine given name in Nepali. Meaning: Light..","Light.",1],
 ["first-name","Sabina","Sabina is a feminine given name in Nepali. Meaning: A popular girls' name..","A popular girls' name.",1],
 ["first-name","Anish","Anish is a masculine given name in Nepali. Meaning: Supreme.. A modern boys' name.","A modern boys' name.",1],
 ["surname","Sharma","Sharma is a Nepali family name. Scholar — a Brahmin title.","Scholar — a Brahmin title.",2],
 ["surname","Thapa","Thapa is a Nepali family name. A Chhetri title.","A Chhetri title.",2],
 ["surname","Gurung","Gurung is a Nepali family name. An ethnic community name.","An ethnic community name.",2],
 ["surname","Rai","Rai is a Nepali family name. An ethnic community name.","An ethnic community name.",2],
 ["place-name","Kathmandu","Kathmandu - From Kasthamandap, the wooden temple.","From Kasthamandap, the wooden temple.",2],
 ["place-name","Pokhara","Pokhara - The lakeside city.","The lakeside city.",2],
 ["naming-convention","Caste and ethnic surnames","Caste and ethnic surnames: Sharma, Thapa, Gurung, and Rai mark community.","Sharma, Thapa, Gurung, and Rai mark community.",3],
 ["naming-convention","Given + family order","Given + family order: Nepali names run given name first, family name last.","Nepali names run given name first, family name last.",3]
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
  var esc="JAH-NMN-".replace(/[.*+?^${}()|[\]\\]/g,'\\$&');
  if(!new RegExp('^'+esc+'\\d{6}$').test(r.id||''))e.push('id');
  if(typeof r.name!=='string'||!r.name.length)e.push('name');
  if(typeof r.meaning!=='string'||!r.meaning.length)e.push('meaning');
  if(typeof r.title!=='string'||!r.title.length)e.push('title');
  if(CATS.indexOf(r.category)<0)e.push('category');
  if(!(r.ladder_rank>=1&&r.ladder_rank<=3))e.push('ladder_rank');
  return {ok:!e.length,errors:e};
}
var gen={version:"jahdb-names-nepali-1.0",generate:generate,validate:validate};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("names-nepali",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
