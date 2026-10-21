(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var CATS=["first-name", "surname", "place-name", "naming-convention"];
var PREFIX="JAH-NMT5-";
/* rows: [category, display name, meaning, origin, ladder_rank] */
var B=[
 ["first-name","Somchai สมชาย","Somchai (สมชาย) is a masculine given name in Thai. Meaning: Worthy man. Som (worthy) + chai (man).","Som (worthy) + chai (man).",1],
 ["first-name","Malee มะลิ","Malee (มะลิ) is a feminine given name in Thai. Meaning: Jasmine..","Jasmine.",1],
 ["first-name","Anan","Anan is a masculine given name in Thai. Meaning: Joy..","Joy.",1],
 ["first-name","Nattaya","Nattaya is a feminine given name in Thai. Meaning: A popular girls' name..","A popular girls' name.",1],
 ["first-name","Prasert","Prasert is a masculine given name in Thai. Meaning: Excellent..","Excellent.",1],
 ["first-name","Siriporn","Siriporn is a feminine given name in Thai. Meaning: Glory + blessing..","Glory + blessing.",1],
 ["first-name","Chai","Chai is a masculine given name in Thai. Meaning: Victory.. A strong boys' name.","A strong boys' name.",1],
 ["surname","Long unique surnames","Long unique surnames is a Thai family name. Since 1913 every Thai surname must be unique to its family.","Since 1913 every Thai surname must be unique to its family.",2],
 ["surname","Sanskrit/Pali roots","Sanskrit/Pali roots is a Thai family name. Somchai, Siriporn, and Prasert draw on the classical pool.","Somchai, Siriporn, and Prasert draw on the classical pool.",2],
 ["surname","No inherited Western-style names","No inherited Western-style names is a Thai family name. Surnames were created, not inherited, in 1913.","Surnames were created, not inherited, in 1913.",2],
 ["surname","Royal bestowals","Royal bestowals is a Thai family name. Some surnames were bestowed by the king.","Some surnames were bestowed by the king.",2],
 ["place-name","Bangkok","Bangkok - From Bang Makok, 'village of olive plums'.","From Bang Makok, 'village of olive plums'.",2],
 ["place-name","Krung Thep","Krung Thep - 'City of angels' — the ceremonial name of Bangkok.","'City of angels' — the ceremonial name of Bangkok.",2],
 ["naming-convention","Unique surnames by law","Unique surnames by law: The 1913 law requires each family's surname to be unique.","The 1913 law requires each family's surname to be unique.",3],
 ["naming-convention","The nickname system","The nickname system: Everyone goes by a short nickname — Lek ('small'), Noi ('little').","Everyone goes by a short nickname — Lek ('small'), Noi ('little').",3]
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
  var esc="JAH-NMT5-".replace(/[.*+?^${}()|[\]\\]/g,'\\$&');
  if(!new RegExp('^'+esc+'\\d{6}$').test(r.id||''))e.push('id');
  if(typeof r.name!=='string'||!r.name.length)e.push('name');
  if(typeof r.meaning!=='string'||!r.meaning.length)e.push('meaning');
  if(typeof r.title!=='string'||!r.title.length)e.push('title');
  if(CATS.indexOf(r.category)<0)e.push('category');
  if(!(r.ladder_rank>=1&&r.ladder_rank<=3))e.push('ladder_rank');
  return {ok:!e.length,errors:e};
}
var gen={version:"jahdb-names-thai-1.0",generate:generate,validate:validate};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("names-thai",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
