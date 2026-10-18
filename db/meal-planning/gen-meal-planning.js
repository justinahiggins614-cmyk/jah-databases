(function(){'use strict';
/* JAH The Meal Planning Database generator — jahdb-meal-planning-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-MEAL-";
var FIELDS=["Weekly Planning","Meal Prep","Pantry & Staples","Budget Groceries","Leftovers","Food Storage & Safety","Family Meals"];
var TOPICS={
 "Weekly Planning": [
  "The Weekly Meal Planning Method - Weekly Planning",
  "Theme Nights and Rotation Menus - Weekly Planning",
  "Planning Around Busy Schedules - Weekly Planning",
  "Breakfast and Lunch Frameworks - Weekly Planning",
  "Seasonal Meal Planning - Weekly Planning",
  "Meal Planning for Dietary Needs - Weekly Planning"
 ],
 "Meal Prep": [
  "Meal Prep Sunday: The System - Meal Prep",
  "Batch Cooking Proteins - Meal Prep",
  "Grains and Starches in Bulk - Meal Prep",
  "Prepped Vegetables and Salads - Meal Prep",
  "Sauces, Dressings, and Flavor Boosters - Meal Prep",
  "Freezer Meals: Cook Once, Eat Twice - Meal Prep"
 ],
 "Pantry & Staples": [
  "Building a Working Pantry - Pantry & Staples",
  "The Essential Spice Collection - Pantry & Staples",
  "Oils, Vinegars, and Condiments - Pantry & Staples",
  "Canned and Jarred Staples - Pantry & Staples",
  "Baking and Breakfast Staples - Pantry & Staples"
 ],
 "Budget Groceries": [
  "Grocery Budgeting That Works - Budget Groceries",
  "Smart Shopping Strategies - Budget Groceries",
  "Buying in Bulk Wisely - Budget Groceries",
  "Reducing Meat Costs - Budget Groceries",
  "Cutting Food Waste to Save Money - Budget Groceries"
 ],
 "Leftovers": [
  "The Art of Leftover Makeovers - Leftovers",
  "Leftover Safety: Storage and Reheating - Leftovers",
  "Planned-Overs: Cooking for Leftovers - Leftovers",
  "Using Up Produce Before It Spoils - Leftovers"
 ],
 "Food Storage & Safety": [
  "Refrigerator Organization and Zones - Food Storage & Safety",
  "Freezer Organization and Inventory - Food Storage & Safety",
  "Pantry Storage: What Goes Where - Food Storage & Safety",
  "Food Safety Essentials at Home - Food Storage & Safety",
  "Understanding Food Dates and Spoilage - Food Storage & Safety"
 ],
 "Family Meals": [
  "Family Dinners That Connect - Family Meals",
  "Cooking With Kids - Family Meals",
  "Hosting Family Meals and Gatherings - Family Meals"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Meal Planning Study — "+safe+"\n"
   + "# Field: "+field+"\n"
   + "record = {'title': \""+safe+"\", 'field': \""+field+"\"}\n"
   + "def summarize(r):\n"
   + "    return r['title'] + ' [' + r['field'] + ']'\n"
   + "print(summarize(record))\n"
   + "print('Sample record — structural sample, not an archive entry.')\n";
}
function generate(seed,opts,rnd){
  opts=opts||{}; rnd=rnd||prng(seed);
  var field=opts.field&&FIELDS.indexOf(opts.field)>=0?opts.field:pick(FIELDS,rnd);
  var pool=TOPICS[field]||["General Study"];
  var topic=pick(pool,rnd);
  var id=PREFIX+String(seed).padStart(6,'0');
  return {
    id:id,
    name:topic+' — meal planning guide record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A meal planning guide record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"meal-planning-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
    _seed:seed
  };
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  if(!new RegExp('^'+PREFIX.replace(/-/g,'\\-')+'\\d{6}$').test(r.id||''))e.push('id');
  if(FIELDS.indexOf(r.field)<0)e.push('field');
  if(!r.src)e.push('src');
  if(!r.demo||!r.demo.program)e.push('demo');
  return {ok:!e.length,errors:e};
}
function driftCheck(record,sample){
  var dups=(sample||[]).filter(function(r){return r&&r.title===record.title&&r.field===record.field;});
  return dups.length?{ok:false,errors:['duplicate topic+field in archive sample']}:{ok:true,errors:[]};
}
var gen={version:'jahdb-meal-planning-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('meal-planning',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
