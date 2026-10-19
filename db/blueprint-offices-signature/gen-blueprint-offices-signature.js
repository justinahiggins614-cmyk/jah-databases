(function(){'use strict';
/* JAH The Office Blueprint Signature Database generator — jahdb-blueprint-offices-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-BOFPS-";
var FIELDS=["Corporate","Medical","Professional","Service"];
var TOPICS={
 "Corporate": [
  "Signature Open-Plan Office - Compact Architectural Blueprint (Signature Edition) - Corporate",
  "Signature Executive Suite - Compact Architectural Blueprint (Signature Edition) - Corporate",
  "Signature Co-Working Hub - Compact Architectural Blueprint (Signature Edition) - Corporate",
  "Signature Call Center - Compact Architectural Blueprint (Signature Edition) - Corporate",
  "Signature Open-Plan Office - Standard Architectural Blueprint (Signature Edition) - Corporate",
  "Signature Executive Suite - Standard Architectural Blueprint (Signature Edition) - Corporate",
  "Signature Co-Working Hub - Standard Architectural Blueprint (Signature Edition) - Corporate",
  "Signature Call Center - Standard Architectural Blueprint (Signature Edition) - Corporate",
  "Signature Open-Plan Office - Grand Architectural Blueprint (Signature Edition) - Corporate",
  "Signature Executive Suite - Grand Architectural Blueprint (Signature Edition) - Corporate",
  "Signature Co-Working Hub - Grand Architectural Blueprint (Signature Edition) - Corporate",
  "Signature Call Center - Grand Architectural Blueprint (Signature Edition) - Corporate"
 ],
 "Medical": [
  "Signature Medical Office - Compact Architectural Blueprint (Signature Edition) - Medical",
  "Signature Dental Clinic - Compact Architectural Blueprint (Signature Edition) - Medical",
  "Signature Medical Office - Standard Architectural Blueprint (Signature Edition) - Medical",
  "Signature Dental Clinic - Standard Architectural Blueprint (Signature Edition) - Medical",
  "Signature Medical Office - Grand Architectural Blueprint (Signature Edition) - Medical",
  "Signature Dental Clinic - Grand Architectural Blueprint (Signature Edition) - Medical"
 ],
 "Professional": [
  "Signature Law Firm Office - Compact Architectural Blueprint (Signature Edition) - Professional",
  "Signature Government Office - Compact Architectural Blueprint (Signature Edition) - Professional",
  "Signature Creative Studio Office - Compact Architectural Blueprint (Signature Edition) - Professional",
  "Signature Law Firm Office - Standard Architectural Blueprint (Signature Edition) - Professional",
  "Signature Government Office - Standard Architectural Blueprint (Signature Edition) - Professional",
  "Signature Creative Studio Office - Standard Architectural Blueprint (Signature Edition) - Professional",
  "Signature Law Firm Office - Grand Architectural Blueprint (Signature Edition) - Professional",
  "Signature Government Office - Grand Architectural Blueprint (Signature Edition) - Professional",
  "Signature Creative Studio Office - Grand Architectural Blueprint (Signature Edition) - Professional"
 ],
 "Service": [
  "Signature Bank Branch - Compact Architectural Blueprint (Signature Edition) - Service",
  "Signature Insurance Office - Compact Architectural Blueprint (Signature Edition) - Service",
  "Signature Real Estate Office - Compact Architectural Blueprint (Signature Edition) - Service",
  "Signature Bank Branch - Standard Architectural Blueprint (Signature Edition) - Service",
  "Signature Insurance Office - Standard Architectural Blueprint (Signature Edition) - Service",
  "Signature Real Estate Office - Standard Architectural Blueprint (Signature Edition) - Service",
  "Signature Bank Branch - Grand Architectural Blueprint (Signature Edition) - Service"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Offices Blueprint Study — "+safe+"\n"
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
    name:topic+' — office blueprint record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A office blueprint record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"blueprint-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-blueprint-offices-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('blueprint-offices-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
