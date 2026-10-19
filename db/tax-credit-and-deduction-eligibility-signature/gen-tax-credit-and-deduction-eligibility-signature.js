(function(){'use strict';
/* JAH Tax Credit and Deduction Eligibility Database generator — jahdb-tax-credit-and-deduction-eligibility-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-TAXCADS-";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={"Foundations": ["Credits vs Deductions (Signature Edition)", "The Standard Deduction (Signature Edition)", "Earned Income Tax Credit (Signature Edition)", "Child Tax Credit (Signature Edition)", "Education Credits (Signature Edition)", "Retirement Savings Credit (Signature Edition)", "Mortgage Interest Deduction (Signature Edition)", "State and Local Tax Deduction (Signature Edition)", "Charitable Deductions (Signature Edition)", "Medical Expense Deduction (Signature Edition)", "Business Expense Deductions (Signature Edition)"], "Compounded": ["Home Office Deduction (Signature Edition)", "Mileage Deductions (Signature Edition)", "HSA and FSA Benefits (Signature Edition)", "IRA Deduction Rules (Signature Edition)", "Student Loan Interest (Signature Edition)", "Energy Credits (Signature Edition)", "Dependent Care Credit (Signature Edition)", "Filing Status Choices (Signature Edition)", "Withholding Tune-Ups (Signature Edition)", "Estimated Tax Payments (Signature Edition)", "Record-Keeping Systems (Signature Edition)", "Free Filing Options (Signature Edition)"], "Advanced": ["Audit Triggers and Defense (Signature Edition)", "Amending Returns (Signature Edition)", "Tax Scams (Signature Edition)", "Year-End Tax Moves (Signature Edition)", "Life Changes and Taxes (Signature Edition)", "Side Income Reporting (Signature Edition)", "Teaching Tax Basics (Signature Edition)", "The Annual Tax Review (Signature Edition)", "State Tax Differences (Signature Edition)", "Retirement Tax Planning (Signature Edition)", "Estate and Gift Basics (Signature Edition)"]};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "#!/usr/bin/env python3\n\"\"\""+safe+" — tax guide demo.\nRecord demo. Property of Justin Addam Higgins (JAH).\n\"\"\"\n"
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
    name:topic+' — tax guide',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A tax guide of "'+topic+'" in '+field+'. Generated sample record are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"tax-credit-and-deduction-eligibility-signature-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:"jahdb-tax-credit-and-deduction-eligibility-signature-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("tax-credit-and-deduction-eligibility-signature",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
