(function(){'use strict';
/* JAH Investment Risk Education Database generator — jahdb-investment-risk-education-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-INVERES-";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={"Foundations": ["What Risk Really Means (Signature Edition)", "Risk vs Return (Signature Edition)", "Your Time Horizon (Signature Edition)", "Risk Tolerance Honestly (Signature Edition)", "Diversification Basics (Signature Edition)", "Index Funds Explained (Signature Edition)", "Stocks vs Bonds (Signature Edition)", "Asset Allocation (Signature Edition)", "Dollar-Cost Averaging (Signature Edition)", "Fees and Expense Ratios (Signature Edition)", "Inflation Risk (Signature Edition)"], "Compounded": ["Market Crashes (Signature Edition)", "Behavioral Traps (Signature Edition)", "Scam Recognition (Signature Edition)", "Emergency Fund First (Signature Edition)", "Debt vs Investing (Signature Edition)", "Retirement Accounts (Signature Edition)", "Rebalancing (Signature Edition)", "Tax-Efficient Investing (Signature Edition)", "Understanding Prospectuses (Signature Edition)", "Bonds in Depth (Signature Edition)", "International Diversification (Signature Edition)", "Real Estate Investing (Signature Edition)"], "Advanced": ["When to Get Advice (Signature Edition)", "Teaching Investing Basics (Signature Edition)", "The Annual Portfolio Review (Signature Edition)", "Sequence of Returns Risk (Signature Edition)", "Estate Planning Basics (Signature Edition)", "Charitable Giving Strategies (Signature Edition)", "Staying the Course (Signature Edition)", "Understanding Dividends (Signature Edition)", "Market Index Basics (Signature Edition)", "Bear and Bull Markets (Signature Edition)", "Building Your First Portfolio (Signature Edition)"]};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "#!/usr/bin/env python3\n\"\"\""+safe+" — investing guide demo.\nRecord demo. Property of Justin Addam Higgins (JAH).\n\"\"\"\n"
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
    name:topic+' — investing guide',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A investing guide of "'+topic+'" in '+field+'. Generated sample record are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"investment-risk-education-signature-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:"jahdb-investment-risk-education-signature-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("investment-risk-education-signature",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
