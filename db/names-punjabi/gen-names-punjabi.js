(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var CATS=["first-name", "surname", "place-name", "naming-convention"];
var PREFIX="JAH-NMP3-";
/* rows: [category, display name, meaning, origin, ladder_rank] */
var B=[
 ["first-name","Harpreet ਹਰਪ੍ਰੀਤ","Harpreet (ਹਰਪ੍ਰੀਤ) is a unisex given name in Punjabi. Meaning: Love of God. From Har (God) + preet (love); unisex.","From Har (God) + preet (love); unisex.",1],
 ["first-name","Simran ਸਿਮਰਨ","Simran (ਸਿਮਰਨ) is a feminine given name in Punjabi. Meaning: Remembrance (of God). Devotional meditation; a leading girls' name.","Devotional meditation; a leading girls' name.",1],
 ["first-name","Gurpreet ਗੁਰਪ੍ਰੀਤ","Gurpreet (ਗੁਰਪ੍ਰੀਤ) is a unisex given name in Punjabi. Meaning: Love of the Guru. Unisex; devotion to the teacher.","Unisex; devotion to the teacher.",1],
 ["first-name","Arshdeep ਅਰਸ਼ਦੀਪ","Arshdeep (ਅਰਸ਼ਦੀਪ) is a masculine given name in Punjabi. Meaning: Lamp of the sky. A modern boys' name.","A modern boys' name.",1],
 ["first-name","Navjot ਨਵਜੋਤ","Navjot (ਨਵਜੋਤ) is a feminine given name in Punjabi. Meaning: New light. A graceful girls' name.","A graceful girls' name.",1],
 ["first-name","Manpreet ਮਨਪ੍ਰੀਤ","Manpreet (ਮਨਪ੍ਰੀਤ) is a unisex given name in Punjabi. Meaning: Love of the mind. Unisex; sincerity of heart.","Unisex; sincerity of heart.",1],
 ["first-name","Jasleen ਜਸਲੀਨ","Jasleen (ਜਸਲੀਨ) is a feminine given name in Punjabi. Meaning: Absorbed in praise. A devotional girls' name.","A devotional girls' name.",1],
 ["surname","Singh","Singh is a Punjabi family name. 'Lion' — taken by all Sikh men.","'Lion' — taken by all Sikh men.",2],
 ["surname","Kaur","Kaur is a Punjabi family name. 'Princess' — taken by all Sikh women.","'Princess' — taken by all Sikh women.",2],
 ["surname","Gill","Gill is a Punjabi family name. A Jat clan name.","A Jat clan name.",2],
 ["surname","Dhillon","Dhillon is a Punjabi family name. A Jat clan name.","A Jat clan name.",2],
 ["place-name","Amritsar ਅੰਮ੍ਰਿਤਸਰ","Amritsar (ਅੰਮ੍ਰਿਤਸਰ) - 'Pool of nectar' — the holy city.","'Pool of nectar' — the holy city.",2],
 ["place-name","Ludhiana","Ludhiana - From the Lodhi dynasty.","From the Lodhi dynasty.",2],
 ["naming-convention","Singh for men, Kaur for women","Singh for men, Kaur for women: The Khalsa identity gives every Sikh man Singh and every Sikh woman Kaur.","The Khalsa identity gives every Sikh man Singh and every Sikh woman Kaur.",3],
 ["naming-convention","Gurmukhi spellings","Gurmukhi spellings: Punjabi names are written in the Gurmukhi script.","Punjabi names are written in the Gurmukhi script.",3]
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
  var esc="JAH-NMP3-".replace(/[.*+?^${}()|[\]\\]/g,'\\$&');
  if(!new RegExp('^'+esc+'\\d{6}$').test(r.id||''))e.push('id');
  if(typeof r.name!=='string'||!r.name.length)e.push('name');
  if(typeof r.meaning!=='string'||!r.meaning.length)e.push('meaning');
  if(typeof r.title!=='string'||!r.title.length)e.push('title');
  if(CATS.indexOf(r.category)<0)e.push('category');
  if(!(r.ladder_rank>=1&&r.ladder_rank<=3))e.push('ladder_rank');
  return {ok:!e.length,errors:e};
}
var gen={version:"jahdb-names-punjabi-1.0",generate:generate,validate:validate};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("names-punjabi",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
