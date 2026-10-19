(function(){'use strict';
/* JAH Signature Physician Profession Database generator — "jahdb-profession-physician-signature-1.0".
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-PMDS-";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={"Foundations": ["What Physicians Do (Signature Edition)", "History of Medicine (Signature Edition)", "Core Clinical Skills (Signature Edition)", "The Education Path: Pre-med to Attending (Signature Edition)", "Licensing and Board Certification (Signature Edition)", "Tools of the Trade (Signature Edition)", "A Day in the Life (Signature Edition)", "Workplaces and Settings (Signature Edition)", "Medical Ethics (Signature Edition)", "Income and Career Outlook (Signature Edition)", "Giants of Medicine (Signature Edition)", "Getting Started: The Pre-med Years (Signature Edition)"], "Compounded": ["Choosing a Specialty (Signature Edition)", "Residency: The Forge (Signature Edition)", "The Differential Diagnosis (Signature Edition)", "The Patient Relationship (Signature Edition)", "The Business of Medicine (Signature Edition)", "Malpractice and Risk (Signature Edition)", "Technology in Medicine (Signature Edition)", "Burnout and Wellness (Signature Edition)", "Leading the Care Team (Signature Edition)", "Boards and Continuing Certification (Signature Edition)", "Subspecialization (Signature Edition)", "The Future of Medicine (Signature Edition)"], "Advanced": ["The Master Clinician (Signature Edition)", "Medical Research (Signature Edition)", "Teaching the Next Generation (Signature Edition)", "Medical Leadership (Signature Edition)", "Global Health (Signature Edition)", "The Physician's Philosophy (Signature Edition)", "Medicine's Impact on Society (Signature Edition)", "The Difficult Conversations (Signature Edition)", "The Physician-Innovator (Signature Edition)", "The Physician's Legacy (Signature Edition)"]};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "#!/usr/bin/env python3\n\"\"\""+safe+" — profession-physician-signature demo.\nRecord demo. Property of Justin Addam Higgins (JAH).\n\"\"\"\n"
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
var gen={version:"jahdb-profession-physician-signature-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("profession-physician-signature",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
