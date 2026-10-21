(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var CATS=["first-name", "surname", "place-name", "naming-convention"];
var PREFIX="JAH-NMT2-";
/* rows: [category, display name, meaning, origin, ladder_rank] */
var B=[
 ["first-name","Murugan முருகன்","Murugan (முருகன்) is a masculine given name in Tamil. Meaning: The Tamil god of war and victory..","The Tamil god of war and victory.",1],
 ["first-name","Priya","Priya is a feminine given name in Tamil. Meaning: Beloved. From Sanskrit.","From Sanskrit.",1],
 ["first-name","Kannan","Kannan is a masculine given name in Tamil. Meaning: A Tamil form of Krishna..","A Tamil form of Krishna.",1],
 ["first-name","Divya","Divya is a feminine given name in Tamil. Meaning: Divine. From Sanskrit.","From Sanskrit.",1],
 ["first-name","Arun","Arun is a masculine given name in Tamil. Meaning: Dawn. From Sanskrit aruna.","From Sanskrit aruna.",1],
 ["first-name","Meena","Meena is a feminine given name in Tamil. Meaning: Fish. A classic girls' name.","A classic girls' name.",1],
 ["first-name","Karthik","Karthik is a masculine given name in Tamil. Meaning: Another name of Murugan..","Another name of Murugan.",1],
 ["surname","Iyer","Iyer is a Tamil family name. A Tamil Brahmin community title.","A Tamil Brahmin community title.",2],
 ["surname","Mudaliar","Mudaliar is a Tamil family name. A traditional title, 'first one'.","A traditional title, 'first one'.",2],
 ["surname","Chettiar","Chettiar is a Tamil family name. A merchant community title.","A merchant community title.",2],
 ["surname","Ravi","Ravi is a Tamil family name. Often used as a patronymic initial rather than a surname.","Often used as a patronymic initial rather than a surname.",2],
 ["place-name","Chennai","Chennai - From Chennappa Nayak, a local ruler.","From Chennappa Nayak, a local ruler.",2],
 ["place-name","Madurai","Madurai - From Mathurai, 'sweetness'.","From Mathurai, 'sweetness'.",2],
 ["naming-convention","Initial + given name","Initial + given name: R. Karthik means Karthik, son of Ravi — the initial is the father's name.","R. Karthik means Karthik, son of Ravi — the initial is the father's name.",3],
 ["naming-convention","Village and father's names","Village and father's names: Older forms add the village name before the father's name.","Older forms add the village name before the father's name.",3]
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
  var esc="JAH-NMT2-".replace(/[.*+?^${}()|[\]\\]/g,'\\$&');
  if(!new RegExp('^'+esc+'\\d{6}$').test(r.id||''))e.push('id');
  if(typeof r.name!=='string'||!r.name.length)e.push('name');
  if(typeof r.meaning!=='string'||!r.meaning.length)e.push('meaning');
  if(typeof r.title!=='string'||!r.title.length)e.push('title');
  if(CATS.indexOf(r.category)<0)e.push('category');
  if(!(r.ladder_rank>=1&&r.ladder_rank<=3))e.push('ladder_rank');
  return {ok:!e.length,errors:e};
}
var gen={version:"jahdb-names-tamil-1.0",generate:generate,validate:validate};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("names-tamil",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
