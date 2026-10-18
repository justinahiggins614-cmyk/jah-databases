(function(){'use strict';
/* JAH The Public Grants Funding Signature Database generator — jahdb-public-grants-funding-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-GRANTFUND-SIG-";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={"Foundations": ["Federal Grant Basics and Grants.gov (Signature Edition)", "State Grant Programs (Signature Edition)", "Formula Grants (Signature Edition)", "Discretionary and Project Grants (Signature Edition)", "Block Grants (Signature Edition)", "Matching Requirements (Signature Edition)", "Eligibility Determination (Signature Edition)", "SAM.gov Registration (Signature Edition)", "The Unique Entity Identifier (UEI) (Signature Edition)", "Application Narratives (Signature Edition)", "Grant Budget Development (Signature Edition)", "Indirect Cost Rates (Signature Edition)"], "Compounded": ["Cost Sharing and Match Documentation (Signature Edition)", "Grant Review and Scoring (Signature Edition)", "Notices of Award (Signature Edition)", "Period of Performance (Signature Edition)", "Allowable and Unallowable Costs (Signature Edition)", "Uniform Guidance: 2 CFR Part 200 (Signature Edition)", "Procurement Standards for Grantees (Signature Edition)", "Subrecipient Monitoring (Signature Edition)", "Payment Management and Drawdowns (Signature Edition)", "Continuation Applications (Signature Edition)", "No-Cost Extensions (Signature Edition)", "Carryover of Funds (Signature Edition)"], "Advanced": ["The Single Audit (Signature Edition)", "Federal Financial Reporting (SF-425) (Signature Edition)", "Performance Reporting (Signature Edition)", "Grant Closeout Procedures (Signature Edition)", "Grant Fraud Prevention (Signature Edition)", "Program Income (Signature Edition)", "Equipment Disposition (Signature Edition)", "Record Retention for Grants (Signature Edition)", "Debarment and Suspension Checks (Signature Edition)", "Cost Principles: Direct vs Indirect (Signature Edition)"]};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Grant Funding Study — "+safe+"\n"
   + "# Field: "+field+"\n"
   + "record = {'title': \""+safe+"\", 'field': \""+field+"\"}\n"
   + "def summarize(r):\n"
   + "    return r['title'] + ' [' + r['field'] + ']'\n"
   + "print(summarize(record))\n"
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
    name:topic+' — grant funding record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A grant funding record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"grant-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:"jahdb-public-grants-funding-signature-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("public-grants-funding-signature",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
