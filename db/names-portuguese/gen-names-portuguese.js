(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var CATS=["first-name", "surname", "place-name", "naming-convention"];
var PREFIX="JAH-NMP2-";
/* rows: [category, display name, meaning, origin, ladder_rank] */
var B=[
 ["first-name","João","João is a masculine given name in Portuguese. Meaning: God is gracious. The Portuguese form of John.","The Portuguese form of John.",1],
 ["first-name","Maria","Maria is a feminine given name in Portuguese. Meaning: Beloved. Long the most common girls' name.","Long the most common girls' name.",1],
 ["first-name","José","José is a masculine given name in Portuguese. Meaning: God will increase. The Portuguese form of Joseph.","The Portuguese form of Joseph.",1],
 ["first-name","Ana","Ana is a feminine given name in Portuguese. Meaning: Grace. From Hebrew Hannah.","From Hebrew Hannah.",1],
 ["first-name","Miguel","Miguel is a masculine given name in Portuguese. Meaning: Who is like God?. The Portuguese form of Michael.","The Portuguese form of Michael.",1],
 ["first-name","Sofia","Sofia is a feminine given name in Portuguese. Meaning: Wisdom. From Greek.","From Greek.",1],
 ["first-name","Tiago","Tiago is a masculine given name in Portuguese. Meaning: The Portuguese form of James..","The Portuguese form of James.",1],
 ["surname","Silva","Silva is a Portuguese family name. 'Forest' — the most common Portuguese surname.","'Forest' — the most common Portuguese surname.",2],
 ["surname","Santos","Santos is a Portuguese family name. 'Saints'.","'Saints'.",2],
 ["surname","Oliveira","Oliveira is a Portuguese family name. 'Olive tree'.","'Olive tree'.",2],
 ["surname","Ferreira","Ferreira is a Portuguese family name. 'Ironworks' — occupational.","'Ironworks' — occupational.",2],
 ["place-name","Lisboa","Lisboa - From Olisipo, the Roman name — Lisbon.","From Olisipo, the Roman name — Lisbon.",2],
 ["place-name","Porto","Porto - 'Port' — the harbor city.","'Port' — the harbor city.",2],
 ["naming-convention","Two surnames","Two surnames: Portuguese names carry the mother's family name then the father's.","Portuguese names carry the mother's family name then the father's.",3],
 ["naming-convention","Maria and José compounds","Maria and José compounds: Maria and José combine freely: Maria José, José Maria.","Maria and José combine freely: Maria José, José Maria.",3]
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
  var esc="JAH-NMP2-".replace(/[.*+?^${}()|[\]\\]/g,'\\$&');
  if(!new RegExp('^'+esc+'\\d{6}$').test(r.id||''))e.push('id');
  if(typeof r.name!=='string'||!r.name.length)e.push('name');
  if(typeof r.meaning!=='string'||!r.meaning.length)e.push('meaning');
  if(typeof r.title!=='string'||!r.title.length)e.push('title');
  if(CATS.indexOf(r.category)<0)e.push('category');
  if(!(r.ladder_rank>=1&&r.ladder_rank<=3))e.push('ladder_rank');
  return {ok:!e.length,errors:e};
}
var gen={version:"jahdb-names-portuguese-1.0",generate:generate,validate:validate};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("names-portuguese",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
