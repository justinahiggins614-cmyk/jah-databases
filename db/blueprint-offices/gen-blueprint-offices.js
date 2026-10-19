(function(){'use strict';
/* JAH The Office Blueprint Database generator — jahdb-blueprint-offices-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-BOFP-";
var FIELDS=["Corporate","Medical","Professional","Service"];
var TOPICS={
 "Corporate": [
  "Open-Plan Office - Compact Architectural Blueprint - Corporate",
  "Executive Suite - Compact Architectural Blueprint - Corporate",
  "Co-Working Hub - Compact Architectural Blueprint - Corporate",
  "Call Center - Compact Architectural Blueprint - Corporate",
  "Open-Plan Office - Standard Architectural Blueprint - Corporate",
  "Executive Suite - Standard Architectural Blueprint - Corporate",
  "Co-Working Hub - Standard Architectural Blueprint - Corporate",
  "Call Center - Standard Architectural Blueprint - Corporate",
  "Open-Plan Office - Grand Architectural Blueprint - Corporate",
  "Executive Suite - Grand Architectural Blueprint - Corporate",
  "Co-Working Hub - Grand Architectural Blueprint - Corporate",
  "Call Center - Grand Architectural Blueprint - Corporate"
 ],
 "Medical": [
  "Medical Office - Compact Architectural Blueprint - Medical",
  "Dental Clinic - Compact Architectural Blueprint - Medical",
  "Medical Office - Standard Architectural Blueprint - Medical",
  "Dental Clinic - Standard Architectural Blueprint - Medical",
  "Medical Office - Grand Architectural Blueprint - Medical",
  "Dental Clinic - Grand Architectural Blueprint - Medical"
 ],
 "Professional": [
  "Law Firm Office - Compact Architectural Blueprint - Professional",
  "Government Office - Compact Architectural Blueprint - Professional",
  "Creative Studio Office - Compact Architectural Blueprint - Professional",
  "Law Firm Office - Standard Architectural Blueprint - Professional",
  "Government Office - Standard Architectural Blueprint - Professional",
  "Creative Studio Office - Standard Architectural Blueprint - Professional",
  "Law Firm Office - Grand Architectural Blueprint - Professional",
  "Government Office - Grand Architectural Blueprint - Professional",
  "Creative Studio Office - Grand Architectural Blueprint - Professional"
 ],
 "Service": [
  "Bank Branch - Compact Architectural Blueprint - Service",
  "Insurance Office - Compact Architectural Blueprint - Service",
  "Real Estate Office - Compact Architectural Blueprint - Service",
  "Bank Branch - Standard Architectural Blueprint - Service",
  "Insurance Office - Standard Architectural Blueprint - Service",
  "Real Estate Office - Standard Architectural Blueprint - Service",
  "Bank Branch - Grand Architectural Blueprint - Service"
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
var gen={version:'jahdb-blueprint-offices-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('blueprint-offices',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
