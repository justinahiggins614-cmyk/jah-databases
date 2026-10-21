(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var CATS=["first-name", "surname", "place-name", "naming-convention"];
var PREFIX="JAH-NMT6-";
/* rows: [category, display name, meaning, origin, ladder_rank] */
var B=[
 ["first-name","Jose","Jose is a masculine given name in Tagalog. Meaning: God will increase..","God will increase.",1],
 ["first-name","Maria","Maria is a feminine given name in Tagalog. Meaning: Beloved..","Beloved.",1],
 ["first-name","Juan","Juan is a masculine given name in Tagalog. Meaning: God is gracious..","God is gracious.",1],
 ["first-name","Rosa","Rosa is a feminine given name in Tagalog. Meaning: Rose..","Rose.",1],
 ["first-name","Pedro","Pedro is a masculine given name in Tagalog. Meaning: Stone..","Stone.",1],
 ["first-name","Ana","Ana is a feminine given name in Tagalog. Meaning: Grace..","Grace.",1],
 ["first-name","Miguel","Miguel is a masculine given name in Tagalog. Meaning: Who is like God?.","Who is like God?",1],
 ["surname","Dela Cruz","Dela Cruz is a Tagalog family name. 'Of the Cross'.","'Of the Cross'.",2],
 ["surname","Santos","Santos is a Tagalog family name. 'Saints'.","'Saints'.",2],
 ["surname","Reyes","Reyes is a Tagalog family name. 'Kings'.","'Kings'.",2],
 ["surname","Bautista","Bautista is a Tagalog family name. 'Baptist'.","'Baptist'.",2],
 ["place-name","Maynila","Maynila - From the nilad plant — Manila.","From the nilad plant — Manila.",2],
 ["place-name","Quezon City","Quezon City - Named for President Manuel Quezon.","Named for President Manuel Quezon.",2],
 ["naming-convention","Mother's maiden as middle name","Mother's maiden as middle name: The middle name is the mother's maiden surname.","The middle name is the mother's maiden surname.",3],
 ["naming-convention","Spanish surnames","Spanish surnames: Most Filipino surnames are Spanish in origin.","Most Filipino surnames are Spanish in origin.",3]
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
  var esc="JAH-NMT6-".replace(/[.*+?^${}()|[\]\\]/g,'\\$&');
  if(!new RegExp('^'+esc+'\\d{6}$').test(r.id||''))e.push('id');
  if(typeof r.name!=='string'||!r.name.length)e.push('name');
  if(typeof r.meaning!=='string'||!r.meaning.length)e.push('meaning');
  if(typeof r.title!=='string'||!r.title.length)e.push('title');
  if(CATS.indexOf(r.category)<0)e.push('category');
  if(!(r.ladder_rank>=1&&r.ladder_rank<=3))e.push('ladder_rank');
  return {ok:!e.length,errors:e};
}
var gen={version:"jahdb-names-tagalog-1.0",generate:generate,validate:validate};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("names-tagalog",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
