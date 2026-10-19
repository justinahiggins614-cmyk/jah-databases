(function(){'use strict';
/* JAH The Hyperloop-Style Transport Future Technology Database — Signature Edition generator — jahdb-futuretech-63-hyperloop-style-transport-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-FT63-SIG-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={"Foundations": ["Hyperloop Style Transport — Medhurst Proposes the Tube Train (Signature Edition)", "Hyperloop Style Transport — the Crystal Palace Pneumatic Railway (Signature Edition)", "Hyperloop Style Transport — Beach's Pneumatic Subway (Signature Edition)", "Hyperloop Style Transport — Pneumatic Mail Under New York (Signature Edition)", "Hyperloop Style Transport — the Vactrain Concept (Signature Edition)", "Hyperloop Style Transport — Shanghai Maglev - 431 km/h (Signature Edition)", "Hyperloop Style Transport — Hyperloop Alpha (Signature Edition)", "Hyperloop Style Transport — the Hyperloop Startups (Signature Edition)", "Hyperloop Style Transport — the Pod Competition (Signature Edition)", "Hyperloop Style Transport — Propulsion Proven (Signature Edition)", "Hyperloop Style Transport — 310 km/h in the Tube (Signature Edition)"], "Compounded": ["Hyperloop Style Transport — Toulouse Builds Tubes (Signature Edition)", "Hyperloop Style Transport — the First Hyperloop Passengers (Signature Edition)", "Hyperloop Style Transport — the Cargo Pivot (Signature Edition)", "Hyperloop Style Transport — the Flagship Folds (Signature Edition)", "Hyperloop Style Transport — Hardt Carries the Torch (Signature Edition)", "Hyperloop Style Transport — Longer Test Tracks (Signature Edition)", "Hyperloop Style Transport — Swisspod (Signature Edition)", "Hyperloop Style Transport — Maglev Accelerates (Signature Edition)", "Hyperloop Style Transport — Europe's Tube Lab (Signature Edition)", "Hyperloop Style Transport — Freight Leads the Tube (Signature Edition)", "Hyperloop Style Transport — The First Commercial Line (Signature Edition)", "Hyperloop Style Transport — 1,000 km/h Passenger Service (Signature Edition)"], "Advanced": ["Hyperloop Style Transport — Intercity Hyperloop Networks (Signature Edition)", "Hyperloop Style Transport — Cargo Hyperloop Networks (Signature Edition)", "Hyperloop Style Transport — Global Safety Certification (Signature Edition)", "Hyperloop Style Transport — Commuter Hyperloops (Signature Edition)", "Hyperloop Style Transport — Hyperloop Transit Hubs (Signature Edition)", "Hyperloop Style Transport — Solar-Powered Tubes (Signature Edition)", "Hyperloop Style Transport — Transcontinental Tubes (Signature Edition)", "Hyperloop Style Transport — Undersea Tubes (Signature Edition)", "Hyperloop Style Transport — Tubes vs. Short-Haul Air (Signature Edition)", "Hyperloop Style Transport — Continental Tube Grids (Signature Edition)", "Hyperloop Style Transport — The Everyday Hyperloop - Working Version (Signature Edition)"]};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Hyperloop Style Transport study \u2014 "+safe+"\n"
   + "# Field: "+field+"\n"
   + "record = {'title': \""+safe+"\", 'field': \""+field+"\"}\n"
   + "def summarize(r):\n"
   + "    return r['title'] + ' [' + r['field'] + ']'\n"
   + "print(summarize(record))\n"
   + "print('Sample record \u2014 structural sample, not an archive entry.')\n";
}
function generate(seed,opts,rnd){
  opts=opts||{}; rnd=rnd||prng(seed);
  var field=opts.field&&FIELDS.indexOf(opts.field)>=0?opts.field:pick(FIELDS,rnd);
  var pool=TOPICS[field]||["General Study"];
  var topic=pick(pool,rnd);
  var id=PREFIX+String(seed).padStart(6,'0');
  return {
    id:id,
    name:topic+' — technology study record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A technology study record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"futuretech-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-futuretech-63-hyperloop-style-transport-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('futuretech-63-hyperloop-style-transport-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
