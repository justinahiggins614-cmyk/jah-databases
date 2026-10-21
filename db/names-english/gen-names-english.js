(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var CATS=["first-name", "surname", "place-name", "naming-convention"];
var PREFIX="JAH-NME2-";
/* rows: [category, display name, meaning, origin, ladder_rank] */
var B=[
 ["first-name","James","James is a masculine given name in English. Meaning: Supplanter. From Hebrew Ya'aqov, through Greek Iakobos and Latin Iacomus; borne by kings and apostles.","From Hebrew Ya'aqov, through Greek Iakobos and Latin Iacomus; borne by kings and",1],
 ["first-name","Mary","Mary is a feminine given name in English. Meaning: Beloved; of debated Hebrew origin. From Hebrew Miryam, of uncertain meaning; often glossed 'beloved' or 'bitt","From Hebrew Miryam, of uncertain meaning; often glossed 'beloved' or 'bitter'.",1],
 ["first-name","William","William is a masculine given name in English. Meaning: Resolute protector. From Germanic Wilhelm; brought to England by William the Conqueror in 1066.","From Germanic Wilhelm; brought to England by William the Conqueror in 1066.",1],
 ["first-name","Elizabeth","Elizabeth is a feminine given name in English. Meaning: My God is an oath. From Hebrew Elisheva; borne by two English queens.","From Hebrew Elisheva; borne by two English queens.",1],
 ["first-name","John","John is a masculine given name in English. Meaning: God is gracious. From Hebrew Yochanan via Greek and Latin; long the most common English male name.","From Hebrew Yochanan via Greek and Latin; long the most common English male name",1],
 ["first-name","Sophia","Sophia is a feminine given name in English. Meaning: Wisdom. From Greek sophia; popular across Europe in many spellings.","From Greek sophia; popular across Europe in many spellings.",1],
 ["first-name","Alexander","Alexander is a masculine given name in English. Meaning: Defender of men. From Greek Alexandros; spread by Alexander the Great.","From Greek Alexandros; spread by Alexander the Great.",1],
 ["surname","Smith","Smith is a English family name. Occupational: a worker in metal, from Old English smið.","Occupational: a worker in metal, from Old English smið.",2],
 ["surname","Johnson","Johnson is a English family name. Patronymic: son of John.","Patronymic: son of John.",2],
 ["surname","Brown","Brown is a English family name. Descriptive: brown hair or complexion.","Descriptive: brown hair or complexion.",2],
 ["surname","Taylor","Taylor is a English family name. Occupational: a tailor, from Old French tailleur.","Occupational: a tailor, from Old French tailleur.",2],
 ["place-name","Oxford","Oxford - Ford for oxen — the river crossing where oxen passed.","Ford for oxen — the river crossing where oxen passed.",2],
 ["place-name","Cambridge","Cambridge - Bridge over the River Cam.","Bridge over the River Cam.",2],
 ["naming-convention","Given–middle–family order","Given–middle–family order: English names run given name first, family name last; middle names are common and often honor relatives.","English names run given name first, family name last; middle names are common an",3],
 ["naming-convention","-son patronymics","-son patronymics: Johnson, Wilson, and Jackson began as 'son of John, Will, Jack' before freezing into inherited surnames.","Johnson, Wilson, and Jackson began as 'son of John, Will, Jack' before freezing ",3]
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
  var esc="JAH-NME2-".replace(/[.*+?^${}()|[\]\\]/g,'\\$&');
  if(!new RegExp('^'+esc+'\\d{6}$').test(r.id||''))e.push('id');
  if(typeof r.name!=='string'||!r.name.length)e.push('name');
  if(typeof r.meaning!=='string'||!r.meaning.length)e.push('meaning');
  if(typeof r.title!=='string'||!r.title.length)e.push('title');
  if(CATS.indexOf(r.category)<0)e.push('category');
  if(!(r.ladder_rank>=1&&r.ladder_rank<=3))e.push('ladder_rank');
  return {ok:!e.length,errors:e};
}
var gen={version:"jahdb-names-english-1.0",generate:generate,validate:validate};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("names-english",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
