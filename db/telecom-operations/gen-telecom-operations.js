(function(){'use strict';
/* JAH The Telecom Operations Database generator — jahdb-telecom-operations-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-TLCO-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "What Telecom Networks Are — Industry Overview - Foundations",
  "The Telephone Numbering Plan - Foundations",
  "Copper Lines and DSL Broadband - Foundations",
  "Cable Broadband and DOCSIS - Foundations",
  "Fiber Optics and GPON - Foundations",
  "Mobile Networks — Cells and Towers - Foundations",
  "SIM Cards and Subscriber Identity - Foundations",
  "Voice Calls — From Dial to Ring - Foundations",
  "SMS and Text Messaging - Foundations",
  "Wi-Fi Fundamentals - Foundations",
  "IP Addresses and the Internet - Foundations",
  "Telecom Math I — Decibels and Signal Power - Foundations",
 ],
 "Compounded": [
  "4G LTE Networks - Compounded",
  "5G Networks and Network Slicing - Compounded",
  "The Mobile Core Network - Compounded",
  "Radio Access Networks (RAN) - Compounded",
  "Backhaul and Transport - Compounded",
  "Routing — OSPF and BGP - Compounded",
  "VoLTE and VoNR Voice - Compounded",
  "Roaming Between Networks - Compounded",
  "Billing Systems — OSS and BSS - Compounded",
  "Provisioning New Customers - Compounded",
  "MVNOs — Virtual Operators - Compounded",
 ],
 "Advanced": [
  "Spectrum Coordination - Advanced",
  "Network Planning and Capacity - Advanced",
  "Quality of Service (QoS) - Advanced",
  "Submarine Cables - Advanced",
  "Satellite Communications - Advanced",
  "Edge Computing in Telecom - Advanced",
  "Network Security Operations - Advanced",
  "Outage Management and Restoration - Advanced",
  "Service Level Agreements (SLAs) - Advanced",
  "Number Portability - Advanced",
  "Telecom Mastery Review — Running the Whole Network - Advanced",
 ],
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "#!/usr/bin/env python3\n"
   + "# "+safe+" -- structural sample demo. Property of Justin Addam Higgins (JAH).\n"
   + "# FSPL structural sample calculator (telecom operations)\n"
   + "import math\n"
   + "f, d = 2400.0, 5.0\n"
   + "fspl = 20*math.log10(d) + 20*math.log10(f) + 32.44\n"
   + "print('sample frequency MHz:', f)\n"
   + "print('sample distance km:', d)\n"
   + "print('sample FSPL dB:', round(fspl,2))\n"
   + "assert fspl > 0\n"
   + "print('OK: structural sample demo ran')\n";
}
function generate(seed,opts,rnd){
  opts=opts||{}; rnd=rnd||prng(seed);
  var field=opts.field&&FIELDS.indexOf(opts.field)>=0?opts.field:pick(FIELDS,rnd);
  var pool=TOPICS[field]||["General Study"];
  var topic=pick(pool,rnd);
  var id=PREFIX+String(seed).padStart(6,'0');
  return {
    id:id,
    name:topic+' — telecom operations record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A telecom operations record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"telecom-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-telecom-operations-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('telecom-operations',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
