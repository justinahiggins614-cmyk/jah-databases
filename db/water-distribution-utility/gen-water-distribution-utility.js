(function(){'use strict';
/* JAH The Water Distribution Utility Database generator — jahdb-water-distribution-utility-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-WDU-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "What a Water Distribution System Is \u2014 Foundations",
  "Sources: Where Drinking Water Comes From \u2014 Foundations",
  "Treatment Basics: Making Water Safe \u2014 Foundations",
  "The Network: Pipes, Pumps, Tanks \u2014 Foundations",
  "Pressure: The System's Lifeblood \u2014 Foundations",
  "Flow and Head Loss Basics \u2014 Foundations",
  "Demand: How Much, When \u2014 Foundations",
  "Water Quality in the Network \u2014 Foundations",
  "Disinfection: Chlorine and Friends \u2014 Foundations",
  "Storage Tanks: Why Water Waits \u2014 Foundations",
  "Pumps: Moving Water Uphill \u2014 Foundations",
  "Valves: Controlling the Network \u2014 Foundations"
 ],
 "Compounded": [
  "Hazen-Williams and Darcy-Weisbach \u2014 Compounded",
  "Network Hydraulics and EPANET \u2014 Compounded",
  "Pressure Zones \u2014 Compounded",
  "Extended-Period Simulation \u2014 Compounded",
  "Water Hammer: Surge Protection \u2014 Compounded",
  "Leakage: Finding Lost Water \u2014 Compounded",
  "The Infrastructure Leakage Index (ILI) \u2014 Compounded",
  "District Metered Areas (DMAs) \u2014 Compounded",
  "Chlorine Decay and Booster Stations \u2014 Compounded",
  "Water Age and Quality \u2014 Compounded",
  "Demand Forecasting \u2014 Compounded",
  "Pump Scheduling and Energy \u2014 Compounded"
 ],
 "Advanced": [
  "Asset Condition Assessment \u2014 Advanced",
  "Pipe Failure Prediction \u2014 Advanced",
  "Main Replacement Planning \u2014 Advanced",
  "Smart Metering (AMI) \u2014 Advanced",
  "SCADA and Real-Time Control \u2014 Advanced",
  "Contamination Warning Systems \u2014 Advanced",
  "Fire Flow Requirements \u2014 Advanced",
  "Hydraulic Model Calibration \u2014 Advanced",
  "3D-Printable Pipe Fittings and Trainers \u2014 Advanced",
  "Resilience: Emergency Response Planning \u2014 Advanced"
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
var gen={version:'jahdb-water-distribution-utility-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('water-distribution-utility',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
