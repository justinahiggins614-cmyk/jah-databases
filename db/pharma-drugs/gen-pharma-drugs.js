/* ✳ JAH Drug Database generator. Property of Justin Addam Higgins (JAH).
   Deterministic (seeded) drug record generator: jahdb-pharma-drugs-1.0.
   All names are invented for this fictional catalog. */
(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(s,r){return r[(s()*r.length)|0];}
function ri(s,a,b){return a+((s()*(b-a+1))|0);}
function pad(n){return String(n).padStart(6,'0');}

var CATS=['antibiotic','analgesic','antihypertensive','antidepressant','vaccine','generic'];
var FORMS=['tablet','capsule','injection','syrup'];

var G1=['cor','ta','vin','dex','mol','zep','fre','glan','mir','sal','brex','tol','nov','ax','quim'];
var G2=['ta','vin','dor','cil','mex','pral','fen','gor','sil','trex'];
var G3=['ine','azole','mycin','pril','statin','olol','pam','vir'];
var BRAND_CORE=['Zentiva','Bralex','Novacur','Medalor','Curaphen','Virexal','Sanatrol','Lumidex','Theranox','Probion'];

var INDIC={
antibiotic:['bacterial pneumonia','urinary tract infection','strep pharyngitis','cellulitis','sinusitis','bronchitis','skin infection','ear infection'],
analgesic:['chronic back pain','osteoarthritis pain','migraine','postoperative pain','neuropathic pain','dental pain','muscle strain','tension headache'],
antihypertensive:['essential hypertension','heart failure','post-MI care','diabetic nephropathy','atrial fibrillation rate control','chronic kidney disease','angina','stroke prevention'],
antidepressant:['major depressive disorder','generalized anxiety','panic disorder','OCD','PTSD','social anxiety','treatment-resistant depression','seasonal affective disorder'],
vaccine:['influenza prevention','pneumococcal disease','hepatitis B','tetanus prophylaxis','measles-mumps-rubella','HPV prevention','COVID-19 booster','shingles prevention'],
generic:['hypertension','type 2 diabetes','high cholesterol','asthma','allergic rhinitis','GERD','hypothyroidism','chronic pain']
};
var INTERACT=['ibuprofen','warfarin','alcohol','grapefruit juice','caffeine','acetaminophen','antacids','St. John\'s wort','digoxin','metformin','lisinopril','sertraline'];

function uniqPick(rnd,arr,n){
  var out=[],used={},tries=0;
  while(out.length<n&&tries<60){tries++;var v=pick(rnd,arr);if(!used[v]){used[v]=1;out.push(v);}}
  return out;
}
function generate(seed,opts,rnd){
  rnd=rnd||prng(seed);
  var cat=(opts&&opts.category&&CATS.indexOf(opts.category)>=0)?opts.category:pick(rnd,CATS);
  var generic=(pick(rnd,G1)+pick(rnd,G2)+pick(rnd,G3)).toLowerCase();
  var nb=ri(rnd,1,3), brands=uniqPick(rnd,BRAND_CORE.map(function(b){return b+generic.slice(0,3);}),nb);
  if(!brands.length)brands=[pick(rnd,BRAND_CORE)];
  var indications=uniqPick(rnd,INDIC[cat],ri(rnd,2,4));
  var interactions=uniqPick(rnd,INTERACT,ri(rnd,1,3));
  return {
    id:'JAH-DRUG-'+pad(seed),
    drug_id:'JAH-DRUG-'+pad(seed),
    generic_name:generic,
    brand_names:brands,
    drug_class:cat,
    indications:indications,
    dosage_form:pick(rnd,FORMS),
    fda_approved:rnd()<0.85,
    interactions:interactions
  };
}
function validate(r){
  var e=[];
  if(typeof r.id!=='string'||!/^JAH-DRUG-\d{6}$/.test(r.id))e.push('id');
  if(typeof r.drug_id!=='string'||r.drug_id!==r.id)e.push('drug_id');
  if(typeof r.generic_name!=='string'||!r.generic_name.length)e.push('generic_name');
  if(!Array.isArray(r.brand_names)||r.brand_names.length<1||r.brand_names.length>3||r.brand_names.some(function(b){return typeof b!=='string'||!b.length;}))e.push('brand_names');
  if(CATS.indexOf(r.drug_class)<0)e.push('drug_class');
  if(!Array.isArray(r.indications)||r.indications.length<2||r.indications.length>4||r.indications.some(function(x){return typeof x!=='string'||!x.length;}))e.push('indications');
  if(FORMS.indexOf(r.dosage_form)<0)e.push('dosage_form');
  if(typeof r.fda_approved!=='boolean')e.push('fda_approved');
  if(!Array.isArray(r.interactions)||r.interactions.length<1||r.interactions.length>3||r.interactions.some(function(x){return typeof x!=='string'||!x.length;}))e.push('interactions');
  return {ok:!e.length,errors:e};
}
var gen={version:'jahdb-pharma-drugs-1.0',generate:generate,validate:validate};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('pharma-drugs',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
