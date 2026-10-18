(function(){'use strict';
/* JAH The Engineering Case Studies Signature Database generator — jahdb-engineering-case-studies-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-ENCSS-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "Conveyor Belt Failure at a Packaging Plant (Signature Edition) - Mechanical",
  "Office Building HVAC Retrofit (Signature Edition) - Systems & Controls",
  "Parking Lot Lighting Upgrade (Signature Edition) - Electrical",
  "Warehouse Racking Collapse Investigation (Signature Edition) - Civil & Structural",
  "Pump Seal Failures at a Water Plant (Signature Edition) - Mechanical",
  "Data Center Cooling Upgrade (Signature Edition) - Systems & Controls",
  "Pedestrian Bridge Vibration Complaint (Signature Edition) - Civil & Structural",
  "Motor Control Center Arc Flash Study (Signature Edition) - Electrical",
  "Compressed Air Leak Survey (Signature Edition) - Mechanical",
  "School Gymnasium Roof Snow Load (Signature Edition) - Civil & Structural"
 ],
 "Compounded": [
  "CNC Machine Thermal Drift Correction (Signature Edition) - Mechanical",
  "Hospital Emergency Power System Test (Signature Edition) - Electrical",
  "Bridge Bearing Replacement (Signature Edition) - Civil & Structural",
  "Factory Power Factor Correction (Signature Edition) - Electrical",
  "Injection Molding Warpage Reduction (Signature Edition) - Mechanical",
  "Wastewater Aeration Blower Upgrade (Signature Edition) - Systems & Controls",
  "High-Rise Elevator Modernization (Signature Edition) - Systems & Controls",
  "Substation Ground Grid Remediation (Signature Edition) - Electrical",
  "Retaining Wall Drainage Failure (Signature Edition) - Civil & Structural",
  "Robotic Cell Guarding Redesign (Signature Edition) - Systems & Controls",
  "Boiler Feedwater Pump Cavitation Fix (Signature Edition) - Mechanical",
  "Harmonic Distortion in a Printing Plant (Signature Edition) - Electrical"
 ],
 "Advanced": [
  "Turbine Blade Fatigue Investigation (Signature Edition) - Mechanical",
  "Seismic Retrofit of a Historic Building (Signature Edition) - Civil & Structural",
  "Microgrid Islanding Test (Signature Edition) - Electrical",
  "Dam Spillway Gate Automation (Signature Edition) - Systems & Controls",
  "Crane Runway Girder Fatigue Repair (Signature Edition) - Civil & Structural",
  "Cleanroom Particle Excursion Root Cause (Signature Edition) - Systems & Controls",
  "Wind Turbine Gearbox Failure Analysis (Signature Edition) - Mechanical",
  "Hospital Isolation Room Pressure Control (Signature Edition) - Systems & Controls",
  "Flood Protection Barrier Deployment (Signature Edition) - Civil & Structural",
  "EV Charging Depot Load Management (Signature Edition) - Electrical",
  "Chemical Reactor Agitator Redesign (Signature Edition) - Mechanical",
  "Lessons-Learned Program Design (Signature Edition) - Systems & Controls"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Engineering Case Studies Signature — "+safe+"\n"
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
    name:topic+' — engineering case study record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A engineering case study record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
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
var gen={version:'jahdb-engineering-case-studies-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('engineering-case-studies-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
