(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var CATS=["first-name", "surname", "place-name", "naming-convention"];
var PREFIX="JAH-NMA-";
/* rows: [category, display name, meaning, origin, ladder_rank] */
var B=[
 ["first-name","Muhammad محمد","Muhammad (محمد) is a masculine given name in Arabic. Meaning: Praised. From the root h-m-d, 'to praise'; the most given male name in the world.","From the root h-m-d, 'to praise'; the most given male name in the world.",1],
 ["first-name","Fatima فاطمة","Fatima (فاطمة) is a feminine given name in Arabic. Meaning: Captivating. A leading girls' name across the Muslim world.","A leading girls' name across the Muslim world.",1],
 ["first-name","Ahmed أحمد","Ahmed (أحمد) is a masculine given name in Arabic. Meaning: Most praised. From the same root as Muhammad.","From the same root as Muhammad.",1],
 ["first-name","Layla ليلى","Layla (ليلى) is a feminine given name in Arabic. Meaning: Night. Made famous by classical Arabic love poetry.","Made famous by classical Arabic love poetry.",1],
 ["first-name","Ali علي","Ali (علي) is a masculine given name in Arabic. Meaning: Exalted. From the root '-l-w, 'high'.","From the root '-l-w, 'high'.",1],
 ["first-name","Aisha عائشة","Aisha (عائشة) is a feminine given name in Arabic. Meaning: Alive. From the root '-y-sh, 'to live'.","From the root '-y-sh, 'to live'.",1],
 ["first-name","Omar عمر","Omar (عمر) is a masculine given name in Arabic. Meaning: Flourishing. From the root '-m-r, 'to live long'.","From the root '-m-r, 'to live long'.",1],
 ["surname","Haddad حداد","Haddad (حداد) is a Arabic family name. 'Blacksmith' — occupational.","'Blacksmith' — occupational.",2],
 ["surname","Nasser ناصر","Nasser (ناصر) is a Arabic family name. 'Helper'.","'Helper'.",2],
 ["surname","Al-Farsi","Al-Farsi is a Arabic family name. 'The Persian' — a nisba of origin.","'The Persian' — a nisba of origin.",2],
 ["surname","Najjar نجار","Najjar (نجار) is a Arabic family name. 'Carpenter' — occupational.","'Carpenter' — occupational.",2],
 ["place-name","Cairo القاهرة","Cairo (القاهرة) - 'The Victorious' — Al-Qahira.","'The Victorious' — Al-Qahira.",2],
 ["place-name","Baghdad بغداد","Baghdad (بغداد) - 'Gift of God' — from Persian.","'Gift of God' — from Persian.",2],
 ["naming-convention","Ibn and bint","Ibn and bint: Lineage is recorded as 'son of' (ibn) and 'daughter of' (bint).","Lineage is recorded as 'son of' (ibn) and 'daughter of' (bint).",3],
 ["naming-convention","Kunya: Abu and Umm","Kunya: Abu and Umm: A parent is called 'father of' (Abu) or 'mother of' (Umm) their eldest child.","A parent is called 'father of' (Abu) or 'mother of' (Umm) their eldest child.",3]
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
  var esc="JAH-NMA-".replace(/[.*+?^${}()|[\]\\]/g,'\\$&');
  if(!new RegExp('^'+esc+'\\d{6}$').test(r.id||''))e.push('id');
  if(typeof r.name!=='string'||!r.name.length)e.push('name');
  if(typeof r.meaning!=='string'||!r.meaning.length)e.push('meaning');
  if(typeof r.title!=='string'||!r.title.length)e.push('title');
  if(CATS.indexOf(r.category)<0)e.push('category');
  if(!(r.ladder_rank>=1&&r.ladder_rank<=3))e.push('ladder_rank');
  return {ok:!e.length,errors:e};
}
var gen={version:"jahdb-names-arabic-1.0",generate:generate,validate:validate};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("names-arabic",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
