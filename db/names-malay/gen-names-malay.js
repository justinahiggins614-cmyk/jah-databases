(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var CATS=["first-name", "surname", "place-name", "naming-convention"];
var PREFIX="JAH-NMM2-";
/* rows: [category, display name, meaning, origin, ladder_rank] */
var B=[
 ["first-name","Ahmad","Ahmad is a masculine given name in Malay. Meaning: Most praised..","Most praised.",1],
 ["first-name","Siti","Siti is a feminine given name in Malay. Meaning: From Sita; the classic Malay girls' name..","From Sita; the classic Malay girls' name.",1],
 ["first-name","Nur","Nur is a unisex given name in Malay. Meaning: Light. Unisex; 'radiance'.","Unisex; 'radiance'.",1],
 ["first-name","Muhammad","Muhammad is a masculine given name in Malay. Meaning: Praised..","Praised.",1],
 ["first-name","Aisyah","Aisyah is a feminine given name in Malay. Meaning: Alive..","Alive.",1],
 ["first-name","Faizal","Faizal is a masculine given name in Malay. Meaning: Decisive; arbiter..","Decisive; arbiter.",1],
 ["first-name","Wan","Wan is a unisex given name in Malay. Meaning: A traditional name element marking descent..","A traditional name element marking descent.",1],
 ["surname","Bin and binti","Bin and binti is a Malay family name. 'Son of' and 'daughter of' replace surnames: Ahmad bin Abdullah.","'Son of' and 'daughter of' replace surnames: Ahmad bin Abdullah.",2],
 ["surname","No family surnames traditionally","No family surnames traditionally is a Malay family name. The father's given name is the second name.","The father's given name is the second name.",2],
 ["surname","Arabic name pool","Arabic name pool is a Malay family name. Qur'anic names dominate Malay naming.","Qur'anic names dominate Malay naming.",2],
 ["surname","Sanskrit layer","Sanskrit layer is a Malay family name. Older names like Siti and Dewi come from Sanskrit.","Older names like Siti and Dewi come from Sanskrit.",2],
 ["place-name","Kuala Lumpur","Kuala Lumpur - 'Muddy confluence' — where two rivers meet.","'Muddy confluence' — where two rivers meet.",2],
 ["place-name","Johor","Johor - The southern sultanate's name.","The southern sultanate's name.",2],
 ["naming-convention","Bin/binti","Bin/binti: Ahmad bin Abdullah: 'Ahmad, son of Abdullah' — no surname.","Ahmad bin Abdullah: 'Ahmad, son of Abdullah' — no surname.",3],
 ["naming-convention","No inherited surnames traditionally","No inherited surnames traditionally: Each generation's second name is the father's given name.","Each generation's second name is the father's given name.",3]
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
  var esc="JAH-NMM2-".replace(/[.*+?^${}()|[\]\\]/g,'\\$&');
  if(!new RegExp('^'+esc+'\\d{6}$').test(r.id||''))e.push('id');
  if(typeof r.name!=='string'||!r.name.length)e.push('name');
  if(typeof r.meaning!=='string'||!r.meaning.length)e.push('meaning');
  if(typeof r.title!=='string'||!r.title.length)e.push('title');
  if(CATS.indexOf(r.category)<0)e.push('category');
  if(!(r.ladder_rank>=1&&r.ladder_rank<=3))e.push('ladder_rank');
  return {ok:!e.length,errors:e};
}
var gen={version:"jahdb-names-malay-1.0",generate:generate,validate:validate};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("names-malay",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
