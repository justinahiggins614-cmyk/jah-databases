(function(){'use strict';
/* JAH Workplace Accommodation Processes Database generator — jahdb-workplace-accommodation-processes-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-WORKAPS-";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={"Foundations": ["Know Your Rights Basics (Signature Edition)", "Documenting Your Needs (Signature Edition)", "Writing the Request (Signature Edition)", "The Interactive Process (Signature Edition)", "Common Accommodations (Signature Edition)", "Schedule Modifications (Signature Edition)", "Equipment and Technology (Signature Edition)", "Remote Work Requests (Signature Edition)", "Service Animals at Work (Signature Edition)", "Pregnancy Accommodations (Signature Edition)", "Religious Accommodations (Signature Edition)"], "Compounded": ["Mental Health Accommodations (Signature Edition)", "Temporary Accommodations (Signature Edition)", "The Medical Inquiry Limits (Signature Edition)", "When Requests Are Denied (Signature Edition)", "Retaliation Protection (Signature Edition)", "Confidentiality Rights (Signature Edition)", "Accommodations in Hiring (Signature Edition)", "Performance and Accommodations (Signature Edition)", "Union and Collective Bargaining (Signature Edition)", "Small Employer Realities (Signature Edition)", "Government Employees (Signature Edition)", "State Law Enhancements (Signature Edition)"], "Advanced": ["Documenting Everything (Signature Edition)", "JAN and Free Resources (Signature Edition)", "Working With Your Doctor (Signature Edition)", "Accommodation Reviews (Signature Edition)", "Leaving a Job Well (Signature Edition)", "Supporting a Colleague (Signature Edition)", "Remote Accommodation Tech (Signature Edition)", "The Annual Rights Refresh (Signature Edition)", "Teaching Self-Advocacy (Signature Edition)", "Systemic Advocacy (Signature Edition)"]};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "#!/usr/bin/env python3\n\"\"\""+safe+" — accommodation guide demo.\nRecord demo. Property of Justin Addam Higgins (JAH).\n\"\"\"\n"
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
    name:topic+' — accommodation guide',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A accommodation guide of "'+topic+'" in '+field+'. Generated sample record are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"workplace-accommodation-processes-signature-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:"jahdb-workplace-accommodation-processes-signature-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("workplace-accommodation-processes-signature",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
