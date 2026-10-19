(function(){'use strict';
/* JAH Signature Safety-Critical Verification Database generator — "jahdb-safety-critical-verification-signature-1.0".
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-SAFCRS-";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={"Foundations": ["Safety vs Functionality (Signature Edition)", "Hazards and Hazard Analysis (Signature Edition)", "Safe States (Signature Edition)", "Independence in Safety Verification (Signature Edition)", "Fault Injection Testing (Signature Edition)", "Safety Requirements Traceability (Signature Edition)", "Common Cause Failures (Signature Edition)"], "Compounded": ["Safety Integrity Levels (SIL/ASIL) (Signature Edition)", "FMEDA: Failure Modes Effects and Diagnostic Analysis (Signature Edition)", "Proof Testing (Signature Edition)", "Safety-Critical Software Verification (Signature Edition)", "Hardware Fault Tolerance (Signature Edition)", "Safety Cases (Signature Edition)", "Change Impact on Safety (Signature Edition)"], "Advanced": ["STPA: Systems-Theoretic Analysis (Signature Edition)", "Formal Methods for Safety (Signature Edition)", "Safety of Autonomous Systems (Signature Edition)", "Security-Safety Co-Verification (Signature Edition)", "Safety Culture and Organization (Signature Edition)", "The Safety Verification Master Plan (Signature Edition)", "The Safety-Critical Verification Capstone Build (Signature Edition)"]};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "#!/usr/bin/env python3\n\"\"\""+safe+" — safety-critical-verification-signature demo.\nRecord demo. Property of Justin Addam Higgins (JAH).\n\"\"\"\n"
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
    name:topic+' — Signature-original safety verification record',
    title:topic,
    description:"SAMPLE RECORD (generated \u2014 structural sample). A Signature-original safety verification record study. Generated samples are clearly labeled and never presented as archive records.",
    field:field,
    src:"signature-sample",
    sample:true,
    disclaimer:"Generated sample record \u2014 not an archive record. Seeded archive records are the authoritative entries.",
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
var gen={version:"jahdb-safety-critical-verification-signature-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("safety-critical-verification-signature",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
