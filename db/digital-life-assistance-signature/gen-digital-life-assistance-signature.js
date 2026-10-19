(function(){'use strict';
/* JAH Digital Life Assistance Database generator — jahdb-digital-life-assistance-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-DIGILAS-";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={"Foundations": ["Password Manager Setup (Signature Edition)", "Two-Factor Authentication (Signature Edition)", "Email Account Security (Signature Edition)", "Organizing Files (Signature Edition)", "Photo Management (Signature Edition)", "Taming Notifications (Signature Edition)", "The 3-2-1 Backup Rule (Signature Edition)", "Software Updates (Signature Edition)", "Spotting Phishing (Signature Edition)", "Safe Online Shopping (Signature Edition)", "Social Media Privacy (Signature Edition)"], "Compounded": ["Managing Subscriptions (Signature Edition)", "Decluttering the Phone (Signature Edition)", "Wi-Fi Security at Home (Signature Edition)", "Public Wi-Fi Safety (Signature Edition)", "Backing Up Phones (Signature Edition)", "Digital Legacy Planning (Signature Edition)", "Helping Family Stay Safe (Signature Edition)", "Scam Call Defense (Signature Edition)", "Cloud Storage Organization (Signature Edition)", "Email Organization Systems (Signature Edition)", "Calendar and Contacts Hygiene (Signature Edition)", "Smart Home Basics (Signature Edition)"], "Advanced": ["Kid Device Safety (Signature Edition)", "Travel Tech Preparation (Signature Edition)", "Selling or Recycling Devices (Signature Edition)", "Monthly Digital Hygiene (Signature Edition)", "Password Recovery Planning (Signature Edition)", "Digital Minimalism (Signature Edition)", "Accessibility Settings (Signature Edition)", "The Annual Digital Audit (Signature Edition)", "Teaching Digital Skills (Signature Edition)", "Work and Personal Separation (Signature Edition)", "Offline Preparedness (Signature Edition)"]};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "#!/usr/bin/env python3\n\"\"\""+safe+" — digital guide demo.\nRecord demo. Property of Justin Addam Higgins (JAH).\n\"\"\"\n"
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
    name:topic+' — digital guide',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A digital guide of "'+topic+'" in '+field+'. Generated sample record are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"digital-life-assistance-signature-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:"jahdb-digital-life-assistance-signature-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("digital-life-assistance-signature",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
