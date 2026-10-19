(function(){'use strict';
/* JAH Small Business Formation Guide Database generator — jahdb-small-business-formation-guide-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-SMALBFGS-";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={"Foundations": ["Choosing a Structure (Signature Edition)", "Sole Proprietorship (Signature Edition)", "LLC Formation (Signature Edition)", "Corporations (Signature Edition)", "Partnerships (Signature Edition)", "Naming Your Business (Signature Edition)", "State Registration (Signature Edition)", "EIN Application (Signature Edition)", "Business Licenses (Signature Edition)", "Zoning and Permits (Signature Edition)", "Business Banking (Signature Edition)"], "Compounded": ["Bookkeeping Basics (Signature Edition)", "Tax Obligations (Signature Edition)", "Hiring First Employees (Signature Edition)", "Contracts for Business (Signature Edition)", "Business Insurance (Signature Edition)", "Intellectual Property (Signature Edition)", "Pricing Your Work (Signature Edition)", "Finding Customers (Signature Edition)", "Cash Flow Management (Signature Edition)", "Business Plans (Signature Edition)", "Financing Options (Signature Edition)", "Home-Based Business (Signature Edition)"], "Advanced": ["Online Business Specifics (Signature Edition)", "Record Keeping (Signature Edition)", "Annual Compliance (Signature Edition)", "Scaling Decisions (Signature Edition)", "Exit Planning (Signature Edition)", "Common Formation Mistakes (Signature Edition)", "Getting Professional Help (Signature Edition)", "The First 90 Days (Signature Edition)", "The First Year Review (Signature Edition)", "Teaching Entrepreneurship (Signature Edition)", "The Annual Business Checkup (Signature Edition)"]};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "#!/usr/bin/env python3\n\"\"\""+safe+" — formation guide demo.\nRecord demo. Property of Justin Addam Higgins (JAH).\n\"\"\"\n"
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
    name:topic+' — formation guide',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A formation guide of "'+topic+'" in '+field+'. Generated sample record are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"small-business-formation-guide-signature-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:"jahdb-small-business-formation-guide-signature-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("small-business-formation-guide-signature",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
