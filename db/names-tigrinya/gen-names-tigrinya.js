(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var CATS=["first-name", "surname", "place-name", "naming-convention"];
var PREFIX="JAH-NMT7-";
/* rows: [category, display name, meaning, origin, ladder_rank] */
var B=[
 ["first-name","Haile","Haile is a masculine given name in Tigrinya. Meaning: Power.. From Ge'ez.","From Ge'ez.",1],
 ["first-name","Mulu","Mulu is a unisex given name in Tigrinya. Meaning: Full, complete.. Unisex.","Unisex.",1],
 ["first-name","Tesfay","Tesfay is a masculine given name in Tigrinya. Meaning: Hope..","Hope.",1],
 ["first-name","Selam","Selam is a feminine given name in Tigrinya. Meaning: Peace..","Peace.",1],
 ["first-name","Yonas","Yonas is a masculine given name in Tigrinya. Meaning: Dove. The Tigrinya form of Jonah.","The Tigrinya form of Jonah.",1],
 ["first-name","Rahel","Rahel is a feminine given name in Tigrinya. Meaning: Ewe. The Tigrinya form of Rachel.","The Tigrinya form of Rachel.",1],
 ["first-name","Kibrom","Kibrom is a masculine given name in Tigrinya. Meaning: Honor.. A classic boys' name.","A classic boys' name.",1],
 ["surname","Father's given name","Father's given name is a Tigrinya family name. The father's given name is the second name.","The father's given name is the second name.",2],
 ["surname","No inherited surnames","No inherited surnames is a Tigrinya family name. Surnames do not pass down generations.","Surnames do not pass down generations.",2],
 ["surname","Ge'ez roots","Ge'ez roots is a Tigrinya family name. Haile, Selam, and Tesfay draw on Ge'ez.","Haile, Selam, and Tesfay draw on Ge'ez.",2],
 ["surname","Christian name pool","Christian name pool is a Tigrinya family name. Yonas and Rahel come from the biblical pool.","Yonas and Rahel come from the biblical pool.",2],
 ["place-name","Asmara","Asmara - 'They united' — the capital.","'They united' — the capital.",2],
 ["place-name","Mekelle","Mekelle - The Tigrayan capital.","The Tigrayan capital.",2],
 ["naming-convention","Given + father's given","Given + father's given: Each person's second name is the father's given name.","Each person's second name is the father's given name.",3],
 ["naming-convention","Ge'ez and Christian roots","Ge'ez and Christian roots: The pool is Ge'ez vocabulary and biblical names.","The pool is Ge'ez vocabulary and biblical names.",3]
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
  var esc="JAH-NMT7-".replace(/[.*+?^${}()|[\]\\]/g,'\\$&');
  if(!new RegExp('^'+esc+'\\d{6}$').test(r.id||''))e.push('id');
  if(typeof r.name!=='string'||!r.name.length)e.push('name');
  if(typeof r.meaning!=='string'||!r.meaning.length)e.push('meaning');
  if(typeof r.title!=='string'||!r.title.length)e.push('title');
  if(CATS.indexOf(r.category)<0)e.push('category');
  if(!(r.ladder_rank>=1&&r.ladder_rank<=3))e.push('ladder_rank');
  return {ok:!e.length,errors:e};
}
var gen={version:"jahdb-names-tigrinya-1.0",generate:generate,validate:validate};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("names-tigrinya",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
