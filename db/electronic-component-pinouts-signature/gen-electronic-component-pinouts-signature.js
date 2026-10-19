(function(){'use strict';
/* JAH Signature Electronic Component Pinout Database generator — "jahdb-electronic-component-pinouts-signature-1.0".
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-ELECOS-";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={"Foundations": ["Reading a Pinout Diagram (Signature Edition)", "Power and Ground Pins (Signature Edition)", "Common Package Types (Signature Edition)", "Datasheet Pin Tables (Signature Edition)", "Pin 1 Orientation Marks (Signature Edition)", "NC (No-Connect) Pins (Signature Edition)", "Schematic Symbols Must Match Pinouts (Signature Edition)"], "Compounded": ["Multiplexed and Alternate Functions (Signature Edition)", "High-Speed Pin Considerations (Signature Edition)", "Analog Pin Handling (Signature Edition)", "Programming and Debug Interfaces (Signature Edition)", "Power Sequencing Pins (Signature Edition)", "ESD and Protection on Exposed Pins (Signature Edition)", "Pinout Differences Between Variants (Signature Edition)"], "Advanced": ["BGA Pinouts and Fanout (Signature Edition)", "Connector Pinouts and Standards (Signature Edition)", "Differential Pair Pin Assignment (Signature Edition)", "Pinout Verification Checklists (Signature Edition)", "Reverse-Engineering Unknown Pinouts (Signature Edition)", "Pinout Documentation Standards (Signature Edition)", "High-Reliability Pinout Practices (Signature Edition)"]};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "#!/usr/bin/env python3\n\"\"\""+safe+" — electronic-component-pinouts-signature demo.\nRecord demo. Property of Justin Addam Higgins (JAH).\n\"\"\"\n"
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
    name:topic+' — Signature-original component pinout record',
    title:topic,
    description:"SAMPLE RECORD (generated \u2014 structural sample). A Signature-original component pinout record study. Generated samples are clearly labeled and never presented as archive records.",
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
var gen={version:"jahdb-electronic-component-pinouts-signature-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("electronic-component-pinouts-signature",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
