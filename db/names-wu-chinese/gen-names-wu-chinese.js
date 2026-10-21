(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var CATS=["first-name", "surname", "place-name", "naming-convention"];
var PREFIX="JAH-NMWC-";
/* rows: [category, display name, meaning, origin, ladder_rank] */
var B=[
 ["first-name","Wei 伟","Wei (伟) is a masculine given name in Wu Chinese. Meaning: Great. The Wu reading of the same character as Mandarin Wei.","The Wu reading of the same character as Mandarin Wei.",1],
 ["first-name","Fang 芳","Fang (芳) is a feminine given name in Wu Chinese. Meaning: Fragrant..","Fragrant.",1],
 ["first-name","Jian 健","Jian (健) is a masculine given name in Wu Chinese. Meaning: Healthy..","Healthy.",1],
 ["first-name","Li 丽","Li (丽) is a feminine given name in Wu Chinese. Meaning: Beautiful..","Beautiful.",1],
 ["first-name","Min 敏","Min (敏) is a unisex given name in Wu Chinese. Meaning: Quick, clever..","Quick, clever.",1],
 ["first-name","Qiang 强","Qiang (强) is a masculine given name in Wu Chinese. Meaning: Strong..","Strong.",1],
 ["first-name","Hui 慧","Hui (慧) is a feminine given name in Wu Chinese. Meaning: Wise..","Wise.",1],
 ["surname","Wang 王","Wang (王) is a Wu Chinese family name. 'King'.","'King'.",2],
 ["surname","Zhang 张","Zhang (张) is a Wu Chinese family name. 'To stretch (a bow)'.","'To stretch (a bow)'.",2],
 ["surname","Chen 陈","Chen (陈) is a Wu Chinese family name. An ancient state name.","An ancient state name.",2],
 ["surname","Xu 徐","Xu (徐) is a Wu Chinese family name. 'Slow, gentle'.","'Slow, gentle'.",2],
 ["place-name","Shanghai 上海","Shanghai (上海) - 'Above the sea' — the Wu-speaking metropolis.","'Above the sea' — the Wu-speaking metropolis.",2],
 ["place-name","Suzhou 苏州","Suzhou (苏州) - From the Wu region's old name.","From the Wu region's old name.",2],
 ["naming-convention","Family name first","Family name first: The surname leads, as across Chinese languages.","The surname leads, as across Chinese languages.",3],
 ["naming-convention","Shanghainese readings","Shanghainese readings: Wang is read 'Waon' in Shanghainese, not Wang.","Wang is read 'Waon' in Shanghainese, not Wang.",3]
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
  var esc="JAH-NMWC-".replace(/[.*+?^${}()|[\]\\]/g,'\\$&');
  if(!new RegExp('^'+esc+'\\d{6}$').test(r.id||''))e.push('id');
  if(typeof r.name!=='string'||!r.name.length)e.push('name');
  if(typeof r.meaning!=='string'||!r.meaning.length)e.push('meaning');
  if(typeof r.title!=='string'||!r.title.length)e.push('title');
  if(CATS.indexOf(r.category)<0)e.push('category');
  if(!(r.ladder_rank>=1&&r.ladder_rank<=3))e.push('ladder_rank');
  return {ok:!e.length,errors:e};
}
var gen={version:"jahdb-names-wu-chinese-1.0",generate:generate,validate:validate};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("names-wu-chinese",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
