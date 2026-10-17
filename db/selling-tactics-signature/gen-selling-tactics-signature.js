(function(){'use strict';
/* JAH The Selling Tactics Signature Database generator — jahdb-selling-tactics-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-SELLS-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "What Selling Is (Signature Edition) - Foundations",
  "The Psychology of Buying (Signature Edition) - Foundations",
  "Prospecting and Finding Customers (Signature Edition) - Foundations",
  "Qualifying Leads (Signature Edition) - Foundations",
  "First Impressions and Rapport (Signature Edition) - Foundations",
  "Discovery Questions (Signature Edition) - Foundations",
  "Product Knowledge (Signature Edition) - Foundations",
  "Listening as a Selling Skill (Signature Edition) - Foundations",
  "Features Versus Benefits (Signature Edition) - Foundations",
  "Setting Sales Goals and Activity Targets (Signature Edition) - Foundations",
  "Time Management for Sellers (Signature Edition) - Foundations"
 ],
 "Compounded": [
  "The Elevator Pitch (Signature Edition) - Compounded",
  "Sales Presentations (Signature Edition) - Compounded",
  "Storytelling in Sales (Signature Edition) - Compounded",
  "The Objection Handling Method (Signature Edition) - Compounded",
  "Handling Price Objections (Signature Edition) - Compounded",
  "Handling Think-It-Over Objections (Signature Edition) - Compounded",
  "Fundamentals of Sales Negotiation (Signature Edition) - Compounded",
  "Trial Closes (Signature Edition) - Compounded",
  "Closing Techniques (Signature Edition) - Compounded",
  "Follow-Up Systems (Signature Edition) - Compounded",
  "Referral Selling (Signature Edition) - Compounded",
  "Upselling and Cross-Selling (Signature Edition) - Compounded"
 ],
 "Advanced": [
  "SPIN Selling and Consultative Method (Signature Edition) - Advanced",
  "Value-Based Selling (Signature Edition) - Advanced",
  "Enterprise and Complex Sales Cycles (Signature Edition) - Advanced",
  "Multi-Stakeholder Consensus (Signature Edition) - Advanced",
  "Key Account Management (Signature Edition) - Advanced",
  "Pipeline Management and Forecasting (Signature Edition) - Advanced",
  "CRM Discipline (Signature Edition) - Advanced",
  "Ethics of Selling (Signature Edition) - Advanced",
  "Win-Loss Analysis (Signature Edition) - Advanced",
  "Insight Selling: The Challenger Method (Signature Edition) - Advanced",
  "The Relationship and Referral Engine (Signature Edition) - Advanced"
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
var gen={version:'jahdb-selling-tactics-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('selling-tactics-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
