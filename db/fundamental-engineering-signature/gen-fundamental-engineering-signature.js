(function(){'use strict';
/* JAH Signature Engineering Fundamentals Database generator — "jahdb-fundamental-engineering-signature-1.0".
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-FENS-";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={"Foundations": ["The Engineering Design Process (Signature Edition)", "Units and Measurement (Signature Edition)", "Statics (Signature Edition)", "Materials (Signature Edition)", "Factor of Safety (Signature Edition)", "Sketching (Signature Edition)", "Tolerances (Signature Edition)", "Engineering Disciplines (Signature Edition)", "Engineering Ethics (Signature Edition)", "Estimation (Signature Edition)", "Technical Drawing (Signature Edition)", "Prototyping (Signature Edition)"], "Compounded": ["Dynamics (Signature Edition)", "Thermodynamics (Signature Edition)", "Fluid Mechanics (Signature Edition)", "Electric Circuits (Signature Edition)", "Control Systems (Signature Edition)", "Manufacturing Processes (Signature Edition)", "Project Management (Signature Edition)", "CAD (Signature Edition)", "The FE Exam (Signature Edition)", "Failure Analysis (Signature Edition)", "Optimization (Signature Edition)", "The Engineering Team (Signature Edition)"], "Advanced": ["Systems Engineering (Signature Edition)", "Finite Element Analysis (Signature Edition)", "Digital Twins (Signature Edition)", "Robotics (Signature Edition)", "The Energy Transition (Signature Edition)", "Biomedical Engineering (Signature Edition)", "Teaching Engineering (Signature Edition)", "The PE License (Signature Edition)", "The Megaproject (Signature Edition)", "The Engineering Legacy (Signature Edition)"]};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "#!/usr/bin/env python3\n\"\"\""+safe+" — fundamental-engineering-signature demo.\nRecord demo. Property of Justin Addam Higgins (JAH).\n\"\"\"\n"
   + "TOPIC = \""+safe+"\"\n"
   + "FIELD = \""+field+"\"\n"
   + "def summarize():\n"
   + "    return TOPIC + ' [' + FIELD + ']'\n"
   + "print(summarize())\n"
   + "print('Signature sample — structural sample, not an archive entry.')\n";
}
function generate(seed,opts,rnd){
  opts=opts||{}; rnd=rnd||prng(seed);
  var field=opts.field&&FIELDS.indexOf(opts.field)>=0?opts.field:pick(FIELDS,rnd);
  var pool=TOPICS[field]||["General Study"];
  var topic=pick(pool,rnd);
  var id=PREFIX+String(seed).padStart(6,'0');
  return {
    id:id,
    name:topic+' — Signature-original fundamental record',
    title:topic,
    description:"SAMPLE RECORD (generated \u2014 structural sample). A Signature-original fundamental record study. Signature original samples are clearly labeled and never presented as archive records.",
    field:field,
    src:"signature-sample",
    sample:true,
    disclaimer:"Generated Signature sample \u2014 not an archive record. Seeded archive records are the authoritative entries.",
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
var gen={version:"jahdb-fundamental-engineering-signature-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("fundamental-engineering-signature",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
