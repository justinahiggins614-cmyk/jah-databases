(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var CATS=["first-name", "surname", "place-name", "naming-convention"];
var PREFIX="JAH-NMJC-";
/* rows: [category, display name, meaning, origin, ladder_rank] */
var B=[
 ["first-name","Wei 伟","Wei (伟) is a masculine given name in Jin Chinese. Meaning: Great..","Great.",1],
 ["first-name","Fang 芳","Fang (芳) is a feminine given name in Jin Chinese. Meaning: Fragrant..","Fragrant.",1],
 ["first-name","Qiang 强","Qiang (强) is a masculine given name in Jin Chinese. Meaning: Strong..","Strong.",1],
 ["first-name","Na 娜","Na (娜) is a feminine given name in Jin Chinese. Meaning: Elegant..","Elegant.",1],
 ["first-name","Chao 超","Chao (超) is a masculine given name in Jin Chinese. Meaning: To surpass..","To surpass.",1],
 ["first-name","Jing 静","Jing (静) is a feminine given name in Jin Chinese. Meaning: Quiet, calm..","Quiet, calm.",1],
 ["first-name","Tao 涛","Tao (涛) is a masculine given name in Jin Chinese. Meaning: Great waves..","Great waves.",1],
 ["surname","Wang 王","Wang (王) is a Jin Chinese family name. 'King'.","'King'.",2],
 ["surname","Li 李","Li (李) is a Jin Chinese family name. 'Plum'.","'Plum'.",2],
 ["surname","Zhang 张","Zhang (张) is a Jin Chinese family name. 'To stretch (a bow)'.","'To stretch (a bow)'.",2],
 ["surname","Liu 刘","Liu (刘) is a Jin Chinese family name. Ancient imperial surname.","Ancient imperial surname.",2],
 ["place-name","Taiyuan 太原","Taiyuan (太原) - 'Great plain' — the Shanxi capital.","'Great plain' — the Shanxi capital.",2],
 ["place-name","Datong 大同","Datong (大同) - 'Great unity'.","'Great unity'.",2],
 ["naming-convention","Family name first","Family name first: The surname leads, as across Chinese languages.","The surname leads, as across Chinese languages.",3],
 ["naming-convention","Generation names","Generation names: Siblings share a generation character.","Siblings share a generation character.",3]
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
  var esc="JAH-NMJC-".replace(/[.*+?^${}()|[\]\\]/g,'\\$&');
  if(!new RegExp('^'+esc+'\\d{6}$').test(r.id||''))e.push('id');
  if(typeof r.name!=='string'||!r.name.length)e.push('name');
  if(typeof r.meaning!=='string'||!r.meaning.length)e.push('meaning');
  if(typeof r.title!=='string'||!r.title.length)e.push('title');
  if(CATS.indexOf(r.category)<0)e.push('category');
  if(!(r.ladder_rank>=1&&r.ladder_rank<=3))e.push('ladder_rank');
  return {ok:!e.length,errors:e};
}
var gen={version:"jahdb-names-jin-chinese-1.0",generate:generate,validate:validate};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("names-jin-chinese",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
