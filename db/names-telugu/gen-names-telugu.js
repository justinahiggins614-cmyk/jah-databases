(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var CATS=["first-name", "surname", "place-name", "naming-convention"];
var PREFIX="JAH-NMT3-";
/* rows: [category, display name, meaning, origin, ladder_rank] */
var B=[
 ["first-name","Srinivas శ్రీనివాస","Srinivas (శ్రీనివాస) is a masculine given name in Telugu. Meaning: Abode of Lakshmi. A name of Vishnu; among the most common.","A name of Vishnu; among the most common.",1],
 ["first-name","Lakshmi","Lakshmi is a feminine given name in Telugu. Meaning: Goddess of fortune..","Goddess of fortune.",1],
 ["first-name","Ravi","Ravi is a masculine given name in Telugu. Meaning: Sun. From Sanskrit.","From Sanskrit.",1],
 ["first-name","Anitha","Anitha is a feminine given name in Telugu. Meaning: Grace. A popular girls' name.","A popular girls' name.",1],
 ["first-name","Venkatesh","Venkatesh is a masculine given name in Telugu. Meaning: Lord of Venkata (Tirupati)..","Lord of Venkata (Tirupati).",1],
 ["first-name","Divya","Divya is a feminine given name in Telugu. Meaning: Divine..","Divine.",1],
 ["first-name","Krishna","Krishna is a masculine given name in Telugu. Meaning: The divine cowherd; 'all-attractive'..","The divine cowherd; 'all-attractive'.",1],
 ["surname","Reddy","Reddy is a Telugu family name. A landholding community title.","A landholding community title.",2],
 ["surname","Rao","Rao is a Telugu family name. A title of respect, 'king'.","A title of respect, 'king'.",2],
 ["surname","Chowdary","Chowdary is a Telugu family name. A traditional headman title.","A traditional headman title.",2],
 ["surname","Naidu","Naidu is a Telugu family name. A title of leadership.","A title of leadership.",2],
 ["place-name","Hyderabad","Hyderabad - 'City of Hyder' — founded by Muhammad Quli Qutb Shah.","'City of Hyder' — founded by Muhammad Quli Qutb Shah.",2],
 ["place-name","Amaravati","Amaravati - 'Abode of the immortals'.","'Abode of the immortals'.",2],
 ["naming-convention","Family name first","Family name first: Reddy Srinivas: the family or community name comes first.","Reddy Srinivas: the family or community name comes first.",3],
 ["naming-convention","Names of gods","Names of gods: Children are commonly named directly for deities.","Children are commonly named directly for deities.",3]
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
  var esc="JAH-NMT3-".replace(/[.*+?^${}()|[\]\\]/g,'\\$&');
  if(!new RegExp('^'+esc+'\\d{6}$').test(r.id||''))e.push('id');
  if(typeof r.name!=='string'||!r.name.length)e.push('name');
  if(typeof r.meaning!=='string'||!r.meaning.length)e.push('meaning');
  if(typeof r.title!=='string'||!r.title.length)e.push('title');
  if(CATS.indexOf(r.category)<0)e.push('category');
  if(!(r.ladder_rank>=1&&r.ladder_rank<=3))e.push('ladder_rank');
  return {ok:!e.length,errors:e};
}
var gen={version:"jahdb-names-telugu-1.0",generate:generate,validate:validate};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("names-telugu",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
