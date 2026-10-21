(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var CATS=["first-name", "surname", "place-name", "naming-convention"];
var PREFIX="JAH-NMMC-";
/* rows: [category, display name, meaning, origin, ladder_rank] */
var B=[
 ["first-name","Wei 伟","Wei (伟) is a masculine given name in Mandarin Chinese. Meaning: Great. A leading character in boys' names, chosen for strength.","A leading character in boys' names, chosen for strength.",1],
 ["first-name","Fang 芳","Fang (芳) is a feminine given name in Mandarin Chinese. Meaning: Fragrant. A classic character in girls' names, evoking flowers.","A classic character in girls' names, evoking flowers.",1],
 ["first-name","Lei 磊","Lei (磊) is a masculine given name in Mandarin Chinese. Meaning: Piles of stone; steadfast. Built from three 'stone' characters; suggests firmness.","Built from three 'stone' characters; suggests firmness.",1],
 ["first-name","Min 敏","Min (敏) is a unisex given name in Mandarin Chinese. Meaning: Quick, clever. A popular unisex character meaning agile of mind.","A popular unisex character meaning agile of mind.",1],
 ["first-name","Jing 静","Jing (静) is a feminine given name in Mandarin Chinese. Meaning: Quiet, calm. Favored for girls; suggests composure.","Favored for girls; suggests composure.",1],
 ["first-name","Tao 涛","Tao (涛) is a masculine given name in Mandarin Chinese. Meaning: Great waves. Evokes the ocean's power; common in boys' names.","Evokes the ocean's power; common in boys' names.",1],
 ["first-name","Xin 欣","Xin (欣) is a feminine given name in Mandarin Chinese. Meaning: Joyful. Suggests happiness and delight.","Suggests happiness and delight.",1],
 ["surname","Wang 王","Wang (王) is a Mandarin Chinese family name. 'King' — the most common Chinese surname.","'King' — the most common Chinese surname.",2],
 ["surname","Li 李","Li (李) is a Mandarin Chinese family name. 'Plum' — ancient surname of Tang emperors.","'Plum' — ancient surname of Tang emperors.",2],
 ["surname","Zhang 张","Zhang (张) is a Mandarin Chinese family name. 'To stretch (a bow)' — from an archery term.","'To stretch (a bow)' — from an archery term.",2],
 ["surname","Liu 刘","Liu (刘) is a Mandarin Chinese family name. Ancient surname of Han emperors.","Ancient surname of Han emperors.",2],
 ["place-name","Beijing 北京","Beijing (北京) - 'Northern capital' — named for its position.","'Northern capital' — named for its position.",2],
 ["place-name","Shanghai 上海","Shanghai (上海) - 'Above the sea' — the city by the water.","'Above the sea' — the city by the water.",2],
 ["naming-convention","Family name first","Family name first: Wang Wei is Mr. Wang: the surname comes first, the given name second.","Wang Wei is Mr. Wang: the surname comes first, the given name second.",3],
 ["naming-convention","Generation names","Generation names: Siblings often share one generation character, chosen for their whole generation.","Siblings often share one generation character, chosen for their whole generation",3]
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
  var esc="JAH-NMMC-".replace(/[.*+?^${}()|[\]\\]/g,'\\$&');
  if(!new RegExp('^'+esc+'\\d{6}$').test(r.id||''))e.push('id');
  if(typeof r.name!=='string'||!r.name.length)e.push('name');
  if(typeof r.meaning!=='string'||!r.meaning.length)e.push('meaning');
  if(typeof r.title!=='string'||!r.title.length)e.push('title');
  if(CATS.indexOf(r.category)<0)e.push('category');
  if(!(r.ladder_rank>=1&&r.ladder_rank<=3))e.push('ladder_rank');
  return {ok:!e.length,errors:e};
}
var gen={version:"jahdb-names-mandarin-chinese-1.0",generate:generate,validate:validate};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("names-mandarin-chinese",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
