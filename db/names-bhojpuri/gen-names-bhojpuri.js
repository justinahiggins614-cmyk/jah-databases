(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var CATS=["first-name", "surname", "place-name", "naming-convention"];
var PREFIX="JAH-NMB2-";
/* rows: [category, display name, meaning, origin, ladder_rank] */
var B=[
 ["first-name","Ram","Ram is a masculine given name in Bhojpuri. Meaning: The hero of the Ramayana..","The hero of the Ramayana.",1],
 ["first-name","Sita","Sita is a feminine given name in Bhojpuri. Meaning: The heroine of the Ramayana; 'furrow'..","The heroine of the Ramayana; 'furrow'.",1],
 ["first-name","Ramesh","Ramesh is a masculine given name in Bhojpuri. Meaning: Lord of Rama..","Lord of Rama.",1],
 ["first-name","Poonam","Poonam is a feminine given name in Bhojpuri. Meaning: Full moon..","Full moon.",1],
 ["first-name","Suresh","Suresh is a masculine given name in Bhojpuri. Meaning: Ruler of gods..","Ruler of gods.",1],
 ["first-name","Munni","Munni is a feminine given name in Bhojpuri. Meaning: An affectionate girls' name..","An affectionate girls' name.",1],
 ["first-name","Bablu","Bablu is a masculine given name in Bhojpuri. Meaning: An affectionate boys' name..","An affectionate boys' name.",1],
 ["surname","Singh","Singh is a Bhojpuri family name. 'Lion'.","'Lion'.",2],
 ["surname","Yadav","Yadav is a Bhojpuri family name. Descendant of Yadu — a community name.","Descendant of Yadu — a community name.",2],
 ["surname","Tiwari","Tiwari is a Bhojpuri family name. From Tripati, 'learned in three Vedas'.","From Tripati, 'learned in three Vedas'.",2],
 ["surname","Mishra","Mishra is a Bhojpuri family name. 'Mixed' — a Brahmin title.","'Mixed' — a Brahmin title.",2],
 ["place-name","Varanasi","Varanasi - Between the Varuna and Asi rivers.","Between the Varuna and Asi rivers.",2],
 ["place-name","Patna","Patna - From Pataliputra, the ancient capital.","From Pataliputra, the ancient capital.",2],
 ["naming-convention","Ram and Sita devotion","Ram and Sita devotion: Devotional names from the Ramayana dominate.","Devotional names from the Ramayana dominate.",3],
 ["naming-convention","Caste-linked surnames","Caste-linked surnames: Surnames like Tiwari and Yadav mark community.","Surnames like Tiwari and Yadav mark community.",3]
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
  var esc="JAH-NMB2-".replace(/[.*+?^${}()|[\]\\]/g,'\\$&');
  if(!new RegExp('^'+esc+'\\d{6}$').test(r.id||''))e.push('id');
  if(typeof r.name!=='string'||!r.name.length)e.push('name');
  if(typeof r.meaning!=='string'||!r.meaning.length)e.push('meaning');
  if(typeof r.title!=='string'||!r.title.length)e.push('title');
  if(CATS.indexOf(r.category)<0)e.push('category');
  if(!(r.ladder_rank>=1&&r.ladder_rank<=3))e.push('ladder_rank');
  return {ok:!e.length,errors:e};
}
var gen={version:"jahdb-names-bhojpuri-1.0",generate:generate,validate:validate};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("names-bhojpuri",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
