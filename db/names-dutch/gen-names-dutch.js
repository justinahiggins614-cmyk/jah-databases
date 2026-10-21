(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var CATS=["first-name", "surname", "place-name", "naming-convention"];
var PREFIX="JAH-NMD2-";
/* rows: [category, display name, meaning, origin, ladder_rank] */
var B=[
 ["first-name","Jan","Jan is a masculine given name in Dutch. Meaning: God is gracious. The Dutch form of John.","The Dutch form of John.",1],
 ["first-name","Maria","Maria is a feminine given name in Dutch. Meaning: Beloved..","Beloved.",1],
 ["first-name","Pieter","Pieter is a masculine given name in Dutch. Meaning: Stone. The Dutch form of Peter.","The Dutch form of Peter.",1],
 ["first-name","Anna","Anna is a feminine given name in Dutch. Meaning: Grace..","Grace.",1],
 ["first-name","Willem","Willem is a masculine given name in Dutch. Meaning: Resolute protector. The Dutch form of William.","The Dutch form of William.",1],
 ["first-name","Sophie","Sophie is a feminine given name in Dutch. Meaning: Wisdom..","Wisdom.",1],
 ["first-name","Lars","Lars is a masculine given name in Dutch. Meaning: Crowned with laurel.. From Laurentius.","From Laurentius.",1],
 ["surname","Jansen","Jansen is a Dutch family name. 'Son of Jan' — the -sen patronymic.","'Son of Jan' — the -sen patronymic.",2],
 ["surname","De Vries","De Vries is a Dutch family name. 'The Frisian'.","'The Frisian'.",2],
 ["surname","Van den Berg","Van den Berg is a Dutch family name. 'From the mountain'.","'From the mountain'.",2],
 ["surname","Bakker","Bakker is a Dutch family name. 'Baker' — occupational.","'Baker' — occupational.",2],
 ["place-name","Amsterdam","Amsterdam - 'Dam on the Amstel'.","'Dam on the Amstel'.",2],
 ["place-name","Rotterdam","Rotterdam - 'Dam on the Rotte'.","'Dam on the Rotte'.",2],
 ["naming-convention","-sen patronymics","-sen patronymics: Jansen, Pietersen: 'son of' frozen into surnames.","Jansen, Pietersen: 'son of' frozen into surnames.",3],
 ["naming-convention","Van, van der, van den","Van, van der, van den: 'From', 'from the': Van den Berg, Van Dijk ('from the dike').","'From', 'from the': Van den Berg, Van Dijk ('from the dike').",3]
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
  var esc="JAH-NMD2-".replace(/[.*+?^${}()|[\]\\]/g,'\\$&');
  if(!new RegExp('^'+esc+'\\d{6}$').test(r.id||''))e.push('id');
  if(typeof r.name!=='string'||!r.name.length)e.push('name');
  if(typeof r.meaning!=='string'||!r.meaning.length)e.push('meaning');
  if(typeof r.title!=='string'||!r.title.length)e.push('title');
  if(CATS.indexOf(r.category)<0)e.push('category');
  if(!(r.ladder_rank>=1&&r.ladder_rank<=3))e.push('ladder_rank');
  return {ok:!e.length,errors:e};
}
var gen={version:"jahdb-names-dutch-1.0",generate:generate,validate:validate};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("names-dutch",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
