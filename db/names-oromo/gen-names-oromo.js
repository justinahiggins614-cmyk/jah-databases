(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var CATS=["first-name", "surname", "place-name", "naming-convention"];
var PREFIX="JAH-NMO2-";
/* rows: [category, display name, meaning, origin, ladder_rank] */
var B=[
 ["first-name","Chaltu","Chaltu is a feminine given name in Oromo. Meaning: A classic Oromo girls' name..","A classic Oromo girls' name.",1],
 ["first-name","Tolosa","Tolosa is a masculine given name in Oromo. Meaning: A classic Oromo boys' name..","A classic Oromo boys' name.",1],
 ["first-name","Girma","Girma is a masculine given name in Oromo. Meaning: Amazing..","Amazing.",1],
 ["first-name","Ayantu","Ayantu is a feminine given name in Oromo. Meaning: A popular girls' name..","A popular girls' name.",1],
 ["first-name","Diba","Diba is a masculine given name in Oromo. Meaning: A traditional boys' name..","A traditional boys' name.",1],
 ["first-name","Kuwee","Kuwee is a feminine given name in Oromo. Meaning: A graceful girls' name..","A graceful girls' name.",1],
 ["first-name","Lensa","Lensa is a feminine given name in Oromo. Meaning: A popular girls' name..","A popular girls' name.",1],
 ["surname","Father's name as second name","Father's name as second name is a Oromo family name. The father's given name serves as the second name.","The father's given name serves as the second name.",2],
 ["surname","No inherited surnames traditionally","No inherited surnames traditionally is a Oromo family name. Family names are a modern layer.","Family names are a modern layer.",2],
 ["surname","Circumstance names","Circumstance names is a Oromo family name. Names may record the circumstances of birth.","Names may record the circumstances of birth.",2],
 ["surname","Gadaa generation names","Gadaa generation names is a Oromo family name. The gadaa age-grade system marks generations.","The gadaa age-grade system marks generations.",2],
 ["place-name","Addis Ababa","Addis Ababa - 'New flower' — the capital in Oromo lands.","'New flower' — the capital in Oromo lands.",2],
 ["place-name","Adama","Adama - A major Oromo city.","A major Oromo city.",2],
 ["naming-convention","Father's name as second name","Father's name as second name: Identity chains through the father's given name.","Identity chains through the father's given name.",3],
 ["naming-convention","Meaningful circumstance names","Meaningful circumstance names: Names often record when or how a child was born.","Names often record when or how a child was born.",3]
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
  var esc="JAH-NMO2-".replace(/[.*+?^${}()|[\]\\]/g,'\\$&');
  if(!new RegExp('^'+esc+'\\d{6}$').test(r.id||''))e.push('id');
  if(typeof r.name!=='string'||!r.name.length)e.push('name');
  if(typeof r.meaning!=='string'||!r.meaning.length)e.push('meaning');
  if(typeof r.title!=='string'||!r.title.length)e.push('title');
  if(CATS.indexOf(r.category)<0)e.push('category');
  if(!(r.ladder_rank>=1&&r.ladder_rank<=3))e.push('ladder_rank');
  return {ok:!e.length,errors:e};
}
var gen={version:"jahdb-names-oromo-1.0",generate:generate,validate:validate};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("names-oromo",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
