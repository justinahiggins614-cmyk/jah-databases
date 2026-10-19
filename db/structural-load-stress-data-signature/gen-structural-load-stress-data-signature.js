(function(){'use strict';
/* JAH Signature Structural Load and Stress Database generator — "jahdb-structural-load-stress-data-signature-1.0".
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-STRLOS-";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={"Foundations": ["Types of Loads (Signature Edition)", "Load Combinations (Signature Edition)", "Stress, Strain, and Strength (Signature Edition)", "Allowable Stress Design (Signature Edition)", "Load and Resistance Factor Design (Signature Edition)", "Free-Body Diagrams (Signature Edition)", "Beams: Bending and Shear (Signature Edition)"], "Compounded": ["Columns and Buckling (Signature Edition)", "Connections (Signature Edition)", "Trusses (Signature Edition)", "Frames and Moment Connections (Signature Edition)", "Foundations (Signature Edition)", "Wind Loads (Signature Edition)", "Seismic Loads (Signature Edition)"], "Advanced": ["Finite Element Basics (Signature Edition)", "Fatigue Analysis (Signature Edition)", "Dynamic Analysis (Signature Edition)", "Structural Optimization (Signature Edition)", "Failure Investigation (Signature Edition)", "The Structural Checklist (Signature Edition)", "The Structural Load and Stress Capstone Build (Signature Edition)"]};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "#!/usr/bin/env python3\n\"\"\""+safe+" — structural-load-stress-data-signature demo.\nRecord demo. Property of Justin Addam Higgins (JAH).\n\"\"\"\n"
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
    name:topic+' — Signature-original structural record',
    title:topic,
    description:"SAMPLE RECORD (generated \u2014 structural sample). A Signature-original structural record study. Generated samples are clearly labeled and never presented as archive records.",
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
var gen={version:"jahdb-structural-load-stress-data-signature-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("structural-load-stress-data-signature",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
