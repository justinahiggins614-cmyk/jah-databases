(function(){'use strict';
/* JAH The Component Compatibility Matrix Database generator — jahdb-component-compatibility-matrix-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-CPCM-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "What Compatibility Means - Foundations",
  "Reading and Writing a Compatibility Matrix - Foundations",
  "The Five Dimensions of a Pairing - Foundations",
  "Voltage-Level Compatibility - Foundations",
  "Logic Families and Their Pairings - Foundations",
  "Current and Power Delivery Compatibility - Foundations",
  "Connector Mechanical Fit and Mating - Foundations",
  "Protocol Compatibility: UART, SPI, I2C, CAN, USB, Ethernet - Foundations",
  "Signal Integrity and Impedance Matching - Foundations",
  "Tolerance and Clearance for Mating Parts - Foundations",
  "Reading Two Datasheets Side by Side - Foundations",
  "Material Compatibility Basics - Foundations"
 ],
 "Compounded": [
  "Galvanic Corrosion Pairings - Compounded",
  "Thermal Expansion Compatibility - Compounded",
  "Chemical and Environmental Compatibility - Compounded",
  "Solder and Joining Compatibility - Compounded",
  "Power Supply Interoperability - Compounded",
  "Grounding and Shielding Compatibility - Compounded",
  "Battery Chemistry Pairings - Compounded",
  "RF Module Interoperability - Compounded",
  "Firmware and API Version Compatibility - Compounded",
  "Memory and Storage Interface Compatibility - Compounded",
  "Display and Camera Interface Compatibility - Compounded",
  "Sensor Module Compatibility - Compounded",
  "Motor and Driver Compatibility - Compounded",
  "Network Stack and Middleware Compatibility - Compounded"
 ],
 "Advanced": [
  "EMC Compatibility Between Modules - Advanced",
  "Timing Closure Across Interfaces - Advanced",
  "Derating and Reliability of Pairings - Advanced",
  "Cross-Reference Substitution Matrices - Advanced",
  "Full System Integration Matrices - Advanced",
  "Compatibility Testing and Verification - Advanced",
  "Lifecycle and Obsolescence in Pairings - Advanced",
  "Building Your Own Compatibility Matrix - Advanced"
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
var gen={version:'jahdb-component-compatibility-matrix-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('component-compatibility-matrix',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
