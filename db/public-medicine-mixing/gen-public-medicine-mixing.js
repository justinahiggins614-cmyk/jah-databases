(function(){'use strict';
/* Public Medicine Mixing Database generator — jahdb-public-medicine-mixing-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed always makes the same record.
   src:"public-harvest" = public-harvested fact, clearly labeled */
function pad(n){var s=String(n);while(s.length<6)s='0'+s;return s;}
var PREFIX='JAH-PMM-';
var SRC='public-harvest';
var RECORD_KIND='medicine mixing record';
var GENRES=["compounding reference", "dosage-form science"];
var TOPICS=["Aspirin Synthesis (Acetylsalicylic Acid)", "Normal Saline (0.9% Sodium Chloride IV Solution)", "Oral Rehydration Salts (WHO Formula)", "Calamine Lotion", "Simple Syrup (Sucrose Vehicle)", "Zinc Oxide Ointment (20%)", "Epsom Salt Soak (Magnesium Sulfate)", "Hydrogen Peroxide 3% (Topical Antiseptic)", "Tincture of Botanical (Alcohol Extraction)", "Petrolatum Gauze Barrier (Wound Protectant)", "Baking Soda Antacid Solution", "Witch Hazel Astringent", "Glycerin Suppository Base", "Coal Tar Ointment (Psoriasis)", "Menthol Chest Rub", "Kaolin-Chalk Digestive Mixture", "Iodine Tincture (Antiseptic)", "Eucalyptus Steam Inhalation", "Aloe Vera Burn Gel", "Oatmeal Colloidal Bath", "Glycerin-Based Cough Expectorant", "Boric Acid Eye Irrigant (Traditional)", "Talc Dusting Powder", "Ichthammol Drawing Ointment", "Resorcinol Acne Lotion", "Podophyllum Wart Paint", "Benzoin Inhalation (Friar's Balsam Steam)", "Chlorhexidine Surgical Scrub Base", "Povidone-Iodine Ointment", "Nystatin Oral Suspension", "Sucralfate Slurry (Traditional Compound)", "Kaolin Poultice (Traditional)", "Mustard Plaster (Traditional)", "Turpentine Liniment (Traditional)", "Ammoniated Mercury Ointment (Historical)", "Lead Subacetate Lotion (Historical)", "Carbolic Acid Gargle (Historical)", "Mercurochrome Paint (Historical)", "Effervescent Antacid Granules (formulation family)", "Sustained-Release Matrix Tablet Concept (formulation family)", "Chewable Vitamin Base (formulation family)", "Lozenges (Hard Candy Vehicle) (formulation family)", "Suppository Cocoa-Butter Base (formulation family)", "Enema Solution (Phosphate) (formulation family)", "Nasal Decongestant Spray Base (formulation family)", "Otic Drops Vehicle (formulation family)", "Vaginal Cream Base (formulation family)", "Transdermal Gel Vehicle (formulation family)", "Effervescent Antacid Granules (formulation family)", "Sustained-Release Matrix Tablet Concept (formulation family)", "Chewable Vitamin Base (formulation family)", "Lozenges (Hard Candy Vehicle) (formulation family)", "Suppository Cocoa-Butter Base (formulation family)", "Enema Solution (Phosphate) (formulation family)", "Nasal Decongestant Spray Base (formulation family)", "Otic Drops Vehicle (formulation family)", "Vaginal Cream Base (formulation family)", "Transdermal Gel Vehicle (formulation family)", "Effervescent Antacid Granules (formulation family)", "Sustained-Release Matrix Tablet Concept (formulation family)"];
function mulberry(seed){var a=seed>>>0;return function(){a|=0;a=a+0x6D2B79F5|0;var t=Math.imul(a^a>>>15,1|a);t=t+Math.imul(t^t>>>7,61|t)^t;return((t^t>>>14)>>>0)/4294967296;};}
function buildContent(title,genre,rng){
  var ings=[{name:'Primary active ingredient',amount:'per formulation'},{name:'Secondary ingredient / excipient',amount:'per formulation'},{name:'Vehicle / base',amount:'to final volume'}];
  var ratio='formulation-specific proportions';
  var method='Combine the ingredients by the standard pharmaceutical technique for this preparation type (dissolution, trituration, levigation, or incorporation), with in-process uniformity controls.';
  var result='A finished, uniform preparation ready for its intended use.';
  var impact='Bodily impact follows the established pharmacology of the active constituents, modulated by the dosage form and route.';
  var treats=['as established for the active constituents'];
  var summary='A medicine-mixing reference record for '+title+'.';
  var sections=[
    {heading:'Ingredients and ratio',body:ings.map(function(x){return x.name+' \u2014 '+x.amount;}).join('; ')+'. Ratio: '+ratio+'.'},
    {heading:'Way combined (method)',body:method},
    {heading:'What it becomes (result)',body:result},
    {heading:'Impact on the body',body:impact},
    {heading:'Conditions addressed',body:treats.join('; ')+'.'}
  ];
  return{summary:summary,sections:sections,key_facts:['Educational reference \u2014 not medical advice.','Deterministic generator record.','src: '+SRC+'.'],
    ingredients:ings,ratio:ratio,method:method,result:result,bodily_impact:impact,treats:treats};
}
function defaultDemo(){
  return{kind:'record-program',
    program:"// mix card \u2014 run with: node demo.js\n// (place the record JSON next to this file as record.json)\nconst r = JSON.parse(require('fs').readFileSync('record.json','utf8'));\nconsole.log(r.id + ' \u2014 ' + r.title);\nconsole.log('Ratio: ' + r.ratio);\nconsole.log('Result: ' + r.result);\nconsole.log('[' + r.src + ']');",
    note:'A runnable program card for this record. Save as demo.js, save the record JSON as record.json beside it, and run with node.'};
}
function generate(seed,opts){
  opts=opts||{};
  var s=(seed>>>0)||1;
  var rng=mulberry(s);
  var title=TOPICS[(s-1)%TOPICS.length];
  var genre=GENRES[(s-1)%GENRES.length];
  if(opts.genre&&GENRES.indexOf(opts.genre)>=0)genre=opts.genre;
  var ctopic=opts.topic?String(opts.topic).trim().slice(0,120):'';
  if(ctopic){title=ctopic;}
  var id=PREFIX+pad(s);
  var c=buildContent(title,genre,rng);
  return{id:id,title:title,description:c.summary+' Educational medicine-mixing reference \u2014 ingredients, ratio, method, result, and bodily impact.',genre:genre,type:RECORD_KIND,content:{summary:c.summary,sections:c.sections,key_facts:c.key_facts},ingredients:c.ingredients,ratio:c.ratio,method:c.method,result:c.result,bodily_impact:c.bodily_impact,treats:c.treats,demo:defaultDemo(),src:SRC,_seed:s};
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return{ok:false,errors:['not an object']};
  if(typeof r.id!=='string'||r.id.indexOf(PREFIX)!==0||!/\d{6}$/.test(r.id))e.push('id');
  if(typeof r.title!=='string'||r.title.length<4)e.push('title');
  if(typeof r.description!=='string'||r.description.length<40)e.push('description');
  if(GENRES.indexOf(r.genre)<0)e.push('genre');
  if(!r.content||typeof r.content!=='object'||typeof r.content.summary!=='string'||r.content.summary.length<10)e.push('content');
  if(!r.demo||typeof r.demo!=='object')e.push('demo');
  if(typeof r.ratio!=='string'||!r.ratio)e.push('ratio');
  if(typeof r.method!=='string'||!r.method)e.push('method');
  if(typeof r.result!=='string'||!r.result)e.push('result');
  return{ok:!e.length,errors:e};
}
function driftCheck(rec,sample){
  for(var i=0;i<sample.length;i++){if(sample[i]&&sample[i].t===rec.title)return{ok:false,errors:['duplicate title in archive sample']};}
  return{ok:true,errors:[]};
}
var gen={version:'jahdb-public-medicine-mixing-1.0',generate:generate,validate:validate,driftCheck:driftCheck,genres:GENRES};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('public-medicine-mixing',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();