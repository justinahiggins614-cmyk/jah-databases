(function(){'use strict';
/* JAH The Machine Blueprint Signature Database generator — jahdb-blueprint-machines-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-BMPS-";
var FIELDS=["Material Handling","Power","Processing"];
var TOPICS={
 "Material Handling": [
  "Signature Conveyor System - Compact Architectural Blueprint (Signature Edition) - Material Handling",
  "Signature Farm Tractor - Compact Architectural Blueprint (Signature Edition) - Material Handling",
  "Signature Excavator - Compact Architectural Blueprint (Signature Edition) - Material Handling",
  "Signature Conveyor System - Standard Architectural Blueprint (Signature Edition) - Material Handling",
  "Signature Farm Tractor - Standard Architectural Blueprint (Signature Edition) - Material Handling",
  "Signature Excavator - Standard Architectural Blueprint (Signature Edition) - Material Handling",
  "Signature Conveyor System - Grand Architectural Blueprint (Signature Edition) - Material Handling",
  "Signature Farm Tractor - Grand Architectural Blueprint (Signature Edition) - Material Handling",
  "Signature Excavator - Grand Architectural Blueprint (Signature Edition) - Material Handling"
 ],
 "Power": [
  "Signature Steam Engine - Compact Architectural Blueprint (Signature Edition) - Power",
  "Signature Wind Turbine - Compact Architectural Blueprint (Signature Edition) - Power",
  "Signature Generator Set - Compact Architectural Blueprint (Signature Edition) - Power",
  "Signature Steam Engine - Standard Architectural Blueprint (Signature Edition) - Power",
  "Signature Wind Turbine - Standard Architectural Blueprint (Signature Edition) - Power",
  "Signature Generator Set - Standard Architectural Blueprint (Signature Edition) - Power",
  "Signature Steam Engine - Grand Architectural Blueprint (Signature Edition) - Power",
  "Signature Wind Turbine - Grand Architectural Blueprint (Signature Edition) - Power"
 ],
 "Processing": [
  "Signature Industrial Press - Compact Architectural Blueprint (Signature Edition) - Processing",
  "Signature Water Pump Station - Compact Architectural Blueprint (Signature Edition) - Processing",
  "Signature Air Compressor Station - Compact Architectural Blueprint (Signature Edition) - Processing",
  "Signature CNC Mill - Compact Architectural Blueprint (Signature Edition) - Processing",
  "Signature Industrial 3D Printer - Compact Architectural Blueprint (Signature Edition) - Processing",
  "Signature Lathe - Compact Architectural Blueprint (Signature Edition) - Processing",
  "Signature Industrial Press - Standard Architectural Blueprint (Signature Edition) - Processing",
  "Signature Water Pump Station - Standard Architectural Blueprint (Signature Edition) - Processing",
  "Signature Air Compressor Station - Standard Architectural Blueprint (Signature Edition) - Processing",
  "Signature CNC Mill - Standard Architectural Blueprint (Signature Edition) - Processing",
  "Signature Industrial 3D Printer - Standard Architectural Blueprint (Signature Edition) - Processing",
  "Signature Lathe - Standard Architectural Blueprint (Signature Edition) - Processing",
  "Signature Industrial Press - Grand Architectural Blueprint (Signature Edition) - Processing",
  "Signature Water Pump Station - Grand Architectural Blueprint (Signature Edition) - Processing",
  "Signature Air Compressor Station - Grand Architectural Blueprint (Signature Edition) - Processing",
  "Signature CNC Mill - Grand Architectural Blueprint (Signature Edition) - Processing",
  "Signature Industrial 3D Printer - Grand Architectural Blueprint (Signature Edition) - Processing"
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
var gen={version:'jahdb-blueprint-machines-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('blueprint-machines-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
