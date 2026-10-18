(function(){'use strict';
/* JAH Signature Mercury Database generator — jahdb-mercury-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-MERCS-";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={"Foundations": ["The Iron Heart: The Signature Reading (Signature Edition)", "The 3:2 Spin: The Signature Reading (Signature Edition)", "Ice in the Shadows: The Signature Reading (Signature Edition)", "Caloris: The Signature Reading (Signature Edition)", "The Scarps: The Signature Reading (Signature Edition)", "MESSENGER: The Signature Reading (Signature Edition)", "The Hollows: The Signature Reading (Signature Edition)", "The Magnetosphere: The Signature Reading (Signature Edition)", "BepiColombo: The Signature Reading (Signature Edition)", "The Transit: The Signature Reading (Signature Edition)", "The Exosphere: The Signature Reading (Signature Edition)"], "Compounded": ["The Volatiles: The Signature Reading (Signature Edition)", "The Smooth Plains: The Signature Reading (Signature Edition)", "The Ghost Craters: The Signature Reading (Signature Edition)", "The Polar Deposits: The Signature Reading (Signature Edition)", "The Resonance: The Signature Reading (Signature Edition)", "The Long Day: The Signature Reading (Signature Edition)", "The Sodium Tail: The Signature Reading (Signature Edition)", "The Formation Debate: The Signature Reading (Signature Edition)", "The Gravity Field: The Signature Reading (Signature Edition)", "The Surface Age: The Signature Reading (Signature Edition)", "The Thermal Story: The Signature Reading (Signature Edition)", "The Twin Comparison: The Signature Reading (Signature Edition)"], "Advanced": ["The Interior Model: The Signature Reading (Signature Edition)", "The Dynamo: The Signature Reading (Signature Edition)", "The Orbit's Future: The Signature Reading (Signature Edition)", "The Relativity Lab: The Signature Reading (Signature Edition)", "The Observation Challenge: The Signature Reading (Signature Edition)", "The Names: The Signature Reading (Signature Edition)", "The Heat Budget: The Signature Reading (Signature Edition)", "Venus's Craters: The Signature Reading (Signature Edition)", "Venus's Coming Fleet: The Signature Reading (Signature Edition)", "Why Mercury Endures: The Signature Closing (Signature Edition)", "The 88-Day Year: The Signature Note (Signature Edition)"]};
var KIND="mercury record";
var SRC="signature";
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "#!/usr/bin/env python3\n\"\"\""+safe+" — sample demo.\nRecord demo. Property of Justin Addam Higgins (JAH).\n\"\"\"\n"
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
  var rec={
    id:id,
    name:topic+' — '+KIND,
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A '+KIND+' of "'+topic+'" in '+field+'. Generated sample records are clearly labeled and never presented as archive records.',
    field:field,
    src:SRC,
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"sample-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
    _seed:seed
  };
  if(SRC==='signature')rec.signature_label='Signature original - created in the Signature system; not a public record.';
  return rec;
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
var gen={version:"jahdb-mercury-signature-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("mercury-signature",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
