(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var CATS=["first-name", "surname", "place-name", "naming-convention"];
var PREFIX="JAH-NMV-";
/* rows: [category, display name, meaning, origin, ladder_rank] */
var B=[
 ["first-name","Anh 英","Anh (英) is a unisex given name in Vietnamese. Meaning: Bright; hero. A leading unisex name.","A leading unisex name.",1],
 ["first-name","Linh","Linh is a feminine given name in Vietnamese. Meaning: Spirit. A graceful girls' name.","A graceful girls' name.",1],
 ["first-name","Minh","Minh is a masculine given name in Vietnamese. Meaning: Bright. A classic boys' name.","A classic boys' name.",1],
 ["first-name","Lan","Lan is a feminine given name in Vietnamese. Meaning: Orchid. A delicate girls' name.","A delicate girls' name.",1],
 ["first-name","Duc Đức","Duc (Đức) is a masculine given name in Vietnamese. Meaning: Virtue. A traditional boys' name.","A traditional boys' name.",1],
 ["first-name","Huong","Huong is a feminine given name in Vietnamese. Meaning: Fragrance. A popular girls' name.","A popular girls' name.",1],
 ["first-name","Bao","Bao is a masculine given name in Vietnamese. Meaning: Treasure. A cherished boys' name.","A cherished boys' name.",1],
 ["surname","Nguyen 阮","Nguyen (阮) is a Vietnamese family name. The most common Vietnamese surname — borne by about 40% of the population.","The most common Vietnamese surname — borne by about 40% of the population.",2],
 ["surname","Tran 陳","Tran (陳) is a Vietnamese family name. The Tran dynasty's name.","The Tran dynasty's name.",2],
 ["surname","Le 黎","Le (黎) is a Vietnamese family name. The Le dynasty's name.","The Le dynasty's name.",2],
 ["surname","Pham 范","Pham (范) is a Vietnamese family name. A widespread surname.","A widespread surname.",2],
 ["place-name","Hanoi 河内","Hanoi (河内) - 'Inside the river' — between the Red River's branches.","'Inside the river' — between the Red River's branches.",2],
 ["place-name","Hue","Hue - From Thuan Hoa, the old imperial capital region.","From Thuan Hoa, the old imperial capital region.",2],
 ["naming-convention","Family + middle + given","Family + middle + given: Nguyen Thi Lan: surname first, then middle, then given name.","Nguyen Thi Lan: surname first, then middle, then given name.",3],
 ["naming-convention","Thi and Van","Thi and Van: Thi marks many women's middle names; Van marks many men's.","Thi marks many women's middle names; Van marks many men's.",3]
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
  var esc="JAH-NMV-".replace(/[.*+?^${}()|[\]\\]/g,'\\$&');
  if(!new RegExp('^'+esc+'\\d{6}$').test(r.id||''))e.push('id');
  if(typeof r.name!=='string'||!r.name.length)e.push('name');
  if(typeof r.meaning!=='string'||!r.meaning.length)e.push('meaning');
  if(typeof r.title!=='string'||!r.title.length)e.push('title');
  if(CATS.indexOf(r.category)<0)e.push('category');
  if(!(r.ladder_rank>=1&&r.ladder_rank<=3))e.push('ladder_rank');
  return {ok:!e.length,errors:e};
}
var gen={version:"jahdb-names-vietnamese-1.0",generate:generate,validate:validate};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("names-vietnamese",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
