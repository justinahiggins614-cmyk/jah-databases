(function(){'use strict';
/* JAH Research Data Management Database generator — jahdb-research-data-management-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-RESEDMS-";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={"Foundations": ["Data Management Plans (Signature Edition)", "File Organization (Signature Edition)", "Documentation (Signature Edition)", "FAIR Principles (Signature Edition)", "Choosing Repositories (Signature Edition)", "Data Sharing (Signature Edition)", "Version Control (Signature Edition)", "Sensitive Data (Signature Edition)", "Teaching RDM (Signature Edition)", "The Project Closeout (Signature Edition)", "Metadata Standards (Signature Edition)"], "Compounded": ["Data Dictionaries (Signature Edition)", "Provenance Tracking (Signature Edition)", "Licensing Data (Signature Edition)", "Embargoes (Signature Edition)", "Data Papers (Signature Edition)", "ORCID and Identity (Signature Edition)", "Collaborative RDM (Signature Edition)", "RDM Tools (Signature Edition)", "Costs of RDM (Signature Edition)", "Long-Term Preservation (Signature Edition)", "Data Rescue (Signature Edition)", "Teaching Data Literacy (Signature Edition)"], "Advanced": ["Institutional Support (Signature Edition)", "Funder Compliance (Signature Edition)", "Journal Requirements (Signature Edition)", "Reproducibility (Signature Edition)", "Data Ethics (Signature Edition)", "Indigenous Data (Signature Edition)", "Metrics for Data (Signature Edition)", "The Data Audit (Signature Edition)", "RDM Maturity (Signature Edition)", "Future of RDM (Signature Edition)", "The RDM Community (Signature Edition)"]};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "#!/usr/bin/env python3\n\"\"\""+safe+" — research guide demo.\nRecord demo. Property of Justin Addam Higgins (JAH).\n\"\"\"\n"
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
    name:topic+' — research guide',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A research guide of "'+topic+'" in '+field+'. Generated sample record are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"research-data-management-signature-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:"jahdb-research-data-management-signature-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("research-data-management-signature",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
