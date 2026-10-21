(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var CATS=["first-name", "surname", "place-name", "naming-convention"];
var PREFIX="JAH-NMO-";
/* rows: [category, display name, meaning, origin, ladder_rank] */
var B=[
 ["first-name","Jagannath ଜଗନ୍ନାଥ","Jagannath (ଜଗନ୍ନାଥ) is a masculine given name in Odia. Meaning: Lord of the universe. The presiding deity of Puri; a leading boys' name.","The presiding deity of Puri; a leading boys' name.",1],
 ["first-name","Subhadra","Subhadra is a feminine given name in Odia. Meaning: Auspicious. Sister of Krishna in tradition.","Sister of Krishna in tradition.",1],
 ["first-name","Biju","Biju is a masculine given name in Odia. Meaning: A classic Odia boys' name..","A classic Odia boys' name.",1],
 ["first-name","Sasmita","Sasmita is a feminine given name in Odia. Meaning: Smiling. A popular girls' name.","A popular girls' name.",1],
 ["first-name","Prakash","Prakash is a masculine given name in Odia. Meaning: Light. From Sanskrit.","From Sanskrit.",1],
 ["first-name","Mamata","Mamata is a feminine given name in Odia. Meaning: Affection. From Sanskrit.","From Sanskrit.",1],
 ["first-name","Debasish","Debasish is a masculine given name in Odia. Meaning: Blessing of the gods..","Blessing of the gods.",1],
 ["surname","Mohanty","Mohanty is a Odia family name. A traditional title, 'great minister'.","A traditional title, 'great minister'.",2],
 ["surname","Das","Das is a Odia family name. 'Servant (of God)' — devotional.","'Servant (of God)' — devotional.",2],
 ["surname","Mishra","Mishra is a Odia family name. A Brahmin title.","A Brahmin title.",2],
 ["surname","Pattnaik","Pattnaik is a Odia family name. A traditional title.","A traditional title.",2],
 ["place-name","Bhubaneswar","Bhubaneswar - 'Lord of the universe' — the temple city.","'Lord of the universe' — the temple city.",2],
 ["place-name","Cuttack","Cuttack - From Kataka, 'fort'.","From Kataka, 'fort'.",2],
 ["naming-convention","Given + family name","Given + family name: Odia names run given name first, family name last.","Odia names run given name first, family name last.",3],
 ["naming-convention","Temple-town names","Temple-town names: Children are often named for deities of local temples.","Children are often named for deities of local temples.",3]
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
  var esc="JAH-NMO-".replace(/[.*+?^${}()|[\]\\]/g,'\\$&');
  if(!new RegExp('^'+esc+'\\d{6}$').test(r.id||''))e.push('id');
  if(typeof r.name!=='string'||!r.name.length)e.push('name');
  if(typeof r.meaning!=='string'||!r.meaning.length)e.push('meaning');
  if(typeof r.title!=='string'||!r.title.length)e.push('title');
  if(CATS.indexOf(r.category)<0)e.push('category');
  if(!(r.ladder_rank>=1&&r.ladder_rank<=3))e.push('ladder_rank');
  return {ok:!e.length,errors:e};
}
var gen={version:"jahdb-names-odia-1.0",generate:generate,validate:validate};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("names-odia",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
