(function(){'use strict';
/* JAH The Calibration and Adjustment Instructions Database generator — jahdb-calibration-adjustment-instructions-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-CLBR-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "Calibration Hierarchy and Traceability - Reference Standards",
  "Reference Standard Care and Handling - Reference Standards",
  "Calibration Interval Determination - Reference Standards",
  "As-Found / As-Left Documentation - Calibration Procedures",
  "Digital Multimeter Calibration - Calibration Procedures",
  "Caliper and Micrometer Calibration - Calibration Procedures",
  "Pressure Gauge Calibration - Calibration Procedures",
  "Temperature Sensor Calibration - Calibration Procedures",
  "Scale and Balance Calibration - Calibration Procedures",
  "Torque Wrench Calibration - Calibration Procedures"
 ],
 "Compounded": [
  "Oscilloscope Calibration - Calibration Procedures",
  "Flow Meter Calibration - Calibration Procedures",
  "pH Meter Calibration - Calibration Procedures",
  "Tachometer Calibration - Calibration Procedures",
  "Force Gauge Calibration - Calibration Procedures",
  "Dimensional Gauge Block Comparison - Reference Standards",
  "Tolerance Stack-Up Basics - Tolerances & Uncertainty",
  "Measurement Uncertainty Estimation - Tolerances & Uncertainty",
  "Pass/Fail Decision Rules - Tolerances & Uncertainty",
  "Adjustment of Zero and Span - Calibration Procedures",
  "Hysteresis Testing - Verification",
  "Repeatability Testing - Verification"
 ],
 "Advanced": [
  "Accredited Laboratory Requirements - Reference Standards",
  "Inter-Laboratory Comparisons - Verification",
  "Calibration of Data Acquisition Systems - Calibration Procedures",
  "RF Power Sensor Calibration - Calibration Procedures",
  "Vibration Sensor Calibration - Calibration Procedures",
  "Humidity Chamber Calibration - Calibration Procedures",
  "Automated Calibration Systems - Calibration Procedures",
  "Out-of-Tolerance Response Procedure - Tolerances & Uncertainty",
  "Guard-Banding for Decision Rules - Tolerances & Uncertainty",
  "Software-Controlled Instrument Adjustment - Calibration Procedures",
  "Calibration Certificate Requirements - Verification",
  "Measurement Audit Procedure - Verification"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Calibration Adjustment Instructions — "+safe+"\n"
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
    name:topic+' — calibration instruction record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A calibration instruction record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
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
var gen={version:'jahdb-calibration-adjustment-instructions-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('calibration-adjustment-instructions',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
