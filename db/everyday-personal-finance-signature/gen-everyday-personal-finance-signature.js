(function(){'use strict';
/* JAH Signature Personal Finance Database generator — "jahdb-everyday-personal-finance-signature-1.0".
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-EPFS-";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={"Foundations": ["Budgeting: 50/30/20 (Signature Edition)", "Emergency Fund (Signature Edition)", "Paying Off Debt: Snowball (Signature Edition)", "Credit Score Basics (Signature Edition)", "401(k) and the Match (Signature Edition)", "Roth IRA (Signature Edition)", "Index Fund Investing (Signature Edition)", "Compound Interest (Signature Edition)", "Term Life Insurance (Signature Edition)", "Writing a Will (Signature Edition)", "Health Savings Account (Signature Edition)", "Your Retirement Number (Signature Edition)"], "Compounded": ["Mortgage Basics (Signature Edition)", "Buying a Car Wisely (Signature Edition)", "Saving for College: 529 (Signature Edition)", "Side Hustle Finances (Signature Edition)", "Tax Bracket Basics (Signature Edition)", "Negotiating Salary (Signature Edition)", "Fraud Protection (Signature Edition)", "Estate Planning Basics (Signature Edition)", "Charitable Giving (Signature Edition)", "Starting an LLC (Signature Edition)", "Rental Property Basics (Signature Edition)", "FIRE Movement (Signature Edition)"], "Advanced": ["Roth Conversion Ladder (Signature Edition)", "Backdoor Roth (Signature Edition)", "HSA as Retirement Account (Signature Edition)", "72(t) Early Withdrawals (Signature Edition)", "Revocable Living Trust (Signature Edition)", "Qualified Charitable Distributions (Signature Edition)", "Annuities: The Fine Print (Signature Edition)", "Generational Wealth (Signature Edition)", "Retirement Withdrawal Strategy (Signature Edition)", "Defining Enough (Signature Edition)"]};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "#!/usr/bin/env python3\n\"\"\""+safe+" — everyday-personal-finance-signature demo.\nRecord demo. Property of Justin Addam Higgins (JAH).\n\"\"\"\n"
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
    name:topic+' — Signature-original everyday record',
    title:topic,
    description:"SAMPLE RECORD (generated \u2014 structural sample). A Signature-original everyday record study. Signature original samples are clearly labeled and never presented as archive records.",
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
var gen={version:"jahdb-everyday-personal-finance-signature-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("everyday-personal-finance-signature",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
