(function(){'use strict';
/* JAH The Pharmaceutical Manufacturing and Quality Database generator — jahdb-pharmaceutical-manufacturing-quality-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-PMQ-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "What GMP Is: The Rules That Keep Medicines Safe \u2014 Foundations",
  "The Batch Record: Every Step Documented \u2014 Foundations",
  "Identity, Strength, Quality, Purity: The Four Demands \u2014 Foundations",
  "Raw Material Control: Starting Right \u2014 Foundations",
  "Weighing and Dispensing: Precision at the Start \u2014 Foundations",
  "Manufacturing Formulas and Instructions \u2014 Foundations",
  "In-Process Controls: Checking While Making \u2014 Foundations",
  "Contamination Control Basics \u2014 Foundations",
  "Cleaning and Cleaning Verification \u2014 Foundations",
  "Personnel: Training, Hygiene, Gowning \u2014 Foundations",
  "Facilities: Designed to Prevent Mix-Ups \u2014 Foundations",
  "Documentation: If It Isn't Written Down... \u2014 Foundations"
 ],
 "Compounded": [
  "Process Validation: IQ, OQ, PQ \u2014 Compounded",
  "Cleaning Validation and MACO Limits \u2014 Compounded",
  "Analytical Method Validation (ICH Q2) \u2014 Compounded",
  "Stability Studies (ICH Q1A) \u2014 Compounded",
  "Accelerated Stability and Arrhenius \u2014 Compounded",
  "Specifications and Acceptance Criteria \u2014 Compounded",
  "OOS Investigations: Out-of-Specification \u2014 Compounded",
  "Deviations and Nonconformances \u2014 Compounded",
  "CAPA: Corrective and Preventive Action \u2014 Compounded",
  "Change Control \u2014 Compounded",
  "Sampling Plans and AQL \u2014 Compounded",
  "Environmental Monitoring \u2014 Compounded"
 ],
 "Advanced": [
  "Quality Systems: ICH Q10 \u2014 Advanced",
  "Process Capability: Cpk and Ppk \u2014 Advanced",
  "Continued Process Verification \u2014 Advanced",
  "Sterile Manufacturing and Aseptic Processing \u2014 Advanced",
  "Containment: Potent Compounds \u2014 Advanced",
  "Data Integrity: ALCOA+ \u2014 Advanced",
  "Batch Release and the Qualified Person \u2014 Advanced",
  "Stability-Indicating Methods \u2014 Advanced",
  "Extractables and Leachables \u2014 Advanced",
  "The Site Master File and Inspection Readiness \u2014 Advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Pharma Quality — "+safe+"\n"
   + "# Field: "+field+"\n"
   + "record = {'title': \""+safe+"\", 'field': \""+field+"\"}\n"
   + "def summarize(r):\n"
   + "    return r['title'] + ' [' + r['field'] + ']'\n"
   + "print(summarize(record))\n"
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
    name:topic+' — pharmaceutical quality record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A pharmaceutical quality record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"pharma-quality-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-pharmaceutical-manufacturing-quality-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('pharmaceutical-manufacturing-quality',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
