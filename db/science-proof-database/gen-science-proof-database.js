(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var SLUG="science-proof-database";
var CATS=["evidence","index"];
var PREFIX="JAH-SPROOF-";
var KIND="science proof";
/* rows: [category, title, description-head] — seeded from the archive */
var B=[
 ["evidence","Photoelectric Effect","EVIDENCE: Light ejects electrons from metals. When light shines on a metal, electrons can be ejected — but onl"],
 ["evidence","Double-Slit Experiment","EVIDENCE: Single particles interfere with themselves. Firing electrons one at a time through two slits still b"],
 ["evidence","Constancy of the Speed of Light","EVIDENCE: Light speed is the same in all directions. The Michelson-Morley experiment (1887) tried to detect Ea"],
 ["evidence","Brownian Motion and Atoms","EVIDENCE: Atoms are real: pollen jitters. Robert Brown (1827) saw pollen grains jiggle randomly in water. Eins"],
 ["evidence","Oil Drop Experiment","EVIDENCE: Electric charge comes in lumps. Millikan (1909-1913) sprayed oil droplets between charged plates and"],
 ["evidence","Rutherford Gold Foil","EVIDENCE: Atoms have tiny dense nuclei. Rutherford's team (1909) fired alpha particles at gold foil. Most pass"],
 ["evidence","Hubble Expansion","EVIDENCE: The universe is expanding. Vesto Slipher measured galaxies' redshifts; Edwin Hubble (1929) showed re"],
 ["evidence","Germ Theory of Disease","EVIDENCE: Microbes cause disease. Semmelweis (1847) showed handwashing cut childbed fever deaths; Pasteur prov"],
 ["evidence","DNA Double Helix","EVIDENCE: DNA is a double helix. Rosalind Franklin's X-ray diffraction Photo 51 (1952) showed DNA's helical X "],
 ["evidence","Plate Tectonics","EVIDENCE: Continents drift on moving plates. Wegener proposed continental drift (1912) with little mechanism a"],
 ["evidence","Ozone Hole Discovery","EVIDENCE: CFCs destroy stratospheric ozone. Farman's team (1985) found Antarctic spring ozone collapsing — the"],
 ["evidence","Gravitational Waves","EVIDENCE: Ripples in spacetime detected. Einstein predicted gravitational waves in 1916. LIGO (2015) detected "]
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
