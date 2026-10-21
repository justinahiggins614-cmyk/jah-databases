(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var CATS=["first-name", "surname", "place-name", "naming-convention"];
var PREFIX="JAH-NMK-";
/* rows: [category, display name, meaning, origin, ladder_rank] */
var B=[
 ["first-name","Min-jun 민준","Min-jun (민준) is a masculine given name in Korean. Meaning: Clever + handsome. Meaning fixed by the hanja chosen; a top boys' name.","Meaning fixed by the hanja chosen; a top boys' name.",1],
 ["first-name","Seo-yeon 서연","Seo-yeon (서연) is a feminine given name in Korean. Meaning: Auspicious + beautiful. A leading girls' name.","A leading girls' name.",1],
 ["first-name","Ji-hoon 지훈","Ji-hoon (지훈) is a masculine given name in Korean. Meaning: Wisdom + merit. A classic boys' name.","A classic boys' name.",1],
 ["first-name","Ha-eun 하은","Ha-eun (하은) is a feminine given name in Korean. Meaning: Summer + silver. A modern girls' name.","A modern girls' name.",1],
 ["first-name","Dong-hyun 동현","Dong-hyun (동현) is a masculine given name in Korean. Meaning: East + virtuous. A traditional-style boys' name.","A traditional-style boys' name.",1],
 ["first-name","Su-ah 수아","Su-ah (수아) is a feminine given name in Korean. Meaning: Excellent + beautiful. A modern girls' name.","A modern girls' name.",1],
 ["first-name","Tae-yang 태양","Tae-yang (태양) is a masculine given name in Korean. Meaning: Sun. A bold boys' name.","A bold boys' name.",1],
 ["surname","Kim 김","Kim (김) is a Korean family name. 'Gold' — from the character 金; the most common Korean surname.","'Gold' — from the character 金; the most common Korean surname.",2],
 ["surname","Lee 이","Lee (이) is a Korean family name. 'Plum' — from 李.","'Plum' — from 李.",2],
 ["surname","Park 박","Park (박) is a Korean family name. From 朴.","From 朴.",2],
 ["surname","Choi 최","Choi (최) is a Korean family name. From 崔.","From 崔.",2],
 ["place-name","Seoul 서울","Seoul (서울) - 'Capital' — the name simply means the capital city.","'Capital' — the name simply means the capital city.",2],
 ["place-name","Busan 부산","Busan (부산) - 'Cauldron mountain'.","'Cauldron mountain'.",2],
 ["naming-convention","Family name first","Family name first: Kim Min-jun is Mr. Kim: one-syllable surname first.","Kim Min-jun is Mr. Kim: one-syllable surname first.",3],
 ["naming-convention","Dollimja generation syllable","Dollimja generation syllable: Siblings often share one syllable of the given name, marking their generation.","Siblings often share one syllable of the given name, marking their generation.",3]
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
  var esc="JAH-NMK-".replace(/[.*+?^${}()|[\]\\]/g,'\\$&');
  if(!new RegExp('^'+esc+'\\d{6}$').test(r.id||''))e.push('id');
  if(typeof r.name!=='string'||!r.name.length)e.push('name');
  if(typeof r.meaning!=='string'||!r.meaning.length)e.push('meaning');
  if(typeof r.title!=='string'||!r.title.length)e.push('title');
  if(CATS.indexOf(r.category)<0)e.push('category');
  if(!(r.ladder_rank>=1&&r.ladder_rank<=3))e.push('ladder_rank');
  return {ok:!e.length,errors:e};
}
var gen={version:"jahdb-names-korean-1.0",generate:generate,validate:validate};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("names-korean",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
