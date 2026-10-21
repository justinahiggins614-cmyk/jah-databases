(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var CATS=["first-name", "surname", "place-name", "naming-convention"];
var PREFIX="JAH-NMK3-";
/* rows: [category, display name, meaning, origin, ladder_rank] */
var B=[
 ["first-name","Alan","Alan is a masculine given name in Kurdish. Meaning: A classic Kurdish boys' name..","A classic Kurdish boys' name.",1],
 ["first-name","Dilan","Dilan is a unisex given name in Kurdish. Meaning: Hearts. Unisex; evokes feeling.","Unisex; evokes feeling.",1],
 ["first-name","Rojin","Rojin is a feminine given name in Kurdish. Meaning: A poetic girls' name..","A poetic girls' name.",1],
 ["first-name","Berfin","Berfin is a feminine given name in Kurdish. Meaning: Snowdrop. The early flower; a beloved girls' name.","The early flower; a beloved girls' name.",1],
 ["first-name","Azad","Azad is a masculine given name in Kurdish. Meaning: Free.. A name of hope and freedom.","A name of hope and freedom.",1],
 ["first-name","Jiyan","Jiyan is a feminine given name in Kurdish. Meaning: Life.. A graceful girls' name.","A graceful girls' name.",1],
 ["first-name","Hawre","Hawre is a masculine given name in Kurdish. Meaning: A classic boys' name..","A classic boys' name.",1],
 ["surname","Tribal names","Tribal names is a Kurdish family name. Many Kurds carry tribal or geographic names rather than inherited surnames.","Many Kurds carry tribal or geographic names rather than inherited surnames.",2],
 ["surname","No fixed surnames traditionally","No fixed surnames traditionally is a Kurdish family name. Family names are a modern administrative layer.","Family names are a modern administrative layer.",2],
 ["surname","Nature names","Nature names is a Kurdish family name. Berfin (snowdrop) and Rojin exemplify the nature pool.","Berfin (snowdrop) and Rojin exemplify the nature pool.",2],
 ["surname","Hope names","Hope names is a Kurdish family name. Azad ('free') and Jiyan ('life') name aspirations.","Azad ('free') and Jiyan ('life') name aspirations.",2],
 ["place-name","Diyarbakir","Diyarbakir - The great Kurdish-majority city of the Tigris.","The great Kurdish-majority city of the Tigris.",2],
 ["place-name","Erbil","Erbil - From ancient Arbela — one of the world's oldest cities.","From ancient Arbela — one of the world's oldest cities.",2],
 ["naming-convention","Nature and hope names","Nature and hope names: Kurdish names favor nature (snowdrop, moon) and hope (free, life).","Kurdish names favor nature (snowdrop, moon) and hope (free, life).",3],
 ["naming-convention","Tribal and geographic names","Tribal and geographic names: Identity often runs through tribe or hometown, not surname.","Identity often runs through tribe or hometown, not surname.",3]
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
  var esc="JAH-NMK3-".replace(/[.*+?^${}()|[\]\\]/g,'\\$&');
  if(!new RegExp('^'+esc+'\\d{6}$').test(r.id||''))e.push('id');
  if(typeof r.name!=='string'||!r.name.length)e.push('name');
  if(typeof r.meaning!=='string'||!r.meaning.length)e.push('meaning');
  if(typeof r.title!=='string'||!r.title.length)e.push('title');
  if(CATS.indexOf(r.category)<0)e.push('category');
  if(!(r.ladder_rank>=1&&r.ladder_rank<=3))e.push('ladder_rank');
  return {ok:!e.length,errors:e};
}
var gen={version:"jahdb-names-kurdish-1.0",generate:generate,validate:validate};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("names-kurdish",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
