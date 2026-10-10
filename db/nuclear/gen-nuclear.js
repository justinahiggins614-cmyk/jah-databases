(function(){'use strict';
/* JAH Nuclear Science Database generator — jahdb-nuclear-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed always makes the same record. src:"online" = isotope facts
   verified against published nuclear data; src:"signature" = Signature-authored
   decay-arithmetic study (exact half-life math, clearly labeled). */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
function ri(s,a,b){return a+((s()*(b-a+1))|0);}
var CATS=['medical','power','dating','industrial','research'];
var PREFIX='JAH-NUC-';
/* [symbol, name, half-life, decay mode, application, categories[], daughter (researched only)] */
var ISO=[
 ['H-3','tritium','12.32 years','beta minus','biochemical tracer; self-powered emergency lighting',['research','industrial']],
 ['C-11','carbon-11','20.33 minutes','positron (beta plus)','positron emission tomography (PET) biomedical imaging',['medical']],
 ['C-14','carbon-14','5,730 years','beta minus','radiocarbon dating of artifacts up to about 50,000 years old',['dating','research'],'nitrogen-14'],
 ['Na-24','sodium-24','14.951 hours','beta minus, gamma','cardiovascular tracer; industrial pipeline leak testing',['medical','industrial']],
 ['P-32','phosphorus-32','14.26 days','beta minus','biochemical tracer',['research','medical']],
 ['K-40','potassium-40','1.248 billion years','beta minus, electron capture','potassium-argon dating of rocks',['dating']],
 ['Fe-59','iron-59','44.495 days','beta minus, gamma','red blood cell lifetime tracer',['medical','research']],
 ['Co-60','cobalt-60','5.2713 years','beta minus then gamma (1.17 and 1.33 MeV)','radiation therapy for cancer; industrial sterilization',['medical','industrial'],'nickel-60'],
 ['Tc-99m','technetium-99m','6.006 hours','isomeric transition (gamma)','biomedical imaging of brain, lung, heart, and bone',['medical']],
 ['I-131','iodine-131','8.0207 days','beta minus','thyroid studies and thyroid treatment',['medical']],
 ['I-123','iodine-123','13.2 hours','electron capture, gamma','thyroid imaging',['medical']],
 ['F-18','fluorine-18','109.7 minutes','positron (beta plus)','PET scans',['medical']],
 ['Tl-201','thallium-201','73 hours','electron capture','cardiac stress tests and heart imaging',['medical']],
 ['Ra-226','radium-226','1,600 years','alpha','historical radiation therapy; calibration sources',['industrial','research']],
 ['U-238','uranium-238','4.468 billion years','alpha','dating of rocks and Earth\u2019s crust; 99.3% of natural uranium and non-fissile',['dating','power'],'lead-206'],
 ['U-235','uranium-235','704 million years','alpha','fissile reactor fuel; about 0.7% of natural uranium',['power']],
 ['Pu-239','plutonium-239','24,100 years','alpha','reactor fuel; radioisotope power systems',['power','research']],
 ['Am-241','americium-241','432.2 years','alpha','ionization-type smoke detectors',['industrial']],
 ['Cs-137','cesium-137','30.17 years','beta minus (to barium-137m)','industrial gauges; fission-product studies',['industrial','research'],'barium-137'],
 ['Rn-222','radon-222','3.82 days','alpha','natural background monitoring; lung-dose studies',['research']]
];
var SHIELD={
 alpha:'Alpha particles are stopped by skin or a sheet of paper, but are hazardous if inhaled or ingested.',
 beta:'Beta particles are stopped by a few millimeters of plastic or aluminum.',
 gamma:'Gamma rays need dense shielding such as lead or thick concrete.',
 positron:'Positrons annihilate with electrons, producing two 511 keV gamma photons used in PET imaging.',
 electron:'Electron-capture decay emits characteristic X-rays and is shielded like low-energy gamma.'
};
function shieldFor(mode){
 if(/alpha/.test(mode))return SHIELD.alpha;
 if(/positron/.test(mode))return SHIELD.positron;
 if(/electron capture/.test(mode))return SHIELD.electron;
 if(/gamma/.test(mode))return SHIELD.gamma;
 return SHIELD.beta;
}
var SERIES='Uranium-238 decays through 14 steps — eight alpha and six beta decays — to stable lead-206.';
var LAW='Activity follows first-order kinetics: A = A₀·e^(−λt), with λ = ln 2 / half-life.';
function build(rnd,cat){
 var online=rnd()<0.62;
 var iso=pick(ISO,rnd);
 var cats=iso[5];
 var useCat=cats.indexOf(cat)>=0?cat:pick(cats,rnd);
 var shield=shieldFor(iso[3]);
 var title,desc,spec;
 if(online){
  title=cap(iso[1])+' ('+iso[0]+') — '+iso[4].split(';')[0];
  desc=cap(iso[1])+' ('+iso[0]+') has a half-life of '+iso[2]+' and decays by '+iso[3]+'. '+
   'Its established application: '+iso[4]+'. '+shield+
   (iso[6]?' It decays to '+iso[6]+'.':'')+' '+LAW;
  spec={isotope:iso[1],symbol:iso[0],half_life:iso[2],decay_mode:iso[3],application:iso[4],
   shielding_note:shield,decay_series_note:SERIES,decay_law:LAW};
  if(iso[6])spec.daughter_nuclide=iso[6];
 }else{
  var n=ri(rnd,1,6);
  var frac=Math.pow(0.5,n);
  var pct=(frac*100);
  var pctStr=pct>=1?pct.toFixed(2):pct.toPrecision(3);
  title='Signature Study — '+iso[0]+' after '+n+' half-lives';
  desc='This is a Signature-authored decay-arithmetic study. Starting from any amount of '+iso[1]+' ('+iso[0]+', half-life '+iso[2]+'), '+
   'after '+n+' half-life'+(n>1?'s':'')+' exactly '+(1/frac)+'⁻¹ = '+pctStr+'% remains, by the first-order law A = A₀·e^(−λt). '+
   'It decays by '+iso[3]+'; application: '+iso[4]+'. '+shield;
  spec={isotope:iso[1],symbol:iso[0],half_life:iso[2],decay_mode:iso[3],
   study:{half_lives_elapsed:n,remaining_fraction:'1/'+(1/frac),remaining_percent:pctStr+'%'},
   application:iso[4],shielding_note:shield,decay_law:LAW};
 }
 return {title:title,description:desc,src:online?'online':'signature',spec:spec,cat:useCat};
}
function generate(seed,opts,rnd){
 opts=opts||{};rnd=rnd||prng(seed);
 var want=(opts.category&&CATS.indexOf(opts.category)>=0)?opts.category:null;
 var b;
 if(want){ /* find a record whose isotope serves the requested category */
  for(var t=0;t<40;t++){var c2=build(rnd,want);if(c2.cat===want){b=c2;break;}}
  if(!b)b=build(rnd,want);
 }else{b=build(rnd,pick(CATS,rnd));}
 var id=PREFIX+String(seed).padStart(6,'0');
 return {id:id,title:b.title,description:b.description,category:b.cat,src:b.src,spec:b.spec,_seed:seed};
}
function cap(x){return x.charAt(0).toUpperCase()+x.slice(1);}
function isoBySymbol(sym){for(var i=0;i<ISO.length;i++)if(ISO[i][0]===sym)return ISO[i];return null;}
function validate(r){
 var e=[];
 if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
 if(!/^JAH-NUC-\d{6}$/.test(r.id||''))e.push('id');
 if(typeof r.title!=='string'||r.title.length<10)e.push('title');
 if(typeof r.description!=='string'||r.description.length<80)e.push('description');
 if(CATS.indexOf(r.category)<0)e.push('category');
 if(r.src!=='online'&&r.src!=='signature')e.push('src');
 var s=r.spec;
 if(!s||typeof s!=='object')e.push('spec');
 else{
  var iso=isoBySymbol(s.symbol);
  if(!iso)e.push('spec.symbol');
  else{
   if(s.half_life!==iso[2])e.push('spec.half_life');
   if(s.decay_mode!==iso[3])e.push('spec.decay_mode');
   if(iso[5].indexOf(r.category)<0)e.push('spec.category_match');
  }
  if(typeof s.application!=='string'||!s.application)e.push('spec.application');
  if(typeof s.shielding_note!=='string'||!s.shielding_note)e.push('spec.shielding');
  if(r.src==='signature'){
   if(!s.study||typeof s.study.half_lives_elapsed!=='number')e.push('spec.study');
   else{
    var expect=Math.pow(0.5,s.study.half_lives_elapsed)*100;
    var got=parseFloat(s.study.remaining_percent);
    if(Math.abs(got-expect)>Math.max(0.01,expect*0.01))e.push('spec.study_math');
   }
  }
 }
 return {ok:!e.length,errors:e};
}
var gen={version:'jahdb-nuclear-1.0',generate:generate,validate:validate};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('nuclear',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
