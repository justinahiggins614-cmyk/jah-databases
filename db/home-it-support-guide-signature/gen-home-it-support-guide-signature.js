(function(){'use strict';
/* JAH Home IT Support Guide Database generator — jahdb-home-it-support-guide-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-HOMEISGS-";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={"Foundations": ["Home Network Setup (Signature Edition)", "Wi-Fi Security (Signature Edition)", "Wi-Fi Troubleshooting (Signature Edition)", "Extending Coverage (Signature Edition)", "Password Management (Signature Edition)", "Two-Factor Authentication (Signature Edition)", "Backup Strategy (Signature Edition)", "Cloud Backup (Signature Edition)", "Computer Maintenance (Signature Edition)", "Malware Removal (Signature Edition)", "Phishing Defense (Signature Edition)"], "Compounded": ["Printer Troubleshooting (Signature Edition)", "Smart Home Devices (Signature Edition)", "Streaming and TV (Signature Edition)", "Smartphone Care (Signature Edition)", "Email Management (Signature Edition)", "Parental Controls (Signature Edition)", "Senior Tech Support (Signature Edition)", "Data Recovery (Signature Edition)", "Operating System Reinstall (Signature Edition)", "Hardware Upgrades (Signature Edition)", "Buying Tech Wisely (Signature Edition)", "Selling and Disposing (Signature Edition)"], "Advanced": ["Home Office Tech (Signature Edition)", "Gaming Setup (Signature Edition)", "Voice Assistants (Signature Edition)", "Network Monitoring (Signature Edition)", "VPN Basics (Signature Edition)", "Scam Calls and Texts (Signature Edition)", "Documentation Habit (Signature Edition)", "Teaching Household Tech (Signature Edition)", "The Annual Tech Audit (Signature Edition)", "Two-Factor for the Household (Signature Edition)", "Kids and Devices (Signature Edition)"]};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "#!/usr/bin/env python3\n\"\"\""+safe+" — IT guide demo.\nRecord demo. Property of Justin Addam Higgins (JAH).\n\"\"\"\n"
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
    name:topic+' — IT guide',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A IT guide of "'+topic+'" in '+field+'. Generated sample record are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"home-it-support-guide-signature-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:"jahdb-home-it-support-guide-signature-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("home-it-support-guide-signature",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
