(function(){'use strict';
/* JAH The Installation and Commissioning Procedures Database generator — jahdb-installation-commissioning-procedures-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-ICOP-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "Site Survey and Readiness Checklist - Site Preparation",
  "Receiving, Unpacking, and Damage Inspection - Site Preparation",
  "Foundation and Anchoring Requirements - Site Preparation",
  "Utility Requirements Verification - Site Preparation",
  "Rigging and Placement Procedure - Mechanical Installation",
  "Leveling and Alignment Basics - Mechanical Installation",
  "Mechanical Assembly Sequence - Mechanical Installation",
  "Piping and Ductwork Connection - Mechanical Installation",
  "Electrical Supply Connection Procedure - Electrical & Controls",
  "Grounding and Bonding Verification - Electrical & Controls"
 ],
 "Compounded": [
  "Control Panel Wiring Checkout - Electrical & Controls",
  "Sensor and Instrument Installation - Electrical & Controls",
  "Network and Communication Setup - Electrical & Controls",
  "Safety System Installation and Checkout - Electrical & Controls",
  "Lubrication System Fill and Prime - Startup",
  "First-Energization Procedure - Startup",
  "Dry-Run and Rotation Checks - Startup",
  "Control Loop Tuning at Startup - Startup",
  "Load Testing Procedure - Acceptance Testing",
  "Performance Verification Runs - Acceptance Testing",
  "Punch List Management - Acceptance Testing",
  "Operator Training Handover - Acceptance Testing"
 ],
 "Advanced": [
  "Hazardous-Area Installation Requirements - Site Preparation",
  "Seismic Anchoring and Restraint - Mechanical Installation",
  "High-Voltage Connection Procedure - Electrical & Controls",
  "Functional Safety Validation - Acceptance Testing",
  "Integrated Systems Test - Acceptance Testing",
  "72-Hour Continuous Run Trial - Acceptance Testing",
  "Environmental Compliance Verification - Acceptance Testing",
  "Spare Parts and Documentation Handover - Acceptance Testing",
  "Warranty Activation Procedure - Acceptance Testing",
  "Remote Monitoring Commissioning - Startup",
  "Multi-Unit Synchronized Startup - Startup",
  "Final Sign-Off and Acceptance Certificate - Acceptance Testing"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Installation Commissioning Procedures — "+safe+"\n"
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
    name:topic+' — commissioning procedure record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A commissioning procedure record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
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
var gen={version:'jahdb-installation-commissioning-procedures-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('installation-commissioning-procedures',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
