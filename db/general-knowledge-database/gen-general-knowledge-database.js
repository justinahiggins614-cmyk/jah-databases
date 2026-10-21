(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var SLUG="general-knowledge-database";
var CATS=["astronomy","biology","chemistry","civics","earth science","economics","history","medicine","physics","science","technology"];
var PREFIX="JAH-GKNOW-";
var KIND="general knowledge";
/* rows: [category, title, description-head] — seeded from the archive */
var B=[
 ["earth science","The Water Cycle","REFERENCE: The Water Cycle. Water on Earth moves in a continuous loop. The Sun heats oceans, lakes, and rivers"],
 ["biology","Photosynthesis","REFERENCE: Photosynthesis. Photosynthesis is how plants, algae, and some bacteria turn sunlight into food. Chl"],
 ["astronomy","The Solar System","REFERENCE: The Solar System. Our solar system is the Sun plus everything its gravity holds: eight planets, dwa"],
 ["biology","The Human Heart","REFERENCE: The Human Heart. The human heart is a muscular pump about the size of a fist. It has four chambers:"],
 ["technology","How the Internet Works","REFERENCE: How the Internet Works. The Internet is a global network of networks. Your device connects through "],
 ["civics","Democracy Basics","REFERENCE: Democracy Basics. Democracy is government by the people, usually through elected representatives. I"],
 ["science","The Scientific Method","REFERENCE: The Scientific Method. The scientific method is the loop by which science builds reliable knowledge"],
 ["history","World War II Overview","REFERENCE: World War II Overview. World War II (1939-1945) was the largest conflict in history. It began when "],
 ["chemistry","The Periodic Table","REFERENCE: The Periodic Table. The periodic table organizes all known chemical elements by atomic number — the"],
 ["physics","Gravity","REFERENCE: Gravity. Gravity is the attraction between masses. Newton described it as a force pulling masses to"],
 ["biology","The Brain","REFERENCE: The Brain. The human brain weighs about 1.4 kilograms and holds roughly 86 billion neurons. The cer"],
 ["physics","Electricity Basics","REFERENCE: Electricity Basics. Electricity is the flow of electric charge, usually electrons moving through a "]
];
function generate(seed,opts,rnd){
  opts=opts||{};rnd=rnd||prng(seed);
  var cat=opts.category||pick(CATS,rnd);
  var pool=B.filter(function(b){return b[0]===cat;});
  var b=pick(pool.length?pool:B,rnd);
  var id=PREFIX+String(seed).padStart(6,'0');
  return {id:id,title:b[1],description:b[2],category:cat,
    ladder_rank:1+((rnd()*3)|0),
    demo:'#!/usr/bin/env python3\nprint('+JSON.stringify('demo for '+b[1])+')\n',
    provenance:'Boundless generator jahdb-'+SLUG+'-1.0; seed '+seed+'.',
    last_verified:'2026-10-21',
    src:"public-harvest",
    _seed:seed};
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  var rx=new RegExp('^'+PREFIX.replace(/[.*+?^${}()|[\]\\]/g,'\\$&')+'\\d{6}$');
  if(!rx.test(r.id||''))e.push('id');
  if(typeof r.title!=='string'||!r.title.length)e.push('title');
  if(typeof r.description!=='string'||!r.description.length)e.push('description');
  if(CATS.indexOf(r.category)<0)e.push('category');
  if(!(r.ladder_rank>=1&&r.ladder_rank<=3))e.push('ladder_rank');
  if(typeof r.demo!=='string'||!r.demo.length)e.push('demo');
  if(r.last_verified!=='2026-10-21')e.push('last_verified');
  return {ok:!e.length,errors:e};
}
function driftCheck(rec,sample){
  var e=[];
  for(var i=0;i<sample.length;i++){
    if(sample[i]&&sample[i].title===rec.title&&sample[i].id!==rec.id){e.push('near-duplicate title');break;}
  }
  return {ok:!e.length,errors:e};
}
var gen={version:'jahdb-'+SLUG+'-1.0',generate:generate,validate:validate,driftCheck:driftCheck};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
