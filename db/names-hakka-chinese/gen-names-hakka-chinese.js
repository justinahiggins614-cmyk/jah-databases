(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var CATS=["first-name", "surname", "place-name", "naming-convention"];
var PREFIX="JAH-NMHC-";
/* rows: [category, display name, meaning, origin, ladder_rank] */
var B=[
 ["first-name","Wei 伟","Wei (伟) is a masculine given name in Hakka Chinese. Meaning: Great..","Great.",1],
 ["first-name","Lan 兰","Lan (兰) is a feminine given name in Hakka Chinese. Meaning: Orchid..","Orchid.",1],
 ["first-name","Jian 健","Jian (健) is a masculine given name in Hakka Chinese. Meaning: Healthy..","Healthy.",1],
 ["first-name","Mei 梅","Mei (梅) is a feminine given name in Hakka Chinese. Meaning: Plum blossom..","Plum blossom.",1],
 ["first-name","Qiang 强","Qiang (强) is a masculine given name in Hakka Chinese. Meaning: Strong..","Strong.",1],
 ["first-name","Hui 慧","Hui (慧) is a feminine given name in Hakka Chinese. Meaning: Wise..","Wise.",1],
 ["first-name","Fu 福","Fu (福) is a masculine given name in Hakka Chinese. Meaning: Fortune..","Fortune.",1],
 ["surname","Chen 陈","Chen (陈) is a Hakka Chinese family name. An ancient state name.","An ancient state name.",2],
 ["surname","Huang 黄","Huang (黄) is a Hakka Chinese family name. 'Yellow'.","'Yellow'.",2],
 ["surname","Liu 刘","Liu (刘) is a Hakka Chinese family name. Ancient imperial surname.","Ancient imperial surname.",2],
 ["surname","Lin 林","Lin (林) is a Hakka Chinese family name. 'Forest'.","'Forest'.",2],
 ["place-name","Meizhou 梅州","Meizhou (梅州) - 'Plum prefecture' — the Hakka heartland.","'Plum prefecture' — the Hakka heartland.",2],
 ["place-name","Ganzhou","Ganzhou - A historic Hakka-region city.","A historic Hakka-region city.",2],
 ["naming-convention","Family name first","Family name first: The surname leads, as across Chinese languages.","The surname leads, as across Chinese languages.",3],
 ["naming-convention","Hakka romanizations","Hakka romanizations: Chen is often spelled Chan in Hakka romanization.","Chen is often spelled Chan in Hakka romanization.",3]
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
  var esc="JAH-NMHC-".replace(/[.*+?^${}()|[\]\\]/g,'\\$&');
  if(!new RegExp('^'+esc+'\\d{6}$').test(r.id||''))e.push('id');
  if(typeof r.name!=='string'||!r.name.length)e.push('name');
  if(typeof r.meaning!=='string'||!r.meaning.length)e.push('meaning');
  if(typeof r.title!=='string'||!r.title.length)e.push('title');
  if(CATS.indexOf(r.category)<0)e.push('category');
  if(!(r.ladder_rank>=1&&r.ladder_rank<=3))e.push('ladder_rank');
  return {ok:!e.length,errors:e};
}
var gen={version:"jahdb-names-hakka-chinese-1.0",generate:generate,validate:validate};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("names-hakka-chinese",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
