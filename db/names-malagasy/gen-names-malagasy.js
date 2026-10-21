(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var CATS=["first-name", "surname", "place-name", "naming-convention"];
var PREFIX="JAH-NMM4-";
/* rows: [category, display name, meaning, origin, ladder_rank] */
var B=[
 ["first-name","Voahangy","Voahangy is a feminine given name in Malagasy. Meaning: A classic Malagasy girls' name..","A classic Malagasy girls' name.",1],
 ["first-name","Nirina","Nirina is a unisex given name in Malagasy. Meaning: A common Malagasy name; unisex..","A common Malagasy name; unisex.",1],
 ["first-name","Tahina","Tahina is a masculine given name in Malagasy. Meaning: A common Malagasy boys' name..","A common Malagasy boys' name.",1],
 ["first-name","Hasina","Hasina is a feminine given name in Malagasy. Meaning: A traditional girls' name..","A traditional girls' name.",1],
 ["first-name","Tiana","Tiana is a unisex given name in Malagasy. Meaning: A common Malagasy name; unisex..","A common Malagasy name; unisex.",1],
 ["first-name","Miora","Miora is a feminine given name in Malagasy. Meaning: A popular girls' name..","A popular girls' name.",1],
 ["first-name","Andry","Andry is a masculine given name in Malagasy. Meaning: A classic boys' name..","A classic boys' name.",1],
 ["surname","No traditional surnames","No traditional surnames is a Malagasy family name. Malagasy traditionally use single given names.","Malagasy traditionally use single given names.",2],
 ["surname","Ancestral reuse","Ancestral reuse is a Malagasy family name. Children are often named for ancestors.","Children are often named for ancestors.",2],
 ["surname","Single names complete","Single names complete is a Malagasy family name. One name is a full name.","One name is a full name.",2],
 ["surname","Modern two-name forms","Modern two-name forms is a Malagasy family name. Given + father's name appears in modern records.","Given + father's name appears in modern records.",2],
 ["place-name","Antananarivo","Antananarivo - 'City of a thousand' — the highland capital.","'City of a thousand' — the highland capital.",2],
 ["place-name","Toamasina","Toamasina - The great eastern port.","The great eastern port.",2],
 ["naming-convention","Ancestral names reused","Ancestral names reused: Naming a child for an ancestor honors the lineage.","Naming a child for an ancestor honors the lineage.",3],
 ["naming-convention","Single names common","Single names common: One given name is traditionally complete.","One given name is traditionally complete.",3]
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
  var esc="JAH-NMM4-".replace(/[.*+?^${}()|[\]\\]/g,'\\$&');
  if(!new RegExp('^'+esc+'\\d{6}$').test(r.id||''))e.push('id');
  if(typeof r.name!=='string'||!r.name.length)e.push('name');
  if(typeof r.meaning!=='string'||!r.meaning.length)e.push('meaning');
  if(typeof r.title!=='string'||!r.title.length)e.push('title');
  if(CATS.indexOf(r.category)<0)e.push('category');
  if(!(r.ladder_rank>=1&&r.ladder_rank<=3))e.push('ladder_rank');
  return {ok:!e.length,errors:e};
}
var gen={version:"jahdb-names-malagasy-1.0",generate:generate,validate:validate};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("names-malagasy",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
