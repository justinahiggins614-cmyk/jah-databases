(function(){'use strict';
/* JAH The Selling Tactics Database generator — jahdb-selling-tactics-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-SELL-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "What Selling Is - Foundations",
  "The Psychology of Buying - Foundations",
  "Prospecting and Finding Customers - Foundations",
  "Qualifying Leads - Foundations",
  "First Impressions and Rapport - Foundations",
  "Discovery Questions - Foundations",
  "Product Knowledge - Foundations",
  "Listening as a Selling Skill - Foundations",
  "Features Versus Benefits - Foundations",
  "Setting Sales Goals and Activity Targets - Foundations",
  "Time Management for Sellers - Foundations"
 ],
 "Compounded": [
  "The Elevator Pitch - Compounded",
  "Sales Presentations - Compounded",
  "Storytelling in Sales - Compounded",
  "The Objection Handling Method - Compounded",
  "Handling Price Objections - Compounded",
  "Handling Think-It-Over Objections - Compounded",
  "Fundamentals of Sales Negotiation - Compounded",
  "Trial Closes - Compounded",
  "Closing Techniques - Compounded",
  "Follow-Up Systems - Compounded",
  "Referral Selling - Compounded",
  "Upselling and Cross-Selling - Compounded"
 ],
 "Advanced": [
  "SPIN Selling and Consultative Method - Advanced",
  "Value-Based Selling - Advanced",
  "Enterprise and Complex Sales Cycles - Advanced",
  "Multi-Stakeholder Consensus - Advanced",
  "Key Account Management - Advanced",
  "Pipeline Management and Forecasting - Advanced",
  "CRM Discipline - Advanced",
  "Ethics of Selling - Advanced",
  "Win-Loss Analysis - Advanced",
  "Insight Selling: The Challenger Method - Advanced",
  "The Relationship and Referral Engine - Advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Selling Tactic Study — "+safe+"\n"
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
    name:topic+' — selling tactic record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A selling tactic record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"selling-tactic-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-selling-tactics-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('selling-tactics',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
