(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var CATS=["first-name", "surname", "place-name", "naming-convention"];
var PREFIX="JAH-NMP5-";
/* rows: [category, display name, meaning, origin, ladder_rank] */
var B=[
 ["first-name","Jan","Jan is a masculine given name in Polish. Meaning: God is gracious. The Polish form of John.","The Polish form of John.",1],
 ["first-name","Maria","Maria is a feminine given name in Polish. Meaning: Beloved..","Beloved.",1],
 ["first-name","Piotr","Piotr is a masculine given name in Polish. Meaning: Stone. The Polish form of Peter.","The Polish form of Peter.",1],
 ["first-name","Anna","Anna is a feminine given name in Polish. Meaning: Grace. From Hebrew Hannah.","From Hebrew Hannah.",1],
 ["first-name","Krzysztof","Krzysztof is a masculine given name in Polish. Meaning: Christ-bearer. The Polish form of Christopher.","The Polish form of Christopher.",1],
 ["first-name","Katarzyna","Katarzyna is a feminine given name in Polish. Meaning: Pure. The Polish form of Catherine.","The Polish form of Catherine.",1],
 ["first-name","Michał","Michał is a masculine given name in Polish. Meaning: Who is like God?. The Polish form of Michael.","The Polish form of Michael.",1],
 ["surname","Kowalski","Kowalski is a Polish family name. From kowal, 'smith' — 'the smith's'.","From kowal, 'smith' — 'the smith's'.",2],
 ["surname","Nowak","Nowak is a Polish family name. 'Newcomer' — the most common Polish surname.","'Newcomer' — the most common Polish surname.",2],
 ["surname","Wiśniewski","Wiśniewski is a Polish family name. From wiśnia, 'cherry'.","From wiśnia, 'cherry'.",2],
 ["surname","Zieliński","Zieliński is a Polish family name. From zieleń, 'greenery'.","From zieleń, 'greenery'.",2],
 ["place-name","Warszawa","Warszawa - From Warsz, the legendary founder — Warsaw.","From Warsz, the legendary founder — Warsaw.",2],
 ["place-name","Kraków","Kraków - From Krak, the legendary founder — Cracow.","From Krak, the legendary founder — Cracow.",2],
 ["naming-convention","-ski/-ska endings","-ski/-ska endings: Kowalski for men, Kowalska for women — surnames take gender.","Kowalski for men, Kowalska for women — surnames take gender.",3],
 ["naming-convention","-wicz patronymics","-wicz patronymics: Mickiewicz: 'son of Micko' — the old patronymic suffix.","Mickiewicz: 'son of Micko' — the old patronymic suffix.",3]
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
  var esc="JAH-NMP5-".replace(/[.*+?^${}()|[\]\\]/g,'\\$&');
  if(!new RegExp('^'+esc+'\\d{6}$').test(r.id||''))e.push('id');
  if(typeof r.name!=='string'||!r.name.length)e.push('name');
  if(typeof r.meaning!=='string'||!r.meaning.length)e.push('meaning');
  if(typeof r.title!=='string'||!r.title.length)e.push('title');
  if(CATS.indexOf(r.category)<0)e.push('category');
  if(!(r.ladder_rank>=1&&r.ladder_rank<=3))e.push('ladder_rank');
  return {ok:!e.length,errors:e};
}
var gen={version:"jahdb-names-polish-1.0",generate:generate,validate:validate};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("names-polish",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
