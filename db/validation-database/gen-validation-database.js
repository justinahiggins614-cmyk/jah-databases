(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var SLUG="validation-database";
var CATS=["methodology","validation report"];
var PREFIX="JAH-VALID-";
var KIND="validation report";
/* rows: [category, title, description-head] — seeded from the archive */
var B=[
 ["methodology","Validation Methodology and Standard","METHODOLOGY: the validation standard applied to every report in this database. VALIDATION METHODOLOGY (applies"],
 ["validation report","Validation Report: Form Database, Signature Form Database","VALIDATION REPORT (PASS): Form Database; Signature Form Database. Checks run at build time 2026-10-21; evidenc"],
 ["validation report","Validation Report: Template Database, Signature Template Database","VALIDATION REPORT (PASS): Template Database; Signature Template Database. Checks run at build time 2026-10-21;"],
 ["validation report","Validation Report: Writing Structure Database, Signature Writing Struc","VALIDATION REPORT (PASS): Writing Structure Database; Signature Writing Structure Database. Checks run at buil"],
 ["validation report","Validation Report: Ways to Use Signature Database","VALIDATION REPORT (PASS): Ways to Use Signature Database. Checks run at build time 2026-10-21; evidence publis"],
 ["validation report","Validation Report: Signature Ways to Use Signature Database","VALIDATION REPORT (PASS): Signature Ways to Use Signature Database. Checks run at build time 2026-10-21; evide"],
 ["validation report","Validation Report: General Knowledge Database","VALIDATION REPORT (PASS): General Knowledge Database. Checks run at build time 2026-10-21; evidence published "],
 ["validation report","Validation Report: Signature General Knowledge Database","VALIDATION REPORT (PASS): Signature General Knowledge Database. Checks run at build time 2026-10-21; evidence "],
 ["validation report","Validation Report: Math Proof Database","VALIDATION REPORT (PASS): Math Proof Database. Checks run at build time 2026-10-21; evidence published below; "],
 ["validation report","Validation Report: Signature Math Proof Database","VALIDATION REPORT (PASS): Signature Math Proof Database. Checks run at build time 2026-10-21; evidence publish"],
 ["validation report","Validation Report: Science Proof Database","VALIDATION REPORT (PASS): Science Proof Database. Checks run at build time 2026-10-21; evidence published belo"],
 ["validation report","Validation Report: Signature Science Proof Database","VALIDATION REPORT (PASS): Signature Science Proof Database. Checks run at build time 2026-10-21; evidence publ"]
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
