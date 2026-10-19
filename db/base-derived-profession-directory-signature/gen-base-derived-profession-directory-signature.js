(function(){'use strict';
/* JAH Signature Profession Directory Database generator — "jahdb-base-derived-profession-directory-signature-1.0".
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-BPDS-";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={"Foundations": ["The Profession Directory (Signature Edition)", "How to Use This Directory (Signature Edition)", "Members: Physician and Nurse (Signature Edition)", "Member: Teacher (Signature Edition)", "Member: Software Engineer (Signature Edition)", "Members: Electrician, Plumber, Carpenter (Signature Edition)", "Members: Chef and Farmer (Signature Edition)", "Member: Firefighter (Signature Edition)", "Members: Lawyer and Architect (Signature Edition)", "Public vs Signature Editions in the Directory (Signature Edition)", "The Sector Map (Signature Edition)", "Choosing: Three Questions (Signature Edition)"], "Compounded": ["Apprenticeship Paths (Signature Edition)", "Licensing Across Professions (Signature Edition)", "Salary Comparisons (Signature Edition)", "Career Switching (Signature Edition)", "The Medical Path (Signature Edition)", "The Teaching Path (Signature Edition)", "The Tech Path (Signature Edition)", "The Trades Path (Signature Edition)", "The Chef's Path (Signature Edition)", "The Farmer's Path (Signature Edition)", "The Service Path (Signature Edition)", "The Resume Build (Signature Edition)"], "Advanced": ["The Law and Design Path (Signature Edition)", "The Future of Work (Signature Edition)", "The Master Career Plan (Signature Edition)", "The Portfolio Career (Signature Edition)", "Mentorship (Signature Edition)", "The Second Act (Signature Edition)", "The Directory as Counselor (Signature Edition)", "Cross-DB Verification for Careers (Signature Edition)", "The Career Dossier (Signature Edition)", "The Profession Directory Legacy (Signature Edition)"]};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "#!/usr/bin/env python3\n\"\"\""+safe+" — base-derived-profession-directory-signature demo.\nRecord demo. Property of Justin Addam Higgins (JAH).\n\"\"\"\n"
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
    name:topic+' — Signature-original directory record',
    title:topic,
    description:"SAMPLE RECORD (generated \u2014 structural sample). A Signature-original directory record study. Signature original samples are clearly labeled and never presented as archive records.",
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
var gen={version:"jahdb-base-derived-profession-directory-signature-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("base-derived-profession-directory-signature",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
