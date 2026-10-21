(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var SLUG="template-database-signature";
var CATS=["signature"];
var PREFIX="JAH-TMPL-S-";
var KIND="template";
/* rows: [category, title, description-head] — seeded from the archive */
var B=[
 ["signature","Spec Draft Template","TEMPLATE: Spec Draft Template. The JAH spec draft skeleton: header, overview, manufacture, AI-explains, runnab"],
 ["signature","Wiki Article Template","TEMPLATE: Wiki Article Template. JAH Wiki article skeleton: title, subject, full body, sources. Sources ride o"],
 ["signature","Dictionary Entry Template","TEMPLATE: Dictionary Entry Template. Dictionary entry: headword, pronunciation, part of speech, definition in "],
 ["signature","Database Record Template","TEMPLATE: Database Record Template. The canonical database record shape: identity, full body, ladder rank, dem"],
 ["signature","Boundless Brief Template","TEMPLATE: Boundless Brief Template. Orders a boundless generation run: subject, count, seed, edition. Same see"],
 ["signature","Assistant Build Sheet Template","TEMPLATE: Assistant Build Sheet Template. Builds a personal assistant wired live to its home database. An assi"],
 ["signature","Validation Report Template","TEMPLATE: Validation Report Template. Validation report skeleton: target, checks, evidence, verdict, date. A r"],
 ["signature","Demo Confirmation Template","TEMPLATE: Demo Confirmation Template. Confirms a demo by executing it: command, output, confirmed yes/no. Conf"],
 ["signature","Newspaper Report Template","TEMPLATE: Newspaper Report Template. Newspaper report: headline, beat, full body, byline. Facts first, context"],
 ["signature","Leaks Dossier Template","TEMPLATE: Leaks Dossier Template. Leaks dossier: title, classification, full body, filed-by. The governance fi"],
 ["signature","Song Build Sheet Template","TEMPLATE: Song Build Sheet Template. Song build sheet: title, genre, tempo, structure map, full lyrics. A stra"],
 ["signature","Comic Script Template","TEMPLATE: Comic Script Template. Comic panel script: art direction first, dialogue second. Comics are drawn, t"]
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
