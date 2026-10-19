(function(){'use strict';
/* JAH Home Security Basics Database generator — jahdb-home-security-basics-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-HOMESBS-";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={"Foundations": ["The Layered Approach (Signature Edition)", "Door Security (Signature Edition)", "Deadbolts (Signature Edition)", "Window Security (Signature Edition)", "Sliding Doors (Signature Edition)", "Exterior Lighting (Signature Edition)", "Landscaping for Security (Signature Edition)", "Alarm Systems (Signature Edition)", "Security Cameras (Signature Edition)", "Smart Locks (Signature Edition)", "While Away (Signature Edition)"], "Compounded": ["Spare Keys (Signature Edition)", "Garage Security (Signature Edition)", "Home Safes (Signature Edition)", "Neighborhood Watch (Signature Edition)", "Apartment Security (Signature Edition)", "Home Invasion Response (Signature Edition)", "Teaching Home Security (Signature Edition)", "The Annual Security Review (Signature Edition)", "Lock Bumping Awareness (Signature Edition)", "Doorbell Cameras (Signature Edition)", "Fence and Gate Security (Signature Edition)", "Security Signage (Signature Edition)"], "Advanced": ["Room-by-Room Audit (Signature Edition)", "Travel Security (Signature Edition)", "Valuables Inventory (Signature Edition)", "Security for Seniors (Signature Edition)", "Fire Safety Integration (Signature Edition)", "Security Lighting Tech (Signature Edition)", "Window Bars (Signature Edition)", "Security Doors (Signature Edition)", "Intercom Systems (Signature Edition)", "Panic Buttons (Signature Edition)", "The Move-In Security Setup (Signature Edition)"]};
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
    demo:{kind:"home-security-basics-signature-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:"jahdb-home-security-basics-signature-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("home-security-basics-signature",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
