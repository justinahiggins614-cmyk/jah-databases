(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var SLUG="general-knowledge-database-signature";
var CATS=["signature systems"];
var PREFIX="JAH-GKNOW-S-";
var KIND="general knowledge";
/* rows: [category, title, description-head] — seeded from the archive */
var B=[
 ["signature systems","The Maker's Mark","REFERENCE: The Maker's Mark. A maker's mark is the personal signature a creator puts on their work — the craft"],
 ["signature systems","Deterministic Identity","REFERENCE: Deterministic Identity. Deterministic identity means an ID that is assigned by rule, not by whim. I"],
 ["signature systems","The Teaching Ladder","REFERENCE: The Teaching Ladder. The teaching ladder is the JAH rule that every subject is taught in three rung"],
 ["signature systems","Boundless Generation","REFERENCE: Boundless Generation. Boundless generation is the JAH method for growing archives without bound: a "],
 ["signature systems","Archive-Aware AI","REFERENCE: Archive-Aware AI. An archive-aware AI is one that knows the archive it serves: what it holds, how m"],
 ["signature systems","The Million March","REFERENCE: The Million March. The million march is the standing JAH goal: every database marches toward one mi"],
 ["signature systems","Public and Signature Editions","REFERENCE: Public and Signature Editions. Every JAH database ships in two editions: public and Signature. The "],
 ["signature systems","The Full Record Rule","REFERENCE: The Full Record Rule. The full record rule: every database record is the complete, fully-formed ite"],
 ["signature systems","Provenance on Everything","REFERENCE: Provenance on Everything. In the JAH system, provenance rides on every record: where it came from, "],
 ["signature systems","Drift Control","REFERENCE: Drift Control. Drift control keeps generated records honest: every new record is checked against an"],
 ["signature systems","The Assistant Maker","REFERENCE: The Assistant Maker. The assistant maker is the JAH capability that builds a personal AI assistant "],
 ["signature systems","The All Database Merger","REFERENCE: The All Database Merger. The All Database Merger collects records you have gathered across a databa"]
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
