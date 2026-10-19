(function(){'use strict';
/* JAH Form-Filling Assistance Database generator — jahdb-form-filling-assistance-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-FORMFAS-";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={"Foundations": ["Reading the Instructions First (Signature Edition)", "Gathering Documents Before You Start (Signature Edition)", "Personal Information Fields (Signature Edition)", "Dates and Format Conventions (Signature Edition)", "Financial Information Sections (Signature Edition)", "Employment History Blocks (Signature Edition)", "Signature and Date Lines (Signature Edition)", "Choosing Ink and Legibility (Signature Edition)", "N/A and Blank Fields (Signature Edition)", "Checkboxes and Multiple Choice (Signature Edition)", "The Final Review Pass (Signature Edition)"], "Compounded": ["Government Benefit Applications (Signature Edition)", "Medical Intake Forms (Signature Edition)", "Job Application Forms (Signature Edition)", "Financial Aid and Loan Forms (Signature Edition)", "Housing and Rental Applications (Signature Edition)", "School Enrollment Forms (Signature Edition)", "Tax Forms Basics (Signature Edition)", "Insurance Claim Forms (Signature Edition)", "Immigration Paperwork Basics (Signature Edition)", "Power of Attorney Forms (Signature Edition)", "Name Change Petitions (Signature Edition)", "Small Claims Court Forms (Signature Edition)"], "Advanced": ["Online Forms and Autofill (Signature Edition)", "Correcting Mistakes (Signature Edition)", "Deadlines and Postmarks (Signature Edition)", "Fees and Payment Sections (Signature Edition)", "Witness and Notary Requirements (Signature Edition)", "Keeping Copies and Records (Signature Edition)", "Forms for Someone Else (Signature Edition)", "Appeals and Reconsiderations (Signature Edition)", "Multilingual and Translated Forms (Signature Edition)", "Emergency and Time-Critical Forms (Signature Edition)", "Building a Personal Form Kit (Signature Edition)"]};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "#!/usr/bin/env python3\n\"\"\""+safe+" — form guide demo.\nRecord demo. Property of Justin Addam Higgins (JAH).\n\"\"\"\n"
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
    name:topic+' — form guide',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A form guide of "'+topic+'" in '+field+'. Generated sample record are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"form-filling-assistance-signature-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:"jahdb-form-filling-assistance-signature-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("form-filling-assistance-signature",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
