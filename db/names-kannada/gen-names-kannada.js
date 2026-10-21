(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var CATS=["first-name", "surname", "place-name", "naming-convention"];
var PREFIX="JAH-NMK2-";
/* rows: [category, display name, meaning, origin, ladder_rank] */
var B=[
 ["first-name","Ravi","Ravi is a masculine given name in Kannada. Meaning: Sun. From Sanskrit.","From Sanskrit.",1],
 ["first-name","Lakshmi","Lakshmi is a feminine given name in Kannada. Meaning: Goddess of fortune..","Goddess of fortune.",1],
 ["first-name","Manjunath","Manjunath is a masculine given name in Kannada. Meaning: A name of Shiva, 'lord of Manju'..","A name of Shiva, 'lord of Manju'.",1],
 ["first-name","Divya","Divya is a feminine given name in Kannada. Meaning: Divine..","Divine.",1],
 ["first-name","Prakash","Prakash is a masculine given name in Kannada. Meaning: Light. From Sanskrit.","From Sanskrit.",1],
 ["first-name","Asha","Asha is a feminine given name in Kannada. Meaning: Hope. From Sanskrit.","From Sanskrit.",1],
 ["first-name","Gopal","Gopal is a masculine given name in Kannada. Meaning: Cowherd — a name of Krishna..","Cowherd — a name of Krishna.",1],
 ["surname","Gowda","Gowda is a Kannada family name. A landholding community title.","A landholding community title.",2],
 ["surname","Shetty","Shetty is a Kannada family name. A merchant community title.","A merchant community title.",2],
 ["surname","Kulkarni","Kulkarni is a Kannada family name. Village accountant — a historic office.","Village accountant — a historic office.",2],
 ["surname","Bhat","Bhat is a Kannada family name. Scholar — a Brahmin title.","Scholar — a Brahmin title.",2],
 ["place-name","Bengaluru","Bengaluru - Folk etymology: 'town of boiled beans'.","Folk etymology: 'town of boiled beans'.",2],
 ["place-name","Mysuru","Mysuru - From Mahishuru, land of the buffalo-demon legend.","From Mahishuru, land of the buffalo-demon legend.",2],
 ["naming-convention","Village + father's name","Village + father's name: Older full names chain the village, the father's name, and the given name.","Older full names chain the village, the father's name, and the given name.",3],
 ["naming-convention","No fixed surnames traditionally","No fixed surnames traditionally: Many families adopted surnames only in the modern era.","Many families adopted surnames only in the modern era.",3]
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
  var esc="JAH-NMK2-".replace(/[.*+?^${}()|[\]\\]/g,'\\$&');
  if(!new RegExp('^'+esc+'\\d{6}$').test(r.id||''))e.push('id');
  if(typeof r.name!=='string'||!r.name.length)e.push('name');
  if(typeof r.meaning!=='string'||!r.meaning.length)e.push('meaning');
  if(typeof r.title!=='string'||!r.title.length)e.push('title');
  if(CATS.indexOf(r.category)<0)e.push('category');
  if(!(r.ladder_rank>=1&&r.ladder_rank<=3))e.push('ladder_rank');
  return {ok:!e.length,errors:e};
}
var gen={version:"jahdb-names-kannada-1.0",generate:generate,validate:validate};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("names-kannada",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
