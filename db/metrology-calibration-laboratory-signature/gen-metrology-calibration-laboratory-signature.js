(function(){'use strict';
/* JAH The Metrology and Calibration Laboratory Signature Database generator — jahdb-metrology-calibration-laboratory-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-MCLS-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "What Metrology Is: The Science of Measurement (Signature Edition) \u2014 Foundations",
  "The SI: Seven Base Units (Signature Edition) \u2014 Foundations",
  "Traceability: The Unbroken Chain (Signature Edition) \u2014 Foundations",
  "Calibration vs Adjustment vs Verification (Signature Edition) \u2014 Foundations",
  "Measurement Uncertainty: The Honest Number (Signature Edition) \u2014 Foundations",
  "Type A and Type B Uncertainty (Signature Edition) \u2014 Foundations",
  "The GUM: Guide to Uncertainty (Signature Edition) \u2014 Foundations",
  "Calibration Certificates: Reading Them (Signature Edition) \u2014 Foundations",
  "Reference Standards: The Hierarchy (Signature Edition) \u2014 Foundations",
  "Units and Conversions Done Right (Signature Edition) \u2014 Foundations",
  "Significant Figures and Rounding (Signature Edition) \u2014 Foundations",
  "The Calibration Laboratory: What It Is (Signature Edition) \u2014 Foundations"
 ],
 "Compounded": [
  "Dimensional Calibration: Gauge Blocks (Signature Edition) \u2014 Compounded",
  "Temperature Calibration: Fixed Points and PRTs (Signature Edition) \u2014 Compounded",
  "Pressure Calibration: Deadweight Testers (Signature Edition) \u2014 Compounded",
  "Electrical Calibration: Voltage, Current, Resistance (Signature Edition) \u2014 Compounded",
  "Mass Calibration: From Kilogram to Bench (Signature Edition) \u2014 Compounded",
  "Calibration Intervals: How Often (Signature Edition) \u2014 Compounded",
  "As-Found / As-Left: What Changed (Signature Edition) \u2014 Compounded",
  "Measurement Assurance Programs (Signature Edition) \u2014 Compounded",
  "Interlaboratory Comparisons and En Values (Signature Edition) \u2014 Compounded",
  "ISO/IEC 17025: Competence Requirements (Signature Edition) \u2014 Compounded",
  "CMC: Calibration and Measurement Capability (Signature Edition) \u2014 Compounded",
  "Environmental Controls in the Lab (Signature Edition) \u2014 Compounded"
 ],
 "Advanced": [
  "Uncertainty Budgets in Practice (Signature Edition) \u2014 Advanced",
  "Monte Carlo Uncertainty Evaluation (GUM Supplement 1) (Signature Edition) \u2014 Advanced",
  "Calibration Curve Fitting (Signature Edition) \u2014 Advanced",
  "Drift Analysis and Predictive Intervals (Signature Edition) \u2014 Advanced",
  "Software in Calibration: Validation (Signature Edition) \u2014 Advanced",
  "Dimensional Uncertainty: Thermal Effects (Signature Edition) \u2014 Advanced",
  "Electrical Quantum Standards (Josephson, QHR) (Signature Edition) \u2014 Advanced",
  "Time and Frequency Metrology (Signature Edition) \u2014 Advanced",
  "3D-Printable Calibration Fixtures (Signature Edition) \u2014 Advanced",
  "The National Metrology System: NIST and BIPM (Signature Edition) \u2014 Advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Metrology — "+safe+"\n"
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
    name:topic+' — metrology record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A metrology record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"metrology-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-metrology-calibration-laboratory-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('metrology-calibration-laboratory-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
