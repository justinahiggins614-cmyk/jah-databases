(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var CATS=["first-name", "surname", "place-name", "naming-convention"];
var PREFIX="JAH-NMG-";
/* rows: [category, display name, meaning, origin, ladder_rank] */
var B=[
 ["first-name","Hans","Hans is a masculine given name in German. Meaning: Short of Johannes, 'God is gracious'..","Short of Johannes, 'God is gracious'.",1],
 ["first-name","Friedrich","Friedrich is a masculine given name in German. Meaning: Peaceful ruler. From Germanic fridu + rik.","From Germanic fridu + rik.",1],
 ["first-name","Greta","Greta is a feminine given name in German. Meaning: Pearl. Short of Margarete.","Short of Margarete.",1],
 ["first-name","Otto","Otto is a masculine given name in German. Meaning: Wealth. From Germanic od, 'riches'.","From Germanic od, 'riches'.",1],
 ["first-name","Lena","Lena is a feminine given name in German. Meaning: Short of Helena or Magdalena..","Short of Helena or Magdalena.",1],
 ["first-name","Lukas","Lukas is a masculine given name in German. Meaning: From Lucania. The German form of Luke.","The German form of Luke.",1],
 ["first-name","Emma","Emma is a feminine given name in German. Meaning: Universal. From Germanic ermen.","From Germanic ermen.",1],
 ["surname","Müller","Müller is a German family name. 'Miller' — occupational.","'Miller' — occupational.",2],
 ["surname","Schmidt","Schmidt is a German family name. 'Smith' — occupational.","'Smith' — occupational.",2],
 ["surname","Weber","Weber is a German family name. 'Weaver' — occupational.","'Weaver' — occupational.",2],
 ["surname","Fischer","Fischer is a German family name. 'Fisher' — occupational.","'Fisher' — occupational.",2],
 ["place-name","München","München - 'By the monks' — Munich.","'By the monks' — Munich.",2],
 ["place-name","Hamburg","Hamburg - 'Fortress' — from Hamme burg.","'Fortress' — from Hamme burg.",2],
 ["naming-convention","Given + family name","Given + family name: German names run given name first, family name last.","German names run given name first, family name last.",3],
 ["naming-convention","-chen and -lein","-chen and -lein: Diminutives like Hänsel and Fräulein soften names affectionately.","Diminutives like Hänsel and Fräulein soften names affectionately.",3]
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
  var esc="JAH-NMG-".replace(/[.*+?^${}()|[\]\\]/g,'\\$&');
  if(!new RegExp('^'+esc+'\\d{6}$').test(r.id||''))e.push('id');
  if(typeof r.name!=='string'||!r.name.length)e.push('name');
  if(typeof r.meaning!=='string'||!r.meaning.length)e.push('meaning');
  if(typeof r.title!=='string'||!r.title.length)e.push('title');
  if(CATS.indexOf(r.category)<0)e.push('category');
  if(!(r.ladder_rank>=1&&r.ladder_rank<=3))e.push('ladder_rank');
  return {ok:!e.length,errors:e};
}
var gen={version:"jahdb-names-german-1.0",generate:generate,validate:validate};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("names-german",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
