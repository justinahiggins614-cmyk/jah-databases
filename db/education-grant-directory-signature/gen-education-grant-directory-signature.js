(function(){'use strict';
/* JAH Education Grant Directory Database generator — jahdb-education-grant-directory-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-EDUCGDS-";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={"Foundations": ["FAFSA Fundamentals (Signature Edition)", "Pell Grants (Signature Edition)", "State Grant Programs (Signature Edition)", "Scholarship Searching (Signature Edition)", "Application Strategy (Signature Edition)", "Essay Writing (Signature Edition)", "Recommendation Letters (Signature Edition)", "Work-Study Programs (Signature Edition)", "Employer Tuition Help (Signature Edition)", "Military Education Benefits (Signature Edition)", "Adult Learner Aid (Signature Edition)"], "Compounded": ["Community College Value (Signature Edition)", "Avoiding Scholarship Scams (Signature Edition)", "Tax Benefits for Education (Signature Edition)", "Appealing Aid Decisions (Signature Edition)", "Maintaining Eligibility (Signature Edition)", "Graduate School Funding (Signature Edition)", "Trade School Funding (Signature Edition)", "Study Abroad Funding (Signature Edition)", "The Annual Aid Cycle (Signature Edition)", "Teaching Aid Literacy (Signature Edition)", "Net Price Calculators (Signature Edition)", "Comparing Aid Offers (Signature Edition)"], "Advanced": ["Outside Scholarships and Aid (Signature Edition)", "Dependency Status (Signature Edition)", "Professional Judgment (Signature Edition)", "Satisfactory Academic Progress Appeals (Signature Edition)", "Transfer Student Aid (Signature Edition)", "Part-Time Student Aid (Signature Edition)", "Second Degree Aid (Signature Edition)", "Study Abroad Credits (Signature Edition)", "Gap Year Planning (Signature Edition)", "Homeschooler Aid (Signature Edition)", "Foster Youth Aid (Signature Edition)"]};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "#!/usr/bin/env python3\n\"\"\""+safe+" — grant guide demo.\nRecord demo. Property of Justin Addam Higgins (JAH).\n\"\"\"\n"
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
    name:topic+' — grant guide',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A grant guide of "'+topic+'" in '+field+'. Generated sample record are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"education-grant-directory-signature-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:"jahdb-education-grant-directory-signature-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("education-grant-directory-signature",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
