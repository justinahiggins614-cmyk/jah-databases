(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var CATS=["first-name", "surname", "place-name", "naming-convention"];
var PREFIX="JAH-NMR2-";
/* rows: [category, display name, meaning, origin, ladder_rank] */
var B=[
 ["first-name","Ion","Ion is a masculine given name in Romanian. Meaning: God is gracious. The Romanian form of John.","The Romanian form of John.",1],
 ["first-name","Maria","Maria is a feminine given name in Romanian. Meaning: Beloved..","Beloved.",1],
 ["first-name","Gheorghe","Gheorghe is a masculine given name in Romanian. Meaning: Farmer. The Romanian form of George.","The Romanian form of George.",1],
 ["first-name","Elena","Elena is a feminine given name in Romanian. Meaning: Light. The Romanian form of Helen.","The Romanian form of Helen.",1],
 ["first-name","Andrei","Andrei is a masculine given name in Romanian. Meaning: Manly. The Romanian form of Andrew.","The Romanian form of Andrew.",1],
 ["first-name","Ioana","Ioana is a feminine given name in Romanian. Meaning: God is gracious.. The feminine form of Ion.","The feminine form of Ion.",1],
 ["first-name","Mihai","Mihai is a masculine given name in Romanian. Meaning: Who is like God?. The Romanian form of Michael.","The Romanian form of Michael.",1],
 ["surname","Popescu","Popescu is a Romanian family name. 'Son of the priest' — the -escu suffix.","'Son of the priest' — the -escu suffix.",2],
 ["surname","Ionescu","Ionescu is a Romanian family name. 'Son of Ion'.","'Son of Ion'.",2],
 ["surname","Popa","Popa is a Romanian family name. 'Priest'.","'Priest'.",2],
 ["surname","Dumitru","Dumitru is a Romanian family name. From Demetrius.","From Demetrius.",2],
 ["place-name","București","București - From Bucur, the legendary shepherd — Bucharest.","From Bucur, the legendary shepherd — Bucharest.",2],
 ["place-name","Cluj","Cluj - The Transylvanian capital.","The Transylvanian capital.",2],
 ["naming-convention","-escu patronymics","-escu patronymics: Popescu, Ionescu: -escu marks 'son of'.","Popescu, Ionescu: -escu marks 'son of'.",3],
 ["naming-convention","Given + family order","Given + family order: Romanian names run given name first, family name last.","Romanian names run given name first, family name last.",3]
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
  var esc="JAH-NMR2-".replace(/[.*+?^${}()|[\]\\]/g,'\\$&');
  if(!new RegExp('^'+esc+'\\d{6}$').test(r.id||''))e.push('id');
  if(typeof r.name!=='string'||!r.name.length)e.push('name');
  if(typeof r.meaning!=='string'||!r.meaning.length)e.push('meaning');
  if(typeof r.title!=='string'||!r.title.length)e.push('title');
  if(CATS.indexOf(r.category)<0)e.push('category');
  if(!(r.ladder_rank>=1&&r.ladder_rank<=3))e.push('ladder_rank');
  return {ok:!e.length,errors:e};
}
var gen={version:"jahdb-names-romanian-1.0",generate:generate,validate:validate};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("names-romanian",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
