(function(){'use strict';
/* JAH The Stain Removal Signature Database generator — jahdb-home-cleaning-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-STNRS-";
var FIELDS=["Stain Science Basics", "Food & Drink Stains", "Grease & Oil Stains", "Biological Stains", "Outdoor & Specialty Stains", "Stain Prevention & Fabric Care"];
var TOPICS={
 "Stain Science Basics": [
  "The Golden Rule: Act Fast, Blot Don't Rub (Signature Edition) - Stain Science Basics",
  "Identify the Stain Before You Treat It (Signature Edition) - Stain Science Basics",
  "Reading Care Labels Before Stain Treatment (Signature Edition) - Stain Science Basics",
  "The Basic Stain Kit: What to Keep on Hand (Signature Edition) - Stain Science Basics",
  "Cold Water First: The Temperature Rule (Signature Edition) - Stain Science Basics",
  "Combination Stains: Multi-Step Treatment Plans (Signature Edition) - Stain Science Basics"
 ],
 "Food & Drink Stains": [
  "Coffee and Tea Stains (Signature Edition) - Food & Drink Stains",
  "Red Wine Stains (Signature Edition) - Food & Drink Stains",
  "Chocolate Stains (Signature Edition) - Food & Drink Stains",
  "Tomato Sauce and Ketchup (Signature Edition) - Food & Drink Stains",
  "Fruit Juice and Berry Stains (Signature Edition) - Food & Drink Stains",
  "Tannin Stains: Wine, Coffee, Tea Deep Dive (Signature Edition) - Food & Drink Stains"
 ],
 "Grease & Oil Stains": [
  "Butter and Cooking Oil Spots (Signature Edition) - Grease & Oil Stains",
  "Grease on Work Clothes (Signature Edition) - Grease & Oil Stains",
  "Salad Dressing and Mayonnaise (Signature Edition) - Grease & Oil Stains",
  "Sunscreen and Cosmetics (Signature Edition) - Grease & Oil Stains",
  "Oil Stains on Concrete and Driveways (Signature Edition) - Grease & Oil Stains"
 ],
 "Biological Stains": [
  "Sweat Stains and Yellowing (Signature Edition) - Biological Stains",
  "Protein Stains: Blood, Egg, Dairy (Signature Edition) - Biological Stains",
  "Pet Stains: Urine and Vomit (Signature Edition) - Biological Stains",
  "Stain Removal for Baby and Kids' Clothes (Signature Edition) - Biological Stains"
 ],
 "Outdoor & Specialty Stains": [
  "Grass Stains (Signature Edition) - Outdoor & Specialty Stains",
  "Mud and Dirt (Signature Edition) - Outdoor & Specialty Stains",
  "Ink and Ballpoint Pen (Signature Edition) - Outdoor & Specialty Stains",
  "Crayon and Marker on Fabric (Signature Edition) - Outdoor & Specialty Stains",
  "Rust Stains (Signature Edition) - Outdoor & Specialty Stains",
  "Stains on Upholstery (Signature Edition) - Outdoor & Specialty Stains",
  "Stains on Carpet (Signature Edition) - Outdoor & Specialty Stains"
 ],
 "Stain Prevention & Fabric Care": [
  "Preventing Set-In Stains in the Wash (Signature Edition) - Stain Prevention & Fabric Care",
  "Old, Dried, and Set-In Stains (Signature Edition) - Stain Prevention & Fabric Care",
  "Bleach Spots and Color Loss (Signature Edition) - Stain Prevention & Fabric Care",
  "Dye Transfer in the Wash (Signature Edition) - Stain Prevention & Fabric Care",
  "Stains on Silk, Wool, and Delicates (Signature Edition) - Stain Prevention & Fabric Care",
  "Building a Household Stain Station (Signature Edition) - Stain Prevention & Fabric Care"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# JAH Stain Removal Guide Study — "+safe+"\n"
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
    name:topic+' — stain removal guide record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A stain removal guide record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"stain-removal-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-stain-removal-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('stain-removal-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
