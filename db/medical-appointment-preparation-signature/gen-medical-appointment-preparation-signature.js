(function(){'use strict';
/* JAH Medical Appointment Preparation Database generator — jahdb-medical-appointment-preparation-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-MEDIAPS-";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={"Foundations": ["The One-Page Health Summary (Signature Edition)", "Prioritizing Your Concerns (Signature Edition)", "Medication List Mastery (Signature Edition)", "Symptom Journaling (Signature Edition)", "New Patient Paperwork (Signature Edition)", "Choosing the Right Clinician (Signature Edition)", "Insurance and Referrals (Signature Edition)", "The Opening Two Minutes (Signature Edition)", "Describing Symptoms Well (Signature Edition)", "Asking About Diagnosis (Signature Edition)", "Treatment Option Questions (Signature Edition)"], "Compounded": ["Medication Questions (Signature Edition)", "Bringing a Companion (Signature Edition)", "Language and Interpreters (Signature Edition)", "The After-Visit Summary (Signature Edition)", "Test Result Follow-Up (Signature Edition)", "Referral Navigation (Signature Edition)", "Second Opinions (Signature Edition)", "Telehealth Visits (Signature Edition)", "Urgent Visit Prep (Signature Edition)", "Chronic Condition Reviews (Signature Edition)", "Pediatric Appointments (Signature Edition)", "Geriatric Visit Support (Signature Edition)"], "Advanced": ["Mental Health Appointments (Signature Edition)", "Cost Conversations (Signature Edition)", "Patient Portal Mastery (Signature Edition)", "When Care Disappoints (Signature Edition)", "Emergency Preparedness (Signature Edition)", "Annual Physical Strategy (Signature Edition)", "Teaching Self-Advocacy (Signature Edition)", "The Lifetime Health File (Signature Edition)", "Pre-Visit Paperwork (Signature Edition)", "Bringing a Companion (Signature Edition)", "After-Visit Summary (Signature Edition)"]};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "#!/usr/bin/env python3\n\"\"\""+safe+" — appointment guide demo.\nRecord demo. Property of Justin Addam Higgins (JAH).\n\"\"\"\n"
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
    name:topic+' — appointment guide',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A appointment guide of "'+topic+'" in '+field+'. Generated sample record are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"medical-appointment-preparation-signature-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:"jahdb-medical-appointment-preparation-signature-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("medical-appointment-preparation-signature",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
