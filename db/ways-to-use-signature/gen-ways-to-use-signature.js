(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var SLUG="ways-to-use-signature";
var CATS=["craft","digital","legal","systems"];
var PREFIX="JAH-SIGUSE-";
var KIND="signature use";
/* rows: [category, title, description-head] — seeded from the archive */
var B=[
 ["craft","Maker's Mark on Handmade Goods","HOW-TO: Maker's Mark on Handmade Goods. How craftspeople have signed work for centuries: a consistent mark, ap"],
 ["digital","Digital Watermarking","HOW-TO: Digital Watermarking. Marking digital images and documents so copies trace back to the source. The unm"],
 ["digital","Code Signing Concept","HOW-TO: Code Signing Concept. How software publishers prove a download is really theirs and unmodified. Signin"],
 ["systems","Deterministic ID Coding","HOW-TO: Deterministic ID Coding. The JAH-SPEC-###### scheme: one counter, one pattern, no reuse — IDs that are"],
 ["systems","Signature Stamps on Specs","HOW-TO: Signature Stamps on Specs. How JAH spec drafts earn their SIGNATURE-1 VALID stamp: checked, stamped, d"],
 ["systems","Lineage Coding in Records","HOW-TO: Lineage Coding in Records. Recording what each record came from, so archives stay traceable instead of"],
 ["systems","Provenance Chains","HOW-TO: Provenance Chains. The practice of carrying source history with data, from archives to journalism to s"],
 ["digital","Hash-Based Integrity Marks","HOW-TO: Hash-Based Integrity Marks. Using cryptographic hashes as tamper-evident seals on files. A hash is a s"],
 ["craft","Branding vs Maker's Mark","HOW-TO: Branding vs Maker's Mark. The distinction between a commercial brand and a craftsman's personal mark —"],
 ["legal","Copyright Notice Practice","HOW-TO: Copyright Notice Practice. Standard copyright-notice practice. (General information, not legal advice."],
 ["systems","Timestamping Creations","HOW-TO: Timestamping Creations. Proving when a work existed — the foundation of 'I made this first' claims. A "],
 ["systems","Version Stamping","HOW-TO: Version Stamping. Numbering releases so everyone knows which version they have. Version numbers are pr"]
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
