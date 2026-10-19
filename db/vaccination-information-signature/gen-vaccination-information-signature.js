(function(){'use strict';
/* JAH Vaccination Information Database generator — jahdb-vaccination-information-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-VACCIS-";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={"Foundations": ["How Vaccines Work (Signature Edition)", "Types of Vaccines (Signature Edition)", "The Childhood Schedule (Signature Edition)", "Adult Vaccines (Signature Edition)", "Flu Vaccines Yearly (Signature Edition)", "COVID-19 Vaccines (Signature Edition)", "What to Expect: Side Effects (Signature Edition)", "Vaccine Safety Monitoring (Signature Edition)", "Herd Immunity (Signature Edition)", "Evaluating Claims (Signature Edition)", "Talking With Your Clinician (Signature Edition)"], "Compounded": ["Vaccine Records (Signature Edition)", "Travel Vaccines (Signature Edition)", "Vaccines in Pregnancy (Signature Edition)", "Immunocompromised Guidance (Signature Edition)", "Allergies and Vaccines (Signature Edition)", "Vaccine Ingredients (Signature Edition)", "The Approval Process (Signature Edition)", "Myths and Facts (Signature Edition)", "School Requirements (Signature Edition)", "Workplace Requirements (Signature Edition)", "Vaccine Hesitancy (Signature Edition)", "Global Vaccination (Signature Edition)"], "Advanced": ["Booster Logic (Signature Edition)", "Combination Vaccines (Signature Edition)", "Storing Vaccines Properly (Signature Edition)", "After Vaccination Care (Signature Edition)", "Vaccine Research Literacy (Signature Edition)", "Community Protection (Signature Edition)", "The Annual Vaccine Review (Signature Edition)", "Teaching Vaccine Literacy (Signature Edition)", "Vaccine Records (Signature Edition)", "Travel Vaccines (Signature Edition)", "Vaccine Development (Signature Edition)"]};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "#!/usr/bin/env python3\n\"\"\""+safe+" — vaccination guide demo.\nRecord demo. Property of Justin Addam Higgins (JAH).\n\"\"\"\n"
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
    name:topic+' — vaccination guide',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A vaccination guide of "'+topic+'" in '+field+'. Generated sample record are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"vaccination-information-signature-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:"jahdb-vaccination-information-signature-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("vaccination-information-signature",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
