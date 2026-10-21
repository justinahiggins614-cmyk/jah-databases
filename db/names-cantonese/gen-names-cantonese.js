(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var CATS=["first-name", "surname", "place-name", "naming-convention"];
var PREFIX="JAH-NMC-";
/* rows: [category, display name, meaning, origin, ladder_rank] */
var B=[
 ["first-name","Wai 偉","Wai (偉) is a masculine given name in Cantonese. Meaning: Great. The Cantonese reading of the same character as Mandarin Wei.","The Cantonese reading of the same character as Mandarin Wei.",1],
 ["first-name","Man 文","Man (文) is a masculine given name in Cantonese. Meaning: Cultured. From the character for literature and culture.","From the character for literature and culture.",1],
 ["first-name","Ka-yan 嘉欣","Ka-yan (嘉欣) is a feminine given name in Cantonese. Meaning: Praiseworthy + joyful. A two-character girls' name.","A two-character girls' name.",1],
 ["first-name","Tsz-chung 子聰","Tsz-chung (子聰) is a masculine given name in Cantonese. Meaning: Clever. A modern boys' name.","A modern boys' name.",1],
 ["first-name","Wing 詠","Wing (詠) is a feminine given name in Cantonese. Meaning: To sing. Evokes poetry and song.","Evokes poetry and song.",1],
 ["first-name","Ho-yin 浩然","Ho-yin (浩然) is a masculine given name in Cantonese. Meaning: Vast + correct. Suggests breadth and integrity.","Suggests breadth and integrity.",1],
 ["first-name","Siu-mei 小美","Siu-mei (小美) is a feminine given name in Cantonese. Meaning: Little beauty. An affectionate girls' name.","An affectionate girls' name.",1],
 ["surname","Wong 黃","Wong (黃) is a Cantonese family name. 'Yellow' — the Cantonese reading of Huang.","'Yellow' — the Cantonese reading of Huang.",2],
 ["surname","Chan 陳","Chan (陳) is a Cantonese family name. The Cantonese reading of Chen.","The Cantonese reading of Chen.",2],
 ["surname","Lee 李","Lee (李) is a Cantonese family name. 'Plum' — the Cantonese reading of Li.","'Plum' — the Cantonese reading of Li.",2],
 ["surname","Cheung 張","Cheung (張) is a Cantonese family name. The Cantonese reading of Zhang.","The Cantonese reading of Zhang.",2],
 ["place-name","Hong Kong 香港","Hong Kong (香港) - 'Fragrant harbor'.","'Fragrant harbor'.",2],
 ["place-name","Guangzhou 廣州","Guangzhou (廣州) - 'Broad prefecture'.","'Broad prefecture'.",2],
 ["naming-convention","Family name first","Family name first: Wong Wai is Mr. Wong: surname first, as across Chinese languages.","Wong Wai is Mr. Wong: surname first, as across Chinese languages.",3],
 ["naming-convention","Romanization varies","Romanization varies: The same character 王 is Wong in Cantonese and Wang in Mandarin.","The same character 王 is Wong in Cantonese and Wang in Mandarin.",3]
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
  var esc="JAH-NMC-".replace(/[.*+?^${}()|[\]\\]/g,'\\$&');
  if(!new RegExp('^'+esc+'\\d{6}$').test(r.id||''))e.push('id');
  if(typeof r.name!=='string'||!r.name.length)e.push('name');
  if(typeof r.meaning!=='string'||!r.meaning.length)e.push('meaning');
  if(typeof r.title!=='string'||!r.title.length)e.push('title');
  if(CATS.indexOf(r.category)<0)e.push('category');
  if(!(r.ladder_rank>=1&&r.ladder_rank<=3))e.push('ladder_rank');
  return {ok:!e.length,errors:e};
}
var gen={version:"jahdb-names-cantonese-1.0",generate:generate,validate:validate};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("names-cantonese",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
