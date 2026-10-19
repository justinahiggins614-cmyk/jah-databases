(function(){'use strict';
/* JAH The Vehicle Blueprint Database generator — jahdb-blueprint-vehicles-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-BVP-";
var FIELDS=["Air","Road","Water","Work"];
var TOPICS={
 "Air": [
  "Small Aircraft - Compact Architectural Blueprint - Air",
  "Small Aircraft - Standard Architectural Blueprint - Air",
  "Small Aircraft - Grand Architectural Blueprint - Air"
 ],
 "Road": [
  "Sedan - Compact Architectural Blueprint - Road",
  "Pickup Truck - Compact Architectural Blueprint - Road",
  "City Bus - Compact Architectural Blueprint - Road",
  "Motorcycle - Compact Architectural Blueprint - Road",
  "Bicycle - Compact Architectural Blueprint - Road",
  "Sedan - Standard Architectural Blueprint - Road",
  "Pickup Truck - Standard Architectural Blueprint - Road",
  "City Bus - Standard Architectural Blueprint - Road",
  "Motorcycle - Standard Architectural Blueprint - Road",
  "Bicycle - Standard Architectural Blueprint - Road",
  "Sedan - Grand Architectural Blueprint - Road",
  "Pickup Truck - Grand Architectural Blueprint - Road",
  "City Bus - Grand Architectural Blueprint - Road",
  "Motorcycle - Grand Architectural Blueprint - Road",
  "Bicycle - Grand Architectural Blueprint - Road"
 ],
 "Water": [
  "Sailboat - Compact Architectural Blueprint - Water",
  "Motorboat - Compact Architectural Blueprint - Water",
  "Sailboat - Standard Architectural Blueprint - Water",
  "Motorboat - Standard Architectural Blueprint - Water",
  "Sailboat - Grand Architectural Blueprint - Water",
  "Motorboat - Grand Architectural Blueprint - Water"
 ],
 "Work": [
  "Box Truck - Compact Architectural Blueprint - Work",
  "Tractor-Trailer - Compact Architectural Blueprint - Work",
  "RV Camper - Compact Architectural Blueprint - Work",
  "Fire Truck - Compact Architectural Blueprint - Work",
  "Box Truck - Standard Architectural Blueprint - Work",
  "Tractor-Trailer - Standard Architectural Blueprint - Work",
  "RV Camper - Standard Architectural Blueprint - Work",
  "Fire Truck - Standard Architectural Blueprint - Work",
  "Box Truck - Grand Architectural Blueprint - Work",
  "Tractor-Trailer - Grand Architectural Blueprint - Work"
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
var gen={version:'jahdb-blueprint-vehicles-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('blueprint-vehicles',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
