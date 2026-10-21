(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var CATS=["first-name", "surname", "place-name", "naming-convention"];
var PREFIX="JAH-NMU3-";
/* rows: [category, display name, meaning, origin, ladder_rank] */
var B=[
 ["first-name","Ivan","Ivan is a masculine given name in Ukrainian. Meaning: God is gracious. The Ukrainian form of John.","The Ukrainian form of John.",1],
 ["first-name","Olena","Olena is a feminine given name in Ukrainian. Meaning: Light. The Ukrainian form of Helen.","The Ukrainian form of Helen.",1],
 ["first-name","Taras","Taras is a masculine given name in Ukrainian. Meaning: The poet Shevchenko's name; a national name..","The poet Shevchenko's name; a national name.",1],
 ["first-name","Bohdan","Bohdan is a masculine given name in Ukrainian. Meaning: Given by God. Boh (God) + dan (given).","Boh (God) + dan (given).",1],
 ["first-name","Lesya","Lesya is a feminine given name in Ukrainian. Meaning: Short of Oleksandra; the poet Ukrainka's name..","Short of Oleksandra; the poet Ukrainka's name.",1],
 ["first-name","Mykola","Mykola is a masculine given name in Ukrainian. Meaning: Victory of the people. The Ukrainian form of Nicholas.","The Ukrainian form of Nicholas.",1],
 ["first-name","Solomiya","Solomiya is a feminine given name in Ukrainian. Meaning: Peaceful. From Hebrew Shlomit.","From Hebrew Shlomit.",1],
 ["surname","Shevchenko","Shevchenko is a Ukrainian family name. The -enko suffix — 'descendant of the shoemaker'.","The -enko suffix — 'descendant of the shoemaker'.",2],
 ["surname","Kovalenko","Kovalenko is a Ukrainian family name. 'Smith's descendant' — koval is 'smith'.","'Smith's descendant' — koval is 'smith'.",2],
 ["surname","Bondarenko","Bondarenko is a Ukrainian family name. 'Cooper's descendant'.","'Cooper's descendant'.",2],
 ["surname","Tkachenko","Tkachenko is a Ukrainian family name. 'Weaver's descendant'.","'Weaver's descendant'.",2],
 ["place-name","Kyiv","Kyiv - From Kyi, the legendary founder.","From Kyi, the legendary founder.",2],
 ["place-name","Lviv","Lviv - From Lev, 'lion' — named for a prince.","From Lev, 'lion' — named for a prince.",2],
 ["naming-convention","-enko surnames","-enko surnames: Shevchenko, Kovalenko: -enko marks descent.","Shevchenko, Kovalenko: -enko marks descent.",3],
 ["naming-convention","Given + patronymic + surname","Given + patronymic + surname: Full names run given name, patronymic, then surname.","Full names run given name, patronymic, then surname.",3]
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
  var esc="JAH-NMU3-".replace(/[.*+?^${}()|[\]\\]/g,'\\$&');
  if(!new RegExp('^'+esc+'\\d{6}$').test(r.id||''))e.push('id');
  if(typeof r.name!=='string'||!r.name.length)e.push('name');
  if(typeof r.meaning!=='string'||!r.meaning.length)e.push('meaning');
  if(typeof r.title!=='string'||!r.title.length)e.push('title');
  if(CATS.indexOf(r.category)<0)e.push('category');
  if(!(r.ladder_rank>=1&&r.ladder_rank<=3))e.push('ladder_rank');
  return {ok:!e.length,errors:e};
}
var gen={version:"jahdb-names-ukrainian-1.0",generate:generate,validate:validate};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("names-ukrainian",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
