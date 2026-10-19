(function(){'use strict';
/* JAH Quality Control Essentials Database generator — jahdb-quality-control-essentials-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-QUALCES-";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={"Foundations": ["Defining Quality (Signature Edition)", "Measurement Systems (Signature Edition)", "Statistical Process Control (Signature Edition)", "Control Charts (Signature Edition)", "Process Capability (Signature Edition)", "Inspection (Signature Edition)", "Root Cause Analysis (Signature Edition)", "Corrective Action (Signature Edition)", "Mistake-Proofing (Signature Edition)", "Six Sigma Basics (Signature Edition)", "Lean and Quality (Signature Edition)"], "Compounded": ["Cost of Quality (Signature Edition)", "Supplier Quality (Signature Edition)", "Quality Culture (Signature Edition)", "Audits (Signature Edition)", "Teaching Quality (Signature Edition)", "The Quality Review (Signature Edition)", "Quality Planning (Signature Edition)", "Design of Experiments (Signature Edition)", "Reliability Engineering (Signature Edition)", "Failure Analysis (Signature Edition)", "Calibration (Signature Edition)", "Document Control (Signature Edition)"], "Advanced": ["Training (Signature Edition)", "Management Review (Signature Edition)", "Continuous Improvement (Signature Edition)", "Benchmarking (Signature Edition)", "Quality Tools (Signature Edition)", "FMEA (Signature Edition)", "Customer Feedback (Signature Edition)", "Quality in Services (Signature Edition)", "Regulatory Quality (Signature Edition)", "The Quality Career (Signature Edition)", "Celebrating Quality (Signature Edition)"]};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "#!/usr/bin/env python3\n\"\"\""+safe+" — quality guide demo.\nRecord demo. Property of Justin Addam Higgins (JAH).\n\"\"\"\n"
   + "TOPIC = \""+safe+"\"\n"
   + "FIELD = \""+field+"\"\n"
   + "def summarize():\n"
   + "    return TOPIC + ' [' + FIELD + ']'\n"
   + "print(summarize())\n"
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
    name:topic+' — quality guide',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A quality guide of "'+topic+'" in '+field+'. Generated sample record are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"quality-control-essentials-signature-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:"jahdb-quality-control-essentials-signature-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("quality-control-essentials-signature",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
