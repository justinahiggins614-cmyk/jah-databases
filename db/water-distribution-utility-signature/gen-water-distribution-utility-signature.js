(function(){'use strict';
/* JAH The Water Distribution Utility Signature Database generator — jahdb-water-distribution-utility-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-WDUS-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "What a Water Distribution System Is (Signature Edition) \u2014 Foundations",
  "Sources: Where Drinking Water Comes From (Signature Edition) \u2014 Foundations",
  "Treatment Basics: Making Water Safe (Signature Edition) \u2014 Foundations",
  "The Network: Pipes, Pumps, Tanks (Signature Edition) \u2014 Foundations",
  "Pressure: The System's Lifeblood (Signature Edition) \u2014 Foundations",
  "Flow and Head Loss Basics (Signature Edition) \u2014 Foundations",
  "Demand: How Much, When (Signature Edition) \u2014 Foundations",
  "Water Quality in the Network (Signature Edition) \u2014 Foundations",
  "Disinfection: Chlorine and Friends (Signature Edition) \u2014 Foundations",
  "Storage Tanks: Why Water Waits (Signature Edition) \u2014 Foundations",
  "Pumps: Moving Water Uphill (Signature Edition) \u2014 Foundations",
  "Valves: Controlling the Network (Signature Edition) \u2014 Foundations"
 ],
 "Compounded": [
  "Hazen-Williams and Darcy-Weisbach (Signature Edition) \u2014 Compounded",
  "Network Hydraulics and EPANET (Signature Edition) \u2014 Compounded",
  "Pressure Zones (Signature Edition) \u2014 Compounded",
  "Extended-Period Simulation (Signature Edition) \u2014 Compounded",
  "Water Hammer: Surge Protection (Signature Edition) \u2014 Compounded",
  "Leakage: Finding Lost Water (Signature Edition) \u2014 Compounded",
  "The Infrastructure Leakage Index (ILI) (Signature Edition) \u2014 Compounded",
  "District Metered Areas (DMAs) (Signature Edition) \u2014 Compounded",
  "Chlorine Decay and Booster Stations (Signature Edition) \u2014 Compounded",
  "Water Age and Quality (Signature Edition) \u2014 Compounded",
  "Demand Forecasting (Signature Edition) \u2014 Compounded",
  "Pump Scheduling and Energy (Signature Edition) \u2014 Compounded"
 ],
 "Advanced": [
  "Asset Condition Assessment (Signature Edition) \u2014 Advanced",
  "Pipe Failure Prediction (Signature Edition) \u2014 Advanced",
  "Main Replacement Planning (Signature Edition) \u2014 Advanced",
  "Smart Metering (AMI) (Signature Edition) \u2014 Advanced",
  "SCADA and Real-Time Control (Signature Edition) \u2014 Advanced",
  "Contamination Warning Systems (Signature Edition) \u2014 Advanced",
  "Fire Flow Requirements (Signature Edition) \u2014 Advanced",
  "Hydraulic Model Calibration (Signature Edition) \u2014 Advanced",
  "3D-Printable Pipe Fittings and Trainers (Signature Edition) \u2014 Advanced",
  "Resilience: Emergency Response Planning (Signature Edition) \u2014 Advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Water Utility — "+safe+"\n"
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
    name:topic+' — water utility record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A water utility record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"water-utility-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-water-distribution-utility-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('water-distribution-utility-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
