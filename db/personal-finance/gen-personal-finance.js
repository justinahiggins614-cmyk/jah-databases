(function(){'use strict';
/* JAH The Personal Finance Database generator — jahdb-personal-finance-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-PFIN-";
var FIELDS=["Money Foundations","Budgeting & Saving","Debt & Credit","Banking Basics","Insurance Basics","Investing Basics"];
var TOPICS={
 "Money Foundations": [
  "What Money Is For: Defining Your Financial Values - Money Foundations",
  "Net Worth: Your Real Financial Scorecard - Money Foundations",
  "The Emergency Fund: Your Financial Airbag - Money Foundations",
  "Pay Yourself First: The Automation Principle - Money Foundations",
  "Needs vs Wants: The Spending Filter - Money Foundations",
  "Financial Goals: Short, Medium, and Long Term - Money Foundations"
 ],
 "Budgeting & Saving": [
  "Zero-Based Budgeting: Every Dollar Has a Job - Budgeting & Saving",
  "The 50/30/20 Budget Framework - Budgeting & Saving",
  "Tracking Spending: Finding Your Leaks - Budgeting & Saving",
  "Cutting Costs Without Cutting Joy - Budgeting & Saving",
  "Saving for Big Purchases - Budgeting & Saving",
  "Teaching Kids About Money - Budgeting & Saving"
 ],
 "Debt & Credit": [
  "Good Debt vs Bad Debt - Debt & Credit",
  "The Debt Snowball and Avalanche - Debt & Credit",
  "Credit Scores: What They Are and How to Build Them - Debt & Credit",
  "Credit Cards: Tool or Trap - Debt & Credit",
  "Getting Out of Debt: The Full Campaign - Debt & Credit",
  "Dealing With Collectors and Old Debts - Debt & Credit"
 ],
 "Banking Basics": [
  "Choosing Bank Accounts - Banking Basics",
  "Overdrafts, Fees, and How to Avoid Them - Banking Basics",
  "Direct Deposit, Autopay, and Alerts - Banking Basics",
  "Checks, Cashier's Checks, and Money Orders - Banking Basics",
  "Mobile and Online Banking Safely - Banking Basics"
 ],
 "Insurance Basics": [
  "Insurance 101: What It Is and Isn't - Insurance Basics",
  "Health Insurance Essentials - Insurance Basics",
  "Auto Insurance: Coverage That Matters - Insurance Basics",
  "Home and Renter's Insurance - Insurance Basics",
  "Life and Disability Insurance - Insurance Basics"
 ],
 "Investing Basics": [
  "Investing 101: Risk, Return, and Time - Investing Basics",
  "Retirement Accounts: 401(k)s and IRAs - Investing Basics",
  "Index Funds and Diversification - Investing Basics",
  "Avoiding Investment Scams and Hype - Investing Basics",
  "Annual Financial Review - Investing Basics",
  "Tax Basics Everyone Should Know - Investing Basics"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Personal Finance Study — "+safe+"\n"
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
    name:topic+' — personal finance guide record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A personal finance guide record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"personal-finance-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-personal-finance-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('personal-finance',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
