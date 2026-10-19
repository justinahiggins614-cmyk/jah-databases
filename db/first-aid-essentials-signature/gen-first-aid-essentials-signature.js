(function(){'use strict';
/* JAH First Aid Essentials Database generator — jahdb-first-aid-essentials-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-FIRSAES-";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={"Foundations": ["Scene Safety (Signature Edition)", "Primary Assessment (Signature Edition)", "Calling for Help (Signature Edition)", "Severe Bleeding (Signature Edition)", "CPR Basics (Signature Edition)", "AED Use (Signature Edition)", "Choking (Signature Edition)", "Burns (Signature Edition)", "Wounds (Signature Edition)", "Sprains (Signature Edition)", "Fractures (Signature Edition)"], "Compounded": ["Head Injuries (Signature Edition)", "Heat Emergencies (Signature Edition)", "Cold Emergencies (Signature Edition)", "Allergic Reactions (Signature Edition)", "Seizures (Signature Edition)", "Diabetic Emergencies (Signature Edition)", "Stroke Recognition (Signature Edition)", "Heart Attack Signs (Signature Edition)", "First Aid Kits (Signature Edition)", "Getting Certified (Signature Edition)", "Teaching First Aid (Signature Edition)", "The Skills Review (Signature Edition)"], "Advanced": ["Wound Infection (Signature Edition)", "Nosebleeds (Signature Edition)", "Eye Injuries (Signature Edition)", "Poisoning (Signature Edition)", "Bites and Stings (Signature Edition)", "Drowning Response (Signature Edition)", "Emergency Childbirth (Signature Edition)", "Mental Health Crises (Signature Edition)", "Sports Injuries (Signature Edition)", "Workplace First Aid (Signature Edition)", "Travel First Aid (Signature Edition)"]};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "#!/usr/bin/env python3\n\"\"\""+safe+" — first aid guide demo.\nRecord demo. Property of Justin Addam Higgins (JAH).\n\"\"\"\n"
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
    name:topic+' — first aid guide',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A first aid guide of "'+topic+'" in '+field+'. Generated sample record are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"first-aid-essentials-signature-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:"jahdb-first-aid-essentials-signature-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("first-aid-essentials-signature",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
