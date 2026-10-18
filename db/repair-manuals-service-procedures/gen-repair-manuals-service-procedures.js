(function(){'use strict';
/* JAH The Repair Manuals and Service Procedures Database generator — jahdb-repair-manuals-service-procedures-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-RMSP-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "Visual Inspection Procedure - Diagnostics",
  "Reading and Interpreting Fault Codes - Diagnostics",
  "Power Supply Verification Sequence - Diagnostics",
  "Continuity and Resistance Testing - Diagnostics",
  "Fastener Identification and Torque Basics - Disassembly",
  "Safe Disassembly Order Planning - Disassembly",
  "Cable and Connector Handling - Disassembly",
  "Cleaning Procedures for Service - Repair",
  "Lubrication Basics in Service - Adjustment",
  "Reassembly Verification Checklist - Verification"
 ],
 "Compounded": [
  "Board-Level Diagnostic Procedure - Diagnostics",
  "Electrolytic Capacitor Replacement - Repair",
  "Belt and Chain Replacement - Repair",
  "Bearing Replacement Procedure - Repair",
  "Sensor Recalibration After Repair - Adjustment",
  "Firmware Reflash Service Procedure - Repair",
  "Hydraulic Seal Replacement - Repair",
  "DC Motor Brush Replacement - Repair",
  "Gasket Replacement and Sealing - Repair",
  "Shaft Alignment After Repair - Adjustment",
  "Thermal Paste Renewal on Power Electronics - Repair",
  "Battery Pack Servicing Procedure - Repair"
 ],
 "Advanced": [
  "Intermittent Fault Hunting Method - Diagnostics",
  "Gearbox Overhaul Procedure - Repair",
  "Spindle Rebuild Procedure - Repair",
  "BGA Rework Outline for Service Shops - Repair",
  "Root-Cause Failure Analysis Writeup - Diagnostics",
  "Calibration Restoration After Major Repair - Adjustment",
  "EMC Re-Verification After Repair - Verification",
  "Safety Interlock Restoration and Test - Verification",
  "Pressure System Repair Documentation - Repair",
  "Field Repair Under Constraints - Repair",
  "Repair-Versus-Replace Decision Record - Diagnostics",
  "Final Acceptance Test Protocol - Verification"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Repair Manuals Service Procedures — "+safe+"\n"
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
    name:topic+' — service procedure record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A service procedure record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"python",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-repair-manuals-service-procedures-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('repair-manuals-service-procedures',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
