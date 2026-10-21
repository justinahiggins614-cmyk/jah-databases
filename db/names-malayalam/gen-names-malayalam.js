(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var CATS=["first-name", "surname", "place-name", "naming-convention"];
var PREFIX="JAH-NMM3-";
/* rows: [category, display name, meaning, origin, ladder_rank] */
var B=[
 ["first-name","Mohan","Mohan is a masculine given name in Malayalam. Meaning: Charming. A name of Krishna.","A name of Krishna.",1],
 ["first-name","Lakshmi","Lakshmi is a feminine given name in Malayalam. Meaning: Goddess of fortune..","Goddess of fortune.",1],
 ["first-name","Ravi","Ravi is a masculine given name in Malayalam. Meaning: Sun..","Sun.",1],
 ["first-name","Anitha","Anitha is a feminine given name in Malayalam. Meaning: Grace..","Grace.",1],
 ["first-name","Suresh","Suresh is a masculine given name in Malayalam. Meaning: Ruler of gods..","Ruler of gods.",1],
 ["first-name","Rema","Rema is a feminine given name in Malayalam. Meaning: A classic Malayali girls' name..","A classic Malayali girls' name.",1],
 ["first-name","Vinod","Vinod is a masculine given name in Malayalam. Meaning: Pleasure, delight.. From Sanskrit.","From Sanskrit.",1],
 ["surname","Nair","Nair is a Malayalam family name. A traditional community title.","A traditional community title.",2],
 ["surname","Menon","Menon is a Malayalam family name. A traditional title, 'elder'.","A traditional title, 'elder'.",2],
 ["surname","Pillai","Pillai is a Malayalam family name. A traditional title, 'child (of status)'.","A traditional title, 'child (of status)'.",2],
 ["surname","Varma","Varma is a Malayalam family name. A royal title, 'armor'.","A royal title, 'armor'.",2],
 ["place-name","Kochi","Kochi - The port city — Cochin.","The port city — Cochin.",2],
 ["place-name","Thiruvananthapuram","Thiruvananthapuram - 'City of Lord Ananta'.","'City of Lord Ananta'.",2],
 ["naming-convention","House names","House names: The tharavad (ancestral house) name precedes the given name.","The tharavad (ancestral house) name precedes the given name.",3],
 ["naming-convention","Community surnames","Community surnames: Nair, Menon, and Pillai mark traditional community.","Nair, Menon, and Pillai mark traditional community.",3]
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
  var esc="JAH-NMM3-".replace(/[.*+?^${}()|[\]\\]/g,'\\$&');
  if(!new RegExp('^'+esc+'\\d{6}$').test(r.id||''))e.push('id');
  if(typeof r.name!=='string'||!r.name.length)e.push('name');
  if(typeof r.meaning!=='string'||!r.meaning.length)e.push('meaning');
  if(typeof r.title!=='string'||!r.title.length)e.push('title');
  if(CATS.indexOf(r.category)<0)e.push('category');
  if(!(r.ladder_rank>=1&&r.ladder_rank<=3))e.push('ladder_rank');
  return {ok:!e.length,errors:e};
}
var gen={version:"jahdb-names-malayalam-1.0",generate:generate,validate:validate};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("names-malayalam",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
