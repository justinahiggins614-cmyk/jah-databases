(function(){'use strict';
/* Signature Fast Food Database generator — jahdb-signature-fast-food-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed always makes the same record.
   src:"signature" */
function pad(n){var s=String(n);while(s.length<6)s='0'+s;return s;}
var PREFIX='JAH-SFF-';
var SRC='signature';
var RECORD_KIND='fast food concept';
var GENRES=["Apex Breakfast", "Boundless Tacos", "Duo Bowl", "Golden Lattice", "JAH Fry Co.", "Mosaic Pizza", "Orbit Wings", "Prime Stack"];
var TOPICS=["Prime Stack Classic", "Dual-Pole Melt", "Mosaic Fries", "Golden Lattice Shake", "Boundless Baja Taco", "Junction Quesadilla", "A-Series Nachos", "Prime Coordinate Fries", "2-6-2 Onion Blossom", "Mosaic Sweet Potato Fries", "Apex Hot Wings", "Zero-G Boneless", "Orbital Tenders", "Duo Chicken Bowl", "Duo Salmon Bowl", "Lattice Fried Chicken", "Lattice Sandwich", "Mosaic Pepperoni", "Boundless Veggie", "Apex Breakfast Burrito", "2-6-2 Pancake Stack", "Combo Crunch Wrap", "Infinity Onion Rings", "Black Hole Brownie Blast", "Signature Sliders Trio", "Teriyaki Orbit Bowl", "Cajun Lattice Fries", "Pepperoni Junction Calzone", "Bacon Apex Burrito", "Honey Sriracha Tenders", "Mango Habanero Wings", "Duo Shrimp Bowl", "Lattice Chicken Tenders", "White Mosaic Pizza", "Chorizo 2-6-2 Stack", "Prime Stack Double", "Junction Tostada", "Apex Garlic Parm Wings", "Duo Steak Bowl", "Lattice Biscuit Sandwich", "Mosaic Margherita", "Apex Chilaquiles", "Prime Stack Patty Melt", "Boundless Birria Ramen", "Orbit Cauliflower Wings", "Duo Tofu Bowl", "Lattice Chicken Nuggets", "Mosaic BBQ Chicken Pizza", "Apex Huevos Rancheros", "Smoky Prime Fries", "Prime Stack Chili", "Boundless Fish Tacos", "Junction Burrito Bowl", "Truffle Parm Fries", "Sweet Heat Tots", "Lemon Pepper Wings", "Teriyaki Tenders", "Duo Pork Bowl", "Lattice Spicy Sandwich", "Mosaic Supreme"];
function mulberry(seed){var a=seed>>>0;return function(){a|=0;a=a+0x6D2B79F5|0;var t=Math.imul(a^a>>>15,1|a);t=t+Math.imul(t^t>>>7,61|t)^t;return((t^t>>>14)>>>0)/4294967296;};}
function buildContent(title,genre){
  var summary='A fast food concept record for '+title+' ('+genre+'). Full ingredients, cooking method, and details in the archive.';
  var sections=[
    {heading:'Ingredients and amounts',body:'See the archived record '+title+' for the complete ingredient list.'},
    {heading:'Cooking method (step-by-step)',body:'Full method in the archived record.'},
    {heading:'Details',body:'Full details in the archived record.'}
  ];
  return{summary:summary,sections:sections,key_facts:['Deterministic generator record.','src: '+SRC+'.'],
    ingredients:[{name:'See archived record',amount:'full list'}],
    cook_method:'see archived record',nutrition:'see archived record'};
}
function defaultDemo(){
  return{kind:'record-program',
    program:"// record viewer \u2014 run with: node demo.js\nconst r = JSON.parse(require('fs').readFileSync('record.json','utf8'));\nconsole.log(r.id+' \u2014 '+r.title);\nconsole.log(r.description);\nconsole.log('['+r.src+']');",
    note:'Prints the record. Run: node demo.js'};
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
  return{id:id,title:title,description:c.summary,genre:genre,type:RECORD_KIND,
    content:{summary:c.summary,sections:c.sections,key_facts:c.key_facts},
    ingredients:c.ingredients,cook_method:c.cook_method,nutrition:c.nutrition,
    demo:defaultDemo(),src:SRC,_seed:s};
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
  if(typeof r.cook_method!=='string'||!r.cook_method)e.push('cook_method');
  return{ok:!e.length,errors:e};
}
function driftCheck(rec,sample){
  for(var i=0;i<sample.length;i++){if(sample[i]&&sample[i].t===rec.title)return{ok:false,errors:['duplicate title in archive sample']};}
  return{ok:true,errors:[]};
}
var gen={version:'jahdb-signature-fast-food-1.0',generate:generate,validate:validate,driftCheck:driftCheck,genres:GENRES};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('signature-fast-food',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();