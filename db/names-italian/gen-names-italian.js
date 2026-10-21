(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var CATS=["first-name", "surname", "place-name", "naming-convention"];
var PREFIX="JAH-NMI-";
/* rows: [category, display name, meaning, origin, ladder_rank] */
var B=[
 ["first-name","Giuseppe","Giuseppe is a masculine given name in Italian. Meaning: God will increase. The Italian form of Joseph.","The Italian form of Joseph.",1],
 ["first-name","Maria","Maria is a feminine given name in Italian. Meaning: Beloved..","Beloved.",1],
 ["first-name","Antonio","Antonio is a masculine given name in Italian. Meaning: Priceless. From Roman Antonius.","From Roman Antonius.",1],
 ["first-name","Sofia","Sofia is a feminine given name in Italian. Meaning: Wisdom. From Greek.","From Greek.",1],
 ["first-name","Marco","Marco is a masculine given name in Italian. Meaning: Of Mars. From Roman Marcus.","From Roman Marcus.",1],
 ["first-name","Giulia","Giulia is a feminine given name in Italian. Meaning: Youthful. From Roman Julius.","From Roman Julius.",1],
 ["first-name","Alessandro","Alessandro is a masculine given name in Italian. Meaning: Defender of men. The Italian form of Alexander.","The Italian form of Alexander.",1],
 ["surname","Rossi","Rossi is a Italian family name. 'Red' — the most common Italian surname.","'Red' — the most common Italian surname.",2],
 ["surname","Russo","Russo is a Italian family name. 'Red' — the southern form.","'Red' — the southern form.",2],
 ["surname","Ferrari","Ferrari is a Italian family name. 'Blacksmith' — occupational.","'Blacksmith' — occupational.",2],
 ["surname","Bianchi","Bianchi is a Italian family name. 'White' — descriptive.","'White' — descriptive.",2],
 ["place-name","Roma","Roma - From the Romulus legend — Rome.","From the Romulus legend — Rome.",2],
 ["place-name","Milano","Milano - From Mediolanum, 'middle plain' — Milan.","From Mediolanum, 'middle plain' — Milan.",2],
 ["naming-convention","Named after grandparents","Named after grandparents: Children are traditionally named for their grandparents.","Children are traditionally named for their grandparents.",3],
 ["naming-convention","Descriptive surnames","Descriptive surnames: Rossi, Bianchi, and Neri began as descriptions.","Rossi, Bianchi, and Neri began as descriptions.",3]
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
  var esc="JAH-NMI-".replace(/[.*+?^${}()|[\]\\]/g,'\\$&');
  if(!new RegExp('^'+esc+'\\d{6}$').test(r.id||''))e.push('id');
  if(typeof r.name!=='string'||!r.name.length)e.push('name');
  if(typeof r.meaning!=='string'||!r.meaning.length)e.push('meaning');
  if(typeof r.title!=='string'||!r.title.length)e.push('title');
  if(CATS.indexOf(r.category)<0)e.push('category');
  if(!(r.ladder_rank>=1&&r.ladder_rank<=3))e.push('ladder_rank');
  return {ok:!e.length,errors:e};
}
var gen={version:"jahdb-names-italian-1.0",generate:generate,validate:validate};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("names-italian",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
