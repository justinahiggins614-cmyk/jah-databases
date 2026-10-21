(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var CATS=["first-name", "surname", "place-name", "naming-convention"];
var PREFIX="JAH-NMT4-";
/* rows: [category, display name, meaning, origin, ladder_rank] */
var B=[
 ["first-name","Mehmet","Mehmet is a masculine given name in Turkish. Meaning: The Turkish form of Muhammad..","The Turkish form of Muhammad.",1],
 ["first-name","Ayşe","Ayşe is a feminine given name in Turkish. Meaning: The Turkish form of Aisha; 'alive'..","The Turkish form of Aisha; 'alive'.",1],
 ["first-name","Mustafa","Mustafa is a masculine given name in Turkish. Meaning: Chosen..","Chosen.",1],
 ["first-name","Fatma","Fatma is a feminine given name in Turkish. Meaning: The Turkish form of Fatima..","The Turkish form of Fatima.",1],
 ["first-name","Emre","Emre is a masculine given name in Turkish. Meaning: A classic Turkish boys' name..","A classic Turkish boys' name.",1],
 ["first-name","Elif","Elif is a feminine given name in Turkish. Meaning: The first letter of the Arabic alphabet..","The first letter of the Arabic alphabet.",1],
 ["first-name","Burak","Burak is a masculine given name in Turkish. Meaning: The steed of the Prophet's night journey..","The steed of the Prophet's night journey.",1],
 ["surname","Yılmaz","Yılmaz is a Turkish family name. 'Undaunted' — from the 1934 Surname Law era.","'Undaunted' — from the 1934 Surname Law era.",2],
 ["surname","Kaya","Kaya is a Turkish family name. 'Rock'.","'Rock'.",2],
 ["surname","Demir","Demir is a Turkish family name. 'Iron'.","'Iron'.",2],
 ["surname","Öztürk","Öztürk is a Turkish family name. 'Pure Turk'.","'Pure Turk'.",2],
 ["place-name","Istanbul","Istanbul - From Constantinople — 'city of Constantine'.","From Constantinople — 'city of Constantine'.",2],
 ["place-name","Ankara","Ankara - The modern capital.","The modern capital.",2],
 ["naming-convention","The 1934 Surname Law","The 1934 Surname Law: Every Turkish family chose a Turkish surname in 1934.","Every Turkish family chose a Turkish surname in 1934.",3],
 ["naming-convention","Given + surname","Given + surname: Turkish names run given name first, surname last; middle names are rare.","Turkish names run given name first, surname last; middle names are rare.",3]
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
  var esc="JAH-NMT4-".replace(/[.*+?^${}()|[\]\\]/g,'\\$&');
  if(!new RegExp('^'+esc+'\\d{6}$').test(r.id||''))e.push('id');
  if(typeof r.name!=='string'||!r.name.length)e.push('name');
  if(typeof r.meaning!=='string'||!r.meaning.length)e.push('meaning');
  if(typeof r.title!=='string'||!r.title.length)e.push('title');
  if(CATS.indexOf(r.category)<0)e.push('category');
  if(!(r.ladder_rank>=1&&r.ladder_rank<=3))e.push('ladder_rank');
  return {ok:!e.length,errors:e};
}
var gen={version:"jahdb-names-turkish-1.0",generate:generate,validate:validate};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("names-turkish",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
