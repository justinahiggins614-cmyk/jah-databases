(function(){'use strict';
/* JAH International Legal Resource Directory Database generator — jahdb-international-legal-resource-directory-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-INTELRDS-";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={"Foundations": ["Jurisdiction Basics (Signature Edition)", "Finding Foreign Counsel (Signature Edition)", "Embassy Resources (Signature Edition)", "Document Authentication (Signature Edition)", "Translation Requirements (Signature Edition)", "International Family Law (Signature Edition)", "International Business Law (Signature Edition)", "Immigration Intersections (Signature Edition)", "Travel Legal Preparation (Signature Edition)", "Arrest Abroad (Signature Edition)", "International Contracts (Signature Edition)"], "Compounded": ["Treaty Basics (Signature Edition)", "Human Rights Resources (Signature Edition)", "Asylum Basics (Signature Edition)", "Extradition Concepts (Signature Edition)", "International Estate Issues (Signature Edition)", "Working Abroad Legally (Signature Edition)", "Study Abroad Legalities (Signature Edition)", "Marriage Abroad (Signature Edition)", "Driving and Liability Abroad (Signature Edition)", "Consumer Protection Abroad (Signature Edition)", "Property Abroad (Signature Edition)", "Tax Intersections (Signature Edition)"], "Advanced": ["Emergency Planning (Signature Edition)", "Teaching Cross-Border Literacy (Signature Edition)", "The Annual International Review (Signature Edition)", "International Adoption (Signature Edition)", "Refugee Legal Aid (Signature Edition)", "International Child Support (Signature Edition)", "Foreign Investment Rules (Signature Edition)", "International Wills (Signature Edition)", "Consular Services Detail (Signature Edition)", "International Mediation (Signature Edition)", "Staying Current (Signature Edition)"]};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "#!/usr/bin/env python3\n\"\"\""+safe+" — legal directory demo.\nRecord demo. Property of Justin Addam Higgins (JAH).\n\"\"\"\n"
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
    name:topic+' — legal directory',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A legal directory of "'+topic+'" in '+field+'. Generated sample record are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"international-legal-resource-directory-signature-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:"jahdb-international-legal-resource-directory-signature-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("international-legal-resource-directory-signature",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
