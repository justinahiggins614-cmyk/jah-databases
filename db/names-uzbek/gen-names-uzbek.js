(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var CATS=["first-name", "surname", "place-name", "naming-convention"];
var PREFIX="JAH-NMU4-";
/* rows: [category, display name, meaning, origin, ladder_rank] */
var B=[
 ["first-name","Sardor","Sardor is a masculine given name in Uzbek. Meaning: A leading modern boys' name..","A leading modern boys' name.",1],
 ["first-name","Dilnoza","Dilnoza is a feminine given name in Uzbek. Meaning: A popular girls' name..","A popular girls' name.",1],
 ["first-name","Jasur","Jasur is a masculine given name in Uzbek. Meaning: Brave..","Brave.",1],
 ["first-name","Nodira","Nodira is a feminine given name in Uzbek. Meaning: A classic girls' name..","A classic girls' name.",1],
 ["first-name","Otabek","Otabek is a masculine given name in Uzbek. Meaning: A traditional boys' name..","A traditional boys' name.",1],
 ["first-name","Malika","Malika is a feminine given name in Uzbek. Meaning: Queen..","Queen.",1],
 ["first-name","Timur","Timur is a masculine given name in Uzbek. Meaning: Iron.. The conqueror's name.","The conqueror's name.",1],
 ["surname","Karimov","Karimov is a Uzbek family name. 'Son of Karim' — the -ov suffix.","'Son of Karim' — the -ov suffix.",2],
 ["surname","Yusupov","Yusupov is a Uzbek family name. 'Son of Yusup'.","'Son of Yusup'.",2],
 ["surname","Rahimov","Rahimov is a Uzbek family name. 'Son of Rahim'.","'Son of Rahim'.",2],
 ["surname","Toshpulatov","Toshpulatov is a Uzbek family name. A traditional -ov surname.","A traditional -ov surname.",2],
 ["place-name","Tashkent","Tashkent - 'Stone city'.","'Stone city'.",2],
 ["place-name","Samarkand","Samarkand - From Sogdian; the Silk Road jewel.","From Sogdian; the Silk Road jewel.",2],
 ["naming-convention","-ov/-ev suffixes","-ov/-ev suffixes: Karimov, Yusupov: Soviet-era patronymic suffixes.","Karimov, Yusupov: Soviet-era patronymic suffixes.",3],
 ["naming-convention","Given + patronymic + surname","Given + patronymic + surname: Full names may carry all three in formal use.","Full names may carry all three in formal use.",3]
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
  var esc="JAH-NMU4-".replace(/[.*+?^${}()|[\]\\]/g,'\\$&');
  if(!new RegExp('^'+esc+'\\d{6}$').test(r.id||''))e.push('id');
  if(typeof r.name!=='string'||!r.name.length)e.push('name');
  if(typeof r.meaning!=='string'||!r.meaning.length)e.push('meaning');
  if(typeof r.title!=='string'||!r.title.length)e.push('title');
  if(CATS.indexOf(r.category)<0)e.push('category');
  if(!(r.ladder_rank>=1&&r.ladder_rank<=3))e.push('ladder_rank');
  return {ok:!e.length,errors:e};
}
var gen={version:"jahdb-names-uzbek-1.0",generate:generate,validate:validate};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("names-uzbek",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
