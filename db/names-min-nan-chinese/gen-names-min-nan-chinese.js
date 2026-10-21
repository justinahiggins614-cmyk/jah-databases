(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var CATS=["first-name", "surname", "place-name", "naming-convention"];
var PREFIX="JAH-NMMNC-";
/* rows: [category, display name, meaning, origin, ladder_rank] */
var B=[
 ["first-name","Ah-hui 阿輝","Ah-hui (阿輝) is a masculine given name in Min Nan Chinese. Meaning: Radiance. The Ah- prefix marks affectionate address.","The Ah- prefix marks affectionate address.",1],
 ["first-name","Ah-lian 阿蓮","Ah-lian (阿蓮) is a feminine given name in Min Nan Chinese. Meaning: Lotus..","Lotus.",1],
 ["first-name","Jin 金","Jin (金) is a masculine given name in Min Nan Chinese. Meaning: Gold..","Gold.",1],
 ["first-name","Mei 美","Mei (美) is a feminine given name in Min Nan Chinese. Meaning: Beautiful..","Beautiful.",1],
 ["first-name","Tiong 中","Tiong (中) is a masculine given name in Min Nan Chinese. Meaning: Middle..","Middle.",1],
 ["first-name","Suat 雪","Suat (雪) is a feminine given name in Min Nan Chinese. Meaning: Snow..","Snow.",1],
 ["first-name","Bok 木","Bok (木) is a masculine given name in Min Nan Chinese. Meaning: Wood; tree..","Wood; tree.",1],
 ["surname","Tan 陳","Tan (陳) is a Min Nan Chinese family name. The Hokkien reading of Chen.","The Hokkien reading of Chen.",2],
 ["surname","Lim 林","Lim (林) is a Min Nan Chinese family name. 'Forest' — the Hokkien reading of Lin.","'Forest' — the Hokkien reading of Lin.",2],
 ["surname","Ong 王","Ong (王) is a Min Nan Chinese family name. 'King' — the Hokkien reading of Wang.","'King' — the Hokkien reading of Wang.",2],
 ["surname","Goh 吳","Goh (吳) is a Min Nan Chinese family name. The Hokkien reading of Wu.","The Hokkien reading of Wu.",2],
 ["place-name","Xiamen 廈門","Xiamen (廈門) - 'Mansion gate'.","'Mansion gate'.",2],
 ["place-name","Quanzhou 泉州","Quanzhou (泉州) - 'Spring prefecture'.","'Spring prefecture'.",2],
 ["naming-convention","Hokkien romanizations","Hokkien romanizations: Chen becomes Tan, Lin becomes Lim in Hokkien spelling.","Chen becomes Tan, Lin becomes Lim in Hokkien spelling.",3],
 ["naming-convention","Ah- nicknames","Ah- nicknames: Ah- plus one syllable is the everyday affectionate form.","Ah- plus one syllable is the everyday affectionate form.",3]
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
  var esc="JAH-NMMNC-".replace(/[.*+?^${}()|[\]\\]/g,'\\$&');
  if(!new RegExp('^'+esc+'\\d{6}$').test(r.id||''))e.push('id');
  if(typeof r.name!=='string'||!r.name.length)e.push('name');
  if(typeof r.meaning!=='string'||!r.meaning.length)e.push('meaning');
  if(typeof r.title!=='string'||!r.title.length)e.push('title');
  if(CATS.indexOf(r.category)<0)e.push('category');
  if(!(r.ladder_rank>=1&&r.ladder_rank<=3))e.push('ladder_rank');
  return {ok:!e.length,errors:e};
}
var gen={version:"jahdb-names-min-nan-chinese-1.0",generate:generate,validate:validate};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("names-min-nan-chinese",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
