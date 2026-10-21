(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var CATS=["first-name", "surname", "place-name", "naming-convention"];
var PREFIX="JAH-NMA2-";
/* rows: [category, display name, meaning, origin, ladder_rank] */
var B=[
 ["first-name","Ali","Ali is a masculine given name in Azerbaijani. Meaning: Exalted..","Exalted.",1],
 ["first-name","Leyla","Leyla is a feminine given name in Azerbaijani. Meaning: Night..","Night.",1],
 ["first-name","Elvin","Elvin is a masculine given name in Azerbaijani. Meaning: A modern boys' name..","A modern boys' name.",1],
 ["first-name","Aysel","Aysel is a feminine given name in Azerbaijani. Meaning: Moonlight. Ay (moon) + sel (flood of light).","Ay (moon) + sel (flood of light).",1],
 ["first-name","Tural","Tural is a masculine given name in Azerbaijani. Meaning: A modern boys' name..","A modern boys' name.",1],
 ["first-name","Gunel","Gunel is a feminine given name in Azerbaijani. Meaning: A popular girls' name..","A popular girls' name.",1],
 ["first-name","Orkhan","Orkhan is a masculine given name in Azerbaijani. Meaning: A classic boys' name..","A classic boys' name.",1],
 ["surname","Mammadov","Mammadov is a Azerbaijani family name. 'Son of Mammad' — the -ov suffix.","'Son of Mammad' — the -ov suffix.",2],
 ["surname","Aliyev","Aliyev is a Azerbaijani family name. 'Son of Ali'.","'Son of Ali'.",2],
 ["surname","Huseynov","Huseynov is a Azerbaijani family name. 'Son of Huseyn'.","'Son of Huseyn'.",2],
 ["surname","Guliyev","Guliyev is a Azerbaijani family name. 'Son of Guli'.","'Son of Guli'.",2],
 ["place-name","Baku","Baku - Traditionally 'wind-pounded' — the windy capital.","Traditionally 'wind-pounded' — the windy capital.",2],
 ["place-name","Ganja","Ganja - The historic western city.","The historic western city.",2],
 ["naming-convention","-ov/-ev suffixes","-ov/-ev suffixes: Mammadov, Aliyev: Russian-era patronymic suffixes.","Mammadov, Aliyev: Russian-era patronymic suffixes.",3],
 ["naming-convention","-zade, 'son of'","-zade, 'son of': -zade marks descent in the Persian style.","-zade marks descent in the Persian style.",3]
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
  var esc="JAH-NMA2-".replace(/[.*+?^${}()|[\]\\]/g,'\\$&');
  if(!new RegExp('^'+esc+'\\d{6}$').test(r.id||''))e.push('id');
  if(typeof r.name!=='string'||!r.name.length)e.push('name');
  if(typeof r.meaning!=='string'||!r.meaning.length)e.push('meaning');
  if(typeof r.title!=='string'||!r.title.length)e.push('title');
  if(CATS.indexOf(r.category)<0)e.push('category');
  if(!(r.ladder_rank>=1&&r.ladder_rank<=3))e.push('ladder_rank');
  return {ok:!e.length,errors:e};
}
var gen={version:"jahdb-names-azerbaijani-1.0",generate:generate,validate:validate};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("names-azerbaijani",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
