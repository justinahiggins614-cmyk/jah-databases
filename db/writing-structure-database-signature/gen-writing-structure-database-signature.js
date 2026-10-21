(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var SLUG="writing-structure-database-signature";
var CATS=["signature"];
var PREFIX="JAH-WRITE-S-";
var KIND="writing structure";
/* rows: [category, title, description-head] — seeded from the archive */
var B=[
 ["signature","Signature Spec Draft Structure","WRITING STRUCTURE: Signature Spec Draft Structure. signature Sections: Header block; Overview lens; Manufactur"],
 ["signature","Boundless Record Structure","WRITING STRUCTURE: Boundless Record Structure. signature Sections: Identity; Full body; Ladder rank; Demo; Pro"],
 ["signature","Maker-Mark Application Note","WRITING STRUCTURE: Maker-Mark Application Note. signature Sections: The mark; First use; What it covers; Verif"],
 ["signature","Database Build Brief","WRITING STRUCTURE: Database Build Brief. signature Sections: Name and slug; Subject; Editions; Canon checklist"],
 ["signature","Assistant Build Sheet","WRITING STRUCTURE: Assistant Build Sheet. signature Sections: Name; Role; Home database; Personality; Powers. "],
 ["signature","Validation Report Structure","WRITING STRUCTURE: Validation Report Structure. signature Sections: Target; Method; Evidence; Verdict; Date. W"],
 ["signature","Demo Confirmation Structure","WRITING STRUCTURE: Demo Confirmation Structure. signature Sections: Target demo; How it ran; Output; Confirmed"],
 ["signature","Teaching Ladder Lesson","WRITING STRUCTURE: Teaching Ladder Lesson. signature Sections: Rung 1: simple; Rung 2: compounded; Rung 3: mos"],
 ["signature","Mirror-Sweep Entry","WRITING STRUCTURE: Mirror-Sweep Entry. signature Sections: Signature record; Public counterpart; What matches;"],
 ["signature","Newspaper Report Structure","WRITING STRUCTURE: Newspaper Report Structure. signature Sections: Headline; Beat; Body; Byline. Worked exampl"],
 ["signature","Leaks Dossier Structure","WRITING STRUCTURE: Leaks Dossier Structure. signature Sections: Title; Classification; Body; Filed by. Worked "],
 ["signature","Song Build Structure","WRITING STRUCTURE: Song Build Structure. signature Sections: Title and genre; Tempo; Structure; Lyrics; Mix no"]
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
    src:"signature-generated-completion",
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
