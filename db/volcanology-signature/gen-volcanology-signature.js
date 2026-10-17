(function(){'use strict';
/* JAH The Volcanology Signature Database generator — jahdb-volcanology-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-VSG-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "What Volcanology Is (Signature Edition) - Foundations",
  "How Magma Forms (Signature Edition) - Foundations",
  "Lava: Magma on the Surface (Signature Edition) - Foundations",
  "Plate Tectonics and Volcanic Settings (Signature Edition) - Foundations",
  "The Ring of Fire (Signature Edition) - Foundations",
  "Shield Volcanoes (Signature Edition) - Foundations",
  "Stratovolcanoes (Signature Edition) - Foundations",
  "Cinder Cones (Signature Edition) - Foundations",
  "Craters and Calderas (Signature Edition) - Foundations",
  "Magma Chambers and Plumbing Systems (Signature Edition) - Foundations",
  "Viscosity, Gas, and Eruption Control (Signature Edition) - Foundations",
  "The Basalt-to-Rhyolite Composition Scale (Signature Edition) - Foundations"
 ],
 "Compounded": [
  "Eruption Styles: Hawaiian and Strombolian (Signature Edition) - Compounded",
  "Eruption Styles: Vulcanian and Plinian (Signature Edition) - Compounded",
  "Pyroclastic Flows and Surges (Signature Edition) - Compounded",
  "Lahars: Volcanic Mudflows (Signature Edition) - Compounded",
  "Tephra and Ashfall (Signature Edition) - Compounded",
  "Volcanic Gases and Climate (Signature Edition) - Compounded",
  "The Volcanic Explosivity Index (VEI) (Signature Edition) - Compounded",
  "Lava Flows: Pahoehoe, Aa, and Lava Tubes (Signature Edition) - Compounded",
  "Seismic Monitoring of Volcanoes (Signature Edition) - Compounded",
  "Ground Deformation: GPS, Tilt, and InSAR (Signature Edition) - Compounded",
  "Volcanic Gas Monitoring (Signature Edition) - Compounded",
  "Eruption Forecasting and Alert Levels (Signature Edition) - Compounded"
 ],
 "Advanced": [
  "Supervolcanoes and Caldera-Forming Eruptions (Signature Edition) - Advanced",
  "Magma Chamber Dynamics (Signature Edition) - Advanced",
  "Crystal Fractionation and Magma Differentiation (Signature Edition) - Advanced",
  "Volcanic Hazard Maps and Risk Assessment (Signature Edition) - Advanced",
  "Pyroclastic Density Current Modeling (Signature Edition) - Advanced",
  "Volcano-Generated Tsunamis (Signature Edition) - Advanced",
  "Geothermal Energy from Volcanic Systems (Signature Edition) - Advanced",
  "Magma Mixing and Assimilation (Signature Edition) - Advanced",
  "Vesuvius 79 AD: The Pompeii Eruption (Signature Edition) - Advanced",
  "Tambora 1815 and Krakatau 1883 (Signature Edition) - Advanced",
  "Mount St. Helens 1980 and Pinatubo 1991 (Signature Edition) - Advanced",
  "Frontiers of Volcanology (Signature Edition) - Advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Volcanology Study — "+safe+"\n"
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
    name:topic+' — volcanology record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A volcanology record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"volcanology-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-volcanology-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('volcanology-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
