(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var CATS=["first-name", "surname", "place-name", "naming-convention"];
var PREFIX="JAH-NMH3-";
/* rows: [category, display name, meaning, origin, ladder_rank] */
var B=[
 ["first-name","Musa","Musa is a masculine given name in Hausa. Meaning: The Hausa form of Moses..","The Hausa form of Moses.",1],
 ["first-name","Amina","Amina is a feminine given name in Hausa. Meaning: Trustworthy..","Trustworthy.",1],
 ["first-name","Ibrahim","Ibrahim is a masculine given name in Hausa. Meaning: The Hausa form of Abraham..","The Hausa form of Abraham.",1],
 ["first-name","Fatima","Fatima is a feminine given name in Hausa. Meaning: Captivating..","Captivating.",1],
 ["first-name","Sani","Sani is a masculine given name in Hausa. Meaning: A classic Hausa boys' name..","A classic Hausa boys' name.",1],
 ["first-name","Hadiza","Hadiza is a feminine given name in Hausa. Meaning: A leading Hausa girls' name..","A leading Hausa girls' name.",1],
 ["first-name","Usman","Usman is a masculine given name in Hausa. Meaning: A leading early Muslim name..","A leading early Muslim name.",1],
 ["surname","Father's name as surname","Father's name as surname is a Hausa family name. The father's given name serves as the child's second name.","The father's given name serves as the child's second name.",2],
 ["surname","No inherited surnames traditionally","No inherited surnames traditionally is a Hausa family name. Family names are a modern administrative addition.","Family names are a modern administrative addition.",2],
 ["surname","Islamic name pool","Islamic name pool is a Hausa family name. Qur'anic names dominate: Musa, Ibrahim, Amina.","Qur'anic names dominate: Musa, Ibrahim, Amina.",2],
 ["surname","Day and praise names","Day and praise names is a Hausa family name. Names may mark the day or circumstances of birth.","Names may mark the day or circumstances of birth.",2],
 ["place-name","Kano","Kano - Tradition names it for Kano, a blacksmith of legend.","Tradition names it for Kano, a blacksmith of legend.",2],
 ["place-name","Sokoto","Sokoto - The seat of the Sokoto Caliphate.","The seat of the Sokoto Caliphate.",2],
 ["naming-convention","Suna naming ceremony","Suna naming ceremony: The child is named on the seventh day after birth.","The child is named on the seventh day after birth.",3],
 ["naming-convention","No inherited surnames traditionally","No inherited surnames traditionally: Identity runs through the father's name, not a family surname.","Identity runs through the father's name, not a family surname.",3]
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
  var esc="JAH-NMH3-".replace(/[.*+?^${}()|[\]\\]/g,'\\$&');
  if(!new RegExp('^'+esc+'\\d{6}$').test(r.id||''))e.push('id');
  if(typeof r.name!=='string'||!r.name.length)e.push('name');
  if(typeof r.meaning!=='string'||!r.meaning.length)e.push('meaning');
  if(typeof r.title!=='string'||!r.title.length)e.push('title');
  if(CATS.indexOf(r.category)<0)e.push('category');
  if(!(r.ladder_rank>=1&&r.ladder_rank<=3))e.push('ladder_rank');
  return {ok:!e.length,errors:e};
}
var gen={version:"jahdb-names-hausa-1.0",generate:generate,validate:validate};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("names-hausa",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
