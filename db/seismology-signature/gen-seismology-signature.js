(function(){'use strict';
/* JAH The Seismology Signature Database generator — jahdb-seismology-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-SSG-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "What Is Seismology: The Science of Earthquakes (Signature Edition) - Foundations",
  "Plate Tectonics and the Earthquake Belts (Signature Edition) - Foundations",
  "Faults: Where Earthquakes Begin (Signature Edition) - Foundations",
  "Elastic Rebound: How Stress Becomes an Earthquake (Signature Edition) - Foundations",
  "Body Waves: P-Waves and S-Waves (Signature Edition) - Foundations",
  "Surface Waves: Love and Rayleigh Waves (Signature Edition) - Foundations"
 ],
 "Compounded": [
  "Seismometers: Listening to the Earth (Signature Edition) - Compounded",
  "Reading a Seismogram (Signature Edition) - Compounded",
  "Locating an Earthquake by Triangulation (Signature Edition) - Compounded",
  "The Richter Scale and Local Magnitude (Signature Edition) - Compounded",
  "Moment Magnitude: The Modern Standard (Signature Edition) - Compounded",
  "The Modified Mercalli Intensity Scale (Signature Edition) - Compounded",
  "Seismic Networks: From Local Arrays to the Globe (Signature Edition) - Compounded",
  "Focal Mechanisms: Reading the Fault from the Waves (Signature Edition) - Compounded",
  "Aftershocks, Foreshocks, and Earthquake Swarms (Signature Edition) - Compounded",
  "Tsunamis: Earthquakes That Move the Ocean (Signature Edition) - Compounded",
  "Seismic Hazard Maps (Signature Edition) - Compounded",
  "Earthquake Early Warning (Signature Edition) - Compounded"
 ],
 "Advanced": [
  "Seismic Tomography: Imaging the Earth's Interior (Signature Edition) - Advanced",
  "Seismic Reflection: Imaging the Subsurface (Signature Edition) - Advanced",
  "Seismic Refraction and Crustal Structure (Signature Edition) - Advanced",
  "Induced Seismicity: Human-Triggered Earthquakes (Signature Edition) - Advanced",
  "Slow Slip Events and Episodic Tremor (Signature Edition) - Advanced",
  "Source Spectra and the Corner Frequency (Signature Edition) - Advanced",
  "Stress Drop and Rupture Dynamics (Signature Edition) - Advanced",
  "Ground Motion Prediction Equations (Signature Edition) - Advanced",
  "Site Response and Seismic Microzonation (Signature Edition) - Advanced",
  "Paleoseismology: Reading Ancient Earthquakes (Signature Edition) - Advanced",
  "Earthquake Recurrence and Seismic Gaps (Signature Edition) - Advanced",
  "Probabilistic Seismic Hazard Analysis (Signature Edition) - Advanced",
  "Seismic Anisotropy (Signature Edition) - Advanced",
  "Receiver Functions: The Moho in a Waveform (Signature Edition) - Advanced",
  "Seismic Interferometry: Turning Noise into Signal (Signature Edition) - Advanced",
  "Deep Earth Structure: Core, Mantle, and Discontinuities (Signature Edition) - Advanced",
  "Earthquake Forecasting: Probability, Not Prediction (Signature Edition) - Advanced",
  "Seismic Building Codes and Resilient Design (Signature Edition) - Advanced"
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
var gen={version:'jahdb-seismology-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('seismology-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
