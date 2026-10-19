(function(){'use strict';
/* JAH Unemployment Benefit Navigation Database generator — jahdb-unemployment-benefit-navigation-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-UNEMBNS-";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={"Foundations": ["Filing Immediately (Signature Edition)", "Eligibility Basics (Signature Edition)", "Gathering Employment Records (Signature Edition)", "The Application Process (Signature Edition)", "Weekly Certifications (Signature Edition)", "Work Search Requirements (Signature Edition)", "Benefit Amount Math (Signature Edition)", "Part-Time Work Rules (Signature Edition)", "Severance Interactions (Signature Edition)", "Appealing Denials (Signature Edition)", "Overpayment Notices (Signature Edition)"], "Compounded": ["Identity Verification (Signature Edition)", "Job Search Strategy (Signature Edition)", "Resume Refresh (Signature Edition)", "Interview Preparation (Signature Edition)", "Skill Building During Benefits (Signature Edition)", "Networking While Unemployed (Signature Edition)", "Freelance and Gig Income (Signature Edition)", "Health Insurance Gap (Signature Edition)", "Budgeting on Benefits (Signature Edition)", "Mental Health During Transition (Signature Edition)", "Avoiding Scams (Signature Edition)", "State Program Differences (Signature Edition)"], "Advanced": ["Reemployment Services (Signature Edition)", "Relocation Considerations (Signature Edition)", "Documentation Discipline (Signature Edition)", "When Benefits Exhaust (Signature Edition)", "Teaching Benefit Literacy (Signature Edition)", "Returning to Work (Signature Edition)", "Taxes on Benefits (Signature Edition)", "The Annual Career Review (Signature Edition)", "Benefit Year Planning (Signature Edition)", "Working With Caseworkers (Signature Edition)", "Building the Emergency Fund Next (Signature Edition)"]};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "#!/usr/bin/env python3\n\"\"\""+safe+" — benefits guide demo.\nRecord demo. Property of Justin Addam Higgins (JAH).\n\"\"\"\n"
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
    name:topic+' — benefits guide',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A benefits guide of "'+topic+'" in '+field+'. Generated sample record are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"unemployment-benefit-navigation-signature-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:"jahdb-unemployment-benefit-navigation-signature-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("unemployment-benefit-navigation-signature",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
