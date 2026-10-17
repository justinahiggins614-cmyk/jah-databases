(function(){'use strict';
/* JAH The Component Compatibility Matrix Signature Database generator — jahdb-component-compatibility-matrix-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-CPCMS-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "What Compatibility Means (Signature Edition) - Foundations",
  "Reading and Writing a Compatibility Matrix (Signature Edition) - Foundations",
  "The Five Dimensions of a Pairing (Signature Edition) - Foundations",
  "Voltage-Level Compatibility (Signature Edition) - Foundations",
  "Logic Families and Their Pairings (Signature Edition) - Foundations",
  "Current and Power Delivery Compatibility (Signature Edition) - Foundations",
  "Connector Mechanical Fit and Mating (Signature Edition) - Foundations",
  "Protocol Compatibility: UART, SPI, I2C, CAN, USB, Ethernet (Signature Edition) - Foundations",
  "Signal Integrity and Impedance Matching (Signature Edition) - Foundations",
  "Tolerance and Clearance for Mating Parts (Signature Edition) - Foundations",
  "Reading Two Datasheets Side by Side (Signature Edition) - Foundations",
  "Material Compatibility Basics (Signature Edition) - Foundations"
 ],
 "Compounded": [
  "Galvanic Corrosion Pairings (Signature Edition) - Compounded",
  "Thermal Expansion Compatibility (Signature Edition) - Compounded",
  "Chemical and Environmental Compatibility (Signature Edition) - Compounded",
  "Solder and Joining Compatibility (Signature Edition) - Compounded",
  "Power Supply Interoperability (Signature Edition) - Compounded",
  "Grounding and Shielding Compatibility (Signature Edition) - Compounded",
  "Battery Chemistry Pairings (Signature Edition) - Compounded",
  "RF Module Interoperability (Signature Edition) - Compounded",
  "Firmware and API Version Compatibility (Signature Edition) - Compounded",
  "Memory and Storage Interface Compatibility (Signature Edition) - Compounded",
  "Display and Camera Interface Compatibility (Signature Edition) - Compounded",
  "Sensor Module Compatibility (Signature Edition) - Compounded",
  "Motor and Driver Compatibility (Signature Edition) - Compounded",
  "Network Stack and Middleware Compatibility (Signature Edition) - Compounded"
 ],
 "Advanced": [
  "EMC Compatibility Between Modules (Signature Edition) - Advanced",
  "Timing Closure Across Interfaces (Signature Edition) - Advanced",
  "Derating and Reliability of Pairings (Signature Edition) - Advanced",
  "Cross-Reference Substitution Matrices (Signature Edition) - Advanced",
  "Full System Integration Matrices (Signature Edition) - Advanced",
  "Compatibility Testing and Verification (Signature Edition) - Advanced",
  "Lifecycle and Obsolescence in Pairings (Signature Edition) - Advanced",
  "Building Your Own Compatibility Matrix (Signature Edition) - Advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Compatibility Matrix Study — "+safe+"\n"
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
    name:topic+' — compatibility matrix record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A compatibility matrix record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"compatibility-matrix-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-component-compatibility-matrix-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('component-compatibility-matrix-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
