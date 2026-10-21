(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var CATS=["first-name", "surname", "place-name", "naming-convention"];
var PREFIX="JAH-NMS6-";
/* rows: [category, display name, meaning, origin, ladder_rank] */
var B=[
 ["first-name","Mohan","Mohan is a masculine given name in Sindhi. Meaning: Charming..","Charming.",1],
 ["first-name","Lachman","Lachman is a masculine given name in Sindhi. Meaning: A classic Sindhi boys' name..","A classic Sindhi boys' name.",1],
 ["first-name","Hira","Hira is a feminine given name in Sindhi. Meaning: Diamond..","Diamond.",1],
 ["first-name","Dharam","Dharam is a masculine given name in Sindhi. Meaning: Duty, righteousness..","Duty, righteousness.",1],
 ["first-name","Soni","Soni is a feminine given name in Sindhi. Meaning: Beautiful..","Beautiful.",1],
 ["first-name","Kishore","Kishore is a masculine given name in Sindhi. Meaning: Youthful..","Youthful.",1],
 ["first-name","Bhagwanti","Bhagwanti is a feminine given name in Sindhi. Meaning: Fortunate..","Fortunate.",1],
 ["surname","Advani","Advani is a Sindhi family name. 'Of Adu' — the -ani suffix.","'Of Adu' — the -ani suffix.",2],
 ["surname","Shivdasani","Shivdasani is a Sindhi family name. 'Of Shivdas'.","'Of Shivdas'.",2],
 ["surname","Hinduja","Hinduja is a Sindhi family name. A leading Sindhi surname.","A leading Sindhi surname.",2],
 ["surname","Hotchandani","Hotchandani is a Sindhi family name. 'Of Hotchand'.","'Of Hotchand'.",2],
 ["place-name","Karachi","Karachi - From Kolachi, the old fishing village.","From Kolachi, the old fishing village.",2],
 ["place-name","Hyderabad (Sindh)","Hyderabad (Sindh) - The historic Sindhi city.","The historic Sindhi city.",2],
 ["naming-convention","-ani patronymic suffix","-ani patronymic suffix: Advani: 'descendant of Adu' — the signature Sindhi pattern.","Advani: 'descendant of Adu' — the signature Sindhi pattern.",3],
 ["naming-convention","Hindu and Muslim pools","Hindu and Muslim pools: Sindhi Hindus and Muslims draw on different name pools.","Sindhi Hindus and Muslims draw on different name pools.",3]
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
  var esc="JAH-NMS6-".replace(/[.*+?^${}()|[\]\\]/g,'\\$&');
  if(!new RegExp('^'+esc+'\\d{6}$').test(r.id||''))e.push('id');
  if(typeof r.name!=='string'||!r.name.length)e.push('name');
  if(typeof r.meaning!=='string'||!r.meaning.length)e.push('meaning');
  if(typeof r.title!=='string'||!r.title.length)e.push('title');
  if(CATS.indexOf(r.category)<0)e.push('category');
  if(!(r.ladder_rank>=1&&r.ladder_rank<=3))e.push('ladder_rank');
  return {ok:!e.length,errors:e};
}
var gen={version:"jahdb-names-sindhi-1.0",generate:generate,validate:validate};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("names-sindhi",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
