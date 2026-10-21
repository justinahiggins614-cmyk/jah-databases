(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var CATS=["first-name", "surname", "place-name", "naming-convention"];
var PREFIX="JAH-NMJ2-";
/* rows: [category, display name, meaning, origin, ladder_rank] */
var B=[
 ["first-name","Sari","Sari is a feminine given name in Javanese. Meaning: Essence. The core or best part; a classic girls' name.","The core or best part; a classic girls' name.",1],
 ["first-name","Dewi","Dewi is a feminine given name in Javanese. Meaning: Goddess. From Sanskrit devi.","From Sanskrit devi.",1],
 ["first-name","Budi","Budi is a masculine given name in Javanese. Meaning: Character, mind. From Sanskrit buddhi.","From Sanskrit buddhi.",1],
 ["first-name","Agus","Agus is a masculine given name in Javanese. Meaning: Born in August — a calendar name..","Born in August — a calendar name.",1],
 ["first-name","Wulan","Wulan is a feminine given name in Javanese. Meaning: Moon. A poetic girls' name.","A poetic girls' name.",1],
 ["first-name","Bambang","Bambang is a masculine given name in Javanese. Meaning: A traditional boys' name..","A traditional boys' name.",1],
 ["first-name","Ratna","Ratna is a feminine given name in Javanese. Meaning: Jewel. From Sanskrit.","From Sanskrit.",1],
 ["surname","Mononym tradition","Mononym tradition is a Javanese family name. Many Javanese use a single name — Sukarno, Suharto — with no surname at all.","Many Javanese use a single name — Sukarno, Suharto — with no surname at all.",2],
 ["surname","Sanskrit roots","Sanskrit roots is a Javanese family name. Classical names draw on Sanskrit: Dewi, Budi, Ratna.","Classical names draw on Sanskrit: Dewi, Budi, Ratna.",2],
 ["surname","Arabic layer","Arabic layer is a Javanese family name. Muslim Javanese add Arabic names like Ahmad and Fatimah.","Muslim Javanese add Arabic names like Ahmad and Fatimah.",2],
 ["surname","No inherited surnames","No inherited surnames is a Javanese family name. Family names are not traditional in Java.","Family names are not traditional in Java.",2],
 ["place-name","Yogyakarta","Yogyakarta - 'Fit to prosper' — the sultan's city.","'Fit to prosper' — the sultan's city.",2],
 ["place-name","Surabaya","Surabaya - Legend: sura the shark fought baya the crocodile.","Legend: sura the shark fought baya the crocodile.",2],
 ["naming-convention","Mononyms common","Mononyms common: One name is complete; surnames are a modern import.","One name is complete; surnames are a modern import.",3],
 ["naming-convention","Sanskrit-derived names","Sanskrit-derived names: The classical name pool comes from Sanskrit.","The classical name pool comes from Sanskrit.",3]
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
  var esc="JAH-NMJ2-".replace(/[.*+?^${}()|[\]\\]/g,'\\$&');
  if(!new RegExp('^'+esc+'\\d{6}$').test(r.id||''))e.push('id');
  if(typeof r.name!=='string'||!r.name.length)e.push('name');
  if(typeof r.meaning!=='string'||!r.meaning.length)e.push('meaning');
  if(typeof r.title!=='string'||!r.title.length)e.push('title');
  if(CATS.indexOf(r.category)<0)e.push('category');
  if(!(r.ladder_rank>=1&&r.ladder_rank<=3))e.push('ladder_rank');
  return {ok:!e.length,errors:e};
}
var gen={version:"jahdb-names-javanese-1.0",generate:generate,validate:validate};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("names-javanese",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
