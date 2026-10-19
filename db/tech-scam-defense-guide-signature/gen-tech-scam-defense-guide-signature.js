(function(){'use strict';
/* JAH Tech Scam Defense Guide Database generator — jahdb-tech-scam-defense-guide-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-TECHSDGS-";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={"Foundations": ["How Scams Work (Signature Edition)", "Phishing Emails (Signature Edition)", "Tech Support Scams (Signature Edition)", "IRS and Government Scams (Signature Edition)", "Romance Scams (Signature Edition)", "Investment Scams (Signature Edition)", "Lottery and Prize Scams (Signature Edition)", "Grandparent Scams (Signature Edition)", "Identity Theft (Signature Edition)", "Credit Freezes (Signature Edition)", "Social Engineering (Signature Edition)"], "Compounded": ["Smishing and Vishing (Signature Edition)", "Job Scams (Signature Edition)", "Rental Scams (Signature Edition)", "Charity Scams (Signature Edition)", "Recovery Scams (Signature Edition)", "Elder Fraud (Signature Edition)", "What To Do If Scammed (Signature Edition)", "Reporting Scams (Signature Edition)", "Protecting Family (Signature Edition)", "Business Scams (Signature Edition)", "Online Marketplace Scams (Signature Edition)", "Travel Scams (Signature Edition)"], "Advanced": ["Medical Scams (Signature Edition)", "AI-Powered Scams (Signature Edition)", "Teaching Scam Defense (Signature Edition)", "The Skepticism Habit (Signature Edition)", "Recovery Resources (Signature Edition)", "Community Defense (Signature Edition)", "Staying Current (Signature Edition)", "The Annual Fraud Review (Signature Edition)", "Cryptocurrency Scams (Signature Edition)", "Gift Card Scams (Signature Edition)", "Warranty Scams (Signature Edition)"]};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "#!/usr/bin/env python3\n\"\"\""+safe+" — scam defense guide demo.\nRecord demo. Property of Justin Addam Higgins (JAH).\n\"\"\"\n"
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
    name:topic+' — scam defense guide',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A scam defense guide of "'+topic+'" in '+field+'. Generated sample record are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"tech-scam-defense-guide-signature-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:"jahdb-tech-scam-defense-guide-signature-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("tech-scam-defense-guide-signature",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
