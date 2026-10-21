(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var CATS=["first-name", "surname", "place-name", "naming-convention"];
var PREFIX="JAH-NMC2-";
/* rows: [category, display name, meaning, origin, ladder_rank] */
var B=[
 ["first-name","Juan","Juan is a masculine given name in Cebuano. Meaning: God is gracious..","God is gracious.",1],
 ["first-name","Maria","Maria is a feminine given name in Cebuano. Meaning: Beloved..","Beloved.",1],
 ["first-name","Jose","Jose is a masculine given name in Cebuano. Meaning: God will increase..","God will increase.",1],
 ["first-name","Rosa","Rosa is a feminine given name in Cebuano. Meaning: Rose..","Rose.",1],
 ["first-name","Pedro","Pedro is a masculine given name in Cebuano. Meaning: Stone..","Stone.",1],
 ["first-name","Ana","Ana is a feminine given name in Cebuano. Meaning: Grace..","Grace.",1],
 ["first-name","Miguel","Miguel is a masculine given name in Cebuano. Meaning: Who is like God?.","Who is like God?",1],
 ["surname","Dela Cruz","Dela Cruz is a Cebuano family name. 'Of the Cross' — from the Claveria decree.","'Of the Cross' — from the Claveria decree.",2],
 ["surname","Santos","Santos is a Cebuano family name. 'Saints'.","'Saints'.",2],
 ["surname","Garcia","Garcia is a Cebuano family name. Of debated origin; widespread.","Of debated origin; widespread.",2],
 ["surname","Reyes","Reyes is a Cebuano family name. 'Kings'.","'Kings'.",2],
 ["place-name","Cebu","Cebu - From sibo, 'trade' — the trading port.","From sibo, 'trade' — the trading port.",2],
 ["place-name","Davao","Davao - The great southern city.","The great southern city.",2],
 ["naming-convention","Claveria decree of 1849","Claveria decree of 1849: Spanish authorities assigned surnames from a catalog; most Cebuano surnames date to it.","Spanish authorities assigned surnames from a catalog; most Cebuano surnames date",3],
 ["naming-convention","Saints' names","Saints' names: Given names come overwhelmingly from the Catholic calendar.","Given names come overwhelmingly from the Catholic calendar.",3]
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
  var esc="JAH-NMC2-".replace(/[.*+?^${}()|[\]\\]/g,'\\$&');
  if(!new RegExp('^'+esc+'\\d{6}$').test(r.id||''))e.push('id');
  if(typeof r.name!=='string'||!r.name.length)e.push('name');
  if(typeof r.meaning!=='string'||!r.meaning.length)e.push('meaning');
  if(typeof r.title!=='string'||!r.title.length)e.push('title');
  if(CATS.indexOf(r.category)<0)e.push('category');
  if(!(r.ladder_rank>=1&&r.ladder_rank<=3))e.push('ladder_rank');
  return {ok:!e.length,errors:e};
}
var gen={version:"jahdb-names-cebuano-1.0",generate:generate,validate:validate};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("names-cebuano",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
