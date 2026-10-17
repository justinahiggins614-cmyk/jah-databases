(function(){'use strict';
/* JAH The Volcanology Database generator — jahdb-volcanology-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-VOL-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "What Volcanology Is - Foundations",
  "How Magma Forms - Foundations",
  "Lava: Magma on the Surface - Foundations",
  "Plate Tectonics and Volcanic Settings - Foundations",
  "The Ring of Fire - Foundations",
  "Shield Volcanoes - Foundations",
  "Stratovolcanoes - Foundations",
  "Cinder Cones - Foundations",
  "Craters and Calderas - Foundations",
  "Magma Chambers and Plumbing Systems - Foundations",
  "Viscosity, Gas, and Eruption Control - Foundations",
  "The Basalt-to-Rhyolite Composition Scale - Foundations"
 ],
 "Compounded": [
  "Eruption Styles: Hawaiian and Strombolian - Compounded",
  "Eruption Styles: Vulcanian and Plinian - Compounded",
  "Pyroclastic Flows and Surges - Compounded",
  "Lahars: Volcanic Mudflows - Compounded",
  "Tephra and Ashfall - Compounded",
  "Volcanic Gases and Climate - Compounded",
  "The Volcanic Explosivity Index (VEI) - Compounded",
  "Lava Flows: Pahoehoe, Aa, and Lava Tubes - Compounded",
  "Seismic Monitoring of Volcanoes - Compounded",
  "Ground Deformation: GPS, Tilt, and InSAR - Compounded",
  "Volcanic Gas Monitoring - Compounded",
  "Eruption Forecasting and Alert Levels - Compounded"
 ],
 "Advanced": [
  "Supervolcanoes and Caldera-Forming Eruptions - Advanced",
  "Magma Chamber Dynamics - Advanced",
  "Crystal Fractionation and Magma Differentiation - Advanced",
  "Volcanic Hazard Maps and Risk Assessment - Advanced",
  "Pyroclastic Density Current Modeling - Advanced",
  "Volcano-Generated Tsunamis - Advanced",
  "Geothermal Energy from Volcanic Systems - Advanced",
  "Magma Mixing and Assimilation - Advanced",
  "Vesuvius 79 AD: The Pompeii Eruption - Advanced",
  "Tambora 1815 and Krakatau 1883 - Advanced",
  "Mount St. Helens 1980 and Pinatubo 1991 - Advanced",
  "Frontiers of Volcanology - Advanced"
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
var gen={version:'jahdb-volcanology-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('volcanology',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
