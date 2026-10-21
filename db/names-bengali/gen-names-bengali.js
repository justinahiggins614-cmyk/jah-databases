(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var CATS=["first-name", "surname", "place-name", "naming-convention"];
var PREFIX="JAH-NMB-";
/* rows: [category, display name, meaning, origin, ladder_rank] */
var B=[
 ["first-name","Priya প্রিয়া","Priya (প্রিয়া) is a feminine given name in Bengali. Meaning: Beloved. From Sanskrit; common across eastern India.","From Sanskrit; common across eastern India.",1],
 ["first-name","Arjun অর্জুন","Arjun (অর্জুন) is a masculine given name in Bengali. Meaning: Bright, white. From Sanskrit; the archer hero of the Mahabharata.","From Sanskrit; the archer hero of the Mahabharata.",1],
 ["first-name","Ananya অন্যা","Ananya (অন্যা) is a feminine given name in Bengali. Meaning: Unique. From Sanskrit ananya, 'having no equal'.","From Sanskrit ananya, 'having no equal'.",1],
 ["first-name","Rahul রাহুল","Rahul (রাহুল) is a masculine given name in Bengali. Meaning: Conqueror of miseries. A widely used name of Sanskrit origin.","A widely used name of Sanskrit origin.",1],
 ["first-name","Diya দিয়া","Diya (দিয়া) is a feminine given name in Bengali. Meaning: Lamp, light. Evokes the festival lamp.","Evokes the festival lamp.",1],
 ["first-name","Sourav সৌরভ","Sourav (সৌরভ) is a masculine given name in Bengali. Meaning: Fragrance. From Sanskrit saurabha.","From Sanskrit saurabha.",1],
 ["first-name","Tanvi তন্বী","Tanvi (তন্বী) is a feminine given name in Bengali. Meaning: Delicate. From Sanskrit.","From Sanskrit.",1],
 ["surname","Chatterjee","Chatterjee is a Bengali family name. From Chattopadhyay, a title for village scholars.","From Chattopadhyay, a title for village scholars.",2],
 ["surname","Banerjee","Banerjee is a Bengali family name. From Bandyopadhyay, a Brahmin family title.","From Bandyopadhyay, a Brahmin family title.",2],
 ["surname","Mukherjee","Mukherjee is a Bengali family name. From Mukhopadhyay, 'chief teacher' lineage.","From Mukhopadhyay, 'chief teacher' lineage.",2],
 ["surname","Das দাস","Das (দাস) is a Bengali family name. 'Servant (of God)' — a devotional surname.","'Servant (of God)' — a devotional surname.",2],
 ["place-name","Kolkata","Kolkata - From Kalikata, named for the goddess Kali.","From Kalikata, named for the goddess Kali.",2],
 ["place-name","Dhaka","Dhaka - From the Dhakeshwari temple.","From the Dhakeshwari temple.",2],
 ["naming-convention","Given name + family name","Given name + family name: Modern Bengali names run given name first, family name last.","Modern Bengali names run given name first, family name last.",3],
 ["naming-convention","Honorifics","Honorifics: Sri and Srimati precede names as Mr. and Mrs. do in English.","Sri and Srimati precede names as Mr. and Mrs. do in English.",3]
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
  var esc="JAH-NMB-".replace(/[.*+?^${}()|[\]\\]/g,'\\$&');
  if(!new RegExp('^'+esc+'\\d{6}$').test(r.id||''))e.push('id');
  if(typeof r.name!=='string'||!r.name.length)e.push('name');
  if(typeof r.meaning!=='string'||!r.meaning.length)e.push('meaning');
  if(typeof r.title!=='string'||!r.title.length)e.push('title');
  if(CATS.indexOf(r.category)<0)e.push('category');
  if(!(r.ladder_rank>=1&&r.ladder_rank<=3))e.push('ladder_rank');
  return {ok:!e.length,errors:e};
}
var gen={version:"jahdb-names-bengali-1.0",generate:generate,validate:validate};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("names-bengali",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
