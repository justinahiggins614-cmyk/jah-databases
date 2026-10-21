(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var CATS=["first-name", "surname", "place-name", "naming-convention"];
var PREFIX="JAH-NMG2-";
/* rows: [category, display name, meaning, origin, ladder_rank] */
var B=[
 ["first-name","Amit","Amit is a masculine given name in Gujarati. Meaning: Infinite. From Sanskrit amita.","From Sanskrit amita.",1],
 ["first-name","Priya","Priya is a feminine given name in Gujarati. Meaning: Beloved..","Beloved.",1],
 ["first-name","Rajesh","Rajesh is a masculine given name in Gujarati. Meaning: King of kings..","King of kings.",1],
 ["first-name","Meera","Meera is a feminine given name in Gujarati. Meaning: The poet-saint Mirabai's name..","The poet-saint Mirabai's name.",1],
 ["first-name","Hiren","Hiren is a masculine given name in Gujarati. Meaning: A modern boys' name..","A modern boys' name.",1],
 ["first-name","Kiran","Kiran is a unisex given name in Gujarati. Meaning: Ray of light. Unisex.","Unisex.",1],
 ["first-name","Nisha","Nisha is a feminine given name in Gujarati. Meaning: Night.. From Sanskrit.","From Sanskrit.",1],
 ["surname","Patel","Patel is a Gujarati family name. Village headman — the most common Gujarati surname.","Village headman — the most common Gujarati surname.",2],
 ["surname","Shah","Shah is a Gujarati family name. From Persian shah, 'king' — merchant families.","From Persian shah, 'king' — merchant families.",2],
 ["surname","Mehta","Mehta is a Gujarati family name. Accountant — an occupational title.","Accountant — an occupational title.",2],
 ["surname","Desai","Desai is a Gujarati family name. 'Lord of the land' — a historic title.","'Lord of the land' — a historic title.",2],
 ["place-name","Ahmedabad","Ahmedabad - Founded by Ahmed Shah; 'city of Ahmed'.","Founded by Ahmed Shah; 'city of Ahmed'.",2],
 ["place-name","Surat","Surat - The historic port city.","The historic port city.",2],
 ["naming-convention","-bhai and -ben","-bhai and -ben: Men take -bhai (brother) and women -ben (sister) as respectful suffixes.","Men take -bhai (brother) and women -ben (sister) as respectful suffixes.",3],
 ["naming-convention","Given + father's + family","Given + father's + family: Full names often include the father's given name in the middle.","Full names often include the father's given name in the middle.",3]
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
  var esc="JAH-NMG2-".replace(/[.*+?^${}()|[\]\\]/g,'\\$&');
  if(!new RegExp('^'+esc+'\\d{6}$').test(r.id||''))e.push('id');
  if(typeof r.name!=='string'||!r.name.length)e.push('name');
  if(typeof r.meaning!=='string'||!r.meaning.length)e.push('meaning');
  if(typeof r.title!=='string'||!r.title.length)e.push('title');
  if(CATS.indexOf(r.category)<0)e.push('category');
  if(!(r.ladder_rank>=1&&r.ladder_rank<=3))e.push('ladder_rank');
  return {ok:!e.length,errors:e};
}
var gen={version:"jahdb-names-gujarati-1.0",generate:generate,validate:validate};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("names-gujarati",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
