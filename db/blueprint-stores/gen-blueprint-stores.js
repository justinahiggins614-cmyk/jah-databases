(function(){'use strict';
/* JAH The Store Blueprint Database generator — jahdb-blueprint-stores-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-BSP-";
var FIELDS=["Food Retail","General Retail","Specialty Retail"];
var TOPICS={
 "Food Retail": [
  "Supermarket - Compact Architectural Blueprint - Food Retail",
  "Convenience Store - Compact Architectural Blueprint - Food Retail",
  "Bakery - Compact Architectural Blueprint - Food Retail",
  "Supermarket - Standard Architectural Blueprint - Food Retail",
  "Convenience Store - Standard Architectural Blueprint - Food Retail",
  "Bakery - Standard Architectural Blueprint - Food Retail",
  "Supermarket - Grand Architectural Blueprint - Food Retail",
  "Convenience Store - Grand Architectural Blueprint - Food Retail",
  "Bakery - Grand Architectural Blueprint - Food Retail"
 ],
 "General Retail": [
  "General Store - Compact Architectural Blueprint - General Retail",
  "Hardware Store - Compact Architectural Blueprint - General Retail",
  "Furniture Showroom - Compact Architectural Blueprint - General Retail",
  "General Store - Standard Architectural Blueprint - General Retail",
  "Hardware Store - Standard Architectural Blueprint - General Retail",
  "Furniture Showroom - Standard Architectural Blueprint - General Retail",
  "General Store - Grand Architectural Blueprint - General Retail",
  "Hardware Store - Grand Architectural Blueprint - General Retail",
  "Furniture Showroom - Grand Architectural Blueprint - General Retail"
 ],
 "Specialty Retail": [
  "Clothing Boutique - Compact Architectural Blueprint - Specialty Retail",
  "Bookstore - Compact Architectural Blueprint - Specialty Retail",
  "Pharmacy - Compact Architectural Blueprint - Specialty Retail",
  "Mall Kiosk Court - Compact Architectural Blueprint - Specialty Retail",
  "Auto Parts Store - Compact Architectural Blueprint - Specialty Retail",
  "Garden Center - Compact Architectural Blueprint - Specialty Retail",
  "Clothing Boutique - Standard Architectural Blueprint - Specialty Retail",
  "Bookstore - Standard Architectural Blueprint - Specialty Retail",
  "Pharmacy - Standard Architectural Blueprint - Specialty Retail",
  "Mall Kiosk Court - Standard Architectural Blueprint - Specialty Retail",
  "Auto Parts Store - Standard Architectural Blueprint - Specialty Retail",
  "Garden Center - Standard Architectural Blueprint - Specialty Retail",
  "Clothing Boutique - Grand Architectural Blueprint - Specialty Retail",
  "Bookstore - Grand Architectural Blueprint - Specialty Retail",
  "Pharmacy - Grand Architectural Blueprint - Specialty Retail",
  "Mall Kiosk Court - Grand Architectural Blueprint - Specialty Retail"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Stores Blueprint Study — "+safe+"\n"
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
    name:topic+' — store blueprint record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A store blueprint record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"blueprint-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-blueprint-stores-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('blueprint-stores',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
