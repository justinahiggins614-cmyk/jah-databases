(function(){'use strict';
/* JAH The Troubleshooting Decision Trees Signature Database generator — jahdb-troubleshooting-decision-trees-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-TSHTS-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "No Power - Device Dead (Signature Edition) - Electrical Faults",
  "Blown Fuse Repeats (Signature Edition) - Electrical Faults",
  "Intermittent Power Loss (Signature Edition) - Electrical Faults",
  "Excessive Vibration (Signature Edition) - Mechanical Faults",
  "Unusual Noise - Grinding (Signature Edition) - Mechanical Faults",
  "Overheating Motor (Signature Edition) - Thermal & Fluid Faults",
  "Fluid Leak Found (Signature Edition) - Thermal & Fluid Faults",
  "Device Will Not Start (Signature Edition) - Control & Software Faults",
  "Erratic Sensor Readings (Signature Edition) - Control & Software Faults",
  "Slow or Sluggish Operation (Signature Edition) - Mechanical Faults"
 ],
 "Compounded": [
  "Circuit Breaker Trips Under Load (Signature Edition) - Electrical Faults",
  "Motor Runs But Overloads (Signature Edition) - Electrical Faults",
  "Bearing Noise Progression (Signature Edition) - Mechanical Faults",
  "Belt Slippage and Squeal (Signature Edition) - Mechanical Faults",
  "Hydraulic Pressure Low (Signature Edition) - Thermal & Fluid Faults",
  "Pneumatic System Won't Hold Pressure (Signature Edition) - Thermal & Fluid Faults",
  "Temperature Control Oscillation (Signature Edition) - Control & Software Faults",
  "Communication Loss to Controller (Signature Edition) - Control & Software Faults",
  "Unexpected Shutdowns (Signature Edition) - Control & Software Faults",
  "Poor Product Quality Drift (Signature Edition) - Mechanical Faults",
  "Ground Fault Indication (Signature Edition) - Electrical Faults",
  "Phase Imbalance Alarm (Signature Edition) - Electrical Faults"
 ],
 "Advanced": [
  "Intermittent Fault - Heat-Related (Signature Edition) - Electrical Faults",
  "Resonance and Critical Speeds (Signature Edition) - Mechanical Faults",
  "Cavitation in Pump Systems (Signature Edition) - Thermal & Fluid Faults",
  "Water Hammer Events (Signature Edition) - Thermal & Fluid Faults",
  "Control Loop Instability (Signature Edition) - Control & Software Faults",
  "Firmware Corruption Symptoms (Signature Edition) - Control & Software Faults",
  "EMI-Induced Malfunctions (Signature Edition) - Electrical Faults",
  "Cascade Failure Analysis (Signature Edition) - Mechanical Faults",
  "Root Cause: Lubrication Failure Tree (Signature Edition) - Mechanical Faults",
  "Multi-Symptom Fault Isolation (Signature Edition) - Control & Software Faults",
  "Post-Repair Recurrence Tree (Signature Edition) - Electrical Faults",
  "Chronic Repeat Failure Investigation (Signature Edition) - Thermal & Fluid Faults"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Troubleshooting Decision Trees Signature — "+safe+"\n"
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
    name:topic+' — troubleshooting decision tree record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A troubleshooting decision tree record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
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
var gen={version:'jahdb-troubleshooting-decision-trees-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('troubleshooting-decision-trees-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
