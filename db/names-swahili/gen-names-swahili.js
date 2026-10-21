(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var CATS=["first-name", "surname", "place-name", "naming-convention"];
var PREFIX="JAH-NMS5-";
/* rows: [category, display name, meaning, origin, ladder_rank] */
var B=[
 ["first-name","Juma","Juma is a masculine given name in Swahili. Meaning: Friday. Given to Friday-born boys.","Given to Friday-born boys.",1],
 ["first-name","Amina","Amina is a feminine given name in Swahili. Meaning: Trustworthy..","Trustworthy.",1],
 ["first-name","Baraka","Baraka is a masculine given name in Swahili. Meaning: Blessing..","Blessing.",1],
 ["first-name","Neema","Neema is a feminine given name in Swahili. Meaning: Grace..","Grace.",1],
 ["first-name","Rehema","Rehema is a feminine given name in Swahili. Meaning: Mercy..","Mercy.",1],
 ["first-name","Said","Said is a masculine given name in Swahili. Meaning: Happy..","Happy.",1],
 ["first-name","Zawadi","Zawadi is a feminine given name in Swahili. Meaning: Gift..","Gift.",1],
 ["surname","Arabic patronymics","Arabic patronymics is a Swahili family name. Bin/binti forms appear in coastal Muslim families.","Bin/binti forms appear in coastal Muslim families.",2],
 ["surname","Bantu roots","Bantu roots is a Swahili family name. Names like Zawadi ('gift') are Bantu.","Names like Zawadi ('gift') are Bantu.",2],
 ["surname","No fixed surnames traditionally","No fixed surnames traditionally is a Swahili family name. Family names are a modern layer.","Family names are a modern layer.",2],
 ["surname","Father's name as second name","Father's name as second name is a Swahili family name. The father's given name serves as the second name.","The father's given name serves as the second name.",2],
 ["place-name","Dar es Salaam","Dar es Salaam - 'Haven of peace'.","'Haven of peace'.",2],
 ["place-name","Nairobi","Nairobi - From Maasai 'cool water'.","From Maasai 'cool water'.",2],
 ["naming-convention","Day names","Day names: Juma (Friday) and Khamis (Thursday) mark the birth weekday.","Juma (Friday) and Khamis (Thursday) mark the birth weekday.",3],
 ["naming-convention","Arabic + Bantu blend","Arabic + Bantu blend: The name pool fuses Qur'anic names with Bantu roots.","The name pool fuses Qur'anic names with Bantu roots.",3]
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
  var esc="JAH-NMS5-".replace(/[.*+?^${}()|[\]\\]/g,'\\$&');
  if(!new RegExp('^'+esc+'\\d{6}$').test(r.id||''))e.push('id');
  if(typeof r.name!=='string'||!r.name.length)e.push('name');
  if(typeof r.meaning!=='string'||!r.meaning.length)e.push('meaning');
  if(typeof r.title!=='string'||!r.title.length)e.push('title');
  if(CATS.indexOf(r.category)<0)e.push('category');
  if(!(r.ladder_rank>=1&&r.ladder_rank<=3))e.push('ladder_rank');
  return {ok:!e.length,errors:e};
}
var gen={version:"jahdb-names-swahili-1.0",generate:generate,validate:validate};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("names-swahili",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
