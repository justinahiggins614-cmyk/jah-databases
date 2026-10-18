(function(){'use strict';
/* JAH The Home Cleaning Database generator — jahdb-home-cleaning-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-HCLN-";
var FIELDS=["Cleaning Foundations","Kitchen","Bathroom","Living Areas & Bedrooms","Laundry","Whole-Home Systems"];
var TOPICS={
 "Cleaning Foundations": [
  "Cleaning Top to Bottom, Left to Right - Cleaning Foundations",
  "The Core Cleaning Kit: What You Actually Need - Cleaning Foundations",
  "Reading Labels: Dwell Time and Dilution - Cleaning Foundations",
  "Microfiber: The Cloth That Changed Cleaning - Cleaning Foundations",
  "The 20-Minute Whole-House Reset - Cleaning Foundations",
  "Declutter Before You Clean, Always - Cleaning Foundations"
 ],
 "Kitchen": [
  "The Kitchen Deep Clean, Zone by Zone - Kitchen",
  "Degreasing the Stove, Oven, and Hood - Kitchen",
  "Refrigerator Cleanout and Organization - Kitchen",
  "Cutting Boards, Knives, and Food-Contact Hygiene - Kitchen",
  "Small Appliances: Coffee Maker, Microwave, Toaster - Kitchen",
  "Kitchen Floors: Tile, Vinyl, and Wood - Kitchen"
 ],
 "Bathroom": [
  "The Bathroom in 15 Minutes - Bathroom",
  "Killing Soap Scum and Hard-Water Scale - Bathroom",
  "Toilet Deep Clean Without the Ick - Bathroom",
  "Grout: Cleaning and Keeping It Clean - Bathroom",
  "Bathroom Ventilation and Mildew Prevention - Bathroom",
  "Towels, Mats, and Shower Curtains - Bathroom"
 ],
 "Living Areas & Bedrooms": [
  "Dusting That Actually Removes Dust - Living Areas & Bedrooms",
  "Vacuuming Like a Pro - Living Areas & Bedrooms",
  "Hardwood and Laminate Floor Care - Living Areas & Bedrooms",
  "Bedroom Reset: Bedding, Mattress, and Air - Living Areas & Bedrooms",
  "Windows, Mirrors, and Glass Without Streaks - Living Areas & Bedrooms"
 ],
 "Laundry": [
  "Sorting Laundry the Smart Way - Laundry",
  "Reading Care Labels and Choosing Settings - Laundry",
  "Stain Removal: Act Fast, Treat Right - Laundry",
  "Drying: Machine, Line, and Flat - Laundry",
  "Folding, Hanging, and Putting Away - Laundry",
  "Laundry Scheduling for Busy Households - Laundry"
 ],
 "Whole-Home Systems": [
  "Seasonal Deep-Clean Checklists - Whole-Home Systems",
  "Cleaning With Kids and Pets in the House - Whole-Home Systems",
  "Green Cleaning: What Works and What Does Not - Whole-Home Systems",
  "Hiring and Working With a Cleaning Service - Whole-Home Systems",
  "The Annual Home Cleaning Audit - Whole-Home Systems"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Home Cleaning Study — "+safe+"\n"
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
    name:topic+' — home cleaning guide record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A home cleaning guide record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"home-cleaning-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-home-cleaning-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('home-cleaning',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
