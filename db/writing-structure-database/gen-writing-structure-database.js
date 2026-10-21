(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var SLUG="writing-structure-database";
var CATS=["business","essay","poetry","report","script","story","technical"];
var PREFIX="JAH-WRITE-";
var KIND="writing structure";
/* rows: [category, title, description-head] — seeded from the archive */
var B=[
 ["essay","Five-Paragraph Essay","WRITING STRUCTURE: Five-Paragraph Essay. essay Sections: Introduction; Body paragraph 1; Body paragraph 2; Bod"],
 ["essay","Persuasive Essay","WRITING STRUCTURE: Persuasive Essay. essay Sections: Hook + thesis; Reasons; Evidence; Counterargument; Call t"],
 ["report","Research Report (IMRaD)","WRITING STRUCTURE: Research Report (IMRaD). report Sections: Introduction; Methods; Results; Discussion. Worke"],
 ["story","Short Story (Three-Act)","WRITING STRUCTURE: Short Story (Three-Act). story Sections: Setup; Confrontation; Resolution. Worked example i"],
 ["story","Novel Chapter","WRITING STRUCTURE: Novel Chapter. story Sections: Opening hook; Scene goal; Complication; Chapter turn. Worked"],
 ["script","Screenplay Scene","WRITING STRUCTURE: Screenplay Scene. script Sections: Slugline; Action; Dialogue; Transition. Worked example i"],
 ["technical","Technical Documentation","WRITING STRUCTURE: Technical Documentation. technical Sections: Overview; Prerequisites; Steps; Troubleshootin"],
 ["business","Grant Proposal","WRITING STRUCTURE: Grant Proposal. business Sections: Need statement; Goals; Methods; Budget; Evaluation. Work"],
 ["report","News Article (Inverted Pyramid)","WRITING STRUCTURE: News Article (Inverted Pyramid). report Sections: Lede; Key details; Background; Tail. Work"],
 ["business","Business Memo","WRITING STRUCTURE: Business Memo. business Sections: Header; Purpose; Details; Action. Worked example included"],
 ["technical","Lab Report","WRITING STRUCTURE: Lab Report. technical Sections: Aim; Method; Observations; Conclusion. Worked example inclu"],
 ["essay","Book Review","WRITING STRUCTURE: Book Review. essay Sections: Hook; Summary; Analysis; Verdict. Worked example included in t"]
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
