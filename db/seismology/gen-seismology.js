(function(){'use strict';
/* JAH The Seismology Database generator — jahdb-seismology-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-SEI-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "What Is Seismology: The Science of Earthquakes - Foundations",
  "Plate Tectonics and the Earthquake Belts - Foundations",
  "Faults: Where Earthquakes Begin - Foundations",
  "Elastic Rebound: How Stress Becomes an Earthquake - Foundations",
  "Body Waves: P-Waves and S-Waves - Foundations",
  "Surface Waves: Love and Rayleigh Waves - Foundations"
 ],
 "Compounded": [
  "Seismometers: Listening to the Earth - Compounded",
  "Reading a Seismogram - Compounded",
  "Locating an Earthquake by Triangulation - Compounded",
  "The Richter Scale and Local Magnitude - Compounded",
  "Moment Magnitude: The Modern Standard - Compounded",
  "The Modified Mercalli Intensity Scale - Compounded",
  "Seismic Networks: From Local Arrays to the Globe - Compounded",
  "Focal Mechanisms: Reading the Fault from the Waves - Compounded",
  "Aftershocks, Foreshocks, and Earthquake Swarms - Compounded",
  "Tsunamis: Earthquakes That Move the Ocean - Compounded",
  "Seismic Hazard Maps - Compounded",
  "Earthquake Early Warning - Compounded"
 ],
 "Advanced": [
  "Seismic Tomography: Imaging the Earth's Interior - Advanced",
  "Seismic Reflection: Imaging the Subsurface - Advanced",
  "Seismic Refraction and Crustal Structure - Advanced",
  "Induced Seismicity: Human-Triggered Earthquakes - Advanced",
  "Slow Slip Events and Episodic Tremor - Advanced",
  "Source Spectra and the Corner Frequency - Advanced",
  "Stress Drop and Rupture Dynamics - Advanced",
  "Ground Motion Prediction Equations - Advanced",
  "Site Response and Seismic Microzonation - Advanced",
  "Paleoseismology: Reading Ancient Earthquakes - Advanced",
  "Earthquake Recurrence and Seismic Gaps - Advanced",
  "Probabilistic Seismic Hazard Analysis - Advanced",
  "Seismic Anisotropy - Advanced",
  "Receiver Functions: The Moho in a Waveform - Advanced",
  "Seismic Interferometry: Turning Noise into Signal - Advanced",
  "Deep Earth Structure: Core, Mantle, and Discontinuities - Advanced",
  "Earthquake Forecasting: Probability, Not Prediction - Advanced",
  "Seismic Building Codes and Resilient Design - Advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Seismology Study — "+safe+"\n"
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
    name:topic+' — seismology record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A seismology record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"seismology-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-seismology-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('seismology',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
