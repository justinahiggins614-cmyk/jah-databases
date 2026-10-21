(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var CATS=["first-name", "surname", "place-name", "naming-convention"];
var PREFIX="JAH-NMI3-";
/* rows: [category, display name, meaning, origin, ladder_rank] */
var B=[
 ["first-name","Chiamaka","Chiamaka is a feminine given name in Igbo. Meaning: God is beautiful. Chi (God) + amaka (beautiful).","Chi (God) + amaka (beautiful).",1],
 ["first-name","Obinna","Obinna is a masculine given name in Igbo. Meaning: Father's heart. Obi (heart) + nna (father).","Obi (heart) + nna (father).",1],
 ["first-name","Adaeze","Adaeze is a feminine given name in Igbo. Meaning: King's daughter. Ada (daughter) + eze (king).","Ada (daughter) + eze (king).",1],
 ["first-name","Ngozi","Ngozi is a unisex given name in Igbo. Meaning: Blessing. Unisex.","Unisex.",1],
 ["first-name","Chukwuemeka","Chukwuemeka is a masculine given name in Igbo. Meaning: God has done great. Chukwu (God) + emeka.","Chukwu (God) + emeka.",1],
 ["first-name","Nneka","Nneka is a feminine given name in Igbo. Meaning: Mother is supreme. Nne (mother) + ka (supreme).","Nne (mother) + ka (supreme).",1],
 ["first-name","Ifeanyi","Ifeanyi is a masculine given name in Igbo. Meaning: Nothing is impossible with God..","Nothing is impossible with God.",1],
 ["surname","Okafor","Okafor is a Igbo family name. Born on Afor day — a market-day name.","Born on Afor day — a market-day name.",2],
 ["surname","Eze","Eze is a Igbo family name. 'King'.","'King'.",2],
 ["surname","Obi","Obi is a Igbo family name. 'Heart'.","'Heart'.",2],
 ["surname","Nwosu","Nwosu is a Igbo family name. A traditional family name.","A traditional family name.",2],
 ["place-name","Enugu","Enugu - 'Hilltop' — the coal city.","'Hilltop' — the coal city.",2],
 ["place-name","Onitsha","Onitsha - The great market city on the Niger.","The great market city on the Niger.",2],
 ["naming-convention","Chi- theophoric names","Chi- theophoric names: Most Igbo names begin with Chi/Chukwu, 'God'.","Most Igbo names begin with Chi/Chukwu, 'God'.",3],
 ["naming-convention","Market-day names","Market-day names: Children may be named for the market day of their birth.","Children may be named for the market day of their birth.",3]
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
  var esc="JAH-NMI3-".replace(/[.*+?^${}()|[\]\\]/g,'\\$&');
  if(!new RegExp('^'+esc+'\\d{6}$').test(r.id||''))e.push('id');
  if(typeof r.name!=='string'||!r.name.length)e.push('name');
  if(typeof r.meaning!=='string'||!r.meaning.length)e.push('meaning');
  if(typeof r.title!=='string'||!r.title.length)e.push('title');
  if(CATS.indexOf(r.category)<0)e.push('category');
  if(!(r.ladder_rank>=1&&r.ladder_rank<=3))e.push('ladder_rank');
  return {ok:!e.length,errors:e};
}
var gen={version:"jahdb-names-igbo-1.0",generate:generate,validate:validate};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("names-igbo",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
