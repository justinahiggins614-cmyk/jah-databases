(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var CATS=["first-name", "surname", "place-name", "naming-convention"];
var PREFIX="JAH-NMP-";
/* rows: [category, display name, meaning, origin, ladder_rank] */
var B=[
 ["first-name","Dariush داریوش","Dariush (داریوش) is a masculine given name in Persian. Meaning: Possessing goodness. From Old Persian Darayavaush; borne by Achaemenid kings.","From Old Persian Darayavaush; borne by Achaemenid kings.",1],
 ["first-name","Cyrus کوروش","Cyrus (کوروش) is a masculine given name in Persian. Meaning: Of debated origin. The founder of the Persian Empire; Greek Kyros.","The founder of the Persian Empire; Greek Kyros.",1],
 ["first-name","Sara سارا","Sara (سارا) is a feminine given name in Persian. Meaning: Pure. A leading girls' name.","A leading girls' name.",1],
 ["first-name","Leila لیلی","Leila (لیلی) is a feminine given name in Persian. Meaning: Night. From Arabic layl; a classic poetic name.","From Arabic layl; a classic poetic name.",1],
 ["first-name","Arash آرش","Arash (آرش) is a masculine given name in Persian. Meaning: The hero archer of Iranian legend..","The hero archer of Iranian legend.",1],
 ["first-name","Niloofar نیلوفر","Niloofar (نیلوفر) is a feminine given name in Persian. Meaning: Lotus. The water lily; a graceful girls' name.","The water lily; a graceful girls' name.",1],
 ["first-name","Kian کیان","Kian (کیان) is a masculine given name in Persian. Meaning: Royal. From the Kayanian dynasty of legend.","From the Kayanian dynasty of legend.",1],
 ["surname","Mohammadi","Mohammadi is a Persian family name. 'Of Muhammad' — lineage suffix -i.","'Of Muhammad' — lineage suffix -i.",2],
 ["surname","Hosseini","Hosseini is a Persian family name. 'Of Hossein'.","'Of Hossein'.",2],
 ["surname","Karimi","Karimi is a Persian family name. 'Generous' — from karim.","'Generous' — from karim.",2],
 ["surname","Ahmadi","Ahmadi is a Persian family name. 'Of Ahmad'.","'Of Ahmad'.",2],
 ["place-name","Tehran طهران","Tehran (طهران) - Etymology debated; the modern capital's old name.","Etymology debated; the modern capital's old name.",2],
 ["place-name","Isfahan","Isfahan - Traditionally 'gathering place of the army'.","Traditionally 'gathering place of the army'.",2],
 ["naming-convention","Given + family since 1919","Given + family since 1919: Iran's civil registration law made family names standard in the 20th century.","Iran's civil registration law made family names standard in the 20th century.",3],
 ["naming-convention","Names from the Shahnameh","Names from the Shahnameh: Epic heroes like Rostam and Sohrab supply boys' names.","Epic heroes like Rostam and Sohrab supply boys' names.",3]
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
  var esc="JAH-NMP-".replace(/[.*+?^${}()|[\]\\]/g,'\\$&');
  if(!new RegExp('^'+esc+'\\d{6}$').test(r.id||''))e.push('id');
  if(typeof r.name!=='string'||!r.name.length)e.push('name');
  if(typeof r.meaning!=='string'||!r.meaning.length)e.push('meaning');
  if(typeof r.title!=='string'||!r.title.length)e.push('title');
  if(CATS.indexOf(r.category)<0)e.push('category');
  if(!(r.ladder_rank>=1&&r.ladder_rank<=3))e.push('ladder_rank');
  return {ok:!e.length,errors:e};
}
var gen={version:"jahdb-names-persian-1.0",generate:generate,validate:validate};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("names-persian",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
