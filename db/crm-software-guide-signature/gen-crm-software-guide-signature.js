(function(){'use strict';
/* JAH Signature CRM Software Database generator — "jahdb-crm-software-guide-signature-1.0".
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-CRMSOS-";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={"Foundations": ["What CRM Does (Signature Edition)", "Contacts and History (Signature Edition)", "Sales Pipeline Basics (Signature Edition)", "Choosing a CRM (Signature Edition)", "Data Migration (Signature Edition)", "User Adoption (Signature Edition)", "Basic Reporting (Signature Edition)"], "Compounded": ["Marketing Integration (Signature Edition)", "Customer Service CRM (Signature Edition)", "Automation and Workflows (Signature Edition)", "Lead Management (Signature Edition)", "Segmentation (Signature Edition)", "Integrations (Signature Edition)", "Data Quality (Signature Edition)"], "Advanced": ["Analytics and Forecasting (Signature Edition)", "Enterprise CRM (Signature Edition)", "Industry-Specific CRM (Signature Edition)", "AI in CRM (Signature Edition)", "The CRM Master Reference (Signature Edition)", "Future of Relationships (Signature Edition)", "The CRM Software Power-User Setup (Signature Edition)"]};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "#!/usr/bin/env python3\n\"\"\""+safe+" — crm-software-guide-signature demo.\nRecord demo. Property of Justin Addam Higgins (JAH).\n\"\"\"\n"
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
    name:topic+' — Signature-original CRM software record',
    title:topic,
    description:"SAMPLE RECORD (generated \u2014 structural sample). A Signature-original CRM software record study. Generated samples are clearly labeled and never presented as archive records.",
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
var gen={version:"jahdb-crm-software-guide-signature-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("crm-software-guide-signature",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
