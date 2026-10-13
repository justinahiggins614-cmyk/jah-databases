(function(){'use strict';
/* Public Goat Milk Soap Formulas Database generator — jahdb-public-goat-milk-soap-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed always makes the same record.
   src:"public-harvest" */
function pad(n){var s=String(n);while(s.length<6)s='0'+s;return s;}
var PREFIX='JAH-GMS-';
var SRC='public-harvest';
var RECORD_KIND='goat milk soap formula';
var GENRES=["cold process", "hot process", "liquid soap", "melt-and-pour", "rebatch", "salt bar", "specialty", "whipped soap"];
var TOPICS=["Classic Goat Milk Castile Soap", "Goat Milk Honey Oatmeal Soap", "Goat Milk Lavender Soap", "Goat Milk Shea Butter Soap", "Goat Milk Coconut Cleansing Bar", "Goat Milk Cocoa Butter Soap", "Goat Milk Charcoal Detox Soap", "Goat Milk Rosehip Soap", "Goat Milk Calendula Soap", "Goat Milk Tea Tree Soap", "Goat Milk Unscented Sensitive Soap", "Goat Milk Avocado Soap", "Goat Milk Almond Oil Soap", "Goat Milk Coffee Exfoliant Soap", "Goat Milk Turmeric Soap", "Goat Milk Hot Process Basic Soap", "Goat Milk Hot Process Honey Soap", "Goat Milk Hot Process Oatmeal Soap", "Goat Milk Hot Process Shea Soap", "Goat Milk Hot Process Lavender EO Soap", "Goat Milk Hot Process Peppermint Soap", "Goat Milk Hot Process Citrus Soap", "Goat Milk Hot Process Eucalyptus Soap", "Goat Milk Hot Process Clay Soap", "Goat Milk Hot Process Double Butter Soap", "Goat Milk Melt-and-Pour Honey Swirl Soap", "Goat Milk Melt-and-Pour Lavender Buds Soap", "Goat Milk Melt-and-Pour Oatmeal Honey Soap", "Goat Milk Melt-and-Pour Rose Petal Soap", "Goat Milk Melt-and-Pour Charcoal Stripe Soap", "Goat Milk Melt-and-Pour Coffee Scrub Soap", "Goat Milk Melt-and-Pour Citrus Zest Soap", "Goat Milk Melt-and-Pour Calendula Soap", "Goat Milk Melt-and-Pour Shea Enriched Soap", "Goat Milk Melt-and-Pour Unscented Baby Soap", "Goat Milk Liquid Hand Soap (KOH)", "Goat Milk Liquid Body Wash", "Goat Milk Liquid Shampoo", "Goat Milk Foaming Hand Soap (Diluted Castile)", "Goat Milk Liquid Castile Soap", "Goat Milk Liquid Honey Wash", "Goat Milk Liquid Oatmeal Wash", "Goat Milk Liquid Lavender Wash", "Goat Milk Rebatch Lavender Soap", "Goat Milk Rebatch Honey Oat Soap", "Goat Milk Rebatch Charcoal Soap", "Goat Milk Rebatch Rose Soap", "Goat Milk Rebatch Unscented Soap", "Goat Milk Whipped Sugar Scrub Soap", "Goat Milk Whipped Shaving Soap", "Goat Milk Whipped Body Butter Soap", "Goat Milk Whipped Coffee Scrub Soap", "Goat Milk Sea Salt Spa Bar", "Goat Milk Himalayan Salt Bar", "Goat Milk Clay Facial Bar", "Goat Milk Acne-Fighting Bar", "Goat Milk Eczema Relief Bar", "Goat Milk Shampoo Bar (Solid)", "Goat Milk Pet Shampoo Bar", "Goat Milk Gardener\\'s Scrub Bar"];
function mulberry(seed){var a=seed>>>0;return function(){a|=0;a=a+0x6D2B79F5|0;var t=Math.imul(a^a>>>15,1|a);t=t+Math.imul(t^t>>>7,61|t)^t;return((t^t>>>14)>>>0)/4294967296;};}
function buildContent(title,genre){
  var summary='A goat milk soap formula record for '+title+' ('+genre+'). Full formula below in the archive.';
  var sections=[
    {heading:'Ingredients and ratio',body:'See the archived record '+title+' for the complete measured ingredient list and lye-to-oil ratio.'},
    {heading:'Step-by-step method',body:'Full method in the archived record. Lye safety always: goggles, gloves, ventilation; lye into liquid, never reverse.'},
    {heading:'What it makes (result)',body:'Finished goat milk soap bars per the archived formula.'},
    {heading:'Skin benefits',body:'Goat milk brings lactic acid, vitamins A/D/E, and creamy fats; see the archived record for this formula\u2019s benefits.'},
    {heading:'Variations',body:'See the archived record for tested variations.'}
  ];
  return{summary:summary,sections:sections,key_facts:['Educational reference \u2014 not medical advice.','Deterministic generator record.','src: '+SRC+'.'],
    ingredients:[{name:'See archived record',amount:'full list'}],ratio:'see archived record',
    method:'see archived record',result:'see archived record',bodily_impact:'see archived record',treats:['see archived record']};
}
function defaultDemo(){
  return{kind:'record-program',
    program:"// batch scaler \u2014 run with: node demo.js [factor]\nconst r = JSON.parse(require('fs').readFileSync('record.json','utf8'));\nvar factor=parseFloat(process.argv[2]||'1');\nconsole.log(r.id+' \u2014 '+r.title+' (x'+factor+')');\nr.ingredients.forEach(function(x){var m=String(x.amount).match(/^([0-9.]+)\\s*oz/);console.log(' - '+x.name+': '+(m?(parseFloat(m[1])*factor).toFixed(1)+' oz':x.amount));});\nconsole.log('['+r.src+']');",
    note:'Scales every ounce-measured ingredient. Run: node demo.js 2. Lye safety rules always apply.'};
}
function generate(seed,opts){
  opts=opts||{};
  var s=(seed>>>0)||1;
  var title=TOPICS[(s-1)%TOPICS.length];
  var genre=GENRES[(s-1)%GENRES.length];
  if(opts.genre&&GENRES.indexOf(opts.genre)>=0)genre=opts.genre;
  var ctopic=opts.topic?String(opts.topic).trim().slice(0,120):'';
  if(ctopic){title=ctopic;}
  var id=PREFIX+pad(s);
  var c=buildContent(title,genre);
  return{id:id,title:title,description:c.summary+' Full goat milk soap formula \u2014 ingredients, ratio, method, result, skin benefits, variations.',genre:genre,type:RECORD_KIND,content:{summary:c.summary,sections:c.sections,key_facts:c.key_facts},ingredients:c.ingredients,ratio:c.ratio,method:c.method,result:c.result,bodily_impact:c.bodily_impact,treats:c.treats,demo:defaultDemo(),src:SRC,_seed:s};
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
var gen={version:'jahdb-public-goat-milk-soap-1.0',generate:generate,validate:validate,driftCheck:driftCheck,genres:GENRES};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('public-goat-milk-soap',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();