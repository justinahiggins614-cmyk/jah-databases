(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var CATS=["first-name", "surname", "place-name", "naming-convention"];
var PREFIX="JAH-NMR-";
/* rows: [category, display name, meaning, origin, ladder_rank] */
var B=[
 ["first-name","Ivan","Ivan is a masculine given name in Russian. Meaning: God is gracious. The Russian form of John; the classic Russian name.","The Russian form of John; the classic Russian name.",1],
 ["first-name","Maria","Maria is a feminine given name in Russian. Meaning: Beloved. The Russian form of Mary.","The Russian form of Mary.",1],
 ["first-name","Aleksandr","Aleksandr is a masculine given name in Russian. Meaning: Defender of men. From Greek; borne by tsars.","From Greek; borne by tsars.",1],
 ["first-name","Olga","Olga is a feminine given name in Russian. Meaning: Holy. From Norse Helga.","From Norse Helga.",1],
 ["first-name","Dmitri","Dmitri is a masculine given name in Russian. Meaning: Of Demeter. From the Greek goddess of harvest.","From the Greek goddess of harvest.",1],
 ["first-name","Anastasia","Anastasia is a feminine given name in Russian. Meaning: Resurrection. From Greek anastasis.","From Greek anastasis.",1],
 ["first-name","Sergei","Sergei is a masculine given name in Russian. Meaning: From the Roman family name Sergius..","From the Roman family name Sergius.",1],
 ["surname","Ivanov","Ivanov is a Russian family name. 'Son of Ivan' — patronymic surname.","'Son of Ivan' — patronymic surname.",2],
 ["surname","Petrov","Petrov is a Russian family name. 'Son of Peter'.","'Son of Peter'.",2],
 ["surname","Smirnov","Smirnov is a Russian family name. 'Quiet one' — descriptive.","'Quiet one' — descriptive.",2],
 ["surname","Kuznetsov","Kuznetsov is a Russian family name. 'Smith's son' — occupational.","'Smith's son' — occupational.",2],
 ["place-name","Moscow","Moscow - From the Moskva River.","From the Moskva River.",2],
 ["place-name","Saint Petersburg","Saint Petersburg - Named for Saint Peter by Peter the Great.","Named for Saint Peter by Peter the Great.",2],
 ["naming-convention","Given + patronymic + surname","Given + patronymic + surname: Ivan Ivanovich Petrov: given name, 'son of Ivan', family name.","Ivan Ivanovich Petrov: given name, 'son of Ivan', family name.",3],
 ["naming-convention","Gendered surname endings","Gendered surname endings: -ov becomes -ova, -sky becomes -skaya for women.","-ov becomes -ova, -sky becomes -skaya for women.",3]
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
  var esc="JAH-NMR-".replace(/[.*+?^${}()|[\]\\]/g,'\\$&');
  if(!new RegExp('^'+esc+'\\d{6}$').test(r.id||''))e.push('id');
  if(typeof r.name!=='string'||!r.name.length)e.push('name');
  if(typeof r.meaning!=='string'||!r.meaning.length)e.push('meaning');
  if(typeof r.title!=='string'||!r.title.length)e.push('title');
  if(CATS.indexOf(r.category)<0)e.push('category');
  if(!(r.ladder_rank>=1&&r.ladder_rank<=3))e.push('ladder_rank');
  return {ok:!e.length,errors:e};
}
var gen={version:"jahdb-names-russian-1.0",generate:generate,validate:validate};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("names-russian",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
