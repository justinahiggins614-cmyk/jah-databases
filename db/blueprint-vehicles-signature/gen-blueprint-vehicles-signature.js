(function(){'use strict';
/* JAH The Vehicle Blueprint Signature Database generator — jahdb-blueprint-vehicles-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-BVPS-";
var FIELDS=["Air","Road","Water","Work"];
var TOPICS={
 "Air": [
  "Signature Small Aircraft - Compact Architectural Blueprint (Signature Edition) - Air",
  "Signature Small Aircraft - Standard Architectural Blueprint (Signature Edition) - Air",
  "Signature Small Aircraft - Grand Architectural Blueprint (Signature Edition) - Air"
 ],
 "Road": [
  "Signature Sedan - Compact Architectural Blueprint (Signature Edition) - Road",
  "Signature Pickup Truck - Compact Architectural Blueprint (Signature Edition) - Road",
  "Signature City Bus - Compact Architectural Blueprint (Signature Edition) - Road",
  "Signature Motorcycle - Compact Architectural Blueprint (Signature Edition) - Road",
  "Signature Bicycle - Compact Architectural Blueprint (Signature Edition) - Road",
  "Signature Sedan - Standard Architectural Blueprint (Signature Edition) - Road",
  "Signature Pickup Truck - Standard Architectural Blueprint (Signature Edition) - Road",
  "Signature City Bus - Standard Architectural Blueprint (Signature Edition) - Road",
  "Signature Motorcycle - Standard Architectural Blueprint (Signature Edition) - Road",
  "Signature Bicycle - Standard Architectural Blueprint (Signature Edition) - Road",
  "Signature Sedan - Grand Architectural Blueprint (Signature Edition) - Road",
  "Signature Pickup Truck - Grand Architectural Blueprint (Signature Edition) - Road",
  "Signature City Bus - Grand Architectural Blueprint (Signature Edition) - Road",
  "Signature Motorcycle - Grand Architectural Blueprint (Signature Edition) - Road",
  "Signature Bicycle - Grand Architectural Blueprint (Signature Edition) - Road"
 ],
 "Water": [
  "Signature Sailboat - Compact Architectural Blueprint (Signature Edition) - Water",
  "Signature Motorboat - Compact Architectural Blueprint (Signature Edition) - Water",
  "Signature Sailboat - Standard Architectural Blueprint (Signature Edition) - Water",
  "Signature Motorboat - Standard Architectural Blueprint (Signature Edition) - Water",
  "Signature Sailboat - Grand Architectural Blueprint (Signature Edition) - Water",
  "Signature Motorboat - Grand Architectural Blueprint (Signature Edition) - Water"
 ],
 "Work": [
  "Signature Box Truck - Compact Architectural Blueprint (Signature Edition) - Work",
  "Signature Tractor-Trailer - Compact Architectural Blueprint (Signature Edition) - Work",
  "Signature RV Camper - Compact Architectural Blueprint (Signature Edition) - Work",
  "Signature Fire Truck - Compact Architectural Blueprint (Signature Edition) - Work",
  "Signature Box Truck - Standard Architectural Blueprint (Signature Edition) - Work",
  "Signature Tractor-Trailer - Standard Architectural Blueprint (Signature Edition) - Work",
  "Signature RV Camper - Standard Architectural Blueprint (Signature Edition) - Work",
  "Signature Fire Truck - Standard Architectural Blueprint (Signature Edition) - Work",
  "Signature Box Truck - Grand Architectural Blueprint (Signature Edition) - Work",
  "Signature Tractor-Trailer - Grand Architectural Blueprint (Signature Edition) - Work"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Vehicles Blueprint Study — "+safe+"\n"
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
    name:topic+' — vehicle blueprint record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A vehicle blueprint record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
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
var gen={version:'jahdb-blueprint-vehicles-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('blueprint-vehicles-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
