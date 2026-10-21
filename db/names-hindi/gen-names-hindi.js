(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var CATS=["first-name", "surname", "place-name", "naming-convention"];
var PREFIX="JAH-NMH2-";
/* rows: [category, display name, meaning, origin, ladder_rank] */
var B=[
 ["first-name","Aarav आरव","Aarav (आरव) is a masculine given name in Hindi. Meaning: Peaceful. A leading modern boys' name.","A leading modern boys' name.",1],
 ["first-name","Diya दीया","Diya (दीया) is a feminine given name in Hindi. Meaning: Lamp, light. Evokes light and warmth.","Evokes light and warmth.",1],
 ["first-name","Arjun अर्जुन","Arjun (अर्जुन) is a masculine given name in Hindi. Meaning: Bright. The archer hero of the Mahabharata.","The archer hero of the Mahabharata.",1],
 ["first-name","Priya प्रिया","Priya (प्रिया) is a feminine given name in Hindi. Meaning: Beloved. From Sanskrit.","From Sanskrit.",1],
 ["first-name","Rohan रोहन","Rohan (रोहन) is a masculine given name in Hindi. Meaning: Ascending. Suggests rising and growth.","Suggests rising and growth.",1],
 ["first-name","Ananya अनन्या","Ananya (अनन्या) is a feminine given name in Hindi. Meaning: Unique. From Sanskrit, 'having no equal'.","From Sanskrit, 'having no equal'.",1],
 ["first-name","Vihaan विहान","Vihaan (विहान) is a masculine given name in Hindi. Meaning: Dawn. The first light of morning.","The first light of morning.",1],
 ["surname","Sharma","Sharma is a Hindi family name. Title for scholars and teachers.","Title for scholars and teachers.",2],
 ["surname","Patel","Patel is a Hindi family name. Village headman — common in Gujarat and beyond.","Village headman — common in Gujarat and beyond.",2],
 ["surname","Singh सिंह","Singh (सिंह) is a Hindi family name. 'Lion' — used widely, and by all Sikh men.","'Lion' — used widely, and by all Sikh men.",2],
 ["surname","Gupta","Gupta is a Hindi family name. 'Protected' — an ancient surname.","'Protected' — an ancient surname.",2],
 ["place-name","Mumbai","Mumbai - From Mumbadevi, the city's patron goddess.","From Mumbadevi, the city's patron goddess.",2],
 ["place-name","Varanasi","Varanasi - Between the Varuna and Asi rivers.","Between the Varuna and Asi rivers.",2],
 ["naming-convention","Singh and Kaur","Singh and Kaur: Sikh men take Singh ('lion') and Sikh women take Kaur ('princess').","Sikh men take Singh ('lion') and Sikh women take Kaur ('princess').",3],
 ["naming-convention","Given + family order","Given + family order: Hindi names run given name first, family name last in modern use.","Hindi names run given name first, family name last in modern use.",3]
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
  var esc="JAH-NMH2-".replace(/[.*+?^${}()|[\]\\]/g,'\\$&');
  if(!new RegExp('^'+esc+'\\d{6}$').test(r.id||''))e.push('id');
  if(typeof r.name!=='string'||!r.name.length)e.push('name');
  if(typeof r.meaning!=='string'||!r.meaning.length)e.push('meaning');
  if(typeof r.title!=='string'||!r.title.length)e.push('title');
  if(CATS.indexOf(r.category)<0)e.push('category');
  if(!(r.ladder_rank>=1&&r.ladder_rank<=3))e.push('ladder_rank');
  return {ok:!e.length,errors:e};
}
var gen={version:"jahdb-names-hindi-1.0",generate:generate,validate:validate};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("names-hindi",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
