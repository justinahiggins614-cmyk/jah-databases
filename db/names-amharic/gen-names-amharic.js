(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var CATS=["first-name", "surname", "place-name", "naming-convention"];
var PREFIX="JAH-NMA4-";
/* rows: [category, display name, meaning, origin, ladder_rank] */
var B=[
 ["first-name","Haile","Haile is a masculine given name in Amharic. Meaning: Power.. From Ge'ez.","From Ge'ez.",1],
 ["first-name","Selam","Selam is a feminine given name in Amharic. Meaning: Peace..","Peace.",1],
 ["first-name","Tesfaye","Tesfaye is a masculine given name in Amharic. Meaning: My hope..","My hope.",1],
 ["first-name","Alemayehu","Alemayehu is a masculine given name in Amharic. Meaning: I have seen the world..","I have seen the world.",1],
 ["first-name","Tirunesh","Tirunesh is a feminine given name in Amharic. Meaning: A classic girls' name..","A classic girls' name.",1],
 ["first-name","Girma","Girma is a masculine given name in Amharic. Meaning: Amazing..","Amazing.",1],
 ["first-name","Almaz","Almaz is a feminine given name in Amharic. Meaning: Diamond..","Diamond.",1],
 ["surname","Patronymic only","Patronymic only is a Amharic family name. The father's given name is the second name; no inherited surnames.","The father's given name is the second name; no inherited surnames.",2],
 ["surname","Given + father's given","Given + father's given is a Amharic family name. Haile Tesfaye: Haile, son of Tesfaye.","Haile Tesfaye: Haile, son of Tesfaye.",2],
 ["surname","No family names","No family names is a Amharic family name. Surnames do not pass down generations.","Surnames do not pass down generations.",2],
 ["surname","Ge'ez roots","Ge'ez roots is a Amharic family name. Haile, Selam, and Tesfaye draw on Ge'ez.","Haile, Selam, and Tesfaye draw on Ge'ez.",2],
 ["place-name","Addis Ababa","Addis Ababa - 'New flower' — the capital.","'New flower' — the capital.",2],
 ["place-name","Gondar","Gondar - The historic imperial city.","The historic imperial city.",2],
 ["naming-convention","No inherited surnames","No inherited surnames: Each person's second name is their father's given name.","Each person's second name is their father's given name.",3],
 ["naming-convention","Ge'ez and Christian roots","Ge'ez and Christian roots: The name pool is Ge'ez and Orthodox Christian.","The name pool is Ge'ez and Orthodox Christian.",3]
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
  var esc="JAH-NMA4-".replace(/[.*+?^${}()|[\]\\]/g,'\\$&');
  if(!new RegExp('^'+esc+'\\d{6}$').test(r.id||''))e.push('id');
  if(typeof r.name!=='string'||!r.name.length)e.push('name');
  if(typeof r.meaning!=='string'||!r.meaning.length)e.push('meaning');
  if(typeof r.title!=='string'||!r.title.length)e.push('title');
  if(CATS.indexOf(r.category)<0)e.push('category');
  if(!(r.ladder_rank>=1&&r.ladder_rank<=3))e.push('ladder_rank');
  return {ok:!e.length,errors:e};
}
var gen={version:"jahdb-names-amharic-1.0",generate:generate,validate:validate};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("names-amharic",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
