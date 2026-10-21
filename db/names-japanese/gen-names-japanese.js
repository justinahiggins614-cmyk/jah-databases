(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var CATS=["first-name", "surname", "place-name", "naming-convention"];
var PREFIX="JAH-NMJ-";
/* rows: [category, display name, meaning, origin, ladder_rank] */
var B=[
 ["first-name","Haruto 陽翔","Haruto (陽翔) is a masculine given name in Japanese. Meaning: Sunlight + to soar. A top-ranked modern boys' name; meaning depends on the kanji chosen.","A top-ranked modern boys' name; meaning depends on the kanji chosen.",1],
 ["first-name","Sakura 桜","Sakura (桜) is a feminine given name in Japanese. Meaning: Cherry blossom. Evokes spring and renewal; a classic girls' name.","Evokes spring and renewal; a classic girls' name.",1],
 ["first-name","Ren 蓮","Ren (蓮) is a unisex given name in Japanese. Meaning: Lotus. A unisex name from the lotus flower, symbol of purity.","A unisex name from the lotus flower, symbol of purity.",1],
 ["first-name","Aiko 愛子","Aiko (愛子) is a feminine given name in Japanese. Meaning: Beloved child. Combines 'love' with the traditional -ko ending.","Combines 'love' with the traditional -ko ending.",1],
 ["first-name","Kenji 健二","Kenji (健二) is a masculine given name in Japanese. Meaning: Healthy second son. A traditional boys' name; the second character once marked birth order.","A traditional boys' name; the second character once marked birth order.",1],
 ["first-name","Yuki 雪","Yuki (雪) is a feminine given name in Japanese. Meaning: Snow. Also written 幸 ('happiness') for boys — kanji fixes the meaning.","Also written 幸 ('happiness') for boys — kanji fixes the meaning.",1],
 ["first-name","Daiki 大輝","Daiki (大輝) is a masculine given name in Japanese. Meaning: Great radiance. A strong modern boys' name.","A strong modern boys' name.",1],
 ["surname","Tanaka 田中","Tanaka (田中) is a Japanese family name. 'Middle of the rice field' — the most common Japanese surname.","'Middle of the rice field' — the most common Japanese surname.",2],
 ["surname","Suzuki 鈴木","Suzuki (鈴木) is a Japanese family name. 'Bell tree'.","'Bell tree'.",2],
 ["surname","Sato 佐藤","Sato (佐藤) is a Japanese family name. 'Help' + 'wisteria'.","'Help' + 'wisteria'.",2],
 ["surname","Yamamoto 山本","Yamamoto (山本) is a Japanese family name. 'Base of the mountain'.","'Base of the mountain'.",2],
 ["place-name","Tokyo 東京","Tokyo (東京) - 'Eastern capital' — renamed from Edo in 1868.","'Eastern capital' — renamed from Edo in 1868.",2],
 ["place-name","Kyoto 京都","Kyoto (京都) - 'Capital city' — the imperial capital for a thousand years.","'Capital city' — the imperial capital for a thousand years.",2],
 ["naming-convention","Family name first","Family name first: Tanaka Haruto is Mr. Tanaka: surname first in Japanese order.","Tanaka Haruto is Mr. Tanaka: surname first in Japanese order.",3],
 ["naming-convention","Kanji fixes meaning","Kanji fixes meaning: Parents choose kanji for meaning and stroke count; the same sound can carry many meanings.","Parents choose kanji for meaning and stroke count; the same sound can carry many",3]
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
  var esc="JAH-NMJ-".replace(/[.*+?^${}()|[\]\\]/g,'\\$&');
  if(!new RegExp('^'+esc+'\\d{6}$').test(r.id||''))e.push('id');
  if(typeof r.name!=='string'||!r.name.length)e.push('name');
  if(typeof r.meaning!=='string'||!r.meaning.length)e.push('meaning');
  if(typeof r.title!=='string'||!r.title.length)e.push('title');
  if(CATS.indexOf(r.category)<0)e.push('category');
  if(!(r.ladder_rank>=1&&r.ladder_rank<=3))e.push('ladder_rank');
  return {ok:!e.length,errors:e};
}
var gen={version:"jahdb-names-japanese-1.0",generate:generate,validate:validate};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("names-japanese",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
