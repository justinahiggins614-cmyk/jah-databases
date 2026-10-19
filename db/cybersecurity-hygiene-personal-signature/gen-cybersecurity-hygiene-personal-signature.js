(function(){'use strict';
/* JAH Personal Cybersecurity Hygiene Database generator — jahdb-cybersecurity-hygiene-personal-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-CYBEHPS-";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={"Foundations": ["The Threat Landscape (Signature Edition)", "Automatic Updates (Signature Edition)", "Password Hygiene (Signature Edition)", "Two-Factor Authentication (Signature Edition)", "Phishing Recognition (Signature Edition)", "Safe Browsing (Signature Edition)", "Email Security (Signature Edition)", "Public Wi-Fi (Signature Edition)", "Device Security (Signature Edition)", "Backup Discipline (Signature Edition)", "Social Media Privacy (Signature Edition)"], "Compounded": ["Financial Monitoring (Signature Edition)", "Identity Theft Response (Signature Edition)", "Kids Online Safety (Signature Edition)", "Senior Scam Defense (Signature Edition)", "Teaching Cyber Hygiene (Signature Edition)", "The Annual Security Review (Signature Edition)", "VPN Use (Signature Edition)", "Browser Extensions (Signature Edition)", "Software Sources (Signature Edition)", "Removable Media (Signature Edition)", "IoT Security (Signature Edition)", "Cloud Security (Signature Edition)"], "Advanced": ["Mobile Payments (Signature Edition)", "QR Code Safety (Signature Edition)", "Deepfake Awareness (Signature Edition)", "Data Brokers (Signature Edition)", "Secure Disposal (Signature Edition)", "Travel Cyber Safety (Signature Edition)", "Work From Home Security (Signature Edition)", "Incident Response (Signature Edition)", "Passwordless Future (Signature Edition)", "Cyber Insurance (Signature Edition)", "Teaching Seniors (Signature Edition)"]};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "#!/usr/bin/env python3\n\"\"\""+safe+" — security guide demo.\nRecord demo. Property of Justin Addam Higgins (JAH).\n\"\"\"\n"
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
    name:topic+' — security guide',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A security guide of "'+topic+'" in '+field+'. Generated sample record are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"cybersecurity-hygiene-personal-signature-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:"jahdb-cybersecurity-hygiene-personal-signature-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("cybersecurity-hygiene-personal-signature",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
