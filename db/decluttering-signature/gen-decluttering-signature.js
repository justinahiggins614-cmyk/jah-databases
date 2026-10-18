(function(){'use strict';
/* JAH The Decluttering Signature Database generator — jahdb-home-cleaning-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-DCLTS-";
var FIELDS=["Declutter Mindset", "Room-by-Room Declutter", "Paper & Digital Declutter", "Clothes & Closets", "Sentimental Items", "Keeping Clutter Away"];
var TOPICS={
 "Declutter Mindset": [
  "Why Clutter Happens: The Psychology (Signature Edition) - Declutter Mindset",
  "The Four-Box Method (Signature Edition) - Declutter Mindset",
  "Start Small: The 15-Minute Declutter (Signature Edition) - Declutter Mindset",
  "The 90/90 Rule for Keep Decisions (Signature Edition) - Declutter Mindset",
  "Decluttering Without Guilt (Signature Edition) - Declutter Mindset",
  "The Inflow Audit: Stop Clutter at the Door (Signature Edition) - Declutter Mindset",
  "The 30-Day Declutter Sprint (Signature Edition) - Declutter Mindset",
  "The Maybe Box Technique (Signature Edition) - Declutter Mindset",
  "Minimalism as a Lifestyle (Signature Edition) - Declutter Mindset"
 ],
 "Room-by-Room Declutter": [
  "Bedroom Declutter (Signature Edition) - Room-by-Room Declutter",
  "Kitchen Declutter (Signature Edition) - Room-by-Room Declutter",
  "Bathroom Declutter (Signature Edition) - Room-by-Room Declutter",
  "Living Room Declutter (Signature Edition) - Room-by-Room Declutter",
  "Kids' Stuff Declutter (Signature Edition) - Room-by-Room Declutter",
  "Garage and Storage Declutter (Signature Edition) - Room-by-Room Declutter",
  "Book, Media, and Hobby Declutter (Signature Edition) - Room-by-Room Declutter",
  "The One-Room Deep Declutter Intensive (Signature Edition) - Room-by-Room Declutter"
 ],
 "Paper & Digital Declutter": [
  "Paper Declutter: The Great Purge (Signature Edition) - Paper & Digital Declutter",
  "Digital Declutter: Files and Photos (Signature Edition) - Paper & Digital Declutter",
  "Digital Legacy Declutter (Signature Edition) - Paper & Digital Declutter"
 ],
 "Clothes & Closets": [
  "Closet Declutter: The Try-On Session (Signature Edition) - Clothes & Closets",
  "Wardrobe Capsule: Fewer, Better Clothes (Signature Edition) - Clothes & Closets",
  "Capsule Living Beyond Clothes (Signature Edition) - Clothes & Closets"
 ],
 "Sentimental Items": [
  "Sentimental Items: The Hardest Category (Signature Edition) - Sentimental Items",
  "Hoarding vs Collecting: Knowing the Difference (Signature Edition) - Sentimental Items",
  "Estate Declutter: Clearing a Loved One's Home (Signature Edition) - Sentimental Items",
  "Helping Aging Parents Declutter (Signature Edition) - Sentimental Items"
 ],
 "Keeping Clutter Away": [
  "Selling vs Donating Declutter (Signature Edition) - Keeping Clutter Away",
  "Decluttering With a Partner or Family (Signature Edition) - Keeping Clutter Away",
  "Seasonal Declutter Rhythms (Signature Edition) - Keeping Clutter Away",
  "The No-Buy Challenge (Signature Edition) - Keeping Clutter Away",
  "Maintaining a Decluttered Home for Years (Signature Edition) - Keeping Clutter Away",
  "Decluttering for a Move (Signature Edition) - Keeping Clutter Away",
  "The Legacy of Less: Teaching the Next Generation (Signature Edition) - Keeping Clutter Away"
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
var gen={version:'jahdb-decluttering-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('decluttering-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
