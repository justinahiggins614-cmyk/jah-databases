(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var CATS=["first-name", "surname", "place-name", "naming-convention"];
var PREFIX="JAH-NMXC-";
/* rows: [category, display name, meaning, origin, ladder_rank] */
var B=[
 ["first-name","Wei 伟","Wei (伟) is a masculine given name in Xiang Chinese. Meaning: Great..","Great.",1],
 ["first-name","Fang 芳","Fang (芳) is a feminine given name in Xiang Chinese. Meaning: Fragrant..","Fragrant.",1],
 ["first-name","Jun 军","Jun (军) is a masculine given name in Xiang Chinese. Meaning: Army..","Army.",1],
 ["first-name","Li 丽","Li (丽) is a feminine given name in Xiang Chinese. Meaning: Beautiful..","Beautiful.",1],
 ["first-name","Ping 平","Ping (平) is a unisex given name in Xiang Chinese. Meaning: Peace.. Unisex.","Unisex.",1],
 ["first-name","Yong 勇","Yong (勇) is a masculine given name in Xiang Chinese. Meaning: Brave..","Brave.",1],
 ["first-name","Yan 燕","Yan (燕) is a feminine given name in Xiang Chinese. Meaning: Swallow (the bird)..","Swallow (the bird).",1],
 ["surname","Li 李","Li (李) is a Xiang Chinese family name. 'Plum'.","'Plum'.",2],
 ["surname","Liu 刘","Liu (刘) is a Xiang Chinese family name. Ancient imperial surname.","Ancient imperial surname.",2],
 ["surname","Chen 陈","Chen (陈) is a Xiang Chinese family name. An ancient state name.","An ancient state name.",2],
 ["surname","Wang 王","Wang (王) is a Xiang Chinese family name. 'King'.","'King'.",2],
 ["place-name","Changsha 长沙","Changsha (长沙) - 'Long sandbank'.","'Long sandbank'.",2],
 ["place-name","Hengyang","Hengyang - A historic Hunan city.","A historic Hunan city.",2],
 ["naming-convention","Family name first","Family name first: The surname leads, as across Chinese languages.","The surname leads, as across Chinese languages.",3],
 ["naming-convention","Xiang readings","Xiang readings: Characters carry distinct Hunan pronunciations.","Characters carry distinct Hunan pronunciations.",3]
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
  var esc="JAH-NMXC-".replace(/[.*+?^${}()|[\]\\]/g,'\\$&');
  if(!new RegExp('^'+esc+'\\d{6}$').test(r.id||''))e.push('id');
  if(typeof r.name!=='string'||!r.name.length)e.push('name');
  if(typeof r.meaning!=='string'||!r.meaning.length)e.push('meaning');
  if(typeof r.title!=='string'||!r.title.length)e.push('title');
  if(CATS.indexOf(r.category)<0)e.push('category');
  if(!(r.ladder_rank>=1&&r.ladder_rank<=3))e.push('ladder_rank');
  return {ok:!e.length,errors:e};
}
var gen={version:"jahdb-names-xiang-chinese-1.0",generate:generate,validate:validate};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("names-xiang-chinese",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
