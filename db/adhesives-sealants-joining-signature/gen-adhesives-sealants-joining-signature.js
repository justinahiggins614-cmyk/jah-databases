(function(){'use strict';
/* JAH Signature Adhesives and Joining Database generator — "jahdb-adhesives-sealants-joining-signature-1.0".
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-ADHSES-";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={"Foundations": ["How Adhesive Bonding Works (Signature Edition)", "Adhesive Families (Signature Edition)", "Surface Preparation (Signature Edition)", "Joint Design for Adhesives (Signature Edition)", "Sealant Basics (Signature Edition)", "Cure and Processing (Signature Edition)", "Testing Bonded Joints (Signature Edition)"], "Compounded": ["Structural Bonding (Signature Edition)", "Bonding Different Substrates (Signature Edition)", "Environmental Durability (Signature Edition)", "Disassembly and Repair (Signature Edition)", "Sealant Joint Design (Signature Edition)", "Adhesive Selection Methodology (Signature Edition)", "Process Control for Bonding (Signature Edition)"], "Advanced": ["NDT for Bonded Joints (Signature Edition)", "Bonded Composite Structures (Signature Edition)", "Accelerated Aging and Life Prediction (Signature Edition)", "Adhesive Failure Analysis (Signature Edition)", "Sustainable Bonding (Signature Edition)", "The Bonding Master Checklist (Signature Edition)", "The Adhesives and Joining Capstone Build (Signature Edition)"]};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "#!/usr/bin/env python3\n\"\"\""+safe+" — adhesives-sealants-joining-signature demo.\nRecord demo. Property of Justin Addam Higgins (JAH).\n\"\"\"\n"
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
    name:topic+' — Signature-original adhesive record',
    title:topic,
    description:"SAMPLE RECORD (generated \u2014 structural sample). A Signature-original adhesive record study. Generated samples are clearly labeled and never presented as archive records.",
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
var gen={version:"jahdb-adhesives-sealants-joining-signature-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("adhesives-sealants-joining-signature",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
