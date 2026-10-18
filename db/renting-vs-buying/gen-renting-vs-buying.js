(function(){'use strict';
/* JAH The Renting vs Buying Database generator — jahdb-home-cleaning-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-RVSB-";
var FIELDS=["Decision Foundations", "True Cost Math", "Lifestyle Factors", "Market Timing", "Renting Well", "Buying Well"];
var TOPICS={
 "Decision Foundations": [
  "The Core Trade-Off: Flexibility vs Equity - Decision Foundations",
  "The 5-Year Rule of Thumb - Decision Foundations",
  "The Psychology of Ownership - Decision Foundations",
  "Renting Is Not Throwing Money Away - Decision Foundations",
  "When Renting Wins: Case Studies - Decision Foundations",
  "When Buying Wins: Case Studies - Decision Foundations",
  "Building a Personal Housing Policy - Decision Foundations",
  "Teaching Kids About Housing Economics - Decision Foundations"
 ],
 "True Cost Math": [
  "True Cost of Renting: Beyond the Rent Check - True Cost Math",
  "True Cost of Owning: Beyond the Mortgage - True Cost Math",
  "The NYT-Style Rent vs Buy Calculator Logic - True Cost Math",
  "Opportunity Cost: What Your Down Payment Could Do - True Cost Math",
  "Break-Even Horizon Math - True Cost Math",
  "Tax Implications: The Honest Version - True Cost Math",
  "Leverage and Risk: The Double-Edged Sword - True Cost Math"
 ],
 "Lifestyle Factors": [
  "Lifestyle: How You Actually Live - Lifestyle Factors",
  "Career and Mobility Considerations - Lifestyle Factors",
  "Family Stage and Housing Needs - Lifestyle Factors"
 ],
 "Market Timing": [
  "Market Timing: Should You Wait? - Market Timing",
  "Interest Rates and Your Decision - Market Timing",
  "Advanced: Modeling With Uncertainty - Market Timing",
  "Timing Life Events With Housing Decisions - Market Timing",
  "Recourse vs Non-Recourse: The Fine Print - Market Timing",
  "Selling to Rent: The Reverse Move - Market Timing"
 ],
 "Renting Well": [
  "Renting Well: Maximizing the Renter's Edge - Renting Well",
  "The Renter's Investment Plan - Renting Well",
  "Negotiating Rent Like an Owner Negotiates Price - Renting Well"
 ],
 "Buying Well": [
  "Buying Well: Location First - Buying Well",
  "The Starter Home Strategy - Buying Well",
  "House Hacking Basics - Buying Well",
  "Rentvesting: Rent Where You Live, Own Where It Pays - Buying Well",
  "The 1% Rule and Investment Lenses on Housing - Buying Well",
  "Co-Buying: Friends, Family, and Partners - Buying Well",
  "The Forever Home: Buying Your Last Move - Buying Well"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# JAH Renting vs Buying Guide Study — "+safe+"\n"
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
    name:topic+' — renting vs buying guide record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A renting vs buying guide record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"renting-vs-buying-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-renting-vs-buying-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('renting-vs-buying',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
