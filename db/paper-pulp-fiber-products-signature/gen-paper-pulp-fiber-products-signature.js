(function(){'use strict';
/* JAH Signature Paper Pulp and Fiber Products Database generator — "jahdb-paper-pulp-fiber-products-signature-1.0".
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-PAPPUS-";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={"Foundations": ["Fibers: The Foundation (Signature Edition)", "Pulping Methods (Signature Edition)", "Papermaking Basics (Signature Edition)", "Paper Properties (Signature Edition)", "Recycled Fiber (Signature Edition)", "Paper Grades (Signature Edition)", "Converting Basics (Signature Edition)"], "Compounded": ["Packaging Papers and Board (Signature Edition)", "Printing Papers (Signature Edition)", "Tissue and Towel (Signature Edition)", "Coating and Surface Treatment (Signature Edition)", "Paper Testing (TAPPI) (Signature Edition)", "Process Control (Signature Edition)", "Environmental Aspects (Signature Edition)"], "Advanced": ["Specialty Papers (Signature Edition)", "Nanocellulose and Advanced Fibers (Signature Edition)", "Paper Electronics (Signature Edition)", "Molded Fiber Packaging (Signature Edition)", "The Paper Master Reference (Signature Edition)", "Future of Fiber Products (Signature Edition)", "The Paper Pulp and Fiber Products Capstone Build (Signature Edition)"]};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "#!/usr/bin/env python3\n\"\"\""+safe+" — paper-pulp-fiber-products-signature demo.\nRecord demo. Property of Justin Addam Higgins (JAH).\n\"\"\"\n"
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
    name:topic+' — Signature-original paper record',
    title:topic,
    description:"SAMPLE RECORD (generated \u2014 structural sample). A Signature-original paper record study. Generated samples are clearly labeled and never presented as archive records.",
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
var gen={version:"jahdb-paper-pulp-fiber-products-signature-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("paper-pulp-fiber-products-signature",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
