(function(){'use strict';
/* JAH The Compatibility and Interchangeability Records Signature Database generator — jahdb-compatibility-interchangeability-records-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-CIRS-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "Reading a Parts Cross-Reference Table (Signature Edition) - Parts Cross-Reference",
  "Bearing Interchange Guide (Signature Edition) - Parts Cross-Reference",
  "Fastener Grade Interchange (Signature Edition) - Parts Cross-Reference",
  "Filter Element Cross-Reference (Signature Edition) - Parts Cross-Reference",
  "V-Belt Size Interchange (Signature Edition) - Parts Cross-Reference",
  "Fuse and Breaker Interchange (Signature Edition) - Parts Cross-Reference",
  "O-Ring Size and Material Interchange (Signature Edition) - Parts Cross-Reference",
  "Lamp and Indicator Interchange (Signature Edition) - Parts Cross-Reference",
  "Battery Size Cross-Reference (Signature Edition) - Parts Cross-Reference",
  "Lubricant Equivalents Table (Signature Edition) - Parts Cross-Reference"
 ],
 "Compounded": [
  "Motor Frame Interchange (Signature Edition) - Systems Compatibility",
  "PLC Module Compatibility (Signature Edition) - Systems Compatibility",
  "Sensor Output Compatibility (Signature Edition) - Systems Compatibility",
  "Power Supply Compatibility (Signature Edition) - Systems Compatibility",
  "Hydraulic Component Interchange (Signature Edition) - Systems Compatibility",
  "Pneumatic Fitting Interchange (Signature Edition) - Interfaces & Connectors",
  "Connector and Pinout Compatibility (Signature Edition) - Interfaces & Connectors",
  "Communication Protocol Compatibility (Signature Edition) - Software & Firmware",
  "Firmware Version Compatibility Matrix (Signature Edition) - Software & Firmware",
  "Operating System and Driver Compatibility (Signature Edition) - Software & Firmware",
  "Superseded Part Number Lookup (Signature Edition) - Parts Cross-Reference",
  "Aftermarket vs OEM Interchange Rules (Signature Edition) - Parts Cross-Reference"
 ],
 "Advanced": [
  "Safety-Rated Component Substitution (Signature Edition) - Systems Compatibility",
  "Hazardous-Area Equipment Compatibility (Signature Edition) - Systems Compatibility",
  "Mixed-Vendor System Integration (Signature Edition) - Systems Compatibility",
  "Legacy System Interface Adaptation (Signature Edition) - Interfaces & Connectors",
  "Software Regression Compatibility Testing (Signature Edition) - Software & Firmware",
  "Database and File Format Compatibility (Signature Edition) - Software & Firmware",
  "Cross-Platform Tool Compatibility (Signature Edition) - Software & Firmware",
  "Obsolete Part Redesign Triggers (Signature Edition) - Parts Cross-Reference",
  "Form-Fit-Function Equivalence Documentation (Signature Edition) - Parts Cross-Reference",
  "Interchangeability Risk Assessment (Signature Edition) - Systems Compatibility",
  "Multi-Site Standardization Records (Signature Edition) - Systems Compatibility",
  "Compatibility Audit Procedure (Signature Edition) - Systems Compatibility"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Compatibility Interchangeability Records Signature — "+safe+"\n"
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
var gen={version:'jahdb-compatibility-interchangeability-records-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('compatibility-interchangeability-records-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
