(function(){'use strict';
/* JAH The Climatology Signature Database generator — jahdb-climatology-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-CSG-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "What Climatology Is (Signature Edition) - Foundations",
  "Weather vs Climate (Signature Edition) - Foundations",
  "Earth's Energy Balance (Signature Edition) - Foundations",
  "The Greenhouse Effect (Signature Edition) - Foundations",
  "Albedo and the Climate Energy Budget (Signature Edition) - Foundations",
  "Latitude, Tilt, and the Seasons (Signature Edition) - Foundations",
  "Layers of the Atmosphere (Signature Edition) - Foundations",
  "The Water Cycle (Signature Edition) - Foundations",
  "Pressure Gradients and Wind (Signature Edition) - Foundations",
  "The Coriolis Effect (Signature Edition) - Foundations",
  "The Three-Cell Circulation (Signature Edition) - Foundations",
  "Jet Streams (Signature Edition) - Foundations",
  "Ocean Currents and Heat Transport (Signature Edition) - Foundations",
  "The Koeppen Climate Classification (Signature Edition) - Foundations"
 ],
 "Compounded": [
  "Monsoons (Signature Edition) - Compounded",
  "El Nino and La Nina (ENSO) (Signature Edition) - Compounded",
  "The North Atlantic Oscillation and Teleconnections (Signature Edition) - Compounded",
  "Climate Forcings (Signature Edition) - Compounded",
  "Climate Feedbacks (Signature Edition) - Compounded",
  "Climate Sensitivity (Signature Edition) - Compounded",
  "The Carbon Cycle (Signature Edition) - Compounded",
  "The Ozone Layer (Signature Edition) - Compounded",
  "Urban Heat Islands (Signature Edition) - Compounded",
  "Dendroclimatology: Tree Rings (Signature Edition) - Compounded"
 ],
 "Advanced": [
  "Ice Cores (Signature Edition) - Advanced",
  "General Circulation Models (Signature Edition) - Advanced",
  "Paleoclimate: The Ice Ages (Signature Edition) - Advanced",
  "Milankovitch Cycles (Signature Edition) - Advanced",
  "The Thermohaline Circulation (Signature Edition) - Advanced",
  "Attribution of Climate Change (Signature Edition) - Advanced",
  "Climate Tipping Points (Signature Edition) - Advanced",
  "Sea Level Rise (Signature Edition) - Advanced",
  "Geoengineering (Signature Edition) - Advanced",
  "Frontiers of Climatology (Signature Edition) - Advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Climatology Study — "+safe+"\n"
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
    name:topic+' — climatology record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A climatology record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"climatology-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-climatology-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('climatology-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
