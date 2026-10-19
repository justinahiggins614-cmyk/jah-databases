(function(){'use strict';
/* JAH Signature Laser Cutting and Engraving Database generator — "jahdb-laser-cutting-engraving-signature-1.0".
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-LASCUS-";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={"Foundations": ["How Laser Cutting Works (Signature Edition)", "Laser Types (CO2, Fiber, Diode) (Signature Edition)", "Laser Safety (Signature Edition)", "Materials and Lasers (Signature Edition)", "Kerf and Tolerances (Signature Edition)", "Cut Quality Basics (Signature Edition)", "Engraving Basics (Signature Edition)"], "Compounded": ["Parameter Development (Signature Edition)", "Nesting and Efficiency (Signature Edition)", "Heat Effects and Distortion (Signature Edition)", "Cutting Metals (Signature Edition)", "Cutting Non-Metals (Signature Edition)", "Joints for Laser-Cut Parts (Signature Edition)", "Fume Extraction (Signature Edition)"], "Advanced": ["Rotary Engraving (Signature Edition)", "3D Laser Effects (Signature Edition)", "Production Laser Workflows (Signature Edition)", "Laser Maintenance (Signature Edition)", "Advanced Materials (Signature Edition)", "The Laser Master Reference (Signature Edition)", "The Laser Cutting and Engraving Capstone Build (Signature Edition)"]};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "#!/usr/bin/env python3\n\"\"\""+safe+" — laser-cutting-engraving-signature demo.\nRecord demo. Property of Justin Addam Higgins (JAH).\n\"\"\"\n"
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
    name:topic+' — Signature-original laser record',
    title:topic,
    description:"SAMPLE RECORD (generated \u2014 structural sample). A Signature-original laser record study. Generated samples are clearly labeled and never presented as archive records.",
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
var gen={version:"jahdb-laser-cutting-engraving-signature-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("laser-cutting-engraving-signature",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
