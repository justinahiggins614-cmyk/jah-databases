(function(){'use strict';
/* JAH Signature Firefighter Profession Database generator — "jahdb-profession-firefighter-signature-1.0".
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-PFFS-";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={"Foundations": ["What Firefighters Do (Signature Edition)", "History of the Fire Service (Signature Edition)", "Core Fireground Skills (Signature Edition)", "The Academy Path (Signature Edition)", "Certification: Firefighter I/II (Signature Edition)", "Tools of the Trade (Signature Edition)", "A Day in the Life: The Shift (Signature Edition)", "Career, Volunteer, and Wildland (Signature Edition)", "The Firefighter's Oath (Signature Edition)", "Pay and Career Outlook (Signature Edition)", "Heroes of the Service (Signature Edition)", "Getting Started (Signature Edition)"], "Compounded": ["The Engine Company (Signature Edition)", "The Ladder Company (Signature Edition)", "Technical Rescue (Signature Edition)", "Fire-Based EMS (Signature Edition)", "The Fire Officer (Signature Edition)", "The Fire Chief (Signature Edition)", "Fire Prevention and Investigation (Signature Edition)", "Hazardous Materials (Signature Edition)", "Wildland Firefighting (Signature Edition)", "Firefighter Health and Wellness (Signature Edition)", "Firehouse Culture (Signature Edition)", "The Future: Community Risk Reduction (Signature Edition)"], "Advanced": ["Incident Command System (Signature Edition)", "Fire Behavior Science (Signature Edition)", "Mayday and RIT (Signature Edition)", "Arson Investigation (Signature Edition)", "Teaching the Service (Signature Edition)", "The Chief's Legacy (Signature Edition)", "The Firefighter's Philosophy (Signature Edition)", "The Service's Impact (Signature Edition)", "The Fallen Remembered (Signature Edition)", "The Firefighter's Life (Signature Edition)"]};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "#!/usr/bin/env python3\n\"\"\""+safe+" — profession-firefighter-signature demo.\nRecord demo. Property of Justin Addam Higgins (JAH).\n\"\"\"\n"
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
    name:topic+' — Signature-original profession record',
    title:topic,
    description:"SAMPLE RECORD (generated \u2014 structural sample). A Signature-original profession record study. Signature original samples are clearly labeled and never presented as archive records.",
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
var gen={version:"jahdb-profession-firefighter-signature-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("profession-firefighter-signature",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
