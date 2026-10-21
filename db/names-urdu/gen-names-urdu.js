(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var CATS=["first-name", "surname", "place-name", "naming-convention"];
var PREFIX="JAH-NMU2-";
/* rows: [category, display name, meaning, origin, ladder_rank] */
var B=[
 ["first-name","Ahmed احمد","Ahmed (احمد) is a masculine given name in Urdu. Meaning: Most praised..","Most praised.",1],
 ["first-name","Fatima فاطمہ","Fatima (فاطمہ) is a feminine given name in Urdu. Meaning: Captivating..","Captivating.",1],
 ["first-name","Ali علی","Ali (علی) is a masculine given name in Urdu. Meaning: Exalted..","Exalted.",1],
 ["first-name","Ayesha عائشہ","Ayesha (عائشہ) is a feminine given name in Urdu. Meaning: Alive..","Alive.",1],
 ["first-name","Bilal بلال","Bilal (بلال) is a masculine given name in Urdu. Meaning: The Prophet's muezzin; a classic name..","The Prophet's muezzin; a classic name.",1],
 ["first-name","Zainab زینب","Zainab (زینب) is a feminine given name in Urdu. Meaning: A fragrant flower; the Prophet's daughter's name..","A fragrant flower; the Prophet's daughter's name.",1],
 ["first-name","Usman عثمان","Usman (عثمان) is a masculine given name in Urdu. Meaning: A leading early Muslim name..","A leading early Muslim name.",1],
 ["surname","Khan","Khan is a Urdu family name. Turco-Mongol title, 'leader' — the most common surname.","Turco-Mongol title, 'leader' — the most common surname.",2],
 ["surname","Malik","Malik is a Urdu family name. 'King'.","'King'.",2],
 ["surname","Sheikh","Sheikh is a Urdu family name. 'Elder' — a title of respect.","'Elder' — a title of respect.",2],
 ["surname","Syed","Syed is a Urdu family name. 'Descendant of the Prophet'.","'Descendant of the Prophet'.",2],
 ["place-name","Karachi","Karachi - From Kolachi, the old fishing village.","From Kolachi, the old fishing village.",2],
 ["place-name","Lahore","Lahore - Traditionally from Loh, son of Rama.","Traditionally from Loh, son of Rama.",2],
 ["naming-convention","Ibn/bint lineage","Ibn/bint lineage: Lineage runs 'son of' and 'daughter of', as in Arabic.","Lineage runs 'son of' and 'daughter of', as in Arabic.",3],
 ["naming-convention","Syed and Sheikh","Syed and Sheikh: Honorific surnames mark claimed descent or learning.","Honorific surnames mark claimed descent or learning.",3]
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
  var esc="JAH-NMU2-".replace(/[.*+?^${}()|[\]\\]/g,'\\$&');
  if(!new RegExp('^'+esc+'\\d{6}$').test(r.id||''))e.push('id');
  if(typeof r.name!=='string'||!r.name.length)e.push('name');
  if(typeof r.meaning!=='string'||!r.meaning.length)e.push('meaning');
  if(typeof r.title!=='string'||!r.title.length)e.push('title');
  if(CATS.indexOf(r.category)<0)e.push('category');
  if(!(r.ladder_rank>=1&&r.ladder_rank<=3))e.push('ladder_rank');
  return {ok:!e.length,errors:e};
}
var gen={version:"jahdb-names-urdu-1.0",generate:generate,validate:validate};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("names-urdu",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
