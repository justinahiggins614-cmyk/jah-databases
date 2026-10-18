(function(){'use strict';
/* JAH The Pharmaceutical Manufacturing and Quality Signature Database generator — jahdb-pharmaceutical-manufacturing-quality-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-PMQS-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "What GMP Is: The Rules That Keep Medicines Safe (Signature Edition) \u2014 Foundations",
  "The Batch Record: Every Step Documented (Signature Edition) \u2014 Foundations",
  "Identity, Strength, Quality, Purity: The Four Demands (Signature Edition) \u2014 Foundations",
  "Raw Material Control: Starting Right (Signature Edition) \u2014 Foundations",
  "Weighing and Dispensing: Precision at the Start (Signature Edition) \u2014 Foundations",
  "Manufacturing Formulas and Instructions (Signature Edition) \u2014 Foundations",
  "In-Process Controls: Checking While Making (Signature Edition) \u2014 Foundations",
  "Contamination Control Basics (Signature Edition) \u2014 Foundations",
  "Cleaning and Cleaning Verification (Signature Edition) \u2014 Foundations",
  "Personnel: Training, Hygiene, Gowning (Signature Edition) \u2014 Foundations",
  "Facilities: Designed to Prevent Mix-Ups (Signature Edition) \u2014 Foundations",
  "Documentation: If It Isn't Written Down... (Signature Edition) \u2014 Foundations"
 ],
 "Compounded": [
  "Process Validation: IQ, OQ, PQ (Signature Edition) \u2014 Compounded",
  "Cleaning Validation and MACO Limits (Signature Edition) \u2014 Compounded",
  "Analytical Method Validation (ICH Q2) (Signature Edition) \u2014 Compounded",
  "Stability Studies (ICH Q1A) (Signature Edition) \u2014 Compounded",
  "Accelerated Stability and Arrhenius (Signature Edition) \u2014 Compounded",
  "Specifications and Acceptance Criteria (Signature Edition) \u2014 Compounded",
  "OOS Investigations: Out-of-Specification (Signature Edition) \u2014 Compounded",
  "Deviations and Nonconformances (Signature Edition) \u2014 Compounded",
  "CAPA: Corrective and Preventive Action (Signature Edition) \u2014 Compounded",
  "Change Control (Signature Edition) \u2014 Compounded",
  "Sampling Plans and AQL (Signature Edition) \u2014 Compounded",
  "Environmental Monitoring (Signature Edition) \u2014 Compounded"
 ],
 "Advanced": [
  "Quality Systems: ICH Q10 (Signature Edition) \u2014 Advanced",
  "Process Capability: Cpk and Ppk (Signature Edition) \u2014 Advanced",
  "Continued Process Verification (Signature Edition) \u2014 Advanced",
  "Sterile Manufacturing and Aseptic Processing (Signature Edition) \u2014 Advanced",
  "Containment: Potent Compounds (Signature Edition) \u2014 Advanced",
  "Data Integrity: ALCOA+ (Signature Edition) \u2014 Advanced",
  "Batch Release and the Qualified Person (Signature Edition) \u2014 Advanced",
  "Stability-Indicating Methods (Signature Edition) \u2014 Advanced",
  "Extractables and Leachables (Signature Edition) \u2014 Advanced",
  "The Site Master File and Inspection Readiness (Signature Edition) \u2014 Advanced"
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
var gen={version:'jahdb-pharmaceutical-manufacturing-quality-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('pharmaceutical-manufacturing-quality-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
