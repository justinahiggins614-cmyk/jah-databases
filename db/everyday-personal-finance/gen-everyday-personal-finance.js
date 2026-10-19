(function(){'use strict';
/* JAH Personal Finance Database generator — "jahdb-everyday-personal-finance-1.0".
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-EPF-";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={"Foundations": ["Budgeting: 50/30/20", "Emergency Fund", "Paying Off Debt: Snowball", "Credit Score Basics", "401(k) and the Match", "Roth IRA", "Index Fund Investing", "Compound Interest", "Term Life Insurance", "Writing a Will", "Health Savings Account", "Your Retirement Number"], "Compounded": ["Mortgage Basics", "Buying a Car Wisely", "Saving for College: 529", "Side Hustle Finances", "Tax Bracket Basics", "Negotiating Salary", "Fraud Protection", "Estate Planning Basics", "Charitable Giving", "Starting an LLC", "Rental Property Basics", "FIRE Movement"], "Advanced": ["Roth Conversion Ladder", "Backdoor Roth", "HSA as Retirement Account", "72(t) Early Withdrawals", "Revocable Living Trust", "Qualified Charitable Distributions", "Annuities: The Fine Print", "Generational Wealth", "Retirement Withdrawal Strategy", "Defining Enough"]};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "#!/usr/bin/env python3\n\"\"\""+safe+" — everyday-personal-finance demo.\nRecord demo. Property of Justin Addam Higgins (JAH).\n\"\"\"\n"
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
    name:topic+' — everyday record',
    title:topic,
    description:"SAMPLE RECORD (generated \u2014 structural sample). A everyday record study. Generated samples are clearly labeled and never presented as archive records.",
    field:field,
    src:"public-harvest-sample",
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
var gen={version:"jahdb-everyday-personal-finance-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("everyday-personal-finance",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
