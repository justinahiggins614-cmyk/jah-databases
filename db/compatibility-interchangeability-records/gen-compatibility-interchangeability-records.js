(function(){'use strict';
/* JAH The Compatibility and Interchangeability Records Database generator — jahdb-compatibility-interchangeability-records-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-CIR-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "Reading a Parts Cross-Reference Table - Parts Cross-Reference",
  "Bearing Interchange Guide - Parts Cross-Reference",
  "Fastener Grade Interchange - Parts Cross-Reference",
  "Filter Element Cross-Reference - Parts Cross-Reference",
  "V-Belt Size Interchange - Parts Cross-Reference",
  "Fuse and Breaker Interchange - Parts Cross-Reference",
  "O-Ring Size and Material Interchange - Parts Cross-Reference",
  "Lamp and Indicator Interchange - Parts Cross-Reference",
  "Battery Size Cross-Reference - Parts Cross-Reference",
  "Lubricant Equivalents Table - Parts Cross-Reference"
 ],
 "Compounded": [
  "Motor Frame Interchange - Systems Compatibility",
  "PLC Module Compatibility - Systems Compatibility",
  "Sensor Output Compatibility - Systems Compatibility",
  "Power Supply Compatibility - Systems Compatibility",
  "Hydraulic Component Interchange - Systems Compatibility",
  "Pneumatic Fitting Interchange - Interfaces & Connectors",
  "Connector and Pinout Compatibility - Interfaces & Connectors",
  "Communication Protocol Compatibility - Software & Firmware",
  "Firmware Version Compatibility Matrix - Software & Firmware",
  "Operating System and Driver Compatibility - Software & Firmware",
  "Superseded Part Number Lookup - Parts Cross-Reference",
  "Aftermarket vs OEM Interchange Rules - Parts Cross-Reference"
 ],
 "Advanced": [
  "Safety-Rated Component Substitution - Systems Compatibility",
  "Hazardous-Area Equipment Compatibility - Systems Compatibility",
  "Mixed-Vendor System Integration - Systems Compatibility",
  "Legacy System Interface Adaptation - Interfaces & Connectors",
  "Software Regression Compatibility Testing - Software & Firmware",
  "Database and File Format Compatibility - Software & Firmware",
  "Cross-Platform Tool Compatibility - Software & Firmware",
  "Obsolete Part Redesign Triggers - Parts Cross-Reference",
  "Form-Fit-Function Equivalence Documentation - Parts Cross-Reference",
  "Interchangeability Risk Assessment - Systems Compatibility",
  "Multi-Site Standardization Records - Systems Compatibility",
  "Compatibility Audit Procedure - Systems Compatibility"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Compatibility Interchangeability Records — "+safe+"\n"
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
    name:topic+' — compatibility cross-reference record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A compatibility cross-reference record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
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
var gen={version:'jahdb-compatibility-interchangeability-records-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('compatibility-interchangeability-records',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
