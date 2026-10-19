(function(){'use strict';
/* JAH Car Buying Guide Database generator — jahdb-car-buying-guide-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-CARBGS-";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={"Foundations": ["New vs Used (Signature Edition)", "Defining Your Needs (Signature Edition)", "Budgeting Total Cost (Signature Edition)", "Researching Models (Signature Edition)", "Fair Pricing (Signature Edition)", "Vehicle History Reports (Signature Edition)", "Pre-Purchase Inspection (Signature Edition)", "Test Driving (Signature Edition)", "Financing Basics (Signature Edition)", "Negotiating Price (Signature Edition)", "Dealer Tactics (Signature Edition)"], "Compounded": ["Trade-Ins (Signature Edition)", "Warranties (Signature Edition)", "Insurance Shopping (Signature Edition)", "Paperwork (Signature Edition)", "Leasing (Signature Edition)", "Electric Vehicles (Signature Edition)", "Avoiding Lemons (Signature Edition)", "Private Party Sales (Signature Edition)", "Timing Purchases (Signature Edition)", "Teaching Car Buying (Signature Edition)", "The Ownership Review (Signature Edition)", "Certified Pre-Owned (Signature Edition)"], "Advanced": ["Online Car Buying (Signature Edition)", "Carfax vs Alternatives (Signature Edition)", "Negotiating Add-Ons (Signature Edition)", "Gap Insurance (Signature Edition)", "First Car for Teens (Signature Edition)", "Selling Your Car (Signature Edition)", "Total Cost Calculators (Signature Edition)", "Fleet and Rental Sales (Signature Edition)", "Out-of-State Buying (Signature Edition)", "Lemon Law Claims (Signature Edition)", "The Post-Purchase Check (Signature Edition)"]};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "#!/usr/bin/env python3\n\"\"\""+safe+" — buying guide demo.\nRecord demo. Property of Justin Addam Higgins (JAH).\n\"\"\"\n"
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
    name:topic+' — buying guide',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A buying guide of "'+topic+'" in '+field+'. Generated sample record are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"car-buying-guide-signature-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:"jahdb-car-buying-guide-signature-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("car-buying-guide-signature",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
