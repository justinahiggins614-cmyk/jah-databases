(function(){'use strict';
/* JAH Signature First Aid Database generator — "jahdb-everyday-first-aid-signature-1.0".
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-EFAS-";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={"Foundations": ["Calling 911 (Signature Edition)", "Hands-Only CPR (Signature Edition)", "Choking: 5 and 5 (Signature Edition)", "Severe Bleeding (Signature Edition)", "Recovery Position (Signature Edition)", "Burns (Signature Edition)", "EpiPen for Anaphylaxis (Signature Edition)", "Splinting Fractures (Signature Edition)", "Sprains: RICE (Signature Edition)", "Nosebleeds (Signature Edition)", "Bee Stings (Signature Edition)", "The First Aid Kit (Signature Edition)"], "Compounded": ["Using an AED (Signature Edition)", "Stroke: FAST (Signature Edition)", "Heart Attack (Signature Edition)", "Seizures (Signature Edition)", "Diabetic Emergency (Signature Edition)", "Heat Stroke (Signature Edition)", "Hypothermia (Signature Edition)", "Drowning Response (Signature Edition)", "Child CPR (Signature Edition)", "Infant CPR and Choking (Signature Edition)", "Poisoning (Signature Edition)", "Eye Injuries (Signature Edition)"], "Advanced": ["Tourniquet Use (Signature Edition)", "Improvised First Aid (Signature Edition)", "Recognizing Shock (Signature Edition)", "Spinal Precautions (Signature Edition)", "Snakebites (Signature Edition)", "Biphasic Reactions (Signature Edition)", "Family Emergency Drills (Signature Edition)", "The 72-Hour Go-Bag (Signature Edition)", "CERT Training (Signature Edition)", "Teaching First Aid (Signature Edition)"]};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "#!/usr/bin/env python3\n\"\"\""+safe+" — everyday-first-aid-signature demo.\nRecord demo. Property of Justin Addam Higgins (JAH).\n\"\"\"\n"
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
    name:topic+' — Signature-original everyday record',
    title:topic,
    description:"SAMPLE RECORD (generated \u2014 structural sample). A Signature-original everyday record study. Signature original samples are clearly labeled and never presented as archive records.",
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
var gen={version:"jahdb-everyday-first-aid-signature-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("everyday-first-aid-signature",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
