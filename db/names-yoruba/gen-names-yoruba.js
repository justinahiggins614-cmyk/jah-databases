(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var CATS=["first-name", "surname", "place-name", "naming-convention"];
var PREFIX="JAH-NMY-";
/* rows: [category, display name, meaning, origin, ladder_rank] */
var B=[
 ["first-name","Adeyemi","Adeyemi is a masculine given name in Yoruba. Meaning: The crown befits me. Ade (crown) + yemi (befits me).","Ade (crown) + yemi (befits me).",1],
 ["first-name","Olufemi","Olufemi is a masculine given name in Yoruba. Meaning: God loves me. Olu (God) + femi (loves me).","Olu (God) + femi (loves me).",1],
 ["first-name","Funke","Funke is a feminine given name in Yoruba. Meaning: Given to me to cherish. Short of Olufunke.","Short of Olufunke.",1],
 ["first-name","Adebayo","Adebayo is a masculine given name in Yoruba. Meaning: The crown meets joy. Ade + bayo.","Ade + bayo.",1],
 ["first-name","Temi","Temi is a feminine given name in Yoruba. Meaning: Mine. Short of Temilade, 'mine is the crown'.","Short of Temilade, 'mine is the crown'.",1],
 ["first-name","Babatunde","Babatunde is a masculine given name in Yoruba. Meaning: Father returns. A reincarnation name for a son.","A reincarnation name for a son.",1],
 ["first-name","Yetunde","Yetunde is a feminine given name in Yoruba. Meaning: Mother returns. A reincarnation name for a daughter.","A reincarnation name for a daughter.",1],
 ["surname","Adeyemi","Adeyemi is a Yoruba family name. Given names double as family names in Yoruba use.","Given names double as family names in Yoruba use.",2],
 ["surname","Adebayo","Adebayo is a Yoruba family name. The same pool serves both given and family names.","The same pool serves both given and family names.",2],
 ["surname","Ogunleye","Ogunleye is a Yoruba family name. A praise-name turned surname.","A praise-name turned surname.",2],
 ["surname","Oriki as surname","Oriki as surname is a Yoruba family name. Praise poetry names become inherited surnames.","Praise poetry names become inherited surnames.",2],
 ["place-name","Lagos","Lagos - Portuguese for 'lakes' — the colonial name that stuck.","Portuguese for 'lakes' — the colonial name that stuck.",2],
 ["place-name","Ibadan","Ibadan - From Eba Odan, 'by the edge of the meadow'.","From Eba Odan, 'by the edge of the meadow'.",2],
 ["naming-convention","Oriki praise names","Oriki praise names: Children receive oriki — praise poetry names describing hoped-for character.","Children receive oriki — praise poetry names describing hoped-for character.",3],
 ["naming-convention","Abiku names","Abiku names: A child believed to die and return gets a 'stay' name like Malomo, 'do not go again'.","A child believed to die and return gets a 'stay' name like Malomo, 'do not go ag",3]
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
  var esc="JAH-NMY-".replace(/[.*+?^${}()|[\]\\]/g,'\\$&');
  if(!new RegExp('^'+esc+'\\d{6}$').test(r.id||''))e.push('id');
  if(typeof r.name!=='string'||!r.name.length)e.push('name');
  if(typeof r.meaning!=='string'||!r.meaning.length)e.push('meaning');
  if(typeof r.title!=='string'||!r.title.length)e.push('title');
  if(CATS.indexOf(r.category)<0)e.push('category');
  if(!(r.ladder_rank>=1&&r.ladder_rank<=3))e.push('ladder_rank');
  return {ok:!e.length,errors:e};
}
var gen={version:"jahdb-names-yoruba-1.0",generate:generate,validate:validate};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("names-yoruba",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
