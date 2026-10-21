(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var SLUG="ways-to-use-signature-signature";
var CATS=["signature"];
var PREFIX="JAH-SIGUSE-S-";
var KIND="signature use";
/* rows: [category, title, description-head] — seeded from the archive */
var B=[
 ["signature","Applying the Maker Mark to a Spec Draft","HOW-TO: Applying the Maker Mark to a Spec Draft. The Signature procedure for marking a finished spec draft as "],
 ["signature","Stamping a Database Record","HOW-TO: Stamping a Database Record. How records earn their stamp in the JAH Databases network. The audit log i"],
 ["signature","Coding Lineage for a Mix","HOW-TO: Coding Lineage for a Mix. Lineage coding for program mixes and boundless blends. A mix that hides its "],
 ["signature","Sealing a Boundless Run","HOW-TO: Sealing a Boundless Run. Sealing a boundless generation run so it is reproducible and auditable. Repro"],
 ["signature","Marking a Wiki Article","HOW-TO: Marking a Wiki Article. Marking JAH Wiki articles as reviewed, sourced originals. Revisions get new ma"],
 ["signature","Marking a Dictionary Entry","HOW-TO: Marking a Dictionary Entry. Marking dictionary entries as reviewed Signature originals. A dictionary i"],
 ["signature","Marking a Leaks Dossier","HOW-TO: Marking a Leaks Dossier. Marking JAH-N dossiers filed by the governance itself. Classification marks p"],
 ["signature","Marking a Song Build","HOW-TO: Marking a Song Build. Marking Signature songs as finished, attributable works. The mark travels with t"],
 ["signature","Marking a Comic Script","HOW-TO: Marking a Comic Script. Marking Signature comic scripts before art begins. The script is the comic's b"],
 ["signature","Timestamping a Signature Creation","HOW-TO: Timestamping a Signature Creation. The Signature procedure for proving when a work existed. A timestam"],
 ["signature","Version-Stamping a Release","HOW-TO: Version-Stamping a Release. How Signature releases get their version stamps. Version numbers are compa"],
 ["signature","Edition-Numbering a Signature Print","HOW-TO: Edition-Numbering a Signature Print. Numbering Signature limited editions honestly. The edition's valu"]
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
