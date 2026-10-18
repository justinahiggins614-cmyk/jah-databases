(function(){'use strict';
/* JAH The Wardrobe Essentials Database generator — jahdb-wardrobe-essentials-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-WDES-";
var FIELDS=["Essential Foundations", "The Essentials", "Essential Mastery"];
var TOPICS={
 "Essential Foundations": [
  "The Essential Idea",
  "The White Shirt",
  "The Perfect Jean",
  "The Blazer",
  "The Black Pant",
  "The White Sneaker",
  "The Trench Coat",
  "The Cashmere Sweater",
  "The Little Black Dress",
  "The Leather Jacket",
  "The Ankle Boot",
  "The Tote Bag"
 ],
 "The Essentials": [
  "The Silk Scarf",
  "The Gold Hoops",
  "The Watch",
  "The Ballet Flat",
  "The Crew Socks",
  "The Denim Jacket",
  "The Slip Skirt",
  "The Turtleneck",
  "The Loafers",
  "The Cardigan",
  "The Essential Ten",
  "The Essential Twenty"
 ],
 "Essential Mastery": [
  "Cost Per Wear",
  "The Essential Quality",
  "The Essential Fit",
  "The Essential Care",
  "The Essential Edit",
  "The Essential Travel",
  "The Essential Uniform",
  "The Essential Legacy",
  "The Essential Sunglasses",
  "The Essential Belt"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# essential — "+safe+"\n"
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
    name:topic+' — wardrobe essential record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A wardrobe essential record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"essential-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-wardrobe-essentials-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('wardrobe-essentials',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
