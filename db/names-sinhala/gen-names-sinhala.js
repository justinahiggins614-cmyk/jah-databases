(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var CATS=["first-name", "surname", "place-name", "naming-convention"];
var PREFIX="JAH-NMS4-";
/* rows: [category, display name, meaning, origin, ladder_rank] */
var B=[
 ["first-name","Nimal","Nimal is a masculine given name in Sinhala. Meaning: A classic Sinhala boys' name..","A classic Sinhala boys' name.",1],
 ["first-name","Kamal","Kamal is a masculine given name in Sinhala. Meaning: Lotus. From Sanskrit.","From Sanskrit.",1],
 ["first-name","Sunil","Sunil is a masculine given name in Sinhala. Meaning: A leading boys' name..","A leading boys' name.",1],
 ["first-name","Priyanka","Priyanka is a feminine given name in Sinhala. Meaning: Beloved.. From Sanskrit.","From Sanskrit.",1],
 ["first-name","Chamari","Chamari is a feminine given name in Sinhala. Meaning: A popular girls' name..","A popular girls' name.",1],
 ["first-name","Duminda","Duminda is a masculine given name in Sinhala. Meaning: A classic boys' name..","A classic boys' name.",1],
 ["first-name","Nadeesha","Nadeesha is a feminine given name in Sinhala. Meaning: A popular girls' name..","A popular girls' name.",1],
 ["surname","Perera","Perera is a Sinhala family name. A Portuguese-era surname.","A Portuguese-era surname.",2],
 ["surname","Fernando","Fernando is a Sinhala family name. A Portuguese-era surname.","A Portuguese-era surname.",2],
 ["surname","Jayawardena","Jayawardena is a Sinhala family name. 'Victorious' — a Sinhala surname.","'Victorious' — a Sinhala surname.",2],
 ["surname","Silva","Silva is a Sinhala family name. A Portuguese-era surname.","A Portuguese-era surname.",2],
 ["place-name","Colombo","Colombo - From Kolamba, the old harbor name.","From Kolamba, the old harbor name.",2],
 ["place-name","Kandy","Kandy - From Kanda, 'hill' — the hill capital.","From Kanda, 'hill' — the hill capital.",2],
 ["naming-convention","Ge-names (house names)","Ge-names (house names): The ancestral house name precedes the given name.","The ancestral house name precedes the given name.",3],
 ["naming-convention","Portuguese-era surnames","Portuguese-era surnames: Perera, Fernando, and Silva date to the colonial centuries.","Perera, Fernando, and Silva date to the colonial centuries.",3]
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
  var esc="JAH-NMS4-".replace(/[.*+?^${}()|[\]\\]/g,'\\$&');
  if(!new RegExp('^'+esc+'\\d{6}$').test(r.id||''))e.push('id');
  if(typeof r.name!=='string'||!r.name.length)e.push('name');
  if(typeof r.meaning!=='string'||!r.meaning.length)e.push('meaning');
  if(typeof r.title!=='string'||!r.title.length)e.push('title');
  if(CATS.indexOf(r.category)<0)e.push('category');
  if(!(r.ladder_rank>=1&&r.ladder_rank<=3))e.push('ladder_rank');
  return {ok:!e.length,errors:e};
}
var gen={version:"jahdb-names-sinhala-1.0",generate:generate,validate:validate};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("names-sinhala",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
