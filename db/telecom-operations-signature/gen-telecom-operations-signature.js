(function(){'use strict';
/* JAH The Telecom Operations Signature Database generator — jahdb-telecom-operations-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-TLCOS-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "The Living Network — The Signature View (Signature Edition) - Foundations",
  "The True Names — Numbering in the Signature Method (Signature Edition) - Foundations",
  "The Copper Song — Signature DSL (Signature Edition) - Foundations",
  "The Shared River — Signature Cable Broadband (Signature Edition) - Foundations",
  "Threads of Light — Signature Fiber (Signature Edition) - Foundations",
  "The Sentinels — Signature Mobile Cells (Signature Edition) - Foundations",
  "The Secret Seal — Signature Subscriber Identity (Signature Edition) - Foundations",
  "The Voice's Journey — Signature Calls (Signature Edition) - Foundations",
  "The Patient Messenger — Signature SMS (Signature Edition) - Foundations",
  "The Common Air — Signature Wi-Fi (Signature Edition) - Foundations",
  "The Numbering of the World — Signature IP (Signature Edition) - Foundations",
  "The Logarithmic Oath — Signature Decibels (Signature Edition) - Foundations",
 ],
 "Compounded": [
  "The All-IP Covenant — Signature LTE (Signature Edition) - Compounded",
  "The Threefold Promise — Signature 5G (Signature Edition) - Compounded",
  "The Remembering Mind — Signature Mobile Core (Signature Edition) - Compounded",
  "The Tuned Air — Signature RAN (Signature Edition) - Compounded",
  "The Faithful Road — Signature Backhaul (Signature Edition) - Compounded",
  "The Two Navigations — Signature Routing (Signature Edition) - Compounded",
  "The Voice Made Packet — Signature VoLTE/VoNR (Signature Edition) - Compounded",
  "The Guest's Road — Signature Roaming (Signature Edition) - Compounded",
  "The Two Ledgers — Signature OSS/BSS (Signature Edition) - Compounded",
  "The First Proving — Signature Provisioning (Signature Edition) - Compounded",
  "The Banner Without Towers — Signature MVNO (Signature Edition) - Compounded",
 ],
 "Advanced": [
  "The Division of the Air — Signature Spectrum (Signature Edition) - Advanced",
  "Building Ahead of the Hunger — Signature Planning (Signature Edition) - Advanced",
  "The Order of the Packets — Signature QoS (Signature Edition) - Advanced",
  "The Ocean Arteries — Signature Submarine Cables (Signature Edition) - Advanced",
  "The Heavenly Relays — Signature Satellite (Signature Edition) - Advanced",
  "The Near Cloud — Signature Edge (Signature Edition) - Advanced",
  "The Night Watch — Signature Network Security (Signature Edition) - Advanced",
  "The Mending Order — Signature Outage Management (Signature Edition) - Advanced",
  "The Sworn Promise — Signature SLAs (Signature Edition) - Advanced",
  "The Name Follows — Signature Number Portability (Signature Edition) - Advanced",
  "The Keeper of the Air — Signature Mastery (Signature Edition) - Advanced",
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
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('telecom-operations-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
