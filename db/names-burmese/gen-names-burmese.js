(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var CATS=["first-name", "surname", "place-name", "naming-convention"];
var PREFIX="JAH-NMB3-";
/* rows: [category, display name, meaning, origin, ladder_rank] */
var B=[
 ["first-name","Aung အောင်","Aung (အောင်) is a unisex given name in Burmese. Meaning: Success. Unisex; the most auspicious root.","Unisex; the most auspicious root.",1],
 ["first-name","Khin","Khin is a feminine given name in Burmese. Meaning: Polite, courteous.. A classic girls' name.","A classic girls' name.",1],
 ["first-name","Myo","Myo is a masculine given name in Burmese. Meaning: Noble.. A traditional boys' name.","A traditional boys' name.",1],
 ["first-name","Thant","Thant is a masculine given name in Burmese. Meaning: Clean, pure.. A leading boys' name.","A leading boys' name.",1],
 ["first-name","Su","Su is a feminine given name in Burmese. Meaning: A graceful girls' name..","A graceful girls' name.",1],
 ["first-name","Hla","Hla is a masculine given name in Burmese. Meaning: Handsome.. A classic boys' name.","A classic boys' name.",1],
 ["first-name","Nandar","Nandar is a feminine given name in Burmese. Meaning: A popular girls' name..","A popular girls' name.",1],
 ["surname","No surnames","No surnames is a Burmese family name. Burmese traditionally have no family names at all.","Burmese traditionally have no family names at all.",2],
 ["surname","Given names only","Given names only is a Burmese family name. One or two given names form the complete name.","One or two given names form the complete name.",2],
 ["surname","No inheritance","No inheritance is a Burmese family name. Children's names do not repeat the parents'.","Children's names do not repeat the parents'.",2],
 ["surname","Astrological naming","Astrological naming is a Burmese family name. Names may be chosen by the day of birth and its letter.","Names may be chosen by the day of birth and its letter.",2],
 ["place-name","Yangon ရန်ကုန်","Yangon (ရန်ကုန်) - 'End of strife'.","'End of strife'.",2],
 ["place-name","Mandalay","Mandalay - From Mandala Hill.","From Mandala Hill.",2],
 ["naming-convention","No family names","No family names: A Burmese name is complete without any surname.","A Burmese name is complete without any surname.",3],
 ["naming-convention","Honorifics U and Daw","Honorifics U and Daw: U (uncle) and Daw (aunt) precede names as titles of respect.","U (uncle) and Daw (aunt) precede names as titles of respect.",3]
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
  var esc="JAH-NMB3-".replace(/[.*+?^${}()|[\]\\]/g,'\\$&');
  if(!new RegExp('^'+esc+'\\d{6}$').test(r.id||''))e.push('id');
  if(typeof r.name!=='string'||!r.name.length)e.push('name');
  if(typeof r.meaning!=='string'||!r.meaning.length)e.push('meaning');
  if(typeof r.title!=='string'||!r.title.length)e.push('title');
  if(CATS.indexOf(r.category)<0)e.push('category');
  if(!(r.ladder_rank>=1&&r.ladder_rank<=3))e.push('ladder_rank');
  return {ok:!e.length,errors:e};
}
var gen={version:"jahdb-names-burmese-1.0",generate:generate,validate:validate};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("names-burmese",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
