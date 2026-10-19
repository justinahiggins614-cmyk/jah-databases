(function(){'use strict';
/* JAH Form-Filling Assistance Database generator — jahdb-form-filling-assistance-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-FORMFA-";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={"Foundations": ["Reading the Instructions First", "Gathering Documents Before You Start", "Personal Information Fields", "Dates and Format Conventions", "Financial Information Sections", "Employment History Blocks", "Signature and Date Lines", "Choosing Ink and Legibility", "N/A and Blank Fields", "Checkboxes and Multiple Choice", "The Final Review Pass"], "Compounded": ["Government Benefit Applications", "Medical Intake Forms", "Job Application Forms", "Financial Aid and Loan Forms", "Housing and Rental Applications", "School Enrollment Forms", "Tax Forms Basics", "Insurance Claim Forms", "Immigration Paperwork Basics", "Power of Attorney Forms", "Name Change Petitions", "Small Claims Court Forms"], "Advanced": ["Online Forms and Autofill", "Correcting Mistakes", "Deadlines and Postmarks", "Fees and Payment Sections", "Witness and Notary Requirements", "Keeping Copies and Records", "Forms for Someone Else", "Appeals and Reconsiderations", "Multilingual and Translated Forms", "Emergency and Time-Critical Forms", "Building a Personal Form Kit"]};
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
    src:'public-harvest',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"form-filling-assistance-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:"jahdb-form-filling-assistance-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("form-filling-assistance",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
