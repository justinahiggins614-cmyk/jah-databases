(function(){'use strict';
/* JAH The Warehouse Blueprint Database generator — jahdb-blueprint-warehouses-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-BWP-";
var FIELDS=["Distribution","Specialized","Storage"];
var TOPICS={
 "Distribution": [
  "Distribution Center - Compact Architectural Blueprint - Distribution",
  "Fulfillment Warehouse - Compact Architectural Blueprint - Distribution",
  "Cross-Dock Terminal - Compact Architectural Blueprint - Distribution",
  "Light Manufacturing Warehouse - Compact Architectural Blueprint - Distribution",
  "Intermodal Yard Office - Compact Architectural Blueprint - Distribution",
  "Distribution Center - Standard Architectural Blueprint - Distribution",
  "Fulfillment Warehouse - Standard Architectural Blueprint - Distribution",
  "Cross-Dock Terminal - Standard Architectural Blueprint - Distribution",
  "Light Manufacturing Warehouse - Standard Architectural Blueprint - Distribution",
  "Intermodal Yard Office - Standard Architectural Blueprint - Distribution",
  "Distribution Center - Grand Architectural Blueprint - Distribution",
  "Fulfillment Warehouse - Grand Architectural Blueprint - Distribution",
  "Cross-Dock Terminal - Grand Architectural Blueprint - Distribution",
  "Light Manufacturing Warehouse - Grand Architectural Blueprint - Distribution"
 ],
 "Specialized": [
  "Cold Storage Warehouse - Compact Architectural Blueprint - Specialized",
  "Hazmat Warehouse - Compact Architectural Blueprint - Specialized",
  "Records Archive Warehouse - Compact Architectural Blueprint - Specialized",
  "Cold Storage Warehouse - Standard Architectural Blueprint - Specialized",
  "Hazmat Warehouse - Standard Architectural Blueprint - Specialized",
  "Records Archive Warehouse - Standard Architectural Blueprint - Specialized",
  "Cold Storage Warehouse - Grand Architectural Blueprint - Specialized",
  "Hazmat Warehouse - Grand Architectural Blueprint - Specialized",
  "Records Archive Warehouse - Grand Architectural Blueprint - Specialized"
 ],
 "Storage": [
  "Bulk Storage Shed - Compact Architectural Blueprint - Storage",
  "Self-Storage Facility - Compact Architectural Blueprint - Storage",
  "Grain Silo Complex - Compact Architectural Blueprint - Storage",
  "Retail Back-Stock Warehouse - Compact Architectural Blueprint - Storage",
  "Bulk Storage Shed - Standard Architectural Blueprint - Storage",
  "Self-Storage Facility - Standard Architectural Blueprint - Storage",
  "Grain Silo Complex - Standard Architectural Blueprint - Storage",
  "Retail Back-Stock Warehouse - Standard Architectural Blueprint - Storage",
  "Bulk Storage Shed - Grand Architectural Blueprint - Storage",
  "Self-Storage Facility - Grand Architectural Blueprint - Storage",
  "Grain Silo Complex - Grand Architectural Blueprint - Storage"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Warehouses Blueprint Study — "+safe+"\n"
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
    name:topic+' — warehouse blueprint record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A warehouse blueprint record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
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
var gen={version:'jahdb-blueprint-warehouses-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('blueprint-warehouses',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
