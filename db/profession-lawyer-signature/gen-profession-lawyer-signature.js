(function(){'use strict';
/* JAH Signature Lawyer Profession Database generator — "jahdb-profession-lawyer-signature-1.0".
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-PLWS-";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={"Foundations": ["What Lawyers Do (Signature Edition)", "History of the Legal Profession (Signature Edition)", "Core Legal Skills (Signature Edition)", "Law School and the Bar (Signature Edition)", "Bar Admission (Signature Edition)", "Tools of the Trade (Signature Edition)", "A Day in the Life (Signature Edition)", "Firms and Practice Settings (Signature Edition)", "Legal Ethics: The Model Rules (Signature Edition)", "Pay and Career Outlook (Signature Edition)", "Giants of the Law (Signature Edition)", "Getting Started (Signature Edition)"], "Compounded": ["Litigation: The Courtroom (Signature Edition)", "Trial Advocacy (Signature Edition)", "Corporate and M&A (Signature Edition)", "Public Interest Law (Signature Edition)", "Criminal Law: Prosecution and Defense (Signature Edition)", "In-House Counsel (Signature Edition)", "The Judiciary (Signature Edition)", "Legal Writing Mastery (Signature Edition)", "Rainmaking and Business Development (Signature Edition)", "Solo Practice (Signature Edition)", "Legal Specialties (Signature Edition)", "The Future: AI and Access to Justice (Signature Edition)"], "Advanced": ["Appellate Advocacy (Signature Edition)", "The Master Dealmaker (Signature Edition)", "The Master Trial Lawyer (Signature Edition)", "The General Counsel (Signature Edition)", "The Law Professor (Signature Edition)", "The Clerkship (Signature Edition)", "The Lawyer-Statesman (Signature Edition)", "Teaching the Law (Signature Edition)", "The Lawyer's Legacy (Signature Edition)", "The Lawyer's Philosophy (Signature Edition)"]};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "#!/usr/bin/env python3\n\"\"\""+safe+" — profession-lawyer-signature demo.\nRecord demo. Property of Justin Addam Higgins (JAH).\n\"\"\"\n"
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
var gen={version:"jahdb-profession-lawyer-signature-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("profession-lawyer-signature",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
