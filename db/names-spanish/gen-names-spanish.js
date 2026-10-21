(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var CATS=["first-name", "surname", "place-name", "naming-convention"];
var PREFIX="JAH-NMS2-";
/* rows: [category, display name, meaning, origin, ladder_rank] */
var B=[
 ["first-name","José","José is a masculine given name in Spanish. Meaning: God will increase. The Spanish form of Joseph.","The Spanish form of Joseph.",1],
 ["first-name","María","María is a feminine given name in Spanish. Meaning: Beloved. Long the most common girls' name.","Long the most common girls' name.",1],
 ["first-name","Juan","Juan is a masculine given name in Spanish. Meaning: God is gracious. The Spanish form of John.","The Spanish form of John.",1],
 ["first-name","Carmen","Carmen is a feminine given name in Spanish. Meaning: Of Carmel. From Our Lady of Mount Carmel.","From Our Lady of Mount Carmel.",1],
 ["first-name","Antonio","Antonio is a masculine given name in Spanish. Meaning: Priceless. From the Roman Antonius.","From the Roman Antonius.",1],
 ["first-name","Lucía","Lucía is a feminine given name in Spanish. Meaning: Light. From Latin lux.","From Latin lux.",1],
 ["first-name","Miguel","Miguel is a masculine given name in Spanish. Meaning: Who is like God?. The Spanish form of Michael.","The Spanish form of Michael.",1],
 ["surname","García","García is a Spanish family name. Of debated origin — the most common Spanish surname.","Of debated origin — the most common Spanish surname.",2],
 ["surname","Fernández","Fernández is a Spanish family name. 'Son of Fernando' — patronymic -ez.","'Son of Fernando' — patronymic -ez.",2],
 ["surname","López","López is a Spanish family name. 'Son of Lope' — patronymic -ez.","'Son of Lope' — patronymic -ez.",2],
 ["surname","Martínez","Martínez is a Spanish family name. 'Son of Martín' — patronymic -ez.","'Son of Martín' — patronymic -ez.",2],
 ["place-name","Madrid","Madrid - From Mayrit, the Moorish settlement name.","From Mayrit, the Moorish settlement name.",2],
 ["place-name","Barcelona","Barcelona - From Barcino, the Roman colony.","From Barcino, the Roman colony.",2],
 ["naming-convention","Two surnames","Two surnames: Traditionally the father's first surname then the mother's first surname.","Traditionally the father's first surname then the mother's first surname.",3],
 ["naming-convention","-ez patronymics","-ez patronymics: Fernandez, Lopez, and Martinez began as 'son of'.","Fernandez, Lopez, and Martinez began as 'son of'.",3]
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
  var esc="JAH-NMS2-".replace(/[.*+?^${}()|[\]\\]/g,'\\$&');
  if(!new RegExp('^'+esc+'\\d{6}$').test(r.id||''))e.push('id');
  if(typeof r.name!=='string'||!r.name.length)e.push('name');
  if(typeof r.meaning!=='string'||!r.meaning.length)e.push('meaning');
  if(typeof r.title!=='string'||!r.title.length)e.push('title');
  if(CATS.indexOf(r.category)<0)e.push('category');
  if(!(r.ladder_rank>=1&&r.ladder_rank<=3))e.push('ladder_rank');
  return {ok:!e.length,errors:e};
}
var gen={version:"jahdb-names-spanish-1.0",generate:generate,validate:validate};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("names-spanish",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
