(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var CATS=["first-name", "surname", "place-name", "naming-convention"];
var PREFIX="JAH-NMF-";
/* rows: [category, display name, meaning, origin, ladder_rank] */
var B=[
 ["first-name","Pierre","Pierre is a masculine given name in French. Meaning: Stone. From Greek petros; the French form of Peter.","From Greek petros; the French form of Peter.",1],
 ["first-name","Marie","Marie is a feminine given name in French. Meaning: Beloved. The French form of Mary; long the top girls' name.","The French form of Mary; long the top girls' name.",1],
 ["first-name","Jean","Jean is a masculine given name in French. Meaning: God is gracious. From Hebrew Yochanan.","From Hebrew Yochanan.",1],
 ["first-name","Sophie","Sophie is a feminine given name in French. Meaning: Wisdom. From Greek sophia.","From Greek sophia.",1],
 ["first-name","Louis","Louis is a masculine given name in French. Meaning: Famous warrior. From Germanic Chlodwig; borne by French kings.","From Germanic Chlodwig; borne by French kings.",1],
 ["first-name","Camille","Camille is a unisex given name in French. Meaning: Unisex name of Roman origin..","Unisex name of Roman origin.",1],
 ["first-name","Hugo","Hugo is a masculine given name in French. Meaning: Mind. From Germanic hug, 'thought'.","From Germanic hug, 'thought'.",1],
 ["surname","Martin","Martin is a French family name. 'Of Mars' — from the Roman god of war.","'Of Mars' — from the Roman god of war.",2],
 ["surname","Bernard","Bernard is a French family name. 'Brave bear' — from Germanic.","'Brave bear' — from Germanic.",2],
 ["surname","Dubois","Dubois is a French family name. 'Of the wood' — a place-based surname.","'Of the wood' — a place-based surname.",2],
 ["surname","Laurent","Laurent is a French family name. From Laurentius, 'of Laurentum'.","From Laurentius, 'of Laurentum'.",2],
 ["place-name","Paris","Paris - From the Parisii, the Celtic tribe of the area.","From the Parisii, the Celtic tribe of the area.",2],
 ["place-name","Lyon","Lyon - From Lugdunum, 'fort of the god Lugus'.","From Lugdunum, 'fort of the god Lugus'.",2],
 ["naming-convention","Prénom + nom","Prénom + nom: French names run given name (prénom) first, family name (nom) last.","French names run given name (prénom) first, family name (nom) last.",3],
 ["naming-convention","Saints' names","Saints' names: Children were long named for saints, whose feast days marked the calendar.","Children were long named for saints, whose feast days marked the calendar.",3]
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
  var esc="JAH-NMF-".replace(/[.*+?^${}()|[\]\\]/g,'\\$&');
  if(!new RegExp('^'+esc+'\\d{6}$').test(r.id||''))e.push('id');
  if(typeof r.name!=='string'||!r.name.length)e.push('name');
  if(typeof r.meaning!=='string'||!r.meaning.length)e.push('meaning');
  if(typeof r.title!=='string'||!r.title.length)e.push('title');
  if(CATS.indexOf(r.category)<0)e.push('category');
  if(!(r.ladder_rank>=1&&r.ladder_rank<=3))e.push('ladder_rank');
  return {ok:!e.length,errors:e};
}
var gen={version:"jahdb-names-french-1.0",generate:generate,validate:validate};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("names-french",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
