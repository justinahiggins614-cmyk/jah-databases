(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var SLUG="template-database";
var CATS=["business","code","design","legal","personal"];
var PREFIX="JAH-TMPL-";
var KIND="template";
/* rows: [category, title, description-head] — seeded from the archive */
var B=[
 ["business","Business Letter Template","TEMPLATE: Business Letter Template. The block-format business letter: sender block, date, recipient block, sal"],
 ["business","Resume Template","TEMPLATE: Resume Template. One-page resume skeleton: contact line, experience, education, skills. One page per"],
 ["business","Meeting Agenda Template","TEMPLATE: Meeting Agenda Template. Time-boxed agenda: three items, ten minutes each, action items at the end. "],
 ["business","Project Proposal Template","TEMPLATE: Project Proposal Template. Proposal skeleton: problem, solution, timeline, budget, team. Lead with t"],
 ["code","Python Script Boilerplate","TEMPLATE: Python Script Boilerplate. Minimal runnable Python script: docstring, main(), and the standard guard"],
 ["code","HTML5 Page Boilerplate","TEMPLATE: HTML5 Page Boilerplate. The smallest valid HTML5 page: doctype, charset, viewport, title, body. The "],
 ["design","CSS Stylesheet Starter","TEMPLATE: CSS Stylesheet Starter. Starter stylesheet: variables, reset, body type, and a centered container. C"],
 ["business","Invoice Template","TEMPLATE: Invoice Template. Plain-text invoice: number, bill-to, line item math, total, due date. Always show "],
 ["legal","Simple NDA Template","TEMPLATE: Simple NDA Template. A short mutual NDA: parties, effective date, obligation, term. (General informa"],
 ["legal","Simple Rental Agreement Template","TEMPLATE: Simple Rental Agreement Template. Basic lease skeleton: parties, property, rent, term. (General info"],
 ["business","Press Release Template","TEMPLATE: Press Release Template. Press release shape: headline, dateline, body, quote, contact. The headline "],
 ["business","Email Newsletter Template","TEMPLATE: Email Newsletter Template. Newsletter shape: subject hook, greeting, two stories, unsubscribe link. "]
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
