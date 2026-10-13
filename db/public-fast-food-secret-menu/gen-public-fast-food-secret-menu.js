(function(){'use strict';
/* Public Fast Food Secret Menu Database generator — jahdb-public-fast-food-secret-menu-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed always makes the same record.
   src:"public-harvest" */
function pad(n){var s=String(n);while(s.length<6)s='0'+s;return s;}
var PREFIX='JAH-FFS-';
var SRC='public-harvest';
var RECORD_KIND='secret menu item';
var GENRES=["Arby's", "Burger King", "Chick-fil-A", "Chipotle", "Dairy Queen", "Five Guys", "In-N-Out", "KFC", "McDonald's", "Shake Shack", "Sonic", "Taco Bell", "Wendy's"];
var TOPICS=["Land, Sea & Air Burger", "McGangBang", "McKinley Mac", "Monster Mac", "Neapolitan Shake", "Poor Man\\'s Big Mac", "Grilled Cheese", "McBrunch Burger", "Animal Style Burger", "3x3 / 4x4", "Protein Style", "Flying Dutchman", "Animal Style Fries", "Neapolitan Shake", "Grilled Cheese", "Double Meat", "Suicide Burger", "Rodeo Burger", "Frings", "Mustard Whopper", "The Superman", "Cheesarito", "Double-Grilled Quesadilla", "The Incredible Hulk", "Enchirito", "Spicy Char", "Cookie Icedream Sandwich", "Root Beer Float", "Double Down (Chick-fil-A style)", "T-Rex Burger", "Barnyard Burger", "Grand Slam", "Meat Cube", "Patty Melt", "Double Grilled Cheeseburger", "Dr. Pepper Orgasm", "Purple Sprite", "Frito Pie", "Pickle-O\\'s", "Secret Blizzard Flavors", "Quesarito", "Burritodilla", "Single Taco", "Nachos", "Meat Mountain", "Triple Down", "Poutine", "Peanut Butter Bacon Burger", "Shroom Stack", "Cotton Candy Blizzard", "Mc10:35", "Big McChicken", "In-N-Out Lemon Up", "Well-Done Fries", "Light Fries", "Chili Cheese Burrito", "Green Sauce Everything", "Fries Supreme", "Wendy\\'s Asiago Chicken", "Sonic Ocean Water"];
function mulberry(seed){var a=seed>>>0;return function(){a|=0;a=a+0x6D2B79F5|0;var t=Math.imul(a^a>>>15,1|a);t=t+Math.imul(t^t>>>7,61|t)^t;return((t^t>>>14)>>>0)/4294967296;};}
function buildContent(title,genre){
  var summary='A secret menu item record for '+title+' ('+genre+'). Full ingredients, cooking method, and details in the archive.';
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
var gen={version:'jahdb-public-fast-food-secret-menu-1.0',generate:generate,validate:validate,driftCheck:driftCheck,genres:GENRES};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('public-fast-food-secret-menu',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();