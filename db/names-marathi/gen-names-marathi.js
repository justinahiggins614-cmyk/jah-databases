(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var CATS=["first-name", "surname", "place-name", "naming-convention"];
var PREFIX="JAH-NMM-";
/* rows: [category, display name, meaning, origin, ladder_rank] */
var B=[
 ["first-name","Suresh","Suresh is a masculine given name in Marathi. Meaning: Ruler of gods. From Sanskrit sura + isha.","From Sanskrit sura + isha.",1],
 ["first-name","Sunita","Sunita is a feminine given name in Marathi. Meaning: Well-behaved. From Sanskrit.","From Sanskrit.",1],
 ["first-name","Rahul","Rahul is a masculine given name in Marathi. Meaning: Conqueror of miseries..","Conqueror of miseries.",1],
 ["first-name","Sneha","Sneha is a feminine given name in Marathi. Meaning: Affection. From Sanskrit.","From Sanskrit.",1],
 ["first-name","Amit","Amit is a masculine given name in Marathi. Meaning: Infinite. From Sanskrit amita.","From Sanskrit amita.",1],
 ["first-name","Pooja","Pooja is a feminine given name in Marathi. Meaning: Worship. The ritual offering.","The ritual offering.",1],
 ["first-name","Sachin","Sachin is a masculine given name in Marathi. Meaning: A name of Shiva; also 'pure'..","A name of Shiva; also 'pure'.",1],
 ["surname","Deshmukh","Deshmukh is a Marathi family name. District head — a historic office title.","District head — a historic office title.",2],
 ["surname","Patil","Patil is a Marathi family name. Village head — a historic office title.","Village head — a historic office title.",2],
 ["surname","Kulkarni","Kulkarni is a Marathi family name. Village accountant — a historic office title.","Village accountant — a historic office title.",2],
 ["surname","Joshi","Joshi is a Marathi family name. Astrologer — a historic office title.","Astrologer — a historic office title.",2],
 ["place-name","Pune","Pune - From Punya/Punawadi, an old settlement name.","From Punya/Punawadi, an old settlement name.",2],
 ["place-name","Nagpur","Nagpur - Naga + pur, 'city of the Nagas'.","Naga + pur, 'city of the Nagas'.",2],
 ["naming-convention","Occupational surnames","Occupational surnames: Kulkarni, Deshmukh, and Patil began as village offices.","Kulkarni, Deshmukh, and Patil began as village offices.",3],
 ["naming-convention","Given + father's + family","Given + father's + family: Full names often run given name, father's name, then family name.","Full names often run given name, father's name, then family name.",3]
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
  var esc="JAH-NMM-".replace(/[.*+?^${}()|[\]\\]/g,'\\$&');
  if(!new RegExp('^'+esc+'\\d{6}$').test(r.id||''))e.push('id');
  if(typeof r.name!=='string'||!r.name.length)e.push('name');
  if(typeof r.meaning!=='string'||!r.meaning.length)e.push('meaning');
  if(typeof r.title!=='string'||!r.title.length)e.push('title');
  if(CATS.indexOf(r.category)<0)e.push('category');
  if(!(r.ladder_rank>=1&&r.ladder_rank<=3))e.push('ladder_rank');
  return {ok:!e.length,errors:e};
}
var gen={version:"jahdb-names-marathi-1.0",generate:generate,validate:validate};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("names-marathi",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
