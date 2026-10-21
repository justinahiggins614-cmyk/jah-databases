(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var SLUG="science-proof-database-signature";
var CATS=["evidence","index"];
var PREFIX="JAH-SPROOF-S-";
var KIND="science proof";
/* rows: [category, title, description-head] — seeded from the archive */
var B=[
 ["evidence","The Photon, Simply","EVIDENCE: Light ejects electrons from metals. Signature summary: light arrives in lumps called photons, each c"],
 ["evidence","Waves of Matter","EVIDENCE: Single particles interfere. Signature summary: everything is a little bit wave. Electrons fired one "],
 ["evidence","No Aether","EVIDENCE: Light speed is direction-independent. Signature summary: physicists expected light to surf an invisi"],
 ["evidence","Seeing Molecules","EVIDENCE: Atoms are real. Signature summary: you can't see molecules, but you can watch them shove. Pollen gra"],
 ["evidence","Lumpy Charge","EVIDENCE: Charge is quantized. Signature summary: electricity doesn't flow as a smooth fluid — it comes in ide"],
 ["evidence","The Empty Atom","EVIDENCE: Atoms have nuclei. Signature summary: atoms are almost entirely empty. Fire particles at gold foil a"],
 ["evidence","The Expanding Universe","EVIDENCE: Galaxies recede. Signature summary: the galaxies are all moving away, faster the farther. Hubble's l"],
 ["evidence","Invisible Killers","EVIDENCE: Microbes cause disease. Signature summary: for most of history, disease was miasma and mystery. Then"],
 ["evidence","The Code of Life","EVIDENCE: DNA is a double helix. Signature summary: life's instruction book is a twisted ladder. Franklin's X-"],
 ["evidence","Drifting Continents","EVIDENCE: Plates move. Signature summary: the continents are rafts. Wegener saw the fit and was laughed at; fi"],
 ["evidence","The Healing Sky","EVIDENCE: Ozone hole and recovery. Signature summary: we broke the sky and then fixed it. CFCs released chlori"],
 ["evidence","Ripples in Spacetime","EVIDENCE: Gravitational waves detected. Signature summary: a century after Einstein predicted them, we heard t"]
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
