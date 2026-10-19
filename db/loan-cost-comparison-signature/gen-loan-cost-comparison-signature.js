(function(){'use strict';
/* JAH Loan Cost Comparison Database generator — jahdb-loan-cost-comparison-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-LOANCCS-";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={"Foundations": ["APR vs Interest Rate (Signature Edition)", "Reading an Amortization Table (Signature Edition)", "Total Cost Comparison (Signature Edition)", "Origination Fees and Points (Signature Edition)", "Fixed vs Adjustable Rates (Signature Edition)", "Loan Term Trade-offs (Signature Edition)", "Mortgage Shopping (Signature Edition)", "Auto Loan Tactics (Signature Edition)", "Personal Loan Evaluation (Signature Edition)", "Student Loan Strategy (Signature Edition)", "Prepayment Penalties (Signature Edition)"], "Compounded": ["Balloon Payments (Signature Edition)", "Debt-to-Income Ratios (Signature Edition)", "Credit Score Impact (Signature Edition)", "Down Payments (Signature Edition)", "Private Mortgage Insurance (Signature Edition)", "Refinancing Decisions (Signature Edition)", "Biweekly Payment Programs (Signature Edition)", "Loan Disclosure Documents (Signature Edition)", "Predatory Lending Signs (Signature Edition)", "Co-signing Risks (Signature Edition)", "Home Equity Options (Signature Edition)", "Payday and Title Loans (Signature Edition)"], "Advanced": ["Negotiating With Lenders (Signature Edition)", "Loan Servicing Transfers (Signature Edition)", "Escrow Accounts Explained (Signature Edition)", "Default and Hardship Options (Signature Edition)", "Building a Borrowing Plan (Signature Edition)", "Teaching Borrowing Basics (Signature Edition)", "Annual Loan Review (Signature Edition)", "Business Loan Basics (Signature Edition)", "Medical Debt and Loans (Signature Edition)", "Auto Refinance Timing (Signature Edition)", "The Lifetime Borrowing Audit (Signature Edition)"]};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "#!/usr/bin/env python3\n\"\"\""+safe+" — loan guide demo.\nRecord demo. Property of Justin Addam Higgins (JAH).\n\"\"\"\n"
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
    name:topic+' — loan guide',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A loan guide of "'+topic+'" in '+field+'. Generated sample record are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"loan-cost-comparison-signature-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:"jahdb-loan-cost-comparison-signature-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("loan-cost-comparison-signature",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
