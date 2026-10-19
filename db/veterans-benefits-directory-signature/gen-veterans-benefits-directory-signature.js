(function(){'use strict';
/* JAH Veterans Benefits Directory Database generator — jahdb-veterans-benefits-directory-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-VETEBDS-";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={"Foundations": ["VA Health Care Enrollment (Signature Edition)", "Disability Compensation (Signature Edition)", "Proving Service Connection (Signature Edition)", "C&P Exams (Signature Edition)", "Appealing VA Decisions (Signature Edition)", "GI Bill Education (Signature Edition)", "VA Home Loans (Signature Edition)", "VA Pension (Signature Edition)", "Mental Health Care (Signature Edition)", "Women Veterans (Signature Edition)", "Caregiver Support (Signature Edition)"], "Compounded": ["Burial Benefits (Signature Edition)", "VSO Assistance (Signature Edition)", "State Veterans Benefits (Signature Edition)", "Employment Programs (Signature Edition)", "Homeless Veteran Programs (Signature Edition)", "Family Benefits (Signature Edition)", "Discharge Upgrades (Signature Edition)", "Toxic Exposure Claims (Signature Edition)", "Teaching Fellow Veterans (Signature Edition)", "The Annual VA Review (Signature Edition)", "Aid and Attendance (Signature Edition)", "Housebound Benefits (Signature Edition)"], "Advanced": ["Dental Care (Signature Edition)", "Vision and Hearing (Signature Edition)", "Prescriptions (Signature Edition)", "Travel Reimbursement (Signature Edition)", "Fisher House (Signature Edition)", "Vet Centers (Signature Edition)", "Adaptive Housing (Signature Edition)", "Auto Grants (Signature Edition)", "Life Insurance (Signature Edition)", "Education for Dependents (Signature Edition)", "Pension for Survivors (Signature Edition)"]};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "#!/usr/bin/env python3\n\"\"\""+safe+" — benefits directory demo.\nRecord demo. Property of Justin Addam Higgins (JAH).\n\"\"\"\n"
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
    name:topic+' — benefits directory',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A benefits directory of "'+topic+'" in '+field+'. Generated sample record are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"veterans-benefits-directory-signature-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:"jahdb-veterans-benefits-directory-signature-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("veterans-benefits-directory-signature",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
