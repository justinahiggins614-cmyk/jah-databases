(function(){'use strict';
/* JAH The Troubleshooting Decision Trees Database generator — jahdb-troubleshooting-decision-trees-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-TSHT-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "No Power - Device Dead - Electrical Faults",
  "Blown Fuse Repeats - Electrical Faults",
  "Intermittent Power Loss - Electrical Faults",
  "Excessive Vibration - Mechanical Faults",
  "Unusual Noise - Grinding - Mechanical Faults",
  "Overheating Motor - Thermal & Fluid Faults",
  "Fluid Leak Found - Thermal & Fluid Faults",
  "Device Will Not Start - Control & Software Faults",
  "Erratic Sensor Readings - Control & Software Faults",
  "Slow or Sluggish Operation - Mechanical Faults"
 ],
 "Compounded": [
  "Circuit Breaker Trips Under Load - Electrical Faults",
  "Motor Runs But Overloads - Electrical Faults",
  "Bearing Noise Progression - Mechanical Faults",
  "Belt Slippage and Squeal - Mechanical Faults",
  "Hydraulic Pressure Low - Thermal & Fluid Faults",
  "Pneumatic System Won't Hold Pressure - Thermal & Fluid Faults",
  "Temperature Control Oscillation - Control & Software Faults",
  "Communication Loss to Controller - Control & Software Faults",
  "Unexpected Shutdowns - Control & Software Faults",
  "Poor Product Quality Drift - Mechanical Faults",
  "Ground Fault Indication - Electrical Faults",
  "Phase Imbalance Alarm - Electrical Faults"
 ],
 "Advanced": [
  "Intermittent Fault - Heat-Related - Electrical Faults",
  "Resonance and Critical Speeds - Mechanical Faults",
  "Cavitation in Pump Systems - Thermal & Fluid Faults",
  "Water Hammer Events - Thermal & Fluid Faults",
  "Control Loop Instability - Control & Software Faults",
  "Firmware Corruption Symptoms - Control & Software Faults",
  "EMI-Induced Malfunctions - Electrical Faults",
  "Cascade Failure Analysis - Mechanical Faults",
  "Root Cause: Lubrication Failure Tree - Mechanical Faults",
  "Multi-Symptom Fault Isolation - Control & Software Faults",
  "Post-Repair Recurrence Tree - Electrical Faults",
  "Chronic Repeat Failure Investigation - Thermal & Fluid Faults"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Troubleshooting Decision Trees — "+safe+"\n"
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
var gen={version:'jahdb-troubleshooting-decision-trees-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('troubleshooting-decision-trees',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
