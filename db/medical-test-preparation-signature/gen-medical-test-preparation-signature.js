(function(){'use strict';
/* JAH Medical Test Preparation Database generator — jahdb-medical-test-preparation-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-MEDITPS-";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={"Foundations": ["Understanding Test Orders (Signature Edition)", "Blood Test Basics (Signature Edition)", "Fasting Instructions (Signature Edition)", "Imaging: X-Ray (Signature Edition)", "Imaging: Ultrasound (Signature Edition)", "Imaging: CT Scans (Signature Edition)", "Imaging: MRI (Signature Edition)", "Mammograms (Signature Edition)", "Colonoscopy Prep (Signature Edition)", "Endoscopy Basics (Signature Edition)", "Biopsy Procedures (Signature Edition)"], "Compounded": ["Cardiac Tests (Signature Edition)", "Pulmonary Function Tests (Signature Edition)", "Allergy Testing (Signature Edition)", "Genetic Testing (Signature Edition)", "Pregnancy-Related Tests (Signature Edition)", "Pediatric Test Prep (Signature Edition)", "Test Anxiety Management (Signature Edition)", "Contrast and Dyes (Signature Edition)", "Sedation and Anesthesia (Signature Edition)", "Results: Understanding Reports (Signature Edition)", "False Positives and Negatives (Signature Edition)", "Tracking Results Over Time (Signature Edition)"], "Advanced": ["When Tests Are Unclear (Signature Edition)", "Second Opinions on Results (Signature Edition)", "Cost and Coverage (Signature Edition)", "Preparing Children (Signature Edition)", "The Test Day Checklist (Signature Edition)", "After the Test (Signature Edition)", "Teaching Test Literacy (Signature Edition)", "The Annual Screening Review (Signature Edition)", "Emergency Testing (Signature Edition)", "Genetic Testing Prep (Signature Edition)", "Pediatric Test Prep (Signature Edition)"]};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "#!/usr/bin/env python3\n\"\"\""+safe+" — test guide demo.\nRecord demo. Property of Justin Addam Higgins (JAH).\n\"\"\"\n"
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
    name:topic+' — test guide',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A test guide of "'+topic+'" in '+field+'. Generated sample record are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"medical-test-preparation-signature-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:"jahdb-medical-test-preparation-signature-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("medical-test-preparation-signature",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
