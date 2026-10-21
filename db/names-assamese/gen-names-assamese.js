(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var CATS=["first-name", "surname", "place-name", "naming-convention"];
var PREFIX="JAH-NMA3-";
/* rows: [category, display name, meaning, origin, ladder_rank] */
var B=[
 ["first-name","Jyoti","Jyoti is a unisex given name in Assamese. Meaning: Light. Unisex; from Sanskrit.","Unisex; from Sanskrit.",1],
 ["first-name","Bhabesh","Bhabesh is a masculine given name in Assamese. Meaning: A classic Assamese boys' name..","A classic Assamese boys' name.",1],
 ["first-name","Priyanka","Priyanka is a feminine given name in Assamese. Meaning: Beloved..","Beloved.",1],
 ["first-name","Dhruba","Dhruba is a masculine given name in Assamese. Meaning: Pole star. From Sanskrit.","From Sanskrit.",1],
 ["first-name","Bornali","Bornali is a feminine given name in Assamese. Meaning: A popular girls' name..","A popular girls' name.",1],
 ["first-name","Manab","Manab is a masculine given name in Assamese. Meaning: Human.. A thoughtful boys' name.","A thoughtful boys' name.",1],
 ["first-name","Juri","Juri is a feminine given name in Assamese. Meaning: A common girls' name..","A common girls' name.",1],
 ["surname","Das","Das is a Assamese family name. 'Servant (of God)' — devotional.","'Servant (of God)' — devotional.",2],
 ["surname","Saikia","Saikia is a Assamese family name. Commander of a hundred — an Ahom-era title.","Commander of a hundred — an Ahom-era title.",2],
 ["surname","Barman","Barman is a Assamese family name. A traditional title.","A traditional title.",2],
 ["surname","Deka","Deka is a Assamese family name. A traditional title.","A traditional title.",2],
 ["place-name","Guwahati","Guwahati - Guva (areca nut) + hati (market).","Guva (areca nut) + hati (market).",2],
 ["place-name","Dispur","Dispur - The capital district.","The capital district.",2],
 ["naming-convention","Ahom-era titles","Ahom-era titles: Saikia and Barman began as Ahom military and court titles.","Saikia and Barman began as Ahom military and court titles.",3],
 ["naming-convention","Given + family order","Given + family order: Assamese names run given name first, family name last.","Assamese names run given name first, family name last.",3]
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
  var esc="JAH-NMA3-".replace(/[.*+?^${}()|[\]\\]/g,'\\$&');
  if(!new RegExp('^'+esc+'\\d{6}$').test(r.id||''))e.push('id');
  if(typeof r.name!=='string'||!r.name.length)e.push('name');
  if(typeof r.meaning!=='string'||!r.meaning.length)e.push('meaning');
  if(typeof r.title!=='string'||!r.title.length)e.push('title');
  if(CATS.indexOf(r.category)<0)e.push('category');
  if(!(r.ladder_rank>=1&&r.ladder_rank<=3))e.push('ladder_rank');
  return {ok:!e.length,errors:e};
}
var gen={version:"jahdb-names-assamese-1.0",generate:generate,validate:validate};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("names-assamese",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
