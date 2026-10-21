(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var CATS=["first-name", "surname", "place-name", "naming-convention"];
var PREFIX="JAH-NMP4-";
/* rows: [category, display name, meaning, origin, ladder_rank] */
var B=[
 ["first-name","Ahmad","Ahmad is a masculine given name in Pashto. Meaning: Most praised..","Most praised.",1],
 ["first-name","Gul گل","Gul (گل) is a unisex given name in Pashto. Meaning: Flower. Unisex; a beloved name element.","Unisex; a beloved name element.",1],
 ["first-name","Zar زر","Zar (زر) is a unisex given name in Pashto. Meaning: Gold.. Unisex.","Unisex.",1],
 ["first-name","Palwasha","Palwasha is a feminine given name in Pashto. Meaning: Ray of light.. A graceful girls' name.","A graceful girls' name.",1],
 ["first-name","Zalmai","Zalmai is a masculine given name in Pashto. Meaning: Young.. A classic boys' name.","A classic boys' name.",1],
 ["first-name","Storai","Storai is a feminine given name in Pashto. Meaning: Star.. A poetic girls' name.","A poetic girls' name.",1],
 ["first-name","Tor","Tor is a masculine given name in Pashto. Meaning: Black.. A strong boys' name.","A strong boys' name.",1],
 ["surname","Khan","Khan is a Pashto family name. 'Leader' — the universal title-surname.","'Leader' — the universal title-surname.",2],
 ["surname","Ahmadzai","Ahmadzai is a Pashto family name. 'Son of Ahmad' — the -zai suffix.","'Son of Ahmad' — the -zai suffix.",2],
 ["surname","Popalzai","Popalzai is a Pashto family name. 'Son of Popal' — a tribal name.","'Son of Popal' — a tribal name.",2],
 ["surname","Durrani","Durrani is a Pashto family name. 'Of the pearl age' — the royal tribe.","'Of the pearl age' — the royal tribe.",2],
 ["place-name","Kabul","Kabul - From the Kubha River.","From the Kubha River.",2],
 ["place-name","Kandahar","Kandahar - From Alexandria — Alexander's foundation.","From Alexandria — Alexander's foundation.",2],
 ["naming-convention","-zai, 'son of'","-zai, 'son of': Ahmadzai and Popalzai: -zai marks descent from a named ancestor.","Ahmadzai and Popalzai: -zai marks descent from a named ancestor.",3],
 ["naming-convention","-khel clan suffix","-khel clan suffix: -khel marks the clan or extended family.","-khel marks the clan or extended family.",3]
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
  var esc="JAH-NMP4-".replace(/[.*+?^${}()|[\]\\]/g,'\\$&');
  if(!new RegExp('^'+esc+'\\d{6}$').test(r.id||''))e.push('id');
  if(typeof r.name!=='string'||!r.name.length)e.push('name');
  if(typeof r.meaning!=='string'||!r.meaning.length)e.push('meaning');
  if(typeof r.title!=='string'||!r.title.length)e.push('title');
  if(CATS.indexOf(r.category)<0)e.push('category');
  if(!(r.ladder_rank>=1&&r.ladder_rank<=3))e.push('ladder_rank');
  return {ok:!e.length,errors:e};
}
var gen={version:"jahdb-names-pashto-1.0",generate:generate,validate:validate};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("names-pashto",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
