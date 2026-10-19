(function(){'use strict';
/* JAH Signature Injection Molding and Mold Design Database generator — "jahdb-injection-molding-design-signature-1.0".
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-INJMOS-";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={"Foundations": ["How Injection Molding Works (Signature Edition)", "Wall Thickness (Signature Edition)", "Draft Angles (Signature Edition)", "Ribs and Bosses (Signature Edition)", "Parting Lines (Signature Edition)", "Material Selection Basics (Signature Edition)", "Mold Basics: Cavity and Core (Signature Edition)"], "Compounded": ["Gating Design (Signature Edition)", "Cooling System Design (Signature Edition)", "Ejection Design (Signature Edition)", "Shrinkage and Tolerances (Signature Edition)", "Weld Lines and Flow Defects (Signature Edition)", "Mold Materials and Construction (Signature Edition)", "Process Windows and Control (Signature Edition)"], "Advanced": ["Multi-Cavity and Family Molds (Signature Edition)", "Insert Molding and Overmolding (Signature Edition)", "Mold Flow Simulation (Signature Edition)", "Tooling Cost Estimation (Signature Edition)", "Sustainable Molding (Signature Edition)", "The Molding Master Checklist (Signature Edition)", "The Injection Molding and Mold Design Capstone Build (Signature Edition)"]};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "#!/usr/bin/env python3\n\"\"\""+safe+" — injection-molding-design-signature demo.\nRecord demo. Property of Justin Addam Higgins (JAH).\n\"\"\"\n"
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
    name:topic+' — Signature-original injection molding record',
    title:topic,
    description:"SAMPLE RECORD (generated \u2014 structural sample). A Signature-original injection molding record study. Generated samples are clearly labeled and never presented as archive records.",
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
var gen={version:"jahdb-injection-molding-design-signature-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("injection-molding-design-signature",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
