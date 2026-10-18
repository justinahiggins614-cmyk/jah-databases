(function(){'use strict';
/* JAH The Decluttering Database generator — jahdb-home-cleaning-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-DCLT-";
var FIELDS=["Declutter Mindset", "Room-by-Room Declutter", "Paper & Digital Declutter", "Clothes & Closets", "Sentimental Items", "Keeping Clutter Away"];
var TOPICS={
 "Declutter Mindset": [
  "Why Clutter Happens: The Psychology - Declutter Mindset",
  "The Four-Box Method - Declutter Mindset",
  "Start Small: The 15-Minute Declutter - Declutter Mindset",
  "The 90/90 Rule for Keep Decisions - Declutter Mindset",
  "Decluttering Without Guilt - Declutter Mindset",
  "The Inflow Audit: Stop Clutter at the Door - Declutter Mindset",
  "The 30-Day Declutter Sprint - Declutter Mindset",
  "The Maybe Box Technique - Declutter Mindset",
  "Minimalism as a Lifestyle - Declutter Mindset"
 ],
 "Room-by-Room Declutter": [
  "Bedroom Declutter - Room-by-Room Declutter",
  "Kitchen Declutter - Room-by-Room Declutter",
  "Bathroom Declutter - Room-by-Room Declutter",
  "Living Room Declutter - Room-by-Room Declutter",
  "Kids' Stuff Declutter - Room-by-Room Declutter",
  "Garage and Storage Declutter - Room-by-Room Declutter",
  "Book, Media, and Hobby Declutter - Room-by-Room Declutter",
  "The One-Room Deep Declutter Intensive - Room-by-Room Declutter"
 ],
 "Paper & Digital Declutter": [
  "Paper Declutter: The Great Purge - Paper & Digital Declutter",
  "Digital Declutter: Files and Photos - Paper & Digital Declutter",
  "Digital Legacy Declutter - Paper & Digital Declutter"
 ],
 "Clothes & Closets": [
  "Closet Declutter: The Try-On Session - Clothes & Closets",
  "Wardrobe Capsule: Fewer, Better Clothes - Clothes & Closets",
  "Capsule Living Beyond Clothes - Clothes & Closets"
 ],
 "Sentimental Items": [
  "Sentimental Items: The Hardest Category - Sentimental Items",
  "Hoarding vs Collecting: Knowing the Difference - Sentimental Items",
  "Estate Declutter: Clearing a Loved One's Home - Sentimental Items",
  "Helping Aging Parents Declutter - Sentimental Items"
 ],
 "Keeping Clutter Away": [
  "Selling vs Donating Declutter - Keeping Clutter Away",
  "Decluttering With a Partner or Family - Keeping Clutter Away",
  "Seasonal Declutter Rhythms - Keeping Clutter Away",
  "The No-Buy Challenge - Keeping Clutter Away",
  "Maintaining a Decluttered Home for Years - Keeping Clutter Away",
  "Decluttering for a Move - Keeping Clutter Away",
  "The Legacy of Less: Teaching the Next Generation - Keeping Clutter Away"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# JAH Decluttering Guide Study — "+safe+"\n"
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
    name:topic+' — decluttering guide record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A decluttering guide record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"decluttering-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-decluttering-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('decluttering',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
