(function(){'use strict';
/* JAH Intellectual Property Basics Database generator — jahdb-intellectual-property-basics-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-INTEPBS-";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={"Foundations": ["Copyright Basics (Signature Edition)", "What Copyright Covers (Signature Edition)", "Copyright Registration (Signature Edition)", "Fair Use (Signature Edition)", "Trademark Basics (Signature Edition)", "Trademark Registration (Signature Edition)", "Patent Basics (Signature Edition)", "Provisional Patents (Signature Edition)", "Trade Secrets (Signature Edition)", "Work for Hire (Signature Edition)", "Licensing Basics (Signature Edition)"], "Compounded": ["NDAs That Work (Signature Edition)", "Copyright Infringement (Signature Edition)", "DMCA Takedowns (Signature Edition)", "Public Domain (Signature Edition)", "Creative Commons (Signature Edition)", "IP for Small Business (Signature Edition)", "IP for Inventors (Signature Edition)", "IP for Creators (Signature Edition)", "Enforcement Decisions (Signature Edition)", "IP Valuation Basics (Signature Edition)", "International IP (Signature Edition)", "IP Contracts Checklist (Signature Edition)"], "Advanced": ["Open Source Licensing (Signature Edition)", "IP Due Diligence (Signature Edition)", "Teaching IP Basics (Signature Edition)", "The Annual IP Review (Signature Edition)", "IP Insurance (Signature Edition)", "IP in Employment (Signature Edition)", "Domain Names and IP (Signature Edition)", "IP Audits (Signature Edition)", "Trade Dress (Signature Edition)", "IP in Divorce (Signature Edition)", "Right of Publicity (Signature Edition)"]};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "#!/usr/bin/env python3\n\"\"\""+safe+" — IP guide demo.\nRecord demo. Property of Justin Addam Higgins (JAH).\n\"\"\"\n"
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
    name:topic+' — IP guide',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A IP guide of "'+topic+'" in '+field+'. Generated sample record are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"intellectual-property-basics-signature-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:"jahdb-intellectual-property-basics-signature-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("intellectual-property-basics-signature",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
