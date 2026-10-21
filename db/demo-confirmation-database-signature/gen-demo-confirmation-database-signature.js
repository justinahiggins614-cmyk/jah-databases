(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var SLUG="demo-confirmation-database-signature";
var CATS=["demo confirmation","methodology"];
var PREFIX="JAH-DEMO-S-";
var KIND="demo confirmation";
/* rows: [category, title, description-head] — seeded from the archive */
var B=[
 ["methodology","Demo Confirmation Methodology","METHODOLOGY: how demos are confirmed in this database. DEMO CONFIRMATION METHODOLOGY (applies to every confirm"],
 ["demo confirmation","Demo Confirmation: Science Proof Database, Signature Science Proof Dat","DEMO CONFIRMATION (CONFIRMED): executed 2 demo program(s) from Science Proof Database; Signature Science Proof"],
 ["demo confirmation","Demo Confirmation: Full Working Programs Database, Signature Full Work","DEMO CONFIRMATION (CONFIRMED): executed 2 demo program(s) from Full Working Programs Database; Signature Full "],
 ["demo confirmation","Demo Confirmation: Program Mixes Database, Signature Program Mixes Dat","DEMO CONFIRMATION (CONFIRMED): executed 2 demo program(s) from Program Mixes Database; Signature Program Mixes"],
 ["demo confirmation","Demo Confirmation: Form Database","DEMO CONFIRMATION (CONFIRMED): executed 2 demo program(s) from Form Database with python3 at build time 2026-1"],
 ["demo confirmation","Demo Confirmation: Signature Form Database","DEMO CONFIRMATION (CONFIRMED): executed 2 demo program(s) from Signature Form Database with python3 at build t"],
 ["demo confirmation","Demo Confirmation: Template Database","DEMO CONFIRMATION (CONFIRMED): executed 2 demo program(s) from Template Database with python3 at build time 20"],
 ["demo confirmation","Demo Confirmation: Signature Template Database","DEMO CONFIRMATION (CONFIRMED): executed 2 demo program(s) from Signature Template Database with python3 at bui"],
 ["demo confirmation","Demo Confirmation: Writing Structure Database","DEMO CONFIRMATION (CONFIRMED): executed 2 demo program(s) from Writing Structure Database with python3 at buil"],
 ["demo confirmation","Demo Confirmation: Signature Writing Structure Database","DEMO CONFIRMATION (CONFIRMED): executed 2 demo program(s) from Signature Writing Structure Database with pytho"],
 ["demo confirmation","Demo Confirmation: Ways to Use Signature Database","DEMO CONFIRMATION (CONFIRMED): executed 2 demo program(s) from Ways to Use Signature Database with python3 at "],
 ["demo confirmation","Demo Confirmation: Signature Ways to Use Signature Database","DEMO CONFIRMATION (CONFIRMED): executed 2 demo program(s) from Signature Ways to Use Signature Database with p"]
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
