(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var CATS=["first-name", "surname", "place-name", "naming-convention"];
var PREFIX="JAH-NMI2-";
/* rows: [category, display name, meaning, origin, ladder_rank] */
var B=[
 ["first-name","Budi","Budi is a masculine given name in Indonesian. Meaning: Character, mind. From Sanskrit buddhi.","From Sanskrit buddhi.",1],
 ["first-name","Dewi","Dewi is a feminine given name in Indonesian. Meaning: Goddess. From Sanskrit devi.","From Sanskrit devi.",1],
 ["first-name","Agus","Agus is a masculine given name in Indonesian. Meaning: Born in August..","Born in August.",1],
 ["first-name","Sari","Sari is a feminine given name in Indonesian. Meaning: Essence..","Essence.",1],
 ["first-name","Putri","Putri is a feminine given name in Indonesian. Meaning: Princess..","Princess.",1],
 ["first-name","Rizky","Rizky is a masculine given name in Indonesian. Meaning: Sustenance. From Arabic rizq.","From Arabic rizq.",1],
 ["first-name","Intan","Intan is a feminine given name in Indonesian. Meaning: Diamond..","Diamond.",1],
 ["surname","Mononym tradition","Mononym tradition is a Indonesian family name. Many Indonesians use one name only — Sukarno had no surname.","Many Indonesians use one name only — Sukarno had no surname.",2],
 ["surname","Sanskrit roots","Sanskrit roots is a Indonesian family name. Budi, Dewi, Putri come from Sanskrit.","Budi, Dewi, Putri come from Sanskrit.",2],
 ["surname","Arabic layer","Arabic layer is a Indonesian family name. Muhammad, Ahmad, Fatimah are widespread.","Muhammad, Ahmad, Fatimah are widespread.",2],
 ["surname","No inherited surnames","No inherited surnames is a Indonesian family name. Family names are not traditional.","Family names are not traditional.",2],
 ["place-name","Jakarta","Jakarta - From Jayakarta, 'victorious deed'.","From Jayakarta, 'victorious deed'.",2],
 ["place-name","Bandung","Bandung - The highland city of West Java.","The highland city of West Java.",2],
 ["naming-convention","Mononyms common","Mononyms common: One name is a complete name in Indonesia.","One name is a complete name in Indonesia.",3],
 ["naming-convention","Sanskrit and Arabic sources","Sanskrit and Arabic sources: The name pool blends Sanskrit classics with Arabic names.","The name pool blends Sanskrit classics with Arabic names.",3]
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
  var esc="JAH-NMI2-".replace(/[.*+?^${}()|[\]\\]/g,'\\$&');
  if(!new RegExp('^'+esc+'\\d{6}$').test(r.id||''))e.push('id');
  if(typeof r.name!=='string'||!r.name.length)e.push('name');
  if(typeof r.meaning!=='string'||!r.meaning.length)e.push('meaning');
  if(typeof r.title!=='string'||!r.title.length)e.push('title');
  if(CATS.indexOf(r.category)<0)e.push('category');
  if(!(r.ladder_rank>=1&&r.ladder_rank<=3))e.push('ladder_rank');
  return {ok:!e.length,errors:e};
}
var gen={version:"jahdb-names-indonesian-1.0",generate:generate,validate:validate};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("names-indonesian",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
