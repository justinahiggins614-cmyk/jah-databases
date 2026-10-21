(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var SLUG="form-database-signature";
var CATS=["signature"];
var PREFIX="JAH-FORMS-S-";
var KIND="form";
/* rows: [category, title, description-head] — seeded from the archive */
var B=[
 ["signature","Signature Maker Mark Registration","FORM: Signature Maker Mark Registration. Registers a maker's mark in the Signature system: who made it, what i"],
 ["signature","Spec Filing Intake Form","FORM: Spec Filing Intake Form. Intake for a JAH-SPEC draft filing: title, inventor, category, and the full dra"],
 ["signature","Boundless Generator Request","FORM: Boundless Generator Request. Requests a boundless generation run: subject, how many records, optional se"],
 ["signature","Database Record Submission","FORM: Database Record Submission. Submits one record to a database: which database, the title, the full body, "],
 ["signature","Signature Stamp Application","FORM: Signature Stamp Application. Applies a Signature stamp (e.g. SIGNATURE-1 VALID) to an archive item with "],
 ["signature","Lineage Coding Form","FORM: Lineage Coding Form. Records a lineage link between two archive records: parent, child, and the relation"],
 ["signature","Archive Merge Request","FORM: Archive Merge Request. Requests merging records from one database into another, with the reason on recor"],
 ["signature","AI Assistant Build Order","FORM: AI Assistant Build Order. Orders a personal AI assistant built on a database: name it, define its role, "],
 ["signature","Wiki Article Draft Intake","FORM: Wiki Article Draft Intake. Intake for a JAH Wiki article draft: title, subject, full body, and sources. "],
 ["signature","Leaks Dossier Intake","FORM: Leaks Dossier Intake. Intake for a JAH-N dossier: title, classification level, and the full dossier text"],
 ["signature","Dictionary Entry Submission","FORM: Dictionary Entry Submission. Submits a dictionary entry: headword, pronunciation, part of speech, full d"],
 ["signature","Patent Harvest Record","FORM: Patent Harvest Record. Records a harvested public patent: number, title, filing date, abstract. Harvest "]
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
