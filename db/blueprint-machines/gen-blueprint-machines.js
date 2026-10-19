(function(){'use strict';
/* JAH The Machine Blueprint Database generator — jahdb-blueprint-machines-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-BMP-";
var FIELDS=["Material Handling","Power","Processing"];
var TOPICS={
 "Material Handling": [
  "Conveyor System - Compact Architectural Blueprint - Material Handling",
  "Farm Tractor - Compact Architectural Blueprint - Material Handling",
  "Excavator - Compact Architectural Blueprint - Material Handling",
  "Conveyor System - Standard Architectural Blueprint - Material Handling",
  "Farm Tractor - Standard Architectural Blueprint - Material Handling",
  "Excavator - Standard Architectural Blueprint - Material Handling",
  "Conveyor System - Grand Architectural Blueprint - Material Handling",
  "Farm Tractor - Grand Architectural Blueprint - Material Handling",
  "Excavator - Grand Architectural Blueprint - Material Handling"
 ],
 "Power": [
  "Steam Engine - Compact Architectural Blueprint - Power",
  "Wind Turbine - Compact Architectural Blueprint - Power",
  "Generator Set - Compact Architectural Blueprint - Power",
  "Steam Engine - Standard Architectural Blueprint - Power",
  "Wind Turbine - Standard Architectural Blueprint - Power",
  "Generator Set - Standard Architectural Blueprint - Power",
  "Steam Engine - Grand Architectural Blueprint - Power",
  "Wind Turbine - Grand Architectural Blueprint - Power"
 ],
 "Processing": [
  "Industrial Press - Compact Architectural Blueprint - Processing",
  "Water Pump Station - Compact Architectural Blueprint - Processing",
  "Air Compressor Station - Compact Architectural Blueprint - Processing",
  "CNC Mill - Compact Architectural Blueprint - Processing",
  "Industrial 3D Printer - Compact Architectural Blueprint - Processing",
  "Lathe - Compact Architectural Blueprint - Processing",
  "Industrial Press - Standard Architectural Blueprint - Processing",
  "Water Pump Station - Standard Architectural Blueprint - Processing",
  "Air Compressor Station - Standard Architectural Blueprint - Processing",
  "CNC Mill - Standard Architectural Blueprint - Processing",
  "Industrial 3D Printer - Standard Architectural Blueprint - Processing",
  "Lathe - Standard Architectural Blueprint - Processing",
  "Industrial Press - Grand Architectural Blueprint - Processing",
  "Water Pump Station - Grand Architectural Blueprint - Processing",
  "Air Compressor Station - Grand Architectural Blueprint - Processing",
  "CNC Mill - Grand Architectural Blueprint - Processing",
  "Industrial 3D Printer - Grand Architectural Blueprint - Processing"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Machines Blueprint Study — "+safe+"\n"
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
    name:topic+' — machine blueprint record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A machine blueprint record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
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
var gen={version:'jahdb-blueprint-machines-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('blueprint-machines',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
