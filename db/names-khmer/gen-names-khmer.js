(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var CATS=["first-name", "surname", "place-name", "naming-convention"];
var PREFIX="JAH-NMK4-";
/* rows: [category, display name, meaning, origin, ladder_rank] */
var B=[
 ["first-name","Sok សុខ","Sok (សុខ) is a unisex given name in Khmer. Meaning: Peace. Unisex; the most auspicious root.","Unisex; the most auspicious root.",1],
 ["first-name","Dara តារា","Dara (តារា) is a unisex given name in Khmer. Meaning: Star. Unisex; from Sanskrit tara.","Unisex; from Sanskrit tara.",1],
 ["first-name","Chan ចន្ទ","Chan (ចន្ទ) is a unisex given name in Khmer. Meaning: Moon. Unisex; from Sanskrit chandra.","Unisex; from Sanskrit chandra.",1],
 ["first-name","Malis","Malis is a feminine given name in Khmer. Meaning: Jasmine. A graceful girls' name.","A graceful girls' name.",1],
 ["first-name","Piseth","Piseth is a masculine given name in Khmer. Meaning: A classic boys' name..","A classic boys' name.",1],
 ["first-name","Srey","Srey is a feminine given name in Khmer. Meaning: Girl, woman. A traditional girls' name.","A traditional girls' name.",1],
 ["first-name","Vann","Vann is a unisex given name in Khmer. Meaning: A common unisex name..","A common unisex name.",1],
 ["surname","Family name first","Family name first is a Khmer family name. Hun Sen: Hun is the family name, Sen the given name.","Hun Sen: Hun is the family name, Sen the given name.",2],
 ["surname","Pali/Sanskrit roots","Pali/Sanskrit roots is a Khmer family name. Dara, Chan, and Sok draw on the classical pool.","Dara, Chan, and Sok draw on the classical pool.",2],
 ["surname","No gendered forms","No gendered forms is a Khmer family name. The same names serve all genders.","The same names serve all genders.",2],
 ["surname","Auspicious meanings","Auspicious meanings is a Khmer family name. Peace, star, and moon dominate.","Peace, star, and moon dominate.",2],
 ["place-name","Phnom Penh","Phnom Penh - 'Penh's hill' — named for Lady Penh.","'Penh's hill' — named for Lady Penh.",2],
 ["place-name","Siem Reap","Siem Reap - 'Siam defeated' — the temple city.","'Siam defeated' — the temple city.",2],
 ["naming-convention","Family name first","Family name first: The surname precedes the given name in Khmer order.","The surname precedes the given name in Khmer order.",3],
 ["naming-convention","Auspicious Pali/Sanskrit roots","Auspicious Pali/Sanskrit roots: Names draw on peace, light, and celestial meanings.","Names draw on peace, light, and celestial meanings.",3]
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
  var esc="JAH-NMK4-".replace(/[.*+?^${}()|[\]\\]/g,'\\$&');
  if(!new RegExp('^'+esc+'\\d{6}$').test(r.id||''))e.push('id');
  if(typeof r.name!=='string'||!r.name.length)e.push('name');
  if(typeof r.meaning!=='string'||!r.meaning.length)e.push('meaning');
  if(typeof r.title!=='string'||!r.title.length)e.push('title');
  if(CATS.indexOf(r.category)<0)e.push('category');
  if(!(r.ladder_rank>=1&&r.ladder_rank<=3))e.push('ladder_rank');
  return {ok:!e.length,errors:e};
}
var gen={version:"jahdb-names-khmer-1.0",generate:generate,validate:validate};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("names-khmer",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
